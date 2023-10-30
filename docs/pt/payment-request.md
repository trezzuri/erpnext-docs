# Solicitação de pagamento



**Uma Solicitação de Pagamento é usada para solicitar o pagamento de um Cliente por um Pedido de Venda ou Fatura.**


A solicitação de pagamento é enviada por e-mail e conterá um link para um gateway de pagamento, se configurado. Você pode criar uma solicitação de pagamento por meio de um Pedido de Venda ou Fatura de Venda. Uma solicitação de pagamento também pode ser configurada em um pedido de compra ou fatura de compra para registros internos. Em seguida, os pagamentos podem ser processados ​​em massa usando uma [Ordem de pagamento](/docs/pt/accounts/payment-order).


Para acessar a Solicitação de Pagamento acesse:



> 
> Home > Contabilidade > Contas a Receber > Solicitação de Pagamento
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar a Solicitação de Pagamento, é aconselhável criar primeiro o seguinte:


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Ordem de vendas](/docs/pt/selling/sales-order)
4. [Pedido de compra](/docs/pt/buying/purchase-order)


## 2. Como criar uma solicitação de pagamento


Uma solicitação de pagamento não pode ser criada manualmente, ela é criada a partir de um pedido de venda/compra ou fatura.


### 2.1 Criando solicitação de pagamento via pedido de venda


Em um Pedido de Venda, clique em Criar e depois clique em Pagamento para efetuar um pagamento antecipado. Para saber mais sobre pagamento antecipado, visite a página [Entrada de pagamento antecipado](/docs/pt/accounts/advance-payment-entry).


![Solicitação de pagamento do pedido de vendas](/files/payment-request-from-sales-order.png)


### 2.2 Criando solicitação de pagamento via fatura de vendas


Em uma fatura de vendas, clique em Criar e depois clique em Pagamento para efetuar o pagamento da fatura.


![Solicitação de pagamento da fatura de vendas](/files/payment-request-from-sales-invoice.png)


Selecione a conta apropriada do gateway de pagamento na solicitação de pagamento para lançamento de contas. O titular da conta especificado no gateway de pagamento será considerado para criar um lançamento contábil manual.



> 
> Observação: a moeda da fatura/pedido e a moeda da 'Conta do gateway de pagamento' devem ser iguais.
> 
> 
> 


![Detalhes da solicitação de pagamento](/files/payment-request-details.png)


### 2.3 Notificando o cliente


Você pode notificar o cliente sobre a solicitação de pagamento usando o [Formato de impressão](/docs/pt/setting-up/print/print-format). Se o e-mail de contato do cliente estiver definido, ele será obtido automaticamente. Caso contrário, você pode definir um endereço de e-mail na Solicitação de Pagamento.


![Detalhes da solicitação de pagamento](/files/payment-request-recipient-details.png)


### 2.4 Solicitar e-mail


Aqui está um exemplo de e-mail de solicitação. O URL é gerado automaticamente se você configurou a respectiva integração de pagamento. Para saber mais sobre integrações, [visite esta página](/docs/pt/erpnext_integration).


![Solicitação de pagamento](/files/pr-email.png)


### 2.5 Solicitação de pagamento sem usar nenhum gateway


Caso você não queira utilizar nenhuma integração ou gateway de pagamento e queira apenas enviar uma notificação, basta configurar a Conta Bancária. Você terá que redigir a mensagem de acordo com os dados bancários. A parte pode então transferir o valor para a conta bancária mencionada.


## 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
2. [Condições de pagamento](/docs/pt/accounts/payment-terms)
3. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
4. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



