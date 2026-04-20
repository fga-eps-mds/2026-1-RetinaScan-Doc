# Estrutura Analítica do Projeto

## Introdução

A Estrutura Analítica do Projeto (EAP), também conhecida como WBS (*Work Breakdown Structure*), é uma decomposição hierárquica do escopo total do trabalho a ser executado pela equipe, com o objetivo de organizar e definir as entregas do projeto de forma clara e rastreável. Cada nível da EAP representa um refinamento do trabalho, partindo das grandes áreas até os pacotes de trabalho individuais.

A EAP do RetinaScan foi construída com base no Sequenciador definido durante o Lean Inception, nos épicos do Backlog do Produto e nas sprints planejadas para o semestre.

---

## Estrutura Analítica

### 1. RetinaScan

---

#### 1.1 Milestone 0 — Iniciação do Projeto e Definição do MVP (23/03 – 30/03/2026)

Fase de abertura do projeto com definição de visão, escopo inicial, priorização e organização de base para execução.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.1.1 Visão do Produto (Lean Inception) | Produto | — | Definição dos objetivos, proposta de valor e visão geral do sistema. |
| 1.1.2 Personas e Jornadas de Usuário | Produto | — | Levantamento dos perfis de usuário e principais fluxos de uso do sistema. |
| 1.1.3 Brainstorming e Revisão Técnica, de Negócio e UX | Produto | — | Ideação e avaliação das funcionalidades por valor, esforço e experiência do usuário. |
| 1.1.4 Sequenciador, MVP e Priorização Inicial | Produto | — | Priorização das funcionalidades e definição do MVP para início das entregas. |
| 1.1.5 Planejamento e Governança do Projeto | Gestão | — | Definição de metodologias, ferramentas, heatmap, tabela de conhecimentos, riscos e liderança rotativa. |
| 1.1.6 Comunicação e Acompanhamento de Sprints | Gestão | — | Definição de canais e condução dos ritos Scrum com gestão do board. |
| 1.1.7 Primeira experimentação técnica com IA | Qualidade | — | Exploração técnica inicial para preparar o pipeline de IA. |

---

#### 1.2 Milestone 1 — Estruturação Inicial do Projeto e Primeira Release Minor (RM1) (30/03 – 13/04/2026)

