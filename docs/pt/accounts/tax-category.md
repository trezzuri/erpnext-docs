# Categoria fiscal



**Uma categoria fiscal permite aplicar uma ou mais regras fiscais a transações com base em vários critérios.**


Se você quiser aplicar diferentes tipos de impostos com base em categorias de impostos, crie categorias de impostos a partir de:



> 
> Home > Contabilidade > Impostos > Categoria Fiscal
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma categoria fiscal, é aconselhável criar primeiro o seguinte:


1. [Regra tributária](/docs/pt/accounts/tax-rule)


## 2. Como funciona uma categoria fiscal


Criar uma categoria fiscal é simples, vá até a lista Categoria fiscal, clique em Novo e insira um nome.


* Uma categoria de imposto pode ser vinculada a uma ou mais [Regras fiscais](/docs/pt/accounts/tax-rule).
* Essa Categoria de Imposto pode ser atribuída a um Cliente, portanto, quando esse Cliente for selecionado, a Categoria de Imposto será buscada. Isto também se aplica no caso de um Fornecedor.
* Isso irá buscar o modelo de imposto sobre vendas vinculado à regra fiscal. Assim, as linhas da tabela Imposto serão preenchidas automaticamente.
* A Categoria de Imposto pode ser usada para agrupar Clientes aos quais o mesmo imposto será aplicado. Por exemplo, Governo, ONG, comercial, etc.


![Categoria de imposto na fatura de vendas](/files/tax-category-in-invoice.gif)



> 
> Dica: uma categoria de imposto pode ser atribuída a diversas regras fiscais. Assim, você pode criar diferentes combinações para aplicar impostos automaticamente às transações.
> 
> 
> 


## 3. Atribuição de categoria fiscal


A categoria fiscal é determinada automaticamente em uma transação pelo endereço da parte ou pelo mestre da parte (cliente/fornecedor). Você pode atribuir uma categoria de imposto com base em:


1. [Cliente](/docs/pt/CRM/customer)
2. [Fornecedor](/docs/pt/buying/supplier)
3. [Endereço](/docs/pt/CRM/address) Faturamento ou Envio.
Você pode selecionar se o endereço de cobrança ou o endereço de entrega terá preferência alterando a opção 'Determinar a categoria de imposto do endereço de' nas configurações de contas. A categoria fiscal é determinada primeiro pelo endereço da parte. Se nenhuma categoria fiscal for atribuída ao endereço, será usada a categoria fiscal da parte.
 ![Endereço do gato fiscal](/files/tax-category-in-address.png)
4. [Item](/docs/pt/stock/item#316-item-tax)
5. Você também pode selecionar manualmente a categoria de imposto em uma transação.


## 4. Que efeito a categoria fiscal tem em uma transação?


* Modelos de imposto de item específicos para essa categoria de imposto são definidos automaticamente para itens.
* Você pode criar [Regras fiscais](&lcub;&lcub;docs_base_url}}/user/manual/en/accounts/tax-rule) para definir automaticamente um modelo específico de impostos e cobranças sobre vendas/compra com base em diferentes categorias de impostos nas transações.


## 5. Tópicos Relacionados


1. [Regra tributária](/docs/pt/accounts/tax-rule)
2. [Cliente](/docs/pt/CRM/customer)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Endereço](/docs/pt/CRM/address)



