# Lean Inception

## 1. Introdução

Este documento consolida os resultados da Lean Inception do produto RetinaScan, seguindo a ordem das dinâmicas executadas pela equipe.

Board de referência:
https://www.figma.com/board/KNKoP3IksUy3l2ifxMCK6R/Vis%C3%A3o-do-Produto-FCTE-FM-01-2026-1

## 2. Visão do Produto

**Para** profissionais da saúde envolvidos na triagem oftalmológica da rede pública,
**cujo processo** de triagem é lento, depende de análise posterior e dificulta a identificação rápida de alterações,
**o RetinaScan é uma** ferramenta web de apoio à triagem oftalmológica com inteligência artificial,
**que** reduz o tempo de triagem, realiza análise dos exames, identifica possíveis anomalias e prioriza casos suspeitos para avaliação especializada.
**Diferentemente do** RETINA-AI e do EyeArt,
**nosso produto** é voltado ao processo da saúde pública, priorizando os casos com maior urgência no mesmo fluxo da triagem.

## 3. Produto É, Não É, Faz e Não Faz

### 3.1 É

- ferramenta web;
- solução baseada em IA;
- exclusivo para uso clínico;
- focado na área de oftalmologia;
- auxiliador de triagem;
- voltado para a saúde pública;
- plataforma de classificação binária.

### 3.2 Não É

- ferramenta para diagnóstico definitivo;
- ferramenta para substituir profissionais de saúde;
- sistema mobile ou embarcado;
- ferramenta direcionada ao setor privado;
- ferramenta para uso do paciente;
- ferramenta para identificação de doenças específicas.

### 3.3 Faz

- auxilia na triagem inicial de pacientes no sistema de saúde pública;
- filtra os pacientes com anomalias;
- usa inteligência artificial para identificar automaticamente possíveis anomalias;
- permite revisão de casos com incerteza;
- processa imagens anonimizadas.

### 3.4 Não Faz

- diagnóstico da anomalia;
- diferenciação da gravidade do problema;
- prescrição de tratamento ou medicação;
- agendamento de consulta;
- notificação do paciente;
- exclusão automática de exames sem anomalia detectada.

Conforme a Figura 1, a delimitação do produto explicita o escopo funcional e os limites da solução.

<div align="center">
	<p><strong>Figura 1.</strong> Produto É, Não É, Faz e Não Faz.</p>
	<img src="../assets/imagens/lean-inception/e-nao-e-faz-nao-faz.PNG" alt="Produto É, Não É, Faz e Não Faz"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 4. Objetivos do Produto

Após a ideação, os objetivos foram organizados nos seguintes clusters:

### 4.1 Redução da fila e tempo de espera

- acelerar o encaminhamento de casos suspeitos para especialistas;
- usar a triagem automatizada como ferramenta de detecção de alterações precoces;
- reduzir a carga operacional do profissional, priorizando casos com alterações;
- agilizar o acesso ao profissional de saúde;
- concentrar atendimentos em casos críticos.

### 4.2 Rede pública

- melhorar o processo de triagem;
- apoiar o oftalmologista com IA confiável;
- cobrir mais pacientes com o mesmo time.

### 4.3 Segurança de dados e LGPD

- usar LGPD para proteção de dados dos pacientes;
- garantir anonimidade das imagens;
- proteger dados sensíveis dos pacientes.

### 4.4 Qualidade técnica das imagens

- garantir qualidade das retinografias;
- padronizar imagens para melhorar o desempenho do modelo de IA.

### 4.5 Plataforma

- permitir upload seguro e simples via web em qualquer unidade de saúde;
- facilitar revisão humana de casos duvidosos na própria plataforma;
- ser uma ferramenta intuitiva;
- auxiliar o profissional da saúde.

Os objetivos consolidados por cluster são apresentados na Figura 2.

<div align="center">
	<p><strong>Figura 2.</strong> Objetivos do Produto.</p>
	<img src="../assets/imagens/lean-inception/objetivos.PNG" alt="Objetivos do Produto"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 5. Personas

