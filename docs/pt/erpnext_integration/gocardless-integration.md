# Configurando o GoCardless



Para configurar o GoCardless, vá para `Explorar > Integrações > Configurações do GoCardless`


## Configurar GoCardless


Para habilitar GoCardless em sua conta ERPNext, você precisa configurar os seguintes parâmetros e token de acesso e opcionalmente (mas altamente recomendado), uma chave secreta de Webhooks.


Você pode configurar vários gateways de pagamento GoCardless, se necessário. A escolha da conta do gateway de pagamento determinará qual conta GoCardless será usada para o pagamento.


![Configurações GoCardless](/files/gocardless_account.png)


Ao habilitar o serviço, o sistema criará um registro de Gateway de Pagamento e um Cabeçalho de Conta no plano de conta com o tipo de conta como Banco.


![GoCardless COA](/files/gocardless_coa.png)


Também criará uma conta de gateway de pagamento. Você pode alterar a conta bancária padrão, se necessário, e criar um modelo para a solicitação de pagamento.


![Conta de gateway de pagamento](/files/payment_gateway_account_gocardless.png)


Depois de configurar a conta do gateway de pagamento, seu sistema poderá aceitar pagamentos on-line através do GoCardless.


## Fluxo de pagamentos SEPA


Quando um novo pagamento SEPA é iniciado, o cliente é solicitado a inserir seu IBAN (ou número de conta local) e a validar um mandato SEPA.


Após a validação do mandato, uma solicitação de pagamento é enviada à GoCardless e processada.


Se o cliente já possuir um mandato SEPA válido, quando em vez de enviar um pedido de pagamento ao cliente, o pedido de pagamento é enviado diretamente para GoCardless sem necessidade de o cliente o validar.
O cliente receberá apenas um e-mail de confirmação da GoCardless informando que o pagamento foi processado.


## Cancelamento obrigatório


Você pode configurar um Webhook no GoCardless para desativar automaticamente mandatos cancelados ou expirados no ERPNext.


O URL do endpoint do seu webhook deve ser:


`https://yoursite.com/api/method/erpnext.erpnext_integrations.doctype.gocardless_settings.webhooks`


Neste caso não se esqueça de configurar a sua Chave Secreta dos Webhooks nas configurações da sua conta GoCardless no ERPNext.


## Moedas de transação suportadas


`"EUR", "DKK", "GBP", "SEK"`

