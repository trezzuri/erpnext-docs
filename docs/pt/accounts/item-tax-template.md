# Modelo de imposto de item


**Modelo de imposto de item é útil para tributação de itens.**


Se alguns de seus itens tiverem taxas de imposto diferentes da taxa de imposto padrão atribuída na tabela Impostos e encargos, você poderá criar um Modelo de imposto de item e atribuí-lo a um [Item](/docs/v13/user/manual/en/ estoque/item) ou [Grupo de itens](/docs/v13/user/manual/en/stock/item-group). A alíquota atribuída no Modelo de imposto do item terá preferência sobre a alíquota padrão atribuída na tabela Impostos e encargos.


Por exemplo, se o imposto GST 18% for adicionado à tabela Impostos e Encargos no Pedido de Venda, ele será aplicado a todos os itens desse Pedido de Venda. No entanto, se você precisar aplicar uma taxa de imposto diferente em alguns dos itens, as etapas são fornecidas abaixo


Para acessar a lista de Modelo de imposto de item, vá para



>
> Home > Contabilidade > Impostos > Modelo de imposto de item
>
>
>


Vamos supor que estamos criando um Pedido de Venda. Temos o [Modelo de impostos e cobranças sobre vendas](/docs/v13/user/manual/en/selling/sales-taxes-and-charges-template) mestre para GST 9%. De todos os Itens de Venda, em um Item, apenas 5% GST será aplicado, enquanto outro item está isento de imposto (não tributável). Você precisa selecionar o Chefe de Conta do imposto e definir sua alíquota predominante.


## 1. Pré-requisitos


Antes de criar e usar um modelo de imposto de item, é recomendável criar primeiro o seguinte:


1. [Item](/docs/v13/user/manual/en/stock/item)
2. Habilite 'Adicionar impostos e cobranças automaticamente do modelo de imposto do item' em [Configurações da conta](/docs/v13/user/manual/en/accounts/accounts-settings)


## 2. Como criar um modelo de imposto de item


1. Vá para a lista Modelo de imposto de item e clique em Novo.
2. Insira um título para o Modelo de imposto do item.
3. Selecione uma conta e defina a taxa de substituição. Adicione mais linhas, se necessário.
4. Salve.


Agora o Modelo de Imposto do Item está pronto para ser atribuído a um Item. Para fazer isso, vá para a seção Item, Item Tax e selecione um Item Tax Template:


![Item Tax In Item](/files/item-tax-in-item.png)



>
> Nota: É aconselhável não usar o Modelo de Vendas/Compras selecionado aqui em [Regra Fiscal](/docs/v13/user/manual/en/accounts/regra fiscal), pois pode causar interferência. Se você quiser usar as mesmas alíquotas de imposto para Regra de imposto e Modelo de imposto de item, use um nome diferente para Modelos de imposto sobre vendas/compras.
>
>
>


### 2.1 Mencionar Imposto Aplicável no cadastro do Item


Os modelos de impostos são predefinidos com valores. Para itens que possuem alíquota diferente dos demais, é necessário alterá-la no cadastro de Itens. Acesse a tabela de impostos no Item, adicione uma linha, selecione o tipo de imposto e altere a alíquota. Agora, esta nova taxa irá substituir o modelo ao criar um pedido/fatura. Por exemplo, na captura de tela abaixo, você pode ver que a taxa de imposto está definida como 5 e essa é a taxa que será aplicada nas transações.


![Imposto por item](/files/item-wise-tax.png)


Para o Item totalmente isento de impostos, mencione 0% como taxa de imposto no mestre do Item.


![Item isento de impostos](/files/tax-isento-item.png)



>
> Observação: para que o modelo de imposto do item funcione, você precisa garantir que os tipos de impostos (contas) definidos no modelo de imposto do item (com taxas de imposto alteradas) estejam presentes no modelo de impostos e encargos sobre vendas.
>
>
>



>
> Se você deseja incluir vários itens com taxas de impostos diferentes, é necessário registrá-los em diferentes cabeçalhos de impostos. Por exemplo, IVA 14%, IVA 5%, etc.
>
>
>


### 2.2 Cálculo do Imposto na transação


Em transações de vendas como Cotação, Pedido de Venda e Fatura de Venda, os impostos sobre os itens são calculados de acordo com o Modelo de Impostos e Encargos de Vendas selecionado. No entanto, se alguns itens tiverem um Modelo de imposto de item vinculado, os impostos serão calculados sobre esses itens de acordo com as taxas mencionadas no Modelo de imposto de item, em vez das taxas mencionadas no Modelo de impostos e encargos sobre vendas.


Por exemplo, na captura de tela a seguir, você pode ver que os impostos são calculados em 3%, embora a taxa de acordo com o modelo de impostos e encargos sobre vendas seja de 6,25%.


![Cálculo de imposto](/files/tax-calculation.png)


### 2.3 Modelo de imposto de item para cada item


Você também pode selecionar manualmente um modelo de imposto de item diferente para cada item em uma transação:


![Selecionar modelo de imposto sobre o item](/files/select-item-tax-template.png)


### 2.4 Imposto sobre itens em um grupo de itens


Você pode atribuir o Modelo de imposto do item a um Grupo de itens modificando a tabela Imposto do item na seção Imposto do item no documento Grupo de itens.


![Modelo de imposto do item no grupo de itens](/files/item-tax-template-in-item-group.png)


O Modelo de imposto de item aplicado a um Grupo de itens se aplicará a todos os Itens desse grupo, a menos que um Item individual no Grupo de itens tenha seu próprio Modelo de imposto de item atribuído a ele.


### 2.5 Validade dos Impostos de Item


![Imposto do item no grupo de itens](/files/item-tax-in-item.png)


Você também pode atribuir validade aos modelos de impostos conforme mostrado na imagem acima.


* Com base na data de lançamento da transação, um modelo de imposto válido será obtido automaticamente.
* Se houver mais de um modelo de imposto válido, o primeiro modelo de imposto válido da tabela de impostos do item será obtido.
* No caso de não haver modelos de imposto válidos, o primeiro modelo de imposto sem data 'Válido de' na tabela de impostos do item será obtido.



>
> Observação: ao adicionar itens na fatura de compra, a primeira preferência será dada a 'Data da fatura do fornecedor' em vez de 'Data de postagem' para buscar um modelo de imposto de item válido.
>
>
>


### 2.6 Alguns pontos a observar


* Se você definir a categoria de imposto como vazia, o modelo de imposto padrão do item será aplicado aos itens nas transações.
* Você pode aplicar diferentes modelos de impostos de itens para diferentes categorias de impostos.
* Para que um Modelo de Imposto de Item substitua os impostos, deve haver uma linha na tabela Impostos e Encargos com o mesmo Cabeçalho de Conta de imposto com uma taxa de imposto padrão.
* Se você deseja aplicar impostos apenas nos itens com um modelo de imposto de item, pode definir a taxa de imposto padrão como 0.


### 3. Tópicos Relacionados


1. [Regra fiscal](/docs/v13/user/manual/en/accounts/tax-rule)
2. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
3. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)