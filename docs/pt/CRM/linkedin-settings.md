# Configurações do LinkedIn


As configurações relacionadas ao LinkedIn, como OAuth, podem ser configuradas aqui. O ERPNext precisa de acesso à API por meio da qual a postagem é compartilhada e obtida usando o protocolo de autenticação OAuth 2.0.


## 1. Como configurar o LinkedIn Developer App


Você deve ter o LinkedIn Developer App para sua empresa. O ERPNext interage com este App para compartilhamento do post.


### 1.1 Criar aplicativo de desenvolvedor do LinkedIn


Crie App pelo link `https://www.linkedin.com/developers` preencha todos os detalhes e verifique. E esse App tem os seguintes produtos.


1. Compartilhe no LinkedIn
2. Entre com o LinkedIn
3. Plataforma de desenvolvimento de marketing
![LinkedIn Developer App Product](/files/linkedin-dev-products.png)


### 1.2 Configurar URLs de redirecionamento:


1. Acesse o aplicativo LinkedIn Developers e a guia **Auth**.
2. Na seção **OAuth 2.0 settings**, adicione **Redirect URLs**:
`https://{seusite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Clique em **Atualizar** para fazer alterações.
![URL de redirecionamento do LinkedIn](/files/linkedin-redirect-urls.png)


## 2. Como definir as configurações do LinkedIn


Para acessar as configurações do LinkedIn, acesse:



>
> Início > CRM > Configurações > Configurações do LinkedIn
>
>
>


![Configurações do LinkedIn](/files/linkedin-settings.png)


### ID da empresa


Você obtém o ID da empresa no URL da sua empresa no LinkedIn.
![LinkedIn Company ID](/files/linkedin-company-id.png)


### Chave do Consumidor e Segredo do Consumidor


Você obtém **Consumer Key** e **Consumer Secret** da sua conta de desenvolvedor do LinkedIn, acesse:



>
> `https://www.linkedin.com/developers/` > Meus aplicativos > `{Seu aplicativo}` > Auth
>
>
>


![LinkedIn Client](/files/linkedin-client.png)


Depois de salvar o documento preenchendo **ID da empresa**, **Chave do consumidor** e **Segredo do consumidor**, ele será redirecionado para a página de login do LinkedIn fornecendo credenciais válidas do LinkedIn e clicando em Permitir, o membro aprova seu solicitação do aplicativo para acessar seus dados de membro e interagir com o LinkedIn em seu nome.
![Autorizar LinkedIn](/files/authorize-linkedin.jpg)