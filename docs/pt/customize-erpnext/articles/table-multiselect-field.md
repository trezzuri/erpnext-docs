# Campo MultiSelect da tabela



O campo Table MultiSelect é muito semelhante ao Link Field. A principal diferença é que o campo Table MultiSelect permite selecionar vários valores.


Vamos considerar um exemplo para entender o mesmo. Digamos que você queira atribuir um ToDo a vários usuários, conforme mostrado abaixo:


![Campo MultiSelect de tabela](/files/table-multiselect-field.png)


Você pode adicionar um campo MultiSelect de tabela usando as seguintes etapas:


## Etapa 1: Crie um DocType filho.


Crie um novo DocType, ative as caixas de seleção 'Is Child Table' e 'Editable Grid' e adicione um campo com o tipo 'Link' conforme mostrado abaixo.


Defina o campo do link como obrigatório. Certifique-se de que o campo na tabela secundária esteja marcado como "Na visualização de lista".


![DocType for Table MultiSelect](/files/doctype-for-table-multi-select.png)


## Etapa 2: adicione um campo com o tipo 'Table MultiSelect'.


Crie um campo com o tipo 'Table MultiSelect' e adicione o DocType criado no primeiro passo em 'options'.


![Campo com tipo Table MultiSelect](/files/multi-select-field.png)


Você pode remover qualquer valor selecionado clicando na cruz ao lado do valor selecionado ou colocando o cursor próximo ao valor e pressionando Backspace.


Este campo permite que um valor seja selecionado apenas uma vez.


> Observação: os campos MultiSelect da tabela não podem ser adicionados em DocTypes filhos.



