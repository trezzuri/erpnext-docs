# Nota de crédito


**Uma Nota de Crédito é um documento enviado por um vendedor ao Cliente, notificando que um crédito foi feito em sua conta contra as mercadorias devolvidas pelo comprador.**


É emitida uma Nota de Crédito pelo valor dos bens devolvidos pelo Cliente, podendo ser inferior ou igual ao valor total da encomenda.


## 1. Como fazer uma Nota de Crédito


O utilizador pode fazer uma Nota de Crédito contra a Fatura de Venda ou pode fazer uma Nota de Crédito diretamente da Fatura de Venda sem referência. Observe que para criar uma Nota de Crédito, a fatura deve ser paga usando uma [Entrada de Pagamento](/docs/v13/user/manual/en/accounts/payment-entry).


1. Aceda à respetiva Fatura de Venda e clique em **Criar > Devolução/Nota de Crédito**.
![Nota de crédito da fatura](/files/nota de crédito da fatura.png)
2. Os detalhes do cliente e do item serão obtidos conforme definido na fatura de venda.
3. Se o Cliente pagou parcial ou totalmente, faça uma Entrada de Pagamento contra a Nota Fiscal de Venda original.
4. Salve e envie.


![Nota de crédito](/files/credit-note.png)


A quantidade do item e o valor do pagamento serão negativos, pois é uma devolução.


### 1.1 Como a Nota de Crédito afeta o razão


Uma vez que uma Entrada de Pagamento é criada contra a Nota Fiscal de Venda original, o valor será adicionado à conta do Cliente em negativo para que na próxima vez que ele fizer uma compra, esse valor seja ajustado.


É assim que o livro razão é afetado após uma entrada de pagamento em uma fatura devolvida:
![Registro de notas de crédito](/files/credit-note-ledger.png)


Consulte a página [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas) para obter outros detalhes.


### 1.2 Nenhum pagamento foi feito contra a Nota Fiscal de Venda


Caso **nenhum pagamento** tenha sido feito contra a fatura original, basta cancelar a Nota Fiscal de Venda. Mas, se apenas 5 em 10 Itens forem devolvidos de uma fatura, a criação de uma Nota de Crédito é útil para atualizar o livro razão.


## 2. Exemplo


O cliente Rohan comprou tubos de PVC no valor de Rs 300 + impostos e, no momento da entrega, o cliente descobriu que os produtos estavam danificados. Agora que Rohan devolveu o produto, uma nota de crédito será emitida.


A Nota de Crédito com entrada de pagamento no ERPNext para o exemplo acima é a seguinte:


![Criando nota de crédito](/files/creating-credit-note.gif)


### 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
2. [Nota de Débito](/docs/v13/user/manual/en/accounts/debit-note)
3. [Devolução de vendas](/docs/v13/user/manual/en/stock/vendas-retorno)