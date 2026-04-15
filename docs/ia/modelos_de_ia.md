# Modelos de IA - RetinaScan

## Introdução

Este documento descreve os modelos de inteligência artificial utilizados no projeto RetinaScan AI, incluindo arquitetura, treinamento e versões.

O projeto utiliza como base o modelo **RETFound**, um foundation model treinado para imagens médicas oculares, adaptado para tarefas específicas de análise de imagens de retina por meio de técnicas de fine-tuning.

Para mais detalhes sobre a implementação, código-fonte e instruções de uso, acesse o repositório oficial do projeto:  
[RetinaScan AI no GitHub](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI)

---

## Modelos Utilizados no Projeto


Inicialmente, foi utilizado um modelo pré-treinado do tipo  **MAE (Masked Autoencoder)**, baseado no [RETFound](https://github.com/rmaphoh/RETFound), que serviu como base para os experimentos iniciais. A partir desse modelo, foi realizado um primeiro processo de fine-tuning voltado para a tarefa de classificação utilizando o **dataset RFMiD**.

Em seguida, foi conduzido um novo processo de fine-tuning utilizando uma variação baseada no **DINOv2**, com o objetivo de explorar melhorias de desempenho e representação de características visuais mais robustas.

Atualmente, o projeto faz uso do dataset **RFMiD** e decorrer do desenvolvimento, serão usados outros datasets para aprimorar treinamento.

<div class="md-typeset__scrollwrap">

| Campo | Modelo Base | Modelo de Arquitetura | Dataset | Versão | Data de Treinamento | Epochs |
|:------|:------------|:----------------------|:--------|:-------|:--------------------|:-------|
| [RETFound_mae_natureCFP](https://drive.google.com/drive/folders/1zzlsGu1LXpuL5hHLGziQmI168RTFJDUm) | RETFound_mae | redfound_mae | RFMiD | v1.0.0 | 05/04/2026 | 50 |
| [RETFound_dinov2_ODIR](https://drive.google.com/drive/folders/1lsQwFobQDNoKW4UTAiIKgWpp-AY8zsHH) | RETFound_dinov2 | redfound_dinov2 | ODIR | v2.0.0 | 13/04/2026 | 50 |
| [RETfound_dinov2_RFMiD](https://drive.google.com/drive/folders/1TIbB6AMFzwu7H8p32TuZteQXeadipfq0) | RETFound_dinov2 | redfound_dinov2 | ODIR / RFMiD | v2.1.0 | 13/04/2026 | 50 |

</div>

---
#### Arquitetura

A arquitetura REDFound é baseada no modelo RETFound, que utiliza Vision Transformer (ViT) e foi pré-treinado com aproximadamente 1,6 milhão de imagens de retina por meio de aprendizado autossupervisionado. Esse pré-treinamento permite ao modelo aprender representações visuais robustas e generalizáveis.

O RETFound já foi validado em múltiplas tarefas de detecção de doenças oculares, demonstrando boa capacidade de adaptação. A partir dessa base, a REDFound aplica técnicas de fine-tuning para ajustar o modelo a tarefas específicas do projeto, permitindo uma adaptação eficiente a diferentes datasets e cenários de classificação.

---

#### Configuração

Antes de iniciar o treinamento, revise os principais parâmetros:

| Parâmetro    | Descrição                 |
|:-------------|:--------------------------|
| `DATA_PATH`  | Caminho do dataset        |
| `OUTPUT_DIR` | Diretório de saída        |
| `BATCH_SIZE` | Depende da GPU            |
| `DEVICE`     | `cuda` ou `cpu`           |



Para mais detalhes sobre configuração do ambiente, execução e treinamento dos modelos, acesse:  

[Guia completo no repositório](https://github.com/fga-eps-mds/2026-1-RetinaScan-AI/edit/main/README.md)

---

#### Resultados

Os resultados obtidos demonstram um bom desempenho do modelo na tarefa de classificação. A métrica de **Accuracy** (0.85) indica que o modelo possui alta taxa de acerto geral, enquanto o **F1-score** (0.82) evidencia um equilíbrio consistente entre precisão e recall, sendo especialmente relevante para cenários com possíveis desbalanceamentos nas classes. Esses valores sugerem que o modelo é capaz de identificar padrões relevantes nas imagens de retina de forma confiável.

| Métrica   | Valor |
|:----------|:------|
| Accuracy  | 0.85  |
| F1-score  | 0.82  |

---

#### Observações

- As observações serão adicionadas posteriormente, após uma análise mais aprofundada dos resultados obtidos com a utilização do modelo.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
|:------:|:----:|:----------|:------|:--------|
| 1.0 | 13/04/2026 | Documentação do Fine-tuning inicial do RETFound | [Elias Oliveira](https://github.com/EliasOliver21) | [Harleny A.](https://github.com/Angelicahaas) |
| 1.1 | 15/04/2026 | Adição de descrições e formatação das tabelas | [Harleny A.](https://github.com/Angelicahaas)<br>[Iderlan J.](https://github.com/IderlanJ)<br>[Elias O.](https://github.com/EliasOliver21) | -- |