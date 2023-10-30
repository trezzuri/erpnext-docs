
# Setting up PayPal



A payment gateway is an e-commerce application service provider service that authorizes credit card payments for e-businesses, online retailers, bricks and clicks, or traditional brick and mortar.


A payment gateway facilitates the transfer of information between a payment portal (such as a website, mobile phone or interactive voice response service) and the Front End Processor or acquiring bank.


To setup PayPal ,
`Explore &gt; Integrations &gt; PayPal Settings`


#### Setup PayPal


To enable PayPal payment service, you need to configure parameters like API Username, API Password and Signature.


![PayPal Settings](/files/paypal_settings.png)


You also can set test payment environment, by settings `Use Sandbox`


On enabling service, the system will create Payment Gateway record and Account head in chart of accounts having account type as Bank.


![PayPal COA](/files/paypal_coa.png)


Also it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.


![Payment Gateway Account](/files/payment_gateway_account_paypal.png)


After enabling service and configuring Payment Gateway Account your system is able to accept online payments.


#### Supporting transaction currencies


AUD, BRL, CAD, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, TRY, USD


## Get PayPal credentials


#### Paypal Sanbox API Signature


* Login to paypal developer account, [PayPal Developer Account](https://developer.paypal.com/)
* From **Accounts** tab. create a new business account.
![Payment Request](/files/setup-sanbox-1.png)
* From this account profile you will get your sandbox api credentials
![Payment Request](/files/sanbox-credentials.png)




---


#### PayPal Account API Signature


* Login to PayPal Account and go to profile
![Payment Request](/files/api-step-1.png)
* From **My Selling Tools** go to **api Access**
![Payment Request](/files/api-step-2.png)
* On API Access Page, choose option 2 to generate API credentials
![Payment Request](/files/api-step-3.png)




