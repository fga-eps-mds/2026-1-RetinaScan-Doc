# RetinaScan

O RetinaScan é uma solução de apoio à análise de exames oftalmológicos, com foco em organizar o fluxo clínico e integrar processamento de imagens com IA para suporte à decisão médica.

## Objetivo

Desenvolver uma plataforma que permita:
- cadastro e autenticação de usuários com controle de acesso;
- registro de exames com imagens oftalmológicas;
- processamento assíncrono de inferência com IA;
- consulta de histórico e resultados para acompanhamento clínico.

## Escopo do MVP

- autenticação e gestão básica de usuários;
- cadastro de exames e upload de imagens;
- integração com serviço de inferência;
- visualização de histórico e resultados.

## Visão técnica resumida

A solução utiliza uma arquitetura com serviços desacoplados, incluindo:
- backend principal para regras de negócio;
- serviço de inferência para processamento de IA;
- persistência relacional para dados transacionais;
- armazenamento de objetos para imagens.

Detalhes técnicos completos em [Arquitetura](docs/projeto/arquitetura.md).

## Documentação

- Visão geral: [Index da documentação](docs/index.md)
- Arquitetura: [Arquitetura](docs/projeto/arquitetura.md)
- Modelagem do banco: [Modelagem do Banco de Dados](docs/projeto/modelagem-do-BD.md)
- EAP: [EAP](docs/projeto/EAP.md)
- Backlog do produto: [Backlog do Produto](docs/produto/backlog-do-produto.md)
- Roadmap: [Roadmap do Produto](docs/planejamento/roadmap-do-produto.md)
- Políticas de contribuição:
  - [Política de Branches](docs/guia_de_contribuicao/politica-de-branches.md)
  - [Política de Commits](docs/guia_de_contribuicao/politica-de-commits.md)

## Equipe

A composição da equipe está disponível em [docs/index.md](docs/index.md).