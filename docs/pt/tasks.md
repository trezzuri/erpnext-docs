# Tarefas



**No gerenciamento de projetos, uma tarefa é uma unidade ou atividade acionável que precisa ser concluída.**


![Task](/files/projects-task.png)


Para acessar Tarefas, vá para


> Home > Projetos > Projetos > Tarefa


## 1. Como criar uma tarefa


1. Vá para a Lista de Tarefas e clique em Novo.
2. Adicione o assunto da tarefa.
3. Salvar.


![Task](/files/projects-task-creation-main.gif)


Como alternativa, uma tarefa também pode ser criada a partir de um projeto da seguinte maneira:


1. Vá para o projeto para o qual deseja criar uma nova tarefa.
2. Vá para Tarefa na seção Projeto no Painel. O ícone de adição '+' aqui direciona você para a página de criação de tarefas.
3. Adicione o assunto da tarefa.
4. Salvar.


![Task](/files/projects-task-creation.gif)


### 1.1 Opções adicionais ao criar um projeto


Os seguintes detalhes adicionais podem ser adicionados ao editar uma nova tarefa:


* **Status**: Você pode adicionar o status do projeto ou alterá-lo sempre que necessário, por exemplo, de 'Aberto' para 'Em funcionamento', 'Atrasado','Revisão pendente','Concluído' ou 'Cancelado'
* **Projeto**: Caso uma tarefa seja adicionada de forma independente, você pode optar por vincular a tarefa a um Projeto específico. Se a tarefa for criada a partir de um projeto, os detalhes do projeto serão adicionados automaticamente.
* **Prioridade**: Você pode escolher definir a prioridade da tarefa, ou seja, Baixa, Média, Alta ou Urgente.
* **Problema**: se a tarefa for algo acionável que surge de um problema, esse problema pode ser marcado aqui com a Tarefa.
* **Peso**: Se uma tarefa específica tiver algum peso fora de um projeto, ou não, o peso pode ser especificado aqui. Essa ponderação é calculada no método Porcentagem de conclusão da tarefa por peso da tarefa.
* **Tipo**: Se sua tarefa puder ser definida em um tipo de tarefa específico, por exemplo, Treinamento de usuário ou Demonstração de usuário, você poderá inserir o tipo de tarefa aqui. Ele pode ser usado para filtrar as tarefas com base nos tipos de tarefas.
* **Cor**: Cada tarefa pode ser reconhecida por uma cor diferente. Isso ajuda a identificar uma tarefa durante a criação de gráficos de Gantt.
* **É grupo**: esta caixa pode ser marcada para indicar que uma tarefa é uma tarefa pai e pode ser dividida em várias subtarefas.
* **É modelo**: Esta caixa pode ser marcada para indicar que esta tarefa é uma tarefa modelo e deve ser usada em um modelo de projeto.
* **Tarefa pai**: se uma tarefa específica fizer parte de uma tarefa de grupo, a tarefa pai poderá ser vinculada à tarefa neste campo.


![Task](/files/project-task.png)


## 2. Recursos


### 2.1. Cronograma e detalhes


* **Data de início prevista**: você pode inserir a data em que espera que a tarefa seja iniciada.
* **Data de término prevista**: você pode inserir a data em que espera que esta tarefa seja concluída.
* **Tempo esperado**: você pode inserir o número de horas que espera que sejam gastas nesta tarefa.
* **Progresso**: você pode inserir a porcentagem de progresso de uma tarefa.
* **Início**: Se a tarefa for uma tarefa modelo, este campo pode ser usado para especificar o dia em que esta tarefa deve começar após o início do projeto.
* **Duração**: se a tarefa for uma tarefa modelo, este campo poderá ser usado para atribuir um número específico de dias a esta tarefa.
* **É Marco**: Esta caixa pode ser marcada nos casos em que uma determinada tarefa é um Marco em um Projeto.
* **Descrição**: você pode adicionar uma descrição da tarefa aqui.


**Observação**: com base nos valores dos campos **Início** e **Duração**, a **Data de início esperada** e **Data de término esperada** é calculada para tarefas de projeto criadas usando modelo de projeto. Este cálculo ignora feriados com base na lista de feriados da sua empresa.


![Task](/files/projects-task-timeline.png)


### 2.2. Dependências e tempo real


* **Tarefas Dependentes**: Tarefas Dependentes indicam que uma tarefa específica depende de outra tarefa e a primeira não pode ser concluída antes da conclusão da segunda.


As dependências das tarefas podem ser visualizadas nos gráficos de Gantt da seguinte maneira.


![Task](/files/projects-task-gantt.png)
* **Data de início real**: a data e hora reais em que a tarefa é iniciada são registradas com base em [planilhas de horas](/docs/pt/projects/planilhas de horas/).
* **Data de término real**: a data e hora reais em que a tarefa foi concluída são registradas aqui por meio dos Quadros de Horários.


![Task](/files/projects-task-dependencies.png)


### 2.3. Custo


* **Valor total do custo**: o valor total do custo é capturado aqui por meio dos quadros de horários enviados pelo usuário enquanto trabalha nesta tarefa.
* **Valor total de cobrança**: o valor total com o qual o [Cliente](/docs/pt/CRM/customer) será cobrado através desta tarefa é registrado aqui nas planilhas de horas.
* **Relatório de despesas totais**: o valor total das despesas reivindicadas por um funcionário para a conclusão desta tarefa é registrado e refletido aqui.


### 2.4. Mais informações


* **Departamento**: você pode inserir o Departamento Proprietário da tarefa. Independentemente do departamento Proprietário do Projeto, cada tarefa pode ser realizada por um departamento diferente.
* **Empresa**: Você pode alterar a Empresa para a qual esta Tarefa está sendo realizada. Isso pode ser usado nos casos em que uma empresa esteja executando a Tarefa para sua Empresa Irmã, sua Empresa Controladora ou uma Subsidiária.


![Task](/files/projects-task-costing.png)


## 3. Vídeo






## 4. Tópicos Relacionados


1. [Projeto](/docs/pt/projects/project)
2. [Quadro de horas](/docs/pt/projects/timesheets)



