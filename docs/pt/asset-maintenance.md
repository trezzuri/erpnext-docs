# Manutenção de ativos



**Manutenção de Ativos refere-se a qualquer atividade realizada em Ativos para manter seu desempenho ou condição.**


O ERPNext fornece recursos para rastrear os detalhes de tarefas individuais de manutenção/calibração de um ativo por data, pessoa responsável pela manutenção e data de vencimento da manutenção futura.


Para realizar a Manutenção de Ativos no ERPNext:


1. Ative 'Manutenção necessária' no mestre de ativos.
2. Crie uma equipe de manutenção de ativos.
3. Crie a manutenção de ativos.
4. Um registro de manutenção de ativos é criado.
5. Criar registro de reparo de ativos.


Para acessar a lista Manutenção de Ativos, acesse:
> Home > Ativos > Manutenção > Manutenção de Ativos


## 1. Pré-requisitos


Antes de criar e usar a Manutenção de Ativos, é aconselhável criar primeiro o seguinte:


* [Ativo](/docs/pt/asset/asset) com 'Manutenção necessária' marcada.


![Asset](/files/maintenance-required.png)
* [Equipe de manutenção de ativos](/docs/pt/asset/asset-maintenance-team)


## 2. Como criar Manutenção de Ativos


Para cada ativo, crie um registro de Manutenção de Ativos listando todas as tarefas de manutenção associadas, tipo de manutenção (Manutenção Preventiva ou Calibração), periodicidade, atribuição e data de início e término da manutenção. Com base na data de início e na periodicidade, a próxima data de vencimento é calculada automaticamente e uma tarefa é criada para o responsável.


1. Vá para a lista Manutenção de ativos e clique em Novo.
2. Selecione o recurso.
3. Selecione a equipe de manutenção de ativos.
4. Adicione tarefas de manutenção na tabela.
	1. Defina o status de manutenção como 'Planejado', 'Atrasado' ou 'Cancelado'.
	2. Selecione uma periodicidade para a qual a tarefa precisa ser realizada. A próxima data de vencimento será calculada.
5. Salvar.
6. Depois de salvar, você pode atribuir a tarefa a um usuário.


![Asset](/files/asset-maintenance.png)


Se o item for serializado, o número de série poderá ser inserido.


## 3. Recursos


### 3.1 Tarefas de manutenção


* **Tipo de manutenção**: se esta é uma atividade de manutenção 'Preventiva' ou 'Calibração' para restaurar o funcionamento preciso.
* **Data de início e término**: defina a data de início e a data de término quando a manutenção deve começar e terminar.
* **Última Data de Conclusão**: Se a manutenção não foi realizada na data programada ou antes, a data real da manutenção pode ser registrada aqui.


### 3.2 Manutenção de ativos em ToDo


Ao atribuir a manutenção a um usuário, ela aparecerá na lista de tarefas do usuário.


![Asset](/files/asset-maintenance.png)


## 4. Tópicos Relacionados


1. [Ajuste do valor do ativo](/docs/pt/asset/asset-value-adjustment)
2. [Depreciação de ativos](/docs/pt/asset/asset-depreciation)
3. [Descarte de um ativo](/docs/pt/asset/scrapping-an-asset)



