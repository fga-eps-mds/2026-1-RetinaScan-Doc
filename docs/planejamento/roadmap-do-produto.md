# Roadmap do Produto

## Introdução

O Roadmap do Produto é um planejamento visual das entregas previstas ao longo do semestre, organizadas por sprint. Ele reflete as decisões tomadas durante o Lean Inception — em especial o Sequenciador e a definição do MVP — e serve como referência para o acompanhamento do progresso do projeto RetinaScan.

O projeto é organizado em 9 sprints: 6 Realize Minor (RM) e 3 Realize (R). As sprints RM focam no desenvolvimento incremental das funcionalidades, enquanto as sprints R representam as releases formais do produto, com entrega validada pelo Product Owner.

---

## Sprints e Entregas

### RM1 — Documentação, Configuração e Fundação Técnica
**Período:** 30/03 – 12/04/2026  
**Líderes:** [Gustavo Costa](https://github.com/cwtshh) e [Iderlan Junio](https://github.com/IderlanJ)

Sprint inicial do projeto, abrangendo a entrega completa da documentação base, configuração dos repositórios, decisões estruturais da equipe e as primeiras entregas de desenvolvimento.

**Documentação e Configuração:**

| Entrega | Tipo |
| :--- | :---: |
| Configuração dos repositórios de documentação e desenvolvimento | Infraestrutura |
| Guia de contribuição (commits, branches, código de conduta) | Documentação |
| Arquitetura da solução | Documentação |
| Metodologias adotadas | Documentação |
| EAP e Roadmap do Produto | Documentação |
| Ferramentas, heatmap de horários e tabela de conhecimentos | Documentação |
| Plano de gestão de riscos | Documentação |
| Lean Inception (visão, personas, sequenciador, MVP) | Produto |
| Backlog do produto | Produto |
| Identidade visual e protótipo de alta fidelidade | Produto |
| Definição das duplas de líderes rotativos | Gestão |
| Atas de reuniões | Documentação |

**Desenvolvimento:**

| Entrega | Issue |
| :--- | :---: |
| Cadastro automático de ADMIN | #7 |
| Login do usuário | #10 |
| Cadastro de usuário pelo ADMIN | #8 |
| API de IA com suporte a treinamento de múltiplos modelos | — |
| Resultados dos modelos treinados | — |

---

### R1 — Release 1: Cadastro e Upload de Exames
**Período:** 13/04 – 26/04/2026  
**Líderes:** [Natália Rodrigues](https://github.com/Natyrodrigues) e [André Maia](https://github.com/andre-maia51)

Primeira release do produto, entregando as funcionalidades de registro de exames e envio de imagens oftalmológicas para processamento.

| Entrega | Issue |
| :--- | :---: |
| Cadastro de exame | #13 |
| Upload de imagem do exame | #14 |

---

### RM2 — Pré-processamento e Pipeline de IA
**Período:** 27/04 – 10/05/2026  
**Líderes:** [Zenilda Vieira](https://github.com/ZenildaVieira) e [Cecília Quaresma](https://github.com/cqcoding)

Sprint focada no pré-processamento das imagens e na integração completa do pipeline de inteligência artificial.

| Entrega | Issue |
| :--- | :---: |
| Pré-processamento de imagem | #15 |
| Integração com modelo de IA | #20 |
| Recebimento e interpretação do resultado da IA | #21 |
| Classificação e associação do resultado ao exame | #22 |
| Tratamento de erros no pipeline de IA | #23 |

---

### RM3 — Histórico, Consulta e Validação do Modelo
**Período:** 11/05 – 24/05/2026  
**Líderes:** [Elias Oliveira](https://github.com/EliasOliver21)

Sprint que entrega as funcionalidades de consulta e histórico de exames, o reporte de erros da IA e a validação formal da acurácia do modelo.

| Entrega | Issue |
| :--- | :---: |
| Visualização do histórico de exames | #16 |
| Botão de "Reportar Erro da IA" | #19 |
| Validação da acurácia do modelo de IA | #24 |

---

### R2 — Release 2: MVP
**Data:** 24/05/2026

Segunda release do produto, consolidando o MVP com busca e filtros de exames. A partir deste ponto o sistema está apto para uso clínico básico.

| Entrega | Issue |
| :--- | :---: |
| Busca de exames | #17 |
| Filtros de exames | #18 |

> **Marco:** Conclusão do MVP ✓

---

### RM4 — Relatórios e Métricas
**Período:** 25/05 – 07/06/2026  
**Líderes:** [Eric Camargo](https://github.com/Ericcs10) e [Harleny Angéllica](https://github.com/Angelicahaas)

Sprint de desenvolvimento das funcionalidades de enhancements, entregando relatórios e visualização de métricas.

| Entrega | Issue |
| :--- | :---: |
| Dashboard com métricas das análises | #25 |
| Download de relatório | #26 |
| Compartilhamento de resultado via link | #27 |

---

### RM5 — Estabilização e Qualidade
**Período:** 08/06 – 21/06/2026  
**Líderes:** [Arthur Ribeiro](https://github.com/artrsousa1) e [Vinícius Roriz](https://github.com/vnsrz)

Sprint dedicada à estabilização do produto, ampliação da cobertura de testes, correção de bugs e melhorias de qualidade antes da entrega final.

| Entrega | Tipo |
| :--- | :---: |
| Testes unitários e de integração | Qualidade |
| Correção de bugs identificados | Qualidade |
| Melhorias de desempenho no pipeline de IA | Qualidade |
| Revisão e atualização da documentação | Documentação |

---

### R3 — Release Final
**Data:** 29/06/2026

Terceira e última release do projeto, consolidando todas as entregas do semestre e apresentando o produto para a banca avaliadora.

| Entrega | Tipo |
| :--- | :---: |
| Produto completo com todas as funcionalidades | Produto |
| Documentação final revisada | Documentação |
| Apresentação para a banca | Gestão |

> **Marco:** Entrega final do semestre ✓

---

### RM6 — Encerramento
**Data:** 06/07/2026

Sprint de encerramento do projeto com ajustes pós-apresentação e fechamento das atividades do semestre.

| Entrega | Tipo |
| :--- | :---: |
| Ajustes e correções pós-apresentação | Produto |
| Fechamento das issues e arquivamento dos repositórios | Gestão |
| Registro de lições aprendidas | Gestão |

---

## Visão Geral do Roadmap

| Sprint | Período | Foco | Líderes |
| :----: | :-----: | :--- | :------ |
| RM1 | 30/03 – 12/04 | Documentação, Configuração e Fundação Técnica | Gustavo Costa e Iderlan Junio |
| R1  | 13/04 – 26/04 | Cadastro e Upload de Exames | Natália Rodrigues e André Maia |
| RM2 | 27/04 – 10/05 | Pré-processamento e Pipeline de IA | Zenilda Vieira e Cecília Quaresma |
| RM3 | 11/05 – 24/05 | Histórico, Consulta e Validação do Modelo | Elias Oliveira |
| R2  | 24/05         | **MVP** ✓ | — |
| RM4 | 25/05 – 07/06 | Relatórios e Métricas | Eric Camargo e Harleny Angéllica |
| RM5 | 08/06 – 21/06 | Estabilização e Qualidade | Arthur Ribeiro e Vinícius Roriz |
| R3  | 29/06         | **Release Final** ✓ | — |
| RM6 | 06/07         | Encerramento | — |

---

## Histórico de Versão

| Versão | Data       | Descrição            | Autor                                      | Revisor      |
| :----: | ---------- | -------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/ericcs10) | [xxxx](xxxx) |