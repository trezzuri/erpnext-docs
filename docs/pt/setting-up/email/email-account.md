# Conta de e-mail


**Você pode sincronizar sua conta de e-mail com o SOMA para enviar e receber e-mails do SOMA.**


Você pode gerenciar várias contas de e-mail recebidas e enviadas no SOMA. Deve haver pelo menos uma conta de saída padrão e uma conta de entrada padrão. Se você estiver na nuvem SOMA, o e-mail de saída padrão é definido por nós.


Para acessar as contas de e-mail, acesse:



> 
> Página inicial > Configurações > Conta de e-mail
> 
> 
> 


## 1. Pré-requisitos


Antes de criar uma conta de e-mail, você precisa de um [domínio de e-mail](/docs/pt/setting-up/email/email-domain). No entanto, você pode pular a criação de um domínio de e-mail se estiver usando um dos serviços listados [aqui](/docs/pt/setting-up/email/email-inbox#2-create-an -email-domain).


## 2. Como criar uma conta de e-mail


1. Vá para a lista Conta de e-mail, clique em Novo.
2. Insira o endereço de e-mail com o domínio. [Domínios](/docs/pt/setting-up/email/email-domain) precisam ser criados para criar uma conta de e-mail. Você não precisa criar um domínio se estiver sincronizando um e-mail de determinados provedores conforme listado [aqui](/docs/pt/setting-up/email/email-inbox#2-create -an-email-domain).
3. Digite a senha da conta de e-mail.
4. Salvar. Se as credenciais estiverem corretas, a conta de e-mail será sincronizada.



> 
> Observação: para alguns serviços como o Gmail, pode ser necessário ativar as configurações para permitir aplicativos menos seguros.
> 
> 
> 


### 2.1 Opções adicionais ao criar uma conta de e-mail


1. **Usar ID de login de e-mail diferente**: para usar um login e senha de e-mail alternativos para acessar esta conta. Por exemplo, se você tiver [notifications@example.com](mailto:notifications@example.com) e quiser que os usuários acessem este e-mail com um ID de e-mail alternativo, eles devem marcar esta caixa de seleção. Os destinatários verão [notifications@example.com](mailto:notifications@example.com) como o remetente.
2. **Aguardando senha**: Se você estiver criando esta conta em nome de alguém e a senha for desconhecida, marque esta caixa de seleção. Quando o outro usuário fizer login, ele será solicitado a inserir a senha.
3. **Usar codificação ASCII para senha**: Marcar esta opção usará codificação ASCII para a senha.


## 3. Configuração da conta de e-mail


### 3.1 Contas de e-mail padrão


O SOMA criará modelos para várias contas de e-mail por padrão. Nem todos eles estão ativados. Para ativá-los, você deve definir detalhes válidos da conta de e-mail.


Existem dois tipos de contas de e-mail, enviadas e recebidas. As contas de e-mail de saída usam um serviço SMTP para enviar e-mails e os e-mails são recuperados de sua caixa de entrada usando um IMAP ou POP. A maioria dos provedores de e-mail, como Gmail, Outlook ou Yahoo, fornece esses serviços.


![Defining Criteria](/files/email-account-list.png)


### 3.2 Contas de e-mail de entrada


Para configurar uma conta de e-mail de entrada, marque **Ativar entrada** e defina suas configurações POP3. Se estiver usando um serviço de e-mail popular, elas serão predefinidas para você.


![Incoming EMail](/files/email-account-incoming.png)


As seguintes opções estão disponíveis para e-mails recebidos:


1. **Usar IMAP**
2. **Usar SSL**
3. **Limite de anexos**
4. **Recebimento padrão**: Se marcada, todas as respostas para sua empresa (por exemplo: [replies@yourcomany.com](mailto:replies@yourcomany.com)) virão para esta conta.
5. **Opção de sincronização de e-mail**: sincronizar todos ou apenas os e-mails não vistos.
6. **Contagem de sincronização inicial**: número de e-mails para sincronizar pela primeira vez.


#### Anexando e-mails a documentos


Este recurso cria documentos quando um e-mail é enviado para uma conta de e-mail específica. Por exemplo, você pode anexar [support@example.com](mailto:support@example.com) ao Issue DocType. Ao fazer isso, sempre que um e-mail for enviado para [support@example.com](mailto:support@example.com), o sistema criará um problema para ele. Da mesma forma, se você vincular [jobs@example.com](mailto:jobs@example.com), quando os e-mails forem enviados para [jobs@ example.com](mailto:jobs@example.com), um documento de candidato a emprego é criado.


Ativar vinculação automática em documentos vinculará e-mails a documentos, para saber mais [clique aqui](/docs/pt/setting-up/email/linking-emails-to-document) .


### 3.4 Contas de e-mail de saída


Todos os e-mails enviados do sistema, seja pelo contato do usuário ou por meio de notificações ou e-mails de transações, serão enviados de uma conta de e-mail de saída.


Para configurar uma conta de e-mail de saída, marque **Ativar saída** e defina as configurações do servidor SMTP. Se você estiver usando um serviço de e-mail popular, elas serão predefinidas para você.


![Enviar e-mail](/files/email-account-sending.png)


As seguintes opções estão disponíveis para e-mails enviados:


1. **Usar TLS**
2. **Porta**
3. **Desativar a autenticação do servidor SMTP**
4. **Adicionar assinatura**: a assinatura padrão é anexada ao final de cada e-mail.
5. **Saída padrão**: notificações e e-mails em massa serão enviados deste servidor de saída.
6. **Sempre use o endereço de e-mail da conta como remetente**: o endereço de e-mail desta conta será mencionado como remetente para e-mails enviados.
7. **Enviar mensagem de cancelamento de inscrição em um e-mail**: envie um link para cancelar a inscrição de e-mails enviados desta conta.
8. **Acompanhar status do e-mail**: Rastreie se o seu e-mail foi aberto pelo destinatário. Observe que, se você estiver enviando para vários destinatários, mesmo que um destinatário leia o e-mail, ele será considerado "Aberto".
9. **Ativar resposta automática**: se ativado, insira uma mensagem de resposta automática.
10. **Anexar e-mail de saída à pasta Enviados**: Se estiver usando servidores de e-mail personalizados como Zimbra ou CPanel, o SMTP não anexará e-mails automaticamente à pasta Enviados. A ativação dessa opção garantirá que todos os e-mails sejam explicitamente anexados à pasta Enviados da conta de e-mail.
11. **Usar SSL para e-mails enviados**: use SSL como padrão para e-mails enviados. O padrão é a porta 465.


## 4. Como o SOMA trata as respostas


No SOMA quando você enviar um e-mail para um contato como cliente, o remetente será o usuário que enviou o e-mail. Na propriedade **Reply-To**, o endereço de e-mail será da conta de entrada padrão (como `[replies@yourcompany.com](mailto:replies@yourcompany.com)`) . O SOMA extrairá automaticamente esses e-mails da conta recebida e os marcará na comunicação relevante.



> 
> **Observação para implementadores automáticos:** para e-mails de saída, você deve configurar seu próprio servidor SMTP ou se inscrever em um serviço de retransmissão SMTP como mandrill.com ou sendgrid.com que permite um número maior de transações e-mails a serem enviados. Serviços de e-mail regulares, como o Gmail, restringem você a um número limitado de e-mails por dia.
> 
> 
> 


Se você encontrar erros ao configurar uma conta de e-mail, consulte [esta página](/docs/pt/setting-up/articles/email-error).< /p>
## 5. Vídeo



### 6. Tópicos Relacionados


1. [Caixa de entrada de e-mail](/docs/pt/setting-up/email/email-inbox)
2. [Email Resumo](/docs/pt/setting-up/email/email-digest)
3. [Relatórios de e-mail automático](/docs/pt/setting-up/email/auto-email-reports)
4. [Envio de e-mail](/docs/pt/setting-up/email/sending-email)
5. [Domínio de e-mail](/docs/pt/setting-up/email/email-domain)


