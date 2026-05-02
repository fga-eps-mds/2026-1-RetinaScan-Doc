# Estrutura Analítica do Projeto

## Objetivo do Documento

A Estrutura Analítica do Projeto (EAP) do RetinaScan organiza o escopo total do projeto em entregas verificáveis e pacotes de trabalho gerenciáveis.

Nesta versão, o primeiro nível da EAP está organizado em blocos paralelos separando as atividades de Gestão, Documentação e Dashboard das entregas de Desenvolvimento de Software (Releases R1, R2_MVP, R3 e RM6).

Detalhes operacionais como issues, responsáveis, status, critérios de aceitação e PRs devem ser consultados no ZenHub/GitHub.

---

## Artefato Visual da EAP

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/RBntSw1Xm7n0QYO6OKy7Jw/EAP---RetinaScan?node-id=0-1&embed-host=share" allowfullscreen></iframe>

<p><strong>Fonte:</strong> <a href="https://github.com/andre-maia51">André Maia</a>, 2026. Disponível em: <a href="https://www.figma.com/board/RBntSw1Xm7n0QYO6OKy7Jw/EAP---RetinaScan?node-id=0-1&t=RdfnDUNFLMZm2XYo-1">EAP - RetinaScan</a>.</p>

---

## Estrutura Analítica do Projeto

## 1. RetinaScan

---

### 1.1 Gerenciamento do Projeto

Objetivo: Planejar, monitorar e formalizar a execução e o encerramento do projeto.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.1.1 | Planejamento e Escopo | Consolidação da visão do produto, Lean Inception, Canvas MVP, backlog, roadmap, EAP e refinamento do escopo validável. |
| 1.1.2 | Governança e Gestão | Definição de metodologia, cerimônias, comunicação, custos, riscos e acompanhamento das releases. |
| 1.1.3 | Preparação de Apresentações | Consolidação das evidências e roteiro para bancas e apresentações. |
| 1.1.4 | Registro de Lições Aprendidas | Registro dos aprendizados técnicos, gerenciais e de produto. |
| 1.1.5 | Encerramento Formal | Consolidação das evidências finais e fechamento do projeto. |

---

### 1.2 Design e Documentação

Objetivo: Definir a base técnica, a experiência do usuário e manter a documentação estrutural.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.2.1 | Arquitetura e Modelagem Inicial | Documento de arquitetura, modelagem de dados e decisões técnicas iniciais. |
| 1.2.2 | Protótipo e Identidade Visual | Consolidação da identidade visual e protótipo de alta fidelidade dos fluxos priorizados. |
| 1.2.3 | Revisão Final da Documentação | Atualização dos documentos conforme estado final do produto. |
| 1.2.4 | Revisão Final dos Repositórios | Conferência de README, licença, contribuição, pipelines e organização geral. |

---

### 1.3 Dashboard Gerencial e Analítico

Objetivo: Fornecer análises baseadas em dados sobre a saúde do projeto e do código.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.3.1 | Dashboard Gerencial e Analítico | Métricas de ZenHub/GitHub, SonarCloud, EVM-Ágil, riscos e decisões baseadas em dados. |

---

### 1.4 Produto de Software (Releases)

#### 1.4.1 R1 — Release Major 1
Objetivo: entregar a fundação funcional e técnica necessária para o fluxo inicial do produto.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.1.1 | Repositórios e Configuração | Configuração dos repositórios, políticas de contribuição, templates, código de conduta e versionamento. |
| 1.4.1.2 | CI/CD e Qualidade Inicial | Pipelines, lint, build, testes iniciais, SonarCloud e coleta inicial de métricas. |
| 1.4.1.3 | Autenticação e Controle de Acesso | Login, cadastro inicial de usuários, perfis e controle de acesso. |
| 1.4.1.4 | Segurança e LGPD Inicial | Requisitos iniciais de privacidade, controle de acesso, rastreabilidade e proteção de dados sensíveis. |
| 1.4.1.5 | Cadastro e Upload de Exames | Registro de exames e envio de imagens associadas. |
| 1.4.1.6 | Validação da R1 | Testes, correções e validação com PO/cliente. |

