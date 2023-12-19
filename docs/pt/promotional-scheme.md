# Esquema Promocional




> 
> Introduzido na versão 12
> 
> 
> 


**Um esquema promocional é um desconto temporário em um ou mais produtos.**


Os esquemas promocionais ajudam as empresas a terem sucesso, pois reduzem os preços durante um período limitado de tempo para atrair mais clientes. Eles podem ser facilmente configurados no ERPNext. Um esquema promocional está vinculado a uma regra de precificação, em relação a cada sistema de placas que irá gerar a regra de precificação.


Ao criar um esquema promocional, o sistema cria uma [Regra de preços](/docs/pt/accounts/pricing-rule). Um Esquema Promocional pode ter diversas Regras de Preços associadas a ele. No ERPNext, um esquema promocional é uma maneira mais fácil de gerenciar preços em vários itens/grupos com base em diferentes partes e condições.


Para acessar a lista do Esquema Promocional, acesse:



> 
> Página inicial > Vendas > Itens e preços > Esquema promocional
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


1. Vá para a lista Esquema Promocional e clique em Novo.
2. Insira um título para a regra.
3. Selecione o que aplicar, como código do item, grupo de itens, marca ou transação. Selecionar Transação aplicará o esquema ao valor total da transação.
4. Com base em 'Inscrever-se', o sistema lhe dará a possibilidade de selecionar o Código do Item/Grupo de Item/Marca na tabela.
5. Selecione se o esquema é para venda, compra ou ambos e defina as informações da parte.
6. Na tabela Placas de Desconto de Preço, defina o desconto de preço, desconto de produto.
7. Os usuários também podem aplicar o desconto em outro código de item/grupo de item/marca selecionando o valor do campo Aplicar regra em outro.


![Esquema promocional](/files/promotional-schemes.png)
8. Salvar.



> 
> Observação: ao salvar um Esquema Promocional, uma nova Regra de Preços é criada.
> 
> 
> 


### 2.1 Campos adicionais ao criar um esquema promocional


#### Condições Mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. O Regime Promocional só será aplicado se a soma total dos Itens corresponder às quantidades definidas. Por exemplo, você cria um Esquema Promocional no Item 1 e no Item 2 e define a Quantidade Mínima e Máxima como 30. O Esquema Promocional será aplicado somente se a quantidade total for 30.


#### É cumulativo


Ativar esta opção permite que o Esquema Promocional seja aplicado cumulativamente. Você precisa definir o 'Valor mínimo' e o 'Valor máximo' para isso.


Considere um cenário em que o valor mínimo é 1.500 e o valor máximo é 2.000. Agora, se for criada uma transação de 1.400, o Esquema Promocional não será aplicado. Porém, na criação de uma segunda fatura no valor 600, será aplicado o Regime Promocional. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas à última transação que ultrapassar o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Recursos


### 3.1 Aplicar esquema em outro item


Este recurso verifica a condição do primeiro item, mas aplica esquema/desconto/taxa em outro item.


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' no Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Preços será aplicada ao Item3, já que os dois primeiros Itens estavam presentes na transação.


### 3.2 Informações da parte


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


Você também pode definir um intervalo de datas para a validade do esquema promocional. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco o Programa Promocional não terá limite de prazo.


**Moeda**: Definir uma Moeda aqui fará com que o Esquema Promocional seja aplicado somente quando a Moeda for a mesma na transação.


### 3.4 Placas de desconto de preço


**Descrição da regra**: insira uma descrição para não informar o que este esquema promocional envolve.


#### Quantidade e quantidade


Especifique a quantidade mínima, a quantidade máxima, a quantidade mínima ou a quantidade máxima de um item quando este esquema promocional for aplicável.


Observe que se a quantidade ou valor ficar abaixo ou exceder os limites aqui definidos, o Esquema Promocional não será aplicado. Porém, será aplicado se você tiver habilitado as opções Condições Mistas ou Cumulativas.


### Definindo o desconto/taxa


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vende um item por 100 e deseja vendê-lo por 112 para um grupo específico, selecione Taxa e defina a Taxa como 112.
* **Porcentagem de desconto**: Uma porcentagem de desconto específica pode ser definida. Por exemplo, um desconto de 10% num item no valor de 500 resultaria num preço de 450.
* **Valor do desconto**: Um valor de desconto fixo será aplicado. Por exemplo, se você vende um item por 100 e deseja vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do desconto.


#### Filtros para configuração de desconto


