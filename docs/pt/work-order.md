# Ordem de serviço



**Uma Ordem de Serviço é um documento entregue ao chão de fábrica pelo Planejador de Produção como um sinal para fabricar uma determinada quantidade de um determinado Item.**


![Ordem de trabalho](/files/manufacturing-flow-wo.png)


A Ordem de Serviço também ajuda a gerar os requisitos de material (Entrada de Estoque) para o Item a ser produzido a partir de sua **Lista de Materiais**.


A **Ordem de Serviço** pode ser gerada a partir do [Plano de Produção](/docs/pt/manufacturing/production-plan) com base nas Vendas Pedidos.


Para acessar a lista de Ordens de Serviço, acesse:


> Home > Fabricação > Produção > Ordem de Serviço


## 1. Pré-requisitos


Antes de criar e usar uma Ordem de Serviço, é aconselhável criar primeiro o seguinte:


* [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
* [Operação](/docs/pt/manufacturing/operation)
* [Estação de trabalho](/docs/pt/manufacturing/workstation)


## 2. Como criar uma ordem de serviço


1. Vá para a lista de Ordens de Serviço e clique em Novo.
2. Selecione o item a ser fabricado.
3. A lista técnica padrão desse item será obtida pelo sistema. Você também pode alterar a lista técnica.
4. Insira a quantidade a ser fabricada. Os itens de matéria-prima serão obtidos somente quando isso estiver definido.
5. Se a BOM selecionada tiver Operações mencionadas nela, o sistema irá buscar todas as Operações da BOM, esses valores podem ser alterados. Consulte a [seção 3.2](/docs/pt/manufacturing/work-order#32-operations-table) para saber mais.
6. Defina a Data de Início Planejada (uma Data Estimada na qual você deseja que a Produção comece).
![Ordem de trabalho](/files/work-order.png)
7. **Usar BOM multinível**: ativado por padrão. Se você deseja planejar materiais para submontagens do item que você está fabricando, deixe esta opção habilitada. Se você planejar e fabricar as submontagens separadamente, poderá desativar esta caixa de seleção. Para saber mais, visite [esta página](/docs/pt/manufacturing/articles/managing-multi-level-bom).
8. Selecione Armazéns:
	1. **Armazéns de Origem**: Selecione este Armazém na linha Item. O armazém onde você armazena suas matérias-primas. Cada item necessário pode ter um armazém de origem separado. O armazém de grupo também pode ser selecionado como armazém de origem. Após o envio da Ordem de Serviço, as matérias-primas serão reservadas nestes armazéns para utilização na produção.
	2. **Armazém de trabalho em andamento**: O armazém para onde seus itens serão transferidos quando você iniciar a produção. O Armazém de Grupo também pode ser selecionado como um armazém de Trabalho em Andamento.
	3. **Armazém de destino**: o armazém onde você armazena os itens acabados antes de serem enviados.
	4. **Depósito de Sucata**: Se a lista técnica resultar em material de sucata, o Depósito de Sucata precisa ser selecionado.
9. **Itens Obrigatórios**: Todos os itens necessários (matérias-primas) serão obtidos da BOM e preenchidos nesta tabela. Aqui você também pode alterar o Armazém de Origem para qualquer item. E durante a produção, você pode acompanhar as matérias-primas transferidas desta tabela.


> Observação: você pode salvar uma Ordem de Serviço sem selecionar os Armazéns, mas os Armazéns são obrigatórios para enviar uma Ordem de Serviço.


Uma ordem de serviço também pode ser criada diretamente a partir de um [pedido de vendas](/docs/pt/selling/sales-order#214-after-subusing).


### 2.1 Opções adicionais ao criar uma ordem de serviço


* **Pedido de Venda**: Se você criar uma Ordem de Serviço a partir de um Pedido de Venda, ela será buscada aqui. Você também pode vincular uma Ordem de Venda existente que contenha o Item a ser fabricado a esta Ordem de Serviço.
* **Projeto**: vincule a ordem de serviço a um projeto para acompanhar o progresso em casos como do engenheiro ao pedido.
* **Permitir item alternativo**: Às vezes, durante a fabricação de um produto acabado, materiais específicos podem não estar disponíveis. Por exemplo, usando contas de plástico em vez de cristais de plástico. O produto acabado em si poderia ser diferente. Marcar esta caixa de seleção permitirá que você selecione um item alternativo. Para saber mais, visite [esta página](/docs/pt/manufacturing/item-alternative).
* **Ignorar transferência de material para armazém WIP**: Normalmente, uma entrada de estoque é criada quando as matérias-primas são transferidas para um armazém de trabalho em andamento. Neste caso, a matéria-prima é considerada consumida e o Registro de Estoque é ignorado. A próxima opção será mostrada se você marcar esta caixa de seleção.
* **Backflush de matérias-primas do armazém de trabalho em andamento**: Marcar esta caixa de seleção criará automaticamente uma entrada de estoque com o tipo 'Fabricação'. Isso significa que as matérias-primas foram consumidas do Armazém de Origem, utilizadas para fabricar produtos acabados e outra Entrada de Estoque foi criada para o seu Armazém de Destino.
![Opções ao criar WO](/files/work-order-options.png)


## 3. Recursos


### 3,1 Tempo


A data de início planejada e a data de entrega prevista podem ser definidas aqui. O padrão para Data de início planejada é a data e hora atuais no momento da criação da ordem de serviço.


### 3.2 Tabela de itens obrigatórios


O Armazém de Origem pode ser alterado para os itens de matéria-prima usados ​​aqui. O Armazém padrão pode ser definido no nível do Item no [Item](/docs/pt/stock/item#28-item-defaults) mestre ou globalmente no [Configurações de estoque](/docs/pt/stock/stock-settings#23-default-warehouse).


* **Quantidade necessária**: será calculada automaticamente com base na [Lista de materiais](/docs/pt/manufacturing/bill-of-materials).
* **Quantidade transferida**: assim que a ordem de serviço for iniciada e os cartões de trabalho forem executados, os itens serão transferidos do armazém de origem para o armazém de trabalho em andamento. Este campo mostra a quantidade no Armazém WIP. Observe que se você marcar 'Ignorar transferência de material para armazém WIP', esta coluna não será atualizada.
* **Quantidade Consumida**: Quando o Item do Armazém WIP for consumido e o produto acabado for fabricado, este campo será atualizado.
* **Permitir item alternativo**: Se um item específico (matéria-prima ou subconjunto) não estiver disponível, marcar esta caixa de seleção permitirá que você selecione um item alternativo definido na lista Alternativa de item.
* **Ignorar transferência de material**: se você não deseja transferir a matéria-prima específica para o armazém de trabalho em andamento, será necessário ativar esta caixa de seleção.


Depois de desmarcar esta caixa de seleção para um item, você ainda poderá selecioná-lo na BOM e na ordem de serviço, mas nenhuma entrada de estoque será criada para ele.


Depois que a Ordem de Serviço for salva, os dois campos a seguir também mostrarão a disponibilidade nos respectivos Armazéns na tabela Itens Necessários:


* Quantidade disponível no armazém de origem
* Quantidade disponível no armazém WIP


![Quantidade de material WO](/files/work-order-material-qty.png)


### 3.2 Tabela de operações


Os materiais podem ser transferidos mediante uma Ordem de Serviço ou um Cartão de Trabalho. Geralmente, isso é obtido na [lista de materiais](/docs/pt/manufacturing/bill-of-materials), mas você também pode alterá-lo na ordem de serviço. 


O seguinte será obtido da BOM:


* Na tabela Operações: As Estações de Trabalho onde as Operações serão realizadas
![PO Opeartions](/files/PO-Operations.png)
* Na tabela Itens: As operações que serão realizadas nos Itens
![PO reatribuindo operações](/files/PO-reassigning-operations.png)


Esses valores também podem ser alterados.


Depois que a Ordem de Serviço for salva, os seguintes campos serão mostrados:


* **Quantidade concluída**: o número de itens nos quais esta operação foi realizada.
* **Status**: se a operação está pendente, em andamento ou concluída. O status aqui é atualizado quando os cartões de trabalho são atualizados.
* **Tempo de operação**: é obtido na lista técnica, mas pode ser alterado.
* **Custo operacional planejado**: é calculado com base no tempo de operação, taxa horária, quantidade sendo fabricada, etc.


O Tempo Real de Operação, o Custo Operacional Real, o Horário Real de Início e o Horário Real de Término são atualizados quando os Cartões de Trabalho são atualizados.


### 3.3 Custo operacional


Nesta seção, são mostrados os seguintes itens:


* **Custo Operacional Planejado**: É obtido de acordo com a BOM e as Operações nela definidas.
* **Custo Operacional Real**: É obtido dos Cartões de Trabalho com base nas Operações executadas nos Itens.
* **Custo Operacional Adicional**: Quaisquer despesas adicionais que você possa ter incorrido durante a fabricação do Item podem ser adicionadas aqui.
* **Custo operacional total**: é calculado como custo operacional real + custo operacional adicional.


Esses valores são calculados de acordo com os cartões de trabalho.


![Custos operacionais de ordem de serviço](/files/wo-operation-cost.png)


### 3.4 Mais informações


Aqui a descrição do item e a UDM do estoque são mostradas para o item que está sendo fabricado.


Quando uma ordem de serviço é criada a partir de uma [solicitação de material](/docs/pt/stock/material-request), ela será mostrada aqui.
### 3.5 Transferência de materiais para fabricação


* Depois de enviar sua Ordem de Serviço, você precisará Transferir as Matérias-Primas para iniciar o Processo de Fabricação.
* Isso criará uma entrada de estoque com todos os itens necessários para concluir esta ordem de serviço a serem adicionados ao armazém WIP. Isso adicionará os itens da submontagem como estão ou os explodirá para mostrar as matérias-primas, dependendo se você marcou 'Usar lista técnica multinível' ou não.
* Clique em 'Iniciar'. Depois de clicar em Iniciar, os Cartões de Trabalho serão criados para as [Operações](/docs/pt/manufacturing/job-card) envolvidas.


![Transferir materiais](/files/PO-material-transfer.png)
* Mencione a quantidade de materiais a serem transferidos nesta execução.


![Quantidade de transferência de material](/files/PO-material-transfer-qty.png)
* Você será direcionado para uma entrada de estoque para 'Transferência de material para fabricação'. Envie.
* O material transferido para fabricação será atualizado na ordem de serviço com base na entrada de estoque.


![Entrada de estoque para PO](/files/PO-material-transfer-updated.png)


### 3.6 Transferência de materiais por meio de entrada em estoque


Os casos de uso desta opção são:


* Se uma transferência de material for feita em massa e/ou não precisar ser rastreada em relação a uma ordem de serviço específica.
* Se a responsabilidade pela transferência de material e entrada de produção for de dois usuários separados.


Se for esse o caso, você pode marcar a caixa de seleção 'Pular transferência de material', que permitirá fazer a entrada de estoque do tipo 'Fabricação' diretamente clicando no botão 'Concluir'.


### 3.7 Criando cartões de trabalho


* O progresso na ordem de serviço pode ser rastreado usando cartões de trabalho
* Os rascunhos de cartões de trabalho são criados com base no momento em que uma ordem de serviço é enviada.
* Para criar mais Cartões de Trabalho em uma Ordem de Serviço, clique no sinal de mais ao lado do Cartão de Trabalho no painel da Ordem de Serviço.


Para saber mais sobre cartões de trabalho, visite [esta página](/docs/pt/manufacturing/job-card).


### 3.8 Atualizando produtos acabados


* Depois de concluir a Ordem de Serviço, você precisará atualizar os Produtos Acabados.
* Isso criará uma entrada de estoque que deduzirá todos os itens e subconjuntos do Armazém WIP e os adicionará ao Armazém de Produtos Acabados.
* Clique em 'Concluir'.


![Atualizar produtos acabados](/files/PO-FG-update.png)
* Mencione a quantidade de materiais a serem transferidos.


> Dica: você também pode concluir parcialmente uma Ordem de Serviço atualizando o estoque de Produtos Acabados criando uma Entrada de Estoque.


### 3.9 Planejamento de capacidade na ordem de serviço


* Quando uma Ordem de Serviço é enviada, com base na Data de Início Planejada e na disponibilidade das Estações de Trabalho, o sistema agenda todas as operações para a Ordem de Serviço (se a Ordem de Serviço tiver Operações especificadas).
* Rascunhos de registros de tempo também são criados com base nas operações agendadas.


Ao enviar a ordem de serviço, o sistema reservará um slot para cada uma das operações da ordem de serviço em série após a data de início planejada com base na disponibilidade da estação de trabalho. A disponibilidade da estação de trabalho depende dos horários da estação de trabalho, da lista de feriados e se alguma outra operação de ordem de serviço está agendada nesse horário.


Você pode mencionar o número de dias para o sistema tentar agendar as operações nas Configurações de Fabricação. Isso é definido como 30 dias por padrão. Caso a operação exija tempo superior ao slot disponível, o sistema solicitará que você interrompa as operações. Assim que o agendamento for concluído, o sistema criará Registros de Tempo e os salvará. Você pode modificá-los e enviá-los mais tarde.


### 4.0 Interrupção de uma ordem de serviço


Quando você interrompe uma Ordem de Serviço, seu status é alterado para Interrompido, indicando que todo o processo de produção dessa Ordem de Serviço foi interrompido. Porém, antes de interromper a ordem de serviço, o usuário deve certificar-se de que as matérias-primas que foram transferidas para o armazém de Trabalho em Andamento foram devolvidas ou não. Caso o usuário tenha tentado interromper a ordem de serviço sem devolver a matéria-prima, o sistema gerará o erro e não permitirá que o usuário interrompa a ordem de serviço.


Para interromper uma ordem de serviço, clique no botão 'Parar'.


![PO-stop](/files/PO-stop.png)


Você também pode reabrir a ordem de serviço interrompida.


![Reabrir ordem de serviço](/files/reopen-work-order.png)


### 4.1 Devolver materiais não consumidos às lojas do armazém WIP


Se você transferiu materiais extras para o armazém de Trabalho em Andamento e após a conclusão da ordem de serviço deseja devolvê-los ao armazém da Loja. Então você tem que ir para a Ordem de Serviço e clicar em Devolver Componentes. Após esse sistema cria o lançamento de estoque de devolução com o tipo Transferência de Material para Fabricação.


![Componentes de retorno](/files/return-components.png)


Você também pode verificar os componentes devolvidos em relação à ordem de serviço usando o relatório Materiais consumidos da ordem de serviço


![Quantidade de componentes de devolução](/files/work-order-consumed-materials-returned-qty.png)


## 4. Vídeo






## 5. Tópicos Relacionados


1. [Cartão de trabalho](/docs/pt/manufacturing/job-card)
2. [Lista de seleção](/docs/pt/stock/pick-list#22-create-pick-list-from-work-order)





