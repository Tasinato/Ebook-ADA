# Ada Lovelace — A Primeira Programadora da História

### Quando o algoritmo era mecânico

Ebook educativo de **Rafael Tasinato** sobre Ada Lovelace, Charles Babbage e as origens da programação. Um projeto de produção de conteúdo e divulgação da história da computação, com texto em português e apoio de inteligência artificial na revisão e nas ilustrações.

[**Ler o PDF**](assets/dist/EBOOK%20LOVELACE.pdf) · [**Baixar o EPUB**](https://github.com/Tasinato/Ebook-ADA/raw/refs/heads/main/assets/ebook.epub) · [**Ler os capítulos**](#leitura-por-capítulos) · [**Referências**](src/07-referencias.md)

<img src="assets/capa/ChatGPT%20Image%209%20de%20jan.%20de%202026%2C%2013_09_01.png" alt="Ilustração digital da capa do ebook sobre Ada Lovelace" width="300">

*A capa é uma ilustração produzida com apoio de IA, não um registro histórico.*

## Sobre o projeto

O material apresenta o contexto científico do século XIX, a colaboração entre Ada Lovelace e Charles Babbage, as Notas de 1843 e os conceitos de instruções, dados e execução de procedimentos.

É destinado a estudantes de Computação, Engenharia e Matemática, professores e leitores interessados em história da tecnologia. No portfólio, demonstra organização de conteúdo educativo, escrita, edição e uso declarado de ferramentas de IA.

**Situação:** PDF e EPUB atualizados com a bibliografia revisada e a data de acesso de 22 de maio de 2024, confirmada pelo autor. A referência do Gamma permanece provisória, com identificação pendente. O PDF preserva os capítulos e as ilustrações da edição existente; o EPUB foi reconstruído a partir do texto em Markdown, com capa e sumário navegável. Consulte as [pendências bibliográficas](src/07-referencias.md#pendências-de-identificação-e-edição).

## Como ler

| Formato | Acesso | Uso |
| --- | --- | --- |
| PDF | [Abrir no GitHub](assets/dist/EBOOK%20LOVELACE.pdf) | Leitura com a diagramação disponível no repositório. |
| EPUB | [Baixar arquivo](https://github.com/Tasinato/Ebook-ADA/raw/refs/heads/main/assets/ebook.epub) | Texto adaptável, capa e sumário navegável; sem as ilustrações internas do PDF. |
| Markdown | [Pasta src](src/) | Ler e propor revisões dos capítulos pelo GitHub. |

O procedimento de atualização está documentado em [Geração e validação dos formatos](docs/formatos-de-leitura.md). O script atualiza a bibliografia do PDF e reconstrói o EPUB; alterações nos capítulos Markdown não reconstroem o corpo do PDF.

## Leitura por capítulos

Os títulos abaixo correspondem aos arquivos existentes:

1. [Apresentação](src/00-introdução.md)
2. [Capítulo 1 — O mundo antes dos computadores](src/01-capitulo.md)
3. [Capítulo 2 — Formação intelectual de Ada Lovelace](src/02-capitulo.md)
4. [Capítulo 3 — O encontro com Charles Babbage](src/03-capitulo.md)
5. [Capítulo 4 — As Notas de Ada Lovelace](src/04-capitulo.md)
6. [Capítulo 5 — Limites e legado de Ada Lovelace](src/05-capitulo.md)
7. [Conclusão](src/06-conclusão.md)
8. [Referências bibliográficas](src/07-referencias.md)

## Organização do repositório

```text
src/                 Capítulos e referências em Markdown
assets/capa/         Ilustração da capa
assets/imagens/      Imagens do projeto
assets/ fontes/      Pasta de fontes existente, com espaço inicial no nome
assets/dist/         PDF disponível
assets/ebook.epub    EPUB disponível
scripts/             Atualização da bibliografia do PDF e geração do EPUB
docs/                Procedimento de geração e resultados de validação
README.md            Apresentação e acesso ao material
```

O script `scripts/build_reading_formats.py` atualiza a página de referências do PDF existente e gera o EPUB a partir dos capítulos. Requisitos e limites estão descritos na [documentação dos formatos](docs/formatos-de-leitura.md).

## Validação dos arquivos

- **PDF:** 22 páginas; somente a bibliografia foi substituída, com preservação das outras páginas e conferência visual.
- **EPUB:** validado com EPUBCheck 5.4.0, sem erros ou advertências; links internos e texto dos capítulos conferidos.
- **Limite da revisão:** a validação dos arquivos não substitui a revisão histórica integral. A referência do Gamma continua provisória.

## Revisão editorial e próximos passos

- Conferir referências com links específicos, autoria, título e datas comprováveis.
- Identificar o documento específico do Gamma, mantido provisoriamente a pedido do autor. PDF e EPUB já utilizam a data de acesso confirmada de 22 de maio de 2024. A publicação da Ness Labs foi corrigida para 8 de março de 2022.
- Verificar afirmações históricas e citações diretamente nas fontes, distinguindo evidência de interpretação.
- Conferir a equivalência editorial dos capítulos entre Markdown e PDF antes de uma revisão integral; o EPUB utiliza o texto do Markdown.
- Manter o procedimento de geração e os resultados de validação documentados em docs/formatos-de-leitura.md.
- Conferir créditos e origem de cada imagem, distinguindo ilustração de documento histórico.

O título utiliza o reconhecimento histórico de Ada como primeira programadora. O contexto e as nuances dessa atribuição devem ser tratados no texto e sustentados pelas referências, sem equivaler sua atuação à engenharia de software contemporânea.

## Autoria e uso de IA

Créditos registrados no projeto:

- **Texto e organização:** Rafael Tasinato.
- **Revisão:** Rafael Tasinato, com apoio do ChatGPT.
- **Capa e ilustrações:** Rafael Tasinato, com apoio do DALL·E.

O apoio de IA não substitui a verificação de fatos, citações e referências. A curadoria e a responsabilidade pelo conteúdo são do autor.

## Como contribuir

Abra uma Issue ou um Pull Request com uma proposta específica. Para correções históricas, indique a fonte e a passagem que sustenta a alteração. Revise preferencialmente os arquivos em src/ e identifique se PDF e EPUB também precisarão ser atualizados.

## Licença e atribuição

Conforme a declaração já existente neste projeto, o ebook está sob [Creative Commons Attribution 4.0 International — CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Ao reutilizar o material, informe autor, título, fonte e licença, e indique eventuais alterações. Preserve também os créditos de materiais de terceiros, quando aplicáveis.

> Tasinato, Rafael. *Ada Lovelace — A Primeira Programadora da História: Quando o algoritmo era mecânico*. Repositório Ebook-ADA. CC BY 4.0.

[Perfil do autor no GitHub](https://github.com/Tasinato)
