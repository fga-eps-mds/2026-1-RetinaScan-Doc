# Estrutura Analítica do Projeto

## Introdução

A Estrutura Analítica do Projeto (EAP), também conhecida como WBS (*Work Breakdown Structure*), é uma decomposição hierárquica do escopo total do trabalho a ser executado pela equipe, com o objetivo de organizar e definir as entregas do projeto de forma clara e rastreável. Cada nível da EAP representa um refinamento do trabalho, partindo das grandes áreas até os pacotes de trabalho individuais.

A EAP do RetinaScan foi construída com base no Sequenciador definido durante o Lean Inception, nos épicos do Backlog do Produto e nas sprints planejadas para o semestre.

---

## Estrutura Analítica

### 1. RetinaScan

#### 1.1 Gerenciamento do Projeto

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.1.1 Planejamento | Definição de metodologias, ferramentas, heatmap de horários, tabela de conhecimentos e plano de gestão de riscos. |
| 1.1.2 Comunicação | Estabelecimento dos canais e protocolos de comunicação entre equipe e stakeholders. |
| 1.1.3 Acompanhamento de Sprints | Condução dos ritos Scrum (planning, review, retrospective, daily) e gestão do board ZenHub. |
| 1.1.4 Duplas de Líderes Rotativos | Designação e atuação das duplas de liderança a cada Sprint ao longo do semestre. |

---

#### 1.2 Produto — Lean Inception

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.2.1 Visão do Produto | Definição dos objetivos, proposta de valor e visão geral do sistema. |
| 1.2.2 Personas e Jornadas de Usuário | Levantamento dos perfis de usuário e seus fluxos de uso do sistema. |
| 1.2.3 Brainstorming de Funcionalidades | Ideação e levantamento inicial das funcionalidades da solução. |
| 1.2.4 Revisão Técnica, de Negócio e UX | Avaliação e classificação das funcionalidades por esforço, valor e experiência do usuário. |
| 1.2.5 Sequenciador e MVP | Priorização das funcionalidades e definição do Produto Mínimo Viável. |

---

#### 1.3 Documentação

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.3.1 Guia de Contribuição | Políticas de commits, branches e código de conduta. |
| 1.3.2 Arquitetura | Documento de arquitetura da solução com diagrama e decisões técnicas. |
| 1.3.3 Modelagem do Banco de Dados | Modelagem conceitual e lógica do banco de dados. |
| 1.3.4 Metodologias | Descrição das metodologias e práticas adotadas pela equipe. |
| 1.3.5 EAP | Estrutura analítica de decomposição do escopo do projeto. |
| 1.3.6 Roadmap do Produto | Planejamento visual das entregas ao longo do semestre. |
| 1.3.7 Atas de Reuniões | Registro das reuniões realizadas com a equipe e o Product Owner. |
| 1.3.8 Identidade Visual e Protótipo | Definição da identidade visual e prototipação de alta fidelidade. |

---

#### 1.4 RM1 — Documentação, Configuração e Fundação Técnica (30/03 – 12/04/2026)

Sprint inicial do projeto, abrangendo a entrega completa da documentação base, configuração dos repositórios, decisões estruturais da equipe e as primeiras entregas de desenvolvimento.

**Documentação e Configuração:**

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.4.1 Configuração dos repositórios | Criação e configuração dos repositórios de documentação e desenvolvimento, incluindo pipelines e proteções de branch. |
| 1.4.2 Documentação base | Entrega dos documentos iniciais: arquitetura, metodologias, EAP, roadmap, ferramentas, heatmap, tabela de conhecimentos, plano de riscos e guia de contribuição. |
| 1.4.3 Lean Inception | Entrega dos artefatos do Lean Inception: visão do produto, personas, brainstorming, revisão técnica, sequenciador e MVP. |
| 1.4.4 Decisões da equipe | Definição de metodologias, duplas de líderes rotativos, canais de comunicação e backlog do produto. |

**Desenvolvimento:**

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.4.5 Cadastro automático de ADMIN | #7 | Criação automática do usuário administrador na primeira execução da aplicação. |
| 1.4.6 Login do usuário | #10 | Autenticação via e-mail e senha para acesso ao sistema. |
| 1.4.7 Cadastro de usuário pelo ADMIN | #8 | Cadastro de novos usuários pelo administrador do sistema. |
| 1.4.8 API de IA com suporte a múltiplos modelos | — | Exposição da API de inteligência artificial com capacidade de treinamento e comparação de múltiplos modelos. |
| 1.4.9 Resultados dos modelos treinados | — | Apresentação dos resultados obtidos nos modelos treinados até a sprint. |

