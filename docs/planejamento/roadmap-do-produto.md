# Roadmap do Produto

## Introdução

O Roadmap do Produto é um planejamento visual das entregas previstas ao longo do semestre, organizadas por sprint semanal. Ele reflete as decisões tomadas durante o Lean Inception — em especial o Sequenciador e a definição do MVP — e serve como referência para o acompanhamento do progresso do projeto RetinaScan.

O projeto é organizado em sprints semanais agrupadas em quinzenas. Cada quinzena possui uma dupla de líderes responsável pela facilitação das cerimônias e acompanhamento do progresso. As entregas formais ocorrem nas datas de Release Minor (RM) e Release (R), distribuídas ao longo do semestre.

---

## Visão Geral das Releases e Milestones

| Milestone                                                                        | Data de Entrega | Objetivo Principal                                                 |
| -------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------ |
| 0 - Iniciação do Projeto e Definição do MVP                                      | 30/03/2026      | Lean Inception, definição do MVP, priorização inicial              |
| 1 - Estruturação Inicial do Projeto e Primeira Release Minor (RM1)               | 13/04/2026      | Cadastro de ADMIN, documentação base, setup inicial                |
| 2 - Conclusão da Autenticação e Início do Módulo de Exames (R1)                  | 27/04/2026      | Autenticação, cadastro/upload de exames, protótipo de alta         |
| 3 - Evolução do Módulo de Exames e Iterações com IA (RM2, RM3)                   | 11/05/2026      | Incrementos no cadastro/upload de exames, primeiras integrações IA |
| 4 - Integração com IA e Início do Histórico de Exames (R2)                       | 25/05/2026      | Integração IA, início do histórico de exames                       |
| 5 - Conclusão do Histórico e Consulta e Evolução da Integração com IA (RM4, RM5) | 15/06/2026      | Busca, filtros, reporte de erro IA, interpretação de resultados    |
| 6 - Conclusão do Épico de IA e Entrega do MVP (R3)                               | 29/06/2026      | Classificação de resultados IA, entrega final do MVP               |
| 7 - Ajustes Finais e Estabilização Pós-MVP (RM6)                                 | 06/07/2026      | Ajustes finais após a apresentação, correções, estabilização e encerramento |

---

## Sprints e Entregas detalhadas

#### Milestone 0 - Iniciação do Projeto e Definição do MVP (até 30/03/2026)
- Realizar Lean Inception (visão, personas, MVP, sequenciador)
- Definir e priorizar funcionalidades iniciais
- Primeira experimentação técnica com IA

---

