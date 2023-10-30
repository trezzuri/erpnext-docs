# Configurações do Twitter




> Observação: esta integração não funciona mais devido a alterações na API do Twitter. Isso foi removido do ERPNext a partir da v15.
> 
> 

Configurações relacionadas ao Twitter, como OAuth, podem ser configuradas aqui. O ERPNext precisa de acesso à API através da qual a postagem é compartilhada e obtida usando o protocolo de autenticação OAuth 2.0.

## 1. Como configurar o aplicativo do Twitter

Você deve ter o aplicativo do Twitter para sua empresa. ERPNext interage com este aplicativo para compartilhar Tweet.

### 1.1 Criar aplicativo de desenvolvedor do Twitter

Criar aplicativo por link `https://developer.twitter.com/` e verifique se o aplicativo tem permissão de acesso de **leitura e gravação**. ![Permissão do aplicativo Twitter](/files/twitter-app-permission.png)  
 

### 1.2. Configurar URL de retorno de chamada

1. Selecione seu aplicativo e vá para **Detalhes do aplicativo**.
2. Em seguida, vá para **Editar** e clique em **Editar detalhes**.
3. Adicione o URL do seu site em **URLs de retorno de chamada** como: `https://{seusite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback`
4. Clique em **Salvar** para fazer alterações.

![URL de retorno de chamada do aplicativo do Twitter](/files/twitter-callback-url.png)  


## 2. Como definir as configurações do Twitter

Para acessar as configurações do Twitter, vá para:


> Página inicial > CRM > Configurações > Configurações do Twitter
> 
> 

 ![Configurações do Twitter](/files/twitter-settings.png)  
### 2.1 Chave de API e segredo de chave de API

Você obtém a **chave de API** e o **segredo de chave de API** da sua conta de desenvolvedor do Twitter, vá para:


> `https://developer.twitter.com/` > Meus aplicativos > `{Seu aplicativo}` > Chaves e tokens
> 
> 

![Twitter Keys Tokens](/files/twitter-key-token.png)  


Depois de salvar o documento preenchendo **chave de API** e **segredo de chave de API**, ele será redirecionado para a página de login do Twitter ao fornecer credenciais válidas do Twitter e clicar em **Autorizar aplicativo**, o membro aprova a solicitação do seu aplicativo para acessar os dados do membro e interagir com o Twitter. ![Twitter Authorize App](/files/twitter-authorize-app.png)  






