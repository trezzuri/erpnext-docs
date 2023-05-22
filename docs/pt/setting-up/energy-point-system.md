# Sistema de pontos de energia


**Sistema de Pontos de Energia é um sistema de classificação/carma que você pode habilitar para sua organização.**


Este sistema pode ser usado para acompanhar o desempenho de cada usuário.



> 
> Para ativar o Sistema de pontos de energia, vá para **Configurações de pontos de energia**
>  marque **Ativado**.
> 
> 
> 


## 1. Como usar o Sistema de Pontos de Energia?


Para começar a usar este sistema, você precisa criar algumas regras de pontos de energia (consulte a seção 3. Como criar regras de pontos de energia?) para que os usuários possam obter pontos de energia com base em suas atividades.


## 2. O que são regras de pontos de energia?


As regras de pontos de energia armazenam as informações sobre a atividade e o valor dos pontos a serem alocados.


A regra de ponto de energia tem os seguintes campos:




| Campo | Descrição |
| --- | --- |

| DocType de referência | Tipo de documento ao qual deseja aplicar a regra, por exemplo. Tarefa, ToDo, Problema, etc. |

| Para evento de documento | Opções: Salvar, Enviar, Cancelar e Personalizar.**Observação:** Se a opção "Personalizar" for selecionada, o campo "Condições" torna-se obrigatório |

| Pontos | Pontos a serem alocados. |

| Atribuir pontos aos usuários atribuídos | Se marcado, os usuários atribuídos ao documento de referência receberão pontos. por exemplo. Se os usuários Reema e Jai forem atribuídos a uma tarefa específica, ambos, ou seja, Reema e Jai, receberão pontos quando o documento atender à condição |

| Campo do usuário | Campo a partir do qual o usuário será selecionado, por exemplo. `Resolvido por`, `Modificado por`, `Proprietário`, etc. podem ser usados. Se `Modificado por` for selecionado, a última pessoa a satisfazer a condição doc receberá os pontos. |

| Campo multiplicador | Campo que armazena o valor do multiplicador. Este campo pode receber valores numéricos e decimais que serão multiplicados pelos pontos definidos na regra.  Por exemplo: 2 (multiplicador) \* 10 (pontos definidos na regra) = 20 pontos |

| Condição | Condição para atribuição de pontos. ex. `doc.status == 'Fechado'`A condição acima irá verificar se o campo `status` no documento é 'Fechado' e se sim, então os pontos serão atribuído ao usuário. |

| Inscreva-se apenas uma vez | A regra será aplicada apenas uma vez por documento. |





> 
> **Observação:** o campo do usuário e o campo do multiplicador são obtidos do tipo de documento de referência.
> 
> 
> 


## 3. Como criar regras de pontos de energia?



> 
> Pesquise **Regra de Pontos de Energia** > crie uma nova Regra de Pontos de Energia
> 
> 
> 


Dê uma olhada no seguinte exemplo de regra:
![](/files/issue-closed-rule.png)
A captura de tela acima é a regra para **Fechamento de problema**.
Assim, quando qualquer usuário fechar o problema, ele será recompensado com **10** pontos.


Outros casos podem ser cobertos de forma semelhante.


Suponha que você queira criar uma regra em que um usuário obtenha pontos ao concluir uma tarefa,
você pode fazer isso criando a seguinte regra
![](/files/task-complete-rule.png)


## 4. Características:


### 4.1 Alocação automática de pontos


Com base nas regras de pontos de energia criadas, os usuários receberão pontos automaticamente quando concluírem atividades rastreadas usando o Sistema de Pontos de Energia.


### 4.2 Sistema de revisão


O sistema de avaliação pode ser usado para "Apreciar" ou "Criticar" o trabalho de alguém.


Confira o seguinte GIF para o processo de revisão.
![](/files/review-system.gif)
Para revisão, o usuário precisa ter pontos de revisão que podem ser atribuídos pelo gerente do sistema por meio de **Configurações de ponto de energia**.


Você também pode configurar a alocação de ponto de revisão automática em 'Configurações de ponto de energia':
![](/files/auto-review-point-allocation.png)


### 4.3 Tabela de classificação


Vá para Social Home > Tabela de classificação (barra de navegação lateral)


A tabela de classificação mostra a posição do usuário na organização.


![](/files/leaderboard.png)


### 5. Tópicos Relacionados


1. [Acompanhamento de marcos](/docs/pt/automation/milestone-tracker)