### 5.1 Persona 1 - Dra Meridite Cinza

**Perfil:** 40 anos, médica da família, casada, 4 filhos, sobrecarregada.

**Comportamento:** pragmática, proativa, estressada.

**Necessidades:**

- avaliar rapidamente o paciente;
- tomar decisões seguras mesmo sem conhecimento em oftalmologia;
- reduzir incerteza na decisão de encaminhamento;
- reduzir dependência de encaminhamentos desnecessários.

A representação visual da Persona 1 está na Figura 3.

<div align="center">
	<p><strong>Figura 3.</strong> Persona 1 (Dra Meridite Cinza).</p>
	<img src="../assets/imagens/lean-inception/Persona1.PNG" alt="Persona 1"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

### 5.2 Persona 2 - Derik Carneiro

**Perfil:** técnico de enfermagem, 35 anos, casado, frustrado.

**Comportamento:** responsável, proativo, analítico, curioso.

**Necessidades:**

- agilizar o processo de triagem na coleta das imagens de retina;
- ter direcionamento claro do próximo passo da triagem;
- adquirir conhecimento para avaliar sinais de problemas oculares;
- ter apoio para lidar com a alta demanda de pacientes.

A representação visual da Persona 2 está na Figura 4.

<div align="center">
	<p><strong>Figura 4.</strong> Persona 2 (Derik Carneiro).</p>
	<img src="../assets/imagens/lean-inception/Persona2.PNG" alt="Persona 2"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

### 5.3 Persona 3 - Leon Silva

**Perfil:** 65 anos, diabético, 2 filhas, sociável, pratica exercícios.

**Comportamento:** impaciente, matutino, teimoso, ativo, metódico.

**Necessidades:**

- descobrir se possui algum problema de saúde;
- obter o tratamento apropriado com rapidez;
- ser atendido com agilidade;
- receber orientação clara caso haja problema de saúde.

A representação visual da Persona 3 está na Figura 5.

<div align="center">
	<p><strong>Figura 5.</strong> Persona 3 (Leon Silva).</p>
	<img src="../assets/imagens/lean-inception/Persona3.PNG" alt="Persona 3"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 6. Jornada do Usuário

### Jornada 1 - Triagem e Encaminhamento

1. Recebe um paciente para consulta.
2. Captura a imagem da retina utilizando o aparelho de coleta.
3. Acessa o sistema web RetinaScan.
4. Preenche as informações do paciente no sistema.
5. Transfere a imagem (upload) para o sistema web.
6. Verifica no sistema se a qualidade da imagem foi validada.
7. Se necessário, refaz a captura.
8. Solicita a classificação automática da imagem (IA).
9. Verifica o resultado da classificação (normal ou alterado).
10. Identifica rapidamente os casos com alteração.
11. Analisa se o exame precisa ser priorizado.
12. Decide sobre encaminhamento ao oftalmologista especialista.
13. Registra a decisão no sistema.
14. Orienta o paciente e/ou realiza o encaminhamento.
15. Finaliza a consulta.

O fluxo detalhado da jornada está ilustrado na Figura 6.

<div align="center">
	<p><strong>Figura 6.</strong> Jornada do Usuário.</p>
	<img src="../assets/imagens/lean-inception/jornada-do-usuario.PNG" alt="Jornada do Usuário"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 7. Brainstorming de Funcionalidades

As funcionalidades identificadas foram agrupadas por temas:

### 7.1 Modelo de IA

- modelo treinado com alta acurácia (>90%);
- modelo de IA de processamento rápido (30s);
- pré-processamento de imagem;
- detecção de múltiplas condições de retina.

### 7.2 Segurança

- login e cadastro do profissional da saúde;
- registrar log de acesso;
- registrar decisão e responsável (encaminhar ou não);
- controlar acesso por perfil.

### 7.3 Tratamento de imagem

