# Integração Exotel



Esta integração permite integrar o Exotel na sua conta ERPNext. Leads e seus números de telefone capturados via Exotel podem ser salvos diretamente no seu ERPNext.


## 1. Recursos


* Rastreie as chamadas recebidas em sua conta ERPNext.
* Mostra um pop-up de informações de leads/clientes existentes para os funcionários quando uma chamada é recebida.


## 2. Como configurar


### 2.1 Configure sua conta Exotel


* Faça login em sua conta Exotel e acesse App Bazar.
* Crie um novo aplicativo para um novo fluxo.
* Configure o fluxo como desejar.
* Na sua API de conexão, em "Criar pop-up..." e cole o seguinte URL:
`https://<seu-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`


![Conectar miniaplicativo](/files/connect_applet.png)
![Seção pop-up de chamada](/files/create_popup_section.png)


> **Observação:** substitua `<your-site>` no URL pelo nome do seu site. Por exemplo, se o nome do site for **frappe.erpnext.com** então o URL será:
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`


* Depois disso, adicione um miniaplicativo Passthru em "Após o término da conversa da chamada" e cole o seguinte URL:
`https://<seu-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`


![Seção Após o término da conversa](/files/after_conversation_ends_section.png)


![Seção após o término da chamada](/files/passthru_end_call.png)


> **Observação:** certifique-se de marcar "Make Passthru Async".


* Da mesma forma, adicione um miniaplicativo Passthru na seção "Se ninguém responder..." e cole o seguinte URL:
`https://<seu-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`


![Seção sem resposta](/files/no_response.png)


![Seção após o término da chamada](/files/passthru_missed_call.png)


> **Observação:** certifique-se de marcar "Make Passthru Async".


* Salve o fluxo.
* Agora atribua este aplicativo recém-criado ao seu ExoPhone do qual você recebe suas chamadas comerciais.


### 2.2 Configuração no ERPNext


* No Awesome Bar, vá para 'Configurações do Exotel'.
* Defina seu "Exotel SID" e "Exotel Token". Você pode encontrar sua chave e token da API Exotel em seu [painel Exotel](https://my.exotel.com/apisettings/site#api-credentials).
* Acesse o meio de comunicação.
* Adicione seu ExoPhone e agende esse número. Com base nesta programação, os funcionários receberão o pop-up.



