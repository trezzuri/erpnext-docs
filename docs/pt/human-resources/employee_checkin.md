# Check-in de funcionários



Employee Checkin é usado para manter um registro de todos os check-ins e check-outs de um funcionário na organização. A maioria das organizações usa isso para cálculos de frequência, gerenciamento de turnos e horas de trabalho.

### 1. Pré-requisitos

Para criar um Employee Checkin, você precisa primeiro criar:

* [Funcionário](/docs/pt/human-resources/employee)

Se você deseja que os turnos sejam determinados nas verificações dos funcionários e deseja para processar o atendimento automático, você também precisará criar os seguintes documentos:

* [Tipo de mudança](/docs/pt/human-resources/shift_type )
* [Atribuição de turno](/docs/pt/human-resources/shift_assignment) ou defina um turno padrão no cadastro de funcionários.

### 2 . Como criar um Checkin de Funcionário

#### 2.1 Criando logs manualmente

Para criar um novo Checkin de Funcionário acesse:


> Recursos Humanos > Presença > Checkin de Funcionário 
> 
> 

1. Clique em Novo.
2. Selecione o funcionário.
3. Defina a data e a hora do registro.
4. Defina o tipo de registro como IN/OUT.
5. Salvar.
6. Se você configurou turnos e atribuições de turnos, o Employee Checkin definirá o turno apropriado no qual o carimbo de data e hora cai após o salvamento.
7. Você pode ativar *Ignorar atendimento automático* para pular esse registro enquanto marca presença.
8. Você também pode capturar o local de onde o funcionário esteve registrado ou o ID do dispositivo biométrico.

![Employee Checkin](/files/employee-checkin.png)

Se o atendimento automático estiver habilitado, o registro de atendimento marcado para um conjunto de check-ins será vinculado ao documento posteriormente.

#### 2.2 Integrando o Frappe HR com Dispositivos Biométricos

Se você estiver usando um dispositivo biométrico para registrar check-ins e check-outs de funcionários, você pode usá-lo para criar registros no Frappe HR. Você pode ler mais sobre isso [aqui](/docs/pt/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices).



