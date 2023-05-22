# Caixa de entrada de e-mail


**Assim que uma conta de e-mail for adicionada, a caixa de entrada do e-mail ficará acessível.**


Administrar um negócio envolve muitas trocas de e-mails transacionais com partes como clientes e fornecedores e outros membros da empresa. O recurso Caixa de entrada de e-mail permite que você extraia todos os seus e-mails comerciais para sua conta SOMA. Permitir o acesso a e-mails comerciais com outros detalhes transacionais torna o SOMA uma plataforma única para acessar todas as informações comerciais em um só lugar.


No SOMA, você pode configurar a caixa de entrada de e-mail para cada usuário do sistema. A seguir estão as etapas detalhadas para configurar a caixa de entrada de e-mail para um usuário.


## 1. Criar um usuário


Você pode configurar uma caixa de entrada de e-mail apenas para um usuário do sistema. Portanto, certifique-se de ter adicionado a si mesmo e seus colegas como um usuário e atribuído a eles as permissões necessárias.


Para saber como adicionar um novo usuário, vá para a [Página do usuário.](/docs/pt/setting-up/users-and-permissions/adding-users)


## 2. Crie um domínio de e-mail


O domínio de e-mail para os seguintes serviços está disponível pronto para uso e você pode prosseguir diretamente para criar um [Conta de e-mail](/docs/pt/setting-up/email/email- conta). Saiba mais sobre como criar um domínio de e-mail [aqui](/docs/pt/setting-up/email/email-domain).


* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* **Outlook.com**
* **Yandex.mail**


![Serviço de e-mail](/files/email-service.png)


Para poder enviar e receber e-mails em sua conta SOMA de outros serviços de e-mail (como WebMail ou Gmail), você deve configurar um mestre de domínio de e-mail. Neste mestre, os detalhes do gateway de e-mail, como endereço SMTP, número da porta e detalhes do endereço IMAP/POP3, são capturados. Se você já configurou um cliente de e-mail local (como o Outlook), o mestre de domínio de e-mail requer que os detalhes sejam alimentados da mesma forma.


Para adicionar um novo domínio de e-mail, acesse:



> 
> Página inicial > Configurações > E-mails > Domínio de e-mail > Novo
> 
> 
> 


![Email Domain](/files/email-domain.png)


Saiba mais sobre domínios de e-mail [aqui](/docs/pt/setting-up/email/email-domain). Depois de configurar um domínio de email para seu serviço de email, ele será usado para criar contas de email para todos os usuários em sua conta SOMA.


## 3. Conta de e-mail


Crie uma conta de e-mail com base no ID de e-mail do usuário. Para cada Usuário cuja conta de e-mail será integrada ao SOMA, deverá ser criada uma Conta de E-mail mestre para o mesmo.


Se você estiver criando uma conta de e-mail para seu colega cuja senha de e-mail é desconhecida para você, marque o campo "Aguardando senha". De acordo com esta configuração, um usuário (para quem a conta de e-mail foi criada) receberá uma solicitação para inserir a senha do e-mail ao acessar sua conta SOMA.


![Email Password](/files/email-password.png)



> 
> Se você estiver criando uma conta de e-mail para a caixa de entrada de e-mail de um usuário, deixe o campo Anexar a em branco.
> 
> 
> 


Leia [documentação da conta de e-mail](/docs/pt/setting-up/email/email-account) para obter mais detalhes sobre como configurar.


## 4. Vinculando a conta de e-mail no usuário mestre


Assim que uma conta de e-mail for criada para um usuário, selecione essa conta de e-mail no usuário. Isso garantirá que os e-mails extraídos do referido ID de e-mail sejam acessíveis apenas a este usuário em sua conta SOMA.


![Email User Link](/files/email-user-link.png)


Você pode vincular vários e-mails com um usuário.


## 5. Usando a caixa de entrada de e-mail


Se você configurou corretamente a caixa de entrada de e-mail conforme instruído acima, no login de um usuário, o ícone da caixa de entrada de e-mail ficará visível. Isso levará o usuário à exibição Caixa de entrada de e-mail na conta SOMA. Todos os e-mails recebidos nesse e-mail serão buscados e listados na exibição Caixa de entrada de e-mail. O usuário poderá abrir e-mails e realizar várias ações neles.


### 5.1 Pastas


No SOMA, você pode vincular várias contas de e-mail com um único usuário. Para alternar para a Caixa de entrada de uma conta de e-mail diferente e acessar outras pastas como E-mails enviados, Spam, Lixeira, clique na opção Caixa de entrada de e-mail na barra esquerda.


![Pastas de e-mail](/files/email-folders.png)


### 5.2 Ações


Nos e-mails da sua caixa de entrada, você pode realizar várias ações, como responder, encaminhar, marcar como spam ou lixo.


![Ações de e-mail](/files/email-actions.png)


### 5.3 Revincular


Você pode vincular novamente um e-mail a um documento como Problema, Lead, Oportunidade etc. com base no contexto do e-mail. Selecione o tipo de documento e o documento ao qual vincular o e-mail.


![Make from Email](/files/make-from-email.png)


### 6. Tópicos Relacionados


1. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Envio de e-mail](/docs/pt/setting-up/email/sending-email)
3. [Domínio de e-mail](/docs/pt/setting-up/email/email-domain)
