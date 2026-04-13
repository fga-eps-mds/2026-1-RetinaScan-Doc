# Metodologias

## Introdução

Este documento descreve as metodologias e práticas de desenvolvimento de software adotadas pela equipe do projeto RetinaScan ao longo do semestre. A escolha das abordagens foi orientada pelo contexto acadêmico da disciplina de EPS (Engenharia de Produto de Software) e pelas necessidades do projeto, que envolve equipe distribuída, prazo semestral definido e entregas incrementais validadas com o Product Owner.

A combinação de metodologias ágeis escolhida visa equilibrar organização, flexibilidade e qualidade, permitindo que a equipe responda a mudanças de requisitos, gerencie riscos e entregue valor de forma contínua.

---

## Lean Inception

O projeto foi iniciado com a aplicação do **Lean Inception**, framework criado por Paulo Caroli que combina o *Design Thinking* com o *Lean Startup* para alinhar equipe e stakeholders antes do início do desenvolvimento. O processo foi conduzido de forma assíncrona, com grupos de 3 a 4 integrantes trabalhando em paralelo e realizando validações cruzadas ao final de cada etapa.

As principais atividades realizadas durante o Lean Inception do RetinaScan foram:

- Definição da visão do produto e objetivos de negócio;
- Levantamento de personas e jornadas de usuário;
- Brainstorming de funcionalidades;
- Revisão técnica, de negócio e de UX de cada funcionalidade;
- Construção do Sequenciador;
- Definição do MVP (Produto Mínimo Viável).

O resultado do Lean Inception orientou diretamente a estruturação do Backlog do Produto e a priorização das entregas.

---

## Scrum

A equipe adota o **Scrum** como framework principal de gestão do desenvolvimento. O Scrum organiza o trabalho em ciclos de tempo fixo chamados **Sprints**, permitindo entregas incrementais e inspeções regulares do progresso.

### Papéis

| Papel | Descrição |
| :--- | :--- |
| Product Owner (PO) | Responsável por representar os interesses do cliente, priorizar o backlog e validar as entregas. |
| Scrum Master | Responsável por facilitar os ritos do Scrum, remover impedimentos e garantir que a equipe siga as práticas definidas. |
| Time de Desenvolvimento | Conjunto de membros responsáveis pelo planejamento, execução e entrega das funcionalidades a cada Sprint. |

### Ritos

| Rito | Descrição |
| :--- | :--- |
| Sprint Planning | Reunião de planejamento realizada no início de cada Sprint para definir as issues que serão desenvolvidas no ciclo. |
| Sprint Review | Revisão ao final de cada Sprint para apresentar o que foi entregue e coletar feedback do Product Owner. |
| Sprint Retrospective | Cerimônia interna de reflexão sobre o processo, identificando pontos de melhoria para o próximo ciclo. |
| Daily Standup | Sincronização diária assíncrona entre os membros para alinhamento de progresso, bloqueios e próximos passos. |

### Sprints

As Sprints do projeto têm duração semanal, alinhadas ao calendário da disciplina de EPS. O acompanhamento das tarefas é realizado via **ZenHub**, integrado ao GitHub, onde o backlog, as Sprints ativas e o progresso de cada issue são monitorados pelo time.

### Dupla de Líderes Rotativos

Como adaptação ao Scrum tradicional, a equipe adota a prática de **rodízio de lideranças por quinzena**. Em cada quinzena, os membros definidos conduzem as cerimônias, acompanham o progresso das tarefas e apoiam na remoção de impedimentos. Essa rotatividade garante que todos desenvolvam habilidades de liderança e gestão ao longo do semestre.

A tabela abaixo apresenta o rodízio de lideranças definido para o projeto:

