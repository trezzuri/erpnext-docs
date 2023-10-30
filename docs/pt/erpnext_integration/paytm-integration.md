# Integração com Paytm



**A integração do Paytm permite o processamento de transações com o provedor de gateway de pagamento Paytm.**


A integração Paytm facilita o processamento de pagamentos entre o portal de pagamentos Paytm e o ERPNext. Seus clientes podem optar por pagar com qualquer cartão de crédito/débito, UPI, Netbanking, Paytm Wallet.


Para configurar o Paytm, acesse:
> Integrações > Pagamentos > Configurações Paytm


## 1.Como obter suas credenciais da API Paytm?


1. Para ativar suas credenciais de API, você precisa fazer login em sua conta Paytm.
2. Em seguida, abra a opção Configurações do desenvolvedor na barra lateral.
3. Escolha a opção API Keys, ela deve exibir dois tipos de detalhes da API (Teste/Produção).
4. Os detalhes mencionados nos detalhes da API de produção são as credenciais que você deve usar nas configurações do Paytm.


![Configurações do Razorpay](/files/paytm_credentials.png)


## 2.Configurando o Paytm


Para ativar o serviço de pagamento Paytm, você precisa configurar todos os parâmetros obrigatórios que recebeu do Paytm. Se quiser usar o ambiente de teste da integração, você pode selecionar a opção de teste e usar as credenciais de desenvolvedor da API de teste fornecidas pelo Paytm.
![Configurações do Razorpay](/files/paytm_settings.png)


Ao habilitar a integração do Paytm no ERPNext, o sistema criará um registro do Gateway de Pagamento e um Chefe de Conta no Plano de Conta com o tipo de Conta como Banco, conforme visto na imagem a seguir.


![Stripe COA](/files/paytm_coa.png)


Além disso, criará uma entrada de conta no gateway de pagamento. A conta do gateway de pagamento é o centro de configuração onde você pode definir os chefes de conta e o modelo de e-mail de solicitação de pagamento padrão para solicitar pagamentos de clientes.


![Conta de gateway de pagamento](/files/payment_gateway_account_paytm.png)


Depois de configurar a conta do gateway de pagamento, você poderá aceitar pagamentos on-line via Paytm.


## 3.Moedas de transação de suporte


O Paytm só funcionará para empresas que tenham INR (rúpia indiana) como moeda da empresa.



