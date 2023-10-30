# Configurações de SMS



**Você pode assinar um provedor de SMS para enviar SMS para números de celular.**


Para integrar SMS no ERPNext, entre em contato com um provedor de gateway de SMS que forneça HTTP
API. Eles criarão uma conta para você e fornecerão um nome de usuário exclusivo
e senha.


Para acessar as configurações de SMS, acesse:
> Página inicial > Configurações > Configurações de SMS


Para definir as configurações de SMS no ERPNext, descubra sua API HTTP (um documento
que descreve o método de acesso à interface SMS de terceiros
formulários). Neste documento, você obterá uma URL que é usada para enviar o
SMS usando solicitação HTTP. Usando este URL, você pode definir as configurações de SMS em
ERPNext.


Exemplo de URL de gateway de SMS:



```
http://instant.smses.com/web2sms.php?username=<username>&password;=<password>&to;=<mobilenumber>&sender;=< ;senderid>&message;=<message>

```

![Configuração de SMS 2](/files/sms-settings2.jpg)


> Observação: para URL do SMS Gateway, inclua apenas a string antes de "?".


Exemplo:


`http://instant.smses.com/web2sms.php?username=abcd&password;=abcd&to;=9900XXXXXX&sender;
=DEMO&mensagem=ISSO+É+A+TESTE+SMS`
O URL acima enviará SMS da conta ABCD para o número de celular 9900XXXXXX com
ID do remetente como DEMO com uma mensagem de texto como "ESTE É UM SMS DE TESTE".


Observe que alguns parâmetros no URL são estáticos. Você obterá valores estáticos
do seu provedor de SMS, como nome de usuário, senha, etc. Esses valores estáticos devem
ser inserido na tabela Parâmetros estáticos.


![Configuração de SMS](/files/sms-settings1.png)


## Como configurar o ERPNext com Voip.ms


O primeiro passo é fazer login na conta voip.ms. Em seguida, vá para **Menu principal**, **API SOAP e REST/JSON**.
Ative a API, defina uma senha e coloque o endereço IP do seu servidor na lista de permissões.


Em seguida, vá para DIDs e ative o SMS no número de onde o SMS será enviado.


Defina o gateway de SMS como **https://voip.ms/api/v1/rest.php**


Definir parâmetro de mensagem como **message**


Parâmetro do receptor para **dst**


Crie quatro novos parâmetros estáticos:


* **api\_username** (nome de usuário da conta voip.ms
* **api\_password** (a senha da API configurada há alguns minutos)
* **método** define valor para **sendSMS**
* **did** (o DID de 10 dígitos que será usado para enviar o sms)


![Configuração Voip.MS](/files/voipms sms settings.jpg)


Em seguida, acesse o SMS Center para testar se tudo funciona corretamente.


### Tópicos Relacionados


1. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Notificações](/docs/pt/setting-up/notifications)



