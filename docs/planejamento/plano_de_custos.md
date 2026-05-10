# Plano de Custos

Para maior organização e controle é fundamental um projeto ter um plano de custos bem definido. Um plano de custos claro permite representar os gastos previstos do projeto e detalha onde cada quantia está investida e em qual momento ocorrerão as demandas orçamentárias. Dessa forma, a gestão financeira e a tomada de decisões são facilitadas. [<a href=./#referencias-bibliograficas>1</a>]

## Estimativa de Custos

### Hora de Trabalho

Para calcular o valor do esforço de trabalho de cada membro do time do RetinaScan, adota-se estritamente o custo que cada integrante tem como aluno da Universidade de Brasília (UnB) alocado à disciplina, alinhando-se às diretrizes da orientação acadêmica do projeto. Dessa forma, o valor da hora técnica não reflete valores de mercado (como salários de desenvolvedores), mas sim o investimento público na formação do estudante.

De acordo com [<a href=./#referencias-bibliograficas>2</a>] o valor médio anual de um estudante é de R$ 51.708,00 em 2023. Corrigindo o valor para o ano de 2026, temos o custo médio de R$ 52.991,29 por aluno anual para a universidade [<a href=./#referencias-bibliograficas>3</a>]. Assumindo a média de 40 créditos anuais, temos o custo de R$ 1.324,78 por crédito. Para a disciplina de EPS, de 4 créditos, temos o custo de R$ 5.299,13 por aluno distribuído em 17 semanas ao longo do semestre letivo.

Portanto, o custo de cada integrante por semana no projeto RetinaScan é de R$ 311,71.

---

### Computadores

Para o projeto RetinaScan, dois tipos de computadores estão sendo utilizados: computadores simples para o trabalho de todos os integrantes e dois computadores dedicados para o processamento de modelos de IA. Além disso, segundo a Tabela de Vida Útil de Bens da Receita Federal [<a href=./#referencias-bibliograficas>4</a>] a depreciação de equipamentos de processamento de dados é de 20% ao ano, representando uma vida útil de 5 anos (60 meses) por equipamento. Tendo essas informações estabelecidas, podemos realizar o cálculo de custo semanal de cada tipo de computador durante o projeto.

#### Computadores Simples

Cada membro do time do RetinaScan precisa de um computador para a execução de atividades. Assumindo que um computador com configurações intermediárias de 8 GB de memória RAM, 512 GB de armazenamento e um processador AMD Ryzen 5 seja suficiente, temos o custo de referência de R$3.500,00 por computador [<a href=./#referencias-bibliograficas>5</a>]. Realizando o cálculo de depreciação utilizando a vida útil estabelecida pela Receita, temos que semanalmente cada computador tem o custo de R$13,61.


#### Computadores de IA

Para o processamento e treinamento dos modelos de IA do RetinaScan, o grupo utiliza 2 computadores de alta performance (A e B). Os valores dos computadores A e B são de R$12.939,99 e R$10.100,00, respectivamente. Utilizando a vida útil apontada pela Receita Federal, temos que, os computadores têm o custo semanal de R$50,32 e R$39,28 respectivamente.

---

### Energia

De acordo com a Neoenergia, o custo de 1 kWh no Distrito Federal é de R$ 0,83 [<a href=./#referencias-bibliograficas>6</a>]. A partir dessa tarifa básica, podemos realizar o cálculo do custo de energia elétrica por integrante do time levando em consideração o trabalho de 2 horas diárias (14 horas semanais), desprezando as 4 horas em sala de aula semanais, além do custo de energia dos computadores utilizados para o processamento de IA por 14 horas semanais. 

Cada computador básico tem um consumo médio de 0,04 kWh de energia, assumindo o uso de 2 horas por dia, cada máquina consome por semana o total de 0,56 kWh, ou seja, R$0,46 por semana. Já para os computadores de alta performance, estipulando que o consumo sob estresse de processamento seja de 0,5 kWh por máquina, cada computador consome semanalmente 7 kWh, logo, cada computador consome R$5,81 por semana.

---

### Internet

Assumindo um valor médio de R$100,00 mensais por plano de internet banda larga, 720 horas por mês e 14 horas de trabalho semanais, temos que cada membro do time tem o custo de R$1,94 por semana de internet.

---

### Custo de Hospedagem e Deploy

O deploy está sendo feito em uma VPS na plataforma Contabo [<a href=./#referencias-bibliograficas>7</a>] onde o custo mensal é de aproximadamente US$5.00, que, na cotação atual, está em torno de R$25.00, que representa um custo de R$6.25 por semana. Já a hospedagem está sendo realizada pela plataforma Hostinger [<a href=./#referencias-bibliograficas>8</a>] e, no primeiro ano de hospedagem, o custo é de R$6.00 mensais, representando o valor de R$1.50 por semana.

---

## Planilha de Custos

Todos os cálculos apresentados anteriormente na Estimativa de Custos estão detalhados na planilha a seguir:


<iframe width="1080" height="600" src="https://docs.google.com/spreadsheets/d/1CG2dsizofQNfcRwA9jol768X84Ri4lx42UIi6piAg54/edit?usp=sharing"></iframe>

**Fonte:** [André Maia](https://github.com/andre-maia51), 2026. Disponível em: [custos_FCTE-FM-01](https://docs.google.com/spreadsheets/d/1CG2dsizofQNfcRwA9jol768X84Ri4lx42UIi6piAg54/edit?usp=sharing)


Com isso, é possível ver que o custo total do projeto RetinaScan é de **R$68,710.19**.

## Pressupostos e Ajustes Estruturais

Este documento de custos é de natureza acadêmica descritiva e reflete uma estimativa teórica baseada em pressupostos iniciais. Ajustes estruturais significativos (como mudanças no número de integrantes ou ativação/desativação de componentes de infra) são registrados aqui.

### Pressupostos Iniciais (Baseline)

O cálculo total de **R$68,710.19** foi consolidado com as seguintes premissas:

- **Período:** 17 semanas de desenvolvimento (1º semestre de 2026)
- **Equipe:** 11 integrantes alocados à disciplina EPS
- **Carga de trabalho:** 2 horas diárias por integrante (14 horas/semana)
- **Infraestrutura:** VPS (Contabo) e hospedagem (Hostinger) ativas a partir da semana 1
- **Computadores de IA:** 2 máquinas de alta performance consumindo energia durante desenvolvimento
- **Cotação cambial:** USD 1,00 = R$ 5,00 (referência de 18/04/2026)

Estes pressupostos refletem o planejamento inicial e servem como ponto de referência. Mudanças estruturais relevantes devem ser registradas na tabela abaixo para permitir rastreabilidade e justificativa de variações.

### Tabela de Ajustes Estruturais

| Data | Tipo de Ajuste | Descrição | Impacto (R$) | Novo Total (R$) | Responsável | Justificativa |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| 29/04/2026 | Saída de pessoal | Um integrante saiu do projeto | -5,632.29 | 63,077.90 | [Elias Oliveira](https://github.com/EliasOliver21) | Redução de 11 para 10 integrantes |

### Notas Importantes

- Este documento não realiza controle contábil real de desembolsos, pois trata-se de um projeto acadêmico.
- O valor consolidado na planilha oficial (iframe) reflete o cálculo teórico em vigor.
- Alterações estruturais que impactem significativamente a estimativa (>5%) devem ser documentadas na tabela acima e no histórico de versão.
- Detalhes operacionais de sprints, responsáveis por tarefas e status de implementação devem ser mantidos no ZenHub/GitHub para evitar duplicação.

## Responsáveis e Processo de Validação

### Responsáveis

| Função | Responsável | Contato |
| :--- | :--- | :--- |
| Manutenção da planilha de custos | [André Maia](https://github.com/andre-maia51) | Atualizar cálculos e evidências; reportar mudanças estruturais |
| Aprovação de ajustes estruturais | [Vinícius Rispoli](https://github.com/...) (Product Owner) | Validar impacto de mudanças e aprovar novas estimativas |

### Processo de Aprovação

1. **Identificação de mudança:** um membro do time identifica uma mudança estrutural que impacta custos (ex: saída de integrante, ativação de infra).
2. **Documentação:** responsável pela planilha documenta o impacto na tabela de ajustes estruturais com data, descrição e cálculo revisado.
3. **Validação:** Product Owner revisa e aprova (ou questiona) a mudança em discussão assíncrona.
4. **Registro:** após aprovação, a entrada é confirmada na tabela; o histórico de versão é atualizado com citação ao commit/issue que motivou a mudança.
5. **Comunicação:** a revisão é comunicada ao time via Sprint Review ou documento atualizado no repositório.

### Frequência de Revisão

- **Semanalmente:** revisão planejada para identificar mudanças estruturais pendentes.
- **Sob demanda:** quando houver evento significativo (saída/entrada de integrante, mudança de infraestrutura).
- **Sprint Review:** resumo de ajustes consolidados e comunicação ao time.


## Referências Bibliográficas

> [1] Plano de gerenciamento de custos: como os CFOs devem atuar?. Disponível em: https://www.concur.com.br/blog/article/plano-de-gerenciamento-de-custos. Acesso em: 18/04/2026

> [2] Custo Médio Anual Alunos. Disponível em: https://www.poder360.com.br/poder-economia/alunos-de-universidades-federais-tem-custo-medio-anual-de-r-52-533/. Acesso em: 18/04/2026

> [3] Correção Monetária. Disponível em: https://www3.bcb.gov.br/CALCIDADAO/publico/corrigirPorIndice.do?method=corrigirPorIndice. Acesso em: 18/04/2026

> [4] Tabela de Bens, Receita Federal. Disponível em: https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/81268/visao/vigente#. Acesso em: 17/04/2026

> [5] Notebook ASUS. Disponível em: [https://www.amazon.com.br/Notebook-ASUS-VivoBook-RYZEN-KeepOS](https://www.amazon.com.br/Notebook-ASUS-VivoBook-RYZEN-KeepOS/dp/B0CYW2N6TX/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3MZ74CFS0CFDD&dib=eyJ2IjoiMSJ9.wrnu7r-klWzB5PbAhgr_2dhSCu-ZYxXfg8Am0qSJsOlcSwJoMR12jpOn3mWFxRYibx-XdIFW3sbrFcYDZJgJVwHJ-Zjnqday6IqsJInqUrdv8V0S-Vd6Y0XzMrGJZicFsE5pMDkVLw23_Pysb2VrUD4-S3NWiO68-_MybX1hQvfo9WCxKl_E1BKrh4yyUUO-5JW_31K0xLeGmpxRiSck2Z42YHfAZeDtP0_16ACcaux54w4xm16CShdgZQG4PJyXF5UUooN8CaU173wAJ099DhSUfLLO0Hcf1JbobgYU8YM.spUqTFd9TLgkFdab_F3lO-gRxVc4e0im3t77p7MK6xs&dib_tag=se&keywords=notebook&qid=1776358261&sprefix=notebook%2Caps%2C338&sr=8-5&ufe=app_do%3Aamzn1.fos.9e6a115c-05b9-4b96-8e1c-b1f9ce2ac1a6). Acesso em: 16/04/2026

> [6] Composição Tarifária. Disponível em: https://www.neoenergia.com/web/brasilia/sua-casa/composicao-tarifaria. Acesso em: 16/04/2026

> [7] Contabo. Disponível em: https://contabo.com/en/vps/cloud-vps-10/?image=ubuntu.332&qty=1&contract=12&storage-type=cloud-vps-10-150-gb-ssd. Acesso em: 18/04/2026

> [8] Hostinger: Disponível em: [https://www.hostinger.com/br/precos](https://www.hostinger.com/br/precos?_gl=1*5iuh87*_up*MQ..*_gs*MQ..&gclid=CjwKCAjw14zPBhAuEiwAP3-Eb7F_W6Ts5vhOLi3lIF9Q9fNQ6SbXJQCnSQ7D5fE5eq1lC6mTwx5XWhoCE8AQAvD_BwE&gbraid=0AAAAADMy-hZ_YAcmXooreUI6gOFa_fqAG). Acesso em: 18/04/2026

## Histórico de Versão

| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 18/04/2026 | Criação do documento de planejamento de riscos      | [André Maia](https://github.com/andre-maia51) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.1`  | 21/04/2026 | Correção do custo de hora de trabalho e referências      | [André Maia](https://github.com/andre-maia51) | [Elias Oliveira](https://github.com/EliasOliver21) |
| `1.2`  | 10/05/2026 | Refatoração para pressupostos/ajustes estruturais, adição de responsáveis e processo de validação, referência PMBOK      | [Elias Oliveira](https://github.com/EliasOliver21) | [](https://github.com/...) |