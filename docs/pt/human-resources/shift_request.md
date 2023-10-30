# Solicitação de turno



A solicitação de turno é usada por um funcionário para solicitar um tipo de turno específico.

### 1. Pré-requisitos

Para criar uma solicitação de turno, estes precisam ser criados primeiro:

* [Funcionário](/docs/pt/recursos humanos/funcionário)
* [Tipo de turno](/docs/pt/human-resources/shift_type)

### 2. Como criar uma solicitação de turno

Para criar uma nova solicitação de turno, vá para: > Recursos Humanos > Gerenciamento de turno > Solicitação de turno

1. Vá para Lista de solicitações de turno, Clique em Novo.
2. Selecione Funcionário e Tipo de Turno.
3. Defina a duração do turno usando Data Inicial e Data Até.
4. Selecione o Aprovador. Se o aprovador selecionado não tiver acesso ao documento de solicitação de turno, ele será compartilhado com o aprovador com permissão de "envio".
5. Salvar.
6. Depois que a solicitação de turno for aprovada e enviada, ela criará um [Atribuição de turno](/docs/pt/human-resources/shift_assignment)

![Solicitação de turno](/files/shift-requestae7f8e.png)

 ### 3. Configurando o Aprovador de Solicitação de Turno

Um Aprovador de Solicitação de Turno é um usuário que pode aprovar uma Solicitação de Turno de um Funcionário. O Aprovador de Solicitação de Turno pode ser definido em dois níveis:

* **Nível de Departamento:** Os Aprovadores de Solicitação de Turno para cada departamento podem ser configurados no [Departamento](/docs/pt/human-resources/department) mestre. Vários aprovadores de solicitação de turno podem ser definidos em um departamento.

![Aprovadores de solicitação de turno](/files/department-shift-request-approvers.png)

Quando um Funcionário pertencente a um determinado departamento solicita o Tipo de Turno, o Aprovador de Solicitação de Turno definido no cadastro de departamento desse Funcionário será considerado como seu Aprovador do Tipo de Turno.
* **Nível do funcionário:** O aprovador de solicitação de turno também pode ser definido no cadastro de funcionários.

![Aprovadores de solicitação de turno](/files/employee-shift-request-aprover.png)

Se o Aprovador de solicitação de turno estiver definido tanto no nível do funcionário quanto no nível do departamento, o Aprovador de solicitação de turno no nível do funcionário será considerado como o Aprovador de licença padrão neste caso. 



