
# Assets



**An Asset is any valuable Item owned by a Company.**

Furniture, computers, mobile phones, printers, cars, manufacturing equipment are examples of assets. Generally, an asset is a tangible item that is located on the company premises or is carried by an employee. In some cases, an asset could be an intangible item.

An asset's useful life spans across multiple years and hence its economic value is spread over corresponding years from the accounting perspective. If you buy a printer for $300 and it is expected to be useful for three years, from the accounting perspective $100 is recorded as the expense for three years each instead of all the $300 in the first year. Most countries have rules for such calculations.

In ERPNext, the Asset record is the heart of asset management module. All the transactions related to an Asset like purchasing, depreciation, maintenance, movement, scrapping, sales will be recorded against the Asset record.

To access the Asset list, go to: > Home > Assets > Assets > Asset

## 1. Prerequisites

Before creating and using Asset, it is advised to create the following first:

* [Item](/docs/en/stock/item) with 'Is Fixed Asset' enabled.
* [Asset Category](/docs/en/asset/asset-category)

## 2. How to create an Asset

An Item representing the asset should be created. The **'Maintain Stock'** should be **unchecked** and **'Is Fixed Asset'** must be **checked**.

![Asset Item](/files/asset-item.png)![]()

### 2.1 Auto creation of assets

You can configure ERPNext to automatically create assets on submission of Purchase Receipt by enabling **'Auto Create Assets on Purchase'** in Item.

![Asset](/files/asset-auto-create.png)![]()  


If you have enabled auto asset creation for the item representing an asset, you will have to provide the asset location while submitting the Purchase Receipt.

![Asset Location in Purchase Receipt](/files/asset-location-in-purchase-receipt.png)![]()  


A message confirming the creation of assets is displayed on submission of Purchase Receipt.

![Asset Creation Confirmation Message](/files/asset-auto-create-on-purchase.png)![]()  


### 2.2 Manual creation of assets

If you would like to create assets manually, create an Item with 'Is Fixed Asset' enabled and leave 'Auto Create Assets on Purchase' unchecked . On submission of a Purchase Receipt/Purchase Invoice with that Item a message is shown indicating that you need to create assets manually.

![Manual Creation of Assets](/files/asset-manual-creation-message.png)![]()  


Follow below steps to create assets manually.

1. Go to the Assets list, click on New.
2. Enter a name for the asset.
3. Select the Item Code. Item Name and Asset Category will be fetched automatically.
4. Select the Asset Owner, i.e. Company, Supplier, or Customer.
5. Select the Company/Supplier/Customer.
6. Select the Purchase Receipt/Purchase Invoice. Purchase Date and Gross Purchase Amount will be fetched automatically.
7. Select a Location. Eg: Mumbai Office. This will be fetched automatically if specified in Purchase Receipt items table
8. Set Available-for-use Date. The depreciation will be calculated starting from this date.
9. Save and Submit.

Please note you need create **one asset record for each asset you have bought**. If you have bought five computers and have created just one Purchase Receipt with quantity set to five then you will have to create five asset records manually.

### 2.3 Creating composite assets