### Milestone 1 - Estruturação Inicial do Projeto e Primeira Release Minor (RM1) (até 13/04/2026)
- Implementar cadastro automático de ADMIN (#7)
- Estruturar documentação base:
  - Guia de contribuição, política de commits/branches, código de conduta
  - Arquitetura, metodologias, EAP, roadmap, plano de riscos, heatmap, tabela de conhecimentos
- Aprovação do backlog com o Product Owner
- Configuração dos repositórios
- Atas de reuniões

#### 1ª Quinzena — 30/03 a 12/04/2026
**Líderes:** [Gustavo Costa](https://github.com/cwtshh) e [Iderlan Junio](https://github.com/IderlanJ)  
**Entrega:** RM1 (13/04/2026)

##### Sprint 1 — 30/03 a 05/04/2026

Sprint de abertura do projeto, focada na estruturação inicial do backlog e alinhamento com o Product Owner.

| Entrega                                                            |      Tipo      |
| :----------------------------------------------------------------- | :------------: |
| Levantamento e escrita do backlog do produto                       |    Produto     |
| Aprovação do backlog com o Product Owner                           |    Produto     |
| Configuração dos repositórios de documentação e desenvolvimento    | Infraestrutura |
| Lean Inception (visão, personas, brainstorming, sequenciador, MVP) |    Produto     |

##### Sprint 2 — 06/04 a 12/04/2026

Sprint de consolidação da documentação base e primeiras entregas de desenvolvimento. **Entrega: RM1 (13/04)**

**Documentação:**

| Entrega                                                     |     Tipo     |
| :---------------------------------------------------------- | :----------: |
| Guia de contribuição (commits, branches, código de conduta) | Documentação |
| Arquitetura da solução                                      | Documentação |
| Metodologias adotadas                                       | Documentação |
| EAP e Roadmap do Produto                                    | Documentação |
| Ferramentas, heatmap de horários e tabela de conhecimentos  | Documentação |
| Plano de gestão de riscos (#41)                             | Documentação |
| Documento de Plano de Custos (#40)                          | Documentação |
| Identidade visual e protótipo de alta fidelidade            |   Produto    |
| Definição das duplas de líderes rotativos                   |    Gestão    |
| Atas de reuniões                                            | Documentação |
| Desenvolvimento da documentação do projeto (#31)            | Documentação |
| Revisão de artefatos e regras de versionamento (#36)        | Documentação |
| Templates de Issue e PR (#37, #39)                          | Documentação |

**Desenvolvimento:**

| Entrega                                                  | Issue |
| :------------------------------------------------------- | :---: |
| Cadastro automático de ADMIN                             |  #7   |
| Login do usuário                                         |  #10  |
| Cadastro de usuário pelo ADMIN                           |  #8   |
| feat: adiciona rota para resgatar todos os usuarios (admin) |  #9   |
| API de IA com suporte a treinamento de múltiplos modelos |   —   |
| Resultados dos modelos treinados                         |   —   |

---

### Milestone 2 - Conclusão da Autenticação e Início do Módulo de Exames (R1) (até 27/04/2026)
- Finalizar épico de autenticação e controle de acesso (#1, #3, #4, #5, #7, #8)
- Iniciar cadastro e upload de exames (#2, #13)
- Desenvolver protótipo de alta fidelidade (#1 - Web)
- Refinar documentação: EAP, backlog, plano de custos
- Issues de destaque:  
  - Correção/Atualização de documentos (#35)
  - Cadastro de exame (#13)
  - Upload de imagem do exame (#16)
  - Autenticação e Controle de Acesso (#1)
  - Cadastro e Upload de Exames (#2)

#### 2ª Quinzena — 13/04 a 26/04/2026
**Líderes:** [Natália Rodrigues](https://github.com/Natyrodrigues) e [André Maia](https://github.com/andre-maia51)  
**Entrega:** R1 (27/04/2026)

##### Sprint 3 — 13/04 a 19/04/2026

Sprint de desenvolvimento focada no registro de exames e envio de imagens oftalmológicas.

| Entrega                   | Issue |
| :------------------------ | :---: |
| Cadastro de exame         |  #13  |
| Upload de imagem do exame |  #14  |

##### Sprint 4 — 20/04 a 26/04/2026

Sprint de finalização e entrega da R1. **Entrega: R1 (27/04)**

| Entrega                                       | Issue |
| :-------------------------------------------- | :---: |
| Revisão e validação das funcionalidades da R1 |   —   |
| Correções e ajustes pré-release               |   —   |

> **Marco:** Release 1 — Cadastro e Upload de Exames ✓

---

### Milestone 3 - Evolução do Módulo de Exames e Iterações com IA (RM2, RM3) (até 11/05/2026)
- Incrementar funcionalidades de exames
- Primeiras integrações e experimentos com IA
- Entregas incrementais RM2 e RM3

#### 3ª Quinzena — 27/04 a 10/05/2026
**Líderes:** [Zenilda Vieira](https://github.com/ZenildaVieira) e [Cecília Quaresma](https://github.com/cqcoding)  
**Entregas:** RM2 (04/05/2026) e RM3 (11/05/2026)

##### Sprint 5 — 27/04 a 03/05/2026

Sprint focada no pré-processamento das imagens e início da integração com o pipeline de IA. **Entrega: RM2 (04/05)**

| Entrega                                        | Issue |
| :--------------------------------------------- | :---: |
| Pré-processamento de imagem                    |  #15  |
| Integração com modelo de IA                    |  #20  |
| Recebimento e interpretação do resultado da IA |  #21  |

##### Sprint 6 — 04/05 a 10/05/2026

Sprint de conclusão do pipeline de IA. **Entrega: RM3 (11/05)**

| Entrega                                          | Issue |
| :----------------------------------------------- | :---: |
| Classificação e associação do resultado ao exame |  #22  |
| Tratamento de erros no pipeline de IA            |  #23  |

---

### Milestone 4 - Integração com IA e Início do Histórico de Exames (R2) (até 25/05/2026)
- Integração do sistema com modelo de IA (envio/análise de imagens)
- Início do histórico e consulta de exames para admin/médico
  
#### 4ª Quinzena — 11/05 a 24/05/2026
**Líderes:** [Elias Oliveira](https://github.com/EliasOliver21) e [Yan Luca](https://github.com/yan-luca)  
**Entrega:** R2 (25/05/2026)

##### Sprint 7 — 11/05 a 17/05/2026

Sprint focada nas funcionalidades de histórico, consulta e reporte de erros da IA.

| Entrega                               | Issue |
| :------------------------------------ | :---: |
| Visualização do histórico de exames   |  #16  |
| Botão de "Reportar Erro da IA"        |  #19  |
| Validação da acurácia do modelo de IA |  #24  |

##### Sprint 8 — 18/05 a 24/05/2026

Sprint de finalização do MVP com busca e filtros, e entrega da R2. **Entrega: R2 (25/05)**

| Entrega           | Issue |
| :---------------- | :---: |
| Busca de exames   |  #17  |
| Filtros de exames |  #18  |

> **Marco:** Release 2 — MVP ✓

---

### Milestone 5 - Conclusão do Histórico e Consulta e Evolução da Integração com IA (RM4, RM5) (até 15/06/2026)
- Finalizar funcionalidades de busca, filtros e consulta de exames
- Evoluir integração IA: reporte de erro, interpretação de resultados

#### 5ª Quinzena — 25/05 a 07/06/2026
**Líderes:** [Eric Camargo](https://github.com/Ericcs10) e [Harleny Angélica](https://github.com/Angelicahaas)  
**Entrega:** RM4 (01/06/2026)

##### Sprint 9 — 25/05 a 31/05/2026

Sprint de desenvolvimento das funcionalidades de enhancements. **Entrega: RM4 (01/06)**

| Entrega                                | Issue    |
| :------------------------------------- | :------: |
| Dashboard com métricas das análises    |  #6, #25 |
| Download de relatório                  |  #26     |
| Compartilhamento de resultado via link |  #27     |

##### Sprint 10 — 01/06 a 07/06/2026

Sprint de refinamento e ajustes das funcionalidades de relatórios e métricas.

| Entrega                               |   Tipo    |
| :------------------------------------ | :-------: |
| Refinamento do dashboard e relatórios | Qualidade |
| Correções pós-RM4                     | Qualidade |

---




#### 6ª Quinzena — 08/06 a 21/06/2026
**Líderes:** [Arthur Ribeiro](https://github.com/artrsousa1) e [Vinícius Roriz](https://github.com/vnsrz)  
**Entrega:** RM5 (15/06/2026)

##### Sprint 11 — 08/06 a 14/06/2026

Sprint dedicada à estabilização do produto e ampliação da cobertura de testes. **Entrega: RM5 (15/06)**

| Entrega                                   |   Tipo    |
| :---------------------------------------- | :-------: |
| Testes unitários e de integração          | Qualidade |
| Correção de bugs identificados            | Qualidade |
| Melhorias de desempenho no pipeline de IA | Qualidade |

---

### Milestone 6 - Conclusão do Épico de IA e Entrega do MVP (R3) (até 29/06/2026)
- Finalizar épico de IA: classificação e associação de resultados (#22)
- Entrega final do MVP

##### Sprint 12 — 15/06 a 21/06/2026

Sprint de revisão final da documentação e preparação para a release final.

| Entrega                               |     Tipo     |
| :------------------------------------ | :----------: |
| Revisão e atualização da documentação | Documentação |
| Preparação para a R3                  |    Gestão    |

---

#### 7ª Quinzena — 22/06 a 05/07/2026
**Líderes:** A definir  
**Entregas:** R3 (29/06/2026) e RM6 (06/07/2026)

##### Sprint 13 — 22/06 a 28/06/2026

Sprint de consolidação final do produto e preparação da apresentação. **Entrega: R3 (29/06)**

| Entrega                                       |     Tipo     |
| :-------------------------------------------- | :----------: |
| Produto completo com todas as funcionalidades |   Produto    |
| Documentação final revisada                   | Documentação |
| Preparação da apresentação para a banca       |    Gestão    |

> **Marco:** Release Final ✓

### Milestone 7 - Ajustes Finais e Estabilização Pós-MVP (RM6) (até 06/07/2026)
- Realizar ajustes e correções pós-apresentação, concluir o fechamento das issues pendentes e registrar as lições aprendidas para o encerramento do projeto.


##### Sprint 14 — 29/06 a 05/07/2026

Sprint de encerramento do projeto. **Entrega: RM6 (06/07)**

| Entrega                                               |  Tipo   |
| :---------------------------------------------------- | :-----: |
| Ajustes e correções pós-apresentação                  | Produto |
| Fechamento das issues e arquivamento dos repositórios | Gestão  |
| Registro de lições aprendidas                         | Gestão  |

---



## Visão Geral do Roadmap

| Quinzena |    Período    | Sprint | Foco                                         |     Entrega     | Milestone (ZenHub)  |
| :------: | :-----------: | :----: | :------------------------------------------- | :-------------: | :-----------------: |
|    0ª    | 23/03 – 29/03 |   S0   | Lean Inception                               |        —        | 0  (até 30/03/2026) |
|    1ª    | 30/03 – 05/04 |   S1   | Backlog e alinhamento com PO                 |        —        | 1  (até 13/04/2026) |
|    1ª    | 06/04 – 12/04 |   S2   | Documentação base + Fundação Técnica         | **RM1** (13/04) |          1          |
|    2ª    | 13/04 – 19/04 |   S3   | Cadastro e Upload de Exames                  |        —        | 2  (até 27/04/2026) |
|    2ª    | 20/04 – 26/04 |   S4   | Revisão e validação da R1                    | **R1** (27/04)  |          2          |
|    3ª    | 27/04 – 03/05 |   S5   | Pré-processamento e início do pipeline de IA | **RM2** (04/05) | 3  (até 11/05/2026) |
|    3ª    | 04/05 – 10/05 |   S6   | Conclusão do pipeline de IA                  | **RM3** (11/05) |          3          |
|    4ª    | 11/05 – 17/05 |   S7   | Histórico, Consulta e Validação do Modelo    |        —        | 4  (até 25/05/2026) |
|    4ª    | 18/05 – 24/05 |   S8   | Busca e Filtros — MVP                        | **R2** (25/05)  |          4          |
|    5ª    | 25/05 – 31/05 |   S9   | Relatórios e Métricas                        | **RM4** (01/06) | 5  (até 15/06/2026) |
|    5ª    | 01/06 – 07/06 |  S10   | Refinamento pós-RM4                          |        —        |          5          |
|    6ª    | 08/06 – 14/06 |  S11   | Estabilização e Qualidade                    | **RM5** (15/06) |          5          |
|    6ª    | 15/06 – 21/06 |  S12   | Revisão final e preparação da R3             |        —        | 6  (até 29/06/2026) |
|    7ª    | 22/06 – 28/06 |  S13   | Consolidação final e apresentação            | **R3** (29/06)  |          6          |
|    7ª    | 29/06 – 05/07 |  S14   | Encerramento do projeto                      | **RM6** (06/07) | 7  (até 06/07/2026) |
---

## Histórico de Versão

| Versão | Data       | Descrição                | Autor                                              | Revisor                                            |
| :----: | ---------- | ------------------------ | -------------------------------------------------- | -------------------------------------------------- |
| `1.0`  | 12/04/2026 | Criação do documento     | [Eric Camargo](https://github.com/Ericcs10)        | [Zenilda Vieira](https://github.com/zenildavieira) |
| `1.1`  | 19/04/2026 | Acréscimo das milestones | [Zenilda Vieira](https://github.com/zenildavieira) | [xxxx](xxxx)                                       |