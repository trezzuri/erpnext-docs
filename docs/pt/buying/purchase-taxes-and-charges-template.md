# Modelo de impostos e taxas de compra



**Impostos e Taxas de Compra podem ser aplicados a qualquer item que você comprar.**


O modelo de impostos e encargos de compra é semelhante ao modelo de impostos e encargos sobre vendas. Os modelos criados a partir deste formulário podem ser usados ​​em Pedidos de Compra e Faturas de Compra para registros internos.


Para contas fiscais que você deseja usar nos modelos fiscais, você deve definir o campo Tipo de conta como 'Imposto' para essa conta específica.


Para acessar o modelo de impostos e cobranças de compras, acesse:
> Página inicial > Compra > Configurações > Modelo de impostos e cobranças de compra


## 1. Como adicionar impostos/taxas de compra por meio de um modelo


Antes de criar um novo modelo, observe que já foram criados modelos para muitos dos impostos comumente usados.


1. Clique em Novo.
2. Insira um nome de título para o imposto.
3. Em tipo, defina qual será o imposto calculado e a alíquota do imposto. Existem cinco opções de tipo para as quais o imposto será calculado.
	1. Real: sobre o valor real de cada item.
	2. No total líquido: no total geral de todos os itens.
	3. Valor na linha anterior: serve para capitalizar as cobranças. Por exemplo, ceder cobranças sobre o valor ao qual o imposto já foi aplicado na linha anterior.
	4. Total da linha anterior: o mesmo que acima, mas aplicado ao total da fatura e não apenas ao valor de um item.
4. Selecione um chefe de conta que tenha taxas de imposto pré-definidas ou crie a sua própria.
5. Selecionar padrão aplicará este modelo por padrão para novas transações de compra.
6. Salvar.
![Impostos sobre compras](/files/purchase-taxes.png)


É interestadual: para a Índia. Ao selecionar um cliente na fatura de venda ou na nota de entrega, se os códigos GST do local de fornecimento e o endereço de entrega do cliente não corresponderem, o modelo com 'É interestadual' marcado será definido como modelo de impostos. Se o local de fornecimento e o endereço de entrega forem iguais, será aplicado o modelo de impostos padrão. Isto também se aplica à Nota Fiscal de Compra, na seleção do Fornecedor, os modelos são definidos dependendo dos endereços. Por exemplo, IGST.


## 2. Recursos


### 2.1 Tabela de impostos e taxas de compra


* **Considerar imposto ou cobrança para**: Total-para o total de todos os itens. Avaliação-para cada item. Avaliação e total – aplica-se imposto/taxa a ambos. [Confira este artigo](https://docs.erpnext.com/docs/pt/accounts/articles/difference-in-total-and-valuation-in-tax-and-charges) para saber a diferença.
* **Adicionar ou Deduzir:** se você deseja adicionar ou deduzir o imposto do item.
* **Linha de referência #**: Se o imposto for baseado no "Total da linha anterior", você pode selecionar o número da linha que será usada como base para este cálculo (o padrão é a linha anterior) .
![Tabela de impostos sobre compras](/files/purchase-taxes-table.png)
* **Este Imposto está incluído na Taxa Batica?**: Se marcado, o valor do imposto será considerado como já incluído na Taxa de Impressão/Valor de Impressão.
* **Chefe da conta:** o razão da conta sob a qual esse imposto será contabilizado. Se você selecionar IVA ou qualquer outro valor predefinido, a alíquota será preenchida automaticamente.
* **Centro de custo:** se o imposto/taxa for uma receita (como frete) ou despesa, ele precisará ser contabilizado em um centro de custo.
* **Descrição:** Descrição do imposto (que será impressa nas faturas/cotações).
* **Taxa:** a taxa de imposto, por exemplo: 14 = 14% de imposto.
* **Valor:** o valor do imposto a ser aplicado, por exemplo: 100,00 = ₹100 de imposto.


### 3. Tópicos Relacionados


1. [Pedido de compra](/docs/pt/buying/purchase-order)
2. [Configurações de compra](/docs/pt/buying/buying-settings)