---

#### 1.5 R1 — Release 1: Cadastro e Upload de Exames (13/04 – 26/04/2026)

Primeira release do produto, entregando as funcionalidades de registro de exames e envio de imagens oftalmológicas.

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.5.1 Cadastro de exame | #13 | Registro de um novo exame com informações do paciente. |
| 1.5.2 Upload de imagem do exame | #14 | Envio de imagem oftalmológica associada a um exame. |

---

#### 1.6 RM2 — Pré-processamento e Pipeline de IA (27/04 – 10/05/2026)

Sprint focada no pré-processamento das imagens e na integração completa do pipeline de inteligência artificial.

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.6.1 Pré-processamento de imagem | #15 | Padronização das imagens enviadas antes do processamento pela IA. |
| 1.6.2 Integração com modelo de IA | #20 | Envio das imagens pré-processadas para o modelo de IA. |
| 1.6.3 Recebimento e interpretação do resultado da IA | #21 | Processamento e interpretação da resposta retornada pelo modelo. |
| 1.6.4 Classificação e associação do resultado ao exame | #22 | Vinculação do resultado da IA ao exame correspondente. |
| 1.6.5 Tratamento de erros no pipeline de IA | #23 | Tratamento de falhas durante o processamento assíncrono. |

---

#### 1.7 RM3 — Histórico, Consulta e Validação do Modelo (11/05 – 24/05/2026)

Sprint que entrega as funcionalidades de consulta e histórico de exames, além da validação da acurácia do modelo de IA e do reporte de erros.

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.7.1 Visualização do histórico de exames | #16 | Listagem dos exames realizados anteriormente. |
| 1.7.2 Botão de "Reportar Erro da IA" | #19 | Funcionalidade para que o médico reporte inconsistências no resultado da IA. |
| 1.7.3 Validação da acurácia do modelo de IA | #24 | Validação formal do modelo com acurácia mínima de 90%. |

---

#### 1.8 R2 — Release 2: MVP (24/05/2026)

Segunda release do produto, consolidando o MVP com busca e filtros de exames. A partir deste ponto o sistema está apto para uso clínico básico.

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.8.1 Busca de exames | #17 | Busca de exames específicos por critérios definidos. |
| 1.8.2 Filtros de exames | #18 | Aplicação de filtros para refinamento dos resultados do histórico. |

> **Marco:** Conclusão do MVP ✓

---

#### 1.9 RM4 — Relatórios e Métricas (25/05 – 07/06/2026)

Sprint de desenvolvimento das funcionalidades de enhancements, entregando relatórios e visualização de métricas.

| Pacote de Trabalho | Issue | Descrição |
| :--- | :---: | :--- |
| 1.9.1 Dashboard com métricas das análises | #25 | Visualização de métricas e indicadores dos exames realizados pelo administrador. |
| 1.9.2 Download de relatório | #26 | Exportação de relatórios de exames em formato para download. |
| 1.9.3 Compartilhamento de resultado via link | #27 | Geração de link para compartilhamento controlado de resultados de exames. |

---

#### 1.10 RM5 — Estabilização e Qualidade (08/06 – 21/06/2026)

Sprint dedicada à estabilização do produto, ampliação da cobertura de testes, correção de bugs e melhorias de qualidade antes da entrega final.

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.10.1 Testes unitários e de integração | Ampliação da cobertura de testes nas camadas de domínio e API. |
| 1.10.2 Correção de bugs | Resolução de inconsistências e falhas identificadas nas sprints anteriores. |
| 1.10.3 Melhorias de desempenho | Otimizações no pipeline de inferência e nas consultas ao banco de dados. |
| 1.10.4 Revisão da documentação | Atualização e revisão geral dos documentos do projeto. |

---

#### 1.11 R3 — Release Final (29/06/2026)

Terceira e última release do projeto, consolidando todas as entregas do semestre e apresentando o produto para a banca avaliadora.

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.11.1 Entrega final do produto | Consolidação de todas as funcionalidades desenvolvidas ao longo do semestre. |
| 1.11.2 Documentação final | Revisão e entrega completa de toda a documentação do projeto. |
| 1.11.3 Apresentação | Preparação e apresentação do produto para a banca avaliadora. |