* **Armazém**: Definir um Armazém aqui fará com que o Esquema Promocional seja aplicado somente se o Item for selecionado no Armazém especificado aqui.
* **Prioridade**: considere um grupo de itens, você deseja definir regras específicas para um item do grupo. Isso pode ser feito criando um novo esquema promocional e definindo uma prioridade mais alta.
* **Limite para sugestão**: este é o limite com base no qual o sistema irá notificá-lo para ajustar a quantidade de itens para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicável. Isto também se aplica ao valor definido.
* **Validar regra aplicada**: se o preço inserido não for válido para o item, o sistema não permitirá que você aplique uma taxa/desconto diferente.


### 3.5 Placas de desconto em produtos


Um Desconto de Produto é aplicável quando um ou mais Itens são gratuitos na compra de outros Itens. A maioria dos campos nesta tabela são iguais aos da seção anterior.


As opções adicionais são:
\* **Mesmo Item**: Se você quiser dar o mesmo Item como grátis (desconto no produto) na compra de um Item, marque esta caixa de seleção. Se você quiser oferecer outro item, desmarque e selecione o item a ser oferecido gratuitamente.


* **Aplicar múltiplas regras de precificação**: para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Ativar esta opção aplicará um total de 15% na taxa do item, o que dá 425.
* **UM**: O esquema promocional será aplicado somente se a UM definida aqui corresponder à transação.
* **Taxa**: Um Item pode ser oferecido gratuitamente pelo Fornecedor, mas pode haver algum imposto aplicável. Inserir uma Taxa aqui significa que o Cliente terá que pagar os impostos aplicáveis.


## 4. Tipos de esquema promocional


### 4.1 Desconto no preço


Neste tipo de esquema promocional, o usuário tem a opção de definir o desconto em percentual ou valor com base na quantidade mínima, quantidade máxima, quantidade mínima e valor máximo dos produtos. Os usuários também podem configurar o esquema onde podem definir a taxa fixa para o produto com base na quantidade ou quantidade do produto.


![Desconto no preço do esquema promocional](/files/promotional-schemes-price-discount.png)


### 4.2 Desconto em produtos


Neste tipo de esquema promocional, o usuário tem a opção de oferecer um produto grátis na compra do mesmo produto ou de um produto diferente, com condições como quantidade mínima, quantidade máxima, quantidade mínima, quantidade máxima.


![Desconto em produto do esquema promocional](/files/promotional-schemes-product-discount.png)


## 5. Como configurar um esquema promocional (exemplos)


Vamos entender como configurar um esquema promocional no ERPNext usando alguns exemplos.

### 5.1 Esquemas de condições mistas


O cliente A comprou 10 quantidades de pacotes de Bolo Britannia 5 Rs e 5 quantidades de pacotes de Bolo Britannia 10 Rs. Agora, o Fornecedor quer dar um desconto de 10% ao Cliente A. Este Fornecedor também quer dar um desconto de 10% ao Cliente B que comprou 15 quantidades de pacote de Bolo Britannia 5 Rs.


Assim, o Fornecedor deseja aplicar o desconto nos produtos Bolo Britannia 5 Rs, Bolo Britannia 10 Rs somente se seus Clientes tiverem adquirido 15 quantidades de qualquer produto ou soma de ambos os produtos.


Para configurar isso no ERPNext os passos são os seguintes:


1. Defina Aplicar como código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do item da regra de preços.
3. Ative o campo "Condições mistas".
4. Na tabela de desconto de preço, defina a quantidade mínima e a quantidade máxima como 15.
5. Defina o tipo de desconto como Porcentagem de desconto e a taxa como 10.


![Esquema Promocional Condição Mista](/files/promotional-schemes-mixed-conditions.png)


### 5.2 Para aplicar um desconto em outro item


O cliente A comprou 30 quantidades de pacote de Bolo Britannia 5 Rs e 2 quantidades de Bolo Britannia 15 Rs. O Fornecedor deseja vender o produto Bolo Britannia 15 Rs pelo preço fixo de 12. Aqui o preço original do produto Bolo Britannia 15 Rs é 15.


O Fornecedor deseja aplicar a regra somente se o Cliente tiver adquirido no mínimo 30 quantidades do produto Bolo Britannia 5 Rs ou Bolo Britannia 10 Rs.


Para configurar isso no ERPNext os passos são os seguintes


1. Defina Aplicar como código do item.
2. Defina o código do item Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Código do Item da Regra de Preços.
3. Aplique a regra sobre outros como código do item e defina o código do item como Britannia Cake 15 Rs.
4. Na tabela de desconto de preço, defina a quantidade mínima como 30.
5. Defina o tipo de desconto como Taxa e a taxa como 12.


![Esquema promocional de desconto em outro item](/files/promotional-schemes-discount-on-other.png)


## 6. Tópicos Relacionados


1. [Regra de preços](/docs/pt/accounts/pricing-rule)
2. [Cliente](/docs/pt/CRM/customer)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Item](/docs/pt/stock/item)



