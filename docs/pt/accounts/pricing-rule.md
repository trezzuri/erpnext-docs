# Regra de preços


**Uma regra de preços define as regras de desconto/preço que se aplicam com base em condições definidas.**


Uma regra de preços tem muitas opções com as quais você pode controlar o preço de um item. Filtros como quantidade, data, grupos e outras condições podem ser definidos.


Uma regra de preços é um pouco semelhante a uma [regra fiscal](/docs/pt/accounts/tax-rule).


A seguir estão alguns casos que podem ser resolvidos usando a regra de precificação:


* De acordo com a política de venda promocional, se o Cliente comprar mais de 10 unidades de um artigo, usufrui de 20% de desconto.
* Para o Cliente "XYZ", o preço de venda do Item específico deve ser atualizado como ###.
* Os itens categorizados em um grupo de itens específico têm o mesmo preço de venda ou compra.
* Os clientes pertencentes a um grupo de clientes específico devem obter ### preço de venda ou % de desconto nos itens.
* O fornecedor categorizado em um grupo de fornecedores específico deve ter ### taxa de compra aplicada.


Para que a taxa de desconto e tabela de preços de um item seja aplicada automaticamente, crie regras de preços para ele.


Para acessar a lista de regras de preços, acesse:



> 
> Página inicial > Contabilidade > Regra de preços
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma regra de precificação, é recomendável criar primeiro o seguinte:


1. [Item](/docs/pt/stock/item)
2. [Grupo de itens](/docs/pt/stock/item-group)
3. [Cliente](/docs/pt/CRM/customer)
4. [Fornecedor](/docs/pt/buying/supplier)


## 2. Como criar uma regra de preços


