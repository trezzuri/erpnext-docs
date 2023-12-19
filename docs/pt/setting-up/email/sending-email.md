# Enviando e-mail de qualquer documento



No ERPNext você pode enviar qualquer documento como email (com um anexo em PDF) clicando em Menu > Email após abrir qualquer documento.

![Enviar email](/files/send-email.gif)  


 **Observação:** você deve ter [e-mail de saída Contas](/docs/pt/setting-up/email/email-account) configuradas para isso.

Depois de clicar em enviar, o e-mail é adicionado à fila de e-mails. Ele estará no status Enviando até ser Enviado. O status do e-mail é exibido na fila, caso o envio tenha falhado, ele pode ser enviado clicando em Enviar agora.

![Email Queue](/files/email-queue.png)  


As seguintes opções estão disponíveis ao enviar um e-mail.* **PARA:** Destinatários do e-mail.
* **De:** Se o usuário tiver acesso a várias contas de e-mail de saída, ele poderá selecionar qual conta de e-mail de saída usar. Várias contas de e-mail de saída podem ser configuradas no documento Usuário, adicionando-as à tabela "E-mail do usuário".
* **CC**: cópia carbono do e-mail. Útil quando você deseja manter alguém informado sobre a conversa, mas não deseja enviar o e-mail diretamente para essa pessoa.
* **BCC**: Blind Carbon Copy é semelhante ao CC, mas todos os outros participantes do e-mail não conseguem ver que o e-mail também foi enviado aos destinatários do CCO. Isso é útil para ocultar o endereço de e-mail de certas pessoas se você estiver enviando o e-mail para muitas pessoas que não necessariamente se conhecem.
* **E-mail Modelo**: você pode criar modelos predefinidos para enviar respostas padrão. Os modelos de e-mail já estão disponíveis no sistema para notificação de despacho, notificação de status de licença e notificação de aprovação de licença. Você pode definir um modelo de e-mail padrão por meio de [Personalizar formulário](/docs/pt/customize-erpnext/customize-form).
* **Envie-me uma cópia**: Isso enviará uma cópia para seu endereço de e-mail. É útil garantir que o e-mail foi enviado sem erros.
* **Enviar recibo de leitura**: marcar esta caixa de seleção enviará uma notificação se o destinatário tiver Leia o email. No caso de vários destinatários, mesmo que um tenha lido o e-mail, você receberá uma notificação.
* **Anexar impressão do documento**: anexe o PDF do o documento que você está enviando por e-mail.
* **Selecionar anexos**: quaisquer anexos adicionais podem ser adicionados aqui.

Os dois campos a seguir são os campos que aparecem na tela de impressão:

![Email Print Options](/files/email-print-options.png)  


* **Selecionar formato de impressão**: O formato de impressão do documento. Saiba mais sobre o formato de impressão [aqui](/docs/pt/setting-up/print/print-format).
* **Selecionar idiomas**: o idioma no qual o PDF será gerado.

###  Tópicos relacionados

1. [Domínio de e-mail](/docs/pt/setting-up/email/email-domain)
2. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
3. [Caixa de entrada de e-mail](/docs/pt/setting-up/email/email-inbox)




