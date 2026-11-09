# Geração e validação dos formatos

## Escopo desta atualização

- **PDF:** substituição apenas da página 21 (referências), preservando as outras 21 páginas, incluindo capa, capítulos, ilustrações e apresentação do autor. A numeração total permanece em 22 páginas.
- **EPUB 3:** reconstrução a partir dos oito arquivos Markdown de `src/`, com capa, sumário navegável e créditos. Texto adaptável à tela do leitor. As ilustrações internas e a diagramação do PDF não foram transferidas.
- **Bibliografia:** as mesmas nove entradas nos dois formatos, com as correções de links, data da Ness Labs, DOI de Fuegi e Francis e páginas 11–31 de Misa. Datas de acesso mantidas em 22 maio 2024 por confirmação do autor. A entrada de Fuegi e Francis, que não possuía data de acesso informada, continua sem uma data inventada.
- **Gamma:** mantido provisoriamente; o endereço genérico não comprova qual material foi consultado. A nota editorial acompanha as referências em ambos os formatos. Não foi criado um identificador bibliográfico para esse material.

## Como gerar

Requisitos: Python 3.10 ou superior, `reportlab` e `pypdf`.

```sh
python -m pip install reportlab pypdf
python scripts/build_reading_formats.py
```

O script resolve os caminhos a partir da própria localização. Ele atualiza `assets/dist/EBOOK LOVELACE.pdf` e `assets/ebook.epub`. No Windows, utiliza Times New Roman instalada no sistema; nos demais ambientes, utiliza Times da biblioteca ReportLab. Interrompe se o PDF não tiver 22 páginas, se a bibliografia não estiver na página esperada ou se a nova página ultrapassar o espaço disponível.

**Importante:** esse procedimento não reconstrói o corpo do PDF a partir do Markdown. Para alterar os capítulos do PDF, é necessária uma revisão específica da diagramação. O EPUB contém o texto dos capítulos Markdown; isso não significa equivalência integral com o corpo do PDF.

O identificador UUID do pacote EPUB é técnico e interno, derivado do endereço do repositório; não representa ISBN ou DOI. O campo de modificação registra a geração do arquivo, não uma data histórica de publicação.

## Verificações realizadas nesta revisão

- PDF reaberto com 22 páginas; conteúdo das páginas não alteradas comparado com a edição anterior.
- Página de referências renderizada com Poppler e conferida visualmente: margens, legibilidade, nota editorial e numeração.
- EPUB: arquivo ZIP íntegro, `mimetype` correto e sem compressão na primeira entrada; XML e XHTML analisados sem erros.
- EPUBCheck 5.4.0: **nenhum erro ou advertência**.
- Sumário, apresentação e referências do EPUB renderizados em navegador e conferidos visualmente. A aparência final depende do aplicativo de leitura.

Para repetir a validação EPUB, obtenha o [EPUBCheck oficial](https://github.com/w3c/epubcheck/releases) e execute:

```sh
java -jar caminho/epubcheck.jar assets/ebook.epub
```

A validação estrutural dos formatos não substitui a revisão histórica do conteúdo nem resolve a identificação pendente do Gamma.
