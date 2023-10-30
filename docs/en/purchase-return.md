
# Purchase Return



**A purchased Item being returned is known as a Purchase Return.**


With the Purchase Return feature, you can return products to the
Supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc.


## 1. Prerequisites


Before creating and using a Purchase Return, it is advised that you create the following first:


* [Item](/docs/en/stock/item)
* [Purchase Invoice](/docs/en/accounts/purchase-invoice)


Or


[Purchase Receipt](/docs/en/stock/purchase-receipt)


## 2. How to create a Purchase Return


1. First open the original Purchase Receipt, against which supplier delivered the Items.


![Original Purchase Receipt](/files/purchase-return-original-purchase-receipt.png)
2. Click on 'Create > Return', it will open a new Purchase Receipt with 'Is Return' checked. Items, Rate, and taxes will negative numbers.


![Return Against Purchase Receipt](/files/purchase-return-against-purchase-receipt.png)
3. On submission of Return Purchase Return, the system will decrease item quantity from the mentioned Warehouse. To maintain correct stock valuation, stock balance will also go up according to the original purchase rate of the returned items.


![Return Stock Ledger](/files/purchase-return-stock-ledger.png)
4. In the Accounting Ledger, the Stock In Hand account will be credited and the Stock Received but Not Billed account will be debited.


![Return Stock Ledger](/files/purchase-return-general-ledger.png)


If Perpetual Inventory enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.


## 3. Impact on Stock Return via Purchase Receipt


On Creating a Purchase Return against a Purchase Receipt:


* The **Returned Quantity** in the original Purchase Receipt along with any Purchase Order linked to it, is updated.
* The original Purchase Receipt's status is changed to **Return Issued** if 100% returned:
![Return Issued](/files/purchase-return-issue.png)


### 4. Related Topics


1. [Sales Return](/docs/en/stock/sales-return)
2. [Perpetual Inventory](/docs/en/stock/perpetual-inventory)




