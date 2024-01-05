# Atendimento automático



A presença automática marca a presença dos funcionários atribuídos a um turno com base nos registros do [Employee Checkin](/docs/pt/human-resources/employee_checkin) e o documento [Configurações de atendimento automático](/docs/pt/human-resources/shift-type#2-auto-attendance-settings) desse turno.


> Observação: [Tipo de turno](/docs/en/shift-type) precisa ser configurado e atribuído aos funcionários antes de criar registros de 'Checkin de funcionários'. A presença será marcada como Atendimento automático apenas para registros de check-in criados após configurar e atribuir um funcionário ao seu tipo de turno.
> 
> 

## Etapas para configurar o comparecimento automático

Você pode configurar o Atendimento Automático seguindo as etapas mencionadas abaixo:

### 1. Definir tipo de turno com atendimento automático habilitado

Você terá que definir um tipo de turno com atendimento automático habilitado. Detalhes podem ser encontrados [aqui](/docs/v14/en/shift-type).

### 2. Atribua esses turnos aos funcionários

Depois de configurar um turno, você terá que atribuí-lo aos funcionários. Você pode atribuir isso a um funcionário usando um dos dois métodos abaixo:

* **Usando a atribuição de turno**: você pode usar o [Atribuição de turnos](/docs/pt/human-resources/shift_assignment) documento para atribuir turnos aos funcionários de acordo com a data.
* **Usando o campo Turno Padrão no cadastro de funcionários**: Às vezes você desejaria atribuir um turno para um funcionário para todos os dias. Você pode fazer isso definindo o seguinte campo no Funcionário: `> Funcionário > Detalhes de presença e licença > Turno padrão`


> Observação: A configuração da atribuição de turno tem precedência sobre o turno padrão. ou seja, se você configurou uma atribuição de turno, bem como um turno padrão para um funcionário, o sistema considerará o turno atribuído em vez de um turno padrão.
> 
> 

### 3. Configurar o campo ID do dispositivo de presença em Funcionário

Os sistemas biométricos geralmente têm seus próprios IDs para funcionários. Porém, o Checkin do Funcionário no Frappe HR precisa ser mapeado para um funcionário.

Para mapear o funcionário para seus IDs no sistema Biométrico é necessário definir o seguinte campo com o valor apropriado: `Funcionário > Detalhes de presença e licença > ID do dispositivo de presença (ID de etiqueta biométrica/RF)`

### 4. Importe ou sincronize Checkins de funcionários

Depois de concluir as etapas acima, você poderá importar/sincronizar o [Check-in de funcionários](/docs/pt/human-resources/employee_checkin) e comece a gerar presença automaticamente.

Consulte este artigo para saber mais sobre como preencher Check-ins de funcionários a partir de um sistema externo: [Integrando o Frappe HR com dispositivos de atendimento biométrico](/docs/v14/en/integrating-frappehr-with-biometric-attendance-devices)

## Perguntas frequentes

### 1. Como são determinados os horários reais de início e término de um turno?

Considere um turno matinal:

* Horário de início: 08:00:00
* Horário de término: 11:30:00
* Início do check-in antes do horário de início do turno (em minutos): 60
* Permitir check-out após o horário de término do turno (em minutos): 60

Portanto, o "Hora de início real" do turno = *Horário de Início-Início do check-in antes do horário de início do turno* = 07:00:00

O "Horário de término real" do turno = *Horário de término + Permitir check-out depois horário de término do turno* = 12:30:00.

### 2. Quando a presença é marcada automaticamente para um turno específico?

Tenta-se que a presença automática para cada registro de 'Tipo de turno' seja marcada a cada hora. Você também pode acionar o atendimento automático manualmente para um único tipo de turno pressionando o botão 'Marcar atendimento automático' no documento Tipo de turno.

Após a "**Última sincronização de check-in**" após o horário real de término do turno, todos os check-ins de funcionários desse turno serão processados ​​para marcação de presença.

Por exemplo: Considere um turno matinal:

* Horário de início : 08:00:00
* Horário de término: 11:30:00
* Início do check-in antes do horário de início do turno (em minutos): 60
* Permitir check-out após o horário de término do turno (em minutos): 60

Então o "Horário de início real" do turno é 07:00:00 e o horário de término real do turno é 12:30:00.

Quando o carimbo de data e hora da "Última sincronização de check-in" passar de 12:30 :00, indica que todos os registros de check-in possíveis para aquele turno específico foram sincronizados/capturados e é nesse momento que a marcação de presença é tentada.

### 3. Como o Atendimento Automático determina o turno de um Funcionário?

O turno de um Funcionário em uma determinada data é determinado pelas seguintes etapas:

* Turno atribuído a um Funcionário Funcionário na data indicada no documento 'Atribuição de turno'.
* Se o acima não for encontrado, o turno será selecionado no campo 'Turno padrão' da seção 'Funcionário ' documento.
* Finalmente, se um turno também não for encontrado no documento 'Funcionário', então assume-se que o Funcionário não pertence a nenhum turno na data determinada e nenhuma tentativa de presença é marcada pelo trabalho de Atendimento Automático.

### 4. Como o Atendimento Automático determina a Lista de Feriados de um Funcionário?

A Lista de Feriados de um funcionário é determinada da seguinte forma:

* Se o 'Tipo de Turno' determinado pelo funcionário tiver uma lista de feriados, então isso será considerado.
* Caso contrário, a lista de feriados será obtida do campo 'Lista de feriados' no documento Funcionário ou da 'Lista de feriados padrão' no documento Empresa, nesta ordem.

Observação: É importante que a Lista de Feriados seja determinada corretamente pelo Atendimento Automático para não marcar o funcionário como 'Ausente' no feriados.

### 5. A maioria dos dispositivos biométricos não retorna o tipo de registro exato. Nesses casos, como o atendimento automático determinará qual registro está ENTRADA/SAÍDA e como ele calcula as horas de trabalho?

Isso é determinado por 2 campos na configuração do Tipo de Turno:

* Determinar check-in e check-out
* Cálculo do horário de trabalho com base em

Tem foi explicado em detalhes [aqui](/docs/v14/en/shift-type#2-auto-attendance-settings).



