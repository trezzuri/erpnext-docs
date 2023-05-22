# Vinculando e-mails a documentos



> 
> Introduzido na v12
> 
> 
> 


**Um e-mail pode ser vinculado a vários documentos no ERPNext.**


Isso pode ser feito das duas maneiras a seguir:


* Agregação de e-mail em contato, cliente, fornecedor.
* Link de e-mail automático.


## 1. Agregação de e-mail para cliente e fornecedor


A agregação de e-mail ocorre em Contato, Cliente e Fornecedor. Todos os e-mails enviados ou recebidos de um contato podem ser visualizados na linha do tempo desse contato e também na linha do tempo vinculada do cliente ou do fornecedor. Para ativar a agregação de e-mail, faça o seguinte:


1. Em um contato, adicione links para o cliente ou fornecedor, respectivamente.


![Adicionar cliente/fornecedor em contato](/files/contact-link.png)
2. Agora, quando um e-mail é enviado ou recebido do contato associado ao cliente ou fornecedor, esse e-mail é vinculado ao cliente ou fornecedor mencionado na seção de links do contato.


![Com filtros](/files/email_aggregation.gif)


## 2. Link de e-mail automático para um documento


A vinculação automática de e-mail vincula um e-mail ao documento especificado no endereço de e-mail exclusivo gerado pelo sistema para um documento. Se um e-mail for enviado ou recebido usando o endereço de e-mail exclusivo, o sistema vinculará esse e-mail ao documento.


1. Ative a vinculação automática de e-mail na conta de e-mail. Este recurso pode ser usado apenas com uma conta de e-mail por vez.


![Adicionar cliente/fornecedor em contato](/files/enable_email_link.png)
2. Depois que esse recurso for ativado, você verá um ID de e-mail exclusivo gerado usando o ID de e-mail mencionado na conta de e-mail.
3. Agora você pode copiar o ID de e-mail clicando nele e pode enviar ou receber e-mails usando o ID de e-mail exclusivo. Se um e-mail contiver esse ID de e-mail exclusivo na seção Destinatários, Cc ou Bcc, o sistema vinculará esse e-mail ao documento especificado.


![Adicionar cliente/fornecedor em contato](/files/email_link.gif)


### 3. Tópicos Relacionados


1. [Relatórios de e-mail automático](/docs/pt/setting-up/email/auto-email-reports)
2. [Envio de e-mail de qualquer documento](/docs/pt/setting-up/email/sending-email)
3. [Acompanhamento de documento](/docs/pt/setting-up/email/document-follow)
