# Nota de entrega



**Uma Nota de Entrega é feita quando uma remessa é enviada do Armazém da empresa para o cliente.**


Uma cópia da Nota de Entrega geralmente é enviada junto com o transportador. A entrega
Nota contém a lista de Itens que são enviados na remessa e atualiza o
inventário. A Nota de Entrega é uma etapa opcional e uma Fatura de Venda pode ser criada diretamente de um Pedido de Venda.


Para acessar a lista de Notas de Entrega, acesse:
> Home > Estoque > Transações de estoque > Nota de entrega


![Fluxo da nota de entrega](/files/delivery-note-flow.png)


## 1. Pré-requisitos


Antes de criar e usar uma Nota de Entrega, é aconselhável que você crie primeiro o seguinte:


* [Ordem de vendas](/docs/pt/selling/sales-order)


> Nota: A partir da versão 13 introduzimos o livro-razão imutável que altera as regras para cancelamento de entradas de estoque e lançamento de transações de estoque retroativas no ERPNext. [Saiba mais aqui](/docs/pt/accounts/articles/immutable-ledger-in-erpnext).


## 2. Como criar uma Nota de Entrega


A entrada da Nota de Entrega é muito semelhante a um Recibo de Compra. Geralmente é criado a partir de um Pedido de Venda “Enviado” (que não é enviado) clicando em Criar > Entrega.


Para criar uma nota de entrega *manualmente* (não recomendado), siga estas etapas:


1. Vá para a lista de Notas de Entrega e clique em Novo.
2. Os detalhes do cliente e do item podem ser obtidos clicando em 'Obter itens de> Pedido de venda'.
3. A UOM e as taxas serão obtidas automaticamente.
4. Salvar e enviar.


![Nota de entrega](/files/delivery-note.png)


Para buscar itens de um pedido de vendas, clique em Obter itens de > Pedido de vendas. Isso abrirá um pop-up onde você poderá pesquisar pedidos de vendas e selecionar um.


Você notará que todas as informações sobre itens não enviados e outros detalhes serão transferidos do seu pedido de venda se você criar a nota de entrega a partir daí.


Você também pode editar a data e hora de postagem. A data e hora atuais são definidas quando você cria a Nota de Entrega.


### 2.1 Status


Estes são os status em que uma nota de entrega pode estar:


* **Rascunho**: um rascunho foi salvo, mas ainda precisa ser enviado ao sistema.
* **A faturar**: ainda será cobrado usando uma [fatura de vendas](/docs/pt/accounts/sales-invoice).
* **Concluído**: Enviou e enviou todos os itens.
* **Devolução emitida**: todos os itens foram devolvidos.
* **Cancelado**: cancelou a nota de entrega.
* **Fechado**: O objetivo do Fechamento é gerenciar o fechamento a descoberto. Por exemplo, seu cliente pediu 20 unidades, mas fechou em 15 unidades. Os 5 restantes não serão enviados nem cobrados.


### 2.2 Entregas parciais


Quando você cria uma Nota de Entrega a partir de um Pedido de Venda, as quantidades podem ser alteradas. Portanto, se o Pedido de Venda contiver 10 Itens a serem entregues e você estiver entregando apenas 5 nesta semana e o restante na próxima, você poderá criar 2 Notas de Entrega em duas semanas.


### 2.3 Da lista de seleção


Você pode criar notas de entrega em massa, também a partir de listas de seleção. Em uma lista de seleção enviada, clique em Criar-> Nota de entrega. 


![](/files/Screenshot 2021-12-29 às 12.28.06 PM.png)


Isso criaria Notas de Entrega separadas para Pedidos de Vendas, agrupados por Cliente.
Se um item da lista de seleção não estiver vinculado a um pedido de vendas (adicionado manualmente pelo usuário), um DN separado também será criado para todos esses itens.


## 3. Ações relacionadas


### 3.1 Detalhes do pedido de compra do cliente


Você pode inserir o número do pedido de compra do cliente aqui para referência.


### 3.2 Endereço e contato


* **Endereço de Envio**: O endereço do Cliente para onde os Itens serão enviados.
* **Pessoa de Contato**: Se o Cliente for uma organização, adicione a Pessoa de Contato neste campo.


Para a Índia, os seguintes detalhes podem ser adicionados para o GST:


* GSTIN do cliente
* Local de fornecimento
* Endereço de cobrança GSTIN
* GSTIN da empresa
* Nome do endereço da empresa


[Contatos](/docs/pt/CRM/contact) e [Endereços](/docs/pt/CRM/address) são armazenados separadamente para que você possa anexar vários contatos ou endereços ao cliente.


### 3.3 Moeda e lista de preços


Você pode definir a moeda na qual a nota de entrega será enviada. Geralmente é obtido se definido no Pedido de Venda. Se você definir uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar Ignorar regra de preços ignorará as regras de preços definidas em Contas > Regra de preços.


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.4 Armazéns


