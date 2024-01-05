# Condições de pagamento



**Um prazo de pagamento ajuda a definir um cronograma de acordo com o qual os pagamentos serão feitos.**


Uma condição de pagamento define uma parcela de pagamento específica. Por exemplo, pagamento de 50% no frete e 50% na entrega do item. Você pode salvar as condições de pagamento do seu negócio no ERPNext e incluí-las em todos os documentos do ciclo de vendas/compra. O ERPNext fará todos os lançamentos do Razão Geral de acordo.


No ERPNext, o formulário Condições de Pagamento define apenas porcentagens de parcela. O cronograma de pagamento real pode ser facilmente aplicado usando o modelo de condições de pagamento.


Você pode usar os Termos de Pagamento nos seguintes documentos:


* Fatura de vendas
* Fatura de compra
* Pedido de venda
* Pedido de compra
* Cotação


Para acessar o Termo de Pagamento acesse:
> Home > Contabilidade > Mestres Contábeis > Prazo de Pagamento


![Termos de pagamento](/files/payment-terms.png)


## 1. Como criar um Termo de Pagamento


1. Vá para a lista de Condições de Pagamento e clique em Novo.
2. Insira um nome para o Prazo de Pagamento (por exemplo: 50% pós-envio).
3. Insira a parte da fatura. Se você inserir 50, a parcela será de 50% do valor da fatura.
4. Selecione um tipo de data de vencimento.
5. Em Dias de Crédito, insira o número de dias após os quais o valor restante deverá ser pago.
6. Salvar.


Os campos são explicados da seguinte forma:


* **Nome da condição de pagamento:** o nome desta condição de pagamento.
* **Data de Vencimento Baseada em:** A base pela qual a data de vencimento do Prazo de Pagamento deve ser calculada. Isso é calculado X número de dias a partir da **data de lançamento** da fatura/pedido. Existem três opções:
	+ **Dia(s) após a data da fatura**: A data de vencimento deve ser calculada em dias relativos à data de lançamento da fatura. Por exemplo, se 7 for inserido na data 20, a data de vencimento será 27.
	+ **Dia(s) após o final do mês da fatura**: A data de vencimento deve ser calculada em dias relativos ao último dia do mês em que a fatura foi criada. Por exemplo, se 7 for inserido no mês atual e o último dia do mês for 30, a data de vencimento será o dia 7 do mês seguinte.
	+ **Mês(es) após o final do mês da fatura**: A data de vencimento deve ser calculada em meses relativos ao último dia do mês em que a fatura foi criada. Por exemplo, se 3 for inserido em 20 de janeiro, a data de vencimento será em 20 de março.
* **Parcela da Fatura:** A parcela do valor total da fatura à qual esta Condição de Pagamento deve ser aplicada. O valor fornecido será considerado como porcentagem, ou seja, 50 = 50% do total geral da fatura/pedidos
* **Dias de crédito (opcional):** O número de dias ou meses de crédito permitido dependendo da opção escolhida no campo Data de vencimento com base em. 0 significa que nenhum crédito é permitido.
* **Descrição:** (opcional) Uma breve descrição do Prazo de Pagamento.


### 1.1 Configurando desconto em pagamentos antecipados


Você pode configurar condições de pagamento com desconto de forma que, se o pagamento for feito dentro do período especificado, algum valor/porcentagem do valor da fatura será descontado. Os seguintes campos definem a configuração do desconto:


* **Tipo de desconto:** o padrão é porcentagem. Você também pode alterá-lo para Valor.
* **Desconto:** em termos de porcentagem ou valor (por exemplo, 10% ou ₹ 5.000).
* **Validade do desconto com base em:** Este campo funciona de forma semelhante ao campo Data de vencimento com base em na seção anterior.
* **Validade do desconto:** o número de dias ou meses em que o desconto é válido em relação à data da fatura (por exemplo, 10 dias após a data da fatura).


![Termos de pagamento com desconto](/files/payment-terms-with-discount.png)


Agora você pode vincular as Condições de Pagamento a uma Fatura e, ao criar o pagamento com base nessa fatura, o desconto será aplicado automaticamente.


> **Observação**: Este desconto só é aplicado em um Lançamento de Pagamento feito a partir de uma fatura individual. Lançamentos de Pagamento realizados de forma independente, onde são buscadas referências de faturas, não terão nenhum desconto por pagamento antecipado aplicado.


### 1.2 Condições de pagamento em documentos convertidos


Ao converter ou copiar documentos no ciclo de venda/compra, serão copiadas as Condições de Pagamento anexas. Ao criar um Pedido de Venda a partir de uma Cotação, a Data de Vencimento nas Condições de Pagamento estará de acordo com a Cotação, esta precisa ser atualizada.


Para facilitar o uso, você também pode definir um modelo de condições de pagamento e simplesmente selecioná-lo novamente.


### 1.3 Adicionando condições de pagamento aos documentos


Depois de criar o modelo de condições de pagamento, você poderá usá-lo em transações de vendas e compras. Com base no valor definido nas Condições de Pagamento e no valor da transação, será definido o cronograma de pagamento, com uma Data de Vencimento para cada placa de pagamento.


![Cronograma de pagamento](/files/payment-term-in-invoice.png)


Observação: o cronograma de pagamento pode ser mostrado na visualização de impressão usando o [Print Format Builder](/docs/pt/setting-up/print/print-format-builder).


### 2. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



