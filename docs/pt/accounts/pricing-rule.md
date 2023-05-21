# Regra de preços


**Uma regra de preços define as regras de desconto/preço que se aplicam com base em condições definidas.**


Uma regra de preços tem muitas opções com as quais você pode controlar o preço de um item. Filtros como quantidade, data, grupos e outras condições podem ser definidos.


Uma regra de preços é um pouco semelhante a uma [regra fiscal](/docs/v13/user/manual/en/accounts/tax-rule).


A seguir estão alguns casos que podem ser resolvidos usando a regra de precificação:


* De acordo com a política de venda promocional, se o Cliente adquirir mais de 10 unidades de um artigo, usufrui de 20% de desconto.
* Para o Cliente "XYZ", o preço de venda do Item específico deve ser atualizado como ###.
* Os itens categorizados em um grupo de itens específico têm o mesmo preço de venda ou compra.
* Os clientes pertencentes a um grupo de clientes específico devem obter ### preço de venda ou % de desconto nos itens.
* O fornecedor categorizado em Grupo de fornecedores específico deve ter ### taxa de compra aplicada.


Para que a Taxa de Desconto e Lista de Preços de um Item seja aplicada automaticamente, crie Regras de Preços para ele.


Para acessar a lista de regras de preços, acesse:



>
> Home > Contabilidade > Regra de preços
>
>
>


## 1. Pré-requisitos


Antes de criar e usar uma Regra de Precificação, é aconselhável criar primeiro o seguinte:


1. [Item](/docs/v13/user/manual/en/stock/item)
2. [Grupo de itens](/docs/v13/user/manual/en/stock/item-group)
3. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
4. [Fornecedor](/docs/v13/user/manual/en/buying/supplier)


## 2. Como criar uma Regra de Precificação


