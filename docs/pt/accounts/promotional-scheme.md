# Esquema promocional



>
> Introduzido na versão 12
>
>
>


**Um Esquema Promocional é um desconto temporário em um ou mais produtos.**


Os esquemas promocionais ajudam as empresas a obter sucesso, pois preços mais baixos por um período limitado de tempo para atrair mais clientes. Eles podem ser facilmente configurados no ERPNext. Um esquema Promocional está vinculado a uma regra de precificação, contra cada sistema de laje que gerará a regra de precificação.


Ao criar um esquema promocional, o sistema cria uma [regra de preços](/docs/v13/user/manual/en/accounts/pricing-rule). Um Esquema Promocional pode ter várias Regras de Preços associadas a ele. No ERPNext, um esquema promocional é uma maneira mais fácil de gerenciar preços em vários itens/grupos com base em diferentes partes e condições.


Para acessar a lista de Programas Promocionais, acesse:



>
> Home > Venda > Itens e preços > Esquema promocional
>
>
>


## 1. Pré-requisitos


Antes de criar e usar um Esquema Promocional, é aconselhável criar primeiro o seguinte:


1. [Item](/docs/v13/user/manual/en/stock/item)
2. [Grupo de itens](/docs/v13/user/manual/en/stock/item-group)
3. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
4. [Fornecedor](/docs/v13/user/manual/en/buying/supplier)


## 2. Como criar um esquema promocional


1. Vá para a lista de Esquema promocional e clique em Novo.
2. Insira um título para a regra.
3. Selecione o que aplicar, como código do item, grupo de itens, marca ou transação. Selecionar Transação aplicará o esquema no valor total da transação.
4. Com base em 'Aplicar em', o sistema fornecerá a você a opção de selecionar o Código do item / Grupo do item / Marca na tabela.
5. Selecione se o esquema é para Venda, Compra ou ambos e defina as informações da parte.
6. Na tabela Tabelas de desconto de preço, defina o desconto de preço, desconto de produto.
7. Os usuários também podem aplicar o desconto em outro Código de item/Grupo de item/Marca selecionando o valor do campo Aplicar regra em outro.


![Esquema promocional](/files/promotional-schemes.png)
8. Salve.



>
> Nota: Ao guardar um Esquema Promocional, é criada uma nova Regra de Preços.
>
>
>


### 2.1 Campos adicionais ao criar um Esquema Promocional


#### Condições Mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. O Esquema Promocional será aplicado apenas se a soma total dos Artigos corresponder às quantidades definidas. Por exemplo, você cria um esquema promocional no item 1 e no item 2 e define a quantidade mínima e máxima como 30, o esquema promocional será aplicado somente se a quantidade total for 30.


#### é cumulativo


A habilitação desta opção permite que o Esquema Promocional seja aplicado cumulativamente. Você precisa definir 'Min Amt' e 'Max Amt' para isso.


Considere um cenário em que Min Amt é 1.500 e Max Amt é 2.000. Agora, se uma transação for criada para 1.400, o Esquema Promocional não será aplicado. No entanto, ao criar uma segunda fatura no valor de 600, o Esquema promocional será aplicado. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas na última transação que ultrapasse o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Características


### 3.1 Aplicar esquema em outro item


Este recurso verifica a condição do primeiro item, mas aplica esquema/desconto/taxa em outro item.


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' no Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Precificação será aplicada no Item3, pois os dois primeiros itens estavam presentes na transação.


### 3.2 Informações da Parte


Defina se o Esquema Promocional é para Venda ou Compra do Item.


Com base na sua seleção, você pode definir a aplicabilidade para um dos seguintes mestres.


* [Cliente](/docs/v13/user/manual/en/CRM/cliente)
* [Grupo de clientes](/docs/v13/user/manual/en/CRM/customer-group)
* [Território](/docs/v13/user/manual/en/selling/território)
* [Parceiro de vendas](/docs/v13/user/manual/en/selling/sales-partner)
* [Campanha](/docs/v13/user/manual/en/CRM/campanha)
* [Fornecedor](/docs/v13/user/manual/en/buying/supplier)
*Grupo Fornecedor


### 3.3 Validade


Você também pode definir um intervalo de datas para quando o Esquema Promocional será válido. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco o Esquema Promocional não terá limite de prazo.


**Moeda**: Definir uma Moeda aqui fará com que o Esquema Promocional seja aplicado somente quando a Moeda for a mesma da transação.


### 3.4 Placas de desconto de preço


**Descrição da Regra**: Insira uma descrição para não saber o que este Esquema Promocional implica.


#### Quantidade e valor


Especifique a quantidade mínima, quantidade máxima, quantidade mínima ou quantidade máxima de um Item quando este Esquema Promocional for aplicável.


Observe que se a quantidade ou valor ficar aquém ou exceder os limites aqui estabelecidos, o Esquema Promocional não será aplicado. No entanto, será aplicado se você tiver habilitado as opções Condições Mistas ou Cumulativas.


### Configurando o Desconto/Taxa


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vender um Item por 100 e quiser vendê-lo por 112 para uma festa específica, selecione Taxa e defina a Taxa como 112.
* **Porcentagem de desconto**: Uma porcentagem de desconto específica pode ser definida. Por exemplo, um desconto de 10% em um item no valor de 500 resultaria em um preço de 450.
* **Valor do desconto**: Será aplicado um valor de desconto fixo. Por exemplo, se você vender um Item por 100 e quiser vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do Desconto.


#### Filtros para configuração de desconto


* **Armazém**: Definir um Armazém aqui fará com que o Esquema Promocional seja aplicado somente se o Item for selecionado no Armazém especificado aqui.
* **Prioridade**: Considere um Grupo de Itens, você deseja definir regras específicas para um Item do grupo. Isso pode ser feito criando um novo esquema promocional e definindo uma prioridade mais alta.
* **Limite para Sugestão**: Este é o limite com base no qual o sistema irá notificá-lo para ajustar a Quantidade de Item para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicado. Isso também se aplica ao valor definido.
* **Validar Regra Aplicada**: Se o preço inserido não for válido para o Item, o sistema não permitirá que você aplique uma taxa/desconto diferente.


### 3.5 Placas de desconto de produtos


Um Desconto de Produto é aplicável quando um ou mais Itens são gratuitos na compra de outros Itens. A maioria dos campos nesta tabela é a mesma da seção anterior.


As opções adicionais são:
\* **Mesmo Item**: Se você quiser dar o mesmo Item como grátis (desconto de produto) na compra de um Item, ative esta caixa de seleção. Se você quiser dar outro Item, desmarque e selecione o Item a ser dado gratuitamente.


* **Aplique várias regras de precificação**: Para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Habilitar esta opção aplicará um total de 15% na Taxa do Item, que dá 425.
* **UM**: O Esquema Promocional será aplicado somente se a UM definida aqui corresponder à transação.
* **Taxa**: Um Item pode ser oferecido gratuitamente pelo Fornecedor, mas pode haver algum imposto aplicável. Inserir uma Tarifa aqui significa que o Cliente terá que pagar os impostos aplicáveis.


## 4. Tipos de esquemas promocionais


### 4.1 Desconto no Preço


Nesse tipo de esquema promocional, o usuário tem a opção de definir o desconto em termos de porcentagem ou valor com base na quantidade mínima, quantidade máxima, valor mínimo e valor máximo dos produtos. Os usuários também podem configurar o esquema onde podem definir a taxa fixa para o produto com base na quantidade ou quantidade do produto.


![Desconto de preço do esquema promocional](/files/promotional-schemes-price-discount.png)


### 4.2 Desconto de Produto


Nesse tipo de esquema promocional, o usuário tem a opção de dar um produto grátis na compra do mesmo ou de outro produto com condições como quantidade mínima, quantidade máxima, quantidade mínima, quantidade máxima.


![Desconto de produto do esquema promocional](/files/promotional-schemes-product-discount.png)


## 5. Como configurar um Esquema Promocional (Exemplos)


Vamos entender como configurar um esquema promocional no ERPNext através de alguns exemplos.


### 5.1 Esquemas de Condições Mistas


O cliente A comprou 10 quantidades do pacote Britannia Cake 5 Rs e 5 quantidades do pacote Britannia Cake 10 Rs. Agora, o Fornecedor quer dar um desconto de 10% ao Cliente A. Este Fornecedor também quer dar um desconto de 10% ao Cliente B que comprou 15 quantidades de pacote de Bolo Britannia 5 Rs.


Assim, o Fornecedor deseja aplicar o desconto nos produtos Bolo Britannia 5 Rs, Bolo Britannia 10 Rs somente se seus Clientes tiverem adquirido 15 quantidades de qualquer produto ou a soma dos dois produtos.


Para configurar isso no ERPNext os passos são os seguintes:


1. Defina Aplicar em como Código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do item da regra de preços.
3. Ative o campo "Condições mistas".
4. Na tabela de desconto de preço, defina a quantidade mínima e a quantidade máxima como 15.
5. Defina o tipo de desconto como Porcentagem de desconto e a taxa como 10.


![Condição Mista do Esquema Promocional](/files/promotional-schemes-mixed-conditions.png)


### 5.2 Aplicar desconto em outro Item


O cliente A comprou 30 quantidades de pacote Britannia Cake 5 Rs e 2 quantidades de Britannia Cake 15 Rs. O Fornecedor deseja vender o produto Bolo Britannia 15 Rs pela taxa fixa de 12. Aqui, o preço original do produto Bolo Britannia 15 Rs é 15.


O Fornecedor deseja aplicar a regra apenas se o Cliente tiver adquirido no mínimo 30 quantidades do produto Bolo Britannia 5 Rs ou Bolo Britannia 10 Rs.


Para configurar isso no ERPNext os passos são os seguintes


1. Defina Aplicar em como Código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do item da regra de preços.
3. Aplique Rule On Other como Item Code e defina Item Code como Britannia Cake 15 Rs.
4. Na tabela de desconto de preço, defina a quantidade mínima como 30.
5. Defina o tipo de desconto como Taxa e taxa como 12.


![Esquema promocional de desconto em outro item](/files/promotional-schemes-discount-on-other.png)


## 6. Tópicos Relacionados


1. [Regra de preços](/docs/v13/user/manual/en/accounts/pricing-rule)
2. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
3. [Fornecedor](/docs/v13/user/manual/en/buying/supplier)
4. [Item](/docs/v13/user/manual/en/stock/item)