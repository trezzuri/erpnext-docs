
# **Sales Invoice without an Item**



A Sales Invoice is a bill that you send to your Customers against which the Customer makes the payment.

There are cases where the user needs to create sales invoices without an item code (miscellaneous charges, one-time items). There is a way to handle such cases in ERPNext.

## **1. Prerequisites**

Before creating and using a Sales Invoice, it is advised to create the following first:

* [Item](https://docs.erpnext.com/docs/en/stock/item)
* [Customer](https://docs.erpnext.com/docs/en/CRM/customer)
* Optional:


	+ [Sales Order](https://docs.erpnext.com/docs/en/selling/sales-order)
	+ [Delivery Note](https://docs.erpnext.com/docs/en/stock/delivery-note)

## **2. How to create a Sales Invoice without an Item Code**

1. Go to the Sales Invoice list and click on New.
2. Select the Customer.
3. Set the Payment Due Date.
4. In the Items table, click on edit in the first row, and enter the:


	1. Item Name
	2. Description
	3. Quantity
	4. UOM
	5. Rate
	6. Income Account

![ezgif.com-crop (7)](/files/ezgif.com-crop (7).gif "ezgif.com-crop (7).gif")![]()

5. Save and Submit.

Similarly, you can create a Credit Note without an item using this method. An additional step would be to enable “Is Return” and to enter the quantity in negative.

All the other features related to Sales Invoices remain the same - <https://docs.erpnext.com/docs/user/manual/en/sales-invoice>

  





