# Configurações de Agendamento


Você pode encontrar todas as configurações relacionadas ao agendamento de compromissos em Configurações de agendamento de compromissos.


![Appointment Booking Settings](/files/appointment-booking-settings.png)


## 1. Ativar agendamento de consultas


Esta caixa de seleção habilitará o agendamento de consultas e também habilitará a rota `/book_appointment` para usuários do site (seus clientes). Seus clientes verão uma visualização do portal. Para saber mais, visite a [Página de agendamento](/docs/pt/CRM/appointment)


## 2. Detalhes do agente


Nesta seção, você pode adicionar detalhes sobre agentes, como horário de trabalho e feriados.


### 2.1 Disponibilidade de slots


Aqui você pode definir o horário em que seus agentes estão disponíveis para atender a um compromisso. Isso é definido por dia da semana. Cada linha representa um bloco de tempo contínuo, você pode ter várias entradas para cada dia da semana.


Por exemplo, se seus agentes trabalham de segunda a sexta-feira, das 9h às 17h, mas com intervalo para almoço às 13h30 por meia hora. Você precisará criar duas entradas para cada dia. Uma das 9h às 13h30 e outra das 14h às 17h.


### 2.2 Agentes


Esta é a lista de agentes que serão **atribuídos automaticamente** aos compromissos. O número de compromissos que podem existir em um intervalo de tempo também depende do número de funcionários nesta lista.


### 2.3 Lista de feriados


Você pode vincular uma (lista de feriados) [https://erpnext.com/docs/pt/human-resources/holiday-list] aqui para se inscrever no agendamento de compromissos. Se o dia for feriado, não será permitido agendar um horário para esse dia.


## 3. Detalhes do compromisso


Esta seção contém detalhes sobre o próprio compromisso.


### 3.1 Duração do compromisso em minutos


A duração do compromisso em minutos. Isso é usado para calcular intervalos de tempo de compromisso para o portal da web. Alterar isso não afeta os compromissos criados antes da alteração.


### 3.2 Notificar por e-mail


Ativar esta caixa de seleção enviará um e-mail aos participantes dos compromissos, ou seja, seu funcionário e o cliente no dia do compromisso. Alterar esta caixa de seleção não afeta os compromissos criados antes da alteração.


### 3.3 Número de dias que o agendamento pode ser agendado com antecedência


Este é o número de dias que o compromisso pode ser agendado com antecedência. Se a lista de feriados fornecida acima terminar antes da data calculada usando esse número, o agendamento de compromissos será interrompido no final da lista de feriados.


## 4. Configurações de sucesso


### 4.1 URL de redirecionamento de sucesso


Esta é a URL para onde o usuário será redirecionado na criação de um compromisso bem-sucedido via Web Portal. Esse redirecionamento não ocorrerá ao criar compromissos na interface do usuário do Desk.
Deixe em branco para casa. Isso é relativo ao URL do site, por exemplo, "about" redirecionará para "https://yoursitename.com/about"

