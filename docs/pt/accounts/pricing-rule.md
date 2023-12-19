# Regra de preços



**Uma regra de preços define as regras de descontos/preços aplicáveis ​​com base nas condições definidas.**


Uma regra de preços tem muitas opções com as quais você pode controlar o preço de um item. Filtros como quantidade, data, grupos e outras condições podem ser definidos.


Uma regra de preços é um pouco semelhante a uma [regra fiscal](/docs/pt/accounts/tax-rule).


A seguir estão alguns casos que podem ser resolvidos usando a regra de precificação:


* De acordo com a política de venda promocional, se o Cliente adquirir mais de 10 unidades de um artigo, usufrui de 20% de desconto.
* Para o Cliente "XYZ", o preço de venda do Item específico deve ser atualizado como ###.
* Os itens categorizados em um grupo de itens específico têm o mesmo preço de venda ou compra.
* Os clientes pertencentes a um grupo de clientes específico devem obter ### preço de venda ou% de desconto em itens.
* O fornecedor categorizado em um grupo de fornecedores específico deve ter ### taxa de compra aplicada.


Para que o desconto e a taxa da lista de preços sejam aplicados automaticamente para um item, crie regras de preços para ele.


Para acessar a lista de regras de preços, acesse:



> 
> Página inicial > Contabilidade > Regra de preços
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma regra de precificação, é aconselhável criar primeiro o seguinte:


1. [Item](/docs/pt/stock/item)
2. [Grupo de itens](/docs/pt/stock/item-group)
3. [Cliente](/docs/pt/CRM/customer)
4. [Fornecedor](/docs/pt/buying/supplier)


## 2. Como criar uma regra de preços


