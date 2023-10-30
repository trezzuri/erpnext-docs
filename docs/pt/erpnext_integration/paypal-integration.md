# Configurando o PayPal



Um gateway de pagamento é um provedor de serviços de aplicativos de comércio eletrônico que autoriza pagamentos com cartão de crédito para empresas eletrônicas, varejistas on-line, lojas físicas ou lojas físicas tradicionais.


Um gateway de pagamento facilita a transferência de informações entre um portal de pagamento (como um site, telefone celular ou serviço interativo de resposta de voz) e o processador front-end ou banco adquirente.


Para configurar o PayPal,
`Explorar > Integrações > Configurações do PayPal`


#### Configurar PayPal


Para ativar o serviço de pagamento PayPal, você precisa configurar parâmetros como nome de usuário da API, senha da API e assinatura.


![Configurações do PayPal](/files/paypal_settings.png)


Você também pode definir um ambiente de pagamento de teste, por meio das configurações `Usar Sandbox`


Ao habilitar o serviço, o sistema criará o registro do Gateway de Pagamento e o cabeçalho da conta no plano de contas tendo o tipo de conta como Banco.


![COA do PayPal](/files/paypal_coa.png)


Também criará uma entrada de conta no gateway de pagamento. A conta do gateway de pagamento é o hub de configuração, a partir dela você pode definir o cabeçalho da conta a partir do COA existente, modelo padrão do corpo do e-mail de solicitação de pagamento.


![Conta de gateway de pagamento](/files/payment_gateway_account_paypal.png)


Depois de ativar o serviço e configurar a conta do gateway de pagamento, seu sistema poderá aceitar pagamentos on-line.


#### Moedas de transação compatíveis


AUD, BRL, CAD, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, TRY , USD


## Obter credenciais do PayPal


#### Assinatura da API Paypal Sanbox


* Faça login na conta de desenvolvedor do PayPal, [Conta de desenvolvedor do PayPal](https://developer.paypal.com/)
* Na guia **Contas**. Criar uma nova conta de negócios.
![Solicitação de pagamento](/files/setup-sanbox-1.png)
* A partir deste perfil de conta você obterá suas credenciais da API sandbox
![Solicitação de pagamento](/files/sanbox-credentials.png)



#### Assinatura da API da conta PayPal


* Faça login na conta do PayPal e vá para o perfil
![Solicitação de pagamento](/files/api-step-1.png)
* Em **Minhas ferramentas de vendas** vá para **Api Access**
![Solicitação de pagamento](/files/api-step-2.png)
* Na página de acesso à API, escolha a opção 2 para gerar credenciais de API
![Solicitação de pagamento](/files/api-step-3.png)