---

#### 1.12 RM6 — Encerramento (06/07/2026)

Sprint de encerramento do projeto com ajustes finais após a release e fechamento das atividades do semestre.

| Pacote de Trabalho | Descrição |
| :--- | :--- |
| 1.12.1 Ajustes pós-apresentação | Correções e melhorias identificadas durante a apresentação final. |
| 1.12.2 Encerramento do projeto | Fechamento das issues, arquivamento dos repositórios e registro das lições aprendidas. |

---

## Diagrama da EAP

```
RetinaScan
├── 1.1 Gerenciamento do Projeto
│   ├── 1.1.1 Planejamento
│   ├── 1.1.2 Comunicação
│   ├── 1.1.3 Acompanhamento de Sprints
│   └── 1.1.4 Duplas de Líderes Rotativos
├── 1.2 Lean Inception
│   ├── 1.2.1 Visão do Produto
│   ├── 1.2.2 Personas e Jornadas
│   ├── 1.2.3 Brainstorming de Funcionalidades
│   ├── 1.2.4 Revisão Técnica, de Negócio e UX
│   └── 1.2.5 Sequenciador e MVP
├── 1.3 Documentação
│   ├── 1.3.1 Guia de Contribuição
│   ├── 1.3.2 Arquitetura
│   ├── 1.3.3 Modelagem do Banco de Dados
│   ├── 1.3.4 Metodologias
│   ├── 1.3.5 EAP
│   ├── 1.3.6 Roadmap do Produto
│   ├── 1.3.7 Atas de Reuniões
│   └── 1.3.8 Identidade Visual e Protótipo
├── 1.4 RM1 — Documentação, Configuração e Fundação Técnica (30/03 – 12/04)
│   ├── 1.4.1 Configuração dos repositórios
│   ├── 1.4.2 Documentação base
│   ├── 1.4.3 Lean Inception
│   ├── 1.4.4 Decisões da equipe
│   ├── 1.4.5 Cadastro automático de ADMIN
│   ├── 1.4.6 Login do usuário
│   ├── 1.4.7 Cadastro de usuário pelo ADMIN
│   ├── 1.4.8 API de IA com suporte a múltiplos modelos
│   └── 1.4.9 Resultados dos modelos treinados
├── 1.5 R1 — Cadastro e Upload de Exames (13/04 – 26/04)
│   ├── 1.5.1 Cadastro de exame
│   └── 1.5.2 Upload de imagem do exame
├── 1.6 RM2 — Pré-processamento e Pipeline de IA (27/04 – 10/05)
│   ├── 1.6.1 Pré-processamento de imagem
│   ├── 1.6.2 Integração com modelo de IA
│   ├── 1.6.3 Recebimento e interpretação do resultado
│   ├── 1.6.4 Classificação e associação do resultado
│   └── 1.6.5 Tratamento de erros no pipeline
├── 1.7 RM3 — Histórico, Consulta e Validação do Modelo (11/05 – 24/05)
│   ├── 1.7.1 Visualização do histórico de exames
│   ├── 1.7.2 Botão de Reportar Erro da IA
│   └── 1.7.3 Validação da acurácia do modelo de IA
├── 1.8 R2 — MVP (24/05)
│   ├── 1.8.1 Busca de exames
│   └── 1.8.2 Filtros de exames
├── 1.9 RM4 — Relatórios e Métricas (25/05 – 07/06)
│   ├── 1.9.1 Dashboard com métricas das análises
│   ├── 1.9.2 Download de relatório
│   └── 1.9.3 Compartilhamento de resultado via link
├── 1.10 RM5 — Estabilização e Qualidade (08/06 – 21/06)
│   ├── 1.10.1 Testes unitários e de integração
│   ├── 1.10.2 Correção de bugs
│   ├── 1.10.3 Melhorias de desempenho
│   └── 1.10.4 Revisão da documentação
├── 1.11 R3 — Release Final (29/06)
│   ├── 1.11.1 Entrega final do produto
│   ├── 1.11.2 Documentação final
│   └── 1.11.3 Apresentação
└── 1.12 RM6 — Encerramento (06/07)
    ├── 1.12.1 Ajustes pós-apresentação
    └── 1.12.2 Encerramento do projeto
```

---

## Histórico de Versão

| Versão | Data       | Descrição            | Autor                                      | Revisor      |
| :----: | ---------- | -------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/ericcs10) | [xxxx](xxxx) |