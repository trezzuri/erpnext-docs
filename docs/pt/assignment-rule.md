# Regra de Atribuição




> 
> Introduzido na versão 12
> 
> 
> 


**Uma regra de atribuição permite configurar a atribuição automática de documentos aos usuários.**


Para atribuir os tickets de suporte automaticamente entre os funcionários que trabalham no suporte, uma Regra de Atribuição pode ser usada.


Para acessar a Regra de Atribuição, acesse:



> 
> Página inicial > Configurações > Regra de atribuição
> 
> 
> 


## 1. Como criar uma regra de atribuição


Para configurar uma atribuição automática:


1. Vá para a lista Regra de Atribuição e clique em Novo.
2. Selecione o tipo de documento que deseja atribuir automaticamente (por exemplo **Emissão**).
3. Escreva a "Descrição" que será adicionada à tarefa.
4. Selecione a condição para a atribuição.
Você pode escrever expressões Python simples para atribuição automática em `Assign Rule`, `Close Rule` e `Unassign Rule`. Você terá acesso a todas as propriedades do documento e poderá usar operadores como >, <, ==, etc e também múltiplas condições como `and` e `or`.


Exemplos:


	* `status == "Aberto"`
	* `issue_type == "Técnico" e prioridade=="Alta" e status == "Aberto"`
5. Selecione a regra de atribuição.


![Regra de atribuição](/files/assignment-rule-select.png)


	* **Round Robin**: atribua cada documento a um usuário em sequência.
	* **Balanceamento de carga**: atribua novos documentos ao usuário que tiver o menor número de atribuições.
	
	
	Selecione a lista de usuários aos quais esta regra de atribuição será aplicada:
	![Usuários na regra de atribuição](/files/auto-assign-2.png)
	* **Com base no campo**: introduzida na v13, esta regra pode ser usada para atribuir um documento ao usuário definido no campo configurado.
	
	
	Selecione o campo Link do usuário que determinará a quem esta regra de atribuição será aplicada:
	![Atribuição de campo](/files/field-auto-assign.png)
6. Salvar.


Você pode usar as propriedades do documento no campo Descrição que fará parte da tarefa. As regras de atribuição de "prioridade" mais alta serão aplicadas primeiro.


Exemplo:


O problema de alta prioridade *O upload do arquivo não funciona* foi atribuído a você.


### 1.1 Regras de atribuição múltipla


Você também pode configurar várias atribuições automáticas para cada tipo de documento. Aquela com a prioridade mais alta será aplicada primeiro.


![Regra de atribuição com prioridade mais alta](/files/assignment-rule-with-higher-priority.png)


regra de atribuição com prioridade mais alta


### 1.2 Definindo a data de vencimento da tarefa


Você pode definir automaticamente datas de vencimento para tarefas com base no campo de data no documento de referência.


Exemplo:


Se desejar definir uma data de vencimento para a atribuição do problema com base na data "Resolução até" do problema, você pode fazer isso selecionando o campo "Resolução até" na opção `Data de vencimento baseada em` na regra de atribuição.


![Data de vencimento baseada em](/files/assignment-rule-due-date-based-on.png)


**Observação:**


* A opção "Data de vencimento com base em" não estará disponível se o "Tipo de documento" ainda não estiver selecionado ou se o tipo de documento selecionado não tiver nenhum campo "Data" ou "Data e hora".
* A data de vencimento na tarefa/tarefa será atualizada sempre que o valor do campo "Data de vencimento com base em" for atualizado no documento de referência.


### 2. Tópicos Relacionados


1. [Fluxos de trabalho](/docs/pt/setting-up/workflows)
2. [Ações de fluxo de trabalho](/docs/pt/setting-up/workflow-actions)



