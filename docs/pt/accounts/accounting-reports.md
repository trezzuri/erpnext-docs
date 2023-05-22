# Relatórios Contábeis


Alguns dos principais relatórios contábeis são:


## 1. Empresa e Contas


### Razão geral


Vá para: **Contas > Empresa e contas > Razão geral**.


O Razão Geral é um relatório detalhado de todas as transações lançadas em cada conta e, para cada transação, há uma conta de Crédito e Débito, portanto, lista todas elas.


O relatório é baseado na tabela GL Entry e pode ser filtrado por vários filtros predefinidos, como Conta, Centros de Custo, Parte, Projeto e Período, etc. Isso ajuda você a obter uma atualização completa de todas as entradas lançadas em um período contra qualquer conta. O resultado pode ser agrupado por Conta, Voucher/Transação e Parte com saldos de abertura e fechamento para cada grupo. No caso de contabilidade em várias moedas, também existe a opção de verificar os valores em qualquer outra moeda que não seja a moeda base da empresa.


![General Ledger](/files/general-ledger.png)


## 2. Demonstrativos Contábeis


### 2.1 Contas a receber e contas a pagar (AR/AP)


Vá para: **Contas > Extratos Contábeis > Contas a Receber**.


Estes relatórios ajudam-no a controlar a quantidade pendente de Clientes e Fornecedores. Ele também fornece análise de vencimento, ou seja, uma divisão do valor pendente com base no período em que o valor está pendente.


![Contas a receber](/files/accounts-receivable.png)


#### 2.1.1 Contas a receber com base em condições de pagamento


Você também pode ver contas a receber com base em [condições de pagamento](/docs/pt/accounts/payment-terms).


O relatório de contas a receber com base nas condições de pagamento pode ser visto clicando na caixa de seleção 'Baseado nas condições de pagamento', conforme mostrado na captura de tela a seguir.


![Contas a receber com base em condições de pagamento](/files/accounts-receivable-based-on-payment-terms.png)


O valor pendente em relação a cada condição de pagamento pode ser visto. **Valor faturado** mostra o valor de cada condição de pagamento e **Valor pago** mostra o valor pago em relação a cada condição de pagamento. O pagamento contra cada prazo é alocado na ordem FIFO.


![Contas a receber](/files/accounts-receivable-2.png)



```
![](/docs/v13/assets/img/accounts/)

```

### 2.2 Balancete


Vá para: **Contas > Extratos Contábeis > Balancete**.


Um balancete é um relatório contábil que lista os saldos de todas as suas contas
(“Ledger” e “Grupo”) para qualquer período de relatório. Uma empresa prepara um balancete periodicamente, geralmente no final de cada período de relatório. O objetivo geral de produzir um balancete é garantir que os lançamentos no sistema de contabilidade de uma empresa estejam matematicamente corretos. Os totais das colunas Débito e Crédito devem ser iguais para qualquer período, para garantir que as entradas estejam corretas. No ERPNext, o relatório mostra as seguintes colunas:


* Abertura (Dr): Saldo devedor inicial a partir da data
* Abertura (Cr): Saldo de crédito inicial na data inicial
* Débito: Valor total debitado na conta entre o período selecionado
* Crédito: valor total creditado na conta entre o período selecionado
* Fechamento (Dr): Saldo devedor final como em To Date
* Fechamento (Cr): Saldo de crédito final como em To Date


Também existem outras opções para incluir ou excluir entradas de encerramento de período, mostrar/ocultar contas com saldo zero e para mostrar saldos P&L (receitas e despesas) não encerrados do ano fiscal anterior. Todos os valores do relatório são mostrados na moeda base da empresa.


![Balancete](/files/trial-balance.png)


### 2.3 Balanço


Vá para: **Contas > Extratos Contábeis > Balanço**.


Um Balanço é a demonstração financeira de uma empresa que declara ativos, passivos e patrimônio em um determinado momento.


O Balanço no ERPNext lhe dá mais flexibilidade para analisar sua posição financeira. Você pode executar o relatório em vários anos para comparar valores. Você pode verificar valores para um livro financeiro ou centro de custo específico. Você também pode escolher qualquer outra moeda para exibir os saldos.


![Balance Sheet](/files/balance-sheet-report.png)


### 2.4 Demonstrativo do fluxo de caixa


Vá para: **Contas > Demonstrativos contábeis > Fluxo de caixa**.


Um fluxo de caixa é uma demonstração financeira que mostra as entradas e saídas de caixa ou equivalentes de caixa de uma empresa. É usado para analisar a posição de liquidez da empresa.


![Cash Flow](/files/cash-flow-report.png)


### 2.5 Declaração de lucros e perdas


Vá para: **Contas > Extratos Contábeis > Demonstrativo de Lucros e Perdas**.


Uma Demonstração de Lucros e Perdas é uma demonstração financeira que resume todas as receitas e despesas em um determinado período. O relatório também é conhecido como Demonstração de P&L.


No ERPNext, você pode executar o relatório em vários anos/períodos para comparar os valores. Você também pode verificar valores para um Livro Financeiro, Projeto ou Centro de Custo específico. Você também pode escolher qualquer outra moeda para exibir os saldos. Se você estiver executando o relatório para ver os saldos trimestrais / mensais, poderá escolher se deseja mostrar os saldos acumulados ou apenas para cada período.


![Relatório de lucros e perdas](/files/profit-and-loss-report.png)


### 2.6 Demonstrações financeiras consolidadas


Vá para: **Contas > Demonstrativos Contábeis > Demonstrativo Financeiro Consolidado**.


O relatório apresenta uma visão consolidada do Balanço, Demonstração de Lucros e Perdas e Fluxo de Caixa de uma empresa do grupo, mesclando as demonstrações financeiras de todas as empresas subsidiárias. Ele mostra os saldos de todas as empresas individuais e também os saldos acumulados de uma empresa do grupo.


![Demonstrações financeiras consolidadas](/files/consolidated-financial-statement.png)


## 3. Impostos


### 3.1 Registro de vendas e compras


Vá para: **Contas > Impostos > Registro de vendas *ou* Registro de compras**.


O relatório Cadastro de Compras e Vendas mostra todas as transações de Compras e Vendas de um determinado período com valor faturado e detalhes de impostos. Neste relatório, cada imposto tem uma coluna separada, para que você possa facilmente obter o total de impostos cobrados/pagos por um período para cada tipo de imposto individual, o que ajuda a pagar os impostos ao governo.


![Sales Register](/files/sales-register.png)


## 4. Orçamento e Centro de Custo


### 4.1 Variação de orçamento


Vá para: **Contas > Orçamento e centro de custo > Relatório de variação de orçamento**.


No ERPNext, você pode atribuir orçamento de despesas para uma conta de despesas em relação a qualquer centro de custo específico. Este relatório oferece uma comparação entre as despesas orçadas e reais e a variação (a diferença entre as duas) na visualização mensal/trimestral/anual.


![Budget Variance](/files/budget-variance-report.png)


## 5. Relatórios fiscais para a Índia


### 5.1 GSTR-1 (Índia)


Vá para: **Contas > Imposto sobre bens e serviços (GST Índia) > GSTR-1**.


O relatório GSTR-1 ajuda os usuários indianos a arquivar a declaração mensal de suprimentos externos. Este relatório mostra todas as transações de vendas da empresa no formato especificado pelo governo. A saída do relatório é alterada com base no tipo de negócio selecionado (B2B, B2C Grande, B2C Pequeno, CDNR e Exportação).


![GSTR-1](/files/gstr-1.png)


### 5.2 GSTR-2 (Índia)


Vá para: **Contas > Imposto sobre bens e serviços (GST Índia) > GSTR-2**.


O relatório GSTR-2 ajuda os usuários indianos a arquivar a declaração mensal de suprimentos internos. O relatório fornece os detalhes de todos os fornecimentos internos de bens ou serviços recebidos durante um mês, no formato especificado pelo governo.


![GSTR-2](/files/gstr-2.png)


## 6. Análise


### 6.1 Registro de compras e vendas de itens


Vá para: **Contas > Analytics > Registro de vendas por item *ou* Registro de compra por item**.


O relatório Item Wise Sales and Purchase Register mostra todas as transações de vendas e compras para um determinado período com taxa de item, quantidade, valor e detalhes de impostos. Neste relatório, os impostos têm uma coluna separada, para que você possa obter facilmente os impostos individuais para cada item individual. A partir deste relatório, você pode ver quais itens são mais vendidos ou comprados.


![Item Wise Sales Register](/files/item-wise-sales-report.png)


Uma análise mais detalhada também pode ser feita usando o filtro 'Agrupar por', que fornece dados de vendas para um cliente, fornecedor, território etc. específico. Você pode descobrir qual item é mais popular em qual região ou qual cliente está comprando qual item mais.


![Group By Sales Register](/files/group-by-sales-register.png)


### 6.2 Tendências de faturas de vendas ou compras


Vá para: **Contas > Analytics > Tendências de fatura de vendas *ou* Tendências de fatura de compra**.


Outro relatório muito útil são as tendências de faturas. A partir deste relatório, você pode obter facilmente os itens de tendências mensais, trimestrais, semestrais ou anuais. Você terá a ideia de vendas e compras em quantidade e valor.


![Tendências de fatura de vendas](/files/sales-invoice-trends.png)


## 7. Para faturar


* **Itens pedidos a serem cobrados:** o relatório mostra os itens que foram pedidos pelos clientes, contra os quais as vendas
A fatura não foi criada/parcialmente criada.
* **Itens entregues a serem cobrados:** os itens que foram entregues aos clientes, mas a Nota Fiscal de venda não foi criada/criada parcialmente.
* **Itens do pedido de compra a serem faturados:** o relatório mostra os itens que foram solicitados aos fornecedores, mas a fatura de compra não foi criada/criada parcialmente.
* **Itens recebidos a serem faturados:** os itens que foram recebidos dos fornecedores, mas a fatura de compra não foi criada/criada parcialmente.


## 8. Outros Relatórios


### 8.1 Balanço de avaliação da Party Wise


Vá para: **Contas > Outros relatórios > Balancete para a parte**.
Normalmente, você pode precisar ver o balancete de seus clientes e fornecedores. Você pode obter facilmente para todos os seus clientes ou fornecedores e também para indivíduos.


![Balancete para Party](/files/party-wise-trail-balance.png)


### 8.2 Saldo de crédito do cliente


O relatório mostra o limite de crédito, pendente e saldo de crédito para cada cliente.


![Saldo de crédito do cliente](/files/customer-credit-balance.png)

