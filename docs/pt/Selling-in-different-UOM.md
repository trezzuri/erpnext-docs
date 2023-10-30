# Vender em unidades de medida diferentes



Uma unidade de medida de preço de venda (UOM) é a UOM com a qual você define o preço dos itens. Você pode ter diversas UOMs de preço de venda para qualquer item de estoque. No entanto, quando o Cliente coloca, a UM de um item pode mudar.


Por exemplo, uma Caneta Item é estocada em Nos, mas vendida em Caixa. Daí faremos Pedido de Venda para Pen in Box.


**Etapa 1:**
No Cadastro de itens, na seção Unidade de medida, você pode listar todas as UM possíveis de um item, com seu Fator de conversão de UM. Atualizar fatores de conversão de UM
Em uma caixa, se você obtiver 10 números de caneta, o fator de conversão UM seria 10.


![Unidade de medida do item](/files/Item-UOM.png)


**Conjunto 2:** 
No Pedido de Venda, você encontrará dois campos UM


1. UM
2. Unidade de medida de estoque


Em ambos os campos, a UM padrão de um item será buscada por padrão. Você deve editar o campo UM e selecionar UM de Venda (Caixa neste caso). A atualização da unidade de medida de vendas serve principalmente para referência do Cliente. No formato de impressão, você verá a quantidade de itens na UM de vendas.


![Unidade de medida do pedido de venda](/files/Sale-Order-UOM.png)


Com base na Quantidade e no Fator de Conversão, a quantidade será calculada na UM de estoque de um item. Se você vender apenas uma caixa, a quantidade por UM de estoque será definida como 10.


**Lançamento no razão de estoque**


Independentemente da UM de vendas selecionada na Ordem de venda, o lançamento no razão de estoque será feito na UM padrão de um item. Portanto, você deve garantir que o fator de conversão seja inserido corretamente ao vender itens em unidades de medida diferentes.


![UOM no razão de estoque](/files/uom-in-stock-ledger.png)