| Quinzena | Período | Evento(s) | Dupla de Líderes |
| :------: | :-------------------: | :-------------------------- | :---------------- |
| 1ª | 30/03 a 12/04/2026 | RM1 (13/04) | [Gustavo Costa](https://github.com/cwtshh) e [Iderlan Junio](https://github.com/IderlanJ) |
| 2ª | 13/04 a 26/04/2026 | R1 (27/04) | [Natália Rodrigues](https://github.com/Natyrodrigues) e [André Maia](https://github.com/andre-maia51) |
| 3ª | 27/04 a 10/05/2026 | RM2 (04/05) e RM3 (11/05) | [Zenilda Vieira](https://github.com/ZenildaVieira) e [Cecília Quaresma](https://github.com/cqcoding) |
| 4ª | 11/05 a 24/05/2026 | R2 (25/05) | [Elias Oliveira](https://github.com/EliasOliver21) e [Yan Luca](https://github.com/yan-luca) |
| 5ª | 25/05 a 07/06/2026 | RM4 (01/06) | [Eric Camargo](https://github.com/Ericcs10) e [Harleny Angélica](https://github.com/Angelicahaas) |
| 6ª | 08/06 a 21/06/2026 | RM5 (15/06) | [Arthur Ribeiro](https://github.com/artrsousa1) e [Vinícius Roriz](https://github.com/vnsrz) |
| 7ª | 22/06 a 05/07/2026 | R3 (29/06) e RM6 (06/07) | A definir |

**Fonte:** Equipe RetinaScan, 2026.

---

## Kanban

Em complemento ao Scrum, a equipe utiliza o **Kanban** como prática de visualização e controle do fluxo de trabalho. O board do ZenHub, integrado ao GitHub, funciona como o quadro Kanban do projeto, organizando as issues em colunas que representam os estados do fluxo — como *To Do*, *In Progress* e *Done* — permitindo que toda a equipe acompanhe o andamento das tarefas em tempo real e identifique gargalos rapidamente.

---

## Práticas de XP (Extreme Programming)

Embora o time não adote o XP de forma integral, algumas de suas práticas técnicas estão presentes de maneira natural no processo de desenvolvimento do RetinaScan, contribuindo para a qualidade e a sustentabilidade do código:

- **Integração Contínua (CI):** O repositório utiliza GitHub Actions para execução automatizada de pipelines de integração, garantindo que cada contribuição seja validada antes de ser incorporada à branch principal.
- **Revisão de código:** Todo código desenvolvido passa por revisão de outro membro da equipe por meio de *Pull Requests*, antes de ser integrado ao repositório.
- **Padronização:** A equipe adota políticas de commits e branches definidas no Guia de Contribuição, garantindo rastreabilidade e consistência no histórico do repositório.
- **Testes automatizados:** A estrutura do projeto prevê camadas de testes unitários e de integração para validar o comportamento das funcionalidades ao longo do desenvolvimento.

Essas práticas, mesmo que não formalmente rotuladas como XP pela equipe, reforçam os princípios de feedback rápido, qualidade contínua e colaboração técnica que caracterizam a metodologia.

---

## Políticas do Repositório

Para garantir a organização e a rastreabilidade do trabalho, a equipe segue políticas documentadas no Guia de Contribuição:

- **Política de Branches:** Define o padrão de nomenclatura e o fluxo de criação de branches para cada tipo de contribuição (features, correções, documentação).
- **Política de Commits:** Estabelece o formato das mensagens de commit, baseado em convenções que facilitam a leitura do histórico e a geração de changelogs.

---

## Comunicação e Alinhamento

A equipe utiliza ferramentas distintas para cada nível de comunicação:

- **Discord e WhatsApp:** Comunicação rápida e informal entre os membros para alinhamentos operacionais do dia a dia.
- **Microsoft Teams:** Realização de reuniões formais com o Product Owner e demais stakeholders.
- **Google Docs e Google Planilhas:** Construção colaborativa de artefatos e controle de planejamento.
- **When2meet:** Levantamento de disponibilidade da equipe para agendamento de cerimônias e reuniões.

---

## Histórico de Versão

| Versão | Data       | Descrição                                      | Autor                                      | Revisor      |
| :----: | ---------- | ---------------------------------------------- | ------------------------------------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do documento                           | [Eric Camargo](https://github.com/ericcs10) | [xxxx](xxxx) |