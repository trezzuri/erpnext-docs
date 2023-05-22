# Campo de seleção múltipla da tabela


O campo Table MultiSelect é muito semelhante ao Link Field. A principal diferença é que o campo Table MultiSelect permite selecionar vários valores.


Vamos considerar um exemplo para entender o mesmo. Digamos que você queira atribuir um ToDo a vários usuários, conforme mostrado abaixo:


![Table MultiSelect Field](/files/table-multiselect-field.png)


Você pode adicionar um campo MultiSelect de tabela usando as seguintes etapas:


## Etapa 1: criar um DocType filho.


Crie um novo DocType, marque as caixas de seleção 'Is Child Table' e 'Editable Grid' e adicione um campo com o tipo 'Link' conforme mostrado abaixo.


Defina o campo do link como obrigatório. Certifique-se de que o campo dentro da tabela filha esteja marcado como "Na exibição de lista".


![DocType for Table MultiSelect](/files/doctype-for-table-multi-select.png)


## Etapa 2: Adicione um campo com o tipo 'Table MultiSelect'.


Crie um campo com o tipo 'Table MultiSelect' e adicione o DocType criado na primeira etapa em 'options'.


![Campo com tipo Table MultiSelect](/files/multi-select-field.png)


Você pode remover qualquer valor selecionado clicando no sinal de cruz ao lado do valor selecionado ou colocando o cursor ao lado do valor e pressionando Backspace.


Este campo permite que um valor seja selecionado apenas uma vez.



> 
> Observação: os campos MultiSelect da tabela não podem ser adicionados em DocTypes filhos.
> 
> 
> 

