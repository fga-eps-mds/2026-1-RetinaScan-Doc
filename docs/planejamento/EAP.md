# Estrutura Analítica do Projeto

## Objetivo do Documento

A Estrutura Analítica do Projeto (EAP) do RetinaScan organiza o escopo total do projeto em entregas verificáveis e pacotes de trabalho gerenciáveis.

Nesta versão, o primeiro nível da EAP está organizado em blocos paralelos separando as atividades de Gestão, Documentação, Dashboard das entregas e Desenvolvimento de Software (Releases R1, R2_MVP, R3 e RM6).

Detalhes operacionais como issues, responsáveis, status, critérios de aceitação e PRs devem ser consultados no ZenHub/GitHub.

---

## Artefato Visual da EAP

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/RBntSw1Xm7n0QYO6OKy7Jw/EAP---RetinaScan?node-id=0-1&embed-host=share" allowfullscreen></iframe>

<p><strong>Fonte:</strong> <a href="https://github.com/andre-maia51">André Maia</a>, 2026. Disponível em: <a href="https://www.figma.com/board/RBntSw1Xm7n0QYO6OKy7Jw/EAP---RetinaScan?node-id=0-1&t=RdfnDUNFLMZm2XYo-1">EAP - RetinaScan</a>.</p>

---

## Estrutura Analítica do Projeto

### 1. RetinaScan

#### 1.1 Gerenciamento do Projeto

Objetivo: Produzir os artefatos de planejamento, monitoramento e encerramento do projeto.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.1.1 | Documento de Visão e Canvas MVP | Definição da visão do produto, delimitação de escopo e estruturação do Produto Mínimo Viável (MVP). |
| 1.1.2 | Roadmap e Backlog do Produto | Mapeamento das entregas no tempo e lista priorizada de requisitos e histórias de usuário. |
| 1.1.3 | Estrutura Analítica do Projeto (EAP) | Subdivisão hierárquica do escopo do projeto em pacotes de trabalho (este documento). |
| 1.1.4 | Manual de Metodologia e Processos | Documento definindo os frameworks ágeis adotados, ritos, cadência de sprints e fluxo de comunicação da equipe. |
| 1.1.5 | Planejamento de Tempo, Custos e EVM | Documentos contendo o Cronograma (Gantt), estimativa de custos e acompanhamento de métricas de Valor Agregado (EVM). |
| 1.1.6 | Plano de Gestão de Riscos | Matriz atualizada de riscos do projeto, probabilidades, impactos e planos de mitigação. |
| 1.1.7 | Material de Apresentação de Releases | Slides, roteiros de demonstração do produto ao vivo e vídeos das bancas R1, R2 e R3 para aprovação do PO. |
| 1.1.8 | Termo de Encerramento do Projeto | Consolidação das evidências finais e documento de fechamento do projeto. |

---

#### 1.2 Design e Documentação

Objetivo: Entregar a base técnica documentada, os artefatos de experiência do usuário e os repositórios estruturados.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.2.1 | Documento de Arquitetura de Software | Documento contendo modelagem da arquitetura, registro de decisões arquiteturais, Diagramas de UML e Documentação dos Endpoints da API. |
| 1.2.2 | Documento de Modelagem de Dados | Documento contendo a modelagem dos dados do sistema, dicionário de dados, diagramas entidade-relacionamento (conceitual) e lógico. |
| 1.2.3 | Documentação e Versionamento de Modelos de IA | Documentos contendo a arquitetura base (RETFound), resultados de fine-tuning, configuração e regras de versionamento semântico dos modelos. |
| 1.2.4 | Protótipos e Guia de Estilo | Guia de identidade visual e protótipo de alta fidelidade dos fluxos priorizados. |
| 1.2.5 | Repositórios e Documentação Finalizados | READMEs, licenças, guias de contribuição e código base devidamente versionados e documentados. |

---

#### 1.3 Dashboard Gerencial e Analítico

Objetivo: Fornecer a ferramenta de análise e a documentação técnica que embase as métricas de saúde do projeto.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.3.1 | Dashboards de Métricas e Documentação Base | Aplicação do Dashboard (ZenHub, SonarCloud) e Documentação acessória contendo a explicação das fórmulas, cálculos, fontes dos dados brutos e justificativas de decisões. |

---

#### 1.4 Produto de Software (Releases)

##### 1.4.1 R1 — Release Major 1
Objetivo: Entregar a fundação funcional e técnica necessária para o fluxo inicial do produto.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.1.1 | Ambientes e Repositórios Configuráveis | Repositórios configurados com políticas de contribuição, templates, código de conduta e versionamento. |
| 1.4.1.2 | Pipelines de CI/CD | Rotinas automatizadas de lint, build, testes iniciais, integração com SonarCloud e coleta de métricas. |
| 1.4.1.3 | Módulo de Autenticação e Perfis | Sistema de login, cadastro inicial de usuários e controle de acesso por perfil. |
| 1.4.1.4 | Requisitos e Termos de Privacidade (LGPD) | Funcionalidades iniciais de privacidade, controle de acesso, rastreabilidade e proteção de dados sensíveis. |

##### 1.4.2 R2_MVP — Entrega do MVP
Objetivo: Entregar o fluxo essencial do usuário contendo o processamento de imagens e buscas de exames.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.2.1 | Módulo de Pré-processamento de Imagens | Funcionalidade responsável pelo tratamento das imagens antes da inferência. |
| 1.4.2.2 | Serviço de Comunicação com IA | Interface de comunicação (integração) entre o sistema e o serviço/modelo de IA. |
| 1.4.2.3 | Módulo de Interpretação de Resultados | Sistema de tratamento da resposta da IA para formato legível e utilizável na aplicação. |
| 1.4.2.4 | Módulo de Associação Resultado-Exame | Estrutura de vinculação do resultado processado ao exame correspondente. |
| 1.4.2.5 | Módulo de Histórico e Consulta | Interface de consulta de exames processados, incluindo busca e filtros básicos. |

##### 1.4.3 R3 — Consolidação Final do Produto
Objetivo: Entregar o produto consolidado com avaliações especializadas, logs de auditoria e segurança avançada.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.3.1 | Módulo de Avaliação por Especialista | Criação de novo perfil de usuário (Oftalmologista) e funcionalidade para inserção e emissão de laudo médico especializado. |
| 1.4.3.2 | Módulo de Preenchimento Automático via DICOM | Funcionalidade que consome os metadados clínicos extraídos das imagens Eyer 2 para auto-completar formulários de exames. |
| 1.4.3.3 | Módulo de Reporte de Inconsistências da IA | Interface para registro e feedback de erros ou discordâncias gerados pelo modelo no diagnóstico. |
| 1.4.3.4 | Sistema de Auditoria e Logs | Infraestrutura de logs para rastreabilidade de ações críticas dos usuários no sistema. |
| 1.4.3.5 | Módulo Estendido de Autenticação | Funcionalidades de recuperação de senha segura e formulário de inscrição via e-mail. |
| 1.4.3.6 | Módulo de Relatórios e Compartilhamento Seguro | Download avançado e funcionalidade de compartilhamento controlado de relatórios via link. |
| 1.4.3.7 | Suíte de Testes Automatizados | Conjunto ampliado de testes unitários, integração, funcionais e relatório final de cobertura de código. |

##### 1.4.4 RM6 — Estabilização de Código
Objetivo: Entregar o repositório final estabilizado e documentado após avaliações.

| Código | Pacote de Trabalho | Descrição |
| :---: | :--- | :--- |
| 1.4.4.1 | Pacote de Ajustes Pós-Apresentação | Implementação de correções e melhorias identificadas na avaliação da R3. |
| 1.4.4.2 | Repositórios Ajustados | Repositórios com pendências (Issues e PRs) finalizadas e organizadas para a entrega final. |

---

## Observação de Rastreabilidade

A EAP apresenta a decomposição do escopo em entregas verificáveis. A rastreabilidade detalhada entre pacotes de trabalho, histórias, critérios de aceitação, responsáveis e PRs deve ser mantida no ZenHub/GitHub.

---

## Política de Atualização

Este documento deve ser atualizado somente quando houver mudança estrutural no escopo das releases.

Alterações operacionais de sprint, status, responsáveis, issues ou PRs não devem ser duplicadas neste documento.

## Referências

> [1] Project Management Institute. A Guide to the Project Management Body of Knowledge (PMBOK Guide). 7. ed. Newtown Square: PMI, 2021. Disponível em:https://www.pmi.org/pmbok-guide-standards/foundational/pmbok

## Histórico de Versão

| Versão | Data       | Descrição            | Autor                                      | Revisor      |
| :----: | ---------- | -------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/ericcs10) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.1`  | 20/04/2026 | Alinhamento da EAP com milestones, sprints e entregas do roadmap do produto | [Zenilda Vieira](https://github.com/zenildavieira) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.2`  | 20/04/2026 | Consolidação dos blocos 1.1, 1.2 e 1.3 dentro de 1.4 e 1.5 para remover redundâncias | [Zenilda Vieira](https://github.com/zenildavieira) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.3` | 02/05/2026 | Alterações de acordo com o Feedback do professor e adição do diagrama | [André Maia](https://github.com/andre-maia51) | - |
| `1.4` | 01/06/2026 | Alteração da EAP e do diagrama seguindo as orientações da R2 | [André Maia](https://github.com/andre-maia51) | - | 
