# Pesquisa global


**A pesquisa global é uma poderosa operação de processamento de texto no ERPNext que o ajudará na pesquisa de um determinado tipo de documento ou documento.**


Para cada sequência de uma determinada palavra ou conjunto de caracteres, você terá um resultado de pesquisa.


### Usando a Awesome Bar para pesquisa global.


![Tree Master Renameing](/files/using-global-search-2.gif)


A Pesquisa Global ajuda os usuários a encontrar informações rapidamente. Ele está localizado no canto superior direito do ERPNext. Basta inserir alguns caracteres na barra de pesquisa para mostrar os resultados de vários tipos de registros diferentes (contato, cliente, problemas, etc.) relacionados a essa palavra-chave. Você também pode personalizar os campos com base nos quais a pesquisa será exibida.


Você também pode digitar várias palavras-chave separadas pelo operador & para encontrar os resultados desejados. Você pode consultar os seguintes casos para exemplos:


* A entrada "apple & iPod" pode retornar documentos com um campo contendo Apple e o outro contendo iPod (fornecedor e item do PO).
* A entrada "iPhone & iPod" pode retornar documentos de destino que contenham itens iPhone e iPod (itens da tabela filho).
* A entrada "iPhone e preto" pode retornar o item com a descrição que contém iPhone e preto (campo de texto longo).
* A entrada 'foo & bar" pode retornar qualquer documento com as tags foo e bar atribuídas. (campo especial de texto longo \_usertags).


### Ativar pesquisa global para campos em um tipo de documento.


![Tree Master Renameing](/files/using-global-search-1.gif)

