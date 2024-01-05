# Fatura de vendas



**Uma fatura de vendas é uma fatura que você envia aos seus clientes, contra a qual o cliente efetua o pagamento.**


A fatura de vendas é uma transação contábil. Ao enviar a fatura de vendas, o sistema atualiza as contas a receber e registra a receita em uma conta do cliente.


Para acessar a lista de Faturas de Vendas, acesse:
> Home > Contabilidade > Contas a Receber > Fatura de Venda


![SO Flow](/files/so-flow.png)


## 1. Pré-requisitos


Antes de criar e usar uma fatura de vendas, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Cliente](/docs/pt/CRM/customer)
* Opcional:


	+ [Ordem de vendas](/docs/pt/selling/sales-order)
	+ [Nota de entrega](/docs/pt/stock/delivery-note)


## 2. Como criar uma fatura de vendas


Uma fatura de venda geralmente é criada a partir de um pedido de venda ou de uma nota de entrega. Os detalhes do item do cliente serão inseridos na fatura de vendas. No entanto, você também pode criar uma fatura de vendas diretamente, por exemplo, uma fatura de PDV.


Para obter os detalhes automaticamente em uma fatura de vendas, clique em **Obter itens de**. Os detalhes podem ser obtidos em um pedido de venda, nota de entrega ou cotação.


Para criação manual, siga estas etapas:


1. Vá para a lista Fatura de vendas e clique em Novo.
2. Selecione o cliente.
3. Defina a data de vencimento do pagamento.
4. Na tabela Itens, selecione os Itens e defina as quantidades.
5. Os preços serão obtidos automaticamente se [Preço do item](/docs/pt/stock/item-price) for adicionado, caso contrário, adicione um preço na tabela.
6. A data e hora da postagem serão definidas como atuais. Você pode editar depois de marcar a caixa de seleção abaixo de Horário da postagem para fazer uma entrada retroativa.
7. Salvar e enviar.
![Nova fatura de vendas](/files/new-sales-invoice.png)


### 2.1 Opções adicionais ao criar uma fatura de vendas


