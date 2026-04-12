# Política de branches

## Objetivo

Definir um padrão de organização de branches para garantir colaboração segura,
histórico limpo e entregas previsíveis ao longo do projeto.

## Estrutura de Branches

O projeto utiliza as seguintes categorias de branch:

- `main`: branch estável, contendo apenas conteúdo aprovado e pronto para entrega.
- `develop`: branch de integração das mudanças do ciclo atual.
- `feature/*`: desenvolvimento de novas funcionalidades, documentos ou melhorias.
- `fix/*`: correções de defeitos ou inconsistências identificadas em desenvolvimento.
- `hotfix/*`: correções urgentes em conteúdo já publicado na `main`.
- `release/*`: preparação final de versão para publicação.

## Convenção de Nomes

Use nomes curtos, claros e em minúsculas, separados por hífen.

Formato recomendado:

- `feature/nome-da-entrega`
- `fix/descricao-do-problema`
- `hotfix/descricao-do-ajuste`
- `release/vX.Y.Z`

Exemplos:

- `feature/politica-de-branches`
- `feature/atualizacao-arquitetura`
- `fix/link-quebrado-menu`
- `hotfix/correcao-roadmap-publicado`

## Fluxo de Trabalho

1. Criar branch a partir de `develop` para mudanças planejadas.
2. Realizar commits seguindo a Política de Commits do projeto.
3. Abrir Pull Request para `develop` com descrição objetiva da alteração.
4. Solicitar revisão de pelo menos um integrante da equipe.
5. Após aprovação, realizar merge.
6. Para publicação, criar `release/*` a partir de `develop` e, depois de validada,
fazer merge em `main` e em `develop`.

## Regras de Proteção

As seguintes regras devem ser aplicadas nas branches principais:

1. `main` e `develop` não devem receber push direto.
2. Alterações nessas branches devem ocorrer apenas via Pull Request.
3. Todo Pull Request deve passar por revisão.
4. Commits e títulos de PR devem seguir padrões claros e descritivos.

## Estratégia de Merge

Priorizar **Squash and Merge** para manter histórico objetivo por entrega.

Exceções podem ser aplicadas quando for necessário preservar histórico detalhado
de commits para rastreabilidade técnica.

## Boas Práticas

- Manter branches pequenas e de curta duração.
- Atualizar a branch com `develop` sempre que necessário para evitar conflitos longos.
- Evitar branches com múltiplos objetivos não relacionados.
- Excluir branches após merge para reduzir ruído no repositório.

## Histórico de Versão

| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação da política de branches | [Yan Luca Viana](https://github.com/yan-luca) |  |