# Recibo de salário



**Um comprovante de salário é um documento emitido para um funcionário. Ele contém uma descrição detalhada dos componentes e valores do salário do funcionário.**


Para acessar o Comprovante de Salário, acesse:
> Home > Recursos Humanos > Folha de Pagamento > Recibo de Salário


## 1. Pré-requisitos


Antes de criar o Comprovante de Salário, é aconselhável que você crie primeiro o seguinte:


* [Funcionário](/docs/pt/human-resources/employee)
* [Estrutura salarial](/docs/pt/human-resources/salary-structure)
* [Atribuição de estrutura salarial](/docs/pt/human-resources/salary-structure-assignment)


## 2. Como criar um comprovante de salário


1. Vá para Recibo de Salário, clique em Novo.
2. Selecione Funcionário. Ao selecionar Funcionário, todos os detalhes do Funcionário serão obtidos na Estrutura Salarial atribuída a esse Funcionário. Isso inclui detalhes como frequência da folha de pagamento, ganhos, deduções, etc.
3. Selecione a data de início e a data de término.
4. Salvar.


## 3. Recurso


### 3.1. Comprovante de salário baseado em frequência/licença


Os usuários de RH podem criar recibo de salário com base na frequência ou licença.
Os dias úteis serão calculados com base nas férias/assiduidade, dependendo do campo **Calcular dias úteis da folha de pagamento com base em** em [Configurações de RH](/docs/pt/human-resources/hr-settings). Se a folha de pagamento for baseada na frequência, então, a **licença sem remuneração** será considerada como ausente e **meio dia** será considerado como meio dia ausente.


### 3.2. Comprovante de salário com base no quadro de horários


Para criar recibo de salário com base no quadro de horários, você precisa criar uma estrutura salarial para quadros de horários.


O Frappe HR também oferece a opção de criar comprovante de salário com base nas horas de trabalho com base no [Quadro de Horários](/docs/pt/projects/timesheets).
Você pode criar o comprovante de salário após enviar o quadro de horários clicando diretamente no botão **Criar comprovante de salário** no canto superior direito.


![Criar comprovante de salário com base em planilhas de horas](/files/create-salary-slip-based-on-timesheets.png)


O valor do pagamento é calculado com base na taxa horária definida na estrutura salarial e é refletido na tabela de rendimentos.


### 3.3 Acumulado no ano e acumulado no mês


Para cada comprovante de salário, 'Acumulado no ano' e 'Acumulado no mês' são computados.


![Acumulado no ano e acumulado no mês](/files/ytd-and-mtd.png)


* **Acumulado no ano**: salário total registrado para esse funcionário específico desde o início do ano (período processado na folha de pagamento ou ano fiscal) até a data de término do comprovante de salário atual.
* **Acumulado no mês**: Salário total registrado para um determinado funcionário desde o início do mês (para o qual o lançamento da folha de pagamento é criado) até a data de término do comprovante de salário atual.


Acumulado no ano também é calculado para cada componente nas tabelas de rendimentos e deduções. O formato de impressão "Recibo de salário com acumulado no ano" está disponível com cálculos acumulados no ano e no mês.


![Acumulado no ano para componentes do comprovante de salário](/files/ytd-component.png)



