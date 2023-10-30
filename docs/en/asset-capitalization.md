
# Asset Capitalization



The Asset Capitalization feature lets you do the following:

* Convert one or more stock items into a new composite asset
* Convert one or more stock items into a new composite asset and capitalize the service expenses’ cost
* Convert one or more assets into a new composite asset
* Convert one or more assets into a new stock item

To access the Asset Capitalization feature, go to:


> Home > Assets > Maintenance > Asset Capitalization
> 
> 

![](/files/jdmoSl4.png)  
  
Let’s go through the aforementioned use cases one by one.

## 1. Convert one or more stock items into a new composite asset

**Steps**:

* Create a new Asset Capitalization
* If you want a new composite Asset to be created, choose the Capitalization Method as "Create a new composite asset" and set the Target Item Code to the fixed asset Item to be linked with the new asset and the Target Asset Location to the Location of the new asset. If you want a WIP composite asset to be used, choose the Capitalization Method as "Choose a WIP composite asset" and set the Target Asset to the composite asset.
* Change the Naming Series, Company, Finance Book and Posting Date if needed
* Enter the stock items to be converted in Consumed Stock Items. If you chose the Capitalization Method as "Choose a WIP composite asset", all the items tagged to the asset through Purchase Receipts/Invoices will be fetched automatically.
* Save and Submit
* Set the depreciation details (if any) of the newly created asset and submit it.

**Accounting effect**:

The Consumed Stock Items will be reduced by the selected qty from the selected warehouses and the Warehouse Stock Accounts will be credited with the issued stock value amount. The Fixed Asset account of the created Asset will be debited by the Total Value.

## 2. Convert one or more stock items into a new composite asset and capitalize the service expenses’ cost

The prerequisites, steps and accounting effect for this is almost the same as the previous one, the only addition being that you can add the Service Expenses, and the Expense Accounts of the services would be credited with the service’s amount.

## 3. Convert one or more assets into a new composite asset

**Prerequisites**:

A new fixed asset Item (with `Is Fixed Asset` checkbox ticked) since it would be the item linked with the new asset.

**Steps**:

* Create a new Asset Capitalization
* Set the Target Item Code to the Item to be linked with the new asset
* Set the Target Asset Location to the Location of the new asset
* Change the Naming Series, Company, Finance Book and Posting Date if needed
* Enter the assets to be converted in Consumed Assets
* Save and Submit
* Set the depreciation details (if any) of the newly created asset and submit it.

**Accounting effect**:

The Consumed Assets will be depreciated (if configured for depreciation) till the posting date and Depreciation Journal Entries will be created in the background. Then they would be disposed of and their status would be set to "Capitalized". The Fixed Asset accounts of the Consumed Assets will be credited by their gross purchase amount and the Accumulated Depreciation accounts will be debited by their total accumulated depreciation. The Fixed Asset account of the created Asset will be debited by the Total Value.

## 4. Convert one or more assets into a new stock item

**Prerequisites**:

A new stock Item (with `Maintain Stock` checkbox ticked) to which the

**Steps**:

* Create a new Asset Capitalization
* Set Entry Type to Decapitalization
* Set the Target Item Code to the new Item
* Set the Target Warehouse and Target Qty
* Change the Naming Series, Company, Finance Book and Posting Date if needed
* Enter the assets to be converted in Consumed Assets
* Save and Submit
* Set the depreciation details (if any) of the newly created asset and submit it.

**Accounting effect**:

The Consumed Assets will be depreciated (if configured for depreciation) till the posting date and Depreciation Journal Entries will be created in the background. Then they would be disposed of and their status would be set to "Decapitalized". The Fixed Asset accounts of the Consumed Assets will be credited by their gross purchase amount and the Accumulated Depreciation accounts will be debited by their total accumulated depreciation. The new stock Item will be added by the Target Qty in the Target Warehouse and Target Warehouse Account will be debited by the Total Value.




