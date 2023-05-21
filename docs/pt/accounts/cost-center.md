# Centro de custo


**Um Centro de Custos é uma parte de uma organização onde custos ou receitas podem ser cobrados.**


No ERPNext você pode utilizar o Centro de Custo como Centro de Lucro.


Seu plano de contas é projetado principalmente para fornecer relatórios ao governo e às autoridades fiscais.


A maioria das empresas tem várias atividades, como diferentes linhas de produtos, segmentos de mercado, áreas de negócios, etc., que compartilham algumas despesas gerais comuns. Eles devem idealmente ter sua própria estrutura para relatar se eles
são rentáveis ​​ou não. Para isso, existe uma estrutura alternativa chamada Tabela de Centros de Custo.


Um Centro de Custo funciona como uma [Dimensão Contábil](/docs/v13/user/manual/en/accounts/accounting-dimensions) que ajuda você a rastrear custos com base em áreas específicas.


O Centro de Custo pode ser definido nestes níveis:


* Empresa
* Item
* Pedido/Fatura


O Centro de Custo pode ser vinculado às seguintes transações:


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)
3. [Entrada de diário](/docs/v13/user/manual/en/accounts/journal-entry)
4. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
5. [Nota de entrega](/docs/v13/user/manual/en/stock/nota de entrega)


E outras transações que podem ser usadas para orçamentação. Você também pode usar o Centro de Custo para [Orçamento](/docs/v13/user/manual/en/accounts/orçamento).


## 1. Árvore de Centro de Custo


Você pode criar uma árvore de Centros de Custo para representar melhor o seu negócio. Cada
A entrada de receita/despesa também é marcada em um centro de custo. Se 'Permitir Entrada de Centro de Custo na Conta de Balanço' estiver marcado em Configurações de Conta, o sistema permitirá que um Usuário marque entrada em Contas de Balanço em relação a um Centro de Custo.


Por exemplo, se você tiver dois tipos de vendas:


*Vendas à vista
* Vendas online


Você pode não ter despesas de envio para seus clientes walk-in e nenhuma compra
aluguel para seus clientes online. Se você deseja obter a rentabilidade de cada
destes separadamente, você deve criar os dois como Centros de Custo e marcar todos
vendas com Centro de Custo "Pessoal" ou "Online". Marque todas as suas compras no
mesma maneira.


Assim, quando você faz sua análise, você entende melhor de que lado
do seu negócio está indo melhor. Como o ERPNext tem a opção de adicionar vários
Empresas, você pode criar Centros de Custo para cada Empresa e gerenciá-los
separadamente.


Para acessar a Tabela de Centros de Custo, acesse:



>
> Home > Contabilidade > Orçamento e Centro de Custo > Tabela de Centros de Custo
>
>
>


## 2. Como configurar a Tabela de Centros de Custo


1. Acesse a Tabela de Centros de Custo.
2. Adicione nós regionais.
3. Adicione outros nós de acordo com suas necessidades.


Selecionar uma empresa diferente exibirá os centros de custo dessa empresa.


![Centro de custo](/files/chart-of-cost-center.png)


![Tabela de Centros de Custo](/files/company-master.png)


### 3. Tópicos Relacionados


1. [Orçamento](/docs/v13/user/manual/en/accounts/orçamento)
2. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
3. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)