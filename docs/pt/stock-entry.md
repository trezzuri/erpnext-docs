# Entrada de estoque



**Uma entrada de estoque permite registrar a movimentação de itens entre armazéns.**


Para acessar a lista de entrada de estoque, acesse:
> Home > Estoque > Transações de estoque > Entrada de estoque


As inscrições em estoque podem ser feitas para os seguintes fins:


* **Problema Material**: Se o material estiver sendo emitido para alguém dentro ou fora da empresa (Material de Saída). Os Itens serão deduzidos do Armazém definido no Armazém de Origem.
* **Recebimento de Material**: Se o material está sendo recebido (Material Recebido). Os itens serão adicionados ao Armazém definido em Armazém de Destino.
* **Transferência de material**: se o material estiver sendo movido de um armazém interno para outro.
* **Transferência de material para fabricação**: se as matérias-primas estão sendo transferidas para fabricação. A transferência pode acontecer em relação a uma [Ordem de Serviço](/docs/pt/manufacturing/work-order) ou a uma [Cartão de trabalho](/docs/pt/manufacturing/job-card). Para saber mais, visite a página [Lista de materiais](/docs/pt/manufacturing/bill-of-materials).
* **Consumo de material para fabricação**: Pode haver diversas entradas de estoque de consumo em uma ordem de serviço de fabricação. [Consulte este link para obter mais detalhes](/docs/pt/manufacturing/articles/material_consumption)
* **Fabricação**: se o Material estiver sendo recebido de uma Operação de Fabricação/Produção.
* **Reembalar**: se os itens originais estiverem sendo reembalados em novos itens.
* **Enviar ao Subcontratado**: Se o Material estiver sendo emitido para uma atividade de subcontrato. Esta entrada é feita a partir de um Pedido de Compra. Para saber mais, visite a página [subcontratação](/docs/pt/manufacturing/subcontracting).


Para saber mais detalhes sobre os tipos de entrada de ações, [visite esta página](/docs/pt/stock/articles/stock-entry-purpose).


## 1. Pré-requisitos


Antes de criar e usar uma entrada de estoque, é aconselhável criar primeiro o seguinte:


* [Armazém](/docs/pt/stock/warehouse)
* [Item](/docs/pt/stock/item)


## 2. Como criar uma entrada de estoque


As entradas de estoque para fins de fabricação geralmente são criadas a partir de uma [Ordem de serviço](/docs/pt/manufacturing/work-order). Para criar uma entrada de estoque manualmente para outros fins, siga estas etapas:


1. Vá para a lista de entrada de estoque e clique em Novo.
2. Selecione a finalidade de entrada de estoque entre as listadas acima.
3. Se você definir os armazéns de origem ou de destino padrão, eles serão preenchidos automaticamente nas linhas da tabela Itens.
4. Os armazéns de origem/destino estarão disponíveis de acordo com a finalidade de entrada de estoque selecionada.
5. Selecione Itens e insira uma quantidade.
6. A taxa batica será obtida e o valor será calculado automaticamente.
7. Salvar e enviar.


![Entrada de estoque](/files/stock-entry.png)


Normalmente, "Source Warehouse" e "Target Warehouse" estão configurados para registrar um movimento.


### 2.1 Opções adicionais ao criar uma entrada de estoque


* **Ordem de Serviço**: Se esta for uma entrada de Fabricação, a Ordem de Serviço será mostrada neste campo.
* **Editar data e hora de lançamento**: permitirá que você edite a data e hora da entrada de estoque.
* **Inspeção necessária**: se uma [Inspeção de qualidade](/docs/pt/stock/quality-inspection) precisar ser realizada no Itens antes de enviar a entrada de estoque.
* **Da BOM**: Se esta for uma entrada de Fabricação, a BOM associada ao Item que está sendo fabricado será mostrada.


### 2.2 Tipo de entrada de estoque


Você também pode criar um Tipo de Entrada de Estoque onde apenas o nome será diferente, por exemplo 'Entrada de Sucata'. O objetivo será Transferência de Material mas o nome será diferente. Isto é útil se você deseja que determinados usuários tenham acesso apenas a ações específicas relacionadas ao estoque.


![Tipo de entrada de estoque](/files/stock-entry-type.png)


## 3. Recursos


### 3.1 A tabela de itens


Detalhes sobre o item, taxa, quantidade, etc. serão mostrados aqui.


Marcar 'Permitir Taxa de Avaliação Zero' permitirá o envio do Recibo de Compra mesmo que a Taxa de Avaliação do Item seja 0. Este pode ser um item de amostra ou devido a um entendimento mútuo com seu Fornecedor.


Diferentes armazéns de origem e destino podem ser definidos para diferentes itens.


![Entrada de estoque](/files/stock_entry_item.png)


### 3.2 Sucata e perda de processo


