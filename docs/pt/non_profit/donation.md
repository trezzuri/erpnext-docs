# Doação



> Introduzido na versão 13


O tipo de documento Doação permite que você registre detalhes da doação do **Doador**.


## 1. Pré-requisitos


Antes de criar uma Doação, você precisa primeiro criar um [Doador](/docs/pt/non_profit/donor).


## 2. Como criar uma doação


Para criar uma nova Doação, acesse:


> Sem fins lucrativos > Doação > Novo


![Donation](/files/donation.png)


1. Selecione o doador. O nome e o e-mail do doador serão obtidos automaticamente.
2. Defina a data da doação.
3. Defina o valor e a forma de pagamento.
4. Salvar e enviar.


## 3. Recursos


### 3.1 Entrada de pagamento para doação


Ao enviar uma doação, você pode criar uma entrada de pagamento usando o botão **Criar entrada de pagamento**.


### 3.2 RazorPay para doações


Você pode configurar o RazorPay para capturar doações. Você pode encontrar instruções sobre como configurar o razorpay [aqui](/docs/pt/erpnext_integration/razorpay-integration).


Você pode seguir as etapas listadas abaixo para configurar o Razorpay para doações.


1. Configurar o RazorPay
2. Configurar o webhook do RazorPay


#### 3.2.1 Configurar RazorPay


Você pode encontrar instruções sobre como configurar o razorpay [aqui](/docs/pt/erpnext_integration/razorpay-integration).


Para capturar as doações, você precisa definir determinados padrões na seção Configurações de doação nas Configurações para organizações sem fins lucrativos


1. **Empresa Padrão**: Esta empresa será definida para as Doações criadas via webhook.
2. **Tipo de doador padrão**: esse tipo de doador será definido para o doador criado por meio do webhook de doação.
3. **Automatizar entradas de pagamento de doações**: você pode ativar esta opção para criar automaticamente entradas de pagamento para entradas de doações criadas via webhook.


Se *Automatizar entradas de pagamento de doações* estiver ativado, você terá que definir a conta de débito e a conta de pagamento de doações padrão para entrada de pagamento.


![Configurações de doação](/files/donation-settings.png)


#### 3.2.2 Configurando o webhook


Você pode configurar um webhook no painel do RazorPay em Configurações. Você pode ler mais sobre webhooks no RazorPay [aqui](https://razorpay.com/docs/webhooks/). Este webhook notificará seu site ERPNext sempre que uma nova doação for criada.


![Donation Webhook](/files/donation-webhook.png)


Você precisará dos seguintes detalhes para configurar o webhook.


1. **URL do Webhook**: A seguir está a URL do seu site ERPNext. Este é o endpoint que o RazorPay utilizará para notificar sobre quaisquer novas doações criadas.



```
https://<seu-site>/api/method/erpnext.non_profit.doctype.donation.donation.capture_razorpay_donations

```
2. **Segredo**: para proteger o endpoint da API, é sempre melhor gerar e definir um segredo do Webhook para o endpoint da API. Para fazer isso, em seu site ERPNext, você pode clicar no botão **Doações > Gerar segredo do webhook** nas configurações da organização sem fins lucrativos. Copie o segredo e cole-o no campo secreto no painel do RazorPay para configurar webhooks.
3. **Evento**: você deve ativar o evento `payment.captured`.
4. **Ativo**: marque esta opção para ativar o webhook.


Com isso, seu webhook é ativado.




