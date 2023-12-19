# Lista de seleção



**Uma lista de seleção é um documento que indica quais itens devem ser retirados de seu estoque para atender pedidos.**


Isso é particularmente útil para remetentes com grande quantidade de estoque, volume de pedidos ou clientes que solicitam muitas unidades de manutenção de estoque (SKU).
A lista de seleção seleciona o armazém onde um item está disponível na base FIFO (First-In-First-Out).
A seleção do Armazém para um item em lote é diferente. No caso de itens em lote, será selecionado o Armazém onde o lote está mais próximo do vencimento.


Para acessar a lista de seleção, acesse:


> Página inicial > Estoque > Transações de estoque > Lista de seleção


## 1. Pré-requisitos


Antes de criar e usar uma lista de seleção, é aconselhável criar primeiro o seguinte:


* [Item em estoque](/docs/pt/stock/item)
* [Armazém](/docs/pt/stock/warehouse)


## 2. Como criar uma lista de seleção


1. Vá para a lista de seleção e clique em Novo.
![Lista de seleção não salva](/files/pick-list-unsaved-doc.png)
2. Defina a empresa.
3. Selecione o objetivo da lista de seleção. Estas são as opções em Finalidade:


	* **Entrega:** Esta opção permitirá que você adicione itens de um pedido de venda para entrega. Depois de enviar a Lista de Retirada, uma nova Nota de Entrega pode ser criada com base no Armazém do qual os itens foram retirados.
	* **Transferência de material para fabricação:** isso permitirá que você selecione uma ordem de serviço da qual as matérias-primas serão retiradas para separação. Será apresentada a você a opção de selecionar o número de produtos acabados para os quais deseja selecionar matérias-primas. Depois de escolher o estoque, você pode criar uma entrada de estoque para os itens separados, ou seja, matérias-primas.
	* **Transferência de material:** isso permitirá que você selecione uma solicitação de material para a qual deseja selecionar itens. Após selecionar o estoque você pode criar uma Entrada de Estoque para os itens selecionados.
4. Adicione o item e a quantidade que deseja selecionar na tabela Locais de itens. Clique em **Obter localização dos itens** para obter o armazém e outros detalhes de cada item.
5. **Armazém pai:** se um armazém pai for selecionado, serão sugeridos armazéns somente sob esse armazém pai.
6. **Obter localizações dos itens:** Assim que os itens a serem selecionados forem finalizados, você pode clicar no botão **Obter localizações dos itens** para obter a seleção do armazém para cada item. Como o Armazém será buscado automaticamente se você obtiver um item de qualquer documento de referência, este botão pode ser útil para adicionar manualmente itens adicionais ou alterar a quantidade de itens existentes na tabela de locais de itens.
7. **Localizações de itens:** terá as informações da localização do item (Armazém), número de série para itens serializados e número de lote para itens em lote.
![Locais de itens](/files/pick-list-item-locations.png)


Se números de série estiverem envolvidos, a linha Item terá a seguinte aparência:
![Detalhe da localização do item](/files/pick-list-item-location-detail.png)
8. Salvar e enviar.
![Lista de seleção enviada](/files/pick-list-submitted-doc.png)


### 2.1 Criar lista de seleção a partir de um pedido de vendas


1. Acesse um [Pedido de venda](/docs/pt/selling/sales-order).
2. Clique no botão **Criar** no canto superior direito do formulário e depois clique na opção **Lista de seleção**.
3. Depois de clicar em Lista de Seleção, todos os dados necessários para a Lista de Seleção serão obtidos do Pedido de Venda.
4. Como alternativa, você pode criar uma nova lista de seleção e clicar em "Obter itens". Isso mostraria um pop-up de todos os pedidos de vendas pendentes.


![](/files/Screenshot 2021-12-29 às 12.04.24 PM.png)


1. Você deverá conseguir ver a tabela de localização de itens com o armazém selecionado para cada item.
2. Salve este documento e ele poderá ser utilizado para seleção de estoque pela pessoa que realiza esta atividade.
3. Envie o documento assim que a separação do estoque for concluída e as quantidades dos itens separados forem atualizadas no documento.


> **Observação:**
>
>-A lista de seleção só pode ser criada para Pedidos de Vendas que tenham '% escolhido' <100
>-Uma **Nota de Entrega** só poderá ser criada se a Lista de Escolha for enviada.


### 2.2 Criar lista de seleção a partir de uma ordem de serviço


1. Acesse uma [Ordem de serviço](/docs/pt/manufacturing/work-order).
2. Clique no botão **Criar lista de seleção**.
3. Você verá uma caixa de diálogo solicitando a quantidade do item de produtos acabados. Isso é necessário para calcular o número de itens de matéria-prima necessários para fabricar a quantidade inserida de item de produtos acabados.
![Dialog For qty](/files/pick-list-dialog-for-qty.png)
4. Você poderá ver a tabela de localização dos itens com o armazém selecionado para cada item de matéria-prima.
5. Salve este documento e então ele poderá ser encaminhado para a pessoa que está separando o estoque.
6. Envie o documento assim que a separação do estoque for concluída e o item selecionado for atualizado no documento adequadamente.


> **Nota:**
>
>-A lista de seleção só pode ser criada para Ordens de Serviço que ainda estejam no estado 'Não Iniciado' ou 'Em Andamento'.
>-Uma **entrada de estoque** só poderá ser criada após o envio da lista de seleção.


### 2.3 Criar lista de seleção a partir da solicitação de material


1. Acesse uma [Solicitação de material](/docs/pt/stock/material-request).
2. Clique no botão **Criar** e depois clique na opção **Lista de seleção**.
3. Você poderá ver a tabela de localização de itens com o armazém selecionado para cada item na solicitação de material.
4. Salve este documento e então ele poderá ser encaminhado para a pessoa que está selecionando o estoque.
5. Envie o documento assim que a separação do estoque for concluída e o item selecionado for atualizado no documento adequadamente.


> **Nota:**
>
>-Somente Solicitações de Materiais do tipo 'Transferência de Materiais' poderão ser utilizadas para criação de Lista de Pick.
>-Uma **entrada de estoque** do tipo 'Transferência de material' pode ser criada após o envio da lista de seleção.


## 3. Recursos


### 3.1. Atualizar estoque atual


Se uma lista de seleção estiver desatualizada, poderá haver uma mudança na disponibilidade de estoque no momento em que uma nota de entrega ou entrada de estoque for criada nela. Clicar em **Atualizar estoque atual** atualizará as quantidades e os armazéns na tabela Locais de itens.


> **Observação:** Este botão fica visível enquanto não houver Notas de Entrega ou Entradas de Estoque na Lista de Seleção.


### 3.2 Leitura de código de barras


A lista de seleção oferece suporte à leitura de código de barras, apresentando duas caixas de seleção. **Modo de digitalização** e **Quantidade de prompts**.


**Modo de verificação**: a ativação do modo de verificação desativa o comportamento padrão de envio da lista de seleção. A quantidade escolhida não será preenchida automaticamente.


**Quantidade do prompt**: quando ativado, em vez de aumentar a quantidade de itens digitalizados em 1, uma caixa de diálogo solicitará que o usuário insira uma quantidade para incrementar.


## 4. Tópicos Relacionados


1. [Ordem de vendas](/docs/pt/selling/sales-order)
2. [Ordem de serviço](/docs/pt/manufacturing/work-order)
3. [Solicitação de material](/docs/pt/stock/material-request)