1. Vá para a lista Regra de preços e clique em Novo.
2. Defina um título para a regra.
3. Selecione o que aplicar em Código do item, Grupo de itens, Marca ou Transação.
4. Selecione se deseja aplicar desconto de preço ou desconto de produto. Se você deseja oferecer produtos gratuitos, selecione o desconto do produto.
![Regra de preços](/files/pricing-rule.png)
5. Para um único item, selecione Código do item e selecione os itens.
6. Se você deseja que a regra de preços seja aplicada a todos os itens, selecione 'Grupo de itens' e selecione **Todos os grupos de itens** (Grupo de itens pai).
7. Defina o desconto/preço a ser aplicado. Para saber mais, [vá para esta seção](/docs/v13/user/manual/en/accounts/pricing-rule#35-price-discount-scheme).
8. Salve.


### 2.1 Opções adicionais ao criar uma Regra de Precificação


#### Armazém


Definir um Armazém aqui fará com que a Regra de Precificação seja aplicada apenas se o Item for selecionado no Armazém especificado aqui.


#### Aplicar regra em


Com base no atributo selecionado no campo 'Aplicar em', você pode definir a regra de precificação com base em um destes:


* [Item](/docs/v13/user/manual/en/stock/item)
* [Grupo de itens](/docs/v13/user/manual/en/stock/item-group)
* Marca
* Transação (sobre o valor total da transação)


Nesta tabela, você pode selecionar o Item/Grupo de Item/Marca específico. Por exemplo, se você selecionar Aplicar em 'Grupo de itens' e selecionar 'Matérias-primas' na tabela, esta regra de precificação será aplicada apenas aos itens que pertencem ao grupo 'Matérias-primas'.


**UM**: A regra de precificação será aplicada somente se a UM definida aqui corresponder à transação.


#### Doença


Neste campo, você pode adicionar uma condição em python para verificar os valores do campo no doctype da transação, conforme mostrado abaixo para Nota Fiscal de Venda:



```
customer=='Nome do cliente' e status!='Atrasado'

```

Por favor, note que apenas condições python de linha única funcionarão, usando nomes de campo do tipo de documento de destino.


#### Condições Mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. A Regra de Precificação será aplicada somente se a soma total dos Itens corresponder às quantidades definidas. Por exemplo, você cria uma regra de preços no item 1 e no item 2 e define a quantidade mínima e máxima como 30, a regra de preços será aplicada somente se a quantidade total for 30.


#### é cumulativo


Habilitar esta opção permite que a Regra de Precificação seja aplicada cumulativamente. Você precisa definir 'Min Amt' e 'Max Amt' para isso.


Considere um cenário em que Min Amt é 1.500 e Max Amt é 2.000. Agora, se uma transação for criada para 1.400, a regra de preços não será aplicada. No entanto, ao criar uma segunda fatura de valor 600, a regra de preços será aplicada. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas na última transação que ultrapasse o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Características


### 3.1 Aplicar regra em outros


Este recurso verifica a condição do primeiro item, mas aplica a regra em outro item.


![Aplicar regra de preços em outro item](/files/pricing-rule-on-other-item.png)


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' no Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Precificação será aplicada no Item3, pois os dois primeiros itens estavam presentes na transação.


### 3.2 Informações da Parte


Defina se a regra de preços é para venda ou compra do item.


Com base na sua seleção, você pode definir a aplicabilidade para um dos seguintes mestres.


* [Cliente](/docs/v13/user/manual/en/CRM/cliente)
* [Grupo de clientes](/docs/v13/user/manual/en/CRM/customer-group)
* [Território](/docs/v13/user/manual/en/selling/território)
* [Parceiro de vendas](/docs/v13/user/manual/en/selling/sales-partner)
* [Campanha](/docs/v13/user/manual/en/CRM/campanha)
* [Fornecedor](/docs/v13/user/manual/en/buying/supplier)
*Grupo Fornecedor


### 3.3 Quantidade e Valor


Especifique a quantidade mínima, quantidade máxima, quantidade mínima ou quantidade máxima de um Item quando esta Regra de Precificação deve ser aplicada.


Observe que, se a quantidade ou valor ficar aquém ou exceder os limites definidos aqui, a regra de preços não será aplicada. No entanto, será aplicado se você tiver habilitado as opções Condições Mistas ou Cumulativas.


![Quantidade e valor da regra de preços](/files/pricing-rule-quantity-and-amount.png)


### 3.4 Validade


Você também pode definir um intervalo de datas para quando a regra de preços será válida. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco a Regra de Precificação não terá limite de tempo.


![Configurações do período da regra de preços](/files/pricing-rule-period-settings.png)


### 3,5 Margem


![Margem da regra de preços](/files/pricing-rule-margin.png)


* **Tipo de Margem**: Ao vender um Item, você pode vendê-lo por uma certa margem. Se você não quiser adicionar preços de venda aos itens todas as vezes e quiser definir uma margem automaticamente, isso pode ser feito com este recurso.
* **Taxa ou Valor de Margem**: A margem definida pode ser baseada em Porcentagem ou Valor, por exemplo: margem de 5% ou margem fixa de $ 50.


Leia [adicionando margem](/docs/v13/user/manual/en/selling/articles/adding-margin) para mais detalhes.


### 3.6 Esquema de Desconto de Preço


A regra real a ser aplicada é definida nesta seção.


![Regra de desconto de preços](/files/pricing-rule-discount-scheme.png)


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vender um Item por 100 e quiser vendê-lo por 112 para uma festa específica, selecione Taxa e defina a Taxa como 112.
* **Porcentagem de desconto**: Uma porcentagem de desconto específica pode ser definida. A porcentagem de desconto pode ser definida para uma [Lista de preços] específica (/docs/v13/user/manual/en/stock/listas de preços). Deixar o campo 'Para lista de preços' em branco aplicará a regra de preços a todas as listas de preços.
* **Valor do desconto**: Será aplicado um valor de desconto fixo. Por exemplo, se você vender um Item por 100 e quiser vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do Desconto.


### 3.7 Configurações Avançadas


![Configurações avançadas da regra de preços](/files/pricing-rule-advanced-settings.png)


* **Limite para Sugestão**: Este é o limite com base no qual o sistema irá notificá-lo para ajustar a Quantidade de Item para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicado. Isso também se aplica ao valor definido.
* **Prioridade**: Considere um Grupo de Itens, você deseja definir regras específicas para um Item do grupo. Isso pode ser feito criando uma nova regra de precificação e definindo uma prioridade mais alta. Isso também pode se aplicar ao Grupo de clientes e ao Grupo de fornecedores.
* **Aplique várias regras de precificação**: Para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Habilitar esta opção aplicará um total de 15% na Taxa do Item, que dá 425.
* **Aplicar desconto na tarifa**: O desconto será composto. Considere o mesmo cenário acima. Ao ativar esta opção, 10% serão aplicados em 500, o que resultará em 450, depois 5% serão aplicados em 450, o que resultará em 427,5.
* **Validar Regra Aplicada**: Mostra a mensagem de validação inserida se o desconto/taxa definido manualmente por você em uma transação não corresponder à Regra de Precificação.


Isso é útil quando o distribuidor top na hierarquia decide o desconto/tarifa a ser aplicado e você só está validando se a Regra de Precificação foi aplicada corretamente.


## 4. Tipos de desconto de regra de preços


### 4.1 Desconto no Preço


1. Em Tipo de margem, você pode definir se a margem é calculada como uma porcentagem ou um valor. Ex.: margem de 10% sobre a tabela de preços do fornecedor na hora da venda.
2. A tarifa mencionada na regra de preços terá prioridade sobre a tabela de preços do item (preço do item).


![Taxa do esquema de descontos de preços](/files/price-discount-scheme-rate.png)
3. A porcentagem de desconto pode ser aplicada para uma tabela de preços específica (venda ou compra). Para aplicá-lo para ambos, deixe o campo 'Para Tabela de Preços' em branco.


![Desconto de esquema de desconto de preço](/files/price-discount-scheme-discount.png)
4. O desconto também pode ser definido em termos de valor.


![Valor do esquema de desconto de preço](/files/price-discount-scheme-amount.png)


### 4.2 Desconto de Produto


1. "Compre 2 quantidades e ganhe 1 quantidade grátis do mesmo item." Para configurar esse tipo de regra, defina o Preço ou Desconto de Produto como 'Desconto de Produto', marque a caixa de seleção Mesmo Item e defina a quantidade.


![Desconto de produto de regra de preços](/files/pricing-rule-same-product-free.png)
2. "Compre 2 quantidades e ganhe 1 quantidade grátis do outro item." Para configurar esse tipo de regras. Defina o preço ou desconto do produto como desconto do produto, desmarque a caixa de seleção 'mesmo item' e defina o 'item gratuito' e a quantidade.


![Pricing Rule Other Product Free](/files/pricing-rule-other-product-free.png)


### 5. Tópicos Relacionados


1. [Esquema promocional](/docs/v13/user/manual/en/accounts/promotional-scheme)
2. [Regra fiscal](/docs/v13/user/manual/en/accounts/tax-rule)
3. [Fornecedor](/docs/v13/user/manual/en/buying/supplier)
4. [Item](/docs/v13/user/manual/en/stock/item)