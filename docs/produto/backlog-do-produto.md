# Backlog do Produto

**Nota:** Os critérios de aceitação de cada issue podem ser consultados no ZenHub através do link abaixo:  
> https://github.com/fga-eps-mds/2026-1-retinascan-doc/issues#workspaces/20261-fcte-fm-01-69bd9cee544e2d00306abb69/board

## Épicos

### Autenticação e Controle de Acesso
**Descrição:**  
Permite o controle seguro de acesso ao sistema, incluindo autenticação de usuários, gerenciamento de permissões e rastreabilidade das ações realizadas.

---

### Cadastro e Upload de Exames
**Descrição:**  
Responsável pelo registro de exames e envio de imagens oftalmológicas para posterior processamento.

---

### Histórico e Consulta
**Descrição:**  
Permite a visualização, busca e análise de exames previamente cadastrados, auxiliando no acompanhamento clínico.

---

### Processamento e IA
**Descrição:**  
Responsável pelo tratamento das imagens e integração com o modelo de IA para geração de resultados automatizados.

---

### Relatórios e Métricas
**Descrição:**  
Permite a visualização, exportação e compartilhamento de informações e resultados dos exames.

---

# Issues

### Cadastro automático de ADMIN
| Campo | Descrição |
| :--- | :--- |
| Épico | Autenticação e Controle de Acesso |
| História de Usuário | Eu, como sistema, desejo criar automaticamente um usuário administrador na primeira execução da aplicação para que seja possível acessar e gerenciar o sistema desde o início. |

---

### Login do usuário
| Campo | Descrição |
| :--- | :--- |
| Épico | Autenticação e Controle de Acesso |
| História de Usuário | Eu, como usuário cadastrado no sistema, desejo autenticar-me utilizando e-mail e senha para que eu possa acessar minha conta com segurança. |

---

### Cadastro de usuário pelo ADMIN
| Campo | Descrição |
| :--- | :--- |
| Épico | Autenticação e Controle de Acesso |
| História de Usuário | Eu, como usuário administrador do sistema, desejo cadastrar novos usuários para que eles possam acessar as funções do sistema. |

---

### Cadastro de exame
| Campo | Descrição |
| :--- | :--- |
| Épico | Cadastro e Upload de Exames |
| História de Usuário | Eu, como médico, desejo cadastrar um novo exame para que eu possa registrar informações de um paciente antes de enviar a imagem para análise. |

---

### Upload de imagem do exame
| Campo | Descrição |
| :--- | :--- |
| Épico | Cadastro e Upload de Exames |
| História de Usuário | Eu, como médico, desejo enviar uma imagem associada a um exame para que ela possa ser utilizada posteriormente no processamento. |

---

### Pré-processamento de imagem
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como sistema, desejo realizar o pré-processamento das imagens enviadas para que elas estejam padronizadas antes de serem utilizadas no processamento pela IA. |

---

### Visualização do histórico de exames
| Campo | Descrição |
| :--- | :--- |
| Épico | Histórico e Consulta |
| História de Usuário | Eu, como médico, desejo visualizar o histórico de exames para que eu possa acompanhar análises realizadas anteriormente. |

---

### Busca de exames
| Campo | Descrição |
| :--- | :--- |
| Épico | Histórico e Consulta |
| História de Usuário | Eu, como médico, desejo buscar exames específicos para que eu possa encontrar rapidamente informações relevantes. |

---

### Filtros de exames
| Campo | Descrição |
| :--- | :--- |
| Épico | Histórico e Consulta |
| História de Usuário | Eu, como médico, desejo aplicar filtros no histórico de exames para que eu possa refinar os resultados exibidos. |

---

### Reportar erro da IA
| Campo | Descrição |
| :--- | :--- |
| Épico | Histórico e Consulta |
| História de Usuário | Eu, como médico, desejo reportar um erro no julgamento da IA para que o sistema possa registrar inconsistências e permitir melhorias futuras. |

---

### Integração com modelo de IA
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como sistema, desejo enviar imagens pré-processadas para o modelo de IA para que elas possam ser analisadas. |

---

### Recebimento e interpretação do resultado da IA
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como sistema, desejo receber e interpretar o resultado retornado pelo modelo de IA para que ele possa ser utilizado no sistema. |

---

### Classificação e associação do resultado ao exame
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como sistema, desejo classificar o exame com base no resultado da IA e associá-lo ao exame correspondente para que o usuário possa consultar posteriormente. |

---

### Tratamento de erros no pipeline de IA
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como sistema, desejo tratar erros durante o processamento da IA para garantir que falhas não comprometam o funcionamento do sistema. |

---

### Validação da acurácia do modelo de IA
| Campo | Descrição |
| :--- | :--- |
| Épico | Processamento e IA |
| História de Usuário | Eu, como equipe de desenvolvimento, desejo validar a acurácia do modelo de IA para garantir que ele atenda aos requisitos mínimos do sistema. |

---

### [ENHANCE03] Compartilhamento de resultados via link
| Campo | Descrição |
| :--- | :--- |
| Épico | Relatórios e Métricas |
| História de Usuário | Eu, como usuário, desejo compartilhar resultados de exames por meio de um link para que outras pessoas possam acessar essas informações de forma controlada. |

---

### [ENHANCE02] Download de relatórios
| Campo | Descrição |
| :--- | :--- |
| Épico | Relatórios e Métricas |
| História de Usuário | Eu, como usuário, desejo fazer o download de relatórios de exames para que eu possa armazenar ou compartilhar essas informações externamente. |

---

### [ENHANCE01] Visualização de métricas
| Campo | Descrição |
| :--- | :--- |
| Épico | Relatórios e Métricas |
| História de Usuário | Eu, como administrador, desejo visualizar métricas sobre os exames realizados para que eu possa analisar padrões e acompanhar o uso do sistema. |








## Histórico de Versão

| Versão | Data       | Descrição | Autor        | Revisor      |
| :----: | ---------- | --------- | ------------ | ------------ |
| `1.0`  | 12/04/2016 | Criação do Documento | [Natália De Morais](https://github.com/Natyrodrigues) | ---- |
