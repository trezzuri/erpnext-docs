# Estrutura salarial



**Estrutura Salarial é o detalhamento do salário oferecido a um Colaborador, em termos da divisão dos diferentes componentes que constituem a remuneração.**

Quaisquer alterações na a Estrutura Salarial, ou seja, entre os componentes pode ter um grande impacto no que o Funcionário faz, como o tipo de isenções fiscais reivindicadas.

O Frappe HR permite definir os Ganhos e Deduções de uma Estrutura Salarial, Folha de Pagamento frequência e forma de pagamento entre outras funcionalidades.

Para acessar a Estrutura Salarial, acesse:


> Home > Recursos Humanos > Folha de Pagamento > Estrutura Salarial
> 
> 

## 1. Pré-requisitos

Antes de criar uma Estrutura Salarial, é aconselhável que você tenha o seguinte:

* [Componente salarial](/docs/pt/human-resources/salary-component)

## 2. Como criar uma estrutura salarial

1. Vá para a lista Estrutura salarial, clique em Novo.
2. Insira o nome da estrutura salarial.
3. Selecione o nome da empresa e a frequência da folha de pagamento.
4. Salve e envie.

## 2. Recursos

### 2.1 Rendimentos e Deduções

Os rendimentos especificam os componentes salariais que são ganhos por um funcionário. Esses componentes normalmente incluem subsídios básicos, bônus e incentivos que são adicionados ao salário total do funcionário. Por outro lado, as Deduções especificam os Componentes Salariais que são deduzidos do Salário Total do funcionário. Normalmente incluem os impostos.


> **Observação:** Somente os componentes salariais definidos como 'Ganhos' serão mostrados na tabela de Ganhos e os componentes definidos como 'Deduções' serão mostrados na tabela Deduções.
> 
> 

Para criar Rendimentos e Deduções, selecione o Componente Salário na coluna Componente. Insira a Fórmula/Condição se não tiver sido especificada anteriormente ao criar o [Salário Componente](/docs/pt/human-resources/salary-component). Além disso, você também pode inserir um valor predefinido na coluna Valor.

![Salary Structure](/files/salary-structure.png)


> **Observação:** certifique-se de clicar na seta para baixo e ativar a caixa de seleção 'Valor baseado na fórmula' caso o componente salarial seja calculado usando uma fórmula.
> 
> 

### 2.2 Conta

Nesta seção, o rel [Modo de pagamento](https://docs.erpnext.com/docs/pt/accounts/articles/mode_of_payment) e o [Conta de pagamento](https://docs.erpnext.com/docs/pt/accounts/chart-of-accounts) usada para pagar o salário pode ser especificada.

### 2.3 Estrutura salarial para salário com base em planilhas de horas

No Frappe HR você também pode definir a Estrutura Salarial do Comprovante de Salário com base no Quadro de Horários, o que permite que a Empresa pague o Funcionário de acordo com a jornada de trabalho.

Etapas para criação da Estrutura Salarial com base em Quadros de horários:

1. Vá para Lista de estrutura salarial, clique em Novo.
2. Marque a caixa de seleção **Recibo de salário com base no quadro de horários**.
3. Selecione o componente salarial.
4. Insira a taxa horária. Com base na Taxa inserida, o valor das horas de trabalho para o componente salarial selecionado será calculado adequadamente.
5. Salvar e enviar.

![Criar recibo de salário com base em planilhas de horas](/files/salary-structure-for-salary-based-on-timesheets.png)

### 2.4 Deixar cobrança Valor por dia

Caso haja licenças resgatáveis ​​para um Funcionário, você pode definir o valor das férias por dia neste campo para esta Estrutura Salarial específica. Com base no 'Componente de ganho' definido no [Tipo de licença](/docs/pt/human-resources/leave-type)  e o valor por dia, o valor do componente Salário será calculado de acordo com o Recibo de Salário.

### 2.5 Benefícios Máximos (Valor)

Neste campo, o O valor máximo de benefícios para a estrutura salarial pode ser especificado. Se este campo for preenchido, certifique-se de que a Estrutura Salarial tenha um  [Componente Salarial](/docs/pt/human-resources/salary-component) com a opção "É Benefícios Flexíveis" marcada, contra a qual esse valor será pago.

Depois que todas as informações forem salvas e enviadas, você pode atribuir a Estrutura Salarial a um Funcionário por meio de o botão **Atribuir estrutura salarial** ou criando uma nova [Atribuição da estrutura salarial](/docs/pt/human-resources/salary-structure-assignment) através do painel.

Você também pode atribuir a estrutura salarial criada a vários funcionários com base no [Classificação do funcionário](/docs/pt/human-resources/employee-grade), [Departamento](/docs/pt/human-recursos/departamento), [Designação](/docs/pt/human-resources/designation), etc. através do botão 'Atribuir aos funcionários'. Além disso, o Comprovante de Salário também pode ser criado diretamente através do painel.

## 3. Tópicos relacionados

1. [Componente salarial](/docs/pt/human-resources/salary-component)
2. [Atribuição de estrutura salarial](/docs/pt/human-resources/salary-structure-assignment)
3. [Entrada da folha de pagamento](/docs/pt/human-resources/payroll-entry)


