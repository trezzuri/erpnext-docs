# Quadro de horários



**Um quadro de horários é o registro do número de horas gastas por um funcionário na conclusão de cada tarefa.**


O quadro de horários também pode ser usado para calcular o valor faturável de um funcionário, para calcular seus salários ou para monitorar a contribuição de um funcionário para um projeto ou tarefa.


No ERPNext, um Quadro de Horários pode ter uma conta de um determinado funcionário trabalhando em múltiplas Tarefas ou Projetos em formato tabular.


![Timesheet](/files/projects-timesheet.png)


Para acessar o Quadro de Horários, acesse,


> Página inicial > Projetos > Controle de tempo > Quadro de horários


## 1. Como criar um quadro de horários


1. Vá para a lista de quadro de horários e clique em Novo.
2. Insira o nome da empresa e o código do funcionário.
3. Adicione os seguintes detalhes ao campo 'Folhas de ponto'.
	* **Tipo de atividade**: adicione o tipo de atividade para a qual a planilha de horas foi criada.
	* **Hora inicial**: insira a data e a hora em que o trabalho foi iniciado.
	* **Horas**: Insira o número de horas para as quais esta planilha de horas foi criada. Um quadro de horários também pode ser usado para monitorar as horas de trabalho em vários dias.
	* **Projeto**: se esta planilha de horas precisar ser marcada para um projeto específico, você poderá adicionar o nome do projeto aqui.
	* **Fatura**: esta caixa precisa ser marcada se esta planilha de horas específica for faturável.
4. Clique em 'Adicionar linha' para adicionar mais planilhas de horas.
5. Salvar.
6. Após salvar o Quadro de Horários, de acordo com os dados inseridos nas diferentes Planilhas de Horários, a Data de Início, a Data de Término e o Total de Horas de Trabalho serão atualizados automaticamente. Clique em Enviar.


### 1.1. Alternativamente, um quadro de horários também pode ser criado a partir de uma tarefa da seguinte maneira:


1. Vá para a tarefa para a qual deseja criar um novo quadro de horários.
2. Vá para 'Quadro de Horários' na seção Atividade no Painel. O ícone de adição '+' aqui redirecionaria você para a página de criação do quadro de horários.
3. Siga as etapas para criar uma planilha de horas.


![Timesheet](/files/projects-timesheet-from-task.gif)


### 1.2. Cronômetro no quadro de horários


**Um cronômetro pode ser usado para registrar o tempo real gasto por um funcionário para concluir uma atividade específica em um quadro de horários.**


#### 1.2.1. Etapas para iniciar um cronômetro:


* Em um quadro de horários Ao clicar em **Iniciar cronômetro**, uma caixa de diálogo será exibida e você deverá inserir os seguintes detalhes:
	+ **Tipo de atividade**: a atividade para a qual você está registrando o tempo.
	+ **Projeto**: o projeto para o qual você está criando o quadro de horários.
	+ **Tarefa**: a tarefa para a qual você está registrando o tempo no quadro de horários.
	+ **Horas esperadas**: insira o número de horas em que você espera que a tarefa termine.


![Temporizador em andamento](/files/projects-timer-in-timesheet.gif)


* Depois de concluir a tarefa, clique em Concluir. Uma nova entrada será criada no Quadro de Horários, e o tempo será registrado como um Quadro de Horários na Tabela de Quadros de Horários no Quadro de Horários.
* Se o tempo exceder as 'Horas esperadas', uma caixa de alerta será exibida.


![Temporizador excedido](/files/projects-timer-time-exceed.png)


### 1.3. Opções adicionais ao criar o quadro de horários


A planilha de horas, quando expandida, permite que você insira os seguintes detalhes:


* **Horário esperado**: insira o tempo provisório necessário para concluir as tarefas nas planilhas de horas.
* **Hora final**: insira a data e a hora em que o trabalho foi concluído.
* **Concluído**: Esta caixa precisa ser marcada se a Tarefa foi concluída durante o envio do Quadro de Horários.
* **Tarefa**: se esta planilha de horas precisar ser marcada para uma tarefa específica, você poderá fazê-lo aqui.
* **Horas de faturamento**: o número de horas pelas quais o cliente precisa ser cobrado por este quadro de horários.
* **Taxa de faturamento**: a taxa pela qual o cliente precisa ser cobrado por este trabalho.
* **Taxa de Custo**: Este é o custo real do trabalho realizado. É obtido do custo da atividade (por funcionário) ou do tipo de atividade e pode ser editado.
* **Valor da cobrança**: o valor da cobrança é calculado automaticamente com base no número de horas faturáveis ​​e na taxa de cobrança.
* **Valor do custo**: o valor do custo é calculado automaticamente com base no número de horas e na taxa de custo.


![Timesheet](/files/projects-time-sheet-expansion.png)


## 2. Recursos


### 2.1 Detalhes de cobrança


* **Total de horas faturáveis**: com base no quadro de horários, o total de horas faturáveis ​​será obtido automaticamente aqui.
* **Valor total faturável**: com base no quadro de horários, o valor total faturável será obtido automaticamente aqui.
* **Total de horas faturadas**: assim que o quadro de horários for enviado, você terá a opção de criar uma fatura de vendas a partir do quadro de horários. O número de horas pelas quais o Cliente será cobrado será obtido aqui e, uma vez enviada a Fatura de Venda, será obtido o Total de Horas Faturadas.
* **Valor total faturado**: de maneira semelhante à forma como o total de horas faturadas é obtido, o valor total faturado também será obtido.
* **Valor total do custo**: com base no quadro de horários, o valor total do custo, conforme especificado pelo funcionário, é marcado aqui.
* **% do valor faturado**: assim que o quadro de horários for enviado e um [vendas A fatura](/docs/pt/projects/sales-invoice-from-timesheet) é criada a partir do quadro de horários, a porcentagem do valor do valor total faturável que foi calculado para o valor total faturado é calculada e refletida aqui.


![Timesheet](/files/projects-timesheet-billing-details.png)


## 3. Depois de salvar a planilha de horas


Depois que um quadro de horários for salvo e enviado, os detalhes como taxa de faturamento e taxa de custo serão bloqueados e não poderão ser alterados. Os seguintes DocTypes podem ser criados após o envio de um Quadro de Horários.


* [Fatura de vendas](/docs/pt/projects/sales-invoice-from-timesheet)
* [Recibo de salário](/docs/pt/projects/salary-slip-from-timesheet)



