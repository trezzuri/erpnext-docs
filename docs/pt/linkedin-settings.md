# Configurações do LinkedIn




> Observação: esta integração está obsoleta e será removida na v15. 
> 
> 

Configurações relacionadas ao LinkedIn, como OAuth, podem ser definidas aqui. O ERPNext precisa de acesso à API através da qual a postagem é compartilhada e obtida usando o protocolo de autenticação OAuth 2.0.

## 1. Como configurar o aplicativo de desenvolvedor do LinkedIn

Você deve ter o aplicativo de desenvolvedor do LinkedIn para sua empresa. ERPNext interage com este aplicativo para compartilhar a postagem.

### 1.1 Criar aplicativo de desenvolvedor do LinkedIn

Criar aplicativo por link `https://www.linkedin.com/developers` preencha todos os dados e verifique. E esse aplicativo tem os seguintes produtos.

1. Compartilhe no LinkedIn
2. Faça login com o LinkedIn
3. Plataforma de desenvolvedor de marketing ![LinkedIn Developer App Product](/files/linkedin-dev-products.png)

### 1.2 Configurar URLs de redirecionamento:

1. Vá para seu LinkedIn Aplicativo para desenvolvedores e, em seguida, a guia **Auth**.
2. Na seção **Configurações do OAuth 2.0**, adicione **URLs de redirecionamento**: `https://{seusite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Clique em **Atualizar** para fazer alterações. ![URL de redirecionamento do LinkedIn](/files/linkedin-redirect-urls.png)

## 2. Como definir as configurações do LinkedIn

Para acessar as configurações do LinkedIn, vá para:


> Página inicial > CRM > Configurações > Configurações do LinkedIn
> 
> 

 ![Configurações do LinkedIn](/files/linkedin-settings.png)  




