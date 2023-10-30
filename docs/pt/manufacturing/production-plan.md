# Plano de produção



**Um Plano de Produção auxilia no planejamento da produção e do material dos Itens planejados para fabricação. Esses itens de produção podem ser comprometidos por meio de Pedidos de Vendas (para Clientes) ou Solicitações de Materiais (internamente).**


O Plano de Produção ajuda o usuário a planejar a produção em relação a vários Pedidos de Vendas ou Solicitações de Materiais. Além disso, auxilia no planejamento da aquisição de materiais para o item de matéria-prima, com base na quantidade de produtos acabados a serem fabricados.


Para acessar a lista do Plano de Produção, acesse:


> Home > Fabricação > Produção > Plano de Produção


## 1. Pré-requisitos


Antes de criar e usar um Plano de Produção, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Solicitação de material](/docs/pt/stock/material-request)
* [Ordem de vendas](/docs/pt/selling/sales-order)
* [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
* [Roteamento](/docs/pt/manufacturing/routing)


## 2. Como criar um plano de produção


Conforme mencionado anteriormente, um Plano de Produção pode ser usado para planejar a fabricação de Itens em relação a Pedidos de Vendas ou Solicitações de Materiais.


As etapas comuns são:


1. Vá para a lista Plano de Produção e clique em Novo.
2. Selecione se deseja obter itens de um [Pedido de venda](/docs/pt/selling/sales-order) ou de um [Solicitação de material](/docs/pt/stock/material-request).


Um Plano de Produção também pode ser criado manualmente onde você pode selecionar os Itens a serem fabricados.


### 2.1 Produção contra pedidos de vendas


1. Selecione a opção Pedido de vendas na lista suspensa 'Obter itens de'. O sistema mostrará os filtros, com os quais você poderá puxar os Pedidos de Venda para a produção. Você não precisa usar todos esses filtros se tiver apenas alguns pedidos de vendas em um determinado período.


![Plano de produção buscar itens](/files/pp_fetch_from.png)
2. Clique em Obter pedidos de vendas para buscar pedidos de vendas com base nos filtros acima.


![Filtros de ordem de vendas](/files/sales_order_filter.png)
3. Clique em 'Obter itens para ordem de serviço' para buscar os itens dos pedidos de vendas acima. Somente os itens para os quais uma BOM estiver presente serão buscados.
![Obter itens para plano de produção](/files/get_items_wo.png)
4. Ao expandir uma linha na tabela Itens a Fabricar, você verá uma opção para 'Incluir Itens Explodidos'. Marcar isto inclui matérias-primas dos itens de submontagem no processo de produção.
5. Se "Consolidar Itens" estiver marcado e salvo, os itens com a mesma BOM serão combinados em um único item com a quantidade planejada total combinada.
![Obter itens combinados para plano de produção](/files/get_items_combined_wo.png)


### 2.2 Produção contra solicitações de materiais


1. Selecione a opção Solicitação de material na lista suspensa Obter itens de. O sistema mostrará os filtros, através dos quais poderemos puxar as Solicitações de Materiais para a produção.


![Filtros de solicitação de material](/files/material_request_filter.png)
2. Clique em 'Obter solicitação de material' para buscar solicitações de material com base nos filtros acima.


![Solicitações de materiais](/files/material_requests.png)
3. Clique em Obter itens para ordem de serviço para buscar os itens das solicitações de materiais acima.


![Item de solicitação de material](/files/material_request_items.png)


### 2.3 Buscando itens do subconjunto


Clicar em 'Obter itens de subconjunto' irá buscar itens de subconjunto da lista técnica dos itens de produtos acabados, na tabela acima.
![Obter itens do subconjunto](/files/get-subassembly-items.png)


#### 2.3.1 Itens de subconjunto


O usuário terá a opção de fazer Internamente (Ordem de Trabalho)/Pedido de Compra de Subcontrato/Solicitação de Compra de Material em relação aos itens de Submontagem usando o Tipo de Fabricação. 


![Tipo de fabricação](/private/files/production_plan_sub_assembly.png)


Se o usuário quiser fazer Solicitação de Material para seus itens de Submontagem, bem como para suas Matérias-Primas Finais, ele deverá selecionar o Tipo de Fabricação como "Solicitação de Material" para itens de Submontagem e a seguir deverá clicar no botão " Obter matérias-primas para compra" para buscar itens de submontagem na tabela de itens do plano de solicitação de material.


![Plano de solicitação de material](/private/files/production_plan_material_request_items.png)


#### 2.3.2 Combinando itens de subconjunto


Se houver produtos acabados que compartilhem o mesmo item de subconjunto, os itens de subconjunto poderão ser combinados.
O critério para combinação seria ter o mesmo Item, Armazém, BOM e Tipo de Fabricação.


![Combinar itens da submontagem](/files/consolidate-subassembly-items.png)


Desta forma, uma ordem de serviço comum pode ser feita para criar subconjuntos em massa para vários produtos acabados.


#### 2.3.3 Ignorar itens disponíveis do subconjunto


Se os itens do subconjunto estiverem disponíveis no estoque ou estarão disponíveis no futuro por meio de pedidos de compra ou ordens de serviço abertas e você não quiser fabricá-los, você pode ativar a caixa de seleção "Ignorar itens de subconjunto disponíveis" . Com esta opção as matérias-primas para fabricação dos itens do subconjunto não serão consideradas na solicitação de materiais. 


![Ignorar itens disponíveis do subconjunto](/private/files/skip_available_sub_assembly_items.png)


### 2.4 Planejamento para solicitações de materiais


Clicar no botão 'Obter matéria-prima para compra' irá buscar os itens de matéria-prima necessários na tabela Plano de solicitação de material. Por exemplo, para fabricar 200 bengalas de plattico, você precisa de 100 números de plattico bruto, mas tem apenas 20 em seu armazém. Clicar neste botão adicionará uma linha com 80 na coluna Quantidade necessária.


![Plano de solicitação de material](/private/files/fetch_materials_for_material_request_purchase.png)


Use as seguintes caixas de seleção para realizar determinadas ações:


* **Incluir itens não estocáveis**: Para incluir itens não estocáveis ​​no planejamento de solicitação de material. ou seja, itens para os quais a caixa de seleção 'Manter estoque' está desmarcada. Consulte a [página do item](/docs/pt/stock/item#12-options-when-creating-an-item) para obter mais detalhes.
* **Incluir itens subcontratados**: para adicionar matérias-primas do item subcontratado se a inclusão de itens explodidos estiver desabilitada.
* **Ignorar Quantidade Projetada Existente**: Se habilitado o sistema criará a Solicitação de Material mesmo que o usuário já tenha solicitado ou solicitado os respectivos itens. Por exemplo, se você precisar de 100 quantidades de matéria-prima A e mesmo se já tiver 150, marcar esta caixa de seleção adicionará uma solicitação de 100 quantidades dessa matéria-prima.
* **Para Armazém**: O usuário pode definir o Armazém para o qual deseja criar a solicitação de material. Ao criar Entradas de Estoque durante o processo produtivo, o sistema irá procurar o estoque de matéria-prima neste Armazém.


#### 2.4.1 Baixar plano de solicitação de material


![Baixar plano de solicitação de material](/private/files/download_material_request_plan.png)


Ao clicar no botão “Baixar Plano de Solicitação de Material” o Usuário obterá a planilha Excel com as matérias-primas necessárias para completar este Plano de Produção. O usuário pode selecionar o Armazém para verificar a quantidade disponível no respectivo Armazém. Ao clicar em "Baixar Plano de Solicitação de Material", um pop-up será aberto para selecionar armazéns. Se o usuário quiser executar o plano para vários armazéns, ele poderá selecionar esses armazéns no pop-up para baixar o plano no formato de planilha Excel. A planilha do Excel será semelhante a:


![Plano de solicitação de material](/files/material_request_excel.png)


### 2.5 Após o envio


Após o envio do Plano de Produção, o Usuário tem a opção de fazer Ordens de Serviço para os itens de produção e Solicitações de Materiais para as matérias-primas. Os usuários também podem definir o Status como **Fechado** no Plano de Produção.


![Menu](/private/files/menu_options_for_production_plan.png)


#### 2.5.1 Fechando um plano de produção


Pode haver ocorrências em que um Plano de Produção esteja parcialmente concluído e seja descontinuado. Isso pode acontecer por motivos como:


* Um dos itens foi produzido de forma independente, fora do Plano de Produção.
* Ocorreu uma mudança nos planos e itens pendentes não serão produzidos.


Em casos como esses, os usuários podem definir o status do Plano de Produção como **Fechado**, para que nenhuma nova Ordem de Serviço ou Solicitação de Material seja criada em relação a ele.


![Fechando um plano de produção](/files/production_plan_status.gif)


O mesmo pode ser **reaberto**.


### 2.6 Fazendo ordem de serviço para os itens da submontagem


O usuário terá a opção de fazer Ordem de Serviço/Ordem de Compra de Subcontrato/Solicitação de Material para Compra em relação aos itens de Submontagem usando o Tipo de Fabricação. 


![Tipo de fabricação](/private/files/production_plan_sub_assembly.png)


Se o usuário quiser fazer uma ordem de serviço para itens de submontagem, selecione o tipo de fabricação como interna e envie-a. Após enviar você deve clicar no botão Criar-> Ordem de Serviço/Pedido de Subcontratação


![Ordem de serviço do subconjunto](/private/files/make_wo_for_sub_assembly_items.png)


## 3. Tópicos Relacionados


1. [Ordem de serviço](/docs/pt/manufacturing/work-order)
2. [Cartão de trabalho](/docs/pt/manufacturing/job-card)



