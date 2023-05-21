# Automatizando Atribuições de Problema no ERPNext


Ferramentas modernas de automação de suporte comprovadamente melhoram o atendimento ao cliente. A automatização da atribuição de problemas de suporte garante que cada tíquete de problema seja atribuído a um especialista em produto e que o cliente busque uma solução para suas dúvidas mais rapidamente. A regra de atribuição foi introduzida na v12 e aqui está como você pode automatizar os problemas de sua equipe de suporte.
Primeiro, precisamos configurar uma conta de e-mail que inclua os e-mails recebidos lá no DocType "Issue" do ERPNext.**1) Crie uma conta de e-mail:**Você precisa atualizar o domínio de e-mail e configurar seu endereço de e-mail de suporte no ERPNext Conta de e-mail. Para saber mais sobre a configuração de e-mail, confira [este link](https://www.youtube.com/watch?v=ChsFbIuG06g&t=122s)
![](/files/NPp14kS.png)
**2) Anexar ao problema:**A caixa de seleção "Ativar entrada" deve ser selecionada para permitir que os e-mails enviados neste endereço de e-mail sejam recebidos aqui. Precisamos capturá-los em um DocType, mencionado em "Anexa a". Nesse caso, queremos anexar todos os e-mails recebidos ao problema
![](/files/STAm8ko.png)
Esta é uma configuração única e você não terá que se preocupar com isso, a menos que precise alterar a senha desse endereço de e-mail por meio de aplicativos de terceiros. A lista de problemas será preenchida com os e-mails enviados aqui. Com o uso de Regras de Atribuição, podemos organizar a agenda da equipe de suporte ao cliente e garantir a resolução oportuna de todos os tickets de suporte abertos.
**3) Definir uma regra de atribuição:**
![](/files/5q4HvOT.gif)
**4) Com base na regra definida na etapa (3), as atribuições serão feitas automaticamente **São feitas como quando um problema é criado ou atualizado. Confira o GIF abaixo para ver a automação em ação quando o status de um tíquete de emissão é *atualizado*:
![](/files/Qb0kAzo.gif)
Nota: Se necessário, a regra também pode ser desativada/atualizada:
![](/files/PZbCDuu.png)
Da mesma forma, você pode automatizar o processo de Vendas no ERPNext para atribuir leads à sua equipe de Vendas e garantir mais taxas de conversão!! Obrigado por ler este artigo! Se precisar de mais ajuda com isso, entre em contato com nossa comunidade [aqui](https://discuss.erpnext.com/)