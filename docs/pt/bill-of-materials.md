# Lista de materiais



**Uma lista de materiais é uma lista de itens e subconjuntos com as quantidades necessárias para fabricar um item.**


Uma BOM também pode conter as operações de fabricação necessárias para fabricar o Item.


Uma **lista de materiais** (BOM) está no centro do sistema de manufatura e é o documento mais importante que ajudará a criar outros tipos de documentos, como ordens de serviço e cartões de trabalho. ERPNext suporta BOM multinível. Para saber mais, visite [esta página](/docs/pt/manufacturing/articles/managing-multi-level-bom).


A **BOM** é uma lista de todos os materiais (comprados ou fabricados) e operações
que vão para a fabricação de um produto acabado ou subconjunto. No ERPNext, cada item (submontagem) poderia
tem sua própria lista técnica, formando assim uma árvore de itens com vários níveis.


![Ordem de serviço](/files/manufacturing-flow-bom.png)


Para fazer solicitações de compra precisas, você deve sempre manter BOMs corretas.


Para acessar a lista BOM, vá para:
> Home > Fabricação > Lista de materiais > Lista de materiais



> Observe que depois que uma BOM é enviada, ela não pode ser editada. Você só pode cancelar o existente, duplicá-lo e enviar outro. Uma BOM também está vinculada a vários locais no módulo de Manufatura, portanto, fazer alterações nela pode ser demorado e tedioso. Portanto, é uma boa prática pensar cuidadosamente e preencher as listas técnicas antes de enviá-las.


## 1. Pré-requisitos


Antes de criar e usar uma BOM, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Operação](/docs/pt/manufacturing/operation)
* [Estação de trabalho](/docs/pt/manufacturing/workstation)
* [Roteamento](/docs/pt/manufacturing/routing)


## 2. Como criar uma lista de materiais


1. Vá para a lista Lista de materiais e clique em Novo.
2. Selecione o item a ser fabricado. O nome do item, unidade de medida, empresa e moeda serão obtidos automaticamente.
3. Insira a quantidade do Item que será fabricado a partir desta Lista de Materiais.
4. Na tabela Itens, selecione as matérias-primas (Itens) necessárias para fabricar o Item. Então prossiga para:


	1. Selecione a quantidade de matéria-prima utilizada.
	2. Defina aqui uma operação de Item para ser buscada posteriormente nas Ordens de Serviço.
	3. Se este item for uma submontagem, a lista técnica padrão dele será buscada.
	4. Selecione o armazém de origem para rastrear o estoque.
	5. Insira o percentual de refugo que restará após a utilização desta matéria-prima.
	![Materiais BOM](/files/bom-materials.png)
5. Na seção Sucata, selecione o item de sucata que será criado durante a fabricação e sua quantidade. O Item de sucata também pode ter uma Taxa se for um subproduto e não um desperdício. Pule esta seção se 100% das matérias-primas forem totalmente utilizadas. Se o Item de refugo for igual ao Item a ser fabricado, ele é definido como Item de Perda de Processo e sua quantidade é subtraída da quantidade do Item fabricado.
![BOM Scrap](/files/bom-scrap.png)
6. Salvar e enviar.


Na tabela Itens, você verá a opção 'Incluir Item na Fabricação'. Matérias-primas precisam ter esta caixa de seleção marcada. Caso existam Operações ou serviços que você precise incluir na BOM que não sejam necessariamente um Item utilizado para fabricação, desmarque esta caixa de seleção. Por exemplo, tratar o plástico com um produto químico envolve algum custo, mas não é um Item e o custo precisa ser rastreado.


![Task](/files/bom-item-include.png)


### 2.1 Lista de materiais com operações


Para adicionar [Operações](/docs/pt/manufacturing/operation) marque a caixa de seleção 'Com operações'. Agora, uma tabela de Operações pode ser vista. Esta opção é útil para rastrear o custo de diversas operações realizadas para fabricar o [Item](/docs/pt/stock/item). As operações podem ser adicionadas facilmente definindo um modelo com o mestre [Roteamento](/docs/pt/manufacturing/routing).


![Task](/files/bom-operations.png)


