# Marca



**Uma marca identifica itens com um nome específico.**


Normalmente, uma Marca é o fabricante ou embalador de um produto específico. Por exemplo, Apple é uma marca que fabrica laptops. Uma Marca não é necessariamente o [Fabricante](/docs/pt/stock/manufacturer) de um Item, é apenas o nome sob o qual um produto é vendido. Por exemplo, se você fabrica copos plásticos, você pode licenciá-los para uma grande marca para que eles os vendam sob sua marca.


No ERPNext, Marcas podem ser atribuídas a Itens para identificar e atribuir certos padrões.


Para acessar a lista de Marcas, acesse:



> 
> Home > Vendas > Vendas > Marca
> 
> 
> 


## 1. Como criar uma marca


1. Vá para a lista Marca e clique em Novo.
2. Insira um nome de marca e uma descrição, se necessário.
3. Salvar.


![Brand](/files/brand.png)


Agora esta Marca pode ser associada a diferentes Itens.


![Marca no item](/files/brand-in-item.png)


## 2. Recursos


### 2.1 Definindo padrões para itens desta marca


![Padrões de marca](/files/brand-defaults.png)


Os seguintes padrões podem ser definidos para uma marca. Ao atribuir esta marca a um Item, os padrões definidos serão buscados ao realizar transações de Venda/Compra com Item desta Marca.


* **Armazém Padrão**: O Armazém do qual o Item será obtido/armazenado dependendo da transação.
* **Lista de Preços Padrão**: A Lista de Preços definida aqui será buscada nas transações de Compra/Venda.


#### Padrões de compra


Ao realizar transações de Compra como Ordem de Compra, Recibo de Compra ou Nota Fiscal de Compra, os padrões definidos aqui serão obtidos ao selecionar o Item desta Marca.


* Centro de custo de compra padrão
* Fornecedor padrão
* Conta de despesas padrão


#### Padrões de vendas


Ao realizar transações de Vendas como Pedido de Venda, Nota de Entrega ou Fatura de Venda, os padrões definidos aqui serão obtidos ao selecionar o Item desta Marca.


* Centro de custo de venda padrão
* Conta de renda padrão


## 3. Tópicos Relacionados


1. [Pedido de compra](/docs/pt/buying/purchase-order)
2. [Ordem de vendas](/docs/pt/selling/sales-order)
3. [Recibo de compra](/docs/pt/stock/purchase-receipt)
4. [Nota de entrega](/docs/pt/stock/delivery-note)
5. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
6. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



