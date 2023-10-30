
# Cannot enable Serial and Batch Number



It is quite possible at times that you do not want to start tracking the inventory as batched and/or serialized but want to start doing so at a later stage.   
The system, by design, doesn't allow you to activate these options once stock transactions have been made.![](/files/a0VHlSB.png)You can read more about why the same is disabled [here](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html).  
To enable the options again, you can either delete all stock transactions for this item, or if that is not an option, you can duplicate the same item and inward the stock with these options checked.  
**STEPS:****﻿**1. You will have to first stock out the current item using Stock Reconciliation Tool (make current stock zero). You can also stock out the item by making a stock entry of type **Material issue**.
2. Then using material receipt, inward the serialized inventory. Refer the following link for help on the same: [https://erpnext.org/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item](https://docs.erpnext.com/docs/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
3. Disable the old items so it cannot be selected in transactions again.

  
**Note:** If you want to maintain the same item code, you will need to rename the existing items, and then create the new item as per the actual item code. Otherwise, you will be maintaining the item under a new code.


