# Esquema promocional



> 
> Introduzido na versão 12
> 
> 
> 


**Um esquema promocional é um desconto temporário em um ou mais produtos.**


Esquemas promocionais ajudam as empresas a obter sucesso como preços mais baixos por um período limitado de tempo para atrair mais clientes. Eles podem ser facilmente configurados no SOMA. Um esquema promocional está vinculado a uma regra de precificação, contra cada sistema de laje que gerará a regra de precificação.


Ao criar um esquema promocional, o sistema cria uma [regra de preços](/docs/pt/accounts/pricing-rule). Um Esquema Promocional pode ter várias Regras de Preços associadas a ele. No SOMA, um esquema promocional é uma maneira mais fácil de gerenciar preços em vários itens/grupos com base em diferentes partes e condições.


Para acessar a lista de esquemas promocionais, acesse:



> 
> Página inicial > Venda > Itens e preços > Esquema promocional
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar um Esquema Promocional, é aconselhável criar primeiro o seguinte:


1. [Item](/docs/pt/stock/item)
2. [Grupo de itens](/docs/pt/stock/item-group)
3. [Cliente](/docs/pt/CRM/customer)
4. [Fornecedor](/docs/pt/buying/supplier)


## 2. Como criar um esquema promocional


1. Vá para a lista de esquemas promocionais e clique em Novo.
2. Digite um título para a regra.
3. Selecione o que aplicar, como código do item, grupo de itens, marca ou transação. Selecionar Transação aplicará o esquema no valor total da transação.
4. Com base em 'Aplicar em', o sistema permitirá que você selecione o Código do item/Grupo de itens/Marca na tabela.
5. Selecione se o esquema é para Venda, Compra ou ambos e defina as informações da parte.
6. Na tabela Tabelas de desconto de preço, defina o desconto de preço, desconto de produto.
7. Os usuários também podem aplicar o desconto em outro Código de item/Grupo de item/Marca selecionando o valor do campo Aplicar regra em outro.


![Esquema promocional](/files/promotional-schemes.png)
8. Salvar.



> 
> Observação: Ao salvar um esquema promocional, uma nova regra de preços é criada.
> 
> 
> 


### 2.1 Campos adicionais ao criar um esquema promocional


#### Condições mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. O Esquema Promocional será aplicado apenas se a soma total dos Artigos corresponder às quantidades definidas. Por exemplo, você cria um esquema promocional no item 1 e no item 2 e define a quantidade mínima e máxima como 30, o esquema promocional será aplicado somente se a quantidade total for 30.


#### É cumulativo


Habilitar esta opção permite que o Esquema Promocional seja aplicado cumulativamente. Você precisa definir 'Min Amt' e 'Max Amt' para isso.


Considere um cenário em que Min Amt é 1.500 e Max Amt é 2.000. Agora, se uma transação for criada para 1.400, o Esquema Promocional não será aplicado. No entanto, ao criar uma segunda fatura no valor de 600, o Esquema promocional será aplicado. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas na última transação que ultrapasse o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Recursos


### 3.1 Aplicar esquema em outro item


Este recurso verifica a condição do primeiro item, mas aplica esquema/desconto/taxa em outro item.


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' em Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Precificação será aplicada no Item3, pois os dois primeiros itens estavam presentes na transação.


### 3.2 Informações da Parte


Defina se o esquema promocional é para venda ou compra do item.


Com base na sua seleção, você pode definir a aplicabilidade para um dos seguintes mestres.


* [Cliente](/docs/pt/CRM/customer)
* [Grupo de clientes](/docs/pt/CRM/customer-group)
* [Território](/docs/pt/selling/territory)
* [Parceiro de vendas](/docs/pt/selling/sales-partner)
* [Campanha](/docs/pt/CRM/campaign)
* [Fornecedor](/docs/pt/buying/supplier)
* Grupo de fornecedores


### 3.3 Validade


Você também pode definir um intervalo de datas para a validade do Esquema Promocional. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco, o Esquema Promocional não terá limite de tempo.


**Moeda**: definir uma moeda aqui fará com que o esquema promocional seja aplicado somente quando a moeda for a mesma na transação.


### 3.4 Tabelas de desconto de preço


**Descrição da regra**: insira uma descrição para não saber o que este esquema promocional implica.


#### Quantidade e valor


Especifique a quantidade mínima, quantidade máxima, quantidade mínima ou quantidade máxima de um Item quando este Esquema Promocional for aplicável.


Observe que, se a quantidade ou valor ficar aquém ou exceder os limites definidos aqui, o Esquema Promocional não será aplicado. No entanto, será aplicado se você tiver ativado as opções Condições Mistas ou Cumulativas.


### Definição do desconto/taxa


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vender um item por 100 e quiser vendê-lo por 112 para uma festa específica, selecione Taxa e defina a taxa como 112.
* **Porcentagem de desconto**: uma porcentagem de desconto específica pode ser definida. Por exemplo, um desconto de 10% em um item no valor de 500 resultaria em um preço de 450.
* **Valor do desconto**: será aplicado um valor de desconto fixo. Por exemplo, se você vender um item por 100 e quiser vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do desconto.


