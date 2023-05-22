# Regra de Atribuição



> 
> Introduzido na versão 12
> 
> 
> 


**Uma regra de atribuição permite configurar a atribuição automática de documentos aos usuários.**


Para atribuir os tickets de suporte automaticamente entre os funcionários que trabalham no suporte, uma regra de atribuição pode ser usada.


Para acessar a regra de atribuição, acesse:



> 
> Página inicial > Configurações > Regra de atribuição
> 
> 
> 


## 1. Como criar uma regra de atribuição


Para configurar uma atribuição automática:


1. Vá para a lista Regra de Atribuição, clique em Novo.
2. Selecione o tipo de documento que deseja atribuir automaticamente (por exemplo, **Problema**).
3. Escreva a "Descrição" que será adicionada ao Afazer.
4. Selecione a condição para a atribuição.
Você pode escrever expressões Python simples para atribuição automática em `Assign Rule`, `Close Rule` e `Unassign Rule`. Você terá acesso a todas as propriedades do documento e poderá usar operadores como >, <, ==, etc e também várias condições como `e` e `ou`.


Exemplos:


	* `status == "Aberto"`
	* `issue_type == "Técnico" e prioridade=="Alta" e status == "Aberto"`
5. Selecione a regra de atribuição.


![Assignment Rule](/files/assignment-rule-select.png)


	* **Round Robin**: atribui cada documento a um usuário em sequência.
	* **Balanceamento de carga**: Atribua novos documentos ao usuário que tiver o menor número de atribuições.
	
	
	Selecione a lista de usuários aos quais esta regra de atribuição será aplicada:
	![Users in Assignment Rule](/files/auto-assign-2.png)
	* **Com base no campo**: introduzida na v13, esta regra pode ser usada para atribuir um documento ao usuário definido no campo configurado.
	
	
	Selecione o campo Link do usuário que determinará a quem esta regra de atribuição será aplicada:
	![Field Assign](/files/field-auto-assign.png)
6. Salvar.


Você pode usar as propriedades do documento no campo Descrição que farão parte da tarefa. Regras de atribuição de 'prioridade' mais alta serão aplicadas primeiro.


Exemplo:


Problema de alta prioridade *O upload de arquivo não está funcionando* foi atribuído a você.


### 1.1 Regras de atribuição múltipla


Você também pode configurar várias atribuições automáticas para cada tipo de documento, aquele com a prioridade mais alta será aplicado primeiro.


![Regra de atribuição com prioridade mais alta](/files/assignment-rule-with-higher-priority.png)


regra de atribuição com prioridade mais alta


### 1.2 Definindo a data de vencimento para a atribuição


Você pode definir automaticamente as datas de entrega das tarefas com base no campo de data no documento de referência.


Exemplo:


Se você deseja definir uma data de vencimento na atribuição do problema com base na data "Resolução até" do problema, pode fazê-lo selecionando o campo "Resolução até" na opção `Data de vencimento baseada em` na regra de atribuição.


![Data de vencimento baseada em](/files/assignment-rule-due-date-based-on.png)


**Observação:**


* A opção "Data de vencimento baseada em" não estará disponível se o "Tipo de documento" ainda não estiver selecionado ou se o Tipo de documento selecionado não tiver nenhum campo "Data" ou "Datahora".
* A data de vencimento na atribuição/ToDo será atualizada sempre que o valor do campo "Due Date Based On" for atualizado no documento de referência.


### 2. Tópicos Relacionados


1. [Fluxos de trabalho](/docs/pt/setting-up/workflows)
2. [Ações do fluxo de trabalho](/docs/pt/setting-up/workflow-actions)
