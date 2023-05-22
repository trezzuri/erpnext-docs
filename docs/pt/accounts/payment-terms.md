# Condições de pagamento


**Um prazo de pagamento ajuda a definir um cronograma de acordo com o qual os pagamentos serão feitos.**


Um Termo de Pagamento define um plano de pagamento específico. Por exemplo, pagamento de 50% no frete e 50% na entrega do item. Você pode salvar as condições de pagamento do seu negócio no SOMA e incluí-las em todos os documentos do ciclo de compra/venda. O SOMA fará todos os lançamentos do Razão de acordo.


No SOMA, o formulário Condições de Pagamento define apenas as porcentagens das parcelas. O cronograma de pagamento real pode ser facilmente aplicado usando o modelo de condições de pagamento.


Você pode usar os Termos de Pagamento nos seguintes documentos:


* Fatura de venda
* Fatura de compra
* Pedido de venda
* Pedido de compra
* Cotação


Para acessar o Termo de Pagamento acesse:



> 
> Início > Contabilidade > Mestres Contábeis > Prazo de Pagamento
> 
> 
> 


![Termos de pagamento](/files/payment-terms.png)


## 1. Como criar uma condição de pagamento


1. Vá para a lista de Condições de pagamento e clique em Novo.
2. Digite um nome para a condição de pagamento (por exemplo: 50% pós-envio).
3. Insira a parte da fatura. Se você inserir 50, a parte será 50% do valor da fatura.
4. Selecione um tipo de data de vencimento.
5. Em Dias de crédito, insira o número de dias após os quais o valor restante deve ser pago.
6. Salvar.


Os campos são explicados da seguinte forma:


* **Nome da condição de pagamento:** o nome desta condição de pagamento.
* **Data de Vencimento Baseada em:** A base pela qual a data de vencimento da Condição de Pagamento deve ser calculada. Isso é calculado em X dias a partir da **data de postagem** da fatura/pedido. Existem três opções:
	+ **Dia(s) após a data da fatura**: A data de vencimento deve ser calculada em dias referentes à data de lançamento da fatura. Por exemplo, se 7 for inserido na data 20, a data de vencimento será 27.
	+ **Dia(s) após o final do mês da fatura**: A data de vencimento deve ser calculada em dias referentes ao último dia do mês em que a fatura foi criada. Por exemplo, se 7 for inserido no mês atual e o último dia do mês for 30, a data de vencimento será 7 do próximo mês.
	+ **Mês(es) após o final do mês da fatura**: A data de vencimento deve ser calculada em meses referentes ao último dia do mês em que a fatura foi criada. Por exemplo, se 3 for inserido em 20 de janeiro, a data de vencimento será em 20 de março.
* **Parcela da fatura:** a parte do valor total da fatura para a qual este Termo de Pagamento deve ser aplicado. O valor fornecido será considerado uma porcentagem, ou seja, 50 = 50% do total geral da fatura/pedidos
* **Dias de Crédito (opcional):** O número de dias ou meses de crédito permitido dependendo da opção escolhida no campo Data de Vencimento Baseada em. 0 significa nenhum crédito permitido.
* **Descrição:** (opcional) Uma breve descrição do Termo de Pagamento.


### 1.1 Configuração de desconto em pagamentos antecipados


Você pode configurar condições de pagamento com desconto de forma que, se o pagamento for feito dentro do período especificado, algum valor/porcentagem do valor da fatura será descontado. Os seguintes campos definem a configuração do desconto:


* **Tipo de desconto:** o padrão é Porcentagem. Você também pode alterá-lo para Valor.
* **Desconto:** em termos de porcentagem ou valor (por exemplo, 10% ou ₹ 5.000).
* **Validade do desconto com base em:** Este campo funciona de maneira semelhante à Data de vencimento com base no campo da seção anterior.
* **Validade do desconto:** o número de dias ou meses em que o desconto é válido em relação à data da fatura (por exemplo, 10 dias após a data da fatura).


![Condições de pagamento com desconto](/files/payment-terms-with-discount.png)


Agora você pode vincular as Condições de Pagamento a uma Fatura e, ao criar o pagamento contra essa fatura, o desconto será aplicado automaticamente.



> 
> **Observação**: Este desconto é aplicado apenas em uma Entrada de Pagamento feita a partir de uma fatura individual. Entradas de pagamento feitas de forma independente, onde as referências da fatura são buscadas, não terão nenhum desconto de pagamento antecipado aplicado.
> 
> 
> 


### 1.2 Condições de pagamento em documentos convertidos


Ao converter ou copiar documentos no ciclo de venda/compra, será copiada(s) a(s) Condição(ões) de Pagamento anexada(s). Ao criar um Pedido de Venda a partir de uma Cotação, a Data de Vencimento nas Condições de Pagamento será de acordo com a Cotação, isso precisa ser atualizado.


Para facilidade de uso, você também pode definir um modelo de condições de pagamento e simplesmente selecioná-lo novamente.


### 1.3 Adicionar condições de pagamento a documentos


Depois de compor o modelo de condições de pagamento, você pode usá-lo em transações de compra e venda. Com base no valor definido para Condições de Pagamento e valor da transação, será definido o cronograma de pagamento, com uma Data de Vencimento para cada placa de pagamento.


![Cronograma de pagamento](/files/payment-term-in-invoice.png)


Observação: a Agenda de pagamento pode ser exibida na Visualização de impressão usando o [Criador de formato de impressão< /a>.](/docs/pt/setting-up/print/print-format-builder)


### 2. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
