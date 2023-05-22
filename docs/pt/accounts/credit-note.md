# Nota de Crédito


**Uma Nota de Crédito é um documento enviado por um vendedor ao Cliente, notificando que um crédito foi feito em sua conta em relação às mercadorias devolvidas pelo comprador.**


É emitida uma Nota de Crédito pelo valor dos bens devolvidos pelo Cliente, podendo ser inferior ou igual ao valor total da encomenda.


## 1. Como fazer uma Nota de Crédito


O usuário pode fazer uma Nota de Crédito contra a Fatura de Venda ou pode fazer uma Nota de Crédito diretamente da Fatura de Venda sem referência. Observe que, para criar uma nota de crédito, a fatura deve ser paga usando uma [Entrada de pagamento](/docs/pt/accounts/payment-entry).


1. Acesse a respectiva Nota Fiscal de Venda e clique em **Criar > Devolução/Nota de Crédito**.
![Nota de crédito da fatura](/files/credit-note-from-invoice.png)
2. Os detalhes do cliente e do item serão obtidos conforme definido na fatura de venda.
3. Se o cliente pagou parcial ou totalmente, faça uma entrada de pagamento contra a fatura de venda original.
4. Salvar e enviar.


![Nota de crédito](/files/credit-note.png)


A quantidade do item e o valor do pagamento serão negativos, pois é uma devolução.


### 1.1 Como a Nota de Crédito afeta o razão


Depois que uma Entrada de Pagamento é criada contra a Fatura de Venda original, o valor será adicionado à conta do Cliente em negativo para que na próxima vez que ele fizer uma compra, esse valor seja ajustado.


É assim que o livro razão é afetado após uma entrada de pagamento em uma fatura devolvida:
![Redit Note Ledger](/files/credit-note-ledger.png)


Consulte a página [Fatura de vendas](/docs/pt/accounts/sales-invoice) para quaisquer outros detalhes.


### 1.2 Nenhum pagamento foi feito contra a fatura de vendas


Caso **nenhum pagamento** tenha sido feito contra a fatura original, você pode simplesmente cancelar a fatura de venda. Mas, se apenas 5 em 10 itens estão sendo devolvidos de uma fatura, a criação de uma nota de crédito é útil para atualizar o razão.


## 2. Exemplo


O cliente Rohan comprou tubos de PVC no valor de Rs 300 + impostos e, no momento da entrega, o cliente descobriu que os produtos estavam danificados. Agora que Rohan devolveu o produto, uma nota de crédito será emitida.


A Nota de Crédito com entrada de pagamento no SOMA para o exemplo acima é a seguinte:


![Criando nota de crédito](/files/creating-credit-note.gif)


### 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
2. [Nota de débito](/docs/pt/accounts/debit-note)
3. [Devolução de vendas](/docs/pt/stock/sales-return)
