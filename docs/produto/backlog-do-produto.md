# Backlog do Produto

## Objetivo do Documento

Este documento funciona como referência de produto e rastreabilidade.
Detalhes operacionais (prioridade, critérios de aceitação, status, responsáveis e discussões técnicas) são mantidos exclusivamente no ZenHub/GitHub para evitar duplicação de documentação.

## Fontes Oficiais

### Workspace principal (ZenHub)

- Board oficial do time: [ZenHub Workspace](https://github.com/fga-eps-mds/2026-1-retinascan-doc/issues#workspaces/20261-fcte-fm-01-69bd9cee544e2d00306abb69/board)

### Repositórios do Produto

- API: [2026-1-RetinaScan-Api](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues)
- Web: [2026-1-RetinaScan-Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues)
- IA: [2026-1-RetinaScan-AI](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/issues)
- Documentação: [2026-1-RetinaScan-Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues)

## Estrutura de Escopo do Produto

| Épico | Objetivo |
| :--- | :--- |
| Autenticação e Controle de Acesso | Garantir acesso seguro ao sistema, perfis de usuário e rastreabilidade de ações. |
| Cadastro e Upload de Exames | Registrar exames e permitir envio de imagens para processamento. |
| Histórico e Consulta | Permitir consulta, busca e filtros sobre exames processados. |
| Processamento e IA | Integrar pipeline de inferência e tratamento de resultados da IA. |
| Relatórios e Métricas | Disponibilizar visualização, exportação e compartilhamento de resultados. |

## Relação com Releases

- R1: foco em autenticação, cadastro/upload e processamento inicial de IA.
- R2: consolidação de histórico, busca e filtros.
- R3: evoluções de relatórios, métricas e compartilhamento.

A distribuição detalhada de issues por release deve ser consultada diretamente no ZenHub.

## Como encontrar as informações no ZenHub

| Item de avaliação | Onde encontrar | Link de referência |
| :--- | :--- | :--- |
| Backlog priorizado | Board do workspace, com ordenação por pipeline e sprint atual | [ZenHub Workspace](https://github.com/fga-eps-mds/2026-1-retinascan-doc/issues#workspaces/20261-fcte-fm-01-69bd9cee544e2d00306abb69/board) |
| Histórias com critérios de aceitação | Issue correspondente no GitHub/ZenHub (descrição e checklist) | [Issues API](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues), [Issues Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues), [Issues IA](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/issues), [Issues Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues) |
| Escopo por release (Release x US) | Milestones e issues vinculadas | [Milestones API](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/milestones), [Milestones Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/milestones), [Milestones IA](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/milestones), [Milestones Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/milestones) |
| Defeitos e mudanças corrigidos | Labels no board/issues (ex.: bug, duplicate, enhancement) e histórico de PRs | [Issues API (labels)](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/issues?q=is%3Aissue%20label%3Abug%2Cduplicate%2Cenhancement), [Issues Web (labels)](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/issues?q=is%3Aissue%20label%3Abug%2Cduplicate%2Cenhancement), [Issues IA (labels)](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/issues?q=is%3Aissue%20label%3Abug%2Cduplicate%2Cenhancement), [Issues Doc (labels)](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/issues?q=is%3Aissue%20label%3Abug%2Cduplicate%2Cenhancement) |
| Evidências de implementação | PRs vinculados às issues | [PRs API](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api/pulls?q=is%3Apr), [PRs Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web/pulls?q=is%3Apr), [PRs IA](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/pulls?q=is%3Apr), [PRs Doc](https://github.com/fga-eps-mds/2026-1-RetinaScan-Doc/pulls?q=is%3Apr) |
| Andamento da sprint | Colunas do board e burndown do workspace | [ZenHub Workspace](https://github.com/fga-eps-mds/2026-1-retinascan-doc/issues#workspaces/20261-fcte-fm-01-69bd9cee544e2d00306abb69/board) |

## Fluxo de Consulta Rápida

1. Localize o épico no board.
2. Abra a issue da história correspondente.
3. Valide os critérios de aceitação na descrição/checklist.
4. Confira milestone/release associada à issue.
5. Abra PRs vinculados para evidência de execução.
6. Em caso de defeitos ou mudança, filtre por labels de bug/duplicate/enhancement.

## Evidências Complementares Fora do ZenHub

Para itens da R1 que não vivem exclusivamente no board, utilize os documentos e artefatos abaixo:

| Evidência | Onde encontrar |
| :--- | :--- |
| Visão do produto e delimitação de escopo | [Lean Inception](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/lean-inception/) |
| Canvas MVP | [Canvas MVP](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/canvas-mvp/) |
| Protótipo de alta fidelidade (Figma) | [Protótipo de Alta Fidelidade](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/produto/prototipo-de-alta/) |
| Arquitetura (4+1) | [Arquitetura](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/projeto/arquitetura/) |
| Modelagem de dados | [Modelagem do Banco de Dados](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/projeto/modelagem-do-BD/) |
| Planejamento de riscos | [Plano de Gestão de Riscos](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/planejamento/plano_de_ger_riscos/) |
| Planejamento de custos | [Plano de Custos](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/planejamento/plano_de_custos/) |
| Roadmap | [Roadmap do Produto](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/planejamento/roadmap-do-produto/) |
| Portal da documentação do projeto | [GitHub Pages - RetinaScan Doc](https://fga-eps-mds.github.io/2026-1-RetinaScan-Doc/) |
| Repositórios de desenvolvimento (API, Web, IA) | [2026-1-RetinaScan-Api](https://github.com/fga-eps-mds/2026-1-RetinaScan-Api), [2026-1-RetinaScan-Web](https://github.com/fga-eps-mds/2026-1-RetinaScan-Web), [2026-1-RetinaScan-AI](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI) |



## Política de Atualização deste Documento

Este arquivo deve ser atualizado somente quando houver mudança estrutural de escopo (ex.: criação, fusão ou remoção de épicos).
Não é necessário atualizar este documento a cada alteração operacional no ZenHub.

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0` | 12/04/2026 | Criação do documento | [Natália De Morais](https://github.com/Natyrodrigues) | ---- |
| `1.1` | 26/04/2026 | Reestruturação para documento de referência com rastreabilidade ao ZenHub | [Zenilda Vieira](https://github.com/ZenildaVieira) e GitHub Copilot | ---- |
