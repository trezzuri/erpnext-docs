# Configurando o Braintree



Para configurar o Braintree, vá para `Explorar > Integrações > Configurações do Braintree`


## Configurar Braintree


Para habilitar o Braintree em sua conta ERPNext, você precisa configurar os seguintes parâmetros:


* ID do comerciante
* Chave pública
* Chave privada


Você pode configurar vários gateways de pagamento Braintree, se necessário. A escolha da conta do gateway de pagamento determinará qual conta Braintree será usada para o pagamento.


![Configurações do Braintree](/files/braintree_account.png)


Ao habilitar o serviço, o sistema criará um registro de Gateway de Pagamento e um cabeçalho de conta no plano de conta com o tipo de conta como Banco.


![Braintree COA](/files/braintree_coa.png)


Também criará uma conta de gateway de pagamento. Você pode alterar a conta bancária padrão, se necessário, e criar um modelo para a solicitação de pagamento.


![Conta de gateway de pagamento](/files/payment_gateway_account_braintree.png)


Depois de configurar a conta do gateway de pagamento, seu sistema poderá aceitar pagamentos on-line através do Braintree.


## Moedas de transação compatíveis


`"AED","AMD","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN", "BIF","BMD","BND","BOB",
"BRL","BSD","BWP","BYN","BZD","CAD","CHF","CLP","CNY","COP","CRC","CVE","CZK ","DJF","DKK",
"DOP","DZD","EGP","ETB","EUR","FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF ","GTQ","GYD",
"HKD","HNL","HRK","HTG","HUF","IDR","ILS","INR","ISK","JMD","JPY","KES","KGS ","KHR","KMF",
"KRW","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","MAD","MDL","MKD","MNT ","MOP","MUR",
"MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","PAB","PEN ","PGK","PHP",
"PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SEK","SGD ","SHP","SLL",
"SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TOP","TRY","TTD","TWD","TZS ","UAH","UGX",
"USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XOF","XPF","YER","ZAR ","ZMK","ZWD"`

