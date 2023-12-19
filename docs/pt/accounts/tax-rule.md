# Regra Fiscal



**Uma regra fiscal aplica automaticamente impostos a transações com base em regras predefinidas.**


Você pode definir qual [Modelo de Imposto](/docs/pt/setting-up/setting-up-taxes.html) deve ser aplicado em uma Venda/Compra transação usando regra fiscal. Isso é decidido por vários fatores, como Cliente, Grupo de Clientes, Fornecedor, Grupo de Fornecedores, Item, Grupo de Itens ou uma combinação destes.


Para acessar a lista de Regras Tributárias, acesse:
> Home > Contabilidade > Impostos > Regras Tributárias


## 1. Pré-requisitos


Antes de criar e usar uma Regra Fiscal, é aconselhável criar primeiro o seguinte:


1. [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template)


Ou
2. [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template)


## 2. Como criar uma regra tributária


1. Vá para a lista de regras fiscais e clique em Novo.
2. Em Tipo de imposto, selecione se o imposto será aplicado nas vendas ou nas compras.
3. Selecione o modelo de imposto a ser aplicado.
4. Salvar.
![Regra Fiscal](/files/tax-rule.png)


Você pode listar itens on-line usando o módulo Website. Selecionar 'Usar para carrinho de compras' também usará esta regra fiscal para transações no carrinho de compras. Para saber mais, visite a página do [Carrinho de compras](/docs/pt/e_commerce/shopping-cart).


> Observação: é aconselhável não usar o modelo de vendas/compra selecionado aqui em [Modelo de imposto de item](/docs/pt/accounts/item-tax-template), pode causar interferência. Se você quiser usar as mesmas taxas de imposto para a Regra Fiscal e o Modelo de Imposto sobre Itens, use um nome diferente para os Modelos de Imposto sobre Vendas/Compras.


## 3. Recursos


### 3.1 Aplicação automática de regra fiscal com base no cliente/fornecedor


Selecione um Cliente/Fornecedor se o imposto for aplicado a uma parte específica. Deixe como Todos os grupos de clientes/Todos os grupos de fornecedores se esta regra fiscal for aplicável a todos os clientes/fornecedores.


Ao selecionar um Cliente/Fornecedor seus endereços de Cobrança e Envio serão buscados se salvos no cadastro do Cliente/Fornecedor.


### 3.2 Aplicação automática de regra fiscal com base no item/grupo de itens


Ao definir um Item ou Grupo de Itens na Regra Fiscal, esta Regra Fiscal será aplicada automaticamente às novas transações que tenham o Item/Grupo de Itens selecionado.


### 3.3 Definindo uma categoria fiscal


Definir uma categoria fiscal permite aplicar múltiplas regras fiscais a uma transação com base em diferentes fatores. Para saber mais, visite a página [Categoria de imposto](/docs/pt/accounts/tax-category).


### 3.4 Validade


Defina uma data de início e de término se o imposto for aplicado apenas por um período especificado. Deixar ambas as datas em branco fará com que a Regra Fiscal não tenha limites de tempo.


### 3,5 Prioridade


Definir um número de prioridade aqui decidirá em qual ordem uma Regra Fiscal será aplicada caso diversas Regras Fiscais tenham critérios semelhantes. '1' é a prioridade mais alta, '2' tem prioridade menor e assim por diante.


## 4. Como funciona a regra tributária?


Vamos configurar a Regra Fiscal para que o sistema aplique automaticamente taxas de imposto específicas quando uma condição específica corresponder. Por exemplo, se a cidade no endereço de cobrança do cliente for 'Malibu', então deverá ser aplicado um imposto estadual de 6,25%, um imposto municipal de 1% e um imposto distrital de 2,25%. 


Crie um modelo de impostos e cobranças sobre vendas conforme mostrado abaixo.


![Cidade específica para CEP](/files/city-specific-tax.png)


Crie uma regra fiscal conforme mostrado abaixo.


![Regra Fiscal](/files/tax-rule.png)


Depois de selecionar um cliente e um endereço de cobrança desse cliente com a cidade como 'Malibu', o sistema aplicará automaticamente os impostos apropriados.


![Regra tributária na fatura de vendas](/files/tax-rule-in-sales-invoice.gif)


### 5. Tópicos Relacionados


1. [Regra de preços](/docs/pt/accounts/pricing-rule)
2. [Modelo de imposto de item](/docs/pt/accounts/item-tax-template)
3. [Categoria de imposto](/docs/pt/accounts/tax-category)
4. [Cliente](/docs/pt/CRM/customer)
5. [Fornecedor](/docs/pt/buying/supplier)



