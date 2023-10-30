# Modelo de impostos e taxas sobre vendas



**Impostos e taxas sobre vendas podem ser aplicados a qualquer item que você vende.**


Os modelos criados a partir deste formulário podem ser usados ​​em Pedidos de Vendas e Faturas de Vendas.


Para contas fiscais que deseja usar nos modelos fiscais, você deve definir o campo Tipo de conta como 'Imposto' para essa conta específica. A forma como o ERPNext configura os impostos é através de modelos. Outros tipos de cobranças que
podem ser aplicados às suas faturas (como frete, seguro etc.) e também podem ser configurados como impostos.


Para saber mais sobre como configurar impostos, visite [esta página](/docs/pt/setting-up/setting-up-taxes).


Para acessar o modelo de impostos e cobranças sobre vendas, acesse:



> 
> Página inicial > Vendas > Configurações > Modelo de impostos e cobranças sobre vendas
> 
> 
> 


Para saber mais sobre como configurar impostos, visite [esta página](/docs/pt/setting-up/setting-up-taxes)


## 1. Como adicionar impostos/taxas sobre vendas por meio de um modelo


Antes de criar um novo modelo, observe que já foram criados modelos para muitos dos impostos comumente usados.


1. Vá para a lista de modelos de impostos e cobranças sobre vendas e clique em Novo.
2. Insira um nome de título para o imposto.
3. Em tipo, defina qual será o imposto calculado e a alíquota do imposto. Existem cinco opções de tipo para as quais o imposto será calculado.
	1. Real: você pode inserir diretamente o valor da despesa.
	2. Total Líquido: No total líquido de todos os itens.
	3. Valor na linha anterior: serve para capitalizar as cobranças. Por exemplo, ceder cobranças sobre o valor ao qual o imposto já foi aplicado na linha anterior.
	4. Total da linha anterior: o mesmo que acima, mas aplicado ao total da fatura e não apenas ao valor de um item.
	5. Na quantidade do item: o imposto será calculado como Taxa de imposto \* Quantidade do item. Por exemplo, se a Taxa de Imposto for 2% e o número de Itens for 1, a Taxa de Imposto será 4, se o número de Itens for 5, a Taxa de Imposto será 10 e assim por diante.
4. Selecione um chefe de conta que tenha taxas de imposto pré-definidas ou crie a sua própria.
5. Selecionar padrão aplicará este modelo por padrão para novas transações de vendas.
6. Salvar.
![Impostos sobre vendas](/files/sales-taxes.png)


**É interestadual**: Para a Índia. Ao selecionar um cliente na fatura de venda ou na nota de entrega, se os códigos GST do local de fornecimento e o endereço de entrega do cliente não corresponderem, o modelo com 'É interestadual' marcado será definido como modelo de impostos. Se o local de fornecimento e o endereço de entrega forem iguais, será aplicado o modelo de impostos padrão. Isto também se aplica à Nota Fiscal de Compra, na seleção do Fornecedor, os modelos são definidos dependendo dos endereços. Por exemplo, IGST.


## 2. Recursos


### 2.1 Tabela de impostos e taxas sobre vendas


* **Considere Imposto ou Taxa para**: Total-para o total de todos os itens. Avaliação-para cada item. Avaliação e total – aplica-se imposto/taxa a ambos. [Confira este artigo](/docs/pt/accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges) para saber a diferença.
* **Linha de referência #**: Se o imposto for baseado no "Total da linha anterior", você pode selecionar o número da linha que será usada como base para este cálculo (o padrão é a linha anterior) .
![Tabela de impostos sobre vendas](/files/sales-taxes-table.png)
* **Este Imposto está incluído na Taxa Batica?**: Se marcado, o valor do imposto será considerado como já incluído na Taxa de Impressão/Valor de Impressão na tabela de Itens de uma transação. Isso é útil quando você deseja fornecer preços com impostos incluídos aos seus clientes. Para contabilizar as taxas que incluem impostos, o sistema calcula o valor líquido deduzindo o valor do imposto a ser aplicado e calcula o imposto sobre ele.
* **Chefe da conta:** o razão da conta sob a qual esse imposto será contabilizado. Se você selecionar IVA ou qualquer outro valor predefinido, a alíquota será preenchida automaticamente.
* **Centro de custo:** se o imposto/taxa for uma receita (como frete) ou despesa, ele precisará ser contabilizado em um centro de custo.
* **Descrição:** Descrição do imposto (que será impressa nas faturas/cotações).
* **Taxa:** a taxa de imposto, por exemplo: 14 = 14% de imposto.
* **Valor:** o valor do imposto a ser aplicado, por exemplo: 100,00 = ₹100 de imposto.


As taxas de imposto definidas no modelo serão a taxa de imposto padrão para todos os itens. Se houver itens que supostamente têm taxas diferentes, você pode substituir a taxa de imposto padrão definindo um modelo de imposto de item para o item ou grupo de itens.


### 3. Tópicos Relacionados


1. [Ordem de vendas](/docs/pt/selling/sales-order)
2. [Configurações de venda](/docs/pt/selling/selling-settings)



