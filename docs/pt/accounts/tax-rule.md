# Regra de Imposto


**Uma regra fiscal aplica impostos automaticamente a transações com base em regras predefinidas.**


Você pode definir qual [Modelo de imposto](/docs/v13/user/manual/en/setting-up/setting-up-taxes.html) deve ser aplicado em uma transação de venda/compra usando Regra de imposto. Isso é decidido por vários fatores, como Cliente, Grupo de clientes, Fornecedor, Grupo de fornecedores, Item, Grupo de itens ou uma combinação deles.


Para acessar a lista de Regras de Imposto, acesse:



>
> Home > Contabilidade > Impostos > Norma Fiscal
>
>
>


## 1. Pré-requisitos


Antes de criar e usar uma regra de imposto, é recomendável criar primeiro o seguinte:


1. [Modelo de impostos e cobranças sobre vendas](/docs/v13/user/manual/en/selling/sales-taxes-and-charges-template)


Ou
2. [Modelo de impostos e cobranças de compra](/docs/v13/user/manual/en/buying/purchase-taxes-and-charges-template)


## 2. Como criar uma regra de imposto


1. Vá para a lista Regra de imposto e clique em Novo.
2. Em Tipo de imposto, selecione se o imposto será aplicado em Vendas ou Compras.
3. Selecione o Modelo de Imposto a ser aplicado.
4. Salve.
![Regra Fiscal](/files/tax-rule.png)


Você pode listar itens online usando o módulo Site. Selecionar 'Usar para Carrinho de Compras' também usará esta Regra de Imposto para transações de Carrinho de Compras. Para saber mais, visite a página [Carrinho de compras](/docs/v13/user/manual/en/e_commerce/carrinho de compras).



>
> Nota: É aconselhável não usar o modelo de vendas/compras selecionado aqui em [Modelo de imposto de item](/docs/v13/user/manual/en/accounts/item-tax-template), pois pode causar interferência. Se você quiser usar as mesmas alíquotas de imposto para Regra de imposto e Modelo de imposto de item, use um nome diferente para Modelos de imposto sobre vendas/compras.
>
>
>


## 3. Características


### 3.1 Aplicação Automática de Regra Fiscal com base no Cliente/Fornecedor


Selecione um Cliente/Fornecedor se o imposto for aplicado a uma parte específica. Deixe-o como Todos os grupos de clientes/Todos os grupos de fornecedores se esta regra fiscal for aplicável a todos os clientes/fornecedores.


Ao selecionar um Cliente/Fornecedor, seus endereços de Cobrança e Envio serão buscados se salvos no cadastro do Cliente/Fornecedor.


### 3.2 Regra de imposto de aplicação automática com base no item/grupo de itens


Ao configurar um Item ou Grupo de Itens na Regra Fiscal, esta Regra Fiscal será automaticamente aplicada a novas transações que tenham o Item/Grupo de Itens selecionado.


### 3.3 Definindo uma categoria de imposto


Definir uma categoria de imposto permite aplicar várias regras de imposto a uma transação com base em diferentes fatores. Para saber mais, visite a página [Categoria fiscal](/docs/v13/user/manual/en/accounts/tax-category).


### 3.4 Validade


Defina uma data inicial e final se o imposto for aplicado apenas por um período especificado. Deixar ambas as datas em branco fará com que a regra de imposto não tenha limites de tempo.


### 3.5 Prioridade


Definir um número de prioridade aqui decidirá em qual ordem uma regra fiscal será aplicada caso várias regras fiscais tenham critérios semelhantes. '1' é a prioridade mais alta, '2' tem prioridade menor e assim por diante.


## 4. Como funciona a regra fiscal?


Vamos configurar a regra de imposto para que o sistema aplique automaticamente taxas de imposto específicas quando uma condição específica corresponder. Por exemplo, se a cidade no endereço de cobrança do cliente for 'Malibu', 6,25% do imposto estadual, 1% do imposto municipal e 2,25% do imposto distrital devem ser aplicados.


Crie um modelo de impostos e cobranças sobre vendas, conforme mostrado abaixo.


![City Specific To Zipcode](/files/city-specific-tax.png)


Crie uma regra de imposto conforme mostrado abaixo.


![Regra Fiscal](/files/tax-rule.png)


Depois de selecionar um cliente e um endereço de cobrança desse cliente com a cidade 'Malibu', o sistema aplica automaticamente os impostos apropriados.


![Regra de imposto na fatura de vendas](/files/tax-rule-in-sales-invoice.gif)


### 5. Tópicos Relacionados


1. [Regra de preços](/docs/v13/user/manual/en/accounts/pricing-rule)
2. [Modelo de imposto do item](/docs/v13/user/manual/en/accounts/item-tax-template)
3. [Categoria fiscal](/docs/v13/user/manual/en/accounts/tax-category)
4. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
5. [Fornecedor](/docs/v13/user/manual/en/buying/supplier)