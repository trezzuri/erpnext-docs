# Incluir link do documento no e-mail de notificação



Ao enviar uma notificação por email no ERPNext, muitas vezes, precisamos que o ID do documento faça parte da mensagem de email como um link. Por exemplo, se definimos um lembrete (notificação) para cada nova Solicitação de Material, gostaríamos que o link da nova Solicitação de Material também fosse enviado por e-mail para nós. Para configurar isso, siga as etapas abaixo:  
1) Vá para a lista de notificações e clique em Novo.  
 2) Crie uma nova notificação para qualquer DocType. Neste caso, tomamos um exemplo de envio de uma notificação por e-mail na criação de cada nova solicitação de material, conforme mostrado abaixo.  
![](/files/6WPgqY6.png)  
  
3) Para enviar o ID do documento do registro associado como um link , copie o snippet abaixo na mensagem de e-mail:**[&lcub;&lcub;doc.name }}](&lcub;&lcub;frappe.utils.get_url_to_form(doc.doctype, doc.name)}})**  
![](/files/vHK6tDW.png)  
4) Agora, ao criar uma nova Solicitação de Material, o seguinte e-mail será recebido devido à Notificação definida acima.  
![](/files/3WOeTEv.png)  
Ao clicar no link, você será direcionado para a nova Solicitação de Material.  
![](/files/4hB36zh.png)   


