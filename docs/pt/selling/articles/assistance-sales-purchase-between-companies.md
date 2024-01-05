# Envio direto entre empresas subsidiárias



**Cenário:**


Nossa empresa tem duas empresas irmãs, onde a SAS atende clientes e pedidos de vendas e a BV administra estoque, compras, mas também alguns clientes locais.


Usando o ERPNext desejamos implementar o seguinte fluxo de trabalho.


1. Contatos do cliente SAS
2. SAS gera um pedido de venda
3. SAS transforma o SO em um pedido de compra para BV
4. BV recebe PO > SO do SAS
5. BV atende o pedido do estoque ao cliente final
6. Faturas BV SAS
7. SAS paga ao BV
8. SAS faturas e contas do cliente final


**Resposta:**


Você pode gerenciar este cenário usando o recurso Drop Shipping do ERPNext. Verifique o link a seguir para saber como funciona no ERPNext.


[https://erpnext.com/docs/user/manual/en/selling/artigos/drop-shipping](https://erpnext.com/docs/user/manual/en/selling/articles/drop-shipping) (com vídeo)


**Etapas:**


1. Para a Empresa SAS, crie um Pedido de Venda para o Cliente. Certifique-se de marcar "Drop Shipping" para o item.
2. Para a Empresa SAS, adicione BV como Fornecedor
3. Crie um pedido de compra (PO) em relação a um pedido de venda. Em PO, selecione BV como Fornecedor. Mas o endereço de entrega será o endereço do cliente.
4. O SAS criará uma fatura de compra, pois é responsável pelo pagamento ao BV.
5. Em relação ao pedido de vendas original, o SAS criará uma fatura de vendas para o cliente e criará uma entrada de pagamento posteriormente.
6. A empresa BV adicionará o SAS como seu cliente. Eles podem criar um Pedido de Venda para registrar receitas em suas contas. Faça nota de entrega para o cliente. Faça fatura de vendas para SAS.



