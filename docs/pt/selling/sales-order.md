# Pedido de venda



**Um pedido de venda é uma confirmação de um pedido de seu cliente.**


Geralmente é um contrato vinculativo com seu cliente. Depois que seu cliente confirmar a cotação, você poderá convertê-la em um pedido de venda.


![Fluxo de vendas](/files/selling-flow-so.png)


Para acessar o Pedido de Venda, acesse:



> 
> Página inicial > Vendas > Vendas > Pedido de vendas
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar um Pedido de Venda, é aconselhável criar primeiro o seguinte:


* [Cliente](/docs/pt/CRM/customer)
* [Item](/docs/pt/stock/item)


## 2. Como criar um pedido de venda


1. Vá para a lista de pedidos de vendas e clique em Novo.
2. Selecione o cliente.
3. Defina a 'Data de entrega'-aplicada a todo o pedido.
4. Com o Tipo de pedido, você pode definir se é um pedido de vendas, um pedido de manutenção ou do [Carrinho de compras](/docs/pt/website/shopping-cart) do seu site. Por padrão, esse valor é definido como "Vendas".
5. No "Pedido de Compra do Cliente" você pode inserir o Nº do Pedido de Compra do Cliente ou outros detalhes que possam ser úteis como referência.
6. Insira os itens e quantidades a serem entregues na tabela Item. Se os Preços dos Itens estiverem definidos para os itens, o campo Taxa será preenchido automaticamente. Caso contrário, insira o item Taxa manualmente. Você também pode substituir a taxa de item preenchida automaticamente caso queira alterar esse valor.
7. Clique em "Salvar" para salvar um rascunho do pedido de venda.
8. "Enviar" para enviar o pedido de vendas ao sistema.


### 2.1 Outras maneiras de criar um pedido de vendas


1. Você também pode criar um pedido de vendas a partir de uma cotação enviada por meio do botão Criar no canto superior direito.


![Fazer pedido de vendas a partir da cotação](/files/make-SO-from-quote.png)
2. Ou você pode criar um novo pedido de vendas e obter detalhes de uma cotação.


![Fazer pedido de venda a partir da cotação](/files/so-from-quote.gif)


Para permitir regras de preços por cliente e por item, ("o cliente A" paga US$ 1,00 pelo "item 1", mas o "cliente B" paga US$ 1,25 pelo "item 1"), há uma caixa de seleção chamada "Permitir usuário para editar a taxa da lista de preços na transação' em [Configurações de venda](/docs/pt/selling/selling-settings). Isso permite salvar o preço do item específico por cliente quando você altera um preço no pedido de venda.


## 3. Recursos


### 3.1 Moeda e lista de preços


Você pode definir a moeda na qual a cotação/pedido de venda será enviada. Se você definir uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar 'Ignorar regra de preços' irá ignorar as [Regras de preços](/docs/pt/accounts/pricing-rule) definidas em Contas > Regra de preços.


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.1 Definir armazém de origem


Se você tiver o mesmo estoque em vários armazéns, definir um armazém aqui fará com que todos os itens da tabela de itens sejam buscados neste armazém. Você precisa ter estoque disponível neste 'armazém de origem' que você está configurando. Observe que esta opção substituirá o 'Armazém padrão' que você definiu no cadastro de itens.


### 3.2 A tabela de itens


* **Data de entrega de cada item**: se houver vários itens e se você inserir uma data de entrega na primeira linha, a data também será copiada para outras linhas onde estiver em branco . Você terá que defini-los, se não estiverem definidos globalmente, na parte superior do pedido de vendas.


Um pedido de venda exibe o valor faturado, a taxa de avaliação e o lucro bruto na tabela de itens quando você clica no triângulo invertido para expandir uma linha.


Você também pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* **Armazém de Entrega**: É o armazém de onde será retirado o estoque para entrega ao seu cliente.
* **Drop Ship**: Esta é uma situação em que você não mantém itens em estoque em seu próprio armazém, mas entrega itens diretamente a um cliente de um distribuidor. Para ativar o envio direto para um item, marque 'O fornecedor entrega ao cliente'. Ao marcar esta opção, a opção Armazém de Entrega desaparecerá, pois você não está enviando o item. Selecione seu fornecedor no campo 'Fornecedor'.