- upload de foto do exame;
- banco de imagens enviadas;
- anonimização das imagens analisadas;
- verificação da qualidade da imagem capturada;
- solicitar nova captura quando qualidade inferior ao limiar;
- pré-processamento antes de enviar para IA.

### 7.4 Página inicial

- dashboard com métricas das análises anteriores;
- histórico de análises;
- acessar lista de exames disponíveis;
- busca por exame;
- filtro de resultados por status (normal/alterado);
- status de revisão (imagens que precisam de atenção).

### 7.5 Página de resultado

- resultado da avaliação da IA;
- download do relatório;
- compartilhamento de resultado;
- botão "Reportar Erro da IA".

As funcionalidades levantadas e agrupadas na ideação estão apresentadas na Figura 7.

<div align="center">
	<p><strong>Figura 7.</strong> Brainstorming de Funcionalidades.</p>
	<img src="../assets/imagens/lean-inception/brainstorm-de-funcionalidades.PNG" alt="Brainstorming de Funcionalidades"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 8. Revisão Técnica, de Negócio e de UX

A revisão utilizou marcações visuais para priorização, esforço e confiança da equipe. O resultado consolidado indicou as funcionalidades mais críticas para compor os primeiros incrementos.

Funcionalidades destacadas na revisão:

- gerenciamento de usuários pelo ADMIN;
- login do profissional da saúde;
- controlar acesso por perfil;
- registrar log de acesso;
- cadastrar exame;
- upload de foto do exame;
- pré-processamento de imagem;
- modelo treinado com alta acurácia;
- resultado da avaliação da IA;
- botão "Reportar Erro da IA";
- histórico de análises;
- busca por relatório;
- filtros de busca;
- dashboard com métricas das análises anteriores;
- download do relatório;
- compartilhamento de resultado.

A priorização resultante da revisão técnica, de negócio e de UX é apresentada na Figura 8.

<div align="center">
	<p><strong>Figura 8.</strong> Revisão Técnica, de Negócio e de UX.</p>
	<img src="../assets/imagens/lean-inception/revisao-tecnica-de-negocio-e-ux.PNG" alt="Revisão Técnica, de Negócio e de UX"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 9. Sequenciador e MVP

Com base no sequenciador, os incrementos foram organizados em 5 ondas:

### 9.1 Incremento 1 - Acesso e segurança básica

- gerenciamento de usuários pelo ADMIN;
- login do profissional da saúde;
- controle de acesso por perfil.

### 9.2 Incremento 2 - Cadastro e processamento inicial

- registrar log de acesso;
- cadastrar exame;
- pré-processamento de imagem;
- upload de foto do exame.

### 9.3 Incremento 3 - Núcleo de IA

- modelo treinado com alta acurácia (90%);
- resultado da avaliação da IA;
- botão de "Reportar Erro da IA".

### 9.4 Incremento 4 - Histórico e busca (MVP)

- histórico de análises;
- busca de relatório;
- filtros de busca.

**MVP definido até este ponto.**

### 9.5 Incremento 5 - Evoluções pós-MVP

- dashboard com métricas das análises anteriores;
- download de relatório;
- compartilhamento de resultado.

Conforme a Figura 9, o sequenciador define os incrementos e delimita o ponto de corte do MVP.

<div align="center">
	<p><strong>Figura 9.</strong> Sequenciador e definição do MVP.</p>
	<img src="../assets/imagens/lean-inception/sequenciador.PNG" alt="Sequenciador e definição do MVP"/>
	<p><strong>Fonte:</strong> Elaboração própria, 2026.</p>
</div>

## 10. Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
| :----: | :--: | :-- | :-- | :-- |
| 1.1 | 13/04/2026 | Correção dos links das imagens para caminhos relativos compatíveis com GitHub Pages. | [Zenilda Vieira](https://github.com/ZenildaVieira) |  |
| 1.0 | 13/04/2026 | Preenchimento do documento com resultados da Lean Inception | [Zenilda Vieira](https://github.com/ZenildaVieira) |  |
