# Campanha por e-mail



**Uma campanha por e-mail é um conjunto coordenado de e-mails enviados a leads ou contatos de acordo com uma programação específica.**


As campanhas por e-mail ainda são uma das maneiras mais eficazes de alcançar seus clientes, contatos ou leads e mantê-los engajados. Por exemplo, você pode configurar campanhas por e-mail para apresentar seu produto aos clientes, com cada e-mail revelando um recurso interessante de seu produto.


Para criar uma campanha por e-mail, acesse:


> Página inicial > CRM > Campanha > Campanha por e-mail


## 1. Pré-requisitos


Antes de criar e usar uma campanha de e-mail, elas precisam ser criadas primeiro:


* [Campanha](/docs/pt/CRM/campaign)
* [Lead](/docs/pt/CRM/lead) ou [Contato](/docs/pt/CRM/contact) ou [Grupo de e-mail](/docs/pt/CRM/email_group)


## 2. Como criar uma campanha por e-mail


1. Vá para a lista Campanha por e-mail e clique em Novo.
2. Selecione a [Campanha](/docs/pt/CRM/campaign) para a qual deseja configurar uma campanha por e-mail.
3. Defina a 'Data de início' da campanha por e-mail.
4. Em 'Campanha por e-mail para', selecione se deseja configurar uma campanha por e-mail para um lead ou contato ou para um grupo de e-mail enviar para vários contatos de e-mail.
5. Em 'Destinatário', selecione o respectivo lead ou contato ou grupo de e-mail para o qual você deseja iniciar a campanha por e-mail.
6. Em 'Remetente', selecione o usuário do sistema que deverá ser o remetente dos e-mails.
7. Salvar


![Campanha por e-mail](/files/email-campaign.png)


A campanha de e-mail acima é para a seguinte campanha:


![Programação da campanha](/files/campaign-email-schedule.png)


**Observação**: o campo **Enviar após (dias)** no Campaign especifica o dia em que o e-mail será enviado em relação à **Data de início** da **campanha por e-mail**. Observe a 'Data de término' na campanha de e-mail acima. É '26-07-2019', ou seja, 4 dias após a 'Data de início', '22-07-2029', já que o cronograma da campanha termina no dia 4.


### 2.1 Criar várias campanhas de e-mail para uma campanha


Você também pode criar novas campanhas por e-mail para diferentes leads ou contatos para a mesma campanha por meio do painel da campanha.


1. Vá para a campanha para a qual deseja criar campanhas por e-mail.
2. Clique em + na frente de Campanhas por e-mail para criar uma nova campanha por e-mail para a campanha.


![Campanhas por e-mail do painel](/files/campaign-dashboard.png)


## 3. Recursos


### 3.1 Comunicação vinculada


Quando os e-mails são enviados para os respectivos leads ou contatos, a Comunicação é vinculada ao documento Campanha por e-mail. Você pode ver todos os e-mails enviados no seu documento.


![Comunicação vinculada](/files/email-campaign-linked-comm.png)


### 3.2 Cancelar assinatura da campanha por e-mail


Se um lead ou contato não quiser continuar recebendo e-mails sobre a campanha, ele poderá cancelar a inscrição na campanha por e-mail por meio do link de cancelamento enviado com o e-mail.


![Link de cancelamento de assinatura](/files/unsubscribe-link.png)


Quando o lead ou contato cancela a assinatura, o status do documento da campanha por e-mail muda para 'Cancelado'.


![Unsubscribed](/files/email-campaign-unsubscribed.png)


### 3.3 Use os campos Lead ou Contato no modelo de e-mail


O modelo de e-mail tem o contexto do documento que você especificou no campo 'Campanha por e-mail para'. Se quiser exibir os campos do seu documento Lead ou Contato em seu modelo de e-mail, você terá que usar `doc.fieldname` para o mesmo.
 Por exemplo, se 'Campanha por e-mail para' for 'Contato', você poderá mencionar o 'nome' do seu contato como `doc.first_name` no modelo de e-mail, conforme mostrado abaixo:


![Documento de modelo de e-mail](/files/email-template-doc.png)
![](/docs/v13/assets/img/crm/)


Então os e-mails enviados ficariam assim:


![Enviar dados do documento da campanha por e-mail](/files/email-campaign-doc-data.png)
![](/docs/v13/assets/img/crm/)


### 3.4 Indicação de status


Status indica o estado da campanha por e-mail, os vários status são:


* **Programada**: quando a campanha por e-mail ainda não foi iniciada, mas está agendada para uma 'Data de início' futura.
* **Em andamento**: a campanha seria marcada como 'Em andamento' entre a 'Data de início' e a 'Data de término' da campanha.
* **Concluída**: após a 'Data de término' da campanha, o status será alterado para 'Concluído'.
* **Cancelamento de inscrição**: quando o Lead ou Contato cancela a inscrição na Campanha.


![Status da campanha por e-mail](/files/email-campaign-status.png)


## 4. Tópicos Relacionados


1. [Campanha](/docs/pt/CRM/campaign)
2. [Líder](/docs/pt/CRM/lead)
3. [Contato](/docs/pt/CRM/contact)


Próximo: [Boletim informativo](/docs/pt/CRM/newsletter)



