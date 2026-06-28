# Plano de Gestão de Qualidade de Produto — Modelo Q-Rapids

## 1. Introdução e Contexto
Este documento formaliza o **Plano de Gestão de Qualidade** para os repositórios do projeto (**Api** e **Web**), utilizando o framework **Q-Rapids** sobre os dados do **SonarQube** e **GitHub**[cite: 1]. 

Como o time já vinha mantendo uma cultura estrita de testes automatizados, baixo índice de duplicação e código modular desde o início do ciclo de desenvolvimento, as métricas brutas do projeto já se encontram em patamares excelentes[cite: 1]. Este plano cumpre o papel de documentar formalmente esses critérios e estipular as ações para as duas últimas sprints do projeto (**Sprint 12** e **Sprint 13**), focando na resolução do déficit de documentação inline sem comprometer a estabilidade do software[cite: 1].

---

## 2. Abordagem Metodológica e Regras de Avaliação
O modelo Q-Rapids organiza a avaliação de qualidade de forma hierárquica em três níveis[cite: 1]:
1. **Indicador Estratégico (*Strategic Indicator*):** Visão macro do produto (*Product Quality Total Score*)[cite: 1].
2. **Fatores de Qualidade (*Quality Factors*):** Aspectos de engenharia (*Maintainability* e *Reliability*), regulamentados por constantes de peso fixas[cite: 1].
3. **Métricas Base (*Metrics*):** Dados brutos extraídos do SonarQube e GitHub[cite: 1].

### Limiares Semafóricos (Aplicados a Product Quality e Métricas Base)
* 🟢 **Verde (Aprovado):** $\ge 0.75$[cite: 1]
* 🟡 **Amarelo (Atenção):** $0.50 - 0.74$[cite: 1]
* 🔴 **Vermelho (Crítico):** $< 0.50$[cite: 1]

*Nota Explicativa:* Os Fatores de Qualidade (Maintainability e Reliability) não utilizam essa escala de cores direta, pois são multiplicados pelas constantes de peso $PC_1$ e $PC_2$ (fixadas em $0.50$), limitando o seu teto matemático máximo a $0.50$[cite: 1].

---

## 3. Memória de Cálculo e Fórmulas Utilizadas

### 3.1. Agregadores de Código e Testes
$$\text{Code Quality} = (\text{Complexity} \times 0.33) + (\text{Comments} \times 0.33) + (\text{Duplication} \times 0.33)$$
* Mapeia a conformidade de arquivos (FIL) para complexidade $\le 10$, linhas de comentários entre $10\% - 30\%$ e duplicação $< 5\%$[cite: 1].

$$\text{Testing Status} = (\text{Test Success} \times 0.25) + (\text{Fast Tests} \times 0.25) + (\text{Coverage} \times 0.50)$$
* Mapeia suítes de testes (UTS) 100% estáveis, execuções rápidas ($< 5\text{ min}$) e arquivos com cobertura $> 60\%$[cite: 1].

### 3.2. Fatores de Qualidade
$$\text{Maintainability (Manutenibilidade)} = \text{Code Quality} \times 0.50$$
$$\text{Reliability (Confiabilidade)} = \text{Testing Status} \times 0.50$$

---

## 4. Diagnóstico e Documentação das Métricas Atuais (Versão 2.2.4)

### 4.1. Repositório: Api (5.856 NCLOC)
* **Product Quality (Total Score):** **0.83** 🟢 (Aprovado)[cite: 1]
* **Maintainability (Manutenibilidade):** 0.33 *(Escala 0 a 0.50)*[cite: 1]
* **Reliability (Confiabilidade):** 0.50 *(Escala 0 a 0.50 - Teto Máximo)*[cite: 1]

#### Histórico de Qualidade Documentado:
* **Complexity (1.00) 🟢:** Funções totalmente modulares com complexidade ciclomática por função $\le 10$[cite: 1].
* **Duplication (1.00) 🟢:** Código limpo e sem redundâncias (linhas duplicadas $< 5\%$)[cite: 1].
* **Test Success (1.00) 🟢:** Suíte de testes unitários 100% estável, sem erros ou falhas[cite: 1].
* **Fast Tests (1.00) 🟢:** Builds de testes rápidos executando em tempo inferior a 5 minutos[cite: 1].
* **Coverage (1.00) 🟢:** Cobertura vacinal ideal e completa nos arquivos elegíveis ($> 60\%$)[cite: 1].
* **Comments (0.02) 🔴:** Único ponto abaixo do esperado devido à escassez de comentários inline ($< 30\%$)[cite: 1].

### 4.2. Repositório: Web (4.439 NCLOC)
* **Product Quality (Total Score):** **0.79** 🟢 (Aprovado)[cite: 1]
* **Maintainability (Manutenibilidade):** 0.33 *(Escala 0 a 0.50)*[cite: 1]
* **Reliability (Confiabilidade):** 0.46 *(Escala 0 a 0.50)*[cite: 1]

