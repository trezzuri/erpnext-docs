# Caixa de entrada de e-mail



**Depois que uma conta de e-mail for adicionada, a caixa de entrada de e-mail ficará acessível.**


Administrar uma empresa envolve muitas trocas de e-mails transacionais com partes como clientes e fornecedores e outros membros da empresa. O recurso Caixa de entrada de e-mail permite que você coloque todos os seus e-mails comerciais em sua conta ERPNext. Permitir o acesso a e-mails comerciais com outros detalhes transacionais torna o ERPNext uma plataforma única para acessar todas as informações comerciais em um só lugar.


No ERPNext, você pode configurar a Caixa de Entrada de Email para cada Usuário do Sistema. A seguir estão as etapas detalhadas para configurar a Caixa de entrada de e-mail para um usuário.


## 1. Crie um usuário


Você pode configurar uma caixa de entrada de e-mail apenas para um usuário do sistema. Portanto, certifique-se de ter adicionado você e seus colegas como usuário e atribuído a eles as permissões necessárias.


Para saber como adicionar um novo usuário, acesse a [página do usuário.](/docs/pt/setting-up/users-and-permissions/adding-users)


## 2. Crie um domínio de e-mail


O domínio de e-mail para os seguintes serviços está disponível imediatamente e você pode prosseguir diretamente para criar um [Conta de e-mail](/docs/pt/setting-up/email/email-conta). Saiba mais sobre como criar um domínio de e-mail [aqui](/docs/pt/setting-up/email/email-domain).


* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* **Outlook.com**
* **Yandex.mail**


![Serviço de e-mail](/files/email-service.png)


Para poder enviar e receber e-mails em sua conta ERPNext de outros serviços de e-mail (como WebMail ou Gmail), você deve configurar um domínio de e-mail mestre. Neste mestre, os detalhes do gateway de e-mail, como endereço SMTP, número da porta e detalhes do endereço IMAP/POP3, são capturados. Se você já configurou um cliente de email local (como o Outlook), o Email Domain Master exige que os detalhes sejam alimentados de forma semelhante.


Para adicionar um novo domínio de e-mail, acesse:


> Página inicial > Configurações > E-mails > Domínio de e-mail > Novo


![Domínio de e-mail](/files/email-domain.png)


Saiba mais sobre domínios de e-mail [aqui](/docs/pt/setting-up/email/email-domain). Depois de configurar um Domínio de Email para o seu Serviço de Email, ele será usado para criar Contas de Email para todos os Usuários da sua conta ERPNext.


## 3. Conta de e-mail


Crie uma conta de e-mail com base no ID de e-mail do usuário. Para cada Usuário cuja conta de e-mail será integrada ao ERPNext, uma Conta de E-mail mestre deverá ser criada para ele.


Se você estiver criando uma conta de e-mail para um colega cuja senha de e-mail é desconhecida para você, marque o campo "Aguardando senha". De acordo com esta configuração, um usuário (para quem a conta de e-mail foi criada) receberá uma solicitação para inserir a senha do e-mail ao acessar sua conta ERPNext.


![Senha do e-mail](/files/email-password.png)


> Se você estiver criando uma conta de e-mail para a caixa de entrada de e-mail de um usuário, deixe o campo Anexar a em branco.


Leia a [documentação da conta de e-mail](/docs/pt/setting-up/email/email-account) para obter mais detalhes sobre como configurar.


## 4. Vinculando conta de e-mail no usuário mestre


Depois que uma conta de e-mail for criada para um usuário, selecione essa conta de e-mail no usuário. Isso garantirá que os e-mails extraídos do referido ID de e-mail serão acessíveis apenas a este usuário em sua conta ERPNext.


![Enviar link de usuário por e-mail](/files/email-user-link.png)


Você pode vincular vários e-mails a um usuário.


## 5. Usando a caixa de entrada de e-mail


Se você configurou corretamente a Caixa de entrada de e-mail conforme as instruções acima, no login de um usuário, o ícone da Caixa de entrada de e-mail ficará visível. Isto irá navegar o usuário para a visualização da caixa de entrada de e-mail dentro da conta ERPNext. Todos os e-mails recebidos nesse e-mail serão obtidos e listados na visualização Caixa de entrada de e-mail. O usuário poderá abrir e-mails e realizar diversas ações neles.


### 5.1 Pastas


No ERPNext, você pode vincular múltiplas contas de e-mail com um único usuário. Para mudar para a Caixa de entrada de uma conta de e-mail diferente e acessar outras pastas como E-mails enviados, Spam, Lixeira, clique na opção Caixa de entrada de e-mail na barra esquerda.


![Pastas de e-mail](/files/email-folders.png)


### 5.2 Ações


Nos e-mails da sua caixa de entrada, você pode realizar diversas ações, como Responder, Encaminhar, Marcar como Spam ou Lixeira.


![Ações de e-mail](/files/email-actions.png)


### 5.3 Revincular


Você pode vincular novamente um e-mail a um documento como Problema, Lead, Oportunidade etc. com base no contexto do e-mail. Selecione o tipo de documento e o documento ao qual vincular o e-mail.


![Make from Email](/files/make-from-email.png)


### 6. Tópicos Relacionados


1. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Enviando e-mail](/docs/pt/setting-up/email/sending-email)
3. [Domínio de e-mail](/docs/pt/setting-up/email/email-domain)



