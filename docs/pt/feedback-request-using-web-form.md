# Solicitação de feedback usando um formulário da web



No ERPNext versão 11, temos uma funcionalidade que permite coletar Feedback de um Cliente e usuários. No ERPNext, esse recurso agora pode ser gerenciado usando ferramentas de personalização integradas como:  
* Custom DocType
* Web Form
* Notificação

  
A seguir estão as etapas sobre como você deve configurar um recurso e começar a coletar feedback.  
**Feedback como um DocType**  
Crie um DocType personalizado para classificação nessas linhas   
![](/files/oUDbd8e.png)  
1. Nos primeiros campos, liste um DocTypes para o qual você deseja coletar uma classificação
2. No campo Nome do Documento, basta inserir o nome do primeiro campo "documento", para que ele se torne um  [Campo Link Dinâmico](https://docs.erpnext.com/docs/pt/customize-erpnext/articles/dynamic-link-fields).
3. Insira um campo de Classificação. Você também pode escolher outros dados ou selecionar um campo, se desejar avaliar essas linhas.

  
**Formulário Web para Formulário de Feedback**   
Depois que um DocType for criado, basta criar um Web Form buscando todos os campos padrão do Feedback doctype.   
![](/files/eWKqJ50.png)  
**Criar uma notificação**  
Uma notificação deve ser criada para enviar um link a um usuário, após o qual ele enviará uma classificação. Você pode definir as condições para acionar um e-mail com base nos recursos padrão de [Notificação](https://erpnext.com/docs/user/manual/en/setting-up/notifications). A seguir está a ajuda sobre como definir uma mensagem e um link que levaria o usuário a um formulário da Web e permitiria o envio de uma classificação.  

```
https://example.erpnext.com/feedback?new=1&document=Sales%20Order&document\_name={ {doc.name}}
```
  
Onde:  
* **example.erpnext.com** será o URL da sua conta ERPNext
* **feedback** será o nome do tipo de documento personalizado adicionado para coletar um feedback
* **document=Sales%20Order&** será o nome do DocType para o qual você deseja enviar uma notificação.
* document\_name=&lcub;&lcub;doc.name}} será coletado nome específico do documento e atualização no campo Nome do documento do formulário de feedback.

  
![](/files/UDBhIaK.png)   
  
**Demonstração rápida:**  
 Aqui está a demonstração de como o link seria gerado, o Formulário Web seria preenchido e capturado no ERPNext.  
![](/files/hEbdh6c.gif)

