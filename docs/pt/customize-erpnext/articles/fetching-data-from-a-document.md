# Obtendo dados de um documento


**Pergunta:** Rastreamos o número do pedido do cliente e o campo Data do pedido no pedido de vendas. Para que esses valores também sejam buscados na Nota Fiscal, inserimos o Campo Personalizado na Nota Fiscal. No entanto, quando criamos a fatura de venda a partir do pedido de venda, os detalhes do pedido de compra do cliente não são buscados.


**Resposta:** Quando os dados são buscados de uma transação para outra, o mapeamento dos dados é feito com base nos nomes dos campos. Se duas transações tiverem campos com exatamente o mesmo nome, seus valores serão mapeados.


Por exemplo, se você deseja que o número do pedido do cliente e a data do pedido sejam obtidos do pedido de venda para a fatura de venda, certifique-se de que os campos personalizados adicionados à fatura de venda tenham exatamente o mesmo nome de campo do pedido de venda.


Pedido de venda (campos padrão)


![Campos padrão no pedido de venda](/files/customize-fetch-data-1.png)


Fatura de vendas (campos personalizados)


![Campo personalizado na fatura de vendas](/files/customize-fetch-data-2.png)


Como os nomes dos campos relacionados ao pedido de compra do cliente são os mesmos no pedido de venda e na fatura de venda, ao criar a fatura de venda a partir do pedido de venda, os valores nesses campos são buscados automaticamente.


![Valores obtidos do pedido de venda para a fatura de venda](/files/customize-fetch-data-3.png)


![Busca de valores do pedido de venda para a fatura de venda](/files/customize-fetching-data.gif)