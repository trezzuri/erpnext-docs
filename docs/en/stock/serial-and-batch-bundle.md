
# Serial and Batch Bundle



> Introduced in Version 15


In version 15, we have introduced the Serial and Batch Bundle. This feature will be used to link Serial / Batch Nos in the Stock transactions.


Before version 15 the Serial No field was a Small Text field. Which meant one column was holding more than one serial number. Because of this design, there were lot of a data integrity issues. So to solve this we have changed the Serial No field from Small Text to Link field in version 15. Since we can't add a child table inside a child table we have added a new doctype "Serial and Batch Bundle" to pick/dispatch multiple Serial / Batch numbers.


![serial and batch bundle](/private/files/serial-and-batch-bundle.png)


## How does this work?


You need a Serial and Batch bundle to be created and linked to stock transactions whenever you have to deal with Serial / Batch numbers. The user needs to create a separate "Serial and Batch Bundle" for each transaction and they can't link the same "Serial and Batch Bundle" to multiple transactions. 


### Auto Creation of Serial and Batch Bundle for Inward Entry


If the user wants to create an auto "Serial and Batch Bundle" for the inward entry then they have to make sure that 'Serial Number Series' has been set for the item Serial Item and the 'Automatically Create New Batch' checkbox with 'Batch Number Series' has set for the Batch Item.


#### For Serial No


![Serial no Configure](/private/files/auto-serial-creation.png)


#### For Batch No


![Batch no Configure](/private/files/auto-batch-creation.png)


After the configuration when the user creates the Purchase Receipt or Stock Entry with the Type "Material Receipt", the system will create the "Serial and Batch Bundle" for inward automatically on submission of the record.


![Auto Serial Batch Bundle Inward](/private/files/auto-create-serial-batch-for-inward.gif)


### Auto Creation of Serial and Batch Bundle for Outward Entry


If the user wants to create an auto "Serial and Batch Bundle" for the outward entry then they have to enable the checkbox "Auto Create Serial and Batch Bundle For Outward" in the stock settings. The user can also set "Pick Serial / Batch Based On" as "FIFO / LIFO / Expiry" in the stock settings.


![Auto Serial Batch Bundle Outward Configure](/private/files/auto-outward-configuration.png)


After the configuration when the user creates the Delivery Note or Stock Entry with the Type "Material Issue", the system will create the "Serial and Batch Bundle" for outward automatically on submission of the record.


![Auto Serial Batch Bundle Outward](/private/files/auto-create-serial-batch-for-outward.gif)


### Manual Creation of Serial and Batch Bundle for Inward Entry


For the "Serial and Batch Bundle", both serial / batch no needs to be present first in the system. So with the manual option user has to first create the Serial / Batch Nos in the system. The user has to use the CSV import option to make Serial / Batch Nos. The blank CSV template can be downloaded using the Serial and Batch Selector.


![Manual Serial Batch Bundle Inward Configure](/private/files/create-using-csv.png)


Complete GIF for manual creation of Serial and Batch Bundle for inward entry is as follow


![Manual Serial Batch Bundle Inward](/private/files/manually-create-serial-no-inward.gif)


### Manual Creation of Serial and Batch Bundle for Outward Entry


Using the Serial and Batch Selector, the user can pick the Serial / Batch Nos based on the "FIFO / LIFO / Expiry" method.


![Manual Serial Batch Bundle Outward Configure](/private/files/serial-batch-selector-outward.png)


Complete GIF for manual creation of Serial and Batch Bundle for outward entry is as follow


![Manual Serial Batch Bundle Outward](/private/files/manually-create-serial-no-outtward.gif)


## History of Serial Numbers


To check the history of Serial Numbers, check the report "Serial No Ledger"


![Serial No Ledger](/private/files/serial-no-ledger-report.png)




