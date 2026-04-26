## Ata de reunião 2 - 01/04/2026

### _Apresentação da equipe_ e Kick off com PO

## Local

Reunião realizada no modelo assíncrono via Teams

## Participantes

**Professor**: Hilmer Neri Rodrigues</br>
**Product Owner**: Vinícius Rispoli de Carvalho, Thiago

**Tabela 1:** Participantes da reunião

| Matrícula | Aluno                              | Presente |
| --------- | ---------------------------------- | -------- |
| 222037648 | André Cláudio Maia da Cunha        | ✓        |
| 221007850 | Arthur Ribeiro e Sousa             | ✓        |
| 221021901 | Cecília Ernesto Silva Quaresma     |          |
| 221007706 | Elias Faria de Oliveira            | ✓        |
| 202016168 | Eric Camargo da Silva              |          |
| 211061814 | Gustavo Costa de Jesus             | ✓        |
| 211061832 | Harleny Angéllica Araújo de Sousa  |          |
| 211062947 | Iderlan Junio Cardoso da Silva     | ✓        |
| 221037975 | Natália Rodrigues de Morais        | ✓        |
| 190020814 | Vinícius Roriz Meireles Silva      |          |
| 211031889 | Yan Luca Viana de Araújo Fontenele |          |
| 212002907 | Zenilda Pedrosa Vieira             | ✓        |

**Fonte:** [Iderlan Junio](https://github.com/IderlanJ), 2026

## Início e término

Na tabela 2 consta o horário de início e o horário de término previsto da reunião, assim como o horário que foi efetivamente realizado.

<div>
<font size="3"><p><b>Tabela 2:</b> Horários</p></font>

<table>
    <thead>
        <tr>
            <th></th>
            <th>Hora de Início</th>
            <th>Hora de Término</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Previsto</td>
            <td>19:30</td>
            <td>20:00</td>
        </tr>
        <tr>
            <td>Realizado</td>
            <td>19:30</td>
            <td>20:30</td>
        </tr>
    </tbody>
</table>

<font size="3"><p><b>Fonte:</b> <a href="https://github.com/IderlanJ">Iderlan Junio</a>, 2026</p></font>

</div>

## Pauta

- Definição do funcionamento do software RetinaScan
- Uso de Inteligência de requisitos do sistema
- Breve levantamento de requisitos do sistema
- Alinhamento com os donos do produto sobre a disciplina e entregas
- Definição do fluxo das imagens e responsabilidade médica
- Questões de armazenamento e integração com telemedicina
- Segurança da informação (LGPD e Criptografia)
- Definição de reuniões periódicas

## Desenvolvimento / Discussões

O Doutor Thiago comentou sobre como o sistema deverá permitr a _classificação de imagens oftalmológicas_ entre _normal_ e _alterado_. Em casos classificados como alterados, o paciente deverá ser encaminhado para um médico oftalmologista.

O produto inclui o uso de _Inteligência Artificial_ para auxiliar na identificação de alterações, fornecendo também uma probabilidade.

_O sistema será utilizado no contexto de médico de família, sendo necessário incluir:_

- Upload de imagens do olho esquerdo e direito
- Opção de _imagem indisponível_ (casos como cegueira ou ausência do olho)
- Dados do paciente: idade, sexo e comorbidades principais
- Destaque para comorbidades como hipertensão e diabetes

Em casos de diabetes:

- Tempo de doença
- Uso ou não de insulina

- Campo para outras comorbidades e observações gerais

### Sobre o fluxo:

- A imagem pode ser capturada por profissionais de saúde, mas o _médico é o responsável pelo encaminhamento_
- A IA realizará a classificação, e o médico decidirá sobre envio à telemedicina
- Inicialmente, todos os médicos receberão treinamento para uso da ferramenta

Foi discutido também o fluxo atual:

- O equipamento envia imagens diretamente para Goiânia
- No projeto, haverá análise local antes do envio
- Em alguns casos, as imagens podem permanecer apenas localmente
- Cada máquina possui capacidade de armazenamento de até 20 mil imagens na nuvem

### Sobre o desenvolvimento:

- Serão entregues 9 versões do produto em modelo iterativo e incremental

### Sobre tecnologia:

- O modelo de IA está em estudo pelo professor Rispoli (Mas reforçou que era importante o aprendizado sobre modelos de IA )

- Comentou sobre as preocupaçÕes com custos de treinamento

### Usuários:

- O sistema esterá integrado à plataforma da Phelcom
- Deve-se considerar uma área administrativa com dados cadastrais relevantes dos médicos

### Reuniões:

- Definido encontro semanal às segundas-feiras, às 19:00/19:30

## Conclusão

Ficou alinhado então que o sistema terá como foco principal _auxiliar o médico na triagem de imagens oftalmológicas por meio da IA_, mantendo a decisão final sob responsabiliade médica.

Foram definidos alguns dos principais requisitos funcionais do sistema, incluindo coleta de dados clínicos, upload de imagens e suporte à análise. Também ficou estabelecido o fluxo inicial de uso, considerando análise local e possível encaminhamento à telemedicina.

Foi apresentado aos donos do projeto que a equipe deverá focar no desenvolvimento incremental do produto, com entregas periódicas. Além disso, deverão ser executadas boas práticas de segurança da informação em conformidade com a LGPD.

Por fim, difiniu o alinhamento contínuo com os professores e reuniões semanais para acompanhamento da evolução do projeto.

A reunião inicial foi essencial para direcionar o grupo em relação aos próximos passos que devem ser tomados na _Lean Inception_.

## Histórico de Versão

| Versão | Data       | Descrição                             | Autor                                        | Revisor      |
| :----: | ---------- | ------------------------------------- | -------------------------------------------- | ------------ |
| `1.0`  | 02/04/2026 | Ata da reunião de apresentação com PO | [Iderlan Junio](https://github.com/IderlanJ) | [André Maia](https://github.com/andre-maia51) |
