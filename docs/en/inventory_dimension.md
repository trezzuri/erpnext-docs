
# Inventory Dimension




> Introduced in Version 14
> 
> 

Inventory dimensions in ERPNext are used to track an inventory with multiple parameters. By default, ERPNext allows to track an inventory using warehouses, batches, and serial numbers. If users want to track inventory with custom parameters then they can configure it using the Inventory Dimension feature. The user gets an option to select the Inventory Dimension on respective inventory documents as well in the stock ledger and stock balance report. With this feature, you can view dimension-wise stock ledger and stock balance reports.

To access the Inventory Dimension list, go to:


> Stock > Settings > Inventory Dimension
> 
> 

## Create Inventory Dimension

![new inventory dimension](/files/new-inventory-dimension.png)![]()

* Create a new record and select the Reference Document which you want to use as a custom Inventory Dimension.
* You can select any non-child document in the reference document.
* Next, the user has to put the dimension name against which the system will create a custom link field in the Applicable Documents.

## Applicable For Documents

### Apply to All Inventory Documents

![inventory dimension applicable for all inventory documents](/files/inventory-dimension-applicable-for-all-inventory-documents.png)![]()  


* It will be used to select the custom Dimension in the inventory-related documents.
* For example, the user has created Inventory Dimension with the name "Shelf" and enabled "Apply to All Inventory Document Types". Then the system will create the custom link field with the name "Shelf" in the inventory documents where Batch No and Serial No fields exist.

### Apply to Specific Document

![inventory dimension applicable for](/files/inventory-dimension-applicable-for.png)![]()  


* If the user wants to add Inventory Dimension to a specific document then they have to disable the checkbox "Apply to All Inventory Document Types" and select the respective document in the "Applicable to Document" field.
* Also if you want to add Inventory Dimension for a specific condition like for stock entry type Issue you want separate dimension as "From Shelf" and stock entry type Material Receipt you want separate dimension as "To Shelf" then that can be possible using "Applicable Condition"
* Applicable Condition only can be visible if "Apply to All Inventory Document Types" is disabled
* You can also use the "Type of Transaction" with options such as Inward or Outward for a condition.

## Use of Inventory Dimension

![inventory dimension on transaction](/files/inventory-dimension-on-transaction.png)![]()  


* Once the Inventory Dimension is created system will create the custom field in respective documents
* User gets an option to select the Inventory Dimension in the respective transaction.
* For example, if the user has added Inventory Dimension as "Shelf" in the Stock Entry Detail document. Then in the stock entry, the child table user gets an option to select shelf (see above image). Post submission of the stock entry system will create the stock ledgers with selected inventory dimensions.

## Validate Negative Stock

![](/files/fqvxY3m.png)![]()  


If user has enabled the "Validate Negative Stock" checkbox in the inventory dimension, system will not allow to make stock transactions if the respective dimensions has negative stock in the respective warehouse. If user has tried to create the stock transaction with negative stock for the inventory dimension then system will throw the below error

  


![](/files/OKgkIqS.png)![]()  


## Stock Balance and Stock Ledger Report

* Users can able to filter the Stock Balance and Stock Ledger report using Inventory Dimension
* With this feature, users can able to see Inventory Dimension wise available quantity

### Stock Balance Report

![inventory dimension stock balance](/files/inventory-dimension-stock-balance.png)![]()  


### Stock Ledger Report

![inventory dimension stock ledger](/files/inventory-dimension-stock-ledger.png)![]()  


  


Note:

User can only use the stock reconciliation with inventory dimensions to enter opening values and they can't use the stock reconciliation to modify the available stock or the valuation. Since we are not maintaining inventory dimensions wise valuation rate there is not sense to allow to modify valuation rate through stock reconciliation. in case if they tried to update the quantity or valuation rate through stock reconciliation, system will throw the below error

  


![](/files/cTOHcyI.png)![]()  





