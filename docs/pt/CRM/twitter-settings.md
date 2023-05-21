# Configurações do Twitter


As configurações relacionadas ao Twitter, como OAuth, podem ser definidas aqui. O ERPNext precisa de acesso à API por meio da qual a postagem é compartilhada e obtida usando o protocolo de autenticação OAuth 2.0.


## 1. Como configurar o Twitter App


Você deve ter o Twitter App para sua empresa. ERPNext interage com este App para compartilhamento Tweet.


### 1.1 Criar aplicativo do desenvolvedor do Twitter


Crie o aplicativo pelo link `https://developer.twitter.com/` e verifique se o aplicativo tem permissão de acesso de **leitura e gravação**.
![Permissão do aplicativo do Twitter](/files/twitter-app-permission.png)


### 1.2. Configurar URL de retorno


1. Selecione seu aplicativo e vá para **Detalhes do aplicativo**.
2. Em seguida, vá para **Editar** e clique em **Editar detalhes**.
3. Adicione o URL do seu site em **Callback URLs** como:
`https://{seusite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback`
4. Clique em **Salvar** para fazer alterações.


![URL de retorno de chamada do aplicativo do Twitter](/files/twitter-callback-url.png)


## 2. Como definir as configurações do Twitter


Para acessar as configurações do Twitter, acesse:



>
> Início > CRM > Configurações > Configurações do Twitter
>
>
>


![Configurações do Twitter](/files/twitter-settings.png)


### 2.1 Chave de API e Segredo da Chave de API


Você obtém **API Key** e **API Key Secret** da sua conta de desenvolvedor do Twitter, acesse:



>
> `https://developer.twitter.com/` > Meus aplicativos > `{Seu aplicativo}` > Chaves e tokens
>
>
>


![Twitter Keys Tokens](/files/twitter-key-token.png)


Depois de salvar o documento preenchendo **API Key** e **API Key Secret**, ele será redirecionado para a página de login do Twitter, fornecendo credenciais válidas do Twitter e clicando em **Autorizar aplicativo**, o membro aprova a solicitação do seu aplicativo para acessar seus dados de membro e interagir com o Twitter.
![Twitter Authorize App](/files/twitter-authorize-app.png)