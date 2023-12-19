# Configurações de compra



Configurações de Compra é onde você pode definir propriedades que serão aplicadas nas transações do módulo Compra.
Você pode encontrar configurações de compra em:
> Página inicial > Compra > Configurações > Configurações de compra


![Configurações de compra](/files/buying-settings.png)


Vejamos as diversas opções que podem ser configuradas:


## 1. Fornecedor


### 1.1 Nomeação de fornecedor por


Quando um Fornecedor é salvo, o sistema gera uma identidade ou nome exclusivo para esse Fornecedor, que pode ser usado para encaminhá-lo em diversas transações de Compra.


Se não for configurado de outra forma, o ERPNext usa o Nome do Fornecedor como nome exclusivo. Se você quiser identificar fornecedores usando nomes como SUPP-00001, SUPP-00002 ou outras séries padronizadas, selecione o valor de Nomeação de fornecedor por como "Série de nomenclatura".


Você pode definir ou selecionar o padrão de série de nomenclatura em: **Configurações > Dados > Série de nomenclatura**


Leia [Série de nomenclatura](/docs/pt/setting-up/settings/naming-series) para saber mais sobre como definir uma série de nomenclatura.


### 1.2 Grupo de fornecedores padrão


Configure qual deve ser o valor padrão do Grupo de Fornecedores ao criar um novo Fornecedor. Por exemplo, se a maioria dos seus fornecedores fornece hardware, você pode definir o padrão como 'Hardware'.


## 2. Compra


### 2.1 Lista de preços de compra padrão


Configure qual deve ser a Lista de Preços padrão ao criar uma nova transação de Compra, o padrão é definido como 'Compra Padrão'. Os preços dos itens serão obtidos nesta Lista de Preços. Você pode modificar a 'Lista de preços' usando a seta na extremidade direita do campo para alterar a moeda e o país.


### 2.2 Pedido de compra obrigatório


Se esta opção estiver configurada como "Sim", o ERPNext impedirá que você crie uma Fatura de Compra ou um Recibo de Compra diretamente sem criar primeiro um Pedido de Compra. Se houver transações de varejo envolvidas onde o pedido ocorre off-line, os pedidos de compra poderão ser ignorados. Se estiver aceitando itens de amostra, você pode criar diretamente um recibo de compra para receber os itens em seu armazém.


Essa configuração pode ser substituída para um fornecedor específico ativando a caixa de seleção "Permitir criação de fatura de compra sem pedido de compra" no cadastro de fornecedores


![Ordem de compra obrigatória](/files/po-required.png)


### 2.3 Recibo de compra obrigatório


Se esta opção estiver configurada como "Sim", o ERPNext impedirá que você crie uma Fatura de Compra sem antes criar um Recibo de Compra. Caso o Item a ser transacionado seja um serviço, não será necessário recibo, você poderá criar diretamente uma Fatura.


Essa configuração pode ser substituída para um fornecedor específico ativando a caixa de seleção "Permitir criação de fatura de compra sem recibo de compra" no cadastro de fornecedores


![Recibo de compra obrigatório](/files/pr-required.png)


### 2.4 Manter a mesma taxa durante todo o ciclo de compra


Se isto estiver habilitado, o ERPNext irá validar se o preço de um Item está mudando em uma Fatura de Compra ou Recibo de Compra criado a partir de um Pedido de Compra, ou seja, irá ajudá-lo a manter a mesma taxa durante todo o ciclo de compra.


Você pode configurar a ação que o sistema deve tomar se a mesma taxa não for mantida no campo "Ação se a mesma taxa não for mantida":


* **Parar**: o ERPNext impedirá que você altere o preço gerando um erro de validação.
* **Avisar**: o sistema permitirá que você salve a transação, mas avisará com uma mensagem se a taxa for alterada.


Observação: este campo só estará visível se Manter a mesma taxa durante todo o ciclo de compra estiver ativado.


### 2.5 Definir custo final com base na taxa da fatura de compra


Se a taxa de recebimento de compra e a taxa de fatura de compra não forem iguais e os usuários quiserem definir o custo final de acordo com a fatura de compra, esse recurso será útil.


Caso de uso


* Criado recibo de compra para o item A com taxa de 100
* O sistema reservou Stock In Hand com taxa de 100
* Após dois dias, o usuário criou uma fatura de compra com base no recibo de compra acima
* Após 2 dias devido à alteração na taxa de câmbio, a taxa na fatura mudou para 150
* Agora o recibo de compra tem taxa 100 enquanto a fatura de compra tem taxa 150
* Se você deseja ajustar o estoque em estoque com taxa de fatura de compra (150), esse recurso será útil


![Recibo de compra obrigatório](/private/files/set-valuation-rate-based-on-purchase-invoice.png)


## 3. Permitir que o item seja adicionado várias vezes em uma transação


Quando esta caixa de seleção está desmarcada, um item não pode ser adicionado várias vezes no mesmo pedido de compra. No entanto, você ainda pode alterar explicitamente a quantidade. Esta é uma caixa de verificação de validação para evitar a compra acidental do mesmo item. Isso pode ser verificado para casos de uso específicos onde há diversas fontes para o mesmo material, por exemplo, na fabricação.


### 4. Tópicos Relacionados


1. [Grupo de fornecedores](/docs/pt/buying/supplier-group)



