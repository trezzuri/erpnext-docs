# Planejamento de capacidade



O planejamento de capacidade é o processo no qual uma organização decide se aceita ou não os novos pedidos com base nos recursos e nas ordens de serviço existentes.


O planejamento de capacidade foi ativado por padrão em sua conta. Para saber mais, acesse:


> Home > Fabricação > Configurações > Configurações de Fabricação


![Ordem de trabalho](/files/capacity_planning_settings.png)


## 1. Pré-requisitos


Antes de criar e usar uma Ordem de Serviço, é aconselhável criar primeiro o seguinte:


* [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
* [Operação](/docs/pt/manufacturing/operation)
* [Estação de trabalho](/docs/pt/manufacturing/workstation)
* [Ordem de serviço](/docs/pt/manufacturing/work-order)


## 2. Como funciona o planejamento de capacidade no ERPNext


O usuário deve definir o número de dias no campo "Planejamento de capacidade para" nas configurações de fabricação para planejar as próximas ordens de serviço. Por exemplo, se você manteve o Planejamento de Capacidade por 30 dias e para fazer 1 produto acabado são necessários 5 dias, então na data atual o usuário só poderá aceitar as 6 ordens de serviço (30/5 = 6). Você poderá realizar a próxima ordem de serviço quando sua [estação de trabalho](/docs/pt/manufacturing/workstation) for liberada.


### 2.1 Criar ordem de serviço com operações


O usuário precisa criar as Ordens de Serviço com Operações para que o sistema rastreie os tempos do [Cartão de Trabalho](/docs/pt/manufacturing/job-card) em relação a Ordem de Serviço.


![Ordem de trabalho](/files/work_order_with_operations.png)


Assim que o usuário enviar a Ordem de Serviço, o sistema gerará o Cartão de Trabalho com os detalhes de horário da Estação de Trabalho disponível. Se 'Permitir Horas Extras' estiver desativado nas Configurações de Fabricação, o sistema agendará o trabalho de acordo com os horários definidos na Estação de Trabalho. Se "Permitir produção em feriados" estiver desativado, o sistema agendará o trabalho apenas em dias úteis.


### 2.2 Capacidade de produção da estação de trabalho


Na Estação de Trabalho o usuário pode definir a 'Capacidade de Produção'. Este é o número de operações que o sistema permitirá que você trabalhe nesta estação de trabalho. Por exemplo, se uma determinada estação de trabalho puder realizar 10 operações ao mesmo tempo, insira a 'Capacidade de produção' como 10.


![Ordem de trabalho](/files/work_station_capacity.png)


### 2.3 Cartão de trabalho com tempo


O sistema criará automaticamente o Cartão de Trabalho com cronometragem para cada operação com base no tempo necessário para concluir essa operação e na disponibilidade da estação de trabalho. O usuário deve definir a data de início planejada e com base no tempo de operação, o sistema calcula a data de término planejada.


![Ordem de serviço](/files/job_card_timing.png)


### 2.4 Data de início e data de término planejadas da ordem de serviço


Com base nas datas de início e término planejadas, os usuários podem calcular a capacidade de suas estações de trabalho. Além disso, eles podem acompanhar o status da ordem de serviço usando o [Calendário](/docs/pt/using-erpnext/calendar).


Para visualizar o calendário, vá para:


> Lista de ordens de serviço > Calendário > Padrão


![Ordem de trabalho](/files/work_order_calendar.png)


### 2.5 Erro de planejamento de capacidade


Se os dias de capacidade de produção forem menores que o tempo necessário para concluir a operação, o sistema gerará um erro de planejamento de capacidade. Neste caso, o usuário deve aumentar o número de dias em "Capacidade de Produção" nas Configurações de Fabricação ou reduzir o número de produtos acabados de acordo com a capacidade das Estações de Trabalho


![Ordem de trabalho](/files/capacity_planning_error.png)



