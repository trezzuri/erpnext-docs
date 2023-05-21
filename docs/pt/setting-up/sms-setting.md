# Configurações de SMS


**Você pode se inscrever em um provedor de SMS para enviar SMS para números de celular.**


Para integrar o SMS no ERPNext, procure um Provedor de Gateway de SMS que forneça HTTP
API. Eles criarão uma conta para você e fornecerão um nome de usuário exclusivo
e senha.


Para acessar as configurações de SMS, vá para:



>
> Início > Configurações > Configurações de SMS
>
>
>


Para definir as configurações de SMS no ERPNext, descubra sua API HTTP (um documento
que descreve o método de acesso à interface SMS de terceiros
formulários). Neste documento, você obterá uma URL que é usada para enviar o
SMS usando solicitação HTTP. Usando este URL, você pode definir as configurações de SMS em
ERPNext.


URL de gateway de SMS de exemplo:



```
http://instant.smses.com/web2sms.php?username=<username>&password;=<password>&to;=<mobilenumber>&sender;=<senderid>&message;=<message>

```

![Configuração de SMS 2](/files/sms-settings2.jpg)



>
> Nota: Para o SMS Gateway URL, inclua apenas a string antes do "?".
>
>
>


Exemplo:



```
http://instant.smses.com/web2sms.php?username=abcd&password;=abcd&to;=9900XXXXXX&sender;
=DEMO&mensagem;=ESTE+É+A+TESTE+SMS

```

O URL acima enviará SMS da conta abcd para o número de celular 9900XXXXXX com
ID do remetente como DEMO com uma mensagem de texto como "ESTE É UM SMS DE TESTE".


Observe que alguns parâmetros na URL são estáticos. Você obterá valores estáticos
do seu provedor de SMS, como nome de usuário, senha, etc. Esses valores estáticos devem
devem ser inseridos na tabela Parâmetros estáticos.


![Configuração de SMS](/files/sms-settings1.png)


## Como configurar o ERPNext com Voip.ms


O primeiro passo é fazer login na conta voip.ms. Em seguida, vá para **Menu principal**, **API SOAP e REST/JSON**.
Ative a API, defina uma senha e coloque na lista de permissões o endereço IP do seu servidor.


Em seguida, vá para DIDs e habilite o SMS no número do qual o SMS será enviado.


Defina o SMS Gateway para **https://voip.ms/api/v1/rest.php**


Defina o parâmetro de mensagem como **mensagem**


Parâmetro do receptor para **dst**


Crie 4 novos parâmetros estáticos:


* **api\_username** (nome de usuário da conta voip.ms
* **api\_password** (a senha da API configurada há alguns minutos)
* **método** define valor para **enviarSMS**
* **did** (os 10 dígitos DID que serão usados ​​para enviar o sms)


![Voip.MS Setting](/files/voipms sms settings.jpg)


Em seguida, vá ao SMS Center para testar se tudo funciona corretamente.


### Tópicos relacionados


1. [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account)
2. [Notificações](/docs/v13/user/manual/en/configuração/notificações)