#### 1.4.2 R2_MVP — Entrega do MVP
Objetivo: entregar o menor produto validável com valor para o usuário.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.2.1 | Processamento de Imagens | Pré-processamento das imagens antes da inferência. |
| 1.4.2.2 | Integração com Modelo de IA | Comunicação entre o sistema e o serviço/modelo de IA. |
| 1.4.2.3 | Interpretação dos Resultados da IA | Tratamento da resposta da IA para uso no sistema. |
| 1.4.2.4 | Associação Resultado-Exame | Vinculação do resultado processado ao exame correspondente. |
| 1.4.2.5 | Histórico e Consulta de Exames | Consulta de exames processados, incluindo busca e filtros como parte do fluxo de histórico. |
| 1.4.2.6 | Reporte de Erro da IA | Registro de inconsistências percebidas no resultado gerado pela IA. |
| 1.4.2.7 | Validação do Modelo | Avaliação inicial da acurácia e comportamento do modelo de IA. |
| 1.4.2.8 | Validação do MVP | Testes funcionais, correções e aceite do fluxo essencial pelo PO/cliente. |

#### 1.4.3 R3 — Consolidação Final do Produto
Objetivo: consolidar o produto planejado para o semestre, evoluindo relatórios, métricas, qualidade e estabilidade.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.3.1 | Relatórios e Métricas do Produto | Dashboard de análises, download de relatório e visualização de indicadores. |
| 1.4.3.2 | Compartilhamento de Resultados | Compartilhamento controlado de resultados, respeitando requisitos de segurança e LGPD. |
| 1.4.3.3 | Refinamento de Histórico e Consulta | Ajustes de usabilidade, busca, filtros e experiência no acompanhamento de exames. |
| 1.4.3.4 | Evolução do Pipeline de IA | Melhorias no processamento, interpretação, tratamento de erros e desempenho. |
| 1.4.3.5 | Gestão de Usuários Completa | Evolução da edição de dados e ajustes do fluxo administrativo. |
| 1.4.3.6 | Testes e Cobertura | Ampliação dos testes unitários, integração, funcionais e acompanhamento de cobertura. |
| 1.4.3.7 | Validação da R3 | Correções finais, aceite da entrega e estabilização do produto. |

#### 1.4.4 RM6 — Estabilização de Código
Objetivo: realizar ajustes finais no código após a apresentação.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.4.1 | Ajustes Pós-Apresentação | Correções e melhorias identificadas após a avaliação da R3. |
| 1.4.4.2 | Fechamento de Issues e PRs | Organização final das pendências nos repositórios. |

---

## Observação de Rastreabilidade

A EAP apresenta a decomposição do escopo em entregas verificáveis. A rastreabilidade detalhada entre pacotes de trabalho, histórias, critérios de aceitação, responsáveis e PRs deve ser mantida no ZenHub/GitHub.

---

## Política de Atualização

Este documento deve ser atualizado somente quando houver mudança estrutural no escopo das releases.

Alterações operacionais de sprint, status, responsáveis, issues ou PRs não devem ser duplicadas neste documento.

## Histórico de Versão

| Versão | Data       | Descrição            | Autor                                      | Revisor      |
| :----: | ---------- | -------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/ericcs10) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.1`  | 20/04/2026 | Alinhamento da EAP com milestones, sprints e entregas do roadmap do produto | [Zenilda Vieira](https://github.com/zenildavieira) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.2`  | 20/04/2026 | Consolidação dos blocos 1.1, 1.2 e 1.3 dentro de 1.4 e 1.5 para remover redundâncias | [Zenilda Vieira](https://github.com/zenildavieira) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.3` | 02/05/2026 | Alterações de acordo com o Feedback do professor e adição do diagrama | [André Maia](https://github.com/andre-maia51) | [xxxx](xxxx)
