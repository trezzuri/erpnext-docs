# Erro de estoque negativo na nota de entrega



**Pergunta**: Ao enviar uma Nota de Entrega, recebo uma mensagem informando que o estoque do item é insuficiente, mas temos estoque do item disponível no Armazém.


**Resposta**: No envio da Nota de Remessa, o nível de estoque é verificado na Data e Hora de Lançamento de uma Nota de Remessa. É possível que você tenha estoque de um Item disponível no Armazém. Mas se você estiver criando uma nota de entrega com data anterior e o item não estiver disponível no depósito na data de lançamento e na hora de lançamento da nota de entrega, é provável que você receba uma mensagem de erro sobre o estoque negativo. Você pode consultar o relatório Stock Ledger para confirmar o mesmo.


Se for esse o caso, você deve editar a data e hora de lançamento de uma nota de entrega e garantir que seja posterior à data e hora de lançamento da entrada do recebimento do item.



