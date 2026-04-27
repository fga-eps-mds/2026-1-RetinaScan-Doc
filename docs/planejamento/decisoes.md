# Registro de Decisões e Evolução do Projeto

Este documento tem como objetivo expor as decisões de gerenciamento e as decisões técnicas da equipe, fundamentando-as nos dados coletados e analisados de forma objetiva através das ferramentas de planejamento e do dashboard analítico. A partir desta visão técnica, buscamos identificar gargalos e oportunidades de melhoria para garantir a evolução contínua do projeto.

Este registro será incrementado ao final de cada ciclo de entrega, conectando as ações tomadas aos resultados reais observados nas métricas de desempenho e qualidade.

---

## 1. Ciclo da Release 1 (27/04/2026)

<details>
<summary><b>Clique para ver os detalhes da Release 1</b></summary>

### 1.1. Aspectos Gerenciais

**Análise do EVM e Ajuste de Carga:** Observando os dados trazidos do **EVM**, o **CPI de 0,781** ao final da terceira sprint (última sprint antes da entrega da release) mostra que a quantidade de SP's não foi adequada ao curto prazo de uma sprint (sete dias). No futuro, iremos limitar a quantidade de SP's para no máximo **80**, desta forma esperamos recuperar um pouco de fôlego da equipe.

<img width="632" height="117" alt="image" src="https://github.com/user-attachments/assets/808f2577-3f3a-42fb-ab14-6f050f10002e" />

**Comunicação e Daily:** Também foi notado durante esse período a dificuldade da comunicação em períodos em que o grupo não está reunido. Por isso, nas próximas sprints iremos aderir a um grupo de **"Daily"** para que, dessa forma, o grupo inteiro esteja ciente de quando uma atividade foi começada ou de quando um integrante esteja enfrentando dificuldades.

**Riscos:** No gerenciamento de riscos, subestimamos muito o impacto que a "dependencia entre atividades" (R09) poderia ter na nossa sprint. Para os próximo ciclos de desenvolvimento iremos fazer ajustes no cronograma e no backlog, além de aumentar o impacto desse risco na nossa planilha de gerenciamento. 

**Realocação de Esforço:** Com o final dessa etapa inicial de trabalho, o trabalho de documentação ficará mais leve. Dessa forma, colocaremos mais membros do grupo para trabalhar em questões de código.

**Gestão de Sprints no Zenhub:** Durante as sprints iniciais, a equipe teve algumas dificuldades com a nova plataforma **Zenhub** em mudar a configuração do tempo das sprints, o que levou a equipe a depender do rótulo dessas sprints para se organizar durante a rotina intensa de desenvolvimento em que não era possível parar o fornecimento de sprints. Agora que realizamos a release, pretendemos resetar o padrão automático de sprints do Zenhub para que possamos redefinir o tempo de sprint para uma semana ao invés de duas, como era da nossa vontade desde o início.

**Densidade de Issues:** Como essas primeiras sprints foram sprints de organização (criação de issues), notamos que a nossa **densidade de issues ficou em 50%**. Acreditamos que esse comportamento se deve ao grande número de issues criadas para o desenvolvimento do backlog, porém iremos observar se esse número irá aumentar.

<img width="644" height="538" alt="image" src="https://github.com/user-attachments/assets/697bbe90-8435-435e-9e63-a809894372e3" />

### 1.2. Decisões Técnicas

Nessa terceira sprint, desenvolvemos o **dashboard analítico** e ele nos ajudou a observar alguns pontos em que será necessária uma mudança:

* **Manutenibilidade e Comentários:** A equipe ficou muito focada em testes e em qualidade (com a ajuda do **Sonar**), mas esquecemos de focar na manutenibilidade do produto, conseguindo atingir uma **métrica 0 no quesito "comentários"**. O objetivo dessa nova sprint é aumentar em **30%** a quantidade de comentários nos dois repositórios (api/web). Dessa forma, esperamos não apenas aumentar a nota em manutenibilidade, mas aumentar a qualidade do nosso produto que atingiu a pontuação **0.8 de 1.0**.

<img width="996" height="502" alt="image" src="https://github.com/user-attachments/assets/17a571ba-a22f-4411-ba0d-d6ecf3449c13" />

---

<img width="964" height="505" alt="image" src="https://github.com/user-attachments/assets/166021f6-5468-4ebb-b762-a9d23d4bdfe9" />

---

<img width="977" height="501" alt="image" src="https://github.com/user-attachments/assets/c31feef3-095e-43c0-a8fe-25264b2e4764" />

---

* **Expansão de Escopo:** Durante o desenvolvimento, notamos algumas lacunas na jornada de usuário e pretendemos aumentar o nosso escopo incluindo: **sistema de alertas/notificações** e **sistema de recuperação de senha**.

</details>

---

## Histórico de versões
| Versão | Data | Modificação | Autor |
|--|--|--|--|
|1.0|27/04/2026 | Criação do documento | [Natália de Morais](https://github.com/Natyrodrigues)|
