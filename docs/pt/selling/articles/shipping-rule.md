# Regra de envio



O mestre de regras de envio ajuda a definir uma regra com base em qual taxa de envio será aplicada em transações de vendas.


A maioria das empresas (principalmente varejo) cobra o frete com base no total da fatura. Se o valor da fatura estiver acima de determinado valor, os custos de envio aplicados serão menores. Se o valor da fatura for menor, os custos de envio aplicados serão um pouco maiores do que os custos de envio elevados aplicados a uma fatura de valor elevado. Você pode configurar a regra de envio para atender ao requisito de variação da taxa de envio com base no total líquido da transação de vendas.


Para configurar a regra de envio, acesse:


`Vendas > Configuração > Regra de envio` ou `Contas > Configuração > Regra de envio`


#### Condições das regras de envio


![Condições das regras de envio](/files/shipping-rule-conditions.png)


Consultando acima, você notará que as despesas de envio estão diminuindo à medida que o valor aumenta. Esta taxa de envio só será aplicada se o total da transação estiver dentro de uma das faixas acima.


#### Válido para países


Você pode definir taxas de envio válidas para todos os países ou especificar um país específico. Se países específicos forem mencionados, as Taxas de Envio serão aplicadas somente se o país do Cliente corresponder ao País mencionado na Regra de Envio.


![Regras de envio específicas do país](/files/country-specific-shipping-rules.gif)


#### Conta de envio


Se as despesas de envio forem aplicadas com base na Regra de Envio, mais valores como Conta de Envio e Centro de Custo também serão necessários para adicionar linha na tabela Impostos e Outros Encargos da transação. Portanto, esses detalhes também são rastreados na Regra de Envio.


![Conta de envio](/files/shipping-account.png)


#### Aplicativo de regra de envio


A seguir está um exemplo de como as despesas de envio são aplicadas automaticamente no pedido de vendas com base na regra de envio.


![Regra de envio no pedido de vendas](/files/shipping-rule-in-sales-order.gif)



