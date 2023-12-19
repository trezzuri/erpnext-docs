# Automatizando atribuições de problemas no ERPNext



Ferramentas modernas de automação de suporte melhoram comprovadamente o atendimento ao cliente. A automatização da atribuição de problemas de suporte garante que cada ticket de problema seja atribuído a um especialista do produto e que o cliente busque a resolução de suas dúvidas com mais rapidez. A regra de atribuição foi introduzida na v12 e veja como você pode automatizar os problemas da sua equipe de suporte.  
Primeiro, precisamos configurar uma conta de e-mail que anexe o email recebido. e-mails recebidos lá no DocType "Issue" do ERPNext.**1) Crie uma conta de e-mail:**Você precisa atualizar o domínio de e-mail e configurar seu suporte endereço de e-mail na conta de e-mail do ERPNext. Para saber mais sobre a configuração de e-mail, confira [este link](https://www.youtube.com/watch?v=ChsFbIuG06g&t=122s)  
 ![](/files/NPp14kS.png)  
**2) Anexar ao problema:**A caixa de seleção "Ativar entrada" deve ser selecionada para permitir que e-mails enviados neste endereço de e-mail sejam recebidos aqui. Precisamos capturá-los em um DocType, mencionado em "Anexa a". Nesse caso, queremos anexar todos os e-mails recebidos a Issue  
![](/files/STAm8ko.png)  
Esta é uma configuração única e você não precisará se preocupar com isso, a menos que precise alterar a senha desse endereço de e-mail por meio de terceiros aplicativos de festa. A lista de problemas será preenchida com os e-mails enviados aqui. Com o uso das Regras de Atribuição, podemos organizar a agenda da equipe de suporte ao cliente e garantir a resolução oportuna de todos os tickets de suporte abertos.  
**3) Definir um Regra de Atribuição:**  
![](/files/5q4HvOT.gif)  
 **4) Com base na regra definida na etapa (3), as atribuições serão feitas automaticamente**Essas são feitas como quando um problema é criado ou atualizado. Confira o GIF abaixo para ver a automação em ação quando o status de um ticket de problema é *atualizado*:  
![](/files/Qb0kAzo.gif)  
Observação: se necessário, a regra também pode ser desativada/atualizada:  
![](/files/PZbCDuu.png)  
Da mesma forma, você pode automatizar o processo de Vendas no ERPNext para atribuir leva para sua equipe de vendas e garante mais taxas de conversão!! Obrigado por ler este artigo! Se precisar de mais ajuda com isso, entre em contato com nossa comunidade [aqui](https://discuss.erpnext.com/)