1. Vá para a lista de regras de preços e clique em Novo.
2. Defina um título para a regra.
3. Selecione o que aplicar em código do item, grupo de itens, marca ou transação.
4. Selecione se deseja aplicar Desconto no preço ou Desconto no produto. Se você quiser oferecer produtos gratuitos, selecione o desconto do produto.
![Regra de preços](/files/pricing-rule.png)
5. Para um único item, selecione Código do item e selecione os itens.
6. Se desejar que a Regra de Preços seja aplicada a todos os itens, selecione 'Grupo de Itens' e selecione **Todos os Grupos de Itens** (Grupo de Itens pai).
7. Defina o desconto/preço a ser aplicado. Para saber mais, [acesse esta seção](/docs/pt/accounts/pricing-rule#35-price-discount-scheme).
8. Salvar.


### 2.1 Opções adicionais ao criar uma regra de precificação


#### Armazém


Definir um Armazém aqui fará com que a Regra de Preços seja aplicada somente se o Item for selecionado no Armazém especificado aqui.


#### Aplicar regra em


Com base no atributo selecionado no campo "Inscrever-se em", você pode definir a regra de preços com base em um destes:


* [Item](/docs/pt/stock/item)
* [Grupo de itens](/docs/pt/stock/item-group)
* Marca
* Transação (sobre o valor total da transação)


Nesta tabela, você pode selecionar o item/grupo de itens/marca específico. Por exemplo, se você selecionar Aplicar em 'Grupo de Itens' e selecionar 'Matérias-Primas' na tabela, esta Regra de Preços será aplicada apenas em Itens que pertencem ao Grupo 'Matérias-Primas'.


**UM**: a regra de preços será aplicada somente se a UM definida aqui corresponder à transação.


#### Condição


Neste campo você pode adicionar uma condição em python para verificar os valores do campo no tipo de documento da transação, como mostrado abaixo para fatura de vendas:



```
customer=='Nome do cliente' e status!='Atrasado'

```

Observe que apenas condições Python de linha única funcionarão, usando nomes de campo do tipo de documento de destino.


#### Condições Mistas


Se você selecionar dois ou mais itens e definir a quantidade mínima e máxima. A Regra de Preços será aplicada apenas se a soma total dos Itens corresponder às quantidades definidas. Por exemplo, você cria uma Regra de Preços no Item 1 e no Item 2 e define a Quantidade Mínima e Máxima como 30. A Regra de Preços será aplicada somente se a quantidade total for 30.


#### É cumulativo


Ativar esta opção permite que a Regra de Preços seja aplicada cumulativamente. Você precisa definir o 'Valor mínimo' e o 'Valor máximo' para isso.


Considere um cenário em que o valor mínimo é 1.500 e o valor máximo é 2.000. Agora, se uma transação for criada para 1.400, a Regra de Preços não será aplicada. Porém, ao criar uma segunda fatura de valor 600, será aplicada a Regra de Preços. Isso aconteceu porque o valor total (acumulado) das faturas somou 2.000. Observe que o desconto será aplicado apenas à última transação que ultrapassar o limite cumulativo.


Isso pode ser útil para dar descontos se um Cliente comprar um Item várias vezes e você quiser recompensá-lo com descontos/preços especiais.


## 3. Recursos


### 3.1 Aplicar regra a outros


Este recurso verifica a condição do primeiro item, mas aplica regras em outro item.


![Aplicar regra de precificação em outro item](/files/pricing-rule-on-other-item.png)


Por exemplo, defina Item1 e Item2 na tabela 'Aplicar regra em' e defina 'Aplicar regra em outro' no Item3. Agora, se a transação tiver Item1, Item2 e Item3, a Regra de Preços será aplicada ao Item3, já que os dois primeiros Itens estavam presentes na transação.


### 3.2 Informações da parte


Defina se a regra de preço é para venda ou compra do item.


Com base na sua seleção, você pode definir a aplicabilidade para um dos seguintes mestres.


* [Cliente](/docs/pt/CRM/customer)
* [Grupo de clientes](/docs/pt/CRM/customer-group)
* [Território](/docs/pt/selling/territory)
* [Parceiro de vendas](/docs/pt/selling/sales-partner)
* [Campanha](/docs/pt/CRM/campaign)
* [Fornecedor](/docs/pt/buying/supplier)
* Grupo de fornecedores


### 3.3 Quantidade e valor


Especifique a quantidade mínima, a quantidade máxima, o valor mínimo ou o valor máximo de um item quando esta regra de preços deve ser aplicada.


Observe que se a quantidade ou valor ficar abaixo ou exceder os limites definidos aqui, a Regra de Preços não será aplicada. Porém, será aplicado se você tiver habilitado as opções Condições Mistas ou Cumulativas.


![Quantidade e valor da regra de preços](/files/pricing-rule-quantity-and-amount.png)


### 3.4 Validade


Você também pode definir um intervalo de datas para a validade da regra de precificação. Isso é útil para uma promoção de vendas. Ao deixar as datas em branco a Regra de Preços não terá limite de prazo.


![Configurações do período da regra de precificação](/files/pricing-rule-period-settings.png)


### Margem 3,5


![Margem da regra de preços](/files/pricing-rule-margin.png)


* **Tipo de margem**: Ao vender um item, você pode vendê-lo por uma determinada margem. Se você não quiser adicionar preços de venda aos itens todas as vezes e quiser definir uma margem automaticamente, isso pode ser feito com este recurso.
* **Taxa ou valor de margem**: a margem definida pode ser baseada em porcentagem ou valor, por exemplo: margem de 5% ou margem fixa de US$ 50.


Leia [adicionar margem](/docs/pt/selling/articles/adding-margin) para obter mais detalhes.


### 3.6 Esquema de desconto de preço


A regra real a ser aplicada é definida nesta seção.


![Desconto na regra de preços](/files/pricing-rule-discount-scheme.png)


* **Taxa**: Esta será a nova taxa para um Item. Por exemplo, se você vende um item por 100 e deseja vendê-lo por 112 para um grupo específico, selecione Taxa e defina a Taxa como 112.
* **Porcentagem de desconto**: Uma porcentagem de desconto específica pode ser definida. A porcentagem de desconto pode ser definida para uma [lista de preços](/docs/pt/stock/price-lists) específica. Deixar 'Para Lista de Preços' em branco aplicará a Regra de Preços a todas as Listas de Preços.
* **Valor do desconto**: Um valor de desconto fixo será aplicado. Por exemplo, se você vende um item por 100 e deseja vendê-lo com um desconto de 7, essa condição pode ser definida usando a opção Valor do desconto.


### 3.7 Configurações avançadas


![Configurações avançadas da regra de precificação](/files/pricing-rule-advanced-settings.png)


* **Limite para sugestão**: este é o limite com base no qual o sistema irá notificá-lo para ajustar a quantidade de itens para desconto. Por exemplo, se a Quantidade Mínima for 10 e o Limite for 9, o sistema notificará para adicionar mais 1 Item para que o desconto seja aplicável. Isto também se aplica ao valor definido.
* **Prioridade**: considere um grupo de itens, você deseja definir regras específicas para um item do grupo. Isso pode ser feito criando uma nova Regra de Preços e definindo uma prioridade mais alta. Isso também pode se aplicar ao Grupo de Clientes e ao Grupo de Fornecedores.
* **Aplicar múltiplas regras de precificação**: para entender isso, considere um item de taxa 500. Existem duas regras de precificação nele, P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Ativar esta opção aplicará um total de 15% na taxa do item, o que dá 425.
* **Aplicar Desconto na Tarifa**: O desconto será capitalizado. Considere o mesmo cenário acima. Ao ativar esta opção, 10% serão aplicados em 500, o que dará 450, e 5% serão aplicados em 450, o que dará 427,5.
* **Validar regra aplicada**: mostra a mensagem de validação inserida se o desconto/taxa definido manualmente por você em uma transação não corresponder à regra de preços.


Isso é útil quando o distribuidor superior na hierarquia decide o desconto/taxa a ser aplicado e você só está validando se a Regra de Preços for aplicada corretamente.


## 4. Tipos de descontos de regras de preços


### 4.1 Desconto no preço


1. Em Tipo de Margem, você pode definir se a margem será calculada como uma porcentagem ou um valor. Ex: margem de 10% na tabela de preços do fornecedor no momento da venda.
2. A taxa mencionada na Regra de Preços terá prioridade sobre a taxa da Lista de Preços do Item (Preço do Item).


![Taxa do esquema de desconto de preço](/files/price-discount-scheme-rate.png)
3. A Porcentagem de Desconto pode ser aplicada para uma Lista de Preços específica (Venda ou Compra). Para aplicá-lo a ambos, deixe o campo 'Para lista de preços' em branco.


![Desconto do esquema de desconto de preço](/files/price-discount-scheme-discount.png)
4. O desconto também pode ser definido em termos de valor.


![Valor do esquema de desconto de preço](/files/price-discount-scheme-amount.png)


### 4.2 Desconto em produtos


1. "Compre 2 quantidades e ganhe 1 quantidade grátis do mesmo item." Para configurar esse tipo de regras, defina o Preço ou Desconto no Produto como 'Desconto no Produto', marque a caixa de seleção Mesmo Item e defina a quantidade.


![Regra de preços para desconto em produtos](/files/pricing-rule-same-product-free.png)
2. "Compre 2 quantidades e ganhe 1 quantidade grátis do outro item." Para configurar este tipo de regras. Defina o Preço ou Desconto do Produto como Desconto do Produto, desmarque a caixa de seleção 'Mesmo Item' e defina o 'Item Grátis' e a quantidade.


![Regra de preços para outro produto gratuito](/files/pricing-rule-other-product-free.png)


### 5. Tópicos Relacionados


1. [Esquema promocional](/docs/pt/accounts/promotional-scheme)
2. [Regra tributária](/docs/pt/accounts/tax-rule)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Item](/docs/pt/stock/item)



