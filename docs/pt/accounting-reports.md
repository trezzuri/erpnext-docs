# Relatórios contábeis



Alguns dos principais relatórios contábeis são:


## 1. Empresa e contas


### Contabilidade Geral


Acesse: **Contas > Empresa e contas > Razão Geral**.


O Razão Geral é um relatório detalhado de todas as transações lançadas em cada conta e para cada transação há uma conta de Crédito e Débito, portanto, lista todas elas.


O relatório é baseado na tabela Entrada Contábil e pode ser filtrado por vários filtros predefinidos, como Conta, Centros de Custo, Parte, Projeto e Período, etc. contra qualquer conta. O resultado pode ser agrupado por Conta, Voucher/Transação e Parte com saldos iniciais e finais para cada grupo. No caso de contabilidade multimoeda, também existe a opção de verificar os valores em qualquer outra moeda que não a moeda base da empresa.


![General Ledger](/files/general-ledger.png)


## 2. Demonstrações Contábeis


### 2.1 Contas a Receber e Contas a Pagar (AR/AP)


Acesse: **Contas > Demonstrativos Contábeis > Contas a Receber**.


Esses relatórios ajudam você a acompanhar o valor pendente de Clientes e Fornecedores. Ele também fornece análise de antiguidade, ou seja, uma divisão do valor pendente com base no período em que o valor está pendente.


![Contas a receber](/files/accounts-receivable.png)


#### 2.1.1 Contas a receber com base nas condições de pagamento


Você também pode ver as contas a receber com base nas [condições de pagamento](/docs/pt/accounts/payment-terms).


O relatório de contas a receber com base nas condições de pagamento pode ser visto clicando na caixa de seleção 'Com base nas condições de pagamento', conforme mostrado na captura de tela a seguir.


![Contas a receber com base nas condições de pagamento](/files/accounts-receivable-based-on-payment-terms.png)


O valor pendente de cada prazo de pagamento pode ser visto. **Valor faturado** mostra o valor de cada condição de pagamento e **Valor pago** mostra o valor pago em cada condição de pagamento. O pagamento de cada prazo é alocado na ordem FIFO.


![Contas a receber](/files/accounts-receivable-2.png)


`![](/docs/v13/assets/img/accounts/)`
### 2.2 Balancete


Acesse: **Contas > Demonstrativos Contábeis > Balancete**.


Um balancete é um relatório contábil que lista os saldos de todas as suas contas
(“Ledger” e “Group”) para qualquer período de relatório. Uma empresa prepara um balancete periodicamente, geralmente no final de cada período de relatório. O objetivo geral da produção de um balancete é garantir que os lançamentos no sistema de contabilidade de uma empresa sejam matematicamente corretos. Os totais das colunas Débito e Crédito devem ser iguais para qualquer período, para garantir que as entradas estejam corretas. No ERPNext, o relatório mostra as seguintes colunas:


* Abertura (Dr): Saldo devedor de abertura na data inicial
* Abertura (Cr): saldo de crédito inicial na data inicial
* Débito: valor total debitado na conta entre o período selecionado
* Crédito: valor total creditado na conta entre o período selecionado
* Fechamento (Dr): saldo devedor final como em até a data
* Fechamento (Cr): Saldo de crédito final até a data


Existem também algumas outras opções para incluir ou excluir lançamentos de encerramento de período, mostrar/ocultar contas com saldo zero e mostrar saldos não fechados de lucros e perdas (receitas e despesas) do ano fiscal anterior. Todos os números do relatório são apresentados na moeda base da empresa.


![Trial Balance](/files/trial-balance.png)


### 2.3 Balanço patrimonial


Acesse: **Contas > Demonstrações Contábeis > Balanço Patrimonial**.


Um Balanço Patrimonial é a demonstração financeira de uma empresa que declara ativos, passivos e patrimônio líquido em um determinado momento.


O Balanço Patrimonial no ERPNext oferece mais flexibilidade para analisar sua posição financeira. Você pode executar o relatório em vários anos para comparar valores. Você pode verificar os valores de um Livro Financeiro ou Centro de Custo específico. Você também pode escolher qualquer outra moeda para exibir os saldos.


![Balance Sheet](/files/balance-sheet-report.png)


### 2.4 Demonstração do fluxo de caixa


Acesse: **Contas > Demonstrações Contábeis > Fluxo de Caixa**.


Um fluxo de caixa é uma demonstração financeira que mostra as entradas e saídas de dinheiro ou equivalentes de caixa de uma empresa. É utilizado para analisar a posição de liquidez da empresa.


![Fluxo de caixa](/files/cash-flow-report.png)


### 2.5 Demonstração de lucros e perdas


Acesse: **Contas > Demonstrações Contábeis > Demonstração de Lucros e Perdas**.


Uma Demonstração de Lucros e Perdas é uma demonstração financeira que resume todas as receitas e despesas em um determinado período. O relatório também é conhecido como Demonstração de P&L.


No ERPNext, você pode executar o relatório em vários anos/períodos para comparar os valores. Você também pode verificar valores de um Livro Financeiro, Projeto ou Centro de Custo específico. Você também pode escolher qualquer outra moeda para exibir os saldos. Se você estiver executando o relatório para ver os saldos trimestrais/mensais, poderá escolher se deseja mostrar os saldos acumulados ou apenas para cada período.


![Relatório de lucros e perdas](/files/profit-and-loss-report.png)


