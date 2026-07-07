# Post-Mortem: Projeto RetinaScan

## 1. Resumo Executivo
Este documento apresenta a análise de Post-Mortem da solução **RetinaScan**, um sistema especializado no gerenciamento de exames e execução de inferências assíncronas utilizando Inteligência Artificial (PyTorch) para análise de imagens de retina. O encerramento do projeto consolidou a entrega de um ecossistema maduro, atingindo plenamente o valor planejado (SPI = 1.00) e demonstrando alto índice de confiabilidade técnica e estabilidade operacional.

## 2. Decisões Arquiteturais e Lições Aprendidas
Uma das principais discussões técnicas do projeto girou em torno do estilo arquitetural de implantação. A equipe optou estrategicamente por **não adotar uma arquitetura baseada estritamente em microsserviços complexos**, concentrando-se na divisão clara em **três repositórios fundamentais**:
* **Frontend:** Interface com o usuário e consumo das APIs via HTTPS.
* **API (Backend Core):** Responsável pelas regras de negócio estruturadas em Node.js com Fastify, TypeORM e PostgreSQL.
* **Mecanismo de IA:** Serviço especializado em FastAPI utilizando Redis e Celery Worker para execução assíncrona do modelo PyTorch.

**Validação por Teste de Carga:** Essa decisão de simplificação para três repositórios foi rigorosamente validada por meio de testes de carga realizados pelo time. Os resultados evidenciaram que a arquitetura suporta com resiliência o fluxo de requisições de inferência sem apresentar gargalos de concorrência ou degradação de desempenho, justificando a eliminação da complexidade desnecessária de múltiplos microsserviços independentes.

## 3. Análise de Métricas de Qualidade (Dashboard Qrapids)
Os indicadores extraídos da ferramenta de análise de qualidade revelam uma distinção evidente entre o comportamento operacional do código e os critérios estritos de documentação interna:

| Métrica / Indicador | Backend (API) | Frontend |
| :--- | :--- | :--- |
| **Product Quality (Pontuação Total)** | 0.84 / 1.00 | 0.79 / 1.00 |
| **Confiabilidade (Reliability)** | 0.50 / 0.50 *(Máxima)* | 0.46 / 0.50 |
| **Manutenibilidade (Maintainability)** | 0.34 / 0.50 | 0.33 / 0.50 |

**Análise Crítica da Manutenibilidade:** Ambas as frentes apresentaram uma redução na nota de manutenibilidade. O diagnóstico técnico apontou que essa depreciação ocorreu pelo fato de os repositórios possuírem uma taxa de linhas de comentários aceitáveis abaixo de 30%. Embora o código seja semanticamente limpo e validado por testes (Vitest no backend), a escassez de documentação inline impactou o indicador do Qrapids. Em contrapartida, a confiabilidade do backend atingiu a pontuação máxima de 0.50, assegurando a robustez das transações e do processamento de exames.

## 4. Gestão de Projeto e Indicadores Ágeis (Agile EVM)
O acompanhamento da execução financeira e de escopo sob a metodologia Agile EVM (Earned Value Management) ao final da Release Major 3 demonstrou uma aderência perfeita ao planejamento inicial:
* **BAC (Budget at Completion / Pontos Planejados):** R$ 15.292,87
* **EV (Earned Value / Valor Agregado Acumulado):** R$ 15.292,87
* **SPI (Schedule Performance Index / Índice de Desempenho de Prazo):** 1.00 *(Entrega rigorosamente no prazo)*
* **ETC (Estimate to Complete / Falta Gastar):** R$ 0,00 *(Todas as metas de esforço foram atingidas)*

O time obteve um aproveitamento expressivo no fluxo de valor, finalizando com sucesso **99 das 106 issues planejadas** no backlog acumulado do projeto.

## 5. Eficiência da Esteira DevOps (CI/CD)
A automação do fluxo de integração e entrega contínua via GitHub Actions demonstrou excelente maturidade tecnológica:
* **Tempo Médio de Feedback da CI:** 0.47 minutos (menos de 30 segundos para validação de builds e testes).
* **Total de Execuções de Builds:** 472 execuções ao longo do ciclo de vida do projeto.

Este tempo de feedback extremamente baixo garantiu agilidade das correções, reduzindo o tempo de ociosidade dos desenvolvedores e evitando a quebra da branch principal durante integrações complexas.

## 6. Conclusões e Recomendações Futuras
* **Pontos Fortes:** O desacoplamento do motor de IA através de filas assíncronas (Redis/Celery) isolou o peso computacional das inferências PyTorch, preservando o tempo de resposta da API principal desenvolvida em Fastify. A previsibilidade de entregas (SPI = 1.00) consagra a maturidade do processo de gestão.
* **Pontos de Melhoria (Lições Aprendidas):** Para projetos subsequentes, é imperativo estabelecer políticas de revisão de código que exijam documentação interna adequada e comentários inline para manter o indicador de manutenibilidade do Qrapids acima das metas ideais (> 30%).

## Histórico de versões
| Versão | Data | Modificação | Autor |
|--|--|--|--|
|1.0|06/07/2026 | Criação do documento | [Natália De Morais](https://github.com/Natyrodrigues) |
