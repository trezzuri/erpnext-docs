# Associação



O tipo de documento Associação permite que você registre detalhes de associação do **Membro**.


Afiliação é um termo que se refere a qualquer organização que permite que as pessoas se inscrevam e muitas vezes exige que elas paguem uma taxa de adesão ou "assinatura".


## 1. Como criar uma assinatura


Para criar uma nova assinatura, acesse:


> Sem fins lucrativos > Associação > Novo


![Membership](/files/membership.png)


**Membro:** Membro é um campo de link que busca detalhes do membro no tipo de documento Membro.


**Status de associação:** Status de associação é um campo de seleção que contém Novo, Atual, Expirado, Pendente e Cancelado. O status Expirado será atualizado automaticamente quando o período de assinatura terminar.


**Seção Detalhes da data de associação:** esta seção contém informações relacionadas à data de início, data de término e data de início da associação.


**Detalhes de pagamento:** esta seção contém detalhes relacionados ao pagamento. Se a pessoa pagou pela assinatura, a caixa de seleção paga está marcada como marcada, caso contrário, desmarcada. O valor é obtido com base no tipo de assinatura.


## 2. Recursos


## 2.1 Gerar fatura


Se você marcou *Ativar faturamento* nas configurações de associação, verá um botão para gerar uma fatura de vendas no formulário de associação.


## 3. Pagamentos de assinatura usando RazorPay


Para pagamentos recorrentes de assinatura, você pode configurar uma assinatura razorpay para membros. Você pode encontrar instruções sobre como configurar o razorpay [aqui](/docs/pt/erpnext_integration/razorpay-integration)


> Observação: esse recurso está disponível apenas na versão 13 e superior.


Você pode seguir as etapas listadas abaixo para configurar uma assinatura Razorpay para assinaturas.


1. Configurar o RazorPay
2. Configurar detalhes de faturamento
3. Planos de configuração
4. Importar membros existentes
5. Configurar o Webhook do RazorPay
6. Configurar site


## 3.1 Configurações de associação


Você pode encontrar instruções sobre como configurar o razorpay [aqui](/docs/pt/erpnext_integration/razorpay-integration). Você pode configurar o faturamento nas configurações de associação no módulo para organizações sem fins lucrativos.


![Membership](/files/razorpay-enabled.png)


Marcar *Ativar RazorPay para assinaturas* mostrará mais opções de configuração.


* **Ciclo de cobrança**: é o período entre as cobranças. Você pode selecionar faturamento mensal ou anual.
* **Frequência de cobrança**: o número de ciclos de cobrança pelos quais o cliente deve ser cobrado. Por exemplo, se um cliente estiver comprando uma assinatura de 1 ano que deve ser cobrada mensalmente, esse valor deverá ser 12.


![Membership](/files/membership-settings.png)


Existem outras configurações disponíveis para faturamento.


* **Ativar faturamento**: marcar esta opção permitirá a criação de faturas para assinaturas usando o botão **Gerar fatura**.
* **Criação automática de fatura para formulários da Web**: se você tiver configurado formulários da Web personalizados, a ativação dessa opção criará automaticamente uma fatura de vendas quando o pagamento for autorizado.
* **Efetuar entrada de pagamento**: cria automaticamente entrada de pagamento para faturas de vendas criadas a partir da associação usando formulários da web.


Marcar *Ativar faturamento* permitirá que você configure a empresa e a conta de débito para suas faturas. Marcar **Efetuar entrada de pagamento** permitirá que você configure a conta de pagamento.


* **Enviar confirmação de adesão**: Se esta opção estiver ativada, você terá a opção de enviar uma confirmação sobre a adesão ao membro assim que a fatura for gerada.
* **Modelo de e-mail**: você pode configurar o modelo de e-mail para a confirmação e defini-lo aqui.


Se *Enviar confirmação de associação* estiver ativado, você poderá ativar *Enviar fatura com e-mail* para enviar a fatura junto com a associação. Você também pode configurar formatos de impressão para assinatura e fatura individualmente aqui.


## 3.2 Configurando planos


O tipo de associação corresponde ao seu plano RazorPay. Você pode ler mais sobre o plano de associação [aqui](/docs/pt/non_profit/membership_type)


![Membership](/files/plan.png)


Quando as opções de assinatura do Razorpay estiverem ativadas, você verá um campo **ID do plano**. É aqui que você pode adicionar o ID do plano do Razorpay.


> Observação: você deve adicionar todos os seus planos ativos e planos legados para obter um faturamento contínuo.


## 3.3 Importando Membros


Se você já tem membros, você pode importá-los usando a [Ferramenta de importação de dados](/docs/pt/setting-up/data/data-import). Aqui está um [tutorial em vídeo](https://www.youtube.com/watch?v=WlGD35DM5LI) do mesmo.


Você precisa importar membros com os seguintes campos.


1. **Nome do membro**: Nome completo do membro
2. **Tipo de adesão**: nome do plano ao qual está inscrito
3. **Endereço de e-mail**: ID de e-mail usado para transações Razorpay
4. **ID da assinatura**: ID da assinatura fornecido pelo RazorPay
5. **ID do cliente**: ID da assinatura fornecido pela RazorPay
6. **PAN de membro**: é opcional


> Observação: as assinaturas do RazorPay serão rastreadas apenas para os membros cujos dados existam na lista de membros.


Esta é a aparência de um membro no ERPNext.
![Membership](/files/member.png)


## 3.4 Configurando o webhook


Você pode configurar um webhook no painel do RazorPay nas configurações. Você pode ler mais sobre webhooks no RazorPay [aqui](https://razorpay.com/docs/webhooks/). Este webhook notificará seu site ERPNext sempre que uma nova assinatura for criada ou renovada.


![Membership](/files/razorpay-webhook.png)


Você precisará dos seguintes detalhes para configurar o webhook.


### 3.4.1 URL do webhook


A seguir está a URL do seu site ERPNext. Este é o endpoint que o RazorPay utilizará para notificar qualquer atividade relacionada à assinatura.



```
https://<seu-site>/api/method/erpnext.non_profit.doctype.membership.membership.trigger_razorpay_subscription

```

### 3.4.2 Eventos


Você deve ativar os eventos `subscription.activated` e `subscription.charged`.


### 3.4.3 Ativo


Marque isto para ativar o webhook


Com isso, seu webhook é ativado


## 3.5 Acionando nova assinatura em seu site


Você pode usar a [integração do lado do cliente RazorPay](https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/) para configurar o pagamento em seu site. Para fazer isso, primeiro você terá que criar um pedido de assinatura com RazorPay contra o qual poderá acionar um pagamento.


Para criar um pedido de assinatura, você pode usar o endpoint `create_member_subscription_order` no ERPNext.


Você pode enviar uma solicitação POST no seguinte endpoint



```
https://<seu-site>/api/method/erpnext.non_profit.doctype.member.member.create_member_subscription_order

```

Os argumentos a serem passados ​​são um dicionário com detalhes dos membros



```
{
    "plan_id": "Foundation Starter"//Nome do plano conforme detalhado em Tipo de associação
    "nome completo": "John Doe",
    "móvel": "7506000000",
    "e-mail": "jane@example.com",
    "pan": "Teste123"
}

```

Na criação bem-sucedida, um membro e um cliente serão criados automaticamente. O endpoint retornará um JSON da seguinte maneira.



```
{
    'subscription_details': {
        'plan_id': 'plan_EXwyxDYDCj3X4v',
        'customer_notify': 1
    },
    'subscrição_id': 'sub_EZycCvXFvqnC6p'
}

```

Você pode usar o `subscription_id` para acionar um pagamento.




