# Metodologia Aplicada no RetinaScan

## Introdução

Este documento descreve **como o time do RetinaScan aplica metodologias e práticas no desenvolvimento real do projeto**, não apenas definições teóricas. A metodologia é o **uso dos métodos** no contexto da equipe, prazos, stakeholders e restrições acadêmicas.

A combinação escolhida visa equilibrar organização, flexibilidade e qualidade, permitindo que a equipe responda a mudanças de requisitos, gerencie riscos e entregue valor incrementalmente a cada semana.

---

## Ciclo de Desenvolvimento: Da Visão ao Produto

### 1. Lean Inception

**O que fazemos:** Antes de qualquer código, a equipe passa por Lean Inception para alinhar visão, stakeholders e escopo com base em Design Thinking + Lean Startup.

**Como na prática:**
- Equipe dividida em grupos de 3-4 pessoas trabalhando em paralelo
- Cada grupo executa uma atividade do framework (Visão, Personas, Jornadas, Brainstorming, Revisões)
- Validações cruzadas ao final de cada etapa garantem consenso
- Resultado: Canvas MVP validado, backlog priorizado, roadmap de releases (R1, R2_MVP, R3)
- **Entrega:** Lean Inception completo, Backlog de Produto no ZenHub, Roadmap documentado

**Impacto:** Define escopo, prioridades e critérios de sucesso. Sem Lean Inception clara, sprints carecem de direção.

---

### 2. Scrum Adaptado: Estrutura Semanal

**O que fazemos:** Organizamos o desenvolvimento em ciclos de **1 semana (Sprint)**, com cerimônias no mesmo dia (segunda-feira, horário da aula).

#### Papéis

| Papel | Responsabilidade |
|-------|---|
| **Product Owner (PO)** | Representa cliente, valida entregas, ajusta prioridades conforme feedback |
| **Scrum Master** (dupla) | Facilita ritos, remove bloqueios, protege equipe de interrupções |
| **Time de Desenvolvimento** | Planeja, executa, entrega incrementos de software |

#### Estrutura da Sprint

**Segunda-feira (Manhã/Horário aula):**

1. **Sprint Review** (30-45 min)
   - Time apresenta o que foi entregue na sprint anterior
   - Time discute como será a entrega para o PO na reunião à noite
   

2. **Sprint Retrospective** (20-30 min)
   - Time reflete: "O que funcionou? O que melhorar?"
   - Identifica pontos de melhoria no processo (ferramentas, comunicação, estimativas)
   - Define 1-2 ações de melhoria para próxima sprint

3. **Sprint Planning** (30-45 min)
   - Time olha backlog priorizado e define o que cabe na sprint
   - Issues são estimadas, tarefas são quebradas, responsáveis são designados
   - Compromisso: O que sai dessa reunião será desenvolvido na semana

**Terça a Domingo:**
- Desenvolvimento contínuo
- Daily (assíncrono no WhatsApp): Status, bloqueios, próximos passos
- PRs são abertos, revisados e mergeados
- Bugs encontrados entram na sprint como "Defeitos" de alta prioridade

**Segunda-feira (Noite, 19h30-20h30):**
- **Sprint Review com PO** no Teams: 
  - Validação formal da entrega com cliente
  - PO valida, aprova ou solicita ajustes
  - Feedback é capturado para próximas prioridades
  - Critérios de aceitação da próxima sprint são apresentados e validados

---

### 3. Kanban: Fluxo Visual de Trabalho

**O que fazemos:** Complementar Scrum com Kanban para visualizar e otimizar o fluxo em tempo real.

**Como na prática:**
- ZenHub integrado ao GitHub funciona como quadro Kanban
- Colunas: **To Do** → **In Progress** → **In Review** → **Done**
- Toda issue tem: título claro, descrição, critérios de aceitação, responsável, labels (feature/bug/tech-debt)
- Daily: equipe monitora se há gargalos, PRs travados em review ou issues bloqueadas
- **Resultado:** Visibilidade total do andamento, identificação rápida de problemas

**Impacto:** Transparência contínua reduz surpresas no Friday e Friday Sprint Planning.

---

### 4. Liderança Rotativa por Quinzena

**O que fazemos:** Ao invés de PM/Scrum Master fixo, rodamos liderança a cada 2 semanas.

**Como na prática:**
- Dupla de líderes: conduzem cerimônias, acompanham progresso, resolvem bloqueios
- Todos desenvolvem experiência de liderança e gestão
- Registram decisões, impedimentos e métricas nas atas de reunião
- Transição suave de conhecimento entre duplas

| Quinzena | Período | Release | Dupla de Líderes |
|----------|---------|---------|---|
| 1ª | 30/03-13/04 | RM1 (13/04) | [Gustavo Costa](https://github.com/cwtshh) e [Iderlan Junio](https://github.com/IderlanJ) |
| 2ª | 13/04-27/04 | **R1 (27/04)** | [Natália Rodrigues](https://github.com/Natyrodrigues) e [André Maia](https://github.com/andre-maia51)|
| 3ª | 27/04-11/05 | RM2 (04/05), RM3 (11/05) | [Harleny Angélica](https://github.com/Angelicahaas) e [Cecília Quaresma](https://github.com/cqcoding) |
| 4ª | 11/05-25/05 |**R2_MVP (25/05)** | [Elias Oliveira](https://github.com/EliasOliver21) e [Yan Luca](https://github.com/yan-luca) |
| 5ª | 25/05-08/06 | RM4 (01/06) | [Eric Camargo](https://github.com/Ericcs10) |
| 6ª | 08/06-22/06 | RM5 (15/06) | [Arthur Ribeiro](https://github.com/artrsousa1) e [Vinícius Roriz](https://github.com/vnsrz) |
| 7ª | 22/06-06/07 | **R3 (29/06)**, RM6 (06/07) | A definir |

**Impacto:** Distribui responsabilidade, desenvolve liderança, reduz dependência de um indivíduo.


---

## Integração Contínua (CI) e Práticas XP

**O que fazemos:** Garantir qualidade através de feedback rápido e automação.

### Práticas Implementadas

| Prática | Como Aplicamos |
|---------|---|
| **Integração Contínua** | Cada PR dispara pipeline no GitHub Actions: lint, build, testes unitários, cobertura |
| **Revisão de Código** | Todo código passa por revisão obrigatória antes de merge via PR. Rejeições são feedback construtivo |
| **Testes Automatizados** | Cobertura ≥85% em código novo. Testes rodam no pipeline; falha = bloqueio de merge |
| **Padronização** | Política de Commits (mensagens semânticas) e Política de Branches (feature/*, bugfix/*, etc) |
| **Build Contínuo** | Repositório compilável a todo momento. Artefatos (binários, .json de métricas) são gerados automaticamente |

### Fluxo PR Típico

1. Dev cria branch local (`git checkout -b feature/US123-descricao`)
2. Dev commita com mensagem semântica (`feat: implementa autenticação`)
3. Dev abre PR no GitHub para a branch `develop`
4. **Pipeline roda automaticamente:** lint → build → testes → cobertura → SonarCloud
5. Reviewer executa: checkout da branch, roda localmente, verifica lógica e padrão
6. Se OK: aprovação e merge
7. Se problema: solicita mudanças com comentários
8. Dev ajusta, novo commit, pipeline roda novamente


**Impacto:** Qualidade garantida, histórico limpo, rastreabilidade total.

---

## Políticas de Repositório

**O que fazemos:** Documentar e enforçar regras para manter repositório consistente e rastreável.

### Política de Branches

```
main          → código em produção/homologação (protegida, requer PR)
develop       → integração contínua (staging para releases)
feature/*     → novas funcionalidades (feature/US123-descricao-curta)
bugfix/*      → correções (bugfix/DEF456-problema)
docs/*        → documentação (docs/diagramas-arquitetura)
chore/*       → tarefas técnicas (chore/atualizar-dependencias)
```

**Regra:** Ninguém faz commit direto em main ou develop. Sempre via PR.

### Política de Commits

```
feat:     Novo recurso (feature/história de usuário)
fix:      Correção de bug
docs:     Documentação apenas
style:    Formatação, sem mudança lógica
refactor: Reescrita sem mudança comportamental
test:     Adição/ajuste de testes
chore:    Atualizações de dependência, config, build
```

**Exemplo:** `feat: implementa autenticação com better-auth`

**Impacto:** Changelog automático, histórico legível, blame funciona bem.

---

## Métricas e Monitoramento de Progresso

**O que fazemos:** Coletar dados continuamente para avaliar saúde do projeto.

### Métricas Capturadas

| Métrica | Ferramenta | Frequência | Uso |
|---------|-----------|-----------|-----|
| **Cobertura de Testes** | SonarCloud | Por PR | Garantir ≥85% em código novo |
| **Qualidade de Código** | SonarCloud | Por PR | Debt, duplicação, vulnerabilidades |
| **Velocidade da Sprint** | ZenHub | Weekly | Story points entregues vs. planejado |
| **Burndown** | ZenHub | Daily | Visual do progresso semana |
| **EVM-Ágil** | Planilha Google | Weekly | VP, VA, CPI, SPI |
| **Distribuição de Issues** | ZenHub | Weekly | Carga por membro |
| **Risco** | Matriz de Risco | Weekly | Eventos críticos monitorados |

### Decisões Baseadas em Dados

Exemplos de decisões documentadas:
- Mudança de ORM por performance (análise de query times no SonarCloud)
- Alocação de débito técnico na sprint (risk matrix mostrava refactor como crítico)
- Escalonamento de bug crítico (burndown mostrava desvio de -30% na sprint)

**Impacto:** Decisões gerenciais são baseadas em evidências.

---

## Adaptações e Lições Aprendidas

**O que fazemos:** A metodologia não é rígida. Adaptamos conforme experiência.

**Impacto:** Metodologia melhora continuamente, não é dogma.

---

## Resumo: Como o RetinaScan "Faz" Metodologia

```
Semana de Aula
├─ Segunda (Manhã): Review + Retro + Planning
├─ Terça-Domingo: Dev contínuo + PRs + Testes
├─ Diário: Sync assíncrona no WhatsApp
└─ Segunda (Noite, 19h30): Review com PO

Contínuo
├─ Kanban no ZenHub
├─ Pipeline CI/CD no GitHub Actions
├─ Métricas no SonarCloud
└─ EVM-Ágil na Planilha Google

Resultado
└─ Entrega semanal de valor, qualidade garantida, equipe engajada
```

---

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
|:----:|------|----------|-------|---------|
| `1.0`  | 12/04/2026 | Criação do documento metodologias.md original                          | [Eric Camargo](https://github.com/ericcs10) | [Zenilda Vieira](https://github.com/zenildavieira) |
| `2.0` | 26/04/2026 | Refatoração: Metodologia como APLICAÇÃO, não definições | [Zenilda Vieira](https://github.com/zenildavieira) e GitHub Copilot | [Harleny Angélica](https://github.com/Angelicahaas) |
| `3.0` | 26/04/2026 | Mundança na liderança rotativa | [Harleny Angélica](https://github.com/Angelicahaas)| |
