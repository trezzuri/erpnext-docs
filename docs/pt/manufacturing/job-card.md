# Cartão de trabalho



**Um Cartão de Trabalho armazena informações reais de produção sobre uma Operação específica executada em uma Estação de Trabalho específica.**


Um Cartão de Trabalho é criado a partir da Ordem de Serviço e entregue a cada uma das Estações de Trabalho no chão de fábrica para iniciar a produção de um item com uma determinada quantidade em cada uma das operações definidas na Ordem de Serviço.


O Cartão de Trabalho permite que a estação de trabalho de cada Operação emita uma “Solicitação de Material” e uma “Transferência de Estoque para Fabricação” para a matéria-prima necessária em um “Cartão de Trabalho”.


A conclusão do Cartão de Trabalho alterará o status da produção na Ordem de Serviço. Podemos acompanhar a conclusão do progresso da produção para cada uma das Operações definidas na Ordem de Serviço.


![Ordem de serviço](/files/manufacturing-flow-jc.png)


Para acessar a lista de Cartões de Trabalho, acesse:
> Home > Fabricação > Produção > Cartão de Trabalho


## 1. Pré-requisitos


Antes de criar e usar um Cartão de Trabalho, é aconselhável criar primeiro o seguinte:


* [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
* [Operação](/docs/pt/manufacturing/operation)
* [Estação de trabalho](/docs/pt/manufacturing/workstation)
* [Ordem de serviço](/docs/pt/manufacturing/work-order)


## 2. Como criar um cartão de trabalho


O Cartão de Trabalho para Operações é criado automaticamente quando uma Ordem de Serviço é enviada.


Esta é a aparência de um cartão de trabalho:


![Cartão de trabalho](/files/job-card.png)


Para usar um cartão de trabalho, siga estas etapas:


1. Clique no botão Iniciar trabalho e, em seguida, em Concluir trabalho quando terminar.
2. Como alternativa, você também pode preencher o horário inicial e o horário final na tabela de registros de tempo.
3. Selecione o Funcionário ao qual o Cartão de Cargo foi atribuído.
4. Insira a quantidade concluída. Este é o número de itens nos quais a operação foi realizada no intervalo de tempo selecionado.
5. Adicione mais linhas na tabela Registros de tempo e registre o tempo usando os botões Iniciar/Concluído.
6. Clique em Enviar.


Em uma Ordem de Serviço, as Operações e Estações de Trabalho são obtidas da BOM de um Item. Para facilitar o uso, você deve garantir que o [Roteamento](/docs/pt/manufacturing/routing) esteja configurado na BOM.


Cada cartão de trabalho criado terá estações de trabalho e operações atribuídas. A matéria-prima necessária de cada Armazém de Origem será calculada com base na quantidade necessária para produção.


Ao enviar uma Ordem de Serviço, os Cartões de Trabalho serão criados automaticamente com base nos valores da tabela Operações.


![Criar Acionista](/files/work-order-job-card-creation.gif)


### 2.1 Selecionar ordem de serviço com item a fabricar


Você pode selecionar 'Transferir material contra' como 'Cartão de trabalho' na lista de materiais para transferir matérias-primas para produção em relação aos cartões de trabalho.


Na Ordem de Serviço, você pode selecionar a opção:


![Criar Acionista](/files/work-order-transfer-against-job-card.png)


### 2.3 Usando um cartão de trabalho


A atribuição do funcionário e os detalhes do horário também serão definidos no Cartão de Trabalho. O tempo necessário para realizar um trabalho pode ser registrado. Se vários funcionários estiverem trabalhando na mesma operação, adicione novos cartões de cargo clicando no botão 'Criar cargo'.


![Criar Acionista](/files/job-card-form.png)


### 2.4 Solicitação de material contra cartão de trabalho


Uma Solicitação de Material será gerada a partir do Cartão de Trabalho como base/pedido para preparar a matéria-prima necessária para o processo de fabricação. A Solicitação de Material levantada terá sua referência ao número original da Carteira de Trabalho.


![Criar Acionista](/files/material-request-against-job-card.png)


Acompanhe o progresso da fabricação na ordem de serviço até a conclusão de cada operação definida na ordem de serviço.


A conclusão do Cartão de Trabalho permite acompanhar o progresso da fabricação dentro da Ordem de Serviço, observando a conclusão de cada Operação relacionada à Ordem de Serviço.


![Conclusão do cartão de trabalho da ordem de trabalho](/files/work-order-job-card-completion.png)


### 2,5 itens de sucata


Ao completar as operações, pode haver chances de que alguns materiais de sucata sejam produzidos. Esses materiais de sucata devem ser adicionados ao inventário. Para isso o usuário precisa colocar os detalhes dos itens sucateados no cartão de trabalho. O usuário também pode definir os materiais defeituosos/materiais quebrados na tabela de itens descartados.


![Conclusão do cartão de trabalho da ordem de trabalho](/files/job_card_scrap_item.png)


## 3. Recursos


### 3.1 Acompanhamento da inspeção de qualidade


> Introduzido na versão 13


Para ordens de produção, a qualidade dos produtos em processo (semiacabados) também precisa ser rastreada. É definido pelo processo (operação) realizado nele, que por sua vez é definido no Cartão de Trabalho. Os testes em processo são diferentes dos testes de materiais de entrada e saída. O monitoramento da qualidade durante a fabricação ajuda a garantir que o produto acabado produzido tenha a qualidade desejada. Você pode criar uma inspeção de qualidade para o item de produção em relação ao cartão de trabalho.


![Inspeção de qualidade no cartão de trabalho](/files/qi-against-job-card.png)
![Link de inspeção de qualidade no cartão de trabalho](/files/qi-link-in-job-card.png)


Para obter mais detalhes, consulte a página [Inspeção de qualidade](/docs/pt/stock/quality-inspection).



