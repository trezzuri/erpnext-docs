# Configurando o login justo



fairlogin é um provedor oAuth compatível com GDPR da fairkom.eu.


Para configurar o fairlogin como um provedor oAuth, acesse:



> 
> Página inicial > Integrações > Chave de login social
> 
> 
> 


## Configurar keycloak


O fairlogin é baseado no keycloak, portanto os parâmetros podem ser semelhantes para qualquer configuração personalizada do oAuth que facilite o keycloak.


Lá você adiciona um novo cliente, seleciona open-id como protocolo do cliente e insere o endereço da sua instância do ERPnext como Raiz, Redirecionamento e URL Base.


Adicionar seu serviço ERNext como cliente está sendo [oferecido como um serviço pela fairkom](https://erp.fairkom.net/cloud/fairlogin-client).


![Configurações do keycloak ERPnext](/files/fairloginKeycloakERPnext.png)


## Configurar login justo


Para habilitar o fairlogin como uma opção de login do ERPNext, você precisa configurar os seguintes parâmetros:


* URL base https://id.fairkom.net/auth/realms/fairlogin/
* Autorizar URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/auth
* URL de redirecionamento/api/method/frappe.integrations.oauth2*logins.login*via\_fairlogin
* URL do token de acesso https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/token
* Ponto final da API https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/userinfo


![Configurações de fairlogin do ERPnext](/files/fairloginERPnextSettings.png)


Ao ativar o serviço, o sistema permitirá o login com qualquer conta fairlogin.


A função padrão de um novo usuário é Blogger (atualmente codificada).