Fase de estruturação do projeto com consolidação da base documental e primeira entrega técnica.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.2.1 Levantamento e escrita do backlog do produto | Produto | — | Organização inicial das funcionalidades e critérios de priorização. |
| 1.2.2 Aprovação do backlog com o Product Owner | Produto | — | Validação do escopo priorizado para as próximas releases. |
| 1.2.3 Configuração dos repositórios de documentação e desenvolvimento | Infraestrutura | — | Estruturação dos repositórios e fluxo de colaboração da equipe. |
| 1.2.4 Guia de Contribuição | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Definição de políticas de contribuição, commits, branches e conduta. |
| 1.5.5 Arquitetura | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Documentação da arquitetura da solução e decisões técnicas iniciais. |
| 1.5.6 Modelagem do Banco de Dados | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Modelagem conceitual/lógica inicial para suportar os módulos do sistema. |
| 1.5.7 Metodologias | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Registro das metodologias e práticas de desenvolvimento adotadas. |
| 1.5.8 EAP | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Estrutura analítica do projeto para organização do escopo. |
| 1.5.9 Roadmap do Produto | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Planejamento de entregas por milestones e sprints. |
| 1.5.10 Atas de Reuniões | Documentação | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Registro de decisões e alinhamentos com equipe e PO. |
| 1.5.11 Identidade Visual e Protótipo | Produto | [Doc#31](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/31) | Definição visual e prototipação de alta fidelidade do produto. |
| 1.5.12 Cadastro automático de ADMIN | Desenvolvimento | [Api#5](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/5) | Implementação do usuário ADMIN inicial do sistema. |

---

#### 1.6 Milestone 2 — Conclusão da Autenticação e Início do Módulo de Exames (R1) (13/04 – 27/04/2026)

Fase de fechamento da autenticação, início do módulo de exames e integração das primeiras entregas de release.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.6.1 Login do usuário (back-end) | Desenvolvimento | [Api#3](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/3) | Implementação de autenticação via API. |
| 1.6.2 Cadastro de usuário pelo ADMIN (back-end e front-end) | Desenvolvimento | [Api#2](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/2), [Web#2](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues/2) | Cadastro de usuários com fluxo integrado entre API e interface. |
| 1.6.3 Gestão de usuários no back-end (edição e solicitação de CPF/CRM) | Desenvolvimento | [Api#4](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/4), [Api#7](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/7) | Evolução do módulo de usuários para atualização de dados sensíveis. |
| 1.6.4 Consolidação do protótipo de alta fidelidade | Produto | [Web#1](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues/1) | Ajuste do protótipo para aderência ao fluxo funcional da release. |
| 1.6.5 Cadastro de exame | Produto | [Doc#13](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/13) | Registro de exames no sistema. |
| 1.6.6 Upload de imagem do exame | Produto | [Doc#14](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/14) | Envio de imagem associada ao exame cadastrado. |
| 1.6.7 Correção de bug na edição de admin cadastrado automaticamente | Qualidade | [Api#13](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/13) | Correção de inconsistência no fluxo de edição do ADMIN. |
| 1.6.8 Refinamento da documentação de apoio à release | Documentação | [Doc#35](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/35), [Doc#40](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/40) | Atualização da documentação para suportar a entrega da R1. |

---

#### 1.7 Milestone 3 — Evolução do Módulo de Exames e Iterações com IA (RM2, RM3) (27/04 – 11/05/2026)

Fase de evolução técnica do pipeline de IA e do processamento de exames.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.7.1 Pré-processamento de imagem | Produto | [Doc#15](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/15) | Padronização das imagens para consumo da IA. |
| 1.7.2 Integração com modelo de IA | Produto | [Doc#20](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/20) | Integração entre sistema e serviço de inferência. |
| 1.7.3 Recebimento e interpretação do resultado da IA | Produto | [Doc#21](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/21) | Tratamento da resposta da IA para uso no sistema. |
| 1.7.4 Classificação e associação do resultado ao exame | Produto | [Doc#22](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/22) | Vinculação do resultado ao exame correspondente. |
| 1.7.5 Tratamento de erros no pipeline de IA | Produto | [Doc#23](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/23) | Tratamento de falhas no fluxo de processamento. |

---

#### 1.8 Milestone 4 — Integração com IA e Início do Histórico de Exames (R2) (11/05 – 25/05/2026)

Fase de consolidação da integração com IA e habilitação da consulta de histórico.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.8.1 Visualização do histórico de exames | Produto | [Doc#16](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/16) | Exibição de exames realizados no histórico do usuário. |
| 1.8.2 Reporte de erro da IA | Produto | [Doc#19](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/19) | Registro de inconsistências percebidas no resultado de IA. |
| 1.8.3 Validação da acurácia do modelo de IA | Qualidade | [Doc#24](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/24) | Validação de desempenho do modelo usado no produto. |
| 1.8.4 Busca de médicos | Produto | [Doc#42](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/42) | Busca de médicos cadastrados pelo administrador. |
| 1.8.5 Busca de exames | Produto | [Doc#17](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/17) | Busca de exames por critérios de consulta. |
| 1.8.6 Filtros de exames | Produto | [Doc#18](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/18) | Refinamento dos resultados exibidos no histórico. |

---

#### 1.9 Milestone 5 — Conclusão do Histórico e Consulta e Evolução da Integração com IA (RM4, RM5) (25/05 – 15/06/2026)

Fase de evolução de relatórios/métricas e refinamento das funcionalidades de consulta e IA.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.9.1 Dashboard com métricas das análises | Produto | [Api#6](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues/6), [Doc#25](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/25) | Visualização consolidada de indicadores de exames. |
| 1.9.2 Download de relatório | Produto | [Doc#26](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/26) | Exportação de relatório de resultados. |
| 1.9.3 Compartilhamento de resultado via link | Produto | [Doc#27](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues/27) | Compartilhamento controlado por link. |
| 1.9.4 Refinamento de busca, filtros e consulta de exames | Qualidade | — | Ajustes funcionais no fluxo de histórico e consulta. |
| 1.9.5 Evolução do reporte de erro e interpretação de resultados da IA | Qualidade | — | Refinamento do ciclo de retorno da IA no sistema. |
| 1.9.6 Edição de dados do usuário (front-end) | Desenvolvimento | [Web#6](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues/6) | Edição de dados de usuário na interface. |

---

#### 1.10 Milestone 6 — Conclusão do Épico de IA e Entrega do MVP (R3) (15/06 – 29/06/2026)

Fase de validação final da IA, revisão de documentação e preparação da entrega final do MVP.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.10.1 Validação final da classificação e associação de resultados da IA | Qualidade | — | Verificação final do comportamento do pipeline de IA para entrega. |
| 1.10.2 Revisão e atualização da documentação | Documentação | — | Atualização da documentação com o estado final da release. |
| 1.10.3 Preparação para a R3 | Gestão | — | Organização da entrega final e alinhamento de apresentação. |
| 1.10.4 Consolidação final do produto e preparação da apresentação | Produto | — | Consolidação do MVP para apresentação à banca. |

---

#### 1.11 Milestone 7 — Ajustes Finais e Estabilização Pós-MVP (RM6) (29/06 – 06/07/2026)

Fase de encerramento do projeto com estabilização e fechamento formal das atividades.

| Pacote de Trabalho | Tipo | Issue | Descrição |
| :--- | :---: | :---: | :--- |
| 1.11.1 Ajustes e correções pós-apresentação | Produto | — | Ajustes finais observados após a apresentação. |
| 1.11.2 Fechamento das issues e arquivamento dos repositórios | Gestão | — | Encerramento de pendências operacionais e organização do repositório final. |
| 1.11.3 Registro de lições aprendidas | Gestão | — | Registro das lições do semestre para retroalimentar próximos ciclos. |

---

## Diagrama da EAP

```
RetinaScan
├── 1.4 Milestone 0 — Iniciação do Projeto e Definição do MVP (23/03 – 30/03)
│   ├── 1.4.1 Visão do Produto
│   ├── 1.4.2 Personas e Jornadas
│   ├── 1.4.3 Brainstorming e Revisão Técnica/Negócio/UX
│   ├── 1.4.4 Sequenciador, MVP e priorização inicial
│   ├── 1.4.5 Planejamento e governança do projeto
│   ├── 1.4.6 Comunicação e acompanhamento de sprints
│   └── 1.4.7 Experimentação técnica com IA
├── 1.5 Milestone 1 — Estruturação Inicial e RM1 (30/03 – 13/04)
│   ├── 1.5.1 Backlog e alinhamento com PO
│   ├── 1.5.2 Configuração dos repositórios
│   ├── 1.5.3 Preparação de base técnica
│   ├── 1.5.4 Guia de Contribuição
│   ├── 1.5.5 Arquitetura
│   ├── 1.5.6 Modelagem do Banco de Dados
│   ├── 1.5.7 Metodologias
│   ├── 1.5.8 EAP
│   ├── 1.5.9 Roadmap do Produto
│   ├── 1.5.10 Atas de Reuniões
│   ├── 1.5.11 Identidade Visual e Protótipo
│   └── 1.5.12 Cadastro automático de ADMIN
├── 1.6 Milestone 2 — Conclusão da Autenticação e Início do Módulo de Exames (13/04 – 27/04)
│   ├── 1.6.1 Autenticação e cadastro de usuários
│   ├── 1.6.2 Gestão de usuários (back-end)
│   ├── 1.6.3 Protótipo de alta fidelidade
│   ├── 1.6.4 Cadastro e upload de exame
│   └── 1.6.5 Refinamentos e correções da release
├── 1.7 Milestone 3 — Evolução do Módulo de Exames e Iterações com IA (27/04 – 11/05)
│   ├── 1.7.1 Pré-processamento de imagem
│   ├── 1.7.2 Integração e retorno da IA
│   └── 1.7.3 Classificação e tratamento de erros
├── 1.8 Milestone 4 — Integração com IA e Início do Histórico de Exames (11/05 – 25/05)
│   ├── 1.8.1 Histórico e consulta de exames
│   ├── 1.8.2 Reporte/validação da IA
│   └── 1.8.3 Busca de médicos
├── 1.9 Milestone 5 — Conclusão do Histórico/Consulta e Evolução da IA (25/05 – 15/06)
│   ├── 1.9.1 Relatórios e métricas
│   ├── 1.9.2 Refinamentos de histórico e IA
│   └── 1.9.3 Gestão de usuários (front-end)
├── 1.10 Milestone 6 — Conclusão do Épico de IA e Entrega do MVP (15/06 – 29/06)
│   ├── 1.10.1 Validação final da IA
│   ├── 1.10.2 Revisão documental
│   ├── 1.10.3 Preparação para R3
│   └── 1.10.4 Consolidação final do produto
└── 1.11 Milestone 7 — Ajustes Finais e Estabilização Pós-MVP (29/06 – 06/07)
    ├── 1.11.1 Ajustes pós-apresentação
    ├── 1.11.2 Fechamento operacional do projeto
    └── 1.11.3 Registro de lições aprendidas
```

---

## Histórico de Versão

| Versão | Data       | Descrição            | Autor                                      | Revisor      |
| :----: | ---------- | -------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/ericcs10) | [xxxx](xxxx) |
| `1.1`  | 20/04/2026 | Alinhamento da EAP com milestones, sprints e entregas do roadmap do produto | [Zenilda Vieira](https://github.com/zenildavieira) | [xxxx](xxxx) |
| `1.2`  | 20/04/2026 | Consolidação dos blocos 1.1, 1.2 e 1.3 dentro de 1.4 e 1.5 para remover redundâncias | [Zenilda Vieira](https://github.com/zenildavieira) | [xxxx](xxxx) |