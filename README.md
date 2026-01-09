# Ada Lovelace — A Primeira Programadora da História  
## Quando o algoritmo era mecânico

Ebook de divulgação acadêmica sobre o legado intelectual de Ada Lovelace, com foco em precisão histórica, clareza conceitual e contextualização do século XIX. O texto evita anacronismos e romantizações, discutindo a contribuição de Ada como **formulação conceitual da programação** (instruções, dados e execução formal), no contexto da Máquina Analítica de Charles Babbage.

---

## Sumário
- [Visão geral](#visão-geral)
- [Objetivo](#objetivo)
- [Público-alvo](#público-alvo)
- [Estrutura do ebook](#estrutura-do-ebook)
- [Critérios metodológicos](#critérios-metodológicos)
- [Como compilar/gerar o ebook](#como-compilargerar-o-ebook)
- [Organização do repositório](#organização-do-repositório)
- [Como contribuir](#como-contribuir)
- [Licença](#licença)
- [Créditos](#créditos)

---

## Visão geral
Este repositório contém o conteúdo e os materiais editoriais do ebook **Ada Lovelace — A Primeira Programadora da História: Quando o algoritmo era mecânico**.

A obra apresenta:
- o contexto científico e tecnológico do início do século XIX;
- o encontro intelectual entre Ada Lovelace e Charles Babbage;
- a Máquina Analítica e sua arquitetura conceitual;
- as Notas A–G (1843) e a formalização de procedimentos algorítmicos;
- os limites explicitamente reconhecidos por Ada (máquina como executora de instruções);
- o legado teórico para a compreensão moderna de programação e computação.

---

## Objetivo
Produzir um texto **sintético, coeso e historicamente fundamentado** que:
- explique a contribuição real de Ada Lovelace para a história da computação;
- esclareça por que ela é reconhecida como a primeira programadora (no sentido histórico e conceitual);
- apresente a computação como disciplina científica baseada em **representação simbólica**, **abstração** e **processos formais**.

---

## Público-alvo
- Estudantes de **Computação**, **Engenharia** e **Matemática**
- Professores e produção de material didático
- Leitores interessados em **história da ciência** e **tecnologia**
- Programadores e pesquisadores que buscam perspectiva histórica rigorosa

---

## Estrutura do ebook
1. **O mundo antes dos computadores**  
   Revolução Industrial, mecanização do cálculo, limites das máquinas existentes e necessidade de métodos de computação mais eficientes.

2. **Formação intelectual de Ada Lovelace**  
   Educação científica no século XIX, matemática aplicada, lógica e a construção de competências técnicas (sem mitificação biográfica).

3. **O encontro com Charles Babbage**  
   Máquina Diferencial, Máquina Analítica e o diálogo intelectual que sustenta a contribuição de Ada.

4. **A Máquina Analítica**  
   Arquitetura, cartões perfurados, memória, unidade de processamento e a ideia de uma máquina de uso geral.

5. **As Notas de Ada Lovelace (A–G)**  
   Tradução do texto de Menabrea e elaboração das Notas, incluindo procedimentos formais (como os números de Bernoulli) e a noção de “programa”.

6. **Limites e legado**  
   A afirmação dos limites da máquina (não “cria” por si) e o legado conceitual duradouro: dados, instruções e processos executáveis.

7. **Conclusão**  
   Síntese do argumento central e relevância para a compreensão histórica da computação.

---

## Critérios metodológicos
Este ebook segue princípios editoriais explícitos:
- **Precisão histórica** e contextualização no século XIX
- **Rejeição de anacronismos** (não tratar a Máquina Analítica como “computador moderno”)
- **Rejeição de romantização** (evitar narrativas de “gênio místico” ou previsões de IA)
- Ênfase em **conceitos**: algoritmo, programa, instruções, dados, execução formal
- Preferência por **fontes primárias** (cartas, notas e publicações do período) e por bibliografia acadêmica consolidada

> Observação: o reconhecimento de Ada Lovelace como “primeira programadora” é apresentado como uma categoria histórica vinculada à descrição formal de procedimentos para uma máquina de uso geral, e não como uma equivalência literal à engenharia de software contemporânea.

---

## Como compilar/gerar o ebook
> **[EDITAR]** Escolha abaixo o seu fluxo (Markdown, LaTeX, Word, etc.).  
Abaixo há três opções comuns. Mantenha somente a que você usar no projeto.

### Opção A — Markdown → PDF (Pandoc)
Pré-requisitos:
- Pandoc
- LaTeX (TeX Live/MiKTeX)

Exemplo:
```bash
pandoc -o dist/ebook.pdf src/ebook.md
```




Opção B — LaTeX → PDF

Pré-requisitos:

TeX Live/MiKTeX

Exemplo:
```
latexmk -pdf -output-directory=dist src/main.tex
```
Opção C — Word/Google Docs
```

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
