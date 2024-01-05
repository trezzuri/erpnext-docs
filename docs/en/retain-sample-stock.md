
# Retaining Sample Stock



**Sample stock is a batch of any Items stored for analyzing should the need arise later.**


The Item for which sample stock is stored can be raw material, packaging material, or finished product.


## 1. Prerequisites


Before using sample retention, it is advised that you create the following first:


* [Item](/docs/en/stock/item)
* [Batch](/docs/en/stock/batch)
* [Warehouse](/docs/en/stock/warehouse)


## 1. How to Set Sample Retention Warehouse in Stock Settings


It is advised to create a new Warehouse separately for retaining samples and not use it in production.


![Sample Retention Warehouse](/files/sample-warehouse.png)


### 1.2 Enable Retain Sample in Item master


Retain Sample is based on Batch hence Has Batch No should be enabled first. Check Retain Sample and set the Maximum allowed samples for a batch.


![Retain Sample](/files/retain-sample.png)


### 1.3 Make Stock Entry


* Whenever a [Stock Entry](/docs/en/stock/stock-entry) is created with the purpose as Material Receipt, for items which have Retain Sample enabled, the Sample Quantity can be set during that Stock Entry. You need to select the Batch Number for the Item/Items. Sample quantity cannot be more than the Maximum sample quantity set in Item Master.


![Retain Sample](/files/material-receipt-sample.png)
* On submission of this Stock Entry, button 'Make Retention Stock Entry' will be available to make another Stock Entry for the transfer of sample items from the mentioned batch to the retention warehouse set in Stock Settings.


![Sample Retention Button](/files/sample-retention-button.png)
* Clicking this button will direct you to new Stock Entry of type 'Material Transfer'. This entry is transfering your sample retention from your Target Warehouse (Stores) to the Sample Retention Warehouse. It will contain all the information, verify and click Submit.


![Retain Sample](/files/material-transfer-sample.png)


### 2. Related Topics


1. [Warehouse](/docs/en/stock/warehouse)




