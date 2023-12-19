# Compras em unidades de medida diferentes



Cada item possui uma unidade de medida de estoque (UM) associada a ele. Por exemplo, a UM da caneta pode ser números (Nos) e a areia pode ser armazenada em kg. No entanto, quando fazemos um pedido ao Fornecedor, a UM de um item pode mudar. Assim como podemos encomendar 1 conjunto/caixa de caneta ou um caminhão de areia ao nosso fornecedor. Ao criar uma transação de compra, você pode alterar a UM de compra de um item.


### Cenário:


O item `Caneta` é estocado em Nos, mas comprado em Box. Daí faremos Pedido de Compra de Caneta in Box.


#### Etapa 1: editar a unidade de medida no pedido de compra


No Pedido de Compra, você encontrará duas UMs fiadas.


* UM
* Unidade de medida de estoque


Em ambos os campos, a UM padrão de um item será buscada por padrão. Você deve editar o campo UM e selecionar UM de Compra (Caixa neste caso). A atualização da unidade de medida de compra serve principalmente para referência do fornecedor. No formato de impressão, você verá a quantidade do item na UM de compra.


![Unidade de medida de compra de item](/files/editing-uom-in-po.gif)


#### Etapa 2: atualizar os fatores de conversão da unidade de medida


Em uma caixa, se você obtiver 20 números de caneta, o fator de conversão UM seria 20.


![Fator de conversão de item](/files/po-conversion-factor.png)


Com base na Quantidade e no Fator de Conversão, a quantidade será calculada na UM de estoque de um item. Se você comprar apenas uma caixa, a quantidade na UM do estoque será definida como 20.


![Quantidade de compra na unidade de medida padrão](/files/po-qty-in-stock-uom.png)


### Lançamento no razão de ações


Independentemente da UM de compra selecionada, o lançamento no razão de estoque será feito na UM padrão de um item. Portanto, você deve garantir que o fator de conversão seja inserido corretamente ao comprar itens em unidades de medida diferentes.


![Formato de impressão na unidade de medida de compra](/files/po-stock-uom-ledger.png)


### Definir fator de conversão no item


No cadastro de itens, na seção Compra, você pode listar todas as UM de compra possíveis de um item, com seu Fator de Conversão de UM.


![Mestre da unidade de medida de compra](/files/item-purchase-uom-conversion.png)




