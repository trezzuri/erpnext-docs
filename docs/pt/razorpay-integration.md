# Integração RazorPay



Um gateway de pagamento é um provedor de serviços de aplicativos de comércio eletrônico que autoriza pagamentos com cartão de crédito para empresas eletrônicas, varejistas on-line, lojas físicas ou lojas físicas tradicionais.


Um gateway de pagamento facilita a transferência de informações entre um portal de pagamento (como um site, telefone celular ou serviço interativo de resposta de voz) e o processador front-end ou banco adquirente.


Para configurar o RazorPay,


`Explorar > Integrações > Configurações do RazorPay`


![Configurações do Razorpay](/files/razorpay-api.gif)


#### Configurar RazorPay


Para ativar o serviço de pagamento RazorPay, você precisa configurar parâmetros como API Key, API Secret


![Configurações do Razorpay](/files/razorpay_settings.png)


Ao habilitar o serviço, o sistema criará o registro do Gateway de Pagamento e o cabeçalho da conta no Plano de Conta com o tipo de conta como Banco.


![Razorpay COA](/files/razorpay_coa.png)


Além disso, criará uma entrada de conta no gateway de pagamento. A conta do gateway de pagamento é o hub de configuração, a partir dela você pode definir o cabeçalho da conta a partir do COA existente, modelo padrão do corpo do e-mail de solicitação de pagamento.


![Conta de gateway de pagamento](/files/payment_gateway_account_razorpay.png)


Depois de ativar o serviço e configurar a conta do gateway de pagamento, seu sistema poderá aceitar pagamentos on-line.


#### Moedas de transação compatíveis


RazorPay só funcionará para empresas que tenham `INR (rúpia indiana)` como moeda.



