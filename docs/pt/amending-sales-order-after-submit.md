# Alteração do pedido de venda após envio



A taxa e a quantidade no pedido de vendas agora podem ser alteradas após o envio usando o botão `Atualizar itens`.


![Atualizar itens](/files/so-update-items.png)


Para atualizar a taxa e a quantidade em um pedido de venda enviado, clique no botão `Atualizar itens`. Uma caixa de diálogo aparecerá para permitir que você faça a alteração.


![Atualizar itens](/files/so-update-items-rate-and-qty.gif)


Observe as seguintes validações e casos de uso:


* Os recursos de atualização verificam se o pedido de venda possui nota de entrega e fatura de venda.
* A quantidade pode ser atualizada para pedidos de venda não entregues e para notas de entrega parcial. Para pedidos de vendas com notas de entrega preenchidas, eles não podem ser atualizados.
* A taxa pode ser atualizada para pedidos de vendas não faturados e parcialmente faturados. Para pedidos de vendas com fatura de vendas enviada, eles não podem ser atualizados.