1. Na tabela “Operações”, adicione as operações que precisam ser realizadas para fabricar este item específico.
2. Para cada operação, você será solicitado a inserir uma [Estação de trabalho](/docs/pt/manufacturing/workstation) onde a operação será executada. Uma estação de trabalho padrão pode ser definida no documento [Operação](/docs/pt/manufacturing/operation).
3. Insira a taxa horária de operação, o tempo de operação em minutos e o tamanho do lote criado com a operação. O Custo Operacional será calculado com base nestes valores.


> Observação: As estações de trabalho são definidas apenas para fins de cálculo de custos de produtos e agendamento de operações de ordens de serviço, não para rastreamento de estoque. O estoque é rastreado em [Armazéns](/docs/pt/stock/warehouse) definidos na tabela Itens da BOM.


Transferir material contra precisa ser definido para uma lista técnica com operações. Os materiais podem ser transferidos de acordo com uma [Ordem de serviço](/docs/pt/manufacturing/work-order) em massa ou [Cartões de trabalho](/docs/v13/user individual/manual/en/manufacturing/job-card). Alterar isso afeta se a 'Transferência de material para fabricação' é feita na ordem de serviço de uma só vez ou várias vezes em relação aos cartões de trabalho individuais. Definir esta opção depende de fatores como o tempo necessário para fabricar o item, o valor dos itens fabricados, o número de peças utilizadas na fabricação, a habilidade do trabalho envolvido, etc.


![BOM transfere materiais contra](/files/bom-transfer-materials.png)


### 2.2 Opções adicionais ao criar uma lista de materiais


* **Está ativo**: um item também pode ser fabricado usando um conjunto alternativo de materiais/operações. Nesse caso, desmarque esta caixa de seleção para desativar esta BOM e usar outra.
* **É padrão**: esta lista técnica será selecionada por padrão em ordens de serviço etc. quando o item for selecionado.
* **Inspeção necessária**: Isso tornará a 'Inspeção de qualidade' obrigatória para matérias-primas e produtos acabados. Selecione o modelo de inspeção de qualidade após marcar esta caixa de seleção.
* **Permitir item alternativo**: Às vezes, durante a fabricação de um produto acabado, materiais específicos podem não estar disponíveis. Se você marcar esta opção, poderá criar e selecionar um item alternativo na lista Alternativa de item. Por exemplo, usando contas de plástico em vez de cristais de plástico. Para obter mais detalhes, visite [esta página](/docs/pt/manufacturing/item-alternative).
* **Permitir o mesmo item várias vezes**: em alguns casos de fabricação, o mesmo item precisa ser adicionado duas vezes. Por exemplo, dois tubos de metal com 0,5 m de comprimento cada para formar outro formato. Aqui a quantidade não pode ser simplesmente definida como 2 e feita, pois a UM mostrará 1m como total, mas precisamos de 0,5m + 0,5m na forma de dois tubos para produção. Marcar esta caixa de seleção permite selecionar o mesmo item várias vezes.
* **Definir taxa de item de submontagem com base na BOM**: Ativar esta caixa de seleção definirá a taxa de itens de submontagem com base em suas BOMs. Se desmarcada, a taxa será obtida a partir da Taxa de Avaliação do Item da submontagem.
* **Taxa de materiais baseada em**: A taxa de matérias-primas utilizadas pode ser calculada com base em diferentes parâmetros.


	+ **Taxa de avaliação**: a taxa de avaliação definida no [Mestre de itens](/docs/pt/stock/item).
	+ **Taxa da última compra**: a taxa é obtida do último [pedido](/docs/pt/selling/sales-order) de vendas/[Fatura](/docs/pt/accounts/sales-invoice).
	+ **Lista de preços**: A taxa será obtida no [Preço do item](/docs/pt/stock/item-price).
	Para obter mais detalhes, visite [esta página](/docs/pt/manufacturing/articles/valuation-based-on-field-in-bom).


## 3. Recursos


### 3.1 Custo da lista de materiais


A seção Custos em uma BOM fornece um custo aproximado de fabricação do item.


O custeio é calculado a partir da Taxa de Avaliação das matérias-primas/subconjuntos envolvidos e dos custos da Operação.


![Costing](/files/bom-costing.png)


Caso a BOM tenha sido enviada quando os custos de Itens/Operações não foram atualizados, você pode atualizar os custos usando o botão **Atualizar Custo**. Isso irá buscar os preços/custos mais recentes.


![Custo de atualização](/files/bom-update-cost.png)


O custo da BOM também pode ser configurado para ser atualizado automaticamente nas Configurações de fabricação, opção 'Atualizar custo da BOM automaticamente'.


### 3.2 Materiais necessários (explodidos)


Esta tabela lista todas as matérias-primas necessárias para fabricar um item. Também busca matéria-prima para os subconjuntos junto com as quantidades. A tabela não explodida não listará as matérias-primas necessárias para a produção dos subconjuntos.


Por exemplo, para fabricar um pincel de barbear de plástico são necessárias algumas matérias-primas e as cerdas como subconjunto. Para o cabo você fabrica seu próprio plástico, mas para as cerdas você usa cristais de plástico bruto.


![Seção Explodida](/files/bom-exploded.png)


#### 3.2.1 Não explodir


Se o usuário quiser excluir os itens explodidos, ele deverá ativar a caixa de seleção "Não explodir" na tabela de itens da BOM. 


##### Caso de uso:


* Computador portátil
	+ Placa-mãe (mantida em estoque)
	+ Teclado


Uma empresa fabricava o Laptop que exigia dois itens de submontagem como Placa-Mãe e Teclado. A empresa faz a fabricação assim que recebe o pedido do cliente. O Tempo de Fabricação da Placa-mãe é maior que o do Teclado, portanto a empresa faz a fabricação da Placa-mãe individualmente independente dos pedidos de venda e mantidos em estoque. Como o item Placa-mãe já está em estoque ajuda a reduzir o Tempo geral de Fabricação do item principal Laptop.
Agora enquanto preparam a BOM para o Laptop no ERPNext, eles não querem Explodir a BOM do item Placa-Mãe mas querem Explodir a BOM do item Teclado. Portanto, adicionamos a caixa de seleção "Do Not Explode" para o item da BOM. Com isso o usuário irá habilitar o checkbox “Do Not Explode” para o item Placa Mãe e não para o item Teclado.


![Seção Explodida](/files/dont_explode_items.png)


### 3.3 Projeto e site


A lista técnica pode ser vinculada a um [Projeto](/docs/pt/projects) para acompanhar o progresso, custos do projeto, etc. cada pedido poderia ser um [Projeto](/docs/pt/projects/project) e os subconjuntos seriam [Tarefas](/docs/v13/user/manual/pt/projetos/tarefas). Nesse caso, a conclusão pode ser rastreada vinculando-se a um projeto.


A BOM também pode ser mostrada no [Site](/docs/pt/website) para produtos de hardware de código aberto. O hardware de código aberto é semelhante ao código aberto, onde as especificações do produto são listadas publicamente.


### 3.4 Modelo de BOM


![Modelo BOM](/files/bom-template.png)


Com o modelo de BOM você pode criar BOMs para itens de modelo (com base nos quais você cria itens variantes). Essas BOMs podem ser usadas como BOM padrão ao criar Ordens de Serviço em relação às variantes do item do modelo. Você também pode adicionar os itens do modelo como matéria-prima na lista técnica do modelo. Ao fazer a Ordem de Serviço a partir do Modelo de BOM, o ERPNext permite selecionar a Variante do Item em relação ao Item do modelo, para mais detalhes verifique a captura de tela a seguir.


![Seleção de variante](/files/variant-selection-against-template.png)


O usuário também pode criar a lista técnica para o item variante usando o modelo de lista técnica. Para criar a lista técnica da variante:


* Acesse o modelo de BOM.
* Clique no botão **Criar**.
* Clique na BOM da variante.
* Selecione o item variante para o qual deseja criar a lista técnica.
* Se a matéria-prima na lista técnica for um item de modelo, o sistema permite selecionar a variante do item.


![Variante BOM](/files/variant-bom.png)


### 3.5 Após o envio


Depois que a BOM for enviada, os seguintes tipos de documentos poderão ser criados na BOM no Painel:


![BOM submit](/files/bom-submit.png)


## 4. Vídeo






### 5. Tópicos Relacionados


1. [Gerenciamento de sucata](/docs/pt/manufacturing/articles/scrap-management)
2. [Consumo de material](/docs/pt/manufacturing/articles/material_consumption)
3. [Estrutura de BOM aninhada](/docs/pt/manufacturing/articles/managing-multi-level-bom)



