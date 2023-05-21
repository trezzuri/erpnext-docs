# Pedido de Pagamento


**Uma Solicitação de Pagamento é usada para solicitar o pagamento de um Cliente para um Pedido de Venda ou Fatura.**


A solicitação de pagamento é enviada por e-mail e conterá um link para um gateway de pagamento, se configurado. Você pode criar uma solicitação de pagamento por meio de um Pedido de Venda ou uma Fatura de Venda. Uma Solicitação de Pagamento também pode ser configurada em uma Ordem de Compra ou uma Fatura de Compra para registros internos. Em seguida, os pagamentos podem ser processados ​​em massa usando uma [Ordem de pagamento](/docs/v13/user/manual/en/accounts/payment-order).


Para acessar a Solicitação de Pagamento acesse:



>
> Home > Contabilidade > Contas a Receber > Solicitação de Pagamento
>
>
>


## 1. Pré-requisitos


Antes de criar e usar a Solicitação de Pagamento, é aconselhável criar primeiro o seguinte:


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)
3. [Pedido de venda](/docs/v13/user/manual/en/selling/pedido de venda)
4. [Pedido de compra](/docs/v13/user/manual/en/buying/purchase-order)


## 2. Como criar uma Solicitação de Pagamento


Uma Solicitação de Pagamento não pode ser criada manualmente, ela é criada a partir de um Pedido de Venda/Compra ou Fatura.


### 2.1 Criação de Solicitação de Pagamento via Pedido de Venda


Em um pedido de venda, clique em Criar e, em seguida, clique em Pagamento para efetuar um pagamento antecipado. Para saber mais sobre pagamento antecipado, visite a página [Entrada de pagamento antecipado](/docs/v13/user/manual/en/accounts/advance-payment-entry).


![Solicitação de pagamento do pedido de venda](/files/payment-request-from-sales-order.png)


### 2.2 Criação de Solicitação de Pagamento via Nota Fiscal de Venda


Em uma fatura de venda, clique em Criar e, em seguida, clique em Pagamento para efetuar o pagamento contra a fatura.


![Solicitação de pagamento da fatura de vendas](/files/payment-request-from-sales-invoice.png)


Selecione a conta de gateway de pagamento apropriada na solicitação de pagamento para lançamento de contas. O chefe da conta especificado no gateway de pagamento será considerado para criar um lançamento contábil manual.



>
> Observação: a moeda da fatura/pedido e a moeda da 'conta do gateway de pagamento' devem ser as mesmas.
>
>
>


![Detalhes da solicitação de pagamento](/files/payment-request-details.png)


### 2.3 Notificando o Cliente


Você pode notificar o cliente da Solicitação de pagamento usando [Formato de impressão](/docs/v13/user/manual/en/setting-up/print/print-format). Se o e-mail de contato do cliente estiver definido, ele será obtido automaticamente. Caso contrário, você pode definir um endereço de e-mail na solicitação de pagamento.


![Detalhes da solicitação de pagamento](/files/payment-request-recipient-details.png)


### 2.4 Pedido de Correio


Aqui está um exemplo de e-mail de solicitação. A URL é gerada automaticamente se você configurou a respectiva integração de pagamento. Para saber mais sobre integrações, [visite esta página](/docs/v13/user/manual/en/erpnext_integration).


![Solicitação de pagamento](/files/pr-email.png)


### 2.5 Solicitação de Pagamento sem usar nenhum Gateway


Caso você não queira usar nenhuma integração ou gateway de pagamento e queira apenas enviar uma notificação, basta definir a Conta Bancária. Você terá que redigir a mensagem de acordo com os dados bancários. A parte pode então transferir o valor para a conta bancária mencionada.


## 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
2. [Condições de pagamento](/docs/v13/user/manual/en/accounts/payment-terms)
3. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
4. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)