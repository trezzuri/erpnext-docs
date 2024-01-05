# Orçamento



**O orçamento é um plano financeiro que ajuda a controlar as despesas da empresa.**


No ERPNext, você pode definir e gerenciar orçamentos em relação a um Centro de Custo ou Projeto. Isso é útil para controlar suas despesas. Com a versão 12, você também pode criar [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions) separadas para marcar transações com campos diferentes.


Por exemplo, se você estiver fazendo vendas on-line, você pode definir um orçamento para anúncios de pesquisa e configurar o ERPNext para interromper ou avisá-lo sobre gastos excessivos além do orçamento definido.


Os orçamentos também são ótimos para fins de planejamento. Ao fazer planos para o próximo exercício financeiro, normalmente você terá como meta uma receita com base na qual definiria suas despesas. Definir um orçamento garantirá que suas despesas não saiam do controle em nenhum momento.


Para acessar a lista de Orçamentos, acesse:
> Home > Contabilidade > Centro de Custo e Orçamento > Orçamento


## 1. Como criar um novo orçamento


1. Vá para a lista Orçamento e clique em Novo.
2. Selecione o orçamento, Centro de custo, Projeto ou uma [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions).
3. Na tabela de contas, selecione uma conta de receitas/despesas para a qual um orçamento será definido. Vamos definir um orçamento para despesas telefônicas para o ano.
![Budget](/files/budget.png)
4. Insira o valor do orçamento para essa conta.
5. Salvar e enviar.


## 2. Recursos


### 2.1 Distribuição Mensal


Você também pode definir um registro de Distribuição Mensal para distribuir o orçamento entre os meses. Se você não definir a distribuição mensal, o ERPNext calculará o orçamento anualmente ou em proporção igual para cada mês.


![Distribuição mensal](/files/monthly-budget-distribution.png)


### 2.2 Ações de controle (alertas)


As ações de controle podem ser acionadas quando:


* Uma [Solicitação de material](/docs/pt/stock/material-request) está sendo enviada
* Um [pedido de compra](/docs/pt/buying/purchase-order) está sendo enviado
* Quando uma despesa real está sendo lançada (por meio de um lançamento contábil manual ou fatura de compra).


Você pode definir uma ação de controle no Orçamento com base em Solicitações de Materiais, Pedidos de Compra ou em despesas reais. Além disso, você pode definir uma ação de controle para orçamentos anuais ou mensais.


![Ações de controle](/files/control-actions.png)


Existem três tipos de ações de controle.


* **Parar**: isso não permitirá que os usuários enviem a transação.
* **Avisar**: mostrará uma mensagem de aviso, mas permitirá que o usuário envie a transação.
* **Ignorar**: isso não impedirá o usuário de enviar transações nem mostrará uma mensagem de erro.


Você pode definir ações separadas para orçamentos mensais e anuais. Se você exceder o orçamento, um aviso será mostrado:


![Aviso de orçamento](/files/budget-warning.png)


Observe que um aviso semelhante será acionado para qualquer tipo de transação definida no orçamento para os chefes de conta específicos.


## 3. Relatório de variação orçamentária


A qualquer momento, você pode verificar o Relatório de variação do orçamento para analisar as despesas reais incorridas versus o orçamento alocado em um centro de custo ou projeto.


Para verificar o relatório de variação do orçamento, acesse:


> Home > Contabilidade > Centro de Custo e Orçamento > Relatório de Variação Orçamentária


![Relatório de variação do orçamento](/files/budget-variance-report.png)


## 4. Vídeo


Aqui está um vídeo de demonstração:






## 5. Tópicos Relacionados


1. [Centro de custos](/docs/pt/accounts/cost-center)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
3. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



