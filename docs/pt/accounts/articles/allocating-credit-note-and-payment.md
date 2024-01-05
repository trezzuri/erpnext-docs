# Alocação de nota de crédito e pagamento



**Pergunta:** Temos clientes que devolvem itens após o pagamento da fatura. Então, como sempre, criamos uma nota de crédito. Mas às vezes não há outras faturas em aberto às quais possamos alocar a nota de crédito. Portanto, neste caso, precisaremos reembolsar os clientes. Como posso registrar esse tipo de transação que não temos crédito negativo nas faturas de lista?

  


**Resposta** 

  


Você deve ser capaz de gerenciar esse cenário específico seguindo as etapas compartilhadas abaixo.

  


1. Primeiro, crie uma nota de crédito em relação a uma fatura
2. Em seguida, crie uma entrada de pagamento para o valor devolvido
3. Use a reconciliação de pagamento para falsificar o pagamento na fatura de venda original (e não na própria nota de crédito).

  


  


**Nota:** No caso de um ciclo de compra, onde você cria uma nota de débito no sistema para um cenário semelhante, as etapas seriam as seguintes:

  


1. Primeiro, crie uma nota de débito no sistema em relação à fatura de compra
2. Em seguida, crie uma entrada de Pagamento para o valor devolvido
3. Use a reconciliação de pagamento para falsificar o pagamento contra a fatura de compra original (e não a própria nota de débito).


