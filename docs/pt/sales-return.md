# Devolução de vendas



**Um item vendido sendo devolvido é conhecido como Devolução de Venda.**


As empresas geralmente devolvem produtos que já foram vendidos. Podem ser devolvidos pelo cliente por problemas de qualidade, não entrega na data acordada ou qualquer outro motivo.


## 1. Pré-requisitos


Antes de criar e usar uma Declaração de Venda, é aconselhável que você crie primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Fatura de vendas](/docs/pt/accounts/sales-invoice) ou [Nota de entrega](/docs/pt/stock/delivery-note)


## 2. Como criar uma Declaração de Venda


1. Primeiro abra a Nota de Entrega/Fatura de Venda original, contra a qual o Cliente devolveu os Itens.


![Nota de entrega original](/files/sales-return-original-delivery-note.png)
2. Em seguida, clique em 'Criar > Devolução de Venda', será aberta uma nova Nota de Entrega com 'É Devolução' marcada, Itens, Taxa e impostos terão números negativos.


![Devolução contra nota de entrega](/files/sales-return-against-delivery-note.png)
3. Você também pode criar o lançamento de devolução em relação à fatura de venda original. Para devolver o estoque junto com a nota de crédito, marque a opção "Atualizar estoque" na fatura de devolução de venda.


![Devolução contra fatura de vendas](/files/sales-return-against-sales-invoice.png)
4. Ao enviar a Nota de Devolução/Fatura de Venda, o sistema aumentará o saldo de estoque no referido Armazém. Para manter a avaliação correta do estoque, o saldo do estoque aumentará de acordo com a taxa de compra original dos itens devolvidos.


![Return Stock Ledger](/files/sales-return-stock-ledger.png)
5. No caso de devolução da fatura de venda, a conta do cliente será creditada e a conta de renda e imposto associada será debitada conforme mostrado no livro contábil.


![Return Stock Ledger](/files/sales-return-general-ledger.png)


Se o Estoque Perpétuo estiver ativado, o sistema também lançará lançamentos contábeis na conta do armazém para sincronizar o saldo da conta do armazém com o saldo do estoque conforme o razão de estoque.


## 3. Impacto na devolução de estoque via guia de remessa


Sobre a criação de uma devolução de venda em relação a uma nota de entrega:


* A **Quantidade devolvida** na Nota de entrega original, juntamente com qualquer pedido de vendas vinculado a ela, é atualizada.
* O status da nota de entrega original é alterado para **Devolução emitida** se 100% for devolvido:
![Devolução emitida](/files/sales-return-issue.png)


## 4. Tópicos Relacionados


1. [Devolução de compra](/docs/pt/stock/purchase-return)
2. [Inventário permanente](/docs/pt/stock/perpetual-inventory)