* **Item de sucata**: Itens de sucata são subprodutos e podem ser tratados como produtos. Os itens de sucata terão a taxa de valorização e serão adicionados ao depósito de sucata. Os usuários podem definir a taxa de avaliação para o item sucateado manualmente no campo Taxa batica.
* **Perda de Processo**: A perda de processo não tem impacto no estoque, isso reduzirá o número de itens FG.
Confira a imagem abaixo, o usuário planejou produzir 100 Itens FG, mas após o processo de fabricação, a quantidade foi produzida como 80. Para produzir 80 Itens FG, o usuário utilizou toda a quantidade de matéria-prima. Portanto, aqui 20 quantidades foram produzidas e, portanto, o sistema marcou-a como Quantidade de perda de processo.
O custo de perda de processo de 20 quantidades foi adicionado às 80 quantidades do Item FG.


![Entrada de estoque](/files/ste_manufacture_process_loss.png)


### 3.3 Custos Adicionais


Se a entrada de estoque for uma entrada de entrada, ou seja, qualquer item estiver sendo recebido em um armazém de destino, você poderá adicionar custos adicionais relacionados (como despesas de envio, taxas alfandegárias, custos operacionais, etc.) associados ao processo. Os custos adicionais serão considerados para cálculo da Taxa de Avaliação dos itens.


Para adicionar custos adicionais:


1. Selecione a conta de despesas na qual as despesas desta entrada de estoque serão registradas.
2. Insira a descrição e o valor do custo na tabela Custos Adicionais.


![Custos adicionais de entrada de estoque](/files/additional-costs-table.png)


Os Custos Adicionais adicionados serão distribuídos entre os itens recebidos (onde o Armazém Alvo mencionado) proporcionalmente com base no Valor Batico dos itens. E o custo adicional distribuído será adicionado à taxa batica do item, para calcular a Taxa de Avaliação.


Quantidade e Taxa são mostradas a seguir quando você expande a tabela Itens.
![Taxa de avaliação do item de entrada de estoque](/files/stock-entry-item-valuation-rate.png)


### 3.4 Dimensões contábeis


Você pode marcar transações diferentes com base em dimensões diferentes. Por padrão, [Projetos](/docs/pt/projects/project) pode ser considerado como uma dimensão, pois é uma prática comum rastrear custos de diferentes projetos. Para saber mais sobre dimensões contábeis, [visite esta página](/docs/pt/accounts/accounting-dimensions).


### 3.5 Configurações de impressão


#### Papel timbrado


Você pode imprimir seu recibo de compra em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


#### Imprimir títulos


Os títulos do recibo de compra também podem ser alterados durante a impressão do documento. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


### 3.6 Mais informações


* **Está Abrindo**: Se esta entrada for a entrada de estoque inicial para os Itens.
* **Observações**: Quaisquer observações adicionais sobre o Item.
* **Porcentagem Transferida**: A porcentagem de Itens transferidos dependendo da finalidade da Entrada em Estoque.
* **Valor total**: o valor total de itens transferidos.


### 3.7 Inventário perpétuo


Se o sistema de inventário permanente estiver ativado, os custos adicionais serão contabilizados na Conta de Despesas mencionada na tabela Custos Adicionais.


![Contábil Geral de Custos Adicionais](/files/stock-entry-additional-cost.png)
![Contábil Geral de Custos Adicionais](/files/additional-costs-general-ledger.png)


### 3.8 Após o envio


Depois de enviar uma entrada de estoque, você pode acessar o razão de estoque ou o razão contábil no painel.


![Conta geral de custos adicionais](/files/stock-entry-submit.png)


## 4. Adicionar ao transporte público


Se você deseja transferir materiais de um armazém para outro e deseja fazer duas entradas para isso, use o recurso "Adicionar ao trânsito".


Para utilizar o recurso "Adicionar ao Trânsito", faça o lançamento do estoque com o tipo "Transferência de Material" e marque a caixa de seleção "Adicionar ao Trânsito". A seguir você precisa selecionar o armazém de origem de onde deseja emitir o material e a seguir selecionar o armazém do tipo “Trânsito” no armazém de destino. Para fazer armazém de trânsito você pode ir ao mestre de armazém e selecionar o tipo de armazém como "Trânsito". Depois disso, adicione os itens na entrada de estoque que precisam ser transferidos e envie-os.


![Adicionar ao transporte público](/files/add_to_transit_entry.png)


Para realizar a segunda entrada de estoque no armazém de destino, o usuário tem duas opções. Eles podem abrir a entrada de estoque original e clicar em "Finalizar trânsito" ou podem criar uma nova entrada de estoque e clicar em "Obter itens de"-> "Entrada de estoque em trânsito". O sistema buscará itens da entrada de estoque original com o armazém de origem (armazém de trânsito) igual ao armazém de destino da entrada de estoque original. O usuário deve definir o armazém de destino e salvar.


![End Transit](/files/end_transit_entry.png)


## 5. Vídeo






### 5. Tópicos Relacionados


1. [Finalidade de entrada de estoque](/docs/pt/stock/articles/stock-entry-purpose)
2. [Reconciliação de estoque](/docs/pt/stock/stock-reconciliation)
3. [Abrir entrada de saldo de estoque para serializados e em lote Artigo](/docs/pt/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
4. [Reconciliação de estoque](/docs/pt/stock/stock-reconciliation)
5. [Ordem de serviço](/docs/pt/manufacturing/work-order)
6. [Plano de produção](/docs/pt/manufacturing/production-plan)
7. [Cartão de trabalho](/docs/pt/manufacturing/job-card)



