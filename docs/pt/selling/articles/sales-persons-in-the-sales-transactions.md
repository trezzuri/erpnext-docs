# Vendedores nas transações de vendas



No ERPNext, o mestre do Vendedor é mantido na [estrutura em árvore](/docs/pt/setting-up/articles/managing-tree-structure-masters.html). O Vendedor pode ser selecionado em todas as transações de vendas.


Os Vendedores também podem ser atualizados no cadastro de Clientes. Ao selecionar o Cliente nas transações, os Vendedores atualizados no Cliente serão inseridos na transação de vendas.


![Vendedor Cliente](/files/sales-person-in-customer.png)


#### Contribuição do vendedor


Se mais de um vendedor estiver trabalhando junto em um pedido, a contribuição (%) deverá ser definida para cada vendedor.


![Pedido do vendedor](/files/sales-person-in-sales-order.png)


Na transação de poupança, com base no Total Líquido e na Contribuição (%), a `Contribuição para o Total Líquido` será calculada para cada Vendedor.


A % de contribuição total para todos os vendedores deve ser de 100%. Se apenas um vendedor for selecionado, a % de contribuição será 100.
#### Relatório de transações do vendedor


Verifique o relatório de transações do vendedor em:


`Venda > Relatórios padrão > Resumo da transação do vendedor`


Este relatório pode ser gerado com base no Pedido de Venda, Nota de Entrega e Nota Fiscal de Venda. Ele lhe dará o valor total da venda feita por um funcionário.


![Relatório de vendedor](/files/sales-person-wise-transaction-summary-report.png)


#### Comissão do vendedor


ERPNext fornece apenas o valor total da venda feita por um vendedor. Se você oferece comissão ao Vendedor, você deve adicionar o Vendedor como Parceiro de Vendas no ERPNext. Para Parceiros de Vendas, você pode definir Comissão (%). Ao ser selecionado no Parceiro de Vendas em uma transação de vendas, com base no Total Líquido, o Valor da Comissão também é calculado. Você pode verificar o relatório de comissão do parceiro de vendas em:


`Contas > Relatórios padrão > Comissão de parceiros de vendas`




