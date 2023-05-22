# Configurações do LinkedIn


Configurações relacionadas ao LinkedIn, como OAuth, podem ser definidas aqui. O SOMA precisa de acesso à API por meio da qual a postagem é compartilhada e obtida usando o protocolo de autenticação OAuth 2.0.


## 1. Como configurar o LinkedIn Developer App


Você deve ter o LinkedIn Developer App para sua empresa. O SOMA interage com este aplicativo para compartilhar a postagem.


### 1.1 Crie um aplicativo para desenvolvedores do LinkedIn


Criar aplicativo pelo link `https://www.linkedin.com/developers` preencha todos os detalhes e verifique. E esse aplicativo tem os seguintes produtos.


1. Compartilhe no LinkedIn
2. Faça login com o LinkedIn
3. Plataforma de desenvolvedor de marketing
![LinkedIn Developer App Product](/files/linkedin-dev-products.png)


### 1.2 Configurar URLs de redirecionamento:


1. Vá para o aplicativo LinkedIn Developers e selecione a guia **Auth**.
2. Na seção **Configurações do OAuth 2.0**, adicione **URLs de redirecionamento**:
`https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Clique em **Atualizar** para fazer alterações.
![LinkedIn Redirect URL](/files/linkedin-redirect-urls.png)


## 2. Como definir as configurações do LinkedIn


Para acessar as configurações do LinkedIn, acesse:



> 
> Página inicial > CRM > Configurações > Configurações do LinkedIn
> 
> 
> 


![LinkedIn Settings](/files/linkedin-settings.png)


### ID da empresa


Você obtém o ID da empresa no URL da sua empresa no LinkedIn.
![LinkedIn Company ID](/files/linkedin-company-id.png)


### Chave do consumidor e segredo do consumidor


Você obtém **Chave do consumidor** e **Segredo do consumidor** da sua conta de desenvolvedor do LinkedIn, acesse:



> 
> `https://www.linkedin.com/developers/` > Meus aplicativos > `{Seu aplicativo}` > Autenticação
> 
> 
> 


![LinkedIn Client](/files/linkedin-client.png)


Depois de salvar o documento preenchendo **ID da empresa**, **Chave do consumidor** e **Segredo do consumidor**, ele será redirecionado para a página de login do LinkedIn fornecendo credenciais válidas do LinkedIn e clicando em Permitir, o membro aprova a solicitação do seu aplicativo para acessar os dados do membro e interagir com o LinkedIn em seu nome.
![Autorizar LinkedIn](/files/authorize-linkedin.jpg)

