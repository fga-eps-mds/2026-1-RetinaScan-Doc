# Regras de Versionamento

Nosso modelo de versionamento para checkpoints de modelos é baseado no [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/)

Possui a estrutura:

- `MODEL_ARCH` :  Arquitetura base
- `NUM_CLASS` :  Formato de saída
- `DATA_PATH` :  Estrutura de dados esperada
- `train.sh` : pipeline de inferência/saída do modelo

## 1. Regras de versionamento

| **MUDANÇA** | **TIPO** | **EXEMPLO** | **JUSTIFICATIVA** |
| --- | --- | --- | --- |
| **MAJOR** (X.0.0) | Mudanças **Incompatíveis** na API pública | Novo `MODEL_ARCH`  (dinov2), train.sh reescrito, nova estrutura de pastas | “**MAJOR** quando mudanças incompatíveis na API” |
| **MINOR** (x.Y.0) | Novas funcionalidades **compatíveis** | Novo dataset (`ODIR/RFMiD`), mesmo pipeline | “**MINOR** quando adicionar funcionalidades mantendo compatibilidade” |
| **PATCH** (x.y.Z) | Correções **compatíveis** | Bug no train.sh | “**PATCH** quando corrigir falhas mantendo compatibilidade” |

## 2. Tabela de Decisão

| **CRITÉRIO** | **MAJOR (x++)** | **MINOR (Y++)** | **PATCH (Z++)** |
| --- | --- | --- | --- |
| Muda `MODEL_ARCH` | [X] |  |  |
| Muda `NUM_CLASS`  | [X] |  |  |
| Reescrita `train.sh`  | [X] |  |  |
| Nova estrutura pastas | [X] |  |  |
| Novo dataset |  | [X] |  |
| Mesmo pipeline |  | [X] |  |
| Bug fix interno |  |  | [X] |
| Melhor logging |  |  | [X] |

### 2.1 Nomenclatura de versionamento

```
nome_modelo_dataset_vMAJOR.MINOR.PATCH-best.pth
```

Obs: as informações do **nome_modelo** e **dataset** é possível localizar no arquivo `train.sh` .

- **nome_modelo :** Identifica a família a qual o modelo pertence.
- **dataset :** Diz em qual dado aquele checkpoint foi treinado.
- **vMAJOR.MINOR.PATCH :** Aplica a regra SemVer oficial.
- **best :** Indica que é o melhor checkpoint daquela rodada.

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
|:------:|:----:|:----------|:------|:--------|
| 1.0 | 16/04/2026 | Documentação regras de versionamento | [Iderlan J.](https://github.com/IderlanJ) [Harleny A.](https://github.com/Angelicahaas) [Elias Oliveira](https://github.com/EliasOliver21) | [Elias Oliveira](https://github.com/EliasOliver21) |