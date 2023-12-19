# Item



**Um item é um produto ou serviço oferecido pela sua empresa.**


O termo Item também se aplica a matérias-primas ou componentes de produtos ainda a serem produzidos (antes de serem vendidos aos clientes). O ERPNext permite que você gerencie todos os tipos de itens, como matérias-primas, subconjuntos, produtos acabados, variantes de itens e itens de serviço.


ERPNext é otimizado para gerenciamento detalhado de suas vendas e compras. Se você trabalha com serviços, pode criar um Item para cada serviço que oferece. Preencher o Item Master é essencial para o sucesso da implementação do ERPNext.


Para acessar a lista de itens, vá para:
> Home > Estoque > Itens e preços > Item


## 1. Pré-requisitos


Antes de criar e usar um item, é aconselhável criar primeiro o seguinte:


* [Grupo de itens](/docs/pt/stock/item-group)
* [Armazém](/docs/pt/stock/warehouse)
* Uma unidade de medida, se necessário


## 2. Como criar um item


1. Vá para a lista de itens e clique em novo.
2. Insira um código de item, o nome será preenchido automaticamente da mesma forma que o código do item ao clicar dentro do campo Nome do item.
3. Selecione um grupo de itens.
4. Insira as unidades de estoque iniciais e a taxa de venda padrão.
5. Salvar.
![Item salvo](/files/item-saved.png)


### 2.1 Propriedades do item


