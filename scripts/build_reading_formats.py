"""Update the PDF bibliography and build an EPUB 3 from the Markdown sources.

Requires Python 3.10+, reportlab and pypdf. Run from any directory.
The PDF's other pages are preserved; the EPUB uses Markdown text and the cover.
"""
from pathlib import Path
from datetime import datetime, timezone
from html import escape
import io
import re
import uuid
import zipfile
import xml.etree.ElementTree as ET

from pypdf import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'assets/dist/EBOOK LOVELACE.pdf'
EPUB = ROOT / 'assets/ebook.epub'
TITLE = 'Ada Lovelace — A Primeira Programadora da História'


def inline(text, pdf=False):
    """Render the inline Markdown subset used by this book, escaping all text."""
    text = escape(text)
    text = re.sub(r'&lt;(https?://[^<>]+?)&gt;',
                  lambda m: '<a href="' + m[1] + '">' + m[1] + '</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>' if pdf else r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>' if pdf else r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'\1' if pdf else r'<code>\1</code>', text)
    return text


def bibliography():
    source = (ROOT / 'src/07-referencias.md').read_text(encoding='utf-8')
    return [p.strip() for p in source.split('## Pendências')[0].split('\n\n')
            if p.strip() and not p.startswith('#')]


def update_pdf():
    reader = PdfReader(PDF)
    assert len(reader.pages) == 22, 'Review page locations before changing a different edition.'
    assert 'CHM' in reader.pages[20].extract_text(), 'Bibliography must be page 21.'
    fontdir = Path('C:/Windows/Fonts')
    if (fontdir / 'times.ttf').exists():
        for name, file in [('Book', 'times.ttf'), ('Book-Bold', 'timesbd.ttf'),
                           ('Book-Italic', 'timesi.ttf'), ('Book-BoldItalic', 'timesbi.ttf')]:
            pdfmetrics.registerFont(TTFont(name, str(fontdir / file)))
        pdfmetrics.registerFontFamily('Book', normal='Book', bold='Book-Bold',
                                      italic='Book-Italic', boldItalic='Book-BoldItalic')
        font = 'Book'
    else:
        font = 'Times-Roman'
    width, height = map(float, reader.pages[20].mediabox[2:])
    buffer = io.BytesIO()
    style = ParagraphStyle('Reference', fontName=font, fontSize=10.5, leading=13,
                           spaceAfter=7, splitLongWords=True, uriWasteReduce=0)
    heading = ParagraphStyle('Heading', fontName='Helvetica', fontSize=19,
                             leading=24, textColor='#0d4e6a', spaceAfter=10)
    note = ParagraphStyle('Note', parent=style, fontSize=9, leading=11,
                          textColor='#444444', spaceBefore=4)
    flow = [Paragraph('Referências Bibliográficas', heading)]
    flow += [Paragraph(inline(p, pdf=True), style) for p in bibliography()]
    flow += [Spacer(1, 3), Paragraph(
        'Nota editorial: a referência do Gamma foi mantida provisoriamente pelo autor; '
        'documento, autoria e data ainda não foram identificados. '
        '[s. d.] indica data de publicação não identificada. '
        'Datas de acesso mantidas conforme informação do autor.', note)]

    def footer(canvas, doc):
        canvas.setFont('Helvetica', 10)
        canvas.setFillColorRGB(0.05, 0.3, 0.42)
        canvas.drawCentredString(width / 2, 29, '21')

    SimpleDocTemplate(buffer, pagesize=(width, height), leftMargin=84, rightMargin=72,
                      topMargin=69, bottomMargin=62).build(flow, onFirstPage=footer,
                                                         onLaterPages=footer)
    replacement = PdfReader(buffer)
    assert len(replacement.pages) == 1, 'Bibliography must fit on one page to preserve numbering.'
    writer = PdfWriter()
    for index, page in enumerate(reader.pages):
        writer.add_page(replacement.pages[0] if index == 20 else page)
    if reader.metadata:
        writer.add_metadata({k: str(v) for k, v in reader.metadata.items() if isinstance(v, str)})
    writer.add_metadata({'/Title': TITLE, '/Author': 'Rafael Tasinato'})
    result = io.BytesIO()
    writer.write(result)
    check = PdfReader(io.BytesIO(result.getvalue()))
    assert len(check.pages) == 22
    for i in range(22):
        if i != 20:
            assert check.pages[i].get_contents().get_data() == reader.pages[i].get_contents().get_data()
    PDF.write_bytes(result.getvalue())


def markdown_body(source):
    """Convert paragraphs/headings/lists, the complete block subset in src/."""
    result = []
    for block in re.split(r'\n\s*\n', source.strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith('#'):
            first = block.splitlines()[0]
            level = min(len(first) - len(first.lstrip('#')), 6)
            result.append(f'<h{level}>' + inline(first.lstrip('#').strip()) + f'</h{level}>')
        elif block.startswith('- '):
            result.append('<ul>' + ''.join('<li>' + inline(line[2:]) + '</li>'
                                          for line in block.splitlines()) + '</ul>')
        else:
            result.append('<p>' + inline(' '.join(block.splitlines())) + '</p>')
    return '\n'.join(result)


def xhtml(title, body):
    result = ('<?xml version="1.0" encoding="utf-8"?>\n'
              '<html xmlns="http://www.w3.org/1999/xhtml" '
              'xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR" lang="pt-BR">'
              '<head><title>' + escape(title) + '</title>'
              '<link rel="stylesheet" type="text/css" href="style.css" /></head>'
              '<body>' + body + '</body></html>')
    ET.fromstring(result)
    return result


def build_epub():
    chapters = []
    for i, path in enumerate(sorted((ROOT / 'src').glob('*.md'))):
        source = path.read_text(encoding='utf-8')
        if i == 7:
            source = source.split('## Pendências')[0] + (
                '\n## Nota editorial\n\nA referência do Gamma foi mantida provisoriamente '
                'pelo autor; documento, autoria e data ainda não foram identificados. '
                '[s. d.] indica data de publicação não identificada. As datas de acesso '
                'foram mantidas conforme informação do autor.\n')
        title = source.splitlines()[0].lstrip('#').strip()
        chapters.append((f'chapter-{i:02}.xhtml', title, markdown_body(source)))
    chapters.append(('credits.xhtml', 'Créditos e edição digital',
        '<h1>Créditos e edição digital</h1><p>Texto e organização: Rafael Tasinato. '
        'Revisão: Rafael Tasinato, com apoio do ChatGPT. Capa: Rafael Tasinato, '
        'com apoio do DALL·E. A capa é uma ilustração digital, não um registro histórico.</p>'
        '<p>Esta edição EPUB foi reconstruída a partir dos capítulos Markdown do '
        'repositório Ebook-ADA. As ilustrações internas e a diagramação do PDF '
        'não fazem parte desta edição de texto adaptável.</p>'
        '<p>Licença: <a href="https://creativecommons.org/licenses/by/4.0/">'
        'Creative Commons Attribution 4.0 International (CC BY 4.0)</a>. '
        'Preserve os créditos de materiais de terceiros.</p>'
        '<p>Fonte: <a href="https://github.com/Tasinato/Ebook-ADA">Ebook-ADA</a>.</p>'))
    nav = '<h1>Sumário</h1><nav epub:type="toc" id="toc"><ol>'
    nav += '<li><a href="cover.xhtml">Capa</a></li>'
    nav += ''.join('<li><a href="' + name + '">' + escape(title) + '</a></li>'
                   for name, title, body in chapters)
    nav += '</ol></nav>'
    manifest = ('<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
                '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>'
                '<item id="cover-image" href="cover.png" media-type="image/png" properties="cover-image"/>'
                '<item id="style" href="style.css" media-type="text/css"/>')
    manifest += ''.join(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>'
                        for i, (name, _, _) in enumerate(chapters))
    spine = '<itemref idref="cover"/><itemref idref="nav"/>'
    spine += ''.join(f'<itemref idref="c{i}"/>' for i in range(len(chapters)))
    modified = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    # A stable internal package identifier, not a bibliographic/publication identifier.
    identifier = uuid.uuid5(uuid.NAMESPACE_URL, 'https://github.com/Tasinato/Ebook-ADA')
    opf = ('<?xml version="1.0" encoding="utf-8"?>'
           '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           f'<dc:identifier id="book-id">urn:uuid:{identifier}</dc:identifier>'
           '<dc:title>' + escape(TITLE) + '</dc:title><dc:language>pt-BR</dc:language>'
           '<dc:creator>Rafael Tasinato</dc:creator>'
           '<dc:rights>Creative Commons Attribution 4.0 International</dc:rights>'
           f'<meta property="dcterms:modified">{modified}</meta></metadata>'
           '<manifest>' + manifest + '</manifest><spine>' + spine + '</spine></package>')
    ET.fromstring(opf)
    cover = next((ROOT / 'assets/capa').glob('*.png'))
    with zipfile.ZipFile(EPUB, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', '<?xml version="1.0"?>'
                   '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>')
        z.writestr('OEBPS/content.opf', opf)
        z.writestr('OEBPS/nav.xhtml', xhtml('Sumário', nav))
        z.writestr('OEBPS/cover.xhtml', xhtml('Capa', '<section epub:type="cover">'
                   '<img src="cover.png" alt="Capa ilustrada de Ada Lovelace" /></section>'))
        z.write(cover, 'OEBPS/cover.png')
        z.writestr('OEBPS/style.css', 'body{font-family:serif;line-height:1.5;margin:5%;}'
                   'h1,h2{color:#0d4e6a;line-height:1.2;}h1{font-size:1.7em;}h2{font-size:1.3em;}'
                   'p{margin:0 0 1em;}a{overflow-wrap:anywhere;}img{max-width:100%;height:auto;}'
                   'li{margin-bottom:.6em;}nav ol{padding-left:1.5em;}')
        for name, title, body in chapters:
            z.writestr('OEBPS/' + name, xhtml(title, body))
    with zipfile.ZipFile(EPUB) as z:
        assert z.testzip() is None
        assert z.infolist()[0].filename == 'mimetype'
        assert z.infolist()[0].compress_type == zipfile.ZIP_STORED
        for name in z.namelist():
            if name.endswith(('.xhtml', '.xml', '.opf')):
                ET.fromstring(z.read(name))


if __name__ == '__main__':
    update_pdf()
    build_epub()
    print('PDF: 22 pages; only bibliography replaced. EPUB: 8 source chapters, cover, navigation and credits.')
