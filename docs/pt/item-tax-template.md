# Modelo de imposto de item



**O modelo de imposto sobre itens é útil para tributação de itens.**


Se alguns de seus itens tiverem taxas de imposto diferentes da taxa de imposto padrão atribuída na tabela Impostos e Encargos, você poderá criar um modelo de imposto de item e atribuí-lo a um [Item](/docs/pt/stock/item) ou [Grupo de itens](/docs/pt/stock/item-group). A alíquota atribuída no Modelo de Imposto do Item terá preferência sobre a alíquota padrão atribuída na tabela Impostos e Encargos.


Por exemplo, se o imposto GST de 18% for adicionado à tabela Impostos e Encargos no Pedido de Venda, ele será aplicado a todos os itens desse Pedido de Venda. No entanto, se você precisar aplicar taxas de imposto diferentes em alguns dos itens, as etapas são fornecidas abaixo


Para acessar a lista de modelos de imposto de item, vá para
> Home > Contabilidade > Impostos > Modelo de Imposto sobre Itens


Vamos supor que estamos criando um Pedido de Venda. Temos o [Modelo de impostos e encargos sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template) mestre para GST 9%. De todos os Itens de Venda, em um Item será aplicado apenas 5% de GST, enquanto outro item está isento de impostos (não tributável). Você precisa selecionar o responsável pela conta do imposto e definir sua alíquota predominante.


## 1. Pré-requisitos


Antes de criar e usar um modelo de imposto de item, é aconselhável criar primeiro o seguinte:


1. [Item](/docs/pt/stock/item)
2. Ative a opção "Adicionar automaticamente impostos e cobranças do modelo de imposto de item" em [Configurações da conta](/docs/pt/accounts/accounts-settings)


## 2. Como criar um modelo de imposto sobre itens


1. Vá para a lista Modelo de imposto de item e clique em Novo.
2. Insira um título para o modelo de imposto de item.
3. Selecione uma conta e defina a taxa predominante. Adicione mais linhas, se necessário.
4. Salvar.


Agora o modelo de imposto de item está pronto para ser atribuído a um item. Para fazer isso, vá para a seção Item, Imposto sobre Itens e selecione um Modelo de Imposto sobre Itens:


![Imposto sobre item no item](/files/item-tax-in-item.png)


> Observação: é aconselhável não usar o modelo de vendas/compra selecionado aqui em [Regra tributária](/docs/pt/accounts/tax-rule), isso pode causar interferência. Se você quiser usar as mesmas taxas de imposto para a Regra Fiscal e o Modelo de Imposto sobre Itens, use um nome diferente para os Modelos de Imposto sobre Vendas/Compras.


### 2.1 Mencionar Imposto Aplicável no cadastro de itens


Os modelos de impostos são predefinidos com valores. Para itens que possuem alíquota de imposto diferente dos demais, é necessário alterá-la no Cadastro de itens. Acesse a tabela de impostos no Item, adicione uma linha, selecione o tipo de imposto e altere a alíquota. Agora, esta nova taxa substituirá o modelo ao criar um pedido/fatura. Por exemplo, na captura de tela abaixo você pode ver que a alíquota do imposto está definida como 5 e essa é a alíquota que será aplicada nas transações.


![Imposto sobre item](/files/item-wise-tax.png)


Para o item totalmente isento de impostos, mencione 0% como alíquota de imposto no cadastro de itens.


![Item isento de impostos](/files/tax-exempted-item.png)


> Observação: para que o Modelo de Imposto sobre Itens funcione, você precisa garantir que os tipos de impostos (contas) definidos no Modelo de Imposto sobre Itens (com taxas de imposto alteradas) estejam presentes no Modelo de Impostos e Encargos sobre Vendas.


> Se você quiser incluir vários itens com diferentes alíquotas de impostos, será necessário registrá-los em diferentes títulos de impostos. Por exemplo, IVA 14%, IVA 5% etc.


### 2.2 Cálculo de imposto na transação


Em transações de vendas como Cotação, Pedido de Venda e Fatura de Venda, os impostos sobre os itens são calculados de acordo com o Modelo de Impostos e Encargos sobre Vendas selecionado. No entanto, se alguns itens tiverem um Modelo de Imposto sobre Itens vinculado, os impostos serão calculados sobre esses itens de acordo com as taxas mencionadas no Modelo de Imposto sobre Itens, em vez das taxas mencionadas no Modelo de Impostos e Encargos sobre Vendas.


Por exemplo, na captura de tela a seguir, você pode ver que os impostos são calculados em 3%, embora a alíquota conforme o modelo de impostos e cobranças sobre vendas seja de 6,25%.


![Cálculo de imposto](/files/tax-calculation.png)


### 2.3 Modelo de imposto de item para cada item


Você também pode selecionar manualmente um modelo de imposto de item diferente para cada item em uma transação:


![Selecionar modelo de imposto de item](/files/select-item-tax-template.png)


### 2.4 Imposto sobre itens em um grupo de itens


Você pode atribuir o Modelo de Imposto sobre Itens a um Grupo de Itens modificando a tabela Imposto sobre Itens na seção Imposto sobre Itens no documento Grupo de Itens.


![Modelo de imposto de item no grupo de itens](/files/item-tax-template-in-item-group.png)


O modelo de imposto de item aplicado a um grupo de itens será aplicado a todos os itens desse grupo, a menos que um item individual no grupo de itens tenha seu próprio modelo de imposto de item atribuído a ele.


### 2.5 Validade dos impostos sobre itens


![Imposto sobre item no grupo de itens](/files/item-tax-in-item.png)


Você também pode atribuir validade a modelos fiscais conforme mostrado na imagem acima.


* Com base na data de lançamento da transação, um modelo de imposto válido será obtido automaticamente.
* Se houver mais de um modelo de imposto válido, o primeiro modelo de imposto válido da tabela Imposto sobre itens será obtido.
* Caso não existam modelos de impostos válidos, o primeiro modelo de imposto sem data 'Válido desde' na tabela Imposto sobre itens será obtido.


> Observação: ao adicionar itens na fatura de compra, a primeira preferência será dada à 'Data da fatura do fornecedor' em vez de 'Data de lançamento' para obter um modelo de imposto de item válido.


### 2.6 Alguns pontos a serem observados


* Se você definir a categoria de imposto como vazia, o modelo de imposto de item padrão será aplicado aos itens nas transações.
* Você pode aplicar diferentes modelos de impostos de itens para diferentes categorias de impostos.
* Para que um modelo de imposto de item substitua os impostos, deve haver uma linha na tabela Impostos e Encargos com o mesmo chefe de conta fiscal com uma taxa de imposto padrão.
* Se desejar aplicar impostos apenas aos itens com um modelo de imposto de item, você poderá definir a taxa de imposto padrão como 0.


### 3. Tópicos Relacionados


1. [Regra tributária](/docs/pt/accounts/tax-rule)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
3. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