* **Definir Armazém de Origem**: É aqui que os Itens serão originados para serem enviados ao Cliente.
* **Para o Armazém**: Em um cenário normal de Vendas, o Item sai do seu Armazém e chega ao Cliente. No entanto, se desejar reter estoque de amostra, insira um Armazém aqui.


### 3.5 Tabela de Itens


* **Código de barras**: você pode rastrear itens usando [códigos de barras](/docs/pt/stock/articles/track-items-using-barcode) .
* O código do item, nome, descrição, imagem e fabricante serão obtidos no [Mestre de itens](/docs/pt/stock/item) .
* **Ler código de barras**: você pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* **Desconto e Margem**: Você pode aplicar um desconto em itens individuais em termos percentuais ou no valor total do item. Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.
* **Taxa**: A taxa é obtida se definida na [Lista de preços](/docs/pt/stock/price-lists) e o valor total é calculado.
* **Modelo de imposto de item**: você pode definir um modelo de imposto de item para aplicar um valor de imposto específico a este item específico. Para saber mais, visite [esta página](/docs/pt/accounts/item-tax-template).
* Os detalhes do Peso do Item por unidade e a UOM do Peso são obtidos se definidos no Cadastro de Itens.
* **Armazém e Referência**: É apresentado o Armazém de onde os Artigos são enviados ao Cliente. Além disso, um Pedido de Venda será mostrado se esta Nota de Entrega for o fluxo de criação: 'Pedido de Venda > Nota de Entrega'.
* **Número do lote e número de série**: se o seu item for serializado ou em lote, você terá que inserir [Número de série](/docs/pt/stock/serial-no) e [Lote](/docs/pt/stock/batch) na tabela Itens. Você tem permissão para inserir vários números de série em uma linha (cada um em uma linha separada) e deve inserir o mesmo número de números de série que a quantidade.


A 'Quantidade disponível no armazém', 'Quantidade de lote disponível no armazém' e 'Quantidade instalada' serão mostradas. Para saber mais sobre a instalação, visite a página [Nota de instalação](/docs/pt/stock/installation-note).


**Observação**: o item precisa ser serializado ou em lote para que esses recursos funcionem. Se o item for serializado, um pop-up aparecerá onde você poderá inserir os números de série.
* Conta de Despesas é a conta da qual o valor será debitado. Marcar 'Permitir Taxa de Avaliação Zero' permitirá o envio da Nota de Entrega mesmo que a Taxa de Avaliação do Item seja 0. Este pode ser um item de amostra ou devido a um entendimento mútuo com seu Fornecedor.
* As Dimensões Contábeis ajudam a marcar cada transação com Dimensões diferentes sem a necessidade de criar novos Centros de Custo. Você precisa criar dimensões contábeis primeiro. Para saber mais, visite [esta página](/docs/pt/accounts/accounting-dimensions).
* **Quebra de página** criará uma quebra de página logo antes deste item durante a impressão.


### 3.6 Acompanhamento da inspeção de qualidade


Se para determinados Itens for obrigatório o registro de Inspeções de Qualidade (caso você tenha definido isso em seu Cadastro de Itens), será necessário atualizar o campo “Inspeção de Qualidade”. O sistema só permitirá que você “Envie” o
Nota de Entrega se você atualizar a “Inspeção de Qualidade”.