If, for example, you want to create a "Computer" asset made from multiple different items like "Monitor", "Keyboard", etc., you can create a composite WIP asset by checking the `is_composite_asset` checkbox. Afterwards, you can tag that asset in the `WIP Composite Asset` field of the Item in Purchase Receipts/Invoices, and once all the items are available, you can use the [Asset Capitalization](https://docs.erpnext.com/docs/user/manual/en/asset-capitalization) feature to capitalize the asset.

![](/files/t6xnhCo.png)![](/files/jdmoSl4.png)![]()  


### 2.4 Importing existing assets

When you move from a legacy system to ERPNext, you will have to add details of all the assets your company has purchased previously along with depreciation details of each asset.

For an existing asset, you can create the asset record directly by checking **"Is Existing Asset"** checkbox and provide below details.

* Gross Purchase Amount
* Purchase Date
* Available-for-use Date
* Opening Accumulated Depreciation: The accumulated depreciation amount which has already been booked for an existing asset.
* Number of Depreciations Booked: Number of depreciation entries already booked.
* Is Fully Depreciated: Mark this checkbox if the existing asset is fully depreciated

Based on these details the schedule for depreciation of remaining amount will be created automatically.

### 2.5 Additional options when creating an Asset

1. **Custodian**: The employee who will carry the asset.
2. **Department**: The department of the Custodian.
3. **Calculate Depreciation**: Enable this checkbox to calculate depreciation of Assets.

## 3. Features

### 3.1 Depreciation

* **Frequency of Depreciation (Months)**: The number of months between depreciations.
* **Total Number of Depreciations**: The total number of depreciations during the useful life of the Asset. In case of existing assets which are partially depreciated, mention the number of pending depreciations. For example, if you set frequency as 12 months and no. of depreciations as 3, 1 depreciation will be booked every 12 months for 3 years.
* **Depreciation Method**: There are four available methods for depreciation: Straight Line, Written Down Value, Double Declining Balance and Manual. You can find more details [here](https://docs.erpnext.com/docs/user/manual/en/asset-depreciation).
* **Depreciation Posting Date**: The date from which booking of depreciation will be started.
* **Expected Value After Useful Life**: Useful Life is the time period over in which the company expects that the asset will be productive. After that period, either the asset is scrapped or sold. In case it is sold, mention the estimated value here. This value is also known as Salvage Value, Scrap Value, or Residual Value.
* **Salvage Value Percentage**: If you want the `Expected Value After Useful Life` to be calculated automatically based on a percent of the `Gross Purchase Amount`, mention the percent here.
* **Rate of Depreciation**: This will be calculated based on the amount entered in expected value after useful life.
* **Finance Book**: The book against which the depreciation entries should be booked. For more details, click [here](/docs/en/accounts/finance-book).
* **Depreciate based on daily pro-rata**: This divides the depreciation amount by the number of days in a calendar period. For example, the depreciation amount in February is less than the depreciation amount for the months that have 31 days.
* **Depreciate based on shifts:** This lets you define the number of shifts the asset would run in a period in order to depreciate it accordingly. You need to first define the shift names with their shift factors in the `Asset Shift Factor` doctype (for example: "half": 0.5, "single": 1, "double": 1.5 and "triple": 2) and set a default. Later if you want to change the shifts of an asset for a particular period, you can do so using the [Asset Shift Allocation](https://docs.erpnext.com/docs/user/manual/en/asset-shift-allocation) doctype, and the remaining shifts are automatically adjusted.

### 3.2 Depreciation Schedule

On booking depreciations against this Asset, the Depreciation Schedule section will be visible. This table has columns for Finance Book, Schedule Date, Depreciation Amount, Amount Depreciated, and Journal Entry.

![Depreciation Schedule](/files/asset-depreciation-schedule.png)![]()  


### 3.3 Insurance Details

If Insurance has been taken for the Asset you're recording, you can store the following Insurance details:

* Policy number
* Insurer
* Insured value
* Insurance Start Date
* Insurance End Date
* Comprehensive Insurance

### 3.4 Accounting Entries

On submission of an asset, "Capital Work in Progress" account will be credited and the asset account related to the asset will be debited. Submission is only possible after entering "Available-to-use Date". If "Available-to-use Date" is a future date, then accounting entry will be booked automatically on that date via the scheduler.

### 3.5 Maintenance

Ticking on Maintenance Required allows recording Asset Maintenance entries for this Asset. To know more, visit the [Asset Maintenance](/docs/en/asset/asset-maintenance) page.

### 3.6 After Submitting

Once you create an Asset, you'll see options to transfer, scrap, or sell the asset. From the Make button, you can adjust its value and make a depreciation entry.

![Asset Submit](/files/asset-submit.png)![]()  


### 4. Related Topics

1. [Asset Maintenance](/docs/en/asset/asset-maintenance)
2. [Asset Movement](/docs/en/asset/asset-movement)
3. [Purchase Receipt](/docs/en/stock/purchase-receipt)
4. [Purchase Invoice](/docs/en/accounts/purchase-invoice)



