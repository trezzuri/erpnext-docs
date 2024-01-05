# Buscando dados de um documento



**Pergunta:** Rastreamos o número do pedido do cliente e o campo Data do pedido no pedido de vendas. Para que esses valores também sejam buscados na Nota Fiscal de Venda, inserimos Campo Personalizado na Nota Fiscal de Venda. No entanto, quando criamos a fatura de vendas a partir do pedido de vendas, os detalhes do pedido de compra do cliente não são obtidos.


**Resposta:** Quando os dados são buscados de uma transação para outra, o mapeamento dos dados é feito com base nos nomes dos campos. Se duas transações tiverem campos com exatamente o mesmo nome, seus valores serão mapeados.


Por exemplo, se você deseja que o número do pedido de compra e a data do pedido do cliente sejam buscados do pedido de vendas para a fatura de vendas, você deve garantir que os campos personalizados adicionados na fatura de vendas tenham exatamente o mesmo nome de campo do pedido de vendas. 


Ordem de venda (campos padrão)


![Campos padrão no pedido de vendas](/files/customize-fetch-data-1.png)


Fatura de vendas (campos personalizados)


![Campo personalizado na fatura de vendas](/files/customize-fetch-data-2.png)


Como os nomes dos campos relacionados ao pedido de venda do cliente são iguais no pedido de vendas e na fatura de vendas, ao criar a fatura de vendas a partir do pedido de vendas, os valores nesses campos são buscados automaticamente.


![Valores obtidos do pedido de vendas para a fatura de vendas](/files/customize-fetch-data-3.png)
![Valores obtidos do pedido de vendas para a fatura de vendas](/files/customize-fetching-data.gif)



