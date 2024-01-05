# Configurações do Google



Para ativar as integrações do Google, o ERPNext precisa de acesso à API através da qual os dados serão sincronizados, o que é obtido usando o protocolo de autenticação OAuth 2.0.


## Como configurar as configurações do Google


### Para Google Agenda, Contatos do Google, Google Drive e Indexação do Google


Para permitir a sincronização com qualquer um dos serviços mencionados acima, você precisa autorizar o ERPNext a obter dados do Google. A seguir está um exemplo de configuração da integração dos Contatos do Google


1. Crie um novo projeto no Google Cloud Platform e gere novas credenciais OAuth 2.0.
![](/files/google_contacts_project_creation.gif)


* Ative o acesso à API na biblioteca de API para a integração que você deseja integrar.


	+ Google Agenda: **API Calendário**
	+ Contatos do Google: **API People**
	+ Google Drive: **API Drive**
	+ Indexação do Google: **API de indexação**![](/files/api.gif)
* Em **API e serviços > Credenciais**, crie uma nova credencial e selecione **Criar ID de cliente OAuth**
* Selecione o tipo de aplicativo **Aplicativo Web**
* Adicione `https://{seusite}` às origens JavaScript autorizadas.
* Adicione `https://{yoursite}?cmd=frappe.integrations.doctype.google_calendar.google_calendar.google_callback` como um URI de redirecionamento autorizado para o Google Agenda.
* Adicione `https://{yoursite}/api/method/frappe.integrations.google_oauth.callback` como um URI de redirecionamento autorizado para o restante dos serviços.


![](/files/google_contacts_oauth.gif)
* Adicione seu ID e segredo do cliente nas configurações do Google em **Página inicial > Integrações > Serviços do Google > Configurações do Google**


### Para Google Maps


Para permitir a sincronização com o Google Maps, você precisa gerar uma chave de API, pois o Google Maps não precisa de acesso aos dados do Google.


1. Crie um novo projeto no Google Cloud Platform e gere uma nova chave de API.


* Ative o acesso à API na biblioteca de APIs da API Directions e adicione a chave da API nas configurações do Google em **Página inicial > Integrações > Serviços do Google > Configurações do Google**.
![](/files/api_key.gif)