* **Nome do item:** O nome do item é o nome real do seu produto ou serviço.
* **Código do Item:** Código do Item é uma forma abreviada para denotar seu Item. Se você tiver poucos itens, é aconselhável manter o nome do item e o código do item iguais. Isso ajuda os novos usuários a reconhecer e atualizar os detalhes do item em todas as transações. Caso você tenha muitos itens com nomes longos e a lista chegue às centenas, é aconselhável codificar. Para entender a nomenclatura dos códigos de item, consulte [Codificação de item](/docs/pt/stock/articles/item-codification). Você também pode gerar código de item com base em uma [Série de nomenclatura](/docs/pt/setting-up/settings/naming-series) ativando esse recurso em [Configurações de estoque](/docs/pt/stock/stock-settings#1-item-naming-by).
* **Grupo de Itens:** Grupo de Itens é usado para categorizar um Item sob vários critérios, como produtos, matérias-primas, serviços, subconjuntos, consumíveis ou todos os grupos de Itens. Crie sua lista de Grupo de Itens padrão em Configuração > Grupo de Itens e pré-selecione a opção enquanto preenche os detalhes do Novo Item em [Grupo de Itens](/docs/pt/stock/item-group). Os grupos de itens podem ser submontagens, matérias-primas, etc., ou com base no seu caso de uso comercial.
* **Unidade de medida padrão:** esta é a unidade de medida padrão que você usará para seu produto. Podem ser Nos, Kgs, Metros, etc. Você pode armazenar todas as UOMs que seu produto exigirá em Configuração> Dados mestre> UOM. Eles podem ser pré-selecionados ao preencher o Novo Item usando o sinal % para obter um pop-up da lista UOM. Visite a página [UoM](/docs/pt/stock/uom) para obter mais detalhes


### 2.2 Opções ao criar um item


* **Desativado**: se você desativar um item, ele não poderá ser selecionado em nenhuma transação.
* **Permitir item alternativo**: Às vezes, ao fabricar um produto acabado, um material específico pode não estar disponível. Se você marcar esta opção, poderá criar e selecionar um item alternativo na lista Alternativa de item. Para saber mais, visite a página [Alternativa de item](/docs/pt/manufacturing/item-alternative).
* **Manter Estoque:** Se você estiver mantendo estoque deste Item em seu Inventário, o ERPNext fará um lançamento no livro razão de estoque para cada transação deste item. Certifique-se de manter esta opção desmarcada ao criar um item sem estoque (fabricado sob encomenda/engenheiro) ou um serviço.
* **Incluir Item na Fabricação**: Isto é para itens de matéria-prima que serão usados ​​para criar produtos acabados. Se o item for um serviço adicional como 'lavagem' que será usado na lista técnica, mantenha-o desmarcado.
* **Taxa de avaliação**: Existem duas opções para manter a avaliação das ações. FIFO (primeiro a entrar-primeiro a sair) e média móvel. Para entender este tópico em detalhes, visite [Avaliação de itens, FIFO e média móvel](/docs/pt/stock/articles/calculation-of-valuation-rate-in-fifo-and-moving-average).
* **Taxa de venda padrão**: ao *criar* um item, inserir um valor neste campo criará automaticamente um [Preço do item](/docs/pt/stock/item-price) no backend. Inserir um valor após o item ter sido salvo não funcionará. Neste caso, o Preço do Item é criado a partir de quaisquer transações com o Item. A taxa pela qual você venderá o item. Isso será obtido em pedidos de vendas e faturas de vendas.
* **É um ativo fixo**: marque esta caixa de seleção se este item for um ativo da empresa. Confira o [Módulo de ativos](/docs/pt/asset) para saber mais.
* **Criar ativos automaticamente na compra**: se o item for um ativo da empresa, marque esta caixa de seleção se desejar criar ativos automaticamente ao comprar este item por meio de [Ciclo de compra](/docs/pt/buying/purchase-order). Confira a [Página de recursos](/docs/pt/asset/asset) para saber mais.
* **Porcentagem de permissão**: esta opção estará disponível somente quando você criar e salvar o item. Esta é a porcentagem pela qual você poderá faturar ou entregar este item a mais. Se não for definido, ele selecionará [Configurações de estoque](/docs/pt/stock/stock-settings#3-limit-percent).
* **Enviando uma imagem**: Para enviar uma imagem para o seu ícone que aparecerá em todas as transações, salve o formulário parcialmente preenchido. Somente após o arquivo ser salvo o botão 'Alterar' aparecerá no ícone da imagem. Clique em Alterar, depois clique em Fazer upload e faça upload da imagem.


Para a Índia:


* **HSN/SAC**: Sistema Harmonizado de Nomenclatura (HSN) e Código de Contabilidade de Serviços (SAC) para GST. Esses números são definidos pelo governo e diferentes itens se enquadram em códigos diferentes. Novos códigos HSN podem ser adicionados se não estiverem presentes na lista.
* **Tem classificação nula ou isenta**: para um item que está sujeito ao GST, mas nenhum imposto é aplicado a ele. Ex.: Cereais.
* **Não é GST**: para um item que não é coberto pelo GST. Ex.: gasolina.


## 3. Recursos


### 3.1 Marca e descrição


* **Marca**: Se você tiver mais de uma marca, salve-as em Vendas > Marca e pré-selecione-as ao preencher um Novo Item.
* **Descrição**: Descrição do item. O texto do Código do Item será obtido por padrão.
![Marca e descrição do item](/files/item-brand-description.png)


### 3.2 Códigos de barras


Os códigos de barras podem ser gravados em Itens para digitalizá-los rapidamente e adicioná-los nas transações. Na tabela Códigos de barras, você pode adicionar o [código de barras de um item para digitalização](/docs/pt/stock/articles/track-items-using-barcode). Existem dois tipos de códigos de barras no ERPNext:


* **EAN**: O número de artigo europeu é um número de 13 dígitos. O EAN é usado internacionalmente e reconhecido por mais sistemas POS.
* **UPC**: o código universal do produto é um número de 12 dígitos. O UPC geralmente é usado apenas nos EUA e no Canadá.


### 3.3 Inventário


* **Prazo de validade em dias**: isto é para um produto [Lote](/docs/pt/stock/batch). O número de dias após os quais o lote do produto ficará inutilizável. Por exemplo, medicamentos.
* **Fim da vida útil**: Para um único item/produto, a data após a qual ele ficará completamente inutilizável. Ou seja, o item ficará inutilizável nas transações e na fabricação. Por exemplo, você usará cristais de plástico para fabricar itens pelos próximos 5 anos, após os quais deseja usar contas de plástico.
* **Garantia**: Para acompanhar o período de garantia, é necessário que o Item seja serializado. Quando este Item é entregue, a data de entrega e o prazo de validade são salvos no cadastro do Número de Série. Através do mestre do número de série, você pode acompanhar o status da garantia.


Um período de garantia é um período de tempo durante o qual um produto adquirido pode ser devolvido ou trocado.


![Garantia do item](/files/item-inventory.png)
* **UM de peso**: a unidade de medida do item. Pode ser Nos, Quilo, etc. A UM de peso que você usa internamente pode ser diferente da UM de compra.
* **Peso por unidade**: o peso real por unidade do item. Ex: 1 quilo de biscoitos ou 10 biscoitos por pacote.
* **Tipo de solicitação de material padrão**: quando você cria uma nova solicitação de material para este item, o campo definido aqui será selecionado por padrão na nova solicitação de material. Isso também é conhecido como 'recuo'.
* **Método de avaliação**: selecione o método de avaliação, seja FIFO ou média móvel. Leia [Métodos de avaliação de itens](/docs/pt/stock/articles/calculation-of-valuation-rate-in-fifo-and-moving-average) para saber mais .
* **Permitir estoque negativo**: When checked the item will be allowed to go negative even if negative stock is disabled from Stock Settings. This is useful if you don't want to enable negative stock on high value items but few select low value items are allowed to go negative for few days.


### 3.4 Automatic Reordering


When the stock of an item dips under a certain quantity, you can set an automatic reorder under 'Auto Reorder' section. This should be enabled in [Stock Settings](/docs/pt/stock/stock-settings#9-automatic-material-request). This will raise a [Material Request](/docs/pt/stock/material-request) for the Item. The user with roles Purchase Manager and Stock Manager will be **notified** when the Material Request is created.


* **Check in (group)**: In which group warehouses to check the quantity of the item.
* **Request for**: Which warehouse to stock the item reorder.
* **Re-order Level**: When this quantity is reached, the reorder will be triggered. Re-order level can be determined based on the lead time and the average daily consumption. For example, you can set the reorder level of Motherboard at 10. When only 10 Motherboards are remaining in stock, the system will either automatically create a Material Request in your ERPNext account.
* **Re-order Qty**: The number of units to be reordered so that the sum of ordering cost and holding cost is at its minimum. The re-order quantity is based on the 'Minimum Order Qty' specified by the supplier and many other factors.


For example, If reorder level is 100 items, your reorder quantity may not necessarily be 100 items. The Reorder quantity can be greater than or equal to the reorder level. It may depend upon lead time, discount, transportation and average daily consumption.
* **Material Request Type**: The [Material Request](/docs/pt/stock/material-request) type with which the stock will be reordered. This depends whether you buy the Item, manufacture it yourself or transfer it between Warehouses.


![Item Reorder](/files/item-reorder.png)


> **Note**: The Material Request is created at 12 midnight depending on the set reorder level.


### 3.5 Multiple Units of Measure


You can add alternate UoMs for an Item. If the default UoM in which you sell is numbers (NoS) but you receive it in Kilos, you can set an additional UoM with an appropriate conversion factor. For example, 500 Nos of screws = 1 Kilogram, so select Kilogram/Litre as UOM and set the conversion factor as 500. To know more about selling in different UoM, visit [this page](/docs/pt/selling/articles/Selling-in-different-UOM).


### 3.6 Serial Numbers


With Serial Numbers, you can track warranty and returns. In case any individual Item is recalled by the supplier the number system helps to track individual Item. The numbering system also manages expiry dates.


Please note that if you sell your items in thousands, and if the items are very small like pens or erasers, you need not serialize them.


In ERPNext, you will have to mention the Serial Number in some accounting entries. If your product is not a big consumer durable Item, if it has no warranty and has no chances of being recalled, avoid giving serial numbers.


![Serial No modal](/files/serial_no_modal.gif)


### 3.7 Batches


A set of Items can be manufactured in batches. This is useful for moving the batch and associate an expiry date with a certain batch.


* **Has Batch No**: Options for batch number, expiry date, and retaining sample stock will be revealed on ticking this checkbox. You cannot activate this if there is any pre-existing transaction for this item. If this is disabled, you'll have to enter the serial numbers manually for every transaction.
* **Batch Number Series**: Prefix that'll be applied to batch numbers. If you set 5x1SCR, then the first batch will be named like 5x1SCR00001 on first transaction/manufacture.
* **Automatically Create New Batch**: If the batch number is not mentioned in transactions, then they will be automatically created according to a format like AAAA.00001. If you always want to manually create a batch number for this item, leave this field blank. This setting will override 'Naming Series Prefix' in Stock Settings. Batch numbers can be set to be generated automatically if you manufacture the Items or can be entered manually if it comes from an external manufacturer.
* **Has Expiry Date**: If you tick this, the batch number will be created according to the expiry date. The expiry dates can be set in the 'Batch' master.
* **Retain Sample**: To retain a minimum number of sample stock of the item. You need to set a Sample Retention Warehouse in Stock Settings for this. To know more, [click here](/docs/pt/stock/retain-sample-stock).
* **Has Serial No**: This is similar to Batch Number Series, it'll be created when you make transactions/manufacture. If you set Serial Number Series as AA, then on the first transaction a serial number like AA00001 will be created.


> Tip: While entering an Item Code in an Items table, if the table requires inventory details, then depending on whether the entered item is batched or serialized, you can enter serial or batch numbers right away in a pop-up dialog.


![Batch No modal](/files/batch_no_modal.png)


> **Note**: Once you mark an item as serialized or batched or neither, you cannot change it after you have made a Stock Entry.


To know more, visit the [Stock Reconciliation](/docs/pt/stock/stock-reconciliation) page.


### 3.8 Variants


An Item Variant is a different version of a Item. To learn more about managing variants see [Item Variants](/docs/pt/stock/item-variants).


### 3.9 Item Defaults


In this section, you can define Company-wide transaction-related defaults for this Item.


* **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions with this item.
* **Default Price List:** Whether Standard Selling or Standard Buying. Likewise, you can also set the purchasing and selling default accounts
* **Supplier**: If a default supplier is set, this supplier will be selected for new purchase transactions.
* **Default Expense Account:** It is the account in which cost of the Item will be debited.
* **Default Income Account:** It is the account in which income from selling the Item will be credited.
* **Default Cost Center:** It is used for tracking expense for this Item.


![Item defaults](/files/item-defaults.png)


> Tip: You can add more rows for multiple companies.


### 3.10 Purchase, Replenishment Details


* **Default Purchase Unit of Measure**: The default UoM that will be used in Purchase transactions.
* **Minimum Order Qty**: The minimum quantity required for purchase transactions like Purchase Orders. If set, the system will not let you proceed with the purchase transaction if the item quantity in the purchase transaction is lesser than the quantity set in this field.
* **Safety Stock**: “Safety Stock” is used in the report “Itemwise Recommended Reorder Level”. Based on Safety Stock, average daily consumption and the lead time, the system suggests Reorder Level of an item.


Reorder Level = Safety Stock + (Average Daily Consumption \* Lead Time)
* **Last Purchase Rate**: The rate at which you last purchased this item using a [Purchase Invoice](/docs/pt/accounts/purchase-invoice) will be displayed here.
* **Is Purchase Item:** If unticked, you won't be able to use this item in purchase transactions.
* **Is Customer Provided Item:** Checked if Item is provided by a customer and received through **Stock Entry > Material Receipt**. If Checked, **Customer** field is Mandatory as the default customer for **Material Request**. To know more visit [this page](/docs/pt/manufacturing/articles/customer-provided-items).
* **Lead time days:** Lead time days are the number of days between ordering the Item and it to reach the Warehouse.


![Purchase details](/files/item-purchase-details.png)


### 3.11 Supplier Details


* **Delivered by Supplier (Drop Ship)**: If the item is delivered directly by the supplier to the customer, tick this checkbox. Read more [here](/docs/pt/selling/articles/drop-shipping).
* **Supplier Codes:** Track Item Code defined by the Suppliers for this Item. In the Purchase transactions, on selecting an Item, a Supplier Part No. will be fetched as well for the Supplier's reference. You can read more about it [here](/docs/pt/buying/articles/maintaining-suppliers-part-no-in-item).


![Item Supplier Details](/files/item-supplier.png)


### 3.12 Foreign Trade Details


If you're sourcing the item from another country, you can set the details here.


* **Country of Origin**: The country from which you're sourcing the item.
* **Customs Tariff Number**: You can create a customs tariff number with a description and use it for reference here to share with custom agencies. Later it can be used to add in Delivery Notes.


### 3.13 Sales Details


* **Grant Commission**: Grant a commission to [Sales Person](/docs/pt/CRM/sales-person) and [Sales Partner](/docs/pt/selling/sales-partner) when this item is sold. If disabled, the sales generated by this item will be ignored in the calculation of commission.
* **Default Sales Unit of Measure**: The default UoM that'll be fetched for sales transactions.
* **Max Discount (%)**: You can define the maximum discount in % to be applied to an item. Eg: if you set 20%, you cannot sell this item with a discount greater than 20%.
* **Is Sales Item**: If unticked, you won't be able to use this item in sales transactions.


![Item Sales Details](/files/item-sales.png)


### 3.14 Deferred Revenue and Deferred Expense


You can enable deferred revenue or expense from the item. Once you tick the checkbox, you'll see options to set the Deferred Expense Account and the number of months through which the revenue/expense is deferred.


For example, consider a yearly gym membership, you pay the money upfront at once but the service is given throughout the year. For the gym owner, this is deferred revenue and for the customer, it is a deferred expense.


![Deferred Revenue](/files/deferred-revenue.png)


Check out the pages on [Deferred Revenue](/docs/pt/accounts/deferred-revenue) for more details.


### 3.15 Customer Details


The Customer may identify an Item with a different Item Code. this is Similar to [Supplier Code](/docs/pt/stock/item#311-supplier-details).


* **Customer Name**: Select a customer here.
* **Customer Group**: This will be fetched based on the Customer you selected in the previous field.
* **Ref Code:** A customer can identify this item with a different number. You can track Item Code assigned by the Customer for this Item. When you create a Sales Order, the Customer's Reference Code for this Item will be shown.


### 3.16 Item Tax


These settings are required only if a particular Item has a different tax rate than the rate defined in the standard tax Account.


You need to create a new 'Item Tax Template' or choose an existing one. For example, if you have a tax Account, “VAT 14%” and this particular Item is exempted from tax, then you select “VAT 14%” in the first column, and set “0” as the tax rate in the second column. Visit the [Item Tax Template](/docs/pt/accounts/item-tax-template) page for more details.


![Item tax template](/files/item-tax-template.png)


You can also set a [Tax Category](/docs/pt/accounts/tax-category) for this Item.


### 3.17 Inspection Criteria


* **Inspection Required before Purchase**: If an inspection is mandatory before the item is purchased, i.e., before you generate Purchase Receipt, tick this checkbox.
* **Inspection Required before Delivery**: If an inspection is required at the time of delivery from your Supplier is mandatory for this Item, tick this checkbox. That is, before you generate a Delivery Note.
* **Quality Inspection Template**: If a Quality Inspection is prepared for this Item, then this template of criteria will automatically be updated in the Quality Inspection table of the Quality Inspection. Examples of Criteria are: Weight, Length, Finish, etc.


Quality Inspection can be done with Quick View and you need not go to a different page to update the details inspection in ERPNext.


Read [Quality Inspection](/docs/pt/stock/quality-inspection) to know more.


### 3.18 Manufacturing


* **Default BOM**: The default [Bill of Materials](/docs/pt/manufacturing/bill-of-materials) used to manufacture this Item.
* **Supply Raw Materials for Purchase**: If you're subcontracting to a vendor, you can choose to provide them with the raw materials to manufacture the item using the default BOM.
* **Manufacturer:** Select the Manufacturer who manufactured this item.
* **Manufacturer Part Number:** Enter the manufacturer part number that the manufacturer has assigned to this item.


![Item Manufacturing](/files/item-manufacturing.png)
* The manufacturer details appear after you've created an 'Item Manufacturer' from the dashboard and selected that record as default. Here, add details for:


	+ Item Code
	+ Enter the manufacturer name
	+ Enter the part number the manufacturer uses to identify this item
	+ Select 'Is Default' to show the manufacturer and part number in the Item record![Item Manufacturer](/files/item-manufacturer.png)


### 3.19 Website


* **Show in Website**: Choose if you want to show this Item on your website. Once you tick this, additional options will be visible to configure the item on your website. To view the item on the website click on the 'See on Website' link on the top left just above the item image. Visit the [Website module](/docs/pt/website) to know more.


![Manufaturing details](/files/item-manufacturing-website.png)
* **Weightage**: Items with higher weight will be displayed first on the website. The limit for the number you can enter here is very high.
* **Slideshow**: A slideshow can be displayed at the top of the page. Visit the [Homepage](/docs/pt/website/homepage) page in Website module to know more.
* **Image**: You can attach an image instead of a Slideshow.
* **Website Warehouse**: Select an existing or create a new warehouse for transactions via your website. This Warehouse will be different from your offline Warehouses. Stock for any online transactions will be deducted from the Warehouses set under Website Warehouse.
* **Website Item Groups**: In this table you can select existing or create new [Item Groups](/docs/pt/stock/item-group) to classify items on your website.
* **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/docs/pt/website/web-page) to know how to add them.


Visit [Manufacturing](/docs/pt/manufacturing) and [Website](/docs/pt/website) to understand these topics in detail.


### 3.20 Website Specifications


This section is for configuring other details about the item.


* **Copy from Item Group:** The 'Website Specifications' details will be fetched as set in a specific Item Group chosen on the previous section (2.17).
* **Website Specifications**: Label and its description for the item. For example, 'Warranty: 1 year'.
* **Website Description**: This will appear on the item page.
* **Website Content**: (*Introduced in v12*) You can create additional styling, etc., use Bootstrap 4 markup to display on the item page.


### 3.21 Hub Publishing Details


The hub is a free online marketplace where Suppliers and Customers can transact. If both parties are on ERPNext, the transactions happen seamlessly. You can visit the hub at: https://hubmarket.org.


* **Publish in Hub**: Choose if you want to publish your item on https://hubmarket.org/. It is a free marketplace. If your supplier/customer is also on ERPNext, the transactions will be seamless. For example, on creating a Purchase Order from your end, a Sales Order will be created on the Supplier's end.
* **Hub Warehouse**: This is a separate Warehouse to maintain the stock for your hub transactions.
* **Synced With Hub**: Sync item and other details with the hub when transactions take place.


## 4. Video








### 5. Related Topics


1. [Item Price](/docs/pt/stock/item-price)
2. [Item Codification](/docs/pt/stock/articles/item-codification)
3. [Item Variants](/docs/pt/stock/item-variants)
4. [Item Group](/docs/pt/stock/item-group)
5. [Item Attribute](/docs/pt/stock/item-attribute)
6. [Item Valuation FIFO And Moving Average](/docs/pt/stock/articles/calculation-of-valuation-rate-in-fifo-and-moving-average)
7. [Maintain Stock Field Frozen In Item Master](/docs/pt/stock/articles/maintain-stock-field-frozen-in-item-master)
8. [Track Items Using Barcode](/docs/pt/stock/articles/track-items-using-barcode)
9. [Serial Number](/docs/pt/stock/serial-no)




