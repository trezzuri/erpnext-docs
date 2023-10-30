# Listas de preços



**Uma lista de preços é uma coleção de preços de itens de venda, compra ou ambos.**


ERPNext permite manter vários [preços de itens de venda e compra](/docs/pt/stock/item-price) usando listas de preços.


As listas de preços podem ser usadas em cenários onde você tem preços diferentes para zonas diferentes (com base nos custos de envio), para moedas diferentes, etc. Um item pode ter vários preços com base no cliente, moeda, região, custo de envio, etc. , que pode ser armazenado como diferentes planos de tarifas.


No ERPNext, todos os preços dos itens são armazenados separadamente. O preço de compra de um item é diferente do preço de venda e, portanto, eles são armazenados separadamente.


Para acessar uma Lista de Preços acesse:


> Home > Venda/Compra/Estoque > Itens e preços > Lista de preços


![Lista de preços](/files/price-list.png)


## 1. Como usar uma lista de preços


* As listas de preços serão usadas ao criar [Preços de itens](/docs/pt/stock/item-price) para rastrear o preço de venda ou compra de um item.
* Países específicos podem ser atribuídos na Lista de Preços.
* Para desabilitar uma lista de preços específica, desmarque a caixa de seleção 'Ativado'. A Lista de Preços Desativada não estará disponível para seleção nas transações de Vendas e Compras.
* **O preço não depende da UOM**: Considere um item, Tomates, que você compra em caixas e vende em quilos. 1 caixa = 10 quilos e o preço de compra de 1 quilo é 10rs. Se esta caixa estiver desmarcada e você selecionar 1 caixa em sua transação, o preço aparecerá apenas para um quilo, pois esse é o único preço do item salvo.


Agora, se você marcar esta caixa de seleção e fizer uma transação com uma Caixa de Tomates, o preço será automaticamente definido como 100, já que o preço de 1 Caixa (10 Quilos) é 100.
* As listas de preços padrão de compra e venda são criadas por padrão.


**Observação**: se você tiver diversas Listas de Preços, poderá selecionar uma Lista de Preços ou marcá-la para um Cliente (para que seja selecionada automaticamente). Os preços dos seus itens serão atualizados automaticamente na lista de preços.


### Tópicos Relacionados


1. [Preço do item](/docs/pt/stock/item-price)



