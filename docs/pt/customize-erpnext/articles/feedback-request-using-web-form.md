# Solicitação de feedback usando um formulário da Web


No ERPNext versão 11, temos uma funcionalidade que permitia coletar um Feedback de um Cliente e usuários. No ERPNext, esse recurso agora pode ser gerenciado usando ferramentas de personalização integradas, como:  
* Custom DocType
* Web Form
* Notificação

  
A seguir estão as etapas sobre como você deve configurar um recurso e começar a coletar feedback.  
**Feedback como um DocType**  
Crie um DocType personalizado para classificação nestas linhas   
![](/files/oUDbd8e.png)  
1. Nos primeiros campos, liste um DocTypes para o qual você deseja coletar uma classificação
2. No campo Nome do documento, basta digitar o nome do primeiro campo "documento", para que se torne um  [Campo de link dinâmico](https://docs.erpnext.com/docs/pt/customize-erpnext/articles/dynamic-link-fields).
3. Insira um campo de avaliação. Você também pode escolher outros dados ou selecionar um campo, se desejar avaliar essas linhas.

  
**Formulário da Web para formulário de feedback**   
Depois que um DocType é criado, basta criar um formulário da Web buscando todos os campos padrão do tipo de documento Feedback.   
![](/files/eWKqJ50.png)  
**Criar uma notificação< /strong>**  
Deve ser criada uma notificação para enviar um link para um usuário após o qual ele enviará uma classificação. Você pode definir as condições para acionar um e-mail com base nos recursos padrão de [Notificação](https://erpnext.com/docs/user/manual/en/setting-up/notifications). A seguir está a ajuda sobre como definir uma mensagem e um link que leve o usuário a um formulário da Web e permita o envio de uma classificação.  

```
https://example.erpnext.com/feedback?new=1&document=Sales%20Order&document\_name={ {doc.name}}
```
  
Onde:  
* **example.erpnext.com** será a URL da sua conta ERPNext
* **feedback** será o nome do tipo de documento personalizado adicionado para coletar um feedback
* **document=Sales%20Order&** será um nome de DocType para o qual você deseja enviar uma notificação
* document\_name={{doc.name}} será coletado nome do documento específico e atualização no campo Nome do documento do formulário de comentários.

  
![](/files/UDBhIaK.png)   
  
**Demonstração rápida:**  
 Aqui está a demonstração de como o link seria gerado, o Web Form seria preenchido e capturado no ERPNext.  
![](/files/hEbdh6c.gif)