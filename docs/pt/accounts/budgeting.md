# Orçamento


**Orçamento é um plano financeiro que auxilia no controle das despesas da Empresa.**


No ERPNext, você pode definir e gerenciar orçamentos em relação a um Centro de Custo ou Projeto. Isso é útil para controlar suas despesas. Com a versão 12, você também pode criar [Dimensões contábeis](/docs/v13/user/manual/en/accounts/accounting-dimensions) separadas para marcar transações com campos diferentes.


Por exemplo, se você estiver fazendo vendas on-line, poderá definir um orçamento para anúncios de pesquisa e configurar o ERPNext para interromper ou avisá-lo sobre gastos excessivos além do orçamento definido.


Os orçamentos também são ótimos para fins de planejamento. Ao fazer planos para o próximo exercício financeiro, você normalmente visa uma receita com base na qual definiria suas despesas. Definir um orçamento garantirá que suas despesas não saiam do controle em nenhum momento.


Para acessar a lista de Orçamento, acesse:



>
> Home > Contabilidade > Centro de Custo e Orçamento > Orçamento
>
>
>


## 1. Como criar um novo orçamento


1. Vá para a lista de Orçamento e clique em Novo.
2. Selecione o orçamento, Centro de custo, Projeto ou [Dimensões contábeis](/docs/v13/user/manual/en/accounts/accounting-dimensions).
3. Na tabela de contas, selecione uma conta de receita/despesa para a qual um orçamento deve ser definido. Vamos definir um orçamento para despesas de telefone para o ano.
![Orçamento](/files/budget.png)
4. Insira o valor do orçamento para essa conta.
5. Salve e envie.


## 2. Características


### 2.1 Distribuição Mensal


Você também pode definir um registro de Distribuição Mensal para distribuir o orçamento entre os meses. Se você não definir a distribuição mensal, o ERPNext calculará o orçamento anualmente ou em igual proporção para todos os meses.


![Distribuição mensal](/files/monthly-budget-distribution.png)


### 2.2 Ações de Controle (Alertas)


As ações de controle podem ser acionadas quando:


* Uma [solicitação de material](/docs/v13/user/manual/en/stock/material-request) está sendo enviada
* Um [pedido de compra](/docs/v13/user/manual/en/buying/purchase-order) está sendo enviado
* Quando uma despesa real está sendo lançada (através de um lançamento contábil manual ou uma fatura de compra).


Você pode definir uma ação de controle no orçamento com base em solicitações de materiais, pedidos de compra ou despesas reais. Além disso, você pode definir uma ação de controle para orçamentos anuais ou mensais.


![Ações de controle](/files/control-actions.png)


Existem três tipos de ações de controle.


* **Parar**: Isso não permitirá que os usuários enviem a transação.
* **Warn**: Isso mostrará uma mensagem de aviso, mas permite que o usuário envie a transação.
* **Ignorar**: Isso não impedirá o usuário de enviar transações nem exibirá uma mensagem de erro.


Você pode definir ações separadas para orçamentos mensais e anuais. Se você exceder o orçamento, um aviso será exibido:


![Aviso de orçamento](/files/budget-warning.png)


Observe que um aviso semelhante será acionado para qualquer tipo de transação definida no orçamento para os chefes de conta específicos.


## 3. Relatório de variação orçamentária


A qualquer momento, você pode verificar o Relatório de variação do orçamento para analisar a despesa real incorrida em relação ao orçamento alocado em relação a um centro de custo ou projeto.


Para verificar o relatório de variação orçamentária, acesse:



>
> Home > Contabilidade > Centro de custo e orçamento > Relatório de variação orçamentária
>
>
>


![Relatório de variação orçamentária](/files/budget-variance-report.png)


## 4. Vídeo


Aqui está uma demonstração em vídeo:






## 5. Tópicos Relacionados


1. [Centro de custo](/docs/v13/user/manual/en/accounts/cost-center)
2. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
3. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)