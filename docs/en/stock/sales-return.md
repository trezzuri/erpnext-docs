
# Sales Return



**A sold Item being returned is known as a Sales Return.**


Businesses often return goods that are already sold. They could be returned by the customer due to quality issues, non-delivery on the agreed date, or any other reason.


## 1. Prerequisites


Before creating and using a Sales Return, it is advised that you create the following first:


* [Item](/docs/en/stock/item)
* [Sales Invoice](/docs/en/accounts/sales-invoice) or [Delivery Note](/docs/en/stock/delivery-note)


## 2. How to create a Sales Return


1. First open the original Delivery Note / Sales Invoice, against which Customer returned the Items.


![Original Delivery Note](/files/sales-return-original-delivery-note.png)
2. Then click on 'Create > Sales Return', it will open a new Delivery Note with 'Is Return' checked, Items, Rate, and taxes will negative numbers.


![Return Against Delivery Note](/files/sales-return-against-delivery-note.png)
3. You can also create the return entry against the original Sales Invoice, to return stock along with credit note, check "Update Stock" option in Return Sales Invoice.


![Return Against Sales Invoice](/files/sales-return-against-sales-invoice.png)
4. On submission of Return Delivery Note / Sales Invoice, the system will increase stock balance in the mentioned Warehouse. To maintain correct stock valuation, stock balance will go up according to the original purchase rate of the returned items.


![Return Stock Ledger](/files/sales-return-stock-ledger.png)
5. In case of Return Sales Invoice, Customer account will be credited and associated income and tax account will be debited as shown in the Accounting Ledger.


![Return Stock Ledger](/files/sales-return-general-ledger.png)


If Perpetual Inventory is enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.


## 3. Impact on Stock Return via Delivery Note


On Creating a Sales Return against a Delivery Note:


* The **Returned Quantity** in the original Delivery Note along with any Sales Order linked to it, is updated.
* The original Delivery Note's status is changed to **Return Issued** if 100% returned:
![Return Issued](/files/sales-return-issue.png)


## 4. Related Topics


1. [Purchase Return](/docs/en/stock/purchase-return)
2. [Perpetual Inventory](/docs/en/stock/perpetual-inventory)




