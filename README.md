Opção B — LaTeX → PDF

Pré-requisitos:

TeX Live/MiKTeX

Exemplo:

latexmk -pdf -output-directory=dist src/main.tex

Opção C — Word/Google Docs

Conteúdo em .docx ou exportação manual para PDF

[EDITAR] Documente aqui o procedimento exato (modelos, estilos, etc.).

Organização do repositório

Sugestão de estrutura (ajuste conforme seu projeto):

.
├─ src/
│  ├─ capitulo-01.md
│  ├─ capitulo-02.md
│  ├─ capitulo-03.md
│  ├─ capitulo-04.md
│  ├─ capitulo-05.md
│  ├─ conclusao.md
│  └─ referencias.md
├─ assets/
│  ├─ capa/
│  ├─ imagens/
│  └─ fontes/
├─ dist/
│  ├─ ebook.pdf
│  └─ ebook.epub
└─ README.md

Como contribuir

Contribuições são bem-vindas, especialmente:

revisão técnica e histórica;

melhorias de clareza e coesão;

padronização de referências;

ajustes editoriais (ABNT, Chicago, etc.), conforme a diretriz do projeto.

Fluxo sugerido:

Abra uma Issue descrevendo o problema/ajuste.

Faça um fork do repositório.

Crie um branch: feat/ajuste-x ou fix/revisao-y.

Envie um Pull Request com descrição objetiva e, se possível, referências.

Licença

[EDITAR] Defina a licença do conteúdo.

Sugestões comuns:

CC BY 4.0 (permite uso com atribuição)

CC BY-NC 4.0 (uso não comercial com atribuição)

Créditos

Texto: [Rafael Tasinato]

Revisão: [Rafael Tasinato - chatgpt]

Capa/ilustração: [Rafael Tasinato- DALL-E]

Projeto: Ebook Ada Lovelace

Se você usar este material em aula, artigo ou repositório derivado, recomenda-se citar o título do ebook e este repositório como fonte.


Se você me disser **em qual formato o ebook está (Markdown, LaTeX ou Word)** e como está a **estrutura de pastas atual**, eu adapto o README para refletir exatamente o seu repositório (com comandos corretos, nomes reais e seção de referências no padrão que você escolher).
