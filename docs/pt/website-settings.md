# Configurações do site



As configurações relacionadas ao site, como página de destino e tema geral do site, podem ser
configurado aqui.


Para acessar as configurações do site, acesse:



> 
> Página inicial > Site > Configuração > Configurações do site
> 
> 
> 


## 1. Página inicial


Configure a página de destino padrão do seu site definindo a **página inicial**
campo para a rota dessa página. Você pode colocar qualquer rota aqui, incluindo padrão
rotas como `home`, `about`, `contact`, `login`, `all-products` e `blog`.


Você também pode definir uma [Página da Web](/docs/pt/website/web-page) como o
página de destino.


Se você quiser usar a [Página inicial](/docs/pt/website/homepage) do ERPNext,
você deve defini-lo como `home`.


![Configurações do site-Landing Page](/files/website-settings-landing-page.png)
*Configurações do site-Página inicial*


Você também pode definir o **Prefixo do título** aqui. Ele será anexado ao título do navegador
em cada página. Você pode colocar o nome da sua empresa aqui.


## 2. Tema do site


Crie um tema personalizado para o seu site e defina-o aqui. Aprender mais sobre
configurando o tema do site [aqui](/docs/pt/website/website-theme).


## 3. Marca


### 3.1 Logotipo da marca


Você pode definir o logotipo da marca do seu site nesta seção. Carregar a marca
Imagem primeiro e depois clique no botão "Definir banner a partir da imagem". Irá gerar um
Banner HTML com o logotipo enviado.


![Configurações do site-Imagem do banner](/files/website-settings-banner-image.png)
*Configurações do site – Imagem do banner*


### 3.2 Favicon


Você também pode definir o favicon do seu site nesta seção. Aparece no
lado esquerdo da guia do navegador.


![Configurações do site-Favicon](/files/website-settings-favicon.png)
*Configurações do site-Favicon*


Visualize seu site clicando em **Ver site** na barra de ação no canto superior direito.


![Site com marca e favicon](/files/website-brand-and-favicon.png)
*Site com marca e favicon*


## 4. Barra superior


Você pode personalizar os itens de menu na barra de navegação do seu site na **barra superior**
seção.


![Configuração do site-Barra superior](/files/website-settings-top-bar.png)
*Configuração do site-Barra superior*


![Itens da barra de navegação do site](/files/website-navbar-items.png)
*Itens da barra de navegação do site*


## 5. Bandeira


Você pode adicionar um banner persistente ao seu site, que será mostrado acima do
barra de navegação em todas as páginas da web. Você pode escrever qualquer marcação válida do Bootstrap 4 aqui.


![Configurações do site-Banner](/files/website-settings-banner.png)
*Configurações do site-Banner*


![Banner do site](/files/website-banner.png)
*Banner do site*


## 6. Rodapé


Você pode adicionar informações de endereço e links categorizados ao rodapé na seção
Seção **Rodapé**.


![Configurações do site-Endereço do rodapé](/files/website-settings-footer-address.png)
*Configurações do site – Endereço do rodapé*


![Configurações do site-Links de rodapé](/files/website-settings-footer-links.png)
*Configurações do site-Links de rodapé*


![Rodapé do site](/files/website-footer.png)
*Rodapé do site*


#### Configurando a seção "Powered by"


Você pode configurar a seção Powered by editando "Rodapé Powered By"


## 7. Integrações com o Google


### 7.1 Indexação do Google


#### Como configurar a indexação automatizada do Google


Para permitir que o ERPNext solicite aos rastreadores do Google a indexação de uma página web, você precisa autorizar o ERPNext a enviar uma solicitação sempre que o usuário solicitar os dados. A integração do Google Drive é configurada com as seguintes etapas:


* Crie credenciais do OAuth 2.0 nas [Configurações do Google](/docs/pt/erpnext_integration/google_settings)
* Ative a indexação nas configurações do site
* Agora clique em **Autorizar acesso à indexação da API** para autorizar o ERPNext a enviar uma solicitação de publicação.
* Uma vez autorizada, uma solicitação de indexação é enviada automaticamente na criação/atualização/lixeira de qualquer nova postagem de blog ou página da web criada pelo usuário.


![Google Integrations](/files/website-settings-integrations.png)
*Integrações com o Google*


### 7.2 Google Analytics


Você pode ativar o Google Analytics em seu site. Basta obter seu [Google Analytics
ID](https://support.google.com/analytics/answer/1008080?hl=en) do seu Google
Console e configure-o aqui.


Por padrão, o Google Analytics coletará o endereço IP completo dos visitantes do seu site.
Ao marcar "Google Analytics Anonimizar IP", o ERPNext instruirá o Google Analytics a
anonimizar o endereço IP antes que ele seja enviado aos servidores do Google. Você pode descobrir mais sobre
o efeito dessa configuração na [documentação do Google](https://support.google.com/analytics/answer/2763052).


## 8. Cabeçalho HTML


Você pode usar esta seção para definir metatags em todas as suas páginas da web. Um comum
caso de uso é adicionar tags de verificação de site do Google.


![Configurações do site-Cabeçalho](/files/website-settings-header.png)
*Configurações do site-Cabeçalho*


## 9. Robôs


Você pode definir regras de `robots.txt` nesta seção. Esta informação é usada por
rastreadores da Web para decidir quais páginas indexar e quais ignorar.


![Configurações do site-Robôs](/files/website-settings-robots-txt.png)
*Configurações do site-Robôs*



> 
> Saiba mais sobre `robots.txt` em [Moz-Robots.txt](https://moz.com/learn/seo/robotstxt)
> 
> 
> 


## 10. Redirecionamentos


Você pode definir um mapeamento de redirecionamentos de rota aqui. Os mapeamentos a seguir
a captura de tela garante que, se um usuário visitar `https://apple.erpnext.com/iphone`,
eles serão redirecionados para `https://apple.erpnext.com/products/iphone`.


ERPNext gerará uma resposta `301 Permanent Redirect` para essas rotas.


![Configurações do site-Redirecionamentos de rotas](/files/website-settings-route-redirects.png)
*Configurações do site-Redirecionamentos de rotas*



> 
> Se você estiver migrando seu site existente para um site baseado em ERPNext,
>  você pode mapear suas rotas antigas para novas aqui e esses redirecionamentos serão
>  escolhido pelo Google e ajudará você a manter suas classificações de SEO.
> 
> 
> 


## 11. Bate-papo


Você pode ativar o bate-papo para visitantes do site na seção Bate-papo. O
O widget de bate-papo será mostrado entre o horário **De** e o horário **Até**. Você também pode
defina **operadores de bate-papo** (usuários) que serão notificados quando um visitante enviar um
mensagem.



> 
> O bate-papo é um recurso experimental.
> 
> 
> 



