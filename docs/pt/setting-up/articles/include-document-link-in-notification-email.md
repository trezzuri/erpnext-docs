# Incluir link do documento no e-mail de notificação


Ao enviar uma notificação por e-mail no ERPNext, muitas vezes, precisamos que o ID do documento faça parte da mensagem de e-mail como um link. Por exemplo, se definimos um lembrete (notificação) para cada nova Solicitação de Material, desejamos que o link da nova Solicitação de Material também seja enviado por e-mail para nós. Para configurá-lo, siga os passos abaixo:
1) Vá para a lista de notificações, clique em Novo.
2) Crie uma nova Notificação para qualquer DocType. Nesse caso, tomamos como exemplo o envio de uma notificação por e-mail na criação de cada nova solicitação de material, conforme mostrado abaixo.
![](/files/6WPgqY6.png)
  
3) Para enviar o ID do documento do registro associado como um link, copie o trecho abaixo na mensagem de e-mail:**<a href="{{frappe.utils.get\_url\_to\_form(doc.doctype, doc .name)}}">{{doc.name}}</a>**
![](/files/vHK6tDW.png)
4) Agora, ao criar uma nova Solicitação de Material, o seguinte e-mail será recebido devido à Notificação definida acima.
![](/files/3WOeTEv.png)
Ao clicar no link, você será direcionado para a nova Solicitação de Material.
![](/files/4hB36zh.png)