# Domínio de e-mail



**O `Domínio de Email` é o nome de exibição de uma rede/conta de serviço de email que você está configurando para seus serviços de email no ERPnext.**


Você pode pular para a criação de uma [conta de e-mail](/docs/pt/setting-up/email/email-account) se estiver usando um dos serviços listados [aqui](/docs/pt/setting-up/email/email-inbox#2-create-an-email-domain).


Você pode configurar Domínios de Email no ERPNext para facilitar a configuração de todas as Contas de Email. Para encontrar as configurações do domínio de e-mail, acesse:


> Página inicial > Configurações > Domínio de e-mail


**Qual ​​é o meu domínio de e-mail?:** Você pode ter adquirido um serviço de e-mail do seu provedor de serviços de Internet ou de serviços de TI. Por exemplo, se você acessar sua caixa de correio comercial com um URL como http://mail.suaempresa.com, espera-se que suaempresa.com seja usado como seu domínio de e-mail. O ERPnext tenta adivinhar o `Domínio de Email` a partir do `Endereço de Email` do exemplo inserido inicialmente se você começou a partir daí.


Se você deseja enviar e receber emails em sua conta ERPNext, você precisa configurar corretamente um `Domínio de Email`. Você pode estar usando serviços de e-mail gratuitos como GMail ou Yahoo. Nesse caso, você não precisa criar um domínio; em vez disso, selecione um provedor de serviços na lista. No entanto, talvez seja necessário permitir o acesso ao ERPNext para sua conta do GMail.


ERPNext cria um modelo `Domínio de Email` usando example.com para sua referência. Você deve adicionar seu novo domínio se quiser usá-lo em sua conta ERPNext.


> **IMPORTANTE:** se o ID real da sua conta de e-mail for diferente do endereço de e-mail comercial usado na configuração da `Conta de e-mail`mais tarde, você precisará usar a opção  `Use um ID de e-mail diferente` ao criar diferentes contas de e-mail de trabalho para se comunicar com seu serviço e use a senha relacionada!


![Domínio de e-mail](/files/email-domain.png)


## 1. Como criar um domínio de e-mail


1. Vá para a lista Domínios de e-mail e clique em Novo.
2. Insira o endereço de e-mail de exemplo. É aqui que você insere seu endereço de e-mail comercial. Por exemplo, se o seu ID de e-mail for seunome@nomedasuaempresa.com, você deverá inseri-lo.
3. Servidor de e-mail. Este é o URL do seu servidor de e-mail ou do serviço de e-mail que você adquiriu. Por exemplo, pode ser mail.suaempresa.com ou imap.suaempresa.com.
4. Use IMAP. IMAP e POP são dois serviços usados ​​pela maioria dos servidores de e-mail para e-mails recebidos. Se o seu servidor de e-mail permitir o serviço IMAP para os e-mails recebidos, mantenha esta opção marcada. Caso contrário, deixe esta opção desmarcada.
5. Use SSL. Se o seu servidor de e-mail usa comunicação SSL (Secure Socket Layer), mantenha esta opção marcada.


**Eu tenho SSL?:** Você pode ter adquirido um certificado SSL do seu provedor de serviços de TI para SSL e ele pode ter configurado o SSL para o seu servidor de e-mail. Se você estiver usando 'https' ao acessar o servidor de e-mail pelo navegador, talvez você tenha configurado o SSL.
6. Use SSL para saída. Se o seu servidor de e-mail usa SSL para saída, habilite-o para usar SSL explicitamente para e-mails de saída. O padrão é a porta 465.
7. Anexar e-mail de saída à pasta enviada. Se você não estiver usando servidores de e-mail padrão fornecidos pelo GMail e serviços semelhantes, talvez seja necessário ativar esta opção para anexar todos os e-mails enviados à caixa de entrada da conta de e-mail. (Recomendado para servidores de e-mail como Zimbra e CPanel).
8. Limite de anexos (MB). Você pode limitar o tamanho dos anexos de arquivos em e-mails enviados pelo ERPNext.
9. Servidor SMTP é o endereço do serviço de e-mail de saída do seu servidor de e-mail.
10. Marque Usar TLS se o seu serviço SMTP suportar TLS para segurança.
11. Porta padrão. O serviço SMTP geralmente é configurado na porta 25. Se o seu servidor de e-mail estiver configurado em um número de porta separado, você poderá configurá-lo aqui.


### 1.1 Depois de salvar o domínio


Depois de clicar em salvar, essas configurações são validadas pelo ERPNext e o Domínio de Email é salvo. Às vezes, isso pode levar alguns segundos e talvez você precise esperar. Esse domínio de e-mail estará disponível em um menu suspenso chamado Domínio na tela Contas de e-mail.


![Domínio de e-mail na conta de e-mail](/files/email-domain1.png)


#### Inseriu tudo, mas ainda não conseguiu configurar o domínio de email?


Se você inseriu e verificou as configurações acima e ainda não consegue configurar o Domínio de E-mail, você pode entrar em contato com o suporte do ERPNext em sua conta para obter ajuda.


### 2. Tópicos Relacionados


1. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Caixa de entrada de e-mail](/docs/pt/setting-up/email/email-inbox)



