# Configurando o Stripe



Para configurar o Stripe,
`Explorar > Integrações > Configurações de faixa`


#### Faixa de configuração


Para ativar o serviço de pagamento Stripe, você precisa configurar parâmetros como Chave Publicável, Chave Secreta
![Configurações do Razorpay](/files/stripe_setting.png)


Ao habilitar o serviço, o sistema criará o registro do Gateway de Pagamento e o cabeçalho da conta no plano de conta com o tipo de conta como Banco.


![Stripe COA](/files/stripe_coa.png)


Também criará uma entrada de conta no gateway de pagamento. A conta do gateway de pagamento é o hub de configuração, a partir dela você pode definir o cabeçalho da conta a partir do COA existente, modelo padrão do corpo do e-mail de solicitação de pagamento.


![Conta de gateway de pagamento](/files/payment_gateway_account_stripe.png)


Depois de configurar a conta do gateway de pagamento, seu sistema poderá aceitar pagamentos on-line.


### Configurar planos de assinatura


Se precisar cobrar um valor recorrente em vez de uma cobrança única, você pode usar o sistema de assinatura do Stripe.


Depois de criar seus planos de faturamento no Stripe, adicione um ou vários novos "Planos de pagamento" no Frappe.


![Plano de pagamento](/files/payment_plan.png)


Depois, ao criar sua solicitação de pagamento, clique no campo de seleção "É uma assinatura" e adicione o sistema irá buscar os planos de assinatura correspondentes dentro da assinatura correspondente.


![Solicitação de pagamento](/files/subscription_payment_request.png)


O ERPNext criará automaticamente uma nova assinatura para este cliente no Stripe.


#### Moedas de transação compatíveis


`"AED", "ALL", "ANG", "ARS", "AUD", "AWG", "BBD", "BDT", "BIF", "BMD", "BND",
"BOB", "BRL", "BSD", "BWP", "BZD", "CAD", "CHF", "CLP", "CNY", "COP", "CRC", "CVE", "CZK ", "DJF",
"DKK", "DOP", "DZD", "EGP", "ETB", "EUR", "FJD", "FKP", "GBP", "GIP", "GMD", "GNF", "GTQ ", "GYD",
"HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "ISK", "JMD", "JPY", "KES", "KHR ", "KMF",
"KRW", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "MAD", "MDL", "MNT", "MOP", "MRO", "MUR ", "MVR",
"MWK", "MXN", "MYR", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "PAB", "PEN", "PGK", "PHP ", "PKR",
"PLN", "PYG", "QAR", "RUB", "SAR", "SBD", "SCR", "SEK", "SGD", "SHP", "SLL", "SOS", "STD ", "SVC",
"SZL", "THB", "TOP", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VND", "VUV ", "WST",
"XAF", "XOF", "XPF", "YER", "ZAR"`

