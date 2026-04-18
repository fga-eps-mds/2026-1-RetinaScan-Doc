# Plano de Custos

Para maior organização e controle é fundamental um projeto ter um plano de custos bem definido. Um plano de custos claro permite representar os gastos previstos do projeto e detalha onde cada quantia está investida e em qual momento ocorrerão as demandas orçamentárias. Dessa forma, a gestão financeira e a tomada de decisões são facilitadas. [<a href=./#referencias-bibliograficas>1</a>]

## Estimativa de Custos

### Hora de Trabalho

Para calcular o valor da hora de trabalho de cada membro do time do RetinaScan, separamos dois parâmetros de valor: (1) O custo que cada integrante tem como aluno da Universidade de Brasília na disciplina; (2) O custo hipotético que cada integrante teria durante o trabalho como desenvolvedor júnior fora do horário de aula no projeto.

Portanto, consideramos um valor para as 4 horas de aula como estudantes e outro valor para as 14 horas de trabalho assíncrono por semana.

#### Valor como Estudante

De acordo com [<a href=./#referencias-bibliograficas>2</a>] o valor médio anual de um estudante é de R$51.708,00 em 2023. Corrigindo o valor para o ano de 2026, temos o custo médio de R$52.991,29 por aluno anual para a Universidade de Brasília [<a href=./#referencias-bibliograficas>3</a>]. Assumindo a média de 40 créditos anuais, temos o custo de R$1.324,78 por crédito. Para a disciplina de EPS, de 4 créditos, temos o custo de R$5.299,13 por aluno e 17 semanas ao longo do semestre letivo. Portanto, o custo semanal de um aluno na disciplina de EPS em 2026 é de R$311,71.

#### Valor como Desenvolvedor Júnior

O site Glassdoor [<a href=./#referencias-bibliograficas>4</a>] informa que um desenvolvedor de software júnior no DF em 2026 recebe entre R$2.000,00 e R$4.000,00. Assumindo como o custo de cada integrante da equipe a média aritmética simples, temos que, cada membro custa R$3.000,00 mensais. Estabelecendo que um mês tem 720 horas e, semanalmente, é esperado 14 horas de trabalho por integrante do time fora da sala de aula, temos que, por semana, cada membro tem um custo de trabalho de R$58,33.

Por fim, o custo de cada integrante por semana no projeto RetinaScan é a soma do valor como estudante e do valor como desenvolvedor júnior fora de sala de aula: R$370,05.

---

### Computadores

Para o projeto RetinaScan, dois tipos de computadores estão sendo utilizados: computadores simples para o trabalho de todos os integrantes e dois computadores dedicados para o processamento de modelos de IA. Além disso, segundo a Tabela de Vida Útil de Bens da Receita Federal [<a href=./#referencias-bibliograficas>5</a>] a depreciação de equipamentos de processamento de dados é de 20% ao ano, representando uma vida útil de 5 anos (60 meses) por equipamento. Tendo essas informações estabelecidas, podemos realizar o cálculo de custo semanal de cada tipo de computador durante o projeto.

#### Computadores Simples

Cada membro do time do RetinaScan precisa de um computador para a execução de atividades. Assumindo que um computador com configurações intermediárias de 8 GB de memória RAM, 512 GB de armazenamento e um processador AMD Ryzen 5 seja suficiente, temos o custo de referência de R$3.500,00 por computador [<a href=./#referencias-bibliograficas>6</a>]. Realizando o cálculo de depreciação utilizando a vida útil estabelecida pela Receita, temos que semanalmente cada computador tem o custo de R$13,61.


#### Computadores de IA

Para o processamento e treinamento dos modelos de IA do RetinaScan, o grupo utiliza 2 computadores de alta performance (A e B). Os valores dos computadores A e B são de R$12.939,99 e R$10.100,00, respectivamente. Utilizando a vida útil apontada pela Receita Federal, temos que, os computadores têm o custo semanal de R$50,32 e R$39,28 respectivamente.

---

### Energia

De acordo com a Neoenergia, o custo de 1 kWh no Distrito Federal é de R$ 0,83 [<a href=./#referencias-bibliograficas>7</a>]. A partir dessa tarifa básica, podemos realizar o cálculo do custo de energia elétrica por integrante do time levando em consideração o trabalho de 2 horas diárias (14 horas semanais), desprezando as 4 horas em sala de aula semanais, além do custo de energia dos computadores utilizados para o processamento de IA por 14 horas semanais. 

Cada computador básico tem um consumo médio de 0,04 kWh de energia, assumindo o uso de 2 horas por dia, cada máquina consome por semana o total de 0,56 kWh, ou seja, R$0,46 por semana. Já para os computadores de alta performance, estipulando que o consumo sob estresse de processamento seja de 0,5 kWh por máquina, cada computador consome semanalmente 7 kWh, logo, cada computador consome R$5,81 por semana.

---

### Internet

Assumindo um valor médio de R$100,00 mensais por plano de internet banda larga, 720 horas por mês e 14 horas de trabalho semanais, temos que cada membro do time tem o custo de R$1,94 por semana de internet.

---

### Custo de Hospedagem e Deploy

O deploy está sendo feito em uma VPS na plataforma Contabo [<a href=./#referencias-bibliograficas>8</a>] onde o custo mensal é de aproximadamente US$5.00, que, na cotação atual, está em torno de R$25.00, que representa um custo de R$6.25 por semana. Já a hospedagem está sendo realizada pela plataforma Hostinger [<a href=./#referencias-bibliograficas>9</a>] e, no primeiro ano de hospedagem, o custo é de R$6.00 mensais, representando o valor de R$1.50 por semana.

---

## Planilha de Custos

Todos os cálculos apresentados anteriormente na Estimativa de Custos estão detalhados na planilha a seguir:


<iframe width="1080" height="600" src="https://docs.google.com/spreadsheets/d/1CG2dsizofQNfcRwA9jol768X84Ri4lx42UIi6piAg54/edit?usp=sharing"></iframe>

**Fonte:** [André Maia](https://github.com/andre-maia51), 2026. Disponível em: [custos_FCTE-FM-01](https://docs.google.com/spreadsheets/d/1CG2dsizofQNfcRwA9jol768X84Ri4lx42UIi6piAg54/edit?usp=sharing)


Com isso, é possível ver que o custo total do projeto RetinaScan é de **R$80.610,19**.


## Referências Bibliográficas

> [1] Plano de gerenciamento de custos: como os CFOs devem atuar?. Disponível em: https://www.concur.com.br/blog/article/plano-de-gerenciamento-de-custos. Acesso em: 18/04/2026

> [2] Custo Médio Anual Alunos. Disponível em: https://www.poder360.com.br/poder-economia/alunos-de-universidades-federais-tem-custo-medio-anual-de-r-52-533/. Acesso em: 18/04/2026

> [3] Correção Monetária. Disponível em: https://www3.bcb.gov.br/CALCIDADAO/publico/corrigirPorIndice.do?method=corrigirPorIndice. Acesso em: 18/04/2026

> [4] Salário Dev. Jr. DF em 2026. Disponível em: https://www.glassdoor.com.br/Sal%C3%A1rios/bras%C3%ADlia-distrito-federal-desenvolvedor-junior-sal%C3%A1rio-SRCH_IL.0,25_IC2494161_KO26,46.htm. Acesso em: 17/04/2026

> [5] Tabela de Bens, Receita Federal. Disponível em: https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/81268/visao/vigente#. Acesso em: 17/04/2026

> [6] Notebook ASUS. Disponível em: [https://www.amazon.com.br/Notebook-ASUS-VivoBook-RYZEN-KeepOS](https://www.amazon.com.br/Notebook-ASUS-VivoBook-RYZEN-KeepOS/dp/B0CYW2N6TX/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3MZ74CFS0CFDD&dib=eyJ2IjoiMSJ9.wrnu7r-klWzB5PbAhgr_2dhSCu-ZYxXfg8Am0qSJsOlcSwJoMR12jpOn3mWFxRYibx-XdIFW3sbrFcYDZJgJVwHJ-Zjnqday6IqsJInqUrdv8V0S-Vd6Y0XzMrGJZicFsE5pMDkVLw23_Pysb2VrUD4-S3NWiO68-_MybX1hQvfo9WCxKl_E1BKrh4yyUUO-5JW_31K0xLeGmpxRiSck2Z42YHfAZeDtP0_16ACcaux54w4xm16CShdgZQG4PJyXF5UUooN8CaU173wAJ099DhSUfLLO0Hcf1JbobgYU8YM.spUqTFd9TLgkFdab_F3lO-gRxVc4e0im3t77p7MK6xs&dib_tag=se&keywords=notebook&qid=1776358261&sprefix=notebook%2Caps%2C338&sr=8-5&ufe=app_do%3Aamzn1.fos.9e6a115c-05b9-4b96-8e1c-b1f9ce2ac1a6). Acesso em: 16/04/2026

> [7] Composição Tarifária. Disponível em: https://www.neoenergia.com/web/brasilia/sua-casa/composicao-tarifaria. Acesso em: 16/04/2026

> [8] Contabo. Disponível em: https://contabo.com/en/vps/cloud-vps-10/?image=ubuntu.332&qty=1&contract=12&storage-type=cloud-vps-10-150-gb-ssd. Acesso em: 18/04/2026

> [9] Hostinger: Disponível em: [https://www.hostinger.com/br/precos](https://www.hostinger.com/br/precos?_gl=1*5iuh87*_up*MQ..*_gs*MQ..&gclid=CjwKCAjw14zPBhAuEiwAP3-Eb7F_W6Ts5vhOLi3lIF9Q9fNQ6SbXJQCnSQ7D5fE5eq1lC6mTwx5XWhoCE8AQAvD_BwE&gbraid=0AAAAADMy-hZ_YAcmXooreUI6gOFa_fqAG). Acesso em: 18/04/2026

## Histórico de Versão

| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 18/04/2026 | Criação do documento de planejamento de riscos      | [André Maia](https://github.com/andre-maia51) | [xxxx](xxxx) |