1. Vá para a lista de regras de preços e clique em Novo.
2. Defina um título para a regra.
3. Selecione o que aplicar no código do item, grupo de itens, marca ou transação.
4. Selecione se deseja aplicar desconto de preço ou desconto de produto. Se você deseja oferecer produtos gratuitos, selecione o desconto do produto.
![Pricing Rule](/files/pricing-rule.png)
5. Para um único item, selecione Código do item e selecione os itens.
6. Se você deseja que a regra de preços seja aplicada a todos os itens, selecione 'Grupo de itens' e selecione **Todos os grupos de itens** (grupo de itens pai).
7. Defina o desconto/preço a ser aplicado. Para saber mais, [vá para esta seção](/docs/pt/accounts/pricing-rule#35-price-discount-scheme).
8. Salvar.


### 2.1 Opções adicionais ao criar uma regra de precificação


#### Armazém


Definir um Armazém aqui fará com que a Regra de Preços seja aplicada somente se o Item for selecionado no Armazém especificado aqui.


#### Aplicar regra em


Com base no atributo selecionado no campo 'Aplicar em', você pode definir a regra de preços com base em um destes:


* [Item](/docs/pt/stock/item)
* [Grupo de itens](/docs/pt/stock/item-group)
* Marca
* Transação (no valor total da transação)


Nesta tabela, você pode selecionar o Item/Grupo de Item/Marca específico. Por exemplo, se você selecionar Aplicar em 'Grupo de itens' e selecionar 'Matérias-primas' na tabela, esta regra de preços será aplicada apenas aos itens que pertencem ao grupo 'Matérias-primas'.


**UM**: a regra de precificação será aplicada somente se a UM definida aqui corresponder à transação.


#### Condição


Neste campo, você pode adicionar uma condição em python para verificar os valores do campo no doctype da transação, conforme mostrado abaixo para Nota Fiscal de Vendas:



```
cliente=='Nome do cliente' e status!='Atrasado'

```

Observe que apenas condições python de linha única funcionarão, usando nomes de campo do tipo de documento de destino.


#### Condições mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. A Regra de Precificação será aplicada somente se a soma total dos Itens corresponder às quantidades definidas. Por exemplo, você cria uma regra de preços no item 1 e no item 2 e define a quantidade mínima e máxima como 30, a regra de preços será aplicada somente se a quantidade total for 30.


#### É cumulativo


Habilitar esta opção permite que a Regra de Precificação seja aplicada cumulativamente. Você precisa definir 'Min Amt' e 'Max Amt' para isso.


Considere um cenário em que Min Amt é 1.500 e Max Amt é 2.000. Agora, se uma transação for criada para 1.400, a regra de preços não será aplicada. No entanto, ao criar uma segunda fatura de valor 600, a regra de preços será aplicada. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas na última transação que ultrapasse o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Recursos


### 3.1 Aplicar regra em outro


Este recurso verifica a condição do primeiro item, mas aplica a regra em outro item.


![Aplicar regra de precificação em outro item](/files/pricing-rule-on-other-item.png)


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' em Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Precificação será aplicada no Item3, pois os dois primeiros itens estavam presentes na transação.


### 3.2 Informações da Parte


Defina se a regra de precificação é para venda ou compra do item.


Com base na sua seleção, você pode definir a aplicabilidade para um dos seguintes mestres.


* [Cliente](/docs/pt/CRM/customer)
* [Grupo de clientes](/docs/pt/CRM/customer-group)
* [Território](/docs/pt/selling/territory)
* [Parceiro de vendas](/docs/pt/selling/sales-partner)
* [Campanha](/docs/pt/CRM/campaign)
* [Fornecedor](/docs/pt/buying/supplier)
* Grupo de fornecedores


### 3.3 Quantidade e valor


Especifique a quantidade mínima, quantidade máxima, quantidade mínima ou quantidade máxima de um item quando esta regra de preços deve ser aplicada.


Observe que, se a quantidade ou valor ficar aquém ou exceder os limites definidos aqui, a regra de preços não será aplicada. No entanto, será aplicado se você tiver ativado as opções Condições Mistas ou Cumulativas.


![Quantidade e valor da regra de preços](/files/pricing-rule-quantity-and-amount.png)


### 3.4 Validade


Você também pode definir um intervalo de datas para quando a regra de preços será válida. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco, a Regra de Precificação não terá limite de tempo.


![Configurações do período da regra de preços](/files/pricing-rule-period-settings.png)


### 3,5 Margem


![Pricing Rule Margin](/files/pricing-rule-margin.png)


* **Tipo de Margem**: Ao vender um Item, você pode vendê-lo por uma certa margem. Se você não quiser adicionar preços de venda aos itens todas as vezes e quiser definir uma margem automaticamente, isso pode ser feito com este recurso.
* **Taxa ou valor de margem**: a margem definida pode ser baseada em porcentagem ou valor, por exemplo: margem de 5% ou margem fixa de US$ 50.


Leia [adicionando margem](/docs/pt/selling/articles/adding-margin) para mais detalhes.


### 3.6 Esquema de descontos de preços


A regra real a ser aplicada é definida nesta seção.


![Desconto da regra de preços](/files/pricing-rule-discount-scheme.png)


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vender um item por 100 e quiser vendê-lo por 112 para uma festa específica, selecione Taxa e defina a taxa como 112.
* **Porcentagem de desconto**: uma porcentagem de desconto específica pode ser definida. A porcentagem de desconto pode ser definida para uma [Lista de preços](/docs/pt/stock/price-lists) específica. Deixar 'Para lista de preços' em branco aplicará a regra de preços a todas as listas de preços.
* **Valor do desconto**: será aplicado um valor de desconto fixo. Por exemplo, se você vender um item por 100 e quiser vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do desconto.


### 3.7 Configurações avançadas


![Configurações avançadas da regra de preços](/files/pricing-rule-advanced-settings.png)


* **Limite para Sugestão**: Este é o limite com base no qual o sistema irá notificá-lo para ajustar a Quantidade de Item para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicado. Isso também se aplica ao valor definido.
* **Prioridade**: considere um grupo de itens, você deseja definir regras específicas para um item do grupo. Isso pode ser feito criando uma nova regra de precificação e definindo uma prioridade mais alta. Isso também pode se aplicar ao Grupo de clientes e ao Grupo de fornecedores.
* **Aplicar várias regras de precificação**: para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Ativar esta opção aplicará um total de 15% na taxa do item, que dá 425.
* **Aplicar desconto na tarifa**: o desconto será composto. Considere o mesmo cenário acima. Ao habilitar esta opção, 10% serão aplicados em 500, o que dará 450, então 5% serão aplicados em 450, o que dará 427,5.
* **Validar regra aplicada**: mostra a mensagem de validação inserida se o desconto/taxa definido manualmente por você em uma transação não corresponder à regra de preços.


Isto é útil quando o distribuidor de topo na hierarquia decide o desconto/tarifa a aplicar e só está a validar se a Regra de Preços for aplicada corretamente.


## 4. Tipos de desconto de regra de preços


### 4.1 Desconto no preço


1. Em Tipo de margem, você pode definir se a margem é calculada como uma porcentagem ou um valor. Ex.: margem de 10% sobre a tabela de preços do fornecedor na hora da venda.
2. A taxa mencionada na regra de preços terá prioridade sobre a taxa da lista de preços do item (preço do item).


![Price Discount Scheme Rate](/files/price-discount-scheme-rate.png)
3. A porcentagem de desconto pode ser aplicada para uma lista de preços específica (venda ou compra). Para aplicá-lo para ambos, deixe o campo 'Para lista de preços' em branco.


![Price Discount Scheme Discount](/files/price-discount-scheme-discount.png)
4. O desconto também pode ser definido em termos de valor.


![Valor do esquema de desconto de preço](/files/price-discount-scheme-amount.png)


### 4.2 Desconto de produto


1. "Compre 2 quantidades e ganhe 1 quantidade grátis do mesmo item." Para configurar esse tipo de regra, defina o Preço ou Desconto de produto como 'Desconto de produto', marque a caixa de seleção Mesmo item e defina a quantidade.


![Desconto de produto de regra de preços](/files/pricing-rule-same-product-free.png)
2. "Compre 2 quantidades e ganhe 1 quantidade grátis do outro item." Para configurar esse tipo de regras. Defina o preço ou desconto do produto como desconto do produto, desmarque a caixa de seleção 'mesmo item' e defina o 'item gratuito' e a quantidade.


![Pricing Rule Other Product Free](/files/pricing-rule-other-product-free.png)


### 5. Tópicos Relacionados


1. [Esquema promocional](/docs/pt/accounts/promotional-scheme)
2. [Regra fiscal](/docs/pt/accounts/tax-rule)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Item](/docs/pt/stock/item)
