# Devolução de compra



**Um item comprado sendo devolvido é conhecido como devolução de compra.**


Com o recurso Devolução de compra, você pode devolver produtos ao
Fornecedor. Isto pode ser devido a uma série de razões, como defeitos nas mercadorias,
qualidade não correspondente, o comprador não precisa do estoque, etc.


## 1. Pré-requisitos


Antes de criar e usar uma Devolução de Compra, é aconselhável que você crie primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Fatura de compra](/docs/pt/accounts/purchase-invoice)


Ou


[Recibo de compra](/docs/pt/stock/purchase-receipt)


## 2. Como criar uma Devolução de Compra


1. Primeiro abra o recibo de compra original, contra o qual o fornecedor entregou os itens.


![Recibo de compra original](/files/purchase-return-original-purchase-receipt.png)
2. Clique em 'Criar > Devolução', um novo recibo de compra será aberto com a opção 'É devolução' marcada. Itens, taxas e impostos terão números negativos.


![Devolução contra recibo de compra](/files/purchase-return-against-purchase-receipt.png)
3. Ao enviar a Devolução de Compra, o sistema diminuirá a quantidade de itens do Armazém mencionado. Para manter a avaliação correta do estoque, o saldo do estoque também aumentará de acordo com a taxa de compra original dos itens devolvidos.


![Return Stock Ledger](/files/purchase-return-stock-ledger.png)
4. No Razão Contábil, a conta Estoque em Mão será creditada e a conta Estoque Recebido mas Não Faturado será debitada.


![Return Stock Ledger](/files/purchase-return-general-ledger.png)


Se o Estoque Perpétuo estiver ativado, o sistema também lançará lançamentos contábeis na conta do armazém para sincronizar o saldo da conta do armazém com o saldo do estoque de acordo com o Razão de Estoque.


## 3. Impacto no retorno de estoque via recibo de compra


Sobre a criação de uma devolução de compra com base em um recibo de compra:


* A **Quantidade devolvida** no recibo de compra original, juntamente com qualquer pedido de compra vinculado a ele, é atualizado.
* O status do recibo de compra original será alterado para **Devolução emitida** se 100% for devolvido:
![Retorno emitido](/files/purchase-return-issue.png)


### 4. Tópicos Relacionados


1. [Retorno de vendas](/docs/pt/stock/sales-return)
2. [Inventário permanente](/docs/pt/stock/perpetual-inventory)



