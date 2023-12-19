# **Fatura de venda sem item**



Uma Fatura de Venda é uma fatura que você envia aos seus Clientes contra a qual o Cliente efetua o pagamento.

Há casos em que o usuário precisa criar faturas de vendas sem um código de item (diversos cobranças, itens únicos). Existe uma maneira de lidar com esses casos no ERPNext.

## **1. Pré-requisitos**

Antes de criar e usar uma fatura de vendas, é aconselhável criar primeiro os seguintes:

* [Item](https://docs.erpnext.com/docs/pt/stock/item)
* [Cliente](https://docs.erpnext.com/docs/pt/CRM/customer)
* Opcional:


	+ [Pedido de venda](https://docs.erpnext.com/docs/pt/venda/pedido de venda)
	+ [Nota de entrega](https://docs.erpnext.com/docs/pt/stock/delivery-note)

## **2. Como criar uma fatura de vendas sem código de item**

1. Vá para a lista de faturas de vendas e clique em Novo.
2. Selecione o Cliente.
3. Defina a Data de Vencimento do Pagamento.
4. Na tabela Itens, clique em editar no campo primeira linha e insira:


	1. Nome do item
	2. Descrição
	3. Quantidade
	4. UOM
	5. Taxa
	6. Conta de receita

![ezgif.com-crop (7)](/files/ezgif.com-crop (7).gif "ezgif.com-crop (7).gif")![]()

5. Salvar e enviar.

Da mesma forma , você pode criar uma nota de crédito sem item usando este método. Uma etapa adicional seria ativar “É devolução” e inserir a quantidade negativa.

Todos os outros recursos relacionados às faturas de vendas permanecem os mesmos-<https://docs.erpnext.com/docs/user/manual/en/sales-invoice>

  




