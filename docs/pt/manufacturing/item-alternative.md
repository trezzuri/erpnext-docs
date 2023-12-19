# Alternativa de item



**Um item alternativo é um item semelhante ao original e pode ser usado no lugar do item original na fabricação.**


Se a matéria-prima definida na lista técnica não estiver disponível durante o processo de produção, seu respectivo item alternativo disponível poderá ser usado para completar o processo de produção.


Primeiro você precisa ativar a opção "Permitir Item Alternativo" no Item.
![Item](/files/allow-alternative-item.png)


Para acessar a lista de alternativas de itens, acesse:
> Home > Estoque > Itens e preços > Alternativa de item


Isso também pode ser feito clicando no sinal de mais ao lado de 'Alternativa de item' no painel mestre de itens.
Você pode ativar a substituição bidirecional entre um item e seu item alternativo se ambos puderem ser usados ​​como alternativa um ao outro.


![Item Alternativo](/files/item-alternative.png)


## 1. Pré-requisitos


Antes de criar e usar uma Alternativa de Item, é aconselhável que você crie primeiro o seguinte:


* [Item](/docs/pt/stock/item)


## 2. Alternativa de item para ordem de serviço


Para permitir o uso de itens alternativos no processo de fabricação, o usuário pode configurar para 'Permitir item alternativo' na lista técnica/ordem de serviço


### 2.1 Provisão para permitir item alternativo na BOM


Você pode ativar 'Permitir item alternativo' em uma lista de materiais e selecionar o item alternativo na entrada de estoque. Isso também pode ser feito com uma Ordem de Serviço.
![Item](/files/allow-alternative-item-bom.png)


### 2.2 Provisão para permitir item alternativo na ordem de serviço


O usuário também pode ativar/desativar a permissão de itens alternativos para ordens de serviço individuais.
![Item](/files/allow-alternative-item-wo.png)


Marcar a caixa de seleção 'Permitir item alternativo' exibirá um botão chamado 'Item alternativo'. Você pode clicar aqui para definir a Alternativa de Item na Ordem de Serviço. É assim que você usa a Alternativa de Item em uma Ordem de Serviço:
![Item](/files/work_order_item_alternative.gif)


É assim que você usa a Alternativa de item com uma entrada de estoque:
![Item](/files/se_item_alternative.gif)


Se a caixa de seleção 'Permitir item alternativo' na tabela de itens estiver desativada, você não poderá definir um item alternativo para este item.


### 2.3 Alternativa de item para subcontrato


No subcontrato, o usuário deve transferir a matéria-prima para o fornecedor subcontratado para obter o produto acabado. Caso a matéria-prima não esteja disponível no estoque, com esta funcionalidade o usuário poderá transferir o item alternativo da matéria-prima subcontratada para o fornecedor. Isso é feito na Entrada de Estoque.


![Item](/files/purchase_order_item_alternative.gif)


Depois disso, ao criar um Recibo de Compra a partir da Ordem de Serviço, o item alternativo será mostrado.


### 3. Tópicos Relacionados


1. [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
2. [Ordem de serviço](/docs/pt/manufacturing/work-order)



