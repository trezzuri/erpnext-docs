# Vinculando e-mails a documentos



>
> Introduzido na v12
>
>
>


**Um e-mail pode ser vinculado a vários documentos no ERPNext.**


Isso pode ser feito das duas maneiras a seguir:


* Agregação de Email em Contato, Cliente, Fornecedor.
* Vinculação automática de e-mail.


## 1. Agregação de Email para Cliente e Fornecedor


A agregação de e-mail ocorre em Contato, Cliente e Fornecedor. Todos os e-mails enviados ou recebidos de um contato podem ser visualizados na linha do tempo desse contato e também na linha do tempo vinculada do cliente ou do fornecedor. Para habilitar a agregação de e-mail, faça o seguinte:


1. Em um Contato, adicione Links para o Cliente ou Fornecedor respectivamente.


![Adicionar cliente/fornecedor no contato](/files/contact-link.png)
2. Agora, quando um e-mail é enviado ou recebido do contato associado ao cliente ou fornecedor, esse e-mail é vinculado ao cliente ou fornecedor mencionado na seção de links do contato.


![Com filtros](/files/email_aggregation.gif)


## 2. E-mail automático com link para um documento


A vinculação automática de e-mail vincula um e-mail ao documento especificado no endereço de e-mail exclusivo gerado pelo sistema para um documento. Se um e-mail for enviado ou recebido usando o endereço de e-mail exclusivo, o sistema vinculará esse e-mail ao documento.


1. Ative a vinculação automática de e-mail na conta de e-mail. Este recurso pode ser usado apenas com uma conta de e-mail por vez.


![Adicionar cliente/fornecedor no contato](/files/enable_email_link.png)
2. Depois que esse recurso for ativado, você verá uma ID de e-mail exclusiva gerada usando a ID de e-mail mencionada na conta de e-mail.
3. Agora você pode copiar o ID de e-mail clicando nele e pode enviar ou receber e-mails usando o ID de e-mail exclusivo. Se um e-mail contiver esse ID de e-mail exclusivo na seção Destinatários, Cc ou Bcc, o sistema vinculará esse e-mail ao documento especificado.


![Adicionar cliente/fornecedor no contato](/files/email_link.gif)


### 3. Tópicos Relacionados


1. [Relatórios de e-mail automático](/docs/v13/user/manual/en/setting-up/email/auto-email-reports)
2. [Enviando e-mail de qualquer documento](/docs/v13/user/manual/en/setting-up/email/sending-email)
3. [Document Follow](/docs/v13/user/manual/en/setting-up/email/document-follow)