### 2.6 Demonstrações financeiras consolidadas


Acesse: **Contas > Demonstrações Contábeis > Demonstrações Financeiras Consolidadas**.


O relatório mostra uma visão consolidada do Balanço Patrimonial, da Demonstração de Lucros e Perdas e do Fluxo de Caixa de uma empresa do grupo, mesclando as demonstrações financeiras de todas as empresas subsidiárias. Mostra os saldos de todas as empresas individuais e também os saldos acumulados de uma empresa do grupo.


![Demonstrações financeiras consolidadas](/files/consolidated-financial-statement.png)


## 3. Impostos


### 3.1 Registro de vendas e compras


Acesse: **Contas > Impostos > Registro de Vendas *ou* Registro de Compras**.


O relatório Registro de Vendas e Compras mostra todas as transações de Vendas e Compras de um determinado período com valor faturado e detalhes fiscais. Neste relatório, cada imposto tem uma coluna separada, para que você possa obter facilmente o total de impostos cobrados/pagos em um período para cada tipo de imposto individual, o que ajuda a pagar os impostos ao governo.


![Registro de vendas](/files/sales-register.png)


## 4. Orçamento e Centro de Custo


### 4.1 Variação do orçamento


Acesse: **Contas > Orçamento e centro de custo > Relatório de variação do orçamento**.


No ERPNext, você pode atribuir orçamento de despesas para uma conta de despesas em relação a qualquer centro de custo específico. Este relatório fornece uma comparação entre as despesas orçadas e reais e a variação (a diferença entre as duas) na visão mensal/trimestral/anual.


![Variação do orçamento](/files/budget-variance-report.png)


## 5. Relatórios fiscais para a Índia


### 5.1 GSTR-1 (Índia)


Acesse: **Contas > Imposto sobre bens e serviços (GST Índia) > GSTR-1**.


O relatório GSTR-1 ajuda os usuários indianos a registrar declarações mensais de suprimentos enviados. Este relatório mostra todas as transações de vendas da empresa no formato especificado pelo governo. A saída do relatório é alterada com base no tipo de negócio selecionado (B2B, B2C Grande, B2C Pequeno, CDNR e Exportação).


![GSTR-1](/files/gstr-1.png)


### 5.2 GSTR-2 (Índia)


Acesse: **Contas > Imposto sobre Bens e Serviços (GST Índia) > GSTR-2**.


O relatório GSTR-2 ajuda os usuários indianos a registrar declarações mensais de suprimentos recebidos. O relatório fornece detalhes de todos os fornecimentos de bens ou serviços recebidos durante um mês, no formato especificado pelo governo.


![GSTR-2](/files/gstr-2.png)


## 6. Análise


### 6.1 Registro de vendas e compras por item


Acesse: **Contas > Análise > Registro de vendas por item *ou* Registro de compra por item**.


O relatório de registro de vendas e compras de itens mostra todas as transações de vendas e compras de um determinado período com taxa de item, quantidade, valor e detalhes de impostos. Neste relatório, os impostos têm uma coluna separada, para que você possa obter facilmente os impostos individuais para cada item individual. A partir deste relatório, você pode ver quais itens são mais vendidos ou comprados.


![Item Wise Sales Register](/files/item-wise-sales-report.png)


Uma análise mais detalhada também pode ser feita usando o filtro 'Agrupar por' que fornece dados de vendas para um cliente, fornecedor, território específico, etc. Você pode descobrir qual item é mais popular em qual região ou qual cliente está comprando qual item mais.


![Agrupar por registro de vendas](/files/group-by-sales-register.png)


### 6.2 Tendências de faturas de vendas ou compras


Acesse: **Contas > Análise > Tendências de faturas de vendas *ou* Tendências de faturas de compras**.


Outro relatório muito útil é o de tendências de faturas. A partir dele você pode obter facilmente os itens de tendência mensalmente, trimestralmente, semestralmente ou anualmente. Você terá uma ideia de vendas e compras tanto em quantidade quanto em valor.


![Tendências da fatura de vendas](/files/sales-invoice-trends.png)


## 7. Para faturar


* **Itens pedidos a serem cobrados:** O relatório mostra os itens que foram pedidos pelos clientes, em relação aos quais as vendas
A fatura não foi criada/foi criada parcialmente.
* **Itens entregues a serem cobrados:** os itens que foram entregues aos clientes, mas a fatura de vendas não foi criada/foi parcialmente criada.
* **Itens do pedido de compra a serem faturados:** O relatório mostra os itens que foram pedidos aos fornecedores, mas a fatura de compra não foi criada/foi parcialmente criada.
* **Itens recebidos a serem faturados:** os itens que foram recebidos dos fornecedores, mas a fatura de compra não foi criada/foi parcialmente criada.


## 8. Outros relatórios


### 8.1 Balancete de teste da parte


Acesse: **Contas > Outros relatórios > Balancete da parte**.
Normalmente você pode precisar ver o balancete de seus clientes e fornecedores. Você pode obter facilmente para todos os seus clientes ou fornecedores e também para indivíduos.


![Balanço de teste para festa](/files/party-wise-trail-balance.png)


### 8.2 Saldo de crédito do cliente


O relatório mostra o limite de crédito, o saldo pendente e o saldo de crédito de cada cliente.


![Saldo de crédito do cliente](/files/customer-credit-balance.png)



