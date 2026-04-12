# Política de Commits

## Objetivo

Padronizar as mensagens de commit para manter o histórico do projeto claro,
rastreável e útil para revisão, manutenção e automações futuras.

## Padrão Adotado

Este projeto adota o padrão **Conventional Commits** com mensagens em português.

Formato da linha de título:

`tipo(escopo-opcional): descrição`

Exemplos:

- `docs: atualiza seção de metodologia no documento de arquitetura`
- `feat(backlog): adiciona critérios de aceite para a sprint 2`
- `fix(mkdocs): corrige link quebrado no menu de navegação`

## Regras da Mensagem

1. O título deve ter no máximo 72 caracteres.
2. A descrição deve ser objetiva e específica.
3. A descrição deve ser escrita em tom imperativo.
4. A descrição não deve terminar com ponto final.
5. O escopo é opcional, mas recomendado quando agregar clareza.
6. Commits genéricos como `update`, `ajustes` e `mudanças` não são permitidos.

## Tipos Permitidos

| Tipo       | Quando usar | Exemplo |
| ---------- | ----------- | ------- |
| `feat`     | Nova funcionalidade ou conteúdo novo relevante | `feat(projeto): adiciona seção de riscos na EAP` |
| `fix`      | Correção de erro, inconsistência ou comportamento incorreto | `fix(docs): corrige sumário da lean inception` |
| `docs`     | Alteração apenas de documentação | `docs: atualiza política de branches` |
| `style`    | Ajustes de formatação sem mudança de conteúdo | `style(roadmap): padroniza cabeçalhos de seção` |
| `refactor` | Reorganização estrutural sem alterar resultado final | `refactor(produto): reorganiza tópicos do backlog` |
| `test`     | Inclusão ou ajuste de testes e validações | `test: adiciona checklist de revisão dos documentos` |
| `chore`    | Tarefas de manutenção, configuração e rotina | `chore: atualiza dependências do mkdocs` |

## Corpo e Rodapé do Commit

Use corpo de commit quando a mudança não puder ser explicada com clareza em uma
única linha, especialmente quando envolver:

- contexto da mudança;
- impactos em outros documentos;
- decisões tomadas.

Formato recomendado:

```text
tipo(escopo-opcional): descrição curta

Contexto: ...
Mudança: ...
Impacto: ...
```

Quando existir issue relacionada, referencie no rodapé:

```text
Refs: #123
```

## Exemplos de Commits Bons e Ruins

### Bons

- `docs: adiciona seção de convenções de escrita no guia de contribuição`
- `fix(arquitetura): corrige referência incorreta ao modelo de dados`
- `chore(mkdocs): ajusta ordem das páginas no menu de navegação`

### Ruins

- `update`
- `ajustes`
- `mudanças no arquivo`
- `fix: coisa errada`

Os exemplos ruins não informam com precisão o que foi alterado, dificultam
rastreabilidade e revisão.

## Histórico de Versão

| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 12/04/2026 | Criação do Documento | [Yan Luca Viana](https://github.com/yan-luca) |  |s