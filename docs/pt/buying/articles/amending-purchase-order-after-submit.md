# Alteração do pedido de compra após envio



A taxa e a quantidade no pedido de compra agora podem ser alteradas após o envio usando o botão `Atualizar itens`.


![Atualizar itens](/files/po-update-items.png)


Para atualizar a taxa e a quantidade em um pedido de compra enviado, clique no botão `Atualizar itens`. Uma caixa de diálogo aparecerá para permitir que você faça a alteração.


![Atualizar itens](/files/po-update-items-rate-and-qty.gif)


Observe as seguintes validações e casos de uso:


* Os recursos de atualização verificam se o pedido de compra possui recibo de compra e fatura de compra.
* A quantidade pode ser atualizada para pedidos de compra não recebidos e parcialmente recebidos. Para Pedido de Compra com Recibo de Compra preenchido, ele não pode ser atualizado.
* A taxa pode ser atualizada para pedidos de compra não faturados e parcialmente faturados. Para Pedido de Compra com Fatura de Compra enviada, ela não pode ser atualizada.



