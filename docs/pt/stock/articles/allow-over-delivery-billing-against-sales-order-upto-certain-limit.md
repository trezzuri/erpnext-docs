# Permitir entrega/faturamento excessivos



Ao criar uma Nota de Entrega, o sistema valida se a quantidade do item é a mesma do Pedido de Venda. Se a quantidade do item tiver aumentado, você receberá a mensagem de validação de entrega excessiva ou recebimento.


Considerando o caso de vendas, se você deseja entregar mais itens do que o mencionado no Pedido de Venda, você deve atualizar "Permitir entrega excessiva ou recebimento até este percentual" no Cadastro de itens.


![Porcentagem de limite discriminado](/files/limit-1.png)


Ao criar uma fatura, a taxa do item também é validada com base na transação anterior, como Pedido de Venda. Isto também se aplica ao criar Recibo de Compra ou Fatura de Compra a partir do Pedido de Compra. A atualização de "Permitir entrega ou recebimento excessivo até esta porcentagem" será aplicada em todas as transações de vendas e compras.


Por exemplo, se você pediu 100 unidades de um item e se a porcentagem de recebimento excedente do item for 50, você poderá fazer um recibo de compra de até 150 unidades.


Atualize o valor global para "Permitir entrega excessiva ou recebimento até esta porcentagem" em Configurações de estoque. O valor atualizado aqui será aplicável a todos os itens.


1. Acesse `Estoque > Configuração > Configurações de estoque`
2. Definir `Porcentagem Limite`.
3. Salvar configurações de estoque.


![](/files/TGPrUJY.png)



