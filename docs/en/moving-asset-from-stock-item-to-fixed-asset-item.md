
# Moving Asset from Stock Item to Fixed Asset Item



**Question:** We have added Asset Item as a Stock / consumable Item. How to move this item to Fixed Asset register, so that Depreciation can be applied on it?  
**Answer:** Please follow the steps given below to have stock item moved to fixed asset item.  
### **Stocking Out Consumable Item**

  
1. Create a Stock Entry of type **Material Issue**
2. Select Items, with respective Source Warehouse, where stock of item is available
3. For an item, select "Stock Adjustment" as a Difference Account.

  
On submission of this Stock Entry, the item in question will be completely stock-out from your Warehouse. Also, the item's valuation will be debited in the Stock Adjustment Account.  
### **Adding Item as Fixed Asset Item**

  
1. Create a New Asset from Assets > New
2. In the Asset master, select Item and enter relevant details
3. Select "Is Existing Asset" as **Yes**.

  
And then again, to update fixed asset account, you have to pass a Journal Entry where you can debit the Fixed Asset account and credit the Stock adjustment account.