#### Histórico de Qualidade Documentado:
* **Complexity (0.98) 🟢:** Componentes e funções de interface bem estruturados e simples[cite: 1].
* **Duplication (0.98) 🟢:** Baixíssimo índice de redundância de código ou styles reutilizados[cite: 1].
* **Test Success (1.00) 🟢:** Testes de interface e hooks rodando com 100% de sucesso[cite: 1].
* **Fast Tests (1.00) 🟢:** Feedback ágil nas execuções de CI da esteira de desenvolvimento[cite: 1].
* **Coverage (0.86) 🟢:** Cobertura de código sólida e amplamente superior à meta estabelecida de 60%[cite: 1].
* **Comments (0.03) 🔴:** Ausência crônica de linhas de comentários aceitáveis no frontend[cite: 1].

---

## 5. Critérios Técnicos de Amostragem

Como o volume total do ecossistema de software ultrapassa 10.000 linhas de código (NCLOC), tentar documentar todos os arquivos indistintamente é inviável e ineficiente[cite: 1]. O plano estabelece uma estratégia de **esforço focado por amostragem de criticidade**, utilizando parâmetros técnicos objetivos extraídos do próprio SonarQube para filtrar onde a intervenção de documentação gera maior retorno em manutenibilidade[cite: 1].

### 5.1. Critérios Técnicos de Filtragem
Os arquivos serão priorizados e incluídos no escopo de atuação com base em dois indicadores técnicos do SonarQube:
1. **Tamanho do Arquivo (Linhas de Código - NCLOC):** Arquivos extensos que centralizam regras de negócio.
    * *Filtro Técnico:* Arquivos com $\ge 150 \text{ NCLOC}$.
2. **Densidade de Lógica Relativa:** Arquivos que possuem ramificações lógicas reais e necessitam de contextualização técnica, evitando o desperdício de tempo em arquivos com complexidade zero.
    * *Filtro Técnico:* Arquivos com complexidade ciclomática total no arquivo $\ge 5$.

### 5.2. Escopo Alvo de Engenharia por Repositório
* **No ecossistema API:** Classes controladoras (*Views/Controllers*) de endpoints centrais e métodos que herdam de modelos de banco de dados com múltiplos relacionamentos. Arquivos de migração automatizada, configurações locais e rotas de roteamento simples estão **fora de escopo**.
* **No ecossistema WEB:** Hooks customizados e componentes de interface que gerenciam estados complexos ou que realizam a integração de chamadas assíncronas com a API. Componentes puramente visuais, folhas de estilo e declarações de tipos estáticos estão **fora de escopo**.
---

## 6. Planejamento Operacional por Sprints

O cronograma operacional remove qualquer outra atividade colateral e foca exclusivamente nas tarefas de documentação inline para forçar a subida dos indicadores de código:

### 6.1. Planejamento Detalhado: Sprint 12 (Jun 22 - Jun 28)
* **Meta da Sprint:** Iniciar a escrita de comentários nos primeiros 50% dos arquivos críticos selecionados pelos critérios de amostragem.
* **Ações de Engenharia:**
  1. **Triagem Imediata (Dia 1):** Varredura automatizada para extrair a lista exata de arquivos que atendem a >= 150 NCLOC e complexidade >= 5.
  2. **Injeção de Comentários - Lote API:** Escrita dedicada de comentários padronizados na primeira metade dos módulos controladores e serviços mapeados da API.
  3. **Injeção de Comentários - Lote Web:** Escrita dedicada de comentários padronizados na primeira metade dos hooks customizados e gerenciadores de estado mapeados no Web.
  4. **Validação Parcial (Dia 6):** Execução de análise local no SonarQube para computar o progresso parcial e garantir que os arquivos alterados sigam com os testes de regressão estáveis.
* **Entregável Técnico:** Primeira metade do ecossistema crítico devidamente documentada no repositório.

### 6.2. Planejamento Detalhado: Sprint 13 (Jun 29 - Final)
* **Meta da Sprint:** Finalizar a escrita de comentários nos 50% restantes dos arquivos críticos e consolidar a métrica `Comments` global acima do patamar mínimo de 15% de densidade.
* **Ações de Engenharia:**
  1. **Injeção de Comentários - Lote API Restante (Dias 1 e 2):** Conclusão da escrita de comentários no restante dos arquivos alvos selecionados para a API.
  2. **Injeção de Comentários - Lote Web Restante (Dias 3 e 4):** Conclusão da escrita de comentários no restante dos arquivos alvos selecionados para o Web.
  3. **Validação Final da Métrica Base (Dia 5):** Disparo de varredura completa do SonarQube para homologar que a densidade geral de comentários atingiu a meta de 15%, forçando a transição do status do agregador de Crítico (🔴) para Atenção (🟡).
* **Entregável Técnico:** 100% dos arquivos críticos de negócio documentados e validação final da métrica de `Maintainability` rebalanceada no Q-Rapids.

---

## 7. Conclusão
O plano de gestão estabelece uma abordagem matemática e pragmática para o encerramento do ciclo de desenvolvimento. Ao focar exclusivamente na atividade de documentação inline nas Sprints 12 e 13, o time divide a carga de trabalho de forma equilibrada, eleva os indicadores de código e garante a entrega de um produto final com qualidade homologada em todos os parâmetros do Q-Rapids.


| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 28/06/2026 | Criação do documento de planejamento de qualidade      | [Natália De Morais](https://github.com/Natyrodrigues) | --- |
