# Termos de pagamento


**Um prazo de pagamento ajuda a definir um cronograma de acordo com o qual os pagamentos serão feitos.**


Um Termo de Pagamento define uma placa de pagamento específica. Por exemplo, pagamento de 50% no frete e 50% na entrega do item. Você pode salvar as condições de pagamento do seu negócio no ERPNext e incluí-las em todos os documentos do ciclo de compra/venda. O ERPNext fará todos os lançamentos do Razão de acordo.


No ERPNext, o formulário Condições de Pagamento define apenas os percentuais das parcelas. O cronograma de pagamento real pode ser facilmente aplicado usando o Modelo de condições de pagamento.


Você pode usar as Condições de Pagamento nos seguintes documentos:


* Nota Fiscal de Venda
* Nota fiscal de compra
* Pedido de venda
* Ordem de Compra
* Cotação


Para acessar o Termo de Pagamento acesse:



>
> Home > Contabilidade > Mestres Contábeis > Prazo de Pagamento
>
>
>


![Condições de pagamento](/files/payment-terms.png)


## 1. Como criar uma Condição de Pagamento


1. Vá para a lista de Condições de Pagamento e clique em Novo.
2. Digite um nome para a Condição de Pagamento (ex: 50% pós-expedição).
3. Insira a parte da Fatura. Se você inserir 50, a parte será 50% do valor da fatura.
4. Selecione um tipo de data de vencimento.
5. Em Dias de Crédito, insira o número de dias após os quais o valor restante deve ser pago.
6. Salve.


Os campos são explicados da seguinte forma:


* **Nome do Termo de Pagamento:** O nome deste Termo de Pagamento.
* **Due Date Based On:** A base pela qual a data de vencimento do Prazo de Pagamento deve ser calculada. Isso é calculado em X dias a partir da **data de postagem** da fatura/pedido. Existem três opções:
+ **Dia(s) após a data da fatura**: A data de vencimento deve ser calculada em dias referentes à data de lançamento da fatura. Por exemplo, se 7 for inserido na data 20, a data de vencimento será 27.
+ **Dia(s) após o final do mês da fatura**: A data de vencimento deve ser calculada em dias referentes ao último dia do mês em que a fatura foi gerada. Por exemplo, se 7 for inserido no mês atual e o último dia do mês for 30, a data de vencimento será 7 do próximo mês.
+ **Mês após o final do mês da fatura**: A data de vencimento deve ser calculada em meses referentes ao último dia do mês em que a fatura foi gerada. Por exemplo, se 3 for inserido em 20 de janeiro, a data de vencimento será em 20 de março.
* **Parcela da Fatura:** A parte do valor total da fatura para a qual esta Condição de Pagamento deve ser aplicada. O valor fornecido será considerado uma porcentagem, ou seja, 50 = 50% do total geral da fatura/pedidos
* **Dias de Crédito (opcional):** O número de dias ou meses de crédito é permitido dependendo da opção escolhida no campo Due Date Based On. 0 significa nenhum crédito permitido.
* **Descrição:** (opcional) Uma breve descrição do Termo de Pagamento.


### 1.1 Configurando Desconto em Pagamentos Antecipados


Você pode configurar condições de pagamento com desconto de forma que, se o pagamento for feito dentro do período especificado, algum valor/porcentagem do valor da fatura será descontado. Os seguintes campos definem a configuração do desconto:


* **Tipo de desconto:** O padrão é Porcentagem. Você também pode alterá-lo para Valor.
* **Desconto:** Em termos de porcentagem ou valor (por exemplo, 10% ou ₹ 5.000).
* **Validade do desconto baseada em:** Este campo funciona de forma semelhante à Data de vencimento baseada em campo na seção anterior.
* **Validade do desconto:** O número de dias ou meses em que o desconto é válido em relação à data da fatura (por exemplo, 10 dias após a data da fatura).


![Condições de pagamento com desconto](/files/payment-terms-with-discount.png)


Agora você pode vincular as Condições de Pagamento a uma Fatura e, ao criar o pagamento contra essa fatura, o desconto será aplicado automaticamente.



>
> **Observação**: Este desconto é aplicado apenas em uma Entrada de Pagamento que é feita a partir de uma fatura individual. Os Lançamentos de Pagamento feitos de forma independente, onde são buscadas as referências da fatura, não terão nenhum desconto de pagamento antecipado aplicado.
>
>
>


### 1.2 Condições de pagamento em documentos convertidos


Ao converter ou copiar documentos no ciclo de compra/venda, será copiado(s) o(s) Termo(s) de Pagamento anexo(s). Ao criar um Pedido de Venda a partir de uma Cotação, a Data de Vencimento nas Condições de Pagamento será de acordo com a Cotação, esta precisa ser atualizada.


Para facilitar o uso, você também pode definir um modelo de condições de pagamento e simplesmente selecioná-lo novamente.


### 1.3 Adicionando Condições de Pagamento a Documentos


Depois de compor o modelo de condições de pagamento, você pode usá-los em transações de compra e venda. Com base no valor definido para Condições de Pagamento e valor da transação, será definido o cronograma de pagamento, com uma Data de Vencimento para cada placa de pagamento.


![Cronograma de pagamento](/files/payment-term-in-invoice.png)


Observação: a Agenda de pagamento pode ser exibida na Visualização de impressão usando o [Construtor de formato de impressão](/docs/v13/user/manual/en/setting-up/print/print-format-builder).


### 2. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)