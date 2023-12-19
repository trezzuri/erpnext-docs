# Projeto



**Um projeto é um trabalho planejado projetado para encontrar informações sobre algo, produzir algo novo ou melhorar algo.**


No ERPNext, o gerenciamento de projetos é orientado por tarefas. Você pode criar um projeto e dividi-lo em várias tarefas.


Um projeto tem um escopo amplo e, portanto, pode ser dividido em tarefas. Pense em criar um novo smartphone para o próximo ano como um projeto. Então, coisas como design, prototipagem, teste, entrega, etc. tornam-se tarefas do projeto.


Embora cada tarefa dentro de um projeto possa ser atribuída a um indivíduo ou a um grupo de indivíduos, a atribuição também pode ser feita no nível do projeto.


Essas tarefas podem ser criadas a partir do próprio projeto ou uma [tarefa](/docs/pt/projects/tasks.html) também pode ser criada separadamente.


Para acessar Projetos, acesse:


> Home > Projetos > Projetos > Projeto


![Project](/files/projects-project-intro7cb73c.png)


## 1. Como criar um projeto


1. Vá para a lista de projetos e clique em Novo.
2. Adicione os seguintes detalhes:
	* **Nome do Projeto**: Título do Projeto.
	* **Status**: O status padrão de um projeto será 'Aberto', que pode ser alterado posteriormente para 'Concluído' ou 'Cancelado'.
	* **Data de término prevista**: insira a data em que você pretende terminar o projeto.
3. Salvar.


### 1.1 Opções adicionais ao criar um projeto


1. **Do modelo**: se você tiver um [Modelo de projeto](/docs/pt/projects/project-template) existente, poderá escolha criar seu projeto usando este modelo.
2. **Data de início prevista**: se você tiver um cronograma fixo para o projeto, poderá definir a data de início esperada e a data de término prevista no formulário.
3. **Tipo de projeto**: você pode classificar seus projetos em diferentes [tipos](/docs/pt/projects/project-type), por exemplo, , Interno ou Externo.
4. **Prioridade**: você pode selecionar o nível de prioridade do projeto com base em quão crucial ele é. Você também pode adicionar mais níveis de prioridade.
5. **Departamento**: se o projeto pertence ou é propriedade de um [Departamento](/docs/pt/human-resources/department) na organização, você pode adicionar isso aqui.
6. **Está ativo**: uma guia Sim/Não, que permite alterar o status ativo do projeto em qualquer estágio posterior.
7. **Método de conclusão**: você pode acompanhar a% de conclusão do seu projeto com base em um dos três métodos, viz. **Manual, conclusão da tarefa, progresso da tarefa e peso da tarefa**.


![Projeto 2](/files/project-proj.png)


Alguns exemplos de como a porcentagem de conclusão é calculada com base nas tarefas:



| Projeto | Atividade | % Progresso | Peso | Status |
| --- | --- | --- | --- | --- |

| SC001 | Construir | 100 | 0,4 | Concluído |

| SC001 | Operar | 100 | 0,2 | Concluído |

| SC001 | Transferir | 50 | 0,2 | Abrir |





| Método | Fórmula | Cálculo | % tarefa concluída |
| --- | --- | --- | --- |

| **Manual** | - | - | Manual |

| **Conclusão da tarefa** | Tarefa concluída/Número total. de tarefas | 2/3 | 66,66 |

| **Progresso da tarefa** | Soma da % de progresso de todas as tarefas/Número total de tarefas | (100+100+50)/3 | 83,33 |

| **Peso da tarefa** | Soma de (peso da tarefa +% de progresso) | (0,4 \* 100 + 0,2 \* 100 + 0,2 \* 100) | 70 |


**Observação:** Se o peso total das Tarefas não for 100, o resultado calculado será dividido pelo peso total.
Por exemplo, se o total dos pesos das tarefas for 70, então a porcentagem concluída = (70/0,8)% = 87,5%.


## 2. Recursos


### 2.1. Detalhes do cliente, usuários e notas


* **Cliente**: Se um Projeto estiver sendo realizado para um determinado Cliente, os detalhes podem ser inseridos aqui.
* **Pedido de vendas**: se um projeto for baseado em um [Pedido de vendas](/docs/pt/selling/sales-order) de um Cliente, você pode obter os detalhes aqui. Isso permitiria que você atualizasse o Cliente sobre o Progresso do projeto de acordo com o Pedido de Venda emitido.
* **Usuários**: você pode adicionar qualquer  [usuário do site](/docs/pt/setting-up/users-and-permissions/adding-users) para dar acesso a este projeto. Por exemplo, você pode adicionar seu cliente como usuário do site, para permitir que ele tenha acesso ao seu projeto para monitorar o progresso e/ou dar sugestões/comentários. Da mesma forma, um Fornecedor ou Funcionário Contratual/Freelancer envolvido no Projeto pode ser adicionado como Usuário.


Além disso, você também pode expandir a janela e selecionar se deseja enviar um e-mail de boas-vindas a qualquer usuário específico ou conceder-lhe direitos de visualização de anexos.


Você pode saber mais sobre como permitir que os usuários visualizem projetos [aqui](/docs/pt/projects/project-customer-portal).
* **Notas**: você pode adicionar notas adicionais ao projeto.


![Projeto-Custeio](/files/projects-customer-users-notes.png)


### 2.2. Datas de início e término


* **Data de início real**: Com base no início real do projeto, rastreado por meio de planilhas de horas, a data e hora de início reais do projeto serão registradas automaticamente.
* **Data de término real**: Com base no término real do projeto, rastreado pela última atualização do quadro de horários, a data e hora de término reais do projeto serão registradas automaticamente. Para saber mais sobre quadros de horários, [clique aqui](/docs/pt/projects/timesheets/).


![Projeto-Custeio](/files/projects-start-time-end-time.png)


### 2.3. Custeio e Faturamento


* **Custo estimado**: insira o custo estimado do projeto.
* **Valor total de vendas**: se você já vinculou o projeto a um pedido de vendas, o valor total do pedido de vendas será preenchido automaticamente aqui.
* **Valor total do custo**: O sistema irá buscar automaticamente o Valor total do custo de todos os quadros de horários vinculados a este projeto.
* **Valor total faturável**: O sistema irá buscar automaticamente o Valor total faturável de todos os quadros de horários vinculados a este projeto.
* **Declaração de despesas totais**: com base nas despesas declaradas por um [Funcionário](/docs/pt/human-resources/employee) para após a conclusão do Projeto, o Relatório de Despesas Total será calculado automaticamente.
* **Valor total faturado**: o valor total faturado é preenchido automaticamente no sistema usando a fatura de vendas criada em relação ao pedido de vendas.
* **Custo total de compra**: O custo total de compra de um projeto é o custo obtido das faturas de compra criadas em relação a um pedido de compra emitido para fornecimento de materiais necessários para um projeto.
* **Custo total do material consumido**: Usando a entrada de estoque feita de acordo com a necessidade de materiais no projeto, o custo total do material consumido é capturado.


### 2.4. Margem


* **Margem bruta**: a margem bruta lhe dará a margem que você tem entre o valor total do custo e o valor total faturado.


**Margem bruta = (Valor total de vendas + Valor total faturável)-Valor total de custos + Valor total faturável + Declaração de despesas total + Custo total de compra + Custo total de material consumido)**
* **% bruta**: a porcentagem do valor total faturado gasto no valor total do custo representa a% bruta.


**((Valor total de vendas + Valor total faturável)-Valor total de custos + Valor total faturável + Declaração de despesas total + Custo total de compra + Custo total de material consumido)/Valor total de vendas)\* 100**


![Projeto-Custeio](/files/projects-costing-and-billing.png)


### 2.5. Monitore o progresso


Ao ativar a opção 'Coletar progresso' marcando a caixa, você poderá adicionar detalhes de monitoramento ao projeto. Um relatório sobre o andamento do projeto será enviado a todas as partes interessadas do projeto.


* **Lista de feriados**: você pode selecionar a [Lista de feriados](/docs/pt/human-resources/holiday-list) para sua empresa. Isso permitirá que você colete os Relatórios de Progresso apenas nos Dias Úteis.
* **Frequência**: você pode definir a frequência com que deseja obter os relatórios. Pode ser definido para uma frequência horária, duas vezes ao dia, diariamente ou semanalmente.


![Projeto-Custeio](/files/projects-monitor-progress.png)


## 3. Tópicos Relacionados


1. [Tarefa](/docs/pt/projects/tasks)
2. [Tipo de projeto](/docs/pt/projects/project-type)
3. [Modelo de projeto](/docs/pt/projects/project-template)