* **Incluir Pagamento (POS)**: Se esta fatura for para vendas no varejo/ponto de venda. [Saiba mais aqui](/docs/pt/accounts/sales-invoice#324-pos-invoices).
* **É Nota de Crédito de Devolução**: Marque esta opção se o cliente tiver devolvido os Itens. Para saber mais detalhes, visite a página [Nota de crédito](/docs/pt/accounts/credit-note).


![Opções de PDV e notas de crédito](/files/pos-and-credit-note-in-sales-invoice.png)


Para a Índia:
**e-Way Bill Não**: De acordo com as regras do GST, os transportadores precisam portar uma e-Way Bill. Para saber como gerar uma fatura eletrônica, [visite esta página](/docs/pt/regional/india/auto-generate-e-way-bill-JSON).


### 2.2 Status


Esses são os status atribuídos automaticamente à fatura de vendas.


* **Rascunho**: um rascunho foi salvo, mas ainda não foi enviado.
* **Enviada**: a fatura foi enviada ao sistema e o razão geral foi atualizado.
* **Pago**: o cliente fez o pagamento e uma [Entrada de pagamento](/docs/pt/accounts/payment-entry) foi enviado.
* **Não paga**: a fatura é gerada, mas o pagamento está pendente, mas dentro da data de vencimento.
* **Atrasado**: o pagamento está pendente além da data de vencimento.
* **Cancelada**: A fatura de venda foi cancelada por qualquer motivo. Quando uma fatura é cancelada, seu impacto na conta e no estoque é desfeito.
* **Nota de Crédito Emitida**: O Item é devolvido pelo Cliente e uma [Nota de Crédito](/docs/pt/accounts/credit-note) é criado nesta fatura.
* **Devolução**: É atribuído à Nota de Crédito criada em relação à Nota Fiscal de Venda original. Embora você também possa criar uma nota de crédito independente.
* **Não pago e com desconto**: o pagamento está pendente e qualquer assinatura em andamento foi descontada usando o [Desconto na fatura.](/docs/pt/accounts/invoice_discounting)
* **Atrasados ​​e com desconto**: o pagamento está pendente além da data de vencimento e qualquer assinatura em andamento foi descontada usando [Desconto na fatura](/docs/pt/accounts/invoice_discounting).


## 3. Recursos


### 3.1 Datas


* **Data de lançamento**: a data em que a fatura de venda afetará seus livros de
contas, ou seja, seu Razão Geral. Isso afetará todos os seus saldos naquele
período contábil.
* **Data de Vencimento**: A data de vencimento do pagamento (se você tiver vendido a crédito).
O limite de crédito pode ser definido no [Cliente](/docs/pt/CRM/customer#24-credit-limit-and-payment-terms) mestre.


### 3.2 Dimensões contábeis


As Dimensões Contábeis permitem marcar transações com base em um Território, Filial, Cliente específico, etc. Isso ajuda a visualizar os demonstrativos contábeis separadamente com base nas dimensões selecionadas. Para saber mais, consulte a ajuda no recurso [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions).


> Observação: Projeto e Centro de Custo são tratados como dimensões por padrão.


### 3.3 Detalhes da ordem de compra do cliente


* **Ordem de compra do cliente**: rastreie o número da ordem de compra recebida do cliente, principalmente para evitar a criação de ordem de venda ou fatura duplicada para a mesma ordem de compra recebida do cliente. Você pode fazer mais configurações relacionadas à validação do número do pedido de compra do cliente em [Configurações de venda](/docs/pt/selling/selling-settings#44-allow-multiple-sales-orders-against-a-customers-purchase-order)
* **Data do pedido de compra do cliente**: a data em que o cliente fez o pedido de compra.


![Detalhes do pedido de compra](/files/purchase-order-details-in-invoice.png)


### 3.4 Endereço e contato


* **Endereço do Cliente:** este é o endereço de cobrança do cliente.
* **Pessoa de Contato**: Se o Cliente for uma empresa, a pessoa a ser contatada é buscada neste campo se definida no [Formulário do cliente](/docs/pt/CRM/cliente).
* **Território:** Um [Território](/docs/pt/selling/territory) é a região à qual o Cliente pertence, obtido de o formulário do Cliente. O valor padrão é Todos os Territórios.
* **Endereço de envio:** Endereço para onde os itens serão enviados.


Para a Índia, os detalhes a seguir podem ser registrados para fins de GST. Você pode capturar esses dados no cadastro de Endereço e Cliente, que seria buscado na Nota Fiscal de Venda.


* Endereço de cobrança GSTIN
* GSTIN do cliente
* Local de fornecimento
* GSTIN da empresa


### 3,5 Moeda


Você pode definir a moeda na qual o pedido da fatura de vendas será enviado. Isso pode ser obtido no cadastro do Cliente ou em transações anteriores, como Pedido de Venda.


* Deseja selecionar a moeda do Cliente apenas para referência do Cliente, enquanto o lançamento das contas será feito apenas na moeda base da Empresa. Saiba mais [aqui](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency).
* Mantenha uma conta a receber separada na moeda do Cliente. A conta a receber desta fatura deve ser lançada nessa própria moeda. Leia [Contabilidade multimoeda](/docs/pt/accounts/multi-currency-accounting) para saber mais.


### 3.6 Lista de preços


Se você selecionar uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar 'Ignorar regra de preços' irá ignorar as [Regras de preços](/docs/pt/accounts/pricing-rule) definidas em Contas > Regra de preços.


Leia a [documentação da lista de preços](/docs/pt/stock/price-lists) para saber mais.


### 3.7 A tabela de itens


> Nota: A partir da versão 13 introduzimos o livro-razão imutável que altera as regras para cancelamento de entradas de estoque e lançamento de transações de estoque retroativas no ERPNext. [Saiba mais aqui](/docs/pt/accounts/articles/immutable-ledger-in-erpnext).


* **Atualizar estoque**
Marcar esta caixa de seleção atualizará o razão de estoque ao enviar a fatura de vendas. Se você criou uma nota de entrega, o razão de estoque será alterado. Se você estiver **ignorando** a criação da Nota de Entrega, marque esta caixa de seleção.
* **Ler código de barras**: você pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* **Conceder Comissão**: conceda uma comissão ao [Vendedor](/docs/pt/CRM/sales-person) e [Parceiro de vendas](/docs/pt/selling/sales-partner) sobre o valor líquido deste item de linha. Se desativado, este item de linha será ignorado no cálculo da comissão.
* The Item Code, name, description, Image, and Manufacturer will be fetched from the [Item master](/docs/pt/stock/item).
* **Discount and Margin**: You can apply a discount on individual Items percentage-wise or on the total amount of the Item. Read [Applying Discount](/docs/pt/selling/articles/applying-discount) for more details.
* **Rate**: The Rate is fetched if set in the [Price List](/docs/pt/stock/price-lists) and the total Amount is calculated.
* **Drop Ship**: Drop Shipping is when you make the sales transaction, but the Item is delivered by the Supplier. To know more, visit the [Drop Shipping](/docs/pt/selling/articles/drop-shipping) page.
* **Accounting Details**: The Income and Expense accounts can be changed here you you wish to. If this Item is an [Asset](/docs/pt/asset/asset), it can be linked here. This is useful when you're [selling an Asset](/docs/pt/asset/selling-an-asset).
* **Deferred Revenue**: If the income for this Item will be billed over the coming months in parts, then tick on 'Enable Deferred Revenue'. To know more, visit the [Deferred Revenue page](/docs/pt/accounts/deferred-revenue).
* **Item Weight**: The Item Weight details per unit and Weight UOM are fetched if set in the Item master.
* **Stock Details**: The following details will be fetched from the Item master:


	+ **Warehouse**: The Warehouse from where the stock will be sent.
	+ **Available Qty at Warehouse**: The quantity available in the selected Warehouse.
* **Batch No and Serial No**: If your Item is serialized or batched, you will have to enter [Serial Number](/docs/pt/stock/serial-no) and [Batch](/docs/pt/stock/batch) in the Items table. You are allowed to enter multiple Serial Numbers in one row (each on a separate line) and you must enter the same number of Serial Numbers as the quantity.
* **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit [this page](/docs/pt/accounts/item-tax-template).
* References: If this Sales Invoice was created from a Sales Order/Delivery Note, it'll be referred here. Also, the Delivered Quantity will be shown.
* **Page Break** will create a page break just before this Item when printing.


### 3.8 Timesheet


If you want to bill Employees working on Projects on an hourly basis (contract based),
they can fill out Timesheets which consists of their billing rate. When you make a new
Sales Invoice, select the Project for which the billing is to be made, and the
corresponding Timesheet entries for that Project will be fetched.


If your Company's Employees are working at a location and it needs to be billed, you can create an Invoice based on the Timesheet.


![SI Timesheet](/files/timesheet-in-sales-invoice.png)


To know more, [visit this page](/docs/pt/projects/sales-invoice-from-timesheet).


### 3.9 Taxes and Charges


The Taxes and Charges will be fetched from the [Sales Order](/docs/pt/selling/sales-order) or [Delivery Note](/docs/pt/stock/delivery-note).


Visit the [Sales Taxes and Charges Template](/docs/pt/selling/sales-taxes-and-charges-template) page to know more about taxes.


The total taxes and charges will be displayed below the table.


To add taxes automatically via a Tax Category, visit [this page](/docs/pt/accounts/tax-category).


Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.


![SI Tax](/files/taxes-in-sales-invoice.png)


#### Shipping Rule


A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/docs/pt/selling/shipping-rule) page.


### 3.10 Loyalty Points Redemption


If the Customer is enrolled in a Loyalty Program, they can choose to redeem it. To know more, visit the [Loyalty Program](/docs/pt/accounts/loyalty-program) page.


### 3.11 Additional Discount


Any additional discounts to the whole Invoice can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.
Visit the [Applying Discount](/docs/pt/selling/articles/applying-discount) page for more details.


![Additional Discount in Sales Invoice](/files/additional-discount-in-sales-invoice.png)


### 3.12 Advance Payment


For high-value Items, the seller can request an advance payment before processing the order. The **Get Advances Received** button opens a popup from where you can fetch the orders where the advance payment was made. To know more, visit the [Advance Payment Entry](/docs/pt/accounts/advance-payment-entry) page.


### 3.13 Payment Terms


The payment for an invoice may be made in parts depending on your understanding with the Supplier. This is fetched if set in the Sales Order. To know more, visit the [Payment Terms](/docs/pt/accounts/payment-terms) page.


### 3.14 Write Off


Write off happens when the Customer pays an amount less than the invoice amount. This may be a small difference like 0.50. Over several orders, this might add up to a big number. For accounting accuracy, this difference amount is 'written off'. To know more, visit the [Payment Terms](/docs/pt/accounts/payment-entry#25-deductions-or-loss) page.


### 3.15 Terms and Conditions


There may be certain terms and conditions on the Item you're selling, these can be applied here. Read [Terms and Condition documentation](/docs/pt/setting-up/print/terms-and-conditions) to know how to add them.


### 3.16 Transporter Information


If you outsource transporting Items to their delivery location, the transporter details can be added. This is not the same as [drop shipping](/docs/pt/selling/articles/drop-shipping).


* **Transporter**: The Supplier who will transport the Item to your Customer. The transporter feature should be enabled in the Supplier master to select the [Supplier](/docs/pt/buying/supplier) here.
* **Driver**: You can add a Driver here who will drive the mode of transport.


The details are usually fetched from the Delivery Note.


![Delivery Note Transport](/files/transporter-details-in-sales-invoice.png)


The following details can be recorded:


* Distance in km
* Mode of Transport whether road, air, rail, or ship.


For India, GST:


* GST Transporter ID
* Transport Receipt No
* Vehicle No
The GST Vehicle Type can be changed


The Transport Receipt Date and Driver Name will be fetched.


### 3.17 Printing Settings


#### Letterhead


You can print your Sales Invoice on your Company's letterhead. Know more [here](/docs/pt/setting-up/print/letter-head).


'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.


#### Print Headings


Sales Invoice headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/pt/setting-up/print/print-headings).


There are additional checkboxes for printing the Sales Invoice without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.


### 3.18 GST Details (for India)


The following details can be set for GST:


* GST Category
* Invoice Copy
* Reverse Charge
* E-commerce GSTIN
* Print Heading


### 3.19 More Information


The following Sales details can be recorded:


* **Campaign**: If this invoice is a part of on ongoing sales Campaign, it can be linked. To know more, visit the [Campaign page](/docs/pt/CRM/campaign).
* **Source**: A Lead Source can be tagged here to know the source of sales. To know more, visit the [Lead Source](/docs/pt/CRM/lead_source) page.


![SI More info](/files/more-information-in-sales-invoice.png)


### 3.20 Accounting Details


* **Debit To**: The account against which receivable will be booked for this Customer.
* **Is Opening Entry**: If this is an opening entry to affect your accounts select 'Yes'. i.e. if you're migrating from another ERP to ERPNext mid year, you might want to use an Opening Entry to update account balances in ERPNext.
* **Remarks**: Any additional remarks about the Sales Invoice can be added here.


![Accounting Details](/files/accounting-details-in-sales-invoice.png)


### 3.21 Commission


If the sale took place via one of your Sales Partners, you can add their commission details here. This is usually fetched from the Sales Order/Delivery Note.


### 3.22 Sales Team


**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal. This is also fetched from the Sales Order/Delivery Note.


### 3.23 Automatically Fetching Item Batch Numbers


If you are selling an Item from a [Batch](/docs/pt/stock/batch),
ERPNext will automatically fetch a batch number for you if "Update Stock"
is checked. The batch number will be fetched on a First Expiring First Out
(FEFO) basis. This is a variant of First In First Out (FIFO) that gives the highest priority to the soonest to expire Items.


Note that if the first batch in the queue cannot satisfy the order on the invoice,
the next batch in the queue that can satisfy the order will be selected. If no batch can satisfy the order, ERPNext will cancel its attempt to automatically fetch a suitable batch number.


### 3.24 POS Invoices


Consider a scenario where the retail transaction is carried out. For e.g: A retail shop.
If you check the **Is POS** checkbox, then all your **POS Profile** data is fetched
into the Sales Invoice and you can easily make payments.


Also, if you check the **Update Stock** the stock will also update automatically,
without the need for a Delivery Note.


![POS Invoice](/files/pos-sales-invoice.png)


### 3.25 After Submitting


On submitting a Sales Invoice, the following documents can be created against it:


1. [Journal Entry](/docs/pt/accounts/journal-entry)
2. [Payment Entry](/docs/pt/accounts/payment-entry)
3. [Payment Request](/docs/pt/accounts/payment-request)
4. [Invoice Discounting](/docs/pt/accounts/invoice_discounting)
5. [Delivery Note](/docs/pt/stock/delivery-note)


![SI Submit](/files/sales-invoice-post-submit.png)


## 4. More


### Accounting Impact


All Sales must be booked against an “Income Account”. This refers to an
Account in the “Income” section of your Chart of Accounts. It is a good
practice to classify your income by type (like product income, service income, etc). The Income Account must be set for each row of the Items table.


> Tip: To set default Income Accounts for Items, you can set it in the Item or
Item Group.


The other account that is affected is the Account of the Customer. That is
automatically set from “Debit To” in the heading section.


You can also mention the Cost Centers in which your Income must be booked.
Remember that your Cost Centers tell you the profitability of the different
lines of business or product. You can also set a default Cost Center in the
Item master. See also: [Accounting Dimensions](/docs/pt/accounts/accounting-dimensions).


### Accounting entries (GL Entry) for a typical double entry “Sale”:


When booking a sale (accrual):


* **Debit:** Customer (grand total)
* **Credit:** Income (net total, minus taxes for each Item)
* **Credit:** Taxes (liabilities to be paid to the government)


![SI Ledger](/files/ledger-updates-on-sales-invoice-submission.png)


> To see entries in your Sales Invoice after you “Submit”, click on “View
Ledger”.


## 5. Related Topics


1. [Cost Center](/docs/pt/accounts/cost-center)
2. [Journal Entry](/docs/pt/accounts/journal-entry)
3. [Payment Entry](/docs/pt/accounts/payment-entry)
4. [Purchase Invoice](/docs/pt/accounts/purchase-invoice)
5. [Purchase Receipt](/docs/pt/stock/purchase-receipt)
6. [Item Wise Taxation](/docs/pt/accounts/item-tax-template)
7. [Sales Order](/docs/pt/selling/sales-order)
8. [Quotation](/docs/pt/selling/quotation)
9. [Delivery Note](/docs/pt/stock/delivery-note)




