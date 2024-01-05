# Configurando e-mail SMTP Sendgrid no ERPNext



SMTP, ou protocolo simples de transferência de e-mail, é uma maneira rápida e fácil de enviar e-mails de um servidor para outro. SendGrid fornece um serviço SMTP que permite entregar seu e-mail através de nosso servidor em vez de seu cliente ou servidor. O ERPNext vem integrado com um cliente de e-mail configurado para que você possa enviar e receber e-mails no ERPNext e anexar a documentos, se necessário.  
**Integrando o SendGrid's API Web**A API SMTP do SendGrid permite que os desenvolvedores especifiquem instruções de tratamento personalizadas para e-mail usando um cabeçalho X-SMTPAPI inserido na mensagem.  
**Etapa 1:** Você precisa criar uma chave de API para autenticar seu aplicativo. Neste caso, *ERPNext*. Saiba mais sobre a integração do SendGrid com SMTP [aqui](https://sendgrid.com/docs/API_Reference/SMTP_API/integrating_with_the_smtp_api.html)  
![](/files/5Wqn0hV.png)  
  
 **Passo 2:** Depois que sua *chave API* for criada, você precisa configurá-la em sua conta ERPNext > Criar uma **Nova** **conta de e-mail.**  
**Endereço de e-mail:** *Seu endereço de e-mail* **ID de login de e-mail:** *Chave de API* [Chave de API gerada na Etapa 1]**Senha:** *Sua senha* **Serviço:** selecione "*SendGrid*"  
![](/files/Q9to7Iu.png)  
  
  
Agora **salve** essas informações e você configurou com sucesso o e-mail SMTP SendGrid no ERPNext.  
Poder para você!  
  
-----**﻿**