Além disso, se você criar um pedido de compra a partir deste pedido de venda, ele será criado para o fornecedor selecionado aqui e apenas para os itens válidos para envio direto.
* **Planejamento**: leia [Quantidade projetada](/docs/pt/stock/projected-quantity) para saber mais sobre os campos em planejamento.


Os outros campos na tabela de itens são semelhantes aos explicados em [Cotação](/docs/pt/selling/quotation#23-the-items-table). 


### 3.3 Lista de embalagem


Isso está vinculado ao [Pacote de produtos](/docs/pt/selling/product-bundle) e aparece somente quando a transação envolve um pacote de produtos.
A tabela “Packing List” será atualizada automaticamente quando você “Salvar” o Pedido de Venda. Se algum item da sua tabela for pacote de produtos (pacotes), a “Lista de embalagem” conterá a lista explodida (detalhada) dos seus itens.


Você será solicitado a selecionar um Armazém de Entrega mesmo para um item de pacote de produtos, esse armazém será então atualizado nos itens da Lista de Embalagem. Você pode alterar o armazém, o número de série e o lote nos itens da lista de embalagem caso os itens do seu pacote de produtos venham de armazéns diferentes.


Esta é a aparência de uma lista de embalagem:


![Lista de embalagem](/files/so-packing-list.png)


### 3.4 Impostos e Taxas


Para adicionar impostos ao seu pedido de vendas, você pode selecionar um [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template) ou adicione os impostos manualmente na tabela Impostos e Encargos sobre Vendas.


O total de impostos e taxas será exibido abaixo da tabela. Clicar em Tax Breakup mostrará todos os componentes e valores.


![Impostos na cotação](/files/sales-order-taxes.png)


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


Se uma categoria de imposto for selecionada, o modelo e a tabela de impostos serão preenchidos automaticamente. Para saber mais, visite [esta página](/docs/pt/accounts/tax-category).


### 3,5 desconto adicional


Além de oferecer desconto por item, você pode adicionar um desconto a todo o pedido de venda nesta seção. Este desconto pode ser baseado no total geral, ou seja, após impostos/encargos, ou no total líquido, ou seja, antes de impostos/encargos. O desconto adicional pode ser aplicado como uma porcentagem ou um valor.


Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.6 Condições de pagamento


Às vezes o pagamento não é feito de uma só vez. Dependendo do acordo, metade do pagamento poderá ser feito antes do envio e a outra metade após o recebimento da mercadoria/serviço. Você pode adicionar um modelo de condições de pagamento ou adicionar os termos manualmente nesta seção.


Leia as [Condições de pagamento](/docs/pt/accounts/payment-terms) para saber mais.


### 3.7 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 3.8 Configurações de impressão


#### Papel timbrado


Você pode imprimir sua cotação/pedido de venda em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados várias vezes na tabela de itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


As cotações também podem ser intituladas como “Fatura Proforma” ou “Proposta”.
Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


### 3.9 Mais informações


* **Campanha:** Uma campanha de vendas pode ser associada à cotação. Um conjunto de cotações pode fazer parte de uma campanha de vendas.
* **Fonte:** Um tipo de fonte de lead pode ser vinculado se estiver citando um lead, seja de uma campanha, de um fornecedor, de uma exposição, etc. Selecione Cliente existente se estiver fazendo uma cotação para um cliente.
* **Referência de pedido entre empresas**: Se duas de suas empresas fizerem parte da mesma organização ou tiverem um relacionamento pai-filho, você poderá vincular um Pedido de Compra a este Pedido de Venda. Saiba mais sobre faturamento entre empresas [aqui](/docs/pt/accounts/inter-company-invoices).
* **Projeto**: se seu pedido de venda fizer parte de um projeto, você poderá vinculá-lo aqui e o andamento do projeto será atualizado.


### 3.10 Status de cobrança e entrega


* **Status**: o status do pedido de vendas, seja Rascunho, Em espera, Para entregar e faturar, Para faturar, Para entregar, Concluído, Cancelado ou Fechado.
* **Porcentagem do valor faturado e entregue**: a porcentagem do valor faturado e dos itens entregues do pedido de venda.


### 3.11 Comissão


Se a venda ocorreu por meio de um de seus parceiros de vendas, você poderá adicionar os detalhes da comissão aqui. Insira a taxa de comissão e o valor da comissão será exibido abaixo.


### 3.12 Equipe de vendas


**Vendedores:** ERPNext permite que você adicione vários Vendedores que possam ter trabalhado neste negócio. Você pode alterar a porcentagem de contribuição dos vendedores e acompanhar quantos incentivos eles ganharam neste negócio.


![Equipe de vendas no pedido de vendas](/files/so-sales-team.png)


### 3.13 Seção de repetição automática


A repetição automática de pedidos de vendas é como uma assinatura. Defina uma data de início e término para a repetição automática. Selecione a repetição automática criada. Para saber mais sobre a repetição automática [clique aqui](/docs/pt/automation/auto-repeat).


### 3.14 Após o envio


O pedido de venda é uma transação “submissível”. Você poderá executar outras etapas (como fazer uma Nota de Entrega) somente após “Enviar” um Pedido de Venda.


Depois de “enviar” seu pedido de vendas, você poderá acionar ações a partir do pedido de vendas:


* Você pode adicionar, atualizar e excluir itens do pedido de vendas clicando no botão **Atualizar itens**. No entanto, você não pode excluir itens que já foram entregues ou que possuem ordens de serviço atribuídas a eles.
* Status: depois de enviado, você pode reter um pedido de vendas ou fechá-lo.
* Criar: A partir de um pedido de vendas enviado, você pode criar o seguinte:


	+ Guia de Entrega-Para fazer um lançamento de remessa. Você também pode fazer Nota de Entrega para itens selecionados com base na data de entrega.
	+ Ordem de Serviço-Para iniciar uma Ordem de Serviço com as matérias-primas.
	+ Fatura de Venda-Para faturar o Pedido.
	+ Solicitação de material-Para solicitar reabastecimento de materiais em caso de falta de estoque.
	+ Solicitação de Matérias-Primas-Para solicitar matérias-primas necessárias para a fabricação.
	+ Projeto-Para criar um projeto baseado no Pedido de Venda.
	+ Assinatura-Para repetir automaticamente o Pedido de Venda, ou seja, torná-lo uma assinatura.
	+ Solicitação de pagamento-Para fazer uma solicitação de pagamento.
	+ Pagamento-Para registrar o pagamento no pedido de vendas.


Essas ações também podem ser vistas na parte superior do Painel. Você também pode fazer um lançamento contábil manual com base no pedido de vendas no painel.


![Ações do pedido de venda enviado](/files/submit-so.png)


### 3.15 Pedido de vendas com tipo de pedido 'Manutenção'


Quando o 'Tipo de Pedido' do Pedido de Venda for 'Manutenção' siga estes passos:


1. Insira a moeda, a lista de preços e os detalhes do item.
2. Mencione impostos e outras informações.
3. Salve e envie o formulário.
4. Depois que o formulário for enviado, o botão Criar fornecerá essas opções específicas para o tipo de pedido de manutenção.


i) Visita de manutenção
 ii) Cronograma de Manutenção.


![Tipo de manutenção de pedido de vendas](/files/so-maintenance.png)



> 
> **Nota 1:**
>  Ao clicar no botão Ação e selecionar 'Visita de Manutenção' você pode preencher diretamente o formulário de visita. Os detalhes do pedido de venda serão obtidos diretamente.
> 
> 
> 



> 
> **Nota 2:**
>  Ao clicar no botão Ação e selecionar 'Cronograma de Manutenção' você pode preencher os detalhes do cronograma. Os detalhes do pedido de venda serão obtidos diretamente.
> 
> 
> 



> 
> **Nota 3:**
>  Ao clicar no botão Fatura você pode fazer uma Fatura para o seu
>  Serviços. Os detalhes dos pedidos de vendas serão obtidos diretamente.
> 
> 
> 


### 4. Tópicos Relacionados


1. [Cotação](/docs/pt/selling/quotation)
2. [Fechar pedido de venda](/docs/pt/selling/articles/close-sales-order)
3. [Alteração do pedido de vendas após o envio](/docs/pt/selling/articles/amending-sales-order-after-submit)
4. [Lista de seleção](/docs/pt/stock/pick-list#21-create-pick-list-from-sales-order)





