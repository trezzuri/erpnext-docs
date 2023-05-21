# domínio de e-mail


**O `Email Domain` é o nome de exibição de uma rede de e-mail/conta de serviço que você está configurando para seus serviços de e-mail no ERPnext.**


Você pode pular para a criação da [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account) se estiver usando um dos serviços listados [aqui](/docs/v13/user /manual/en/setting-up/email/email-inbox#2-create-an-email-domain).


Você pode configurar domínios de e-mail no ERPNext para facilitar a configuração de todas as contas de e-mail. Para encontrar as configurações de domínio de e-mail, acesse:



>
> Início > Configurações > Domínio de e-mail
>
>
>


**Qual é o meu domínio de e-mail?:** Você pode ter adquirido um serviço de e-mail de seu provedor de serviços de Internet ou de TI. Por exemplo, se você acessar sua caixa de correio comercial com URL como http://mail.suaempresa.com, espera-se que suaempresa.com seja usado como seu domínio de e-mail. O ERPnext tenta adivinhar o `Email Domain` do seu exemplo `Email Address` inserido inicialmente, se você começou a partir daí.


Se você deseja enviar e receber e-mails em sua conta ERPNext, você precisa configurar corretamente um `Domínio de e-mail`. Você pode estar usando serviços de e-mail gratuitos como GMail ou Yahoo. Nesse caso, você não precisa criar um domínio, em vez disso, selecione um provedor de serviços na lista. No entanto, você pode ter que permitir o acesso ao ERPNext para sua conta GMail.


O ERPNext cria um template `Email Domain` usando example.com para sua referência. Você deve adicionar seu novo domínio se quiser usá-lo em sua conta ERPNext.



>
> **IMPORTANTE:** Se o ID da sua conta de e-mail atual for diferente do endereço de e-mail de trabalho que você usa na configuração de `Conta de e-mail`, você precisará usar a opção `Usar ID de e-mail diferente` ao criar as diferentes contas de e-mail de trabalho para comunique-se com seu serviço e use a senha relacionada!
>
>
>


![Email Domain](/files/email-domain.png)


## 1. Como criar um domínio de e-mail


1. Vá para a lista Domínio de e-mail, clique em Novo.
2. Insira o endereço de e-mail de exemplo. É aqui que você insere seu endereço de e-mail comercial. Por exemplo, se o seu ID de e-mail for seunome@nomedasuaempresa.com, você deve inseri-lo.
3. Servidor de e-mail. Este é o URL do seu servidor de e-mail ou serviço de e-mail que você comprou. Por exemplo, pode ser mail.suaempresa.com ou imap.suaempresa.com.
4. Use IMAP. IMAP e POP são dois serviços usados ​​pela maioria dos servidores de e-mail para receber e-mails. Se o seu servidor de e-mail permitir o serviço IMAP para os e-mails recebidos, mantenha-o marcado. Caso contrário, deixe isso desmarcado.
5. Use SSL. Se o seu servidor de e-mail usar comunicação SSL (Secure Socket Layer), mantenha-o marcado.


**Tenho SSL?:** Você pode ter adquirido um certificado SSL de seu provedor de serviços de TI para SSL e eles podem ter configurado o SSL para seu servidor de e-mail. Se você estiver usando 'https' ao acessar o servidor de e-mail pelo navegador, talvez tenha configuração SSL.
6. Use SSL para envio. Se o seu servidor de e-mail usar SSL para envio, ative-o para usar SSL explicitamente para envio de e-mail. O padrão é a porta 465.
7. Anexar e-mail de saída à pasta Enviados. Se você não estiver usando servidores de e-mail padrão fornecidos pelo GMail e serviços semelhantes, talvez seja necessário habilitar esta opção para anexar todos os e-mails de saída à caixa de entrada da conta de e-mail. (Recomendado para servidores de e-mail como Zimbra e CPanel).
8. Limite de anexos (MB). Você pode limitar o tamanho dos anexos de arquivos nos e-mails enviados pelo ERPNext.
9. Servidor SMTP é o endereço de serviço de e-mail de saída do seu servidor de e-mail.
10. Marque Usar TLS se seu serviço SMTP oferecer suporte a TLS para segurança.
11. Porta padrão. O serviço SMTP geralmente é definido na porta 25. Se o seu servidor de e-mail estiver configurado em um número de porta separado, você poderá configurá-lo aqui.


### 1.1 Depois de salvar o domínio


Ao clicar em salvar, essas configurações são validadas pelo ERPNext e o Domínio de Email é salvo. Às vezes, isso pode levar alguns segundos e você pode ter que esperar. Esse domínio de e-mail fica disponível em um menu suspenso chamado Domínio na tela Contas de e-mail.


![Domínio de e-mail na conta de e-mail](/files/email-domain1.png)


#### Inseriu tudo, mas ainda não consegue configurar o domínio de e-mail?


Se você inseriu e verificou as configurações acima e ainda não consegue configurar o domínio de e-mail, entre em contato com o suporte do ERPNext em sua conta para obter ajuda.


### 2. Tópicos Relacionados


1. [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account)
2. [Caixa de entrada de e-mail](/docs/v13/user/manual/en/setting-up/email/email-inbox)