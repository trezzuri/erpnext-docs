# Nota de crédito



**Uma Nota de Crédito é um documento enviado por um vendedor ao Cliente, notificando que um crédito foi feito em sua conta contra as mercadorias devolvidas pelo comprador.**


É emitida uma Nota de Crédito pelo valor da mercadoria devolvida pelo Cliente, podendo ser inferior ou igual ao valor total da encomenda.


## 1. Como fazer uma nota de crédito


O usuário pode fazer uma Nota de Crédito contra a Nota Fiscal de Venda ou pode fazer uma Nota de Crédito diretamente da Nota Fiscal de Venda sem referência. Observe que para criar uma nota de crédito, a fatura deve ser paga usando uma [Entrada de pagamento](/docs/pt/accounts/payment-entry).


1. Acesse a respectiva Fatura de Venda e clique em **Criar > Devolução/Nota de Crédito**.
![Nota de crédito da fatura](/files/credit-note-from-invoice.png)
2. Os detalhes do Cliente e do Item serão obtidos conforme definido na Fatura de Venda.
3. Se o Cliente tiver pago parcial ou totalmente, faça um lançamento de pagamento na fatura de venda original.
4. Salvar e enviar.


![Nota de crédito](/files/credit-note.png)


A quantidade do item e o valor do pagamento serão negativos, pois se trata de uma devolução.


### 1.1 Como a nota de crédito afeta o razão


Assim que um Lançamento de Pagamento for criado em relação à Fatura de Venda original, o valor será adicionado negativo à conta do Cliente para que na próxima vez que ele fizer uma compra, esse valor seja ajustado.


É assim que o razão é afetado após um lançamento de pagamento em uma fatura devolvida:
![Ledger de notas de crédito](/files/credit-note-ledger.png)


Consulte a página [Fatura de vendas](/docs/pt/accounts/sales-invoice) para obter outros detalhes.


### 1.2 Nenhum pagamento foi feito na fatura de vendas


Caso **nenhum pagamento** tenha sido feito na fatura original, você poderá simplesmente cancelar a fatura de vendas. Mas, se apenas 5 em cada 10 itens estiverem sendo devolvidos de uma fatura, a criação de uma nota de crédito será útil para atualizar o razão.


## 2. Exemplo


O cliente Rohan comprou tubos de PVC no valor de Rs 300 + impostos e, no momento da entrega, o cliente descobriu que os produtos estavam danificados. Agora que Rohan devolveu o produto, uma Nota de Crédito será emitida.


A nota de crédito com entrada de pagamento no ERPNext para o exemplo acima é como abaixo:


![Criando nota de crédito](/files/creating-credit-note.gif)


### 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
2. [Nota de débito](/docs/pt/accounts/debit-note)
3. [Retorno de vendas](/docs/pt/stock/sales-return)



