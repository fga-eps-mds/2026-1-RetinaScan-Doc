# Roadmap do Produto

## Objetivo do Documento

Este documento apresenta a visão macro de evolução do produto RetinaScan ao longo das releases do semestre.

O Roadmap funciona como referência estratégica de planejamento, conectando Lean Inception, MVP, releases e milestones. Detalhes operacionais como issues, responsáveis, status, critérios de aceitação, PRs e andamento de sprint devem ser consultados diretamente no ZenHub/GitHub, evitando duplicação de documentação.

## Fontes Oficiais

### Workspace Principal

- Board oficial do time: [ZenHub Workspace](https://github.com/fga-eps-mds/2026-1-retinascan-doc/issues#workspaces/20261-fcte-fm-01-69bd9cee544e2d00306abb69/board)

### Repositórios do Produto

- API: [2026-1-RetinaScan-Api](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api)
- Web: [2026-1-RetinaScan-Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web)
- IA: [2026-1-RetinaScan-AI](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI)
- Documentação: [2026-1-RetinaScan-Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc)

## Relação com o Planejamento do Produto

O roadmap foi definido a partir dos artefatos de produto e planejamento:

| Artefato | Finalidade |
| :--- | :--- |
| [Lean Inception](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/lean-inception/) | Origem da visão do produto, personas, funcionalidades e sequenciamento |
| [Canvas MVP](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/canvas-mvp/) | Definição do recorte mínimo de valor |
| [Backlog do Produto](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/backlog-do-produto/) | Estrutura de épicos e rastreabilidade para as histórias no ZenHub |
| [Protótipo de Alta Fidelidade](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/prototipo-de-alta/) | Evidência visual dos fluxos priorizados |
| [Plano de Custos](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/planejamento/plano_de_custos/) | Planejamento de custo por release |
| [Plano de Riscos](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/planejamento/plano_de_ger_riscos/) | Riscos associados ao escopo e entregas |

## Visão Geral das Releases

| Release | Data prevista | Foco principal | Resultado esperado |
| :--- | :---: | :--- | :--- |
| RM1 | 13/04/2026 | Estruturação inicial do projeto | Repositórios configurados, documentação base e primeira entrega técnica |
| R1 | 27/04/2026 | Fundação funcional do produto | Autenticação, cadastro/upload de exames e preparação para integração com IA |
| RM2 / RM3 | 04/05 e 11/05/2026 | Evolução do processamento | Primeiros incrementos relacionados ao pipeline de IA |
| R2_MVP | 25/05/2026 | Entrega do MVP funcional | Fluxo principal validável: exame, imagem, processamento e consulta inicial |
| RM4 / RM5 | 01/06 e 15/06/2026 | Refinamento e estabilização | Melhorias em histórico, relatórios, qualidade e testes |
| R3 | 29/06/2026 | Consolidação final | Produto completo conforme escopo planejado |
| RM6 | 06/07/2026 | Encerramento | Correções finais, documentação e lições aprendidas |

## Escopo Macro por Release

### RM1 — Estruturação Inicial

Objetivo: preparar a base do projeto para desenvolvimento e acompanhamento.

Escopo macro:
- configuração dos repositórios;
- documentação inicial de contribuição, metodologia e planejamento;
- definição do backlog inicial;
- primeira entrega técnica de autenticação/administração;
- alinhamento inicial com Product Owner.

### R1 — Primeira Release Principal

Objetivo: entregar a base funcional necessária para o fluxo principal do produto.

Escopo macro:
- autenticação e controle de acesso;
- cadastro inicial de usuários;
- início do cadastro de exames;
- upload de imagens;
- consolidação do protótipo de alta fidelidade dos fluxos priorizados;
- refinamento dos artefatos de planejamento da release.

Marco esperado:

### RM2 / RM3 — Evolução do Processamento

Objetivo: iniciar a integração entre o produto e o pipeline de IA.

Escopo macro:
- pré-processamento de imagens;
- integração inicial com o modelo de IA;
- recebimento e interpretação preliminar do resultado;
- tratamento inicial de erros no pipeline.

### R2_MVP — Entrega do MVP

Objetivo: entregar o menor produto validável com valor para o usuário.

Escopo macro:
- cadastro de exame;
- upload de imagem;
- processamento por IA;
- associação do resultado ao exame;
- consulta inicial do histórico;
- mecanismos básicos de revisão/erro.

Marco esperado:

> O MVP deve permitir validar o fluxo essencial do RetinaScan: registrar exame, enviar imagem, processar por IA e consultar o resultado.

### RM4 / RM5 — Refinamento e Estabilização

Objetivo: melhorar a experiência, ampliar a qualidade e estabilizar o produto.

Escopo macro:
- evolução do histórico e consulta;
- refinamento de busca e visualização;
- relatórios e métricas;
- melhorias no pipeline de IA;
- ampliação de testes;
- correção de defeitos.

### R3 — Consolidação Final

Objetivo: concluir o produto planejado para o semestre.

Escopo macro:
- estabilização das funcionalidades principais;
- validação final do fluxo com IA;
- revisão final da documentação;
- preparação da apresentação final;
- consolidação das evidências de entrega.

### RM6 — Encerramento

Objetivo: realizar ajustes finais após a apresentação e encerrar o projeto.

Escopo macro:
- correções pós-apresentação;
- fechamento das issues pendentes;
- organização final dos repositórios;
- registro de lições aprendidas.

## Linha do Tempo Resumida

| Período | Sprint | Marco | Foco |
| :---: | :---: | :---: | :--- |
| 23/03 – 30/03 | - | Iniciação | Lean Inception e definição inicial do MVP |
| 30/03 – 13/04 | S1 | RM1 | Estruturação do projeto e documentação base |
| 13/04 – 27/04 | S2–S3 | R1 | Autenticação, cadastro/upload e preparação do fluxo principal |
| 27/04 – 11/05 | S4–S5 | RM2/RM3 | Integração inicial com IA |
| 11/05 – 25/05 | S6–S7 | R2_MVP | Entrega do MVP funcional |
| 25/05 – 15/06 | S8–S9 | RM4/RM5 | Relatórios, refinamentos, testes e estabilização |
| 15/06 – 29/06 | S10–S11 | R3 | Consolidação final do produto |
| 29/06 – 06/07 | S12 | RM6 | Encerramento e ajustes finais |

## Como Consultar o Detalhamento Operacional

| Informação | Onde consultar |
| :--- | :--- |
| Issues por sprint | ZenHub Workspace |
| Histórias vinculadas às releases | Milestones dos repositórios |
| Status das entregas | Board do ZenHub |
| Critérios de aceitação | Descrição/checklist das issues |
| Responsáveis | Assignees nas issues |
| Evidências de implementação | Pull Requests vinculados |
| Defeitos e mudanças | Labels `bug`, `enhancement`, `duplicate` |
| Burndown e progresso | Relatórios do ZenHub |
| Planejado × realizado | Dashboard Gerencial e Analítico |

## Relação com Milestones

As milestones oficiais devem ser mantidas nos repositórios do GitHub/ZenHub. Este documento apenas resume a intenção de cada marco.

| Item | Fonte oficial |
| :--- | :--- |
| Milestones API | [Milestones API](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/milestones) |
| Milestones Web | [Milestones Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/milestones) |
| Milestones IA | [Milestones IA](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/milestones) |
| Milestones Doc | [Milestones Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/milestones) |

## Observações de Escopo

Para manter o roadmap adequado ao tamanho do time e às observações de avaliação:

- o MVP deve priorizar o fluxo essencial de valor;
- funcionalidades auxiliares não devem inflar o escopo da R1;
- filtros, ordenações e buscas devem ser tratados como parte de fluxos maiores de consulta;
- protótipos devem estar relacionados às histórias priorizadas;
- requisitos relacionados à LGPD e criptografia devem aparecer nas histórias e critérios de aceitação correspondentes;
- mudanças de escopo devem ser registradas no ZenHub/GitHub, não duplicadas neste documento.

## Política de Atualização

Este documento deve ser atualizado apenas quando houver mudança estrutural no planejamento do produto, como:

- alteração de releases;
- mudança relevante no escopo macro;
- redefinição do MVP;
- criação, fusão ou remoção de milestones;
- alteração significativa na estratégia de entrega.

Mudanças operacionais de sprint, status de issue, responsáveis, PRs e critérios de aceitação devem permanecer exclusivamente no ZenHub/GitHub.

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0` | 12/04/2026 | Criação do documento | [Eric Camargo](https://github.com/Ericcs10) | [Zenilda Vieira](https://github.com/zenildavieira) |
| `1.1` | 19/04/2026 | Acréscimo das milestones | [Zenilda Vieira](https://github.com/zenildavieira) | ---- |
| `1.2` | 20/04/2026 | Ajustes com base nas issues dos repositórios Doc, API, Web e IA | [Zenilda Vieira](https://github.com/zenildavieira) | ---- |
| `1.3` | 26/04/2026 | Reestruturação como documento de referência, evitando duplicação do ZenHub/GitHub | [Zenilda Vieira](https://github.com/zenildavieira) e GitHub Copilot | ---- |