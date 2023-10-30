# Configurações de agendamento de compromissos



Você pode encontrar todas as configurações relacionadas ao agendamento de compromissos em Configurações de agendamento de compromissos.


![Configurações de reserva de compromisso](/files/appointment-booking-settings.png)


## 1. Ativar agendamento de compromissos


Essa caixa de seleção ativará o agendamento de compromissos e também a rota `/book_appointment` para usuários do site (seus clientes). Seus clientes verão uma visualização do portal. Para saber mais, visite a [Página de agendamento](/docs/pt/CRM/appointment)


## 2. Detalhes do agente


Nesta seção, você pode adicionar detalhes sobre os agentes, como horário de trabalho e feriados.


### 2.1 Disponibilidade de slots


Aqui você pode definir o horário em que seus agentes estarão disponíveis para comparecer a um compromisso. Isso é definido por dia da semana. Cada linha representa um bloco contínuo de tempo. Você pode ter várias entradas para cada dia da semana.


Por exemplo, se seus agentes trabalham de segunda a sexta, das 9h às 17h, mas com intervalo para almoço às 13h30 por meia hora. Você precisará criar duas entradas para cada dia. Uma das 9h às 13h30 e outra das 14h às 17h.


### 2.2 Agentes


Esta é a lista de agentes que serão **atribuídos automaticamente** aos compromissos. O número de compromissos que podem existir em um intervalo de tempo também depende do número de funcionários nesta lista.


### 2.3 Lista de feriados


Você pode vincular uma (lista de feriados)[https://erpnext.com/docs/pt/human-resources/holiday-list] aqui para se inscrever no agendamento de consultas. Caso o dia seja feriado, não será permitido agendamento de consulta nesse dia.


## 3. Detalhes do compromisso


Esta seção contém detalhes sobre o compromisso em si.


### 3.1 Duração do compromisso em minutos


A duração do compromisso em minutos. Isso é usado para calcular intervalos de tempo de compromisso para o portal da web. Alterar isso não afeta os compromissos criados antes da alteração.


### 3.2 Notificar por e-mail


Ativar esta caixa de seleção enviará um e-mail aos participantes dos agendamentos, ou seja, seu funcionário e o cliente no dia do agendamento. Alterar esta caixa de seleção não afeta os compromissos criados antes da alteração.


### 3.3 Número de dias em que o agendamento pode ser agendado com antecedência


Este é o número de dias em que a consulta pode ser agendada com antecedência. Se a Lista de Feriados fornecida acima terminar antes da data calculada usando este número, o agendamento de compromissos será interrompido ao final da lista de feriados.


## 4. Configurações de sucesso


### 4.1 URL de redirecionamento de sucesso


Esta é a URL para onde o usuário será redirecionado na criação de um agendamento bem-sucedido via Web Portal. Esse redirecionamento não ocorrerá ao criar compromissos na UI do Desk.
Deixe em branco para casa. Isso é relativo ao URL do site, por exemplo, "about" será redirecionado para "https://nomedoseusite.com/about"



