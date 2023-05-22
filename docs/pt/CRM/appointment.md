# Agendamento


**Um compromisso é uma reunião pré-combinada entre um líder e um funcionário da sua empresa.**


O tipo de documento de compromisso pode ser usado para agendar e gerenciar a interação com um [Lead](/docs/pt/CRM/lead) ou um [Oportunidade](/ docs/v13/user/manual/en/CRM/opportunity).


Para acessar a lista de compromissos, acesse:



> 
> Página inicial > CRM > Pipeline de vendas > Compromisso
> 
> 
> 


## 1. Pré-requisitos


1. [Configurações de agendamento de horários](/docs/pt/CRM/appointment-booking-settings)
2. [Lista de feriados](/docs/pt/human-resources/holiday-list)
3. [Funcionário](/docs/pt/human-resources/employee)
4. [Lead](/docs/pt/CRM/lead)
5. [E-mail](/docs/pt/setting-up/email/email-account)


## 2. Como criar um compromisso


1. Vá para a lista de compromissos, clique em Novo
2. Selecione o horário agendado do compromisso
3. Insira os detalhes do cliente
4. Em documentos vinculados, se você já criou um lead para o cliente, pode defini-lo aqui. Caso contrário, o sistema criará automaticamente um novo lead com os detalhes do cliente da etapa anterior.
5. Salvar.
![Novo compromisso](/files/new-appointment.png)


### 2.1 Criação de agendamentos via site


Seus clientes/leads podem criar compromissos usando a página da web `yoursitename.com/book_appointment`.


Primeiro eles precisam definir uma data, hora.
![Appointment Webform](/files/appointment-webform.png)


Em seguida, adicione mais detalhes:
![Detalhes do compromisso](/files/appointment-details.png)


Ele corresponderá ao e-mail do cliente com os leads no sistema e, se algum for encontrado, será vinculado ao documento.
Se nenhum lead for encontrado, o compromisso é marcado como "Não verificado" e um e-mail é enviado ao cliente para confirmar seu e-mail


## 3. Recursos


### 3.1 Atribuição automática


Os compromissos são atribuídos automaticamente aos funcionários de acordo com a lista `Agentes` em [Configurações de agendamento de compromissos](/docs/pt/CRM/appointment-booking-settings) . O agente com o menor número de atribuições para o dia do agendamento e que estiver livre no horário agendado é designado para o agendamento.


### 3.2 Confirmação de e-mail


Se não houver nenhum lead correspondente em seu sistema, um e-mail será enviado para o endereço de e-mail no agendamento para confirmar se o endereço de e-mail é válido. Após a confirmação, um novo lead também será criado no sistema junto com o agendamento.

