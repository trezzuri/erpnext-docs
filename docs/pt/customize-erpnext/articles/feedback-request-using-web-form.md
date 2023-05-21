# Solicitação de feedback usando um formulário da Web


Na versão 11 do ERPNext, temos uma funcionalidade que permitia coletar um Feedback de um Cliente e usuários. No ERPNext, esse recurso agora é gerenciável usando ferramentas de personalização integradas, como:
* Tipo de documento personalizado
* Formulário Web
* Notificação

  
A seguir estão as etapas sobre como você deve configurar um recurso e começar a coletar feedback.
**Feedback como um DocType**
Crie um DocType personalizado para classificação nestas linhas
![](/files/oUDbd8e.png)
1. Nos primeiros campos, liste um DocTypes para o qual você deseja coletar uma classificação
2. No campo Nome do Documento, basta inserir o nome do primeiro campo "documento", para que se torne um [Link Dinâmico](https://docs.erpnext.com/docs/v14/user/manual/en/customize -erpnext/articles/dynamic-link-fields).
3. Insira um campo Classificação. Você também pode escolher outros dados ou selecionar o campo, se desejar obter classificação nessas linhas.

  
**Formulário da Web para formulário de feedback**
Depois que um DocType é criado, basta criar um formulário da Web buscando todos os campos padrão do tipo de documento Feedback.
![](/files/eWKqJ50.png)
**Crie uma Notificação**
Uma Notificação deve ser criada para enviar um link para um usuário, seguindo o qual ele enviará uma classificação. Você pode definir as condições para acionar um e-mail com base nos recursos padrão de [Notificação](https://erpnext.com/docs/user/manual/en/setting-up/notifications). A seguir está a ajuda sobre como definir uma mensagem e um link que levaria o usuário a um formulário da Web e permitiria o envio de uma classificação.

```
https://example.erpnext.com/feedback?new=1&document=Sales%20Order&document\_name={{doc.name}}
```
  
Onde:
* **example.erpnext.com** será a URL da sua conta ERPNext
* **feedback** será o nome do tipo de documento personalizado adicionado para coletar um feedback
* **document=Sales%20Order&** será um nome de DocType para o qual você deseja enviar uma notificação
* document\_name={{doc.name}} selecionará o nome do documento específico e atualizará no campo Nome do documento do formulário de feedback.

  
![](/files/UDBhIaK.png)
  
**Demonstração rápida:**
Aqui está a demonstração de como o link seria gerado, o Web Form seria preenchido e capturado no ERPNext.
![](/files/hEbdh6c.gif)