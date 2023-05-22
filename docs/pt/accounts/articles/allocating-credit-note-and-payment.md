# Atribuição de Nota de Crédito e Pagamento


**Pergunta:** Temos clientes que devolvem itens após o pagamento da fatura. Então, como de costume, criamos uma nota de crédito. Mas por vezes não existem outras faturas em aberto às quais possamos atribuir a nota de crédito. Portanto, neste caso, precisaremos pagar os clientes de volta. Como posso registrar este tipo de transações que não temos crédito negativo nas faturas de lista?

  


**Resposta** 

  


Você deve conseguir gerenciar esse cenário específico seguindo as etapas compartilhadas abaixo.

  


< ol>- Primeiro, crie uma nota de crédito contra uma fatura
- Em seguida, crie uma entrada de pagamento para o valor devolvido
- Use a reconciliação de pagamento para imitar o pagamento contra a fatura de venda original (e não a própria nota de crédito).
  


  


**Observação:** No caso de um ciclo de Compra, onde você cria uma nota de débito no sistema para um cenário semelhante, as etapas seriam as seguintes:

  


1. Primeiro, crie uma Nota de Débito no sistema contra a Fatura de Compra
2. Em seguida, crie uma entrada de pagamento para o valor devolvido
3. Use a reconciliação de pagamento para imitar o pagamento contra a Nota Fiscal de Compra original (e não a própria Nota de Débito).