#### Filtros para definir desconto


* **Armazém**: Definir um Armazém aqui fará com que o Esquema Promocional seja aplicado somente se o Item for selecionado no Armazém especificado aqui.
* **Prioridade**: considere um grupo de itens, você deseja definir regras específicas para um item do grupo. Isso pode ser feito criando um novo esquema promocional e definindo uma prioridade mais alta.
* **Limite para Sugestão**: Este é o limite com base no qual o sistema irá notificá-lo para ajustar a Quantidade de Item para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicado. Isso também se aplica ao valor definido.
* **Validar regra aplicada**: Se o preço inserido não for válido para o Item, o sistema não permitirá que você aplique uma tarifa/desconto diferente.


### 3.5 Placas de desconto de produtos


Um desconto de produto é aplicável quando um ou mais itens são gratuitos na compra de outros itens. A maioria dos campos nesta tabela são os mesmos da seção anterior.


As opções adicionais são:
\* **Mesmo Item**: Se você quiser dar o mesmo Item como grátis (desconto de produto) na compra de um Item, ative esta caixa de seleção. Se você quiser dar outro item, desmarque e selecione o item a ser dado gratuitamente.


* **Aplicar várias regras de precificação**: para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Ativar esta opção aplicará um total de 15% na taxa do item, que dá 425.
* **UM**: O Esquema Promocional será aplicado somente se o UM definido aqui corresponder à transação.
* **Taxa**: Um Item pode ser oferecido gratuitamente pelo Fornecedor, mas pode haver algum imposto aplicável. Inserir uma Tarifa aqui significa que o Cliente terá que pagar os impostos aplicáveis.


## 4. Tipos de esquema promocional


### 4.1 Desconto no preço


Neste tipo de esquema promocional, o usuário tem a opção de definir o desconto em termos de porcentagem ou valor com base na quantidade mínima, quantidade máxima, quantidade mínima e quantidade máxima dos produtos. Os usuários também podem configurar o esquema onde podem definir a taxa fixa para o produto com base na quantidade ou valor do produto.


![Desconto de preço do esquema promocional](/files/promotional-schemes-price-discount.png)


### 4.2 Desconto de produto


Neste tipo de esquema promocional, o usuário tem a opção de dar um produto grátis na compra do mesmo ou de outro produto com condições como quantidade mínima, quantidade máxima, quantidade mínima, quantidade máxima.


![Promotional Scheme Product Discount](/files/promotional-schemes-product-discount.png)


## 5. Como configurar um esquema promocional (exemplos)


Vamos entender como configurar um esquema promocional no SOMA através de alguns exemplos.


### 5.1 Esquemas de condições mistas


O cliente A comprou 10 quantidades do pacote Britannia Cake 5 Rs e 5 quantidades do pacote Britannia Cake 10 Rs. Agora, o Fornecedor quer dar um desconto de 10% ao Cliente A. Este Fornecedor também quer dar um desconto de 10% ao Cliente B que comprou 15 quantidades de pacote de Bolo Britannia 5 Rs.


Assim, o Fornecedor deseja aplicar o desconto nos produtos Bolo Britannia 5 Rs, Bolo Britannia 10 Rs somente se seus Clientes tiverem comprado 15 quantidades de qualquer produto ou a soma dos dois produtos.


Para configurar isso no SOMA os passos são os seguintes:


1. Defina Apply On como código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do item da regra de preços.
3. Ative o campo "Condições mistas".
4. Na tabela de desconto de preço, defina a quantidade mínima e a quantidade máxima como 15.
5. Defina o tipo de desconto como Porcentagem de desconto e a taxa como 10.


![Condição mista do esquema promocional](/files/promotional-schemes-mixed-conditions.png)


### 5.2 Para aplicar um desconto em outro item


O cliente A comprou 30 quantidades de pacote Britannia Cake 5 Rs e 2 quantidades de Britannia Cake 15 Rs. O fornecedor deseja vender o produto Britannia Cake 15 Rs à taxa fixa de 12. Aqui, o preço original do produto Britannia Cake 15 Rs é 15.


O Fornecedor deseja aplicar a regra somente se o Cliente tiver comprado no mínimo 30 quantidades do produto Bolo Britannia 5 Rs ou Bolo Britannia 10 Rs.


Para configurar isso no SOMA, as etapas são as seguintes


1. Defina Apply On como código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do item da regra de preços.
3. Aplique a regra em outro como código do item e defina o código do item como Britannia Cake 15 Rs.
4. Na tabela de desconto de preço, defina a quantidade mínima como 30.
5. Defina o tipo de desconto como Taxa e a taxa como 12.


![Desconto de esquema promocional em outro item](/files/promotional-schemes-discount-on-other.png)


## 6. Tópicos Relacionados


1. [Regra de preços](/docs/pt/accounts/pricing-rule)
2. [Cliente](/docs/pt/CRM/customer)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Item](/docs/pt/stock/item)
