# Notificação



**Você pode configurar diversas notificações em seu sistema para lembrá-lo de atividades importantes.**


1. A data de conclusão de uma tarefa.
2. Data de entrega prevista de um pedido de venda.
3. Data prevista de pagamento.
4. Um lembrete de acompanhamento.
5. Se um pedido maior que um valor específico for recebido ou enviado.
6. Notificação de expiração de um contrato.
7. Conclusão/mudança de status de uma tarefa.


Para acessar a configuração de notificação, acesse:


> Página inicial > Configurações > Notificação


## 1. Configurando um alerta


Para configurar uma notificação:


1. Selecione o tipo de documento cujas alterações você deseja observar.
2. Defina quais eventos você deseja assistir em Enviar alerta ativado. Os eventos são:
	1. Novo: Quando um novo documento do tipo selecionado é feito.
	2. Salvar/Enviar/Cancelar: quando um documento do tipo selecionado é salvo, enviado ou cancelado.
	3. Dias Antes/Dias Depois: Acione este alerta alguns dias antes ou depois da **Data de Referência.** Para definir os dias, defina **Dias Antes ou Depois**. Isso pode ser útil para lembrá-lo das próximas datas de vencimento ou para lembrá-lo de acompanhar determinados leads de cotações.
	4. Alteração de valor: quando um determinado valor no tipo selecionado muda.
	5. Método: Envia notificação quando um método específico é acionado. Ex.: before\_insert.
	6. Personalizado: envie uma notificação para uma [Conta de e-mail](/docs/pt/setting-up/email/email-account) selecionada.
3. Defina condições adicionais, se necessário.
4. Defina os destinatários deste alerta. O destinatário pode ser um campo do documento ou uma lista de endereços de e-mail fixos.
5. Escreva a mensagem.
6. Salvar.


### 1.1 Definindo um assunto


Você pode recuperar os dados de um campo específico usando `doc.[field_name]`. Para usá-lo em seu assunto/mensagem, você deve cercá-lo com `{% raw %}&lcub;&lcub; }}{% endraw %}`. Elas são chamadas de tags [Jinja](http://jinja.pocoo.org/). Por exemplo, para obter o nome de um documento, use `{% raw %}&lcub;&lcub; doc.name }}{% endraw %}`. O exemplo a seguir envia um e-mail ao salvar uma tarefa com o assunto "TASK#### foi criada"


![Definir Assunto](/files/email-alert-subject.png)


### 1.2 Configurando condições


As notificações permitem que você defina condições de acordo com os dados de campo em seus documentos. Por exemplo, se você deseja receber um e-mail se um Lead tiver sido salvo como "Interessado" como status, coloque `doc.status == "Interessado"` na caixa de texto de condições. Você também pode definir condições mais complexas combinando-as com o operador **e** ou **ou**.


![Condição de configuração](/files/notification screenshot.jpg)


O exemplo acima enviará uma notificação quando uma tarefa for salva com o status "Aberta" e a "Data de término esperada" da tarefa for a data igual ou anterior à data em que ela foi salva.


### 1.3 Configurando uma mensagem


Você pode usar tags Jinja (`{% raw %}&lcub;&lcub; doc.[field_name] }}{% endraw %}`) e tags HTML na caixa de texto da mensagem.



```
{% raw %}### Pedido vencido



```

A transação &lcub;&lcub; doc.name }} excedeu a data de vencimento. Tome as medidas necessárias.



 {% se comentários %}
 Último comentário: &lcub;&lcub; comments[-1].comment }} por &lcub;&lcub; comments[-1].by }}
 {% endif %}



```
#### Detalhes



```

* Cliente: &lcub;&lcub; doc.customer }}
* Valor: &lcub;&lcub; doc.total\_amount }}

{% enddraw %}


### 1.4 Definir um valor após a definição do alerta


Às vezes, para garantir que a notificação não seja enviada várias vezes, você pode
defina uma propriedade personalizada (por meio do formulário personalizado) como "Notificação enviada" e, em seguida,
defina esta propriedade após o alerta ser enviado definindo **Definir propriedade após alerta**
campo.


Então você pode usar isso como uma condição nas regras de **Condição** para garantir que os e-mails não sejam enviados várias vezes


![Definindo propriedade na notificação](/files/email-alert-subject.png)


### 1.5 Exemplo


1. Definição dos critérios
![Critérios de definição](/files/email-alert-1.png)
2. Configurando os destinatários e a mensagem
![Definir mensagem](/files/email-alert-2.png)



## 2. Notificações do Slack


Se preferir que suas notificações sejam enviadas para um canal dedicado do Slack, você também pode escolher a opção "Slack" nas opções do canal e selecionar o URL apropriado do Webhook do Slack.


### 2.1 URL do webhook do Slack


Um URL de webhook do Slack é um URL que aponta diretamente para um canal do Slack.


Para gerar URLs de webhook, você precisa criar um novo aplicativo Slack:


1. Acesse https://api.slack.com/slack-apps.
2. Clique em "Criar um aplicativo Slack".
![Definir mensagem](/files/slack_notification_1.png)
3. Dê um nome ao seu aplicativo e escolha o espaço de trabalho correto.
Depois que seu aplicativo for criado, vá para a seção "Webhooks de entrada" e adicione um novo Webhook ao Workspace.
![Definir mensagem](/files/slack_notification_2.png)
4. Copie o link criado, volte para o ERPNext e use-o para criar uma nova URL do Slack Webhook em Integrações > URL do Slack Webhook.
![Definir mensagem](/files/slack_notification_3.png)
5. Selecione Slack e seu canal do Slack nos campos canal e canal do Slack na sua notificação


### 2.2 Formato da mensagem


Ao contrário das mensagens de e-mail, o Slack não permite formatação HTML.


Em vez disso, você pode usar a formatação markdown: [Documentação do Slack](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)


Exemplo:
 {% cru %}
 *Pedido vencido*



```
A transação &lcub;&lcub; doc.name }} excedeu a data de vencimento. Por favor, tome as medidas necessárias.


{% se comentários %}
Último comentário: &lcub;&lcub; comments[-1].comment }} por &lcub;&lcub; comments[-1].by }}
{% fim se %}

*Detalhes*

• Cliente: &lcub;&lcub; doc.customer }}
• Valor: &lcub;&lcub; doc.grand_total }}
{% sacar %}

```

![Definir mensagem](/files/slack_notification_4.png)



## 3. Notificações do sistema


Na **versão 12**, introduzimos notificações do sistema para **Tarefas**, **menções**, **documentos compartilhados** e  **Pontos de Energia**. Essas notificações aparecem no menu suspenso de notificações no canto superior direito da barra de navegação.


Na **versão 13**, introduzimos um canal adicional para enviar alertas-**Notificações do sistema**:


![Menu suspenso de notificações](/files/system-notifications-channel.png)


A escolha deste canal enviará uma notificação do sistema quando uma notificação for acionada, em vez de uma notificação por e-mail ou Slack.


![Menu suspenso de notificações](/files/system-notification.png)


Clicar na notificação direciona para o documento **Registro de Notificação** que contém o assunto configurado, a mensagem e o arquivo anexado, se Anexar Impressão estiver definido:


![Menu suspenso de notificações](/files/notification-log.png)


Se os alertas por e-mail/Slack e as notificações do sistema forem necessários, o canal principal pode ser definido como e-mail ou Slack e esta opção pode ser marcada:


![Menu suspenso de notificações](/files/send-system-notification.png)


## 4. WhatsApp


Na **versão 13** introduzimos um canal adicional para enviar alertas-**WhatsApp**:
![Canal de notificações do WhatsApp](/files/twilio-channel.png)


Se preferir que suas notificações sejam enviadas para um número do WhatsApp, você também pode escolher a opção "WhatsApp" nas opções do canal e selecionar o número Twilio apropriado. Os números do Twilio podem ser adicionados às configurações do Twilio no Frappe. As mensagens do WhatsApp só podem ser enviadas para números que contenham códigos de país.


![Configurações do Twilio](/files/twilio-settings.png)


### 4.1 Configurações do Twilio


Para definir as configurações da Twilio, primeiro você precisa obter as credenciais da Twilio nas configurações de conta da sua conta da Twilio. Você só pode adicionar os números de telefone que foram ativados em sua conta Twilio com acesso ao WhatsApp.
![Credenciais do Twilio](/files/twilio-credentials.png)


### 4.2 Formato da mensagem


O WhatsApp permite que seus usuários enviem apenas modelos de mensagens pré-aprovados por eles para seus clientes. Não fazer isso pode resultar em restrições à sua conta Twilio.
![Modelo de mensagem pré-aprovado](/files/twilio-pre-approved-message.png)


## 5. SMS


Na **versão 13** introduzimos um canal adicional para enviar alertas-**SMS**:
![Canal SMS](/files/sms-notification-channel.png)


Para usar este canal, você precisa concluir a configuração de [Configurações de SMS](/docs/pt/setting-up/sms-setting). 


### 6. Tópicos Relacionados


1. [Configurações de SMS](/docs/pt/setting-up/sms-setting)
2. [Acompanhamento de documento](/docs/pt/setting-up/email/document-follow)


### 7. Lembretes únicos


> Observação: esse recurso só está disponível na versão noturna no momento.


Como a configuração de notificações é um processo bastante complicado, o Frappe Framework também fornece uma maneira de configurar lembretes únicos em documentos. Um exemplo dessa notificação seria "Lembre-me de acompanhar esse lead em 4 horas"


Para configurar um lembrete único no documento:


1. Abra o documento no qual deseja definir um lembrete
2. Clique no menu (três pontos) > "Lembrar-me"
3. Selecione o horário, adicione uma descrição para você e clique em "Criar"
4. O sistema enviará uma notificação do sistema na hora que você configurou, com a descrição do lembrete como assunto.



