# Modelos de IA - RetinaScan

## Introdução
Este documento descreve os modelos de inteligência artificial utilizados no projeto RetinaScan AI, incluindo arquitetura, versões e desempenho.

O projeto utiliza como base o modelo **RETFound**, um foundation model treinado para imagens médicas oculares.

---

## Modelos de I.A Utilizados no Projeto

## Modelo v1.0.0 - RETFound (Fine-tuning Inicial)

### Informações Gerais


| Campo | Valor |
|------|------|
| Modelo Base | RETFound_dinov2 |
| Arquitetura | Vision Transformer (ViT) |
| Tipo | Fine-tuned |
| Dataset | RFMiD |
| Versão | v1.1.0 |
| Data de Treinamento | 05/04/2026 |
| Epochs | 30 |


### Arquitetura

O modelo é baseado no RETFound:
- Backbone: Vision Transformer (ViT)
- Pré-treinado em imagens médicas (retina)
- Adaptado via fine-tuning para classificação

[Repositório original](https://github.com/rmaphoh/RETFound)

### Arquivo do Modelo

- Modelo treinado:  
  [Download do modelo](https://seu-link/model_v1_0_0.pth)

- [Código Fonte](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI)

### Configuração

- Framework: PyTorch
- Batch size: 16
- Learning rate: 1e-4
- Otimizador: Adam

### Resultados


| Métrica | Valor |
|--------|------|
| Accuracy | 0.85 |
| F1-score | 0.82 |

### Observações

- Serão adicionadas posteriormente após uma análise mais apurada dos resultados obtido com a utilização do modelo.

## Histórico de Versão
| Versão | Data | Descrição | Autor | Revisor |
| :----: | :--: | :-- | :-- | :-- |
| 1.0 | 13/04/2026 | Documentação do Fine-tuning inicial do RETFound | [Elias Oliveira](https://github.com/EliasOliver21) | -- |