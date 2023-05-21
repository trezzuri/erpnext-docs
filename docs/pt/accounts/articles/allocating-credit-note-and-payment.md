# Atribuição de Nota de Crédito e Pagamento


**Pergunta:** Temos clientes que devolvem itens após o pagamento da fatura. Então, como de costume, criamos uma nota de crédito. Mas por vezes não existem outras faturas em aberto às quais possamos atribuir a nota de crédito. Portanto, neste caso, precisaremos pagar os clientes de volta. Como posso registar este tipo de transacções que não temos crédito negativo nas facturas de lista?

  


**Responder**

  


Você deve ser capaz de gerenciar esse cenário específico seguindo as etapas compartilhadas abaixo.

  


1. Primeiro, crie uma Nota de Crédito contra uma Fatura
2. Em seguida, crie uma Entrada de Pagamento para o valor devolvido
3. Use a reconciliação de pagamento para compensar o pagamento contra a fatura de venda original (e não a própria nota de crédito).

  


  


**Observação:** No caso de um ciclo de Compra, onde você cria uma nota de débito no sistema para um cenário semelhante, as etapas seriam as seguintes:

  


1. Primeiro, crie uma Nota de Débito no sistema contra a Nota Fiscal de Compra
2. Em seguida, crie uma entrada de pagamento para o valor devolvido
3. Use a reconciliação de pagamento para compensar o pagamento contra a fatura de compra original (e não a própria nota de débito).