
# Brand



**A Brand identifies items with a specific name.**


Usually, a Brand is the manufacturer or packer of a specific product. For example, Apple is a brand that manufactures laptops. A Brand is not necessarily the [Manufacturer](/docs/en/stock/manufacturer) of an Item, it's only the name under which a product is sold. For example, if you manufacture plastic cups, you may license it to a big brand so that they sell it under their Brand.


In ERPNext, Brands can be assigned to Items for identifying and assigning certain defaults.


To access the Brand list, go to:



> 
> Home > Selling > Sales > Brand
> 
> 
> 


## 1. How to Create a Brand


1. Go to the Brand list and click on New.
2. Enter a Brand name and enter a description if needed.
3. Save.


![Brand](/files/brand.png)


Now this Brand can be associated with different Items.


![Brand in Item](/files/brand-in-item.png)


## 2. Features


### 2.1 Setting defaults for Items of this Brand


![Brand Defaults](/files/brand-defaults.png)


The following defaults can be set for a Brand. On assigning this brand to an Item, the set defaults will be fetched when performing Sales/Purchase transactions with Item of this Brand.


* **Default Warehouse**: The Warehouse from which the Item will be sourced/stored depending on the transaction.
* **Default Price List**: The Price List set here will be fetched in Purchase/Sales transactions.


#### Purchase Defaults


When performing Purchase transactions like Purchase Order, Purchase Receipt, or Purchase Invoice, the defaults set here will be fetched on selecting Item of this Brand.


* Default Buying Cost Center
* Default Supplier
* Default Expense Account


#### Sales Defaults


When performing Sales transactions like Sales Order, Delivery Note, or Sales Invoice, the defaults set here will be fetched on selecting Item of this Brand.


* Default Selling Cost Center
* Default Income Account


## 3. Related Topics


1. [Purchase Order](/docs/en/buying/purchase-order)
2. [Sales Order](/docs/en/selling/sales-order)
3. [Purchase Receipt](/docs/en/stock/purchase-receipt)
4. [Delivery Note](/docs/en/stock/delivery-note)
5. [Sales Invoice](/docs/en/accounts/sales-invoice)
6. [Purchase Invoice](/docs/en/accounts/purchase-invoice)




