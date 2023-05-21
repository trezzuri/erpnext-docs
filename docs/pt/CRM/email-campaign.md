# Campanha de e-mail


**Uma campanha de e-mail é um conjunto coordenado de e-mails enviados para leads ou contatos de acordo com uma programação específica.**


As campanhas de e-mail ainda são uma das formas mais eficazes de alcançar seus clientes, contatos ou leads e mantê-los engajados. Por exemplo, você pode configurar campanhas de e-mail para apresentar seu produto aos clientes, com cada e-mail revelando um recurso interessante de seu produto.


Para criar uma Campanha de Email, acesse:



>
> Home > CRM > Campanha > Campanha de e-mail
>
>
>


## 1. Pré-requisitos


Antes de criar e usar a campanha de e-mail, eles precisam ser criados primeiro:


* [Campanha](/docs/v13/user/manual/en/CRM/campanha)
* [Lead](/docs/v13/user/manual/en/CRM/lead) ou [Contato](/docs/v13/user/manual/en/CRM/contact) ou [Grupo de e-mail](/docs/v13 /user/manual/en/CRM/email_group)


## 2. Como criar uma campanha de e-mail


1. Vá para a lista Campanha de e-mail, clique em Novo.
2. Selecione a [Campanha](/docs/v13/user/manual/en/CRM/campanha) para a qual você deseja configurar uma campanha de e-mail.
3. Defina a 'Data de início' para a campanha de e-mail.
4. Em 'Campanha de e-mail para', selecione se deseja configurar a campanha de e-mail para um lead ou um contato ou para um grupo de e-mail para enviar a vários contatos de e-mail.
5. Em 'Destinatário', selecione o respectivo Lead ou Contato ou Grupo de Email para o qual você deseja iniciar a Campanha de Email.
6. Em 'Remetente', selecione o usuário do sistema que deverá ser o remetente dos e-mails.
7. Salve


![Campanha por e-mail](/files/email-campaign.png)


A campanha de e-mail acima é para a seguinte campanha:


![Cronograma da campanha](/files/campaign-email-schedule.png)


**Observação**: O campo **Enviar após (dias)** em Campanha especifica o dia em que o e-mail deve ser enviado em relação à **Data de início** da **Campanha por e-mail**. Observe a 'Data final' na campanha de e-mail acima. É '26-07-2019', ou seja, 4 dias após a 'Data de Início', '22-07-2029', pois o Calendário da Campanha termina no dia 4.


### 2.1 Criar várias campanhas de e-mail para uma campanha


Você também pode criar novas Campanhas de E-mail para diferentes Leads ou Contatos para a mesma Campanha através do Painel de Campanhas.


1. Vá para a Campanha para a qual você deseja criar Campanhas de Email.
2. Clique em + na frente de Campanhas de Email para criar uma nova Campanha de Email para a Campanha.


![Campanhas de e-mail do painel](/files/campaign-dashboard.png)


## 3. Características


### 3.1 Comunicação vinculada


Quando os e-mails são enviados para os respectivos leads ou contatos, a Comunicação é vinculada ao documento Campanha de e-mail. Você pode visualizar todos os e-mails enviados em seu documento.


![Comunicação vinculada](/files/email-campaign-linked-comm.png)


### 3.2 Cancelar inscrição da campanha de e-mail


Se um lead ou contato não quiser continuar recebendo e-mails sobre a campanha, ele poderá cancelar a inscrição na Campanha por e-mail por meio do link de cancelamento de inscrição enviado com o e-mail.


![Link de cancelamento de inscrição](/files/unsubscribe-link.png)


Quando o lead ou contato cancela a assinatura, o status do documento Campanha de e-mail muda para 'Cancelado'.


![Cancelado inscrição](/files/email-campaign-unsubscribe.png)


### 3.3 Usar campos de lead ou contato no modelo de e-mail


O modelo de e-mail tem o contexto do documento que você especificou no campo 'Campanha de e-mail para'. Se você quiser exibir os campos do seu documento Lead ou Contato em seu modelo de e-mail, você terá que usar `doc.fieldname` para o mesmo.
 Por exemplo, se 'Campanha de e-mail para' for 'Contato', você pode mencionar o 'primeiro nome' do seu contato como `doc.first_name` no modelo de e-mail, conforme mostrado abaixo:


![Documento de modelo de e-mail](/files/email-template-doc.png)
![](/docs/v13/assets/img/crm/)


Então os e-mails enviados ficariam assim:


![Email Campaign Doc Data](/files/email-campaign-doc-data.png)
![](/docs/v13/assets/img/crm/)


### 3.4 Indicação de status


Status indica o estado da Campanha de Email, os vários Status são:


* **Agendado**: Quando a campanha de e-mail ainda não foi iniciada, mas está programada para uma 'Data de início' futura.
* **Em andamento**: a campanha seria marcada como 'Em andamento' entre a 'Data de início' e a 'Data de término' da campanha.
* **Concluído**: Após a 'Data de término' da campanha, o status será alterado para 'Concluído'.
* **Cancelado**: Quando o Lead ou Contato cancela a assinatura da Campanha.


![Status da campanha por e-mail](/files/email-campaign-status.png)


## 4. Tópicos Relacionados


1. [Campanha](/docs/v13/user/manual/en/CRM/campanha)
2. [Lead](/docs/v13/user/manual/en/CRM/lead)
3. [Contato](/docs/v13/user/manual/en/CRM/contato)


Seguinte: [Newsletter](/docs/v13/user/manual/en/CRM/newsletter)