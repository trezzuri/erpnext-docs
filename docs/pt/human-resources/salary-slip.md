# Recibo de salário



**O comprovante de salário é um documento emitido para um funcionário. Contém uma descrição detalhada dos componentes e valores salariais do funcionário.**

Para acessar o Comprovante de Salário, acesse: > Home > Recursos Humanos > Folha de Pagamento > Comprovante de Salário

## 1 . Pré-requisitos

Antes de criar o Comprovante de Salário, é aconselhável que você crie primeiro o seguinte:

* [Funcionário](/docs/pt/human-resources/employee)
* [Estrutura salarial](/docs/pt/human-resources/salary-structure)
* [Atribuição de estrutura salarial](/docs/pt/human-resources/salary-structure-assignment)
## 2. Como criar um comprovante de salário

1. Vá para comprovante de salário, clique em Novo.
2. Selecione Funcionário. Ao selecionar Funcionário, todos os detalhes do Funcionário serão obtidos na Estrutura Salarial atribuída a esse Funcionário. Isso inclui detalhes como frequência da folha de pagamento, ganhos, deduções, etc.
3. Selecione a data de início e a data de término.
4. Salvar .

## 3. Recurso

### 3.1. Comprovante de salário com base em frequência/licença

Os usuários de RH podem criar comprovante de salário com base em frequência ou licença. Os dias úteis serão calculados com base nas férias/assiduidade, dependendo do campo **Calcular dias úteis da folha de pagamento com base em** em [Configurações de RH](/docs/pt/human-resources/hr-settings). Se a folha de pagamento for baseada na frequência, então, a **licença sem remuneração** será considerada como ausente e **meio dia** será considerado como meio dia ausente.

### 3.2. Comprovante de Salário baseado em Quadro de Horários

Para criar Comprovante de Salário com base em quadro de horários, você precisa criar uma Estrutura Salarial para Quadros de Horários.

O Frappe HR também oferece uma opção para criar comprovante de salário com base em horas de trabalho. em [Quadro de horas](/docs/pt/projects/timesheets). Você pode criar o comprovante de salário após enviar o quadro de horários clicando diretamente no botão **Criar comprovante de salário** no canto superior direito.

![Criar comprovante de salário com base nos quadros de horários](/files/create-salary-slip-based-on-timesheets.png)![]()

O valor do pagamento é calculado com base na taxa horária definida na estrutura salarial e é refletido na tabela de rendimentos.

### 3.3 Acumulado no ano e Acumulado no mês

Para cada comprovante de salário, 'Acumulado no ano' e 'Acumulado no mês' são computados.

![Acumulado no ano e mês até a data](/files/ytd-and-mtd.png)![]()  


+ **Year to Date**: Salário total registrado para aquele funcionário específico desde o início do ano (período da folha de pagamento ou ano fiscal) até a data de término do comprovante de salário atual.
+ **Até a data do mês**: Salário total registrado para um determinado funcionário desde o início do ano fiscal. mês (para o qual a entrada da folha de pagamento é criada) até a data de término do comprovante de salário atual.

Acumulado no ano também é calculado para cada componente nas tabelas de rendimentos e deduções. O formato de impressão "Recibo de salário com acumulado no ano" está disponível com cálculos acumulados no ano e no acumulado do mês.

![Acumulado no ano para componentes do comprovante de salário](/files/ytd-component.png)![]()  
### 3.4 Recibos de salário em massa por e-mail

Por padrão, a entrada da folha de pagamento envia e-mails de comprovantes de salário para todos os funcionários no envio do comprovante de salário se **Enviar comprovante de salário por e-mail para funcionário** estiver ativado nas configurações da folha de pagamento.

![](/files/2FG61KM.png)![]()  


Mas se houver alguns funcionários que não têm um ID de e-mail definido ou a configuração estiver incorreta durante esta ação, você pode usar a ação em massa na visualização de lista de recibo de salário para acionar o envio de e-mails para funcionários selecionados posteriormente.

![bulk](/files/bulk.png "bulk.png")![]()  


  






