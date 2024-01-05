# Configurações de venda



Configurações de Venda é onde você pode definir propriedades e validações que serão aplicadas aos mestres e transações envolvidas no ciclo de vendas.


Para acessar as configurações de vendas, acesse:



> 
> Página inicial > Vendas > Configurações > Configurações de vendas
> 
> 
> 


## Padrões do cliente


![Padrões do cliente](/files/Padrões do cliente.png)


### 1. Nomeação do cliente por


Quando um cliente é salvo, um ID exclusivo é gerado para esse cliente.


Por padrão, o ID do cliente é gerado com base no nome do cliente. Caso queira salvar o Cliente utilizando uma série de nomenclatura, no campo Série de Nomenclatura do Cliente, defina o valor como “Série de Nomenclatura”. Exemplo de IDs de clientes salvos em séries de nomenclatura-"CUST00001, CUST00002, CUST00003..." e assim por diante.


Você pode definir séries de nomes para clientes de:



> 
> Configuração > Dados > Série de nomenclatura
> 
> 
> 


### 2. Grupo de clientes padrão


Selecione um Grupo de Clientes padrão que será atualizado automaticamente ao criar um novo Cliente.


As cotações podem ser criadas tanto para os Clientes quanto para os Leads. Ao converter uma Cotação em Pedido de Venda, que é criado para um Lead, o sistema tenta converter esse Lead em Cliente. Ao criar o Cliente no back-end, o valor do Grupo de Clientes é escolhido nas Configurações de Venda. Se nenhum valor padrão for encontrado para o Grupo de Clientes, você receberá uma mensagem de validação solicitando o Grupo de Clientes. Você também pode converter manualmente um lead em cliente.


### 3. Território padrão


Selecione um Território padrão que será atualizado automaticamente ao criar um novo Cliente.


As cotações podem ser criadas tanto para os Clientes quanto para os Leads. Ao converter uma Cotação em Pedido de Venda, que é criado para um Lead, o sistema tenta converter esse Lead em Cliente. Ao criar o Cliente no back-end, o valor do Território é escolhido nas Configurações de Venda. Se nenhum valor padrão for encontrado para Território, você receberá uma mensagem de validação solicitando o Território. Você também pode converter manualmente um lead em cliente.


## Configurações de CRM


![Configurações de CRM](/files/Configurações de CRM.png)


### 1. Nomeação da campanha por


Assim como para Cliente, você também pode configurar a metodologia de nomenclatura para o mestre da campanha. Por padrão, uma campanha será salva com o Nome da campanha.


### 2. Dias de validade da cotação padrão


As cotações ao cliente são válidas apenas para determinados dias. Na cotação, você pode atualizar a data válida até a data manualmente. Por padrão, a data Válida até é definida automaticamente como 30 dias a partir da data de lançamento da cotação. Você pode alterar o não. de dias neste campo de acordo com seu caso de negócios.


### 3. Fechar oportunidade após dias


Se houver muitas oportunidades com status diferente de Aberta, elas serão fechadas automaticamente após o não. de dias mencionados neste campo.


## Configurações de preço do item


![Configurações de preço do item](/files/Configurações de preço do itemdcf22b.png)


### 1. Lista de preços padrão


A Lista de Preços definida neste campo será atualizada automaticamente no campo Lista de Preços de transações de vendas como Cotação, Pedido de Venda, Nota de Entrega e Fatura de Venda.


### 2. Mantenha a mesma taxa durante todo o ciclo de vendas


Se estiver habilitado, o ERPNext irá validar se o preço de um Item está mudando em uma Nota de Entrega ou Fatura de Venda criada a partir de um Pedido de Venda, ou seja, irá ajudá-lo a manter a mesma taxa durante todo o ciclo de vendas.


### 3. Ação se a mesma taxa não for mantida durante todo o ciclo de vendas


Você pode configurar a ação que o sistema deve tomar se a mesma taxa não for mantida no campo "Ação se a mesma taxa não for mantida durante todo o ciclo de vendas":


* **Parar**: o ERPNext impedirá que você altere o preço gerando um erro de validação.
* **Avisar**: o sistema permitirá que você salve a transação, mas avisará com uma mensagem se a taxa for alterada.


**Observação:** este campo só estará visível se [Manter a mesma taxa durante todo o ciclo de vendas](/docs/pt/selling/selling-settings#2-maintain-same-rate-throughout-sales-cycle) está ativado.


### 4. Função com permissão para substituir ação de parada


Permitir que os usuários adicionem uma função para substituir a ação "Parar" para [Manter a mesma taxa durante todo o ciclo de vendas](/docs/pt/selling/selling-settings#2-maintain-same-rate-throughout-sales-cycle ), se [Ação se a mesma taxa não for mantida](/docs/pt/selling/selling-settings#3-action-if-same-rate-is-not-mantida durante todo o ciclo de vendas) foi definida como Parar.


**Observação:** este campo só estará visível se 'Manter a mesma taxa durante todo o ciclo de vendas' estiver ativado e 'Ação se a mesma taxa não for mantida' estiver definida como Parar.


### 5. Permitir que o usuário edite a taxa da lista de preços nas transações


A tabela de itens nas transações de venda possui um campo denominado Taxa da Lista de Preços. Este campo não é editável por padrão em todas as transações de vendas. Isso é para garantir que o preço de um item seja obtido do registro de Preço do Item e que o usuário não possa editá-lo.


Se você precisar que o preço do item obtido na lista de preços de um item seja editável, desmarque este campo.


### 6. Valide o preço de venda do item em relação à taxa de compra ou taxa de avaliação


Ao realizar vendas, é importante saber que você não está tendo prejuízos. A ativação desta validação validará o Preço de Venda do artigo com o seu preço de avaliação/compra. Se o preço de venda de um item for inferior ao preço de compra, você receberá um aviso quando esta caixa de seleção for marcada.


### 7. Calcule o preço do pacote de produtos com base nas taxas dos itens secundários


Ativar isso fará o seguinte:


* Tornar editável a coluna Taxa de todas as tabelas de itens embalados/pacotes.
* Calcule os preços de todos os [Pacotes de produtos](/docs/pt/selling/product-bundle) na tabela Itens, com base nos preços de seus itens secundários , especificado na tabela Itens embalados/pacote.


**Observação:** se estiver ativado, a atualização da taxa do pacote de produtos na tabela de itens não alterará seu preço. O preço será redefinido com base nos itens secundários ao salvar o documento.


## Configurações de transação


![Configurações de transação](/files/Configurações de transação34784c.png)


### 1. O pedido de vendas é necessário para a criação de faturas de vendas e notas de entrega?


Se você deseja tornar a criação de Pedido de Venda obrigatória antes da criação de uma Fatura de Venda ou de uma Nota de Entrega, então você deve definir o campo 'Pedido de Venda Obrigatório' como 'Sim'. Por padrão, será 'Não'.


Essa configuração pode ser substituída para um cliente específico ativando a caixa de seleção "Permitir criação de fatura de venda sem pedido de venda" no cadastro do cliente.


### 2. A nota de entrega é necessária para a criação da fatura de vendas?


Para tornar a criação da Nota de Entrega obrigatória antes da criação da Fatura de Venda, você deve definir este campo como 'Sim'. Por padrão, será 'Não'.


Essa configuração pode ser substituída para um cliente específico ativando a caixa de seleção "Permitir criação de fatura de venda sem nota de entrega" no cadastro do cliente


### 3. Frequência de atualização de vendas


A frequência com que o progresso do projeto e os detalhes das transações da empresa serão atualizados. Por padrão, é para Cada transação. Você também pode defini-lo como Diário ou Mensal se tiver muitas transações todos os dias.


### 4. Permitir que o item seja adicionado várias vezes em uma transação


Esta é uma verificação de validação que evita que um item seja adicionado várias vezes na mesma transação quando desmarcado. Em alguns casos, isso pode ser uma necessidade explícita. Marque esta caixa.


### 5. Permitir vários pedidos de vendas em relação ao pedido de compra de um cliente


Ao criar um Pedido de Venda, você pode atualizar o ID do Pedido de Compra e a Data recebida do Cliente. Você pode criar apenas um Pedido de Vendas com base no Nº e Data do Pedido de Compra do Cliente. No entanto, se você deseja permitir a criação de vários pedidos de vendas para o mesmo número de pedido do cliente, marque a caixa de seleção "Permitir vários pedidos de vendas para um pedido de compra do cliente".


### 6. Ocultar o número de identificação fiscal do cliente nas transações de vendas


De acordo com a exigência legal, a maioria dos Clientes possui um ID Fiscal exclusivo atribuído a eles. Eles também precisam ter esse número de identificação fiscal obtido nas transações de venda. No entanto, se não desejar usar esta funcionalidade, você pode desativá-la marcando esta propriedade.


### 7. Calcule o preço do pacote de produtos com base nas taxas dos itens secundários


Ao ativar Calcular preço do pacote de produtos com base nas taxas de itens secundários:


A coluna Taxa de Itens Embalados se tornará editável.
A taxa e o preço dos Pacotes de Produtos na tabela de Itens serão atualizados com base nas taxas de seus Itens secundários.


Observação: se a taxa do pacote de produtos for alterada agora, ela será redefinida para a soma com base nas taxas de seus itens secundários ao salvar o documento.



