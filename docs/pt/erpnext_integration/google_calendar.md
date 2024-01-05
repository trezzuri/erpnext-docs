# Integração com o Google Agenda



ERPNext fornece uma integração com o Google Calendar para que todos os usuários sincronizem seus eventos do Google Calendar com o ERPNext.


## Como configurar a integração com o Google Agenda


Para permitir uma sincronização com o Google Calendar, você precisa autorizar o ERPNext a obter dados de eventos do calendário do Google. A integração com o Google Agenda é configurada com as seguintes etapas:


* Crie credenciais do OAuth 2.0 nas [Configurações do Google](/docs/pt/erpnext_integration/google_settings).
* Na lista do Google Agenda, clique em Novo. Insira o nome do calendário e o usuário para quem você deseja sincronizar e salve-o.
* Dependendo dos dados que você deseja sincronizar, você pode selecionar o seguinte
	+ Extrair do Google Calendar-Sincroniza todos os eventos do Google Calendar para o ERPNext.
	+ Push to Google Calendar-Sincroniza todos os eventos do ERPNext com o Google Calendar.
* Agora clique em **Autorizar acesso ao calendário** para autorizar o ERPNext a obter dados de eventos do calendário do Google.
* Uma vez autorizado, você pode sincronizar manualmente o evento do Google Calendar ou deixar o ERPNext sincronizar os Contatos do Google diariamente.


## Como usar a integração com o Google Agenda


### Criando um evento no ERPNext


* Assim que a integração com o Google Calendar for bem-sucedida, todos os eventos criados no ERPNext serão sincronizados se `Push to Google Calendar` estiver marcado.
* Criando um Evento no ERPNext
![](/files/erpnext-gc.gif)
* Excluindo um Evento no ERPNext
![](/files/gc-erpnext.gif)


### Sincronizando eventos do Google Agenda


* Assim que a integração do Google Agenda for bem-sucedida, todos os eventos no Google Agenda serão sincronizados se `Extrair do Google Agenda` estiver marcado.
* Sincronizando Eventos do Google Calendar para o ERPNext
![](/files/gc-sync.gif)



