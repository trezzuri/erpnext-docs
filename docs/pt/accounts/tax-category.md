# Categoria de imposto


**Uma categoria de imposto permite aplicar uma ou mais regras fiscais a transações com base em vários critérios.**


Se você deseja aplicar diferentes tipos de impostos com base nas categorias de impostos, crie categorias de impostos em:



> 
> Página inicial > Contabilidade > Impostos > Categoria fiscal
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma categoria de imposto, é recomendável criar primeiro o seguinte:


1. [Regra fiscal](/docs/pt/accounts/tax-rule)


## 2. Como funciona uma categoria de imposto


Criar uma categoria de imposto é simples, vá para a lista de categoria de imposto, clique em Novo e insira um nome.


* Uma categoria de impostos pode ser vinculada a uma ou mais [Regras de impostos](/docs/pt/accounts/tax-rule).
* Esta categoria de imposto pode ser atribuída a um cliente, portanto, quando esse cliente for selecionado, a categoria de imposto será buscada. Isso também se aplica no caso de um Fornecedor.
* Isso buscará o modelo de imposto sobre vendas vinculado à regra de imposto. Portanto, as linhas da tabela Imposto serão preenchidas automaticamente.
* A categoria de imposto pode ser usada para agrupar clientes aos quais o mesmo imposto será aplicado. Por exemplo, Governo, ONG, comércio, etc.


![Categoria fiscal na fatura de vendas](/files/tax-category-in-invoice.gif)



> 
> Dica: Uma categoria de imposto pode ser atribuída a várias regras de imposto. Assim, você pode criar diferentes combinações para aplicar impostos automaticamente às transações.
> 
> 
> 


## 3. Atribuição de categoria de imposto


A categoria de imposto é determinada automaticamente em uma transação pelo endereço da parte ou mestre da parte (cliente/fornecedor). Você pode atribuir a categoria de imposto com base em:


1. [Cliente](/docs/pt/CRM/customer)
2. [Fornecedor](/docs/pt/buying/supplier)
3. [Endereço](/docs/pt/CRM/address) Cobrança ou Envio.
Você pode selecionar se o endereço de cobrança ou o endereço de entrega tem preferência alterando a opção 'Determinar categoria de imposto de endereço de' em Configurações de contas. A categoria fiscal é determinada a partir do endereço da parte primeiro. Se o endereço não for atribuído a nenhuma categoria de imposto, a categoria de imposto da parte será usada.
 ![Tax Cat Address](/files/tax-category-in-address.png)
4. [Item](/docs/pt/stock/item#316-item-tax)
5. Você também pode selecionar manualmente a categoria de imposto em uma transação.


## 4. Que efeito tem a categoria de imposto em uma transação?


* Modelos de impostos de itens específicos para essa categoria de impostos são definidos automaticamente para os itens.
* Você pode criar [Regras fiscais]({{docs_base_url}}/user/manual/en/accounts/tax-rule) para definir automaticamente um modelo específico de impostos e cobranças sobre vendas/compras com base em diferentes categorias de impostos em transações.


## 5. Tópicos Relacionados


1. [Regra fiscal](/docs/pt/accounts/tax-rule)
2. [Cliente](/docs/pt/CRM/customer)
3. [Fornecedor](/docs/pt/buying/supplier)
4. [Endereço](/docs/pt/CRM/address)