Depois de ativar os critérios de inspeção no [formulário de item](/docs/pt/stock/item#216-inspection-criteria) para vendas e anexar um modelo de inspeção de qualidade lá, as Inspeções de Qualidade podem ser registradas em Notas de Entrega.


### 3.7 Impostos e Taxas


Os impostos e taxas serão obtidos no [Pedido de venda](/docs/pt/buying/purchase-order).


Acesse o [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template)página para saber mais sobre impostos.


O total de impostos e taxas será exibido abaixo da tabela.


Para adicionar impostos automaticamente por meio de uma categoria de imposto, visite [esta página](/docs/pt/accounts/tax-category).


Certifique-se de marcar todos os seus impostos na tabela Impostos e Encargos corretamente para obter uma avaliação precisa.


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


### 3.8 Desconto adicional


Quaisquer descontos adicionais para todo o pedido podem ser definidos nesta seção. Este desconto pode ser baseado no total geral, ou seja, após impostos/encargos, ou no total líquido, ou seja, antes de impostos/encargos. O desconto adicional pode ser aplicado em forma de percentual ou valor.
Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.9 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 3.10 Informações do transportador


Se você terceirizar o transporte dos itens até o local de entrega, os detalhes do transportador poderão ser adicionados. Isso não é o mesmo que [envio direto](/docs/pt/selling/articles/drop-shipping).


* **Transportador**: O Fornecedor que transportará o Item até o seu Cliente. O recurso de transportador deve estar habilitado no cadastro de Fornecedores para selecionar o [Fornecedor](/docs/pt/buying/supplier) aqui.
* **Motorista**: você pode adicionar aqui um motorista que dirigirá o meio de transporte.


![Transporte de nota de entrega](/files/delivery-note-transport.png)


Os seguintes detalhes podem ser registrados:


* Distância em km
* Modo de transporte, seja rodoviário, aéreo, ferroviário ou marítimo.


Para a Índia, GST:


* ID do transportador GST
* Nº do recibo de transporte
* Número do veículo
O tipo de veículo GST pode ser alterado


A data do recibo de transporte e o nome do motorista serão obtidos.


### 3.11 Mais informações


A Nota de Entrega pode ser vinculada ao seguinte para fins de rastreamento:


* [Projeto](/docs/pt/projects/project)
* [Campanha](/docs/pt/CRM/campaign)
* [Fonte](/docs/pt/CRM/lead_source)


### 3.11 Configurações de impressão


#### Papel timbrado


Você pode imprimir sua Nota de Entrega em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados diversas vezes na tabela Itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


Os títulos do recibo de compra também podem ser alterados durante a impressão do documento. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


Existem caixas de seleção adicionais para imprimir a Nota de Entrega sem o valor, isso pode ser útil quando o Item for de alto valor. Você também pode agrupar os mesmos itens em uma linha ao imprimir.


### 3.12 Status


O status do documento e a porcentagem de instalação são mostrados aqui. Quaisquer instruções adicionais para entrega podem ser inseridas aqui.


### 3.13 Comissão


Se a venda ocorreu por meio de um de seus parceiros de vendas, você poderá adicionar os detalhes da comissão aqui. Geralmente, isso é obtido no pedido de vendas.


### 3.14 Equipe de vendas


**Vendedores:** O ERPNext permite que você adicione vários Vendedores que possam ter trabalhado neste negócio.


Isso geralmente é obtido de um pedido de venda, por exemplo:


![Equipe de vendas no pedido de vendas](/files/so-sales-team.png)


### 3.15 Envio de pacotes ou itens com pacote de produtos


Se você estiver enviando itens que possuem um [Pacote de produtos](/docs/pt/selling/product-bundle), o ERPNext criará automaticamente uma “Lista de embalagem” tabela para você com base nos subitens desse item.


Se seus itens forem serializados, para itens do tipo Pacote de Produtos, você terá
para atualizar o Número de Série na tabela “Packing List”.


### 3.16 Empacotando itens em caixas, para envio de contêineres


Se você estiver fazendo a entrega via contêiner ou por peso, poderá usar a opção Embalagem
Deslize para dividir sua Nota de Entrega em unidades menores. Para saber mais sobre uma guia de remessa, visite [esta página](/docs/pt/stock/packing-slip).
vá para:


Você pode criar vários comprovantes de entrega para sua nota de entrega e o ERPNext irá
garantir que as quantidades na guia de remessa não excedam as quantidades contidas
a Nota de Entrega. Observe que você só pode criar uma guia de remessa a partir de uma nota de entrega quando a nota de entrega estiver na fase Rascunho.


### 3.17 Após o envio


Quando a Nota de Entrega é enviada, um lançamento contábil de estoque é feito para cada item e o estoque é atualizado. Pendente
A quantidade no pedido de vendas é atualizada (se aplicável).


O Painel mostrará as seguintes opções:


* [Nota de instalação](/docs/pt/stock/installation-note)
* [Retorno de vendas](/docs/pt/stock/sales-return)
* [Viagem de entrega](/docs/pt/stock/delivery-trip)
* [Fatura de vendas](/docs/pt/accounts/sales-invoice)


![Nota de entrega após envio](/files/delivery-note-submit.png)


> Dica: para proibir a criação de Notas de Entrega sem um Pedido de Venda:


### 3.18 Devolução de um pedido de venda


Depois de entregar um pedido de vendas usando uma nota de entrega, você pode criar uma entrada de devolução caso o [Cliente](/docs/pt/CRM/customer) retorna o Item. Para saber mais, visite a página [Devolução de vendas](/docs/pt/stock/sales-return).


### 3.19 Ignorando nota de entrega


Se você não deseja criar uma nota de entrega após um pedido de venda e deseja criar diretamente uma fatura de venda, ative o recurso em [Configurações de venda](/docs/pt/selling/selling-settings#32-delivery-note-required).


### 4. Tópicos Relacionados


1. [Armazém](/docs/pt/stock/warehouse)
2. [Erro de estoque da nota de entrega](/docs/pt/stock/articles/delivery-note-stock-error)
3. [Transferência de material da nota de entrega e recibo de compra](/docs/pt/stock/articles/material-transfer-from-delivery-note)
4. [Nota de instalação](/docs/pt/stock/installation-note)
5. [Viagem de entrega](/docs/pt/stock/delivery-trip)



