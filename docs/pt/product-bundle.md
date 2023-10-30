# Pacote de produtos



**Um pacote de produtos é um mestre onde você pode listar itens existentes que são agrupados e vendidos como um conjunto (ou pacote).**


Por exemplo, quando você vende um smartphone, você precisa garantir que o carregador, o cabo e o pino ejetor do SIM sejam entregues com ele e que os níveis de estoque desses itens sejam afetados.
Para resolver esse cenário, você pode criar um pacote de produtos para o item principal, ou seja, smartphone. Em seguida, liste os itens a serem entregues, ou seja, smartphone + carregador + cabo + pino ejetor do SIM como os chamados "Itens infantis".


Um pacote de produtos pode ser visto como uma "lista de materiais" no lado das vendas.


A seguir estão as etapas para configurar um pacote de produtos e usá-lo em transações de vendas.


Para acessar o pacote de produtos, acesse:
> Home > Venda > Itens e preços > Pacote de produtos


## 1. Pré-requisitos


Antes de criar e usar um pacote de produtos, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)


## 2. Como criar um pacote de produtos


1. Vá para a lista de pacotes de produtos e clique em Novo.
2. Selecione Item Pai, crie um se ainda não tiver sido criado. Certifique-se de que Manter estoque esteja desmarcado ao criar um item pai. por exemplo: conjunto de jantar.
3. Insira um preço para o item pai. Ele será obtido ao fazer uma transação.
4. Você pode inserir uma descrição para uso interno.
5. Insira os produtos a serem agrupados na tabela Itens e insira suas quantidades.
6. Salvar.
![Pacote de produtos](/files/product-bundle.png)


### 2.1 Selecionando item pai


No mestre do pacote de produtos, há duas seções. O "Item Pai" e uma Lista de itens a serem enviados (Itens Filhos).


O "Item Pai" deve ser visto mais como um recipiente ou item virtual e não como um produto físico.
O "Item pai" deve ser um **item sem estoque**. Para criar um **item sem estoque** você deve desmarcar "Manter Estoque" no Formulário de Item.
Este é um item sem estoque porque não há estoque mantido para ele, mas apenas para os "Itens Filhos".
Se quiser manter o estoque para o item pai, você deverá criar uma lista de materiais (BOM) regular
e empacotá-los usando transações de entrada de estoque.


### 2.2 Selecionando itens filhos


Na tabela Itens, você listará todos os itens filhos para os quais mantemos estoque e são entregues ao cliente.
Lembre-se: o "Item Pai" é apenas virtual, então seu produto principal (um smartphone no nosso exemplo aqui) também deve estar listado na Lista de Itens Filhos (ou Pacote).


## 3. Recursos


### 3.1 Pacote de produtos nas transações de vendas


Ao realizar transações de Vendas (Fatura de Venda, Pedido de Venda, Nota de Entrega) o Item Pai será selecionado na tabela de itens principal.


![Pacote de produtos](/files/product-bundle.gif)


Ao selecionar um Item Pai na tabela de itens principal, seus itens filhos serão buscados na tabela Packing List da transação. Se o item filho for o item serializado, você poderá especificar seu número de série.
na própria tabela Packing List. Ao enviar a transação, o sistema reduzirá o nível de estoque de itens secundários do armazém especificado na tabela Packing List.


**Use o pacote de produtos para gerenciar ofertas/esquemas:**
  

Isso foi descoberto quando um cliente que negociava produtos nutricionais solicitou um recurso para gerenciar ofertas como “Compre um e leve outro”. Para gerenciar o mesmo, ele criou um item não estocável que foi usado como item pai. Na descrição do item, ele inseriu os detalhes da oferta com a imagem do item exibindo a oferta. O produto vendável foi selecionado no Item do Pacote onde a quantidade era dois. Portanto, cada vez que eles vendiam uma quantidade de item pai sob esta oferta, o sistema deduzia duas quantidades de produto do Armazém.
### 4. Tópicos Relacionados


1. [Item](/docs/pt/stock/item)



