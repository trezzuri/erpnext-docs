# Nomeação do número de série



Números de série são valores exclusivos atribuídos a cada unidade de um item. Número de série. ajuda a rastrear detalhes de garantia e vencimento do item. Geralmente itens de alto valor como máquinas, computadores e equipamentos caros são serializados.


Para tornar o item serializado, no item mestre, marque **Tem número de série**.


Existem duas maneiras de o número de série. pode ser gerado no ERPNext.


### 1. Serializando itens de compra


Se os itens comprados forem recebidos com números de série aplicados pelo OEM (fabricante do equipamento original), você também poderá seguir o mesmo número de série no ERPNext. Ao criar o recibo de compra, você deve digitalizar ou inserir manualmente os números de série. para um item. Ao enviar o recibo de compra, os números de série serão criados no backend de acordo com os números de série fornecidos para um item. Se estiver usando o número de série do OEM, no item mestre, o prefixo não deve ser mencionado para serialização. De acordo com este cenário, o campo Prefixo deve ser deixado em branco.


Se os itens recebidos já tiverem seu número de série com código de barras, você pode simplesmente digitalizar esse código de barras para inserir o número de série no recibo de compra. Clique [aqui](https://frappe.io/blog/management/using-barcodes-to-ease-data-entry) para saber mais sobre isso.


Ao enviar o recibo de compra ou entrada de estoque do item serializado, os números de série serão gerados automaticamente.


![Entrada de números de série](/files/serial-naming-1.png)


Os números de série gerados serão atualizados para cada item.


![Números de série criados](/files/serial-naming-2.png)


### 2. Serializando Item de Fabricação


Para serializar item de fabricação, você pode definir a série para geração do número de série no próprio cadastro de itens. Seguindo essa série, o sistema criará números de série para o item quando sua entrada de produção for feita.


#### 2.1 Nº de série Série


Quando o item é definido como serializado, você pode mencionar a série para ele.


![Números de série criados](/files/serial-naming-3.png)


#### 2.2 Entrada de produção para item serializado


Ao enviar a entrada de produção para o item de fabricação, o sistema gerará automaticamente os números de série seguindo as séries conforme especificado no cadastro de itens.


![Números de série criados](/files/serial-naming-4.png)




