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

# Ebook — Ada Lovelace  
**A Primeira Programadora da História**

Este repositório contém os arquivos-fonte do ebook *Ada Lovelace — A Primeira Programadora da História*, desenvolvido com rigor histórico, clareza conceitual e compromisso acadêmico, evitando romantizações ou anacronismos.

---

## Organização do repositório

Sugestão de estrutura (ajuste conforme necessário):

```text
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
```
## Descrição das pastas

### src/
Arquivos principais do ebook em **Markdown**, organizados por capítulos e seções do texto.

### assets/
Recursos visuais e tipográficos utilizados no projeto:

- **capa/**: arquivos da capa do ebook  
- **imagens/**: figuras, ilustrações e diagramas incorporados ao texto  
- **fontes/**: fontes tipográficas utilizadas na composição editorial

### dist/
Versões finais compiladas do ebook:

- **PDF**
- **EPUB**

---

## Como contribuir

Contribuições são bem-vindas, especialmente nas seguintes áreas:

- Revisão técnica e histórica;
- Melhoria de clareza, coesão e precisão conceitual;
- Padronização e verificação de referências bibliográficas;
- Ajustes editoriais (ABNT, Chicago ou outros padrões definidos pelo projeto).

### Fluxo sugerido de contribuição

1. Abra uma **Issue** descrevendo claramente o problema, sugestão ou ajuste proposto.
2. Faça um **fork** do repositório.
3. Crie um branch com nomenclatura adequada, por exemplo:
   - `feat/ajuste-capitulo-3`
   - `fix/revisao-referencias`
4. Envie um **Pull Request** contendo:
   - descrição objetiva das alterações realizadas;
   - justificativa técnica ou editorial;
   - referências, quando aplicável.

---

## Licença

Este ebook está licenciado sob a **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Isso significa que o conteúdo pode ser:

- Compartilhado — copiado e redistribuído em qualquer meio ou formato;
- Adaptado — remixado, transformado e utilizado como base para novos trabalhos;
- Utilizado para fins acadêmicos, educacionais ou comerciais;

Desde que seja fornecida a **Citação**, indicando:

### Citação

Ao reutilizar, adaptar ou redistribuir este conteúdo, a atribuição deve incluir, de forma clara e visível:

- **Título do ebook:** *Ada Lovelace — A Primeira Programadora da História*  
- **Autor:** Rafael Tasinato  
- **Fonte:** Repositório *Ebook Ada Lovelace* (este repositório)  
- **Licença:** Creative Commons Attribution 4.0 International (CC BY 4.0)

Exemplo de atribuição:

> Tasinato, R. *Ada Lovelace — A Primeira Programadora da História*. Repositório Ebook Ada Lovelace. Licenciado sob CC BY 4.0.

A licença completa pode ser consultada em:  
<https://creativecommons.org/licenses/by/4.0/>


## Créditos

- **Texto:** Rafael Tasinato  
- **Revisão:** Rafael Tasinato (com apoio do ChatGPT)  
- **Capa e ilustração:** Rafael Tasinato (DALL·E)  
- **Projeto:** *Ebook Ada Lovelace*

---
