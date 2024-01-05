
# Subcontracting



**In subcontracting, you employ an external party to carry out tasks for your organization, especially manufacturing.**

Subcontracting is a type of job contract that seeks to outsource certain kinds of work to other companies. It allows work on more than one phase of the project to be done at once, often leading to quicker completion.

Subcontracting is practised by various industries. For example, manufacturers who make several products from complex components subcontract certain components and package them at their facilities.

If your business involves outsourcing certain processes to a third-party Supplier where you supply the raw materials and the third party does the labour/production, you can track this by using the subcontracting feature of ERPNext.

## 1. How to Set up Subcontracting

1. Create a Service Item (Non-stock Item). It represents the service cost of the subcontracted operation.

![service itemb2929d](/files/service-itemb2929d.png)![]()
2. Create separate Items for the unprocessed and the processed product. For example, if you supply unpainted X to your Supplier and the Supplier returns you X, you can create two Items: “X-unpainted” and “X”.
3. Create a Warehouse for your Supplier so that you can keep track of Items supplied. (You may supply a month's worth of Items in one go).
4. For the processed Item, in the Item master, enable “Supply Raw Materials for Purchase”.

![fg item](/files/fg-item.png)![]()

### 1.1 Creating a BOM

Make a [Bill Of Materials](/docs/en/manufacturing/bill-of-materials) for the processed Item, with the unprocessed Items as sub-items. Let's consider a simple example, where you manufacture a pen. The processed pen will be named under the Bill of Materials(BOM), whereas, the nib, plastic, ink, etc. will be categorized as sub-items.

This BOM will be without Operations if all of the production work is done by a third party. Let's see with a simple example of a CPU Assembly:

![bom items](/files/bom-items.png)![]()  


### 1.2 Creating a Purchase Order

Make a Subcontract Purchase Order for the Service Item and select the Finished Good Item, the one for which you've created a BOM.

1. Enable the "Is Subcontracted" since this Purchase Order is for Subcontracting.

![po is subcontracted](/files/po-is-subcontracted.png)![]()
2. Here the Rate field value of the Items table in the Purchase Order will be the service cost you have agreed with the third party or the Supplier.

![po items](/files/po-items.png)![]()
3. After filling in the details, Save and Submit the [Purchase Order](/docs/en/buying/purchase-order#35-raw-materials-supplied).

### 1.3 Creating a Subcontracting Order

Make a Subcontracting Order for the Purchase Order by clicking on Create > Subcontracting Order. When you “Save”, in the “Raw Materials Supplied”, all your un-processed Items will be updated based on your Bill of Materials. You can also select the Warehouse in which the raw materials would be reserved for subcontracting under Reserve Warehouse.

![create sco from po](/files/create-sco-from-po.gif)![]()  


1. The costs involved with the subcontracting process should be recorded in the Rate field of the Items table in the Subcontracting Order shown as follows:

![sco all item tables](/files/sco-all-item-tables.png)![]()
2. In the previous image, we are providing the subcontractor with the following items:


	* 8 Motherboards
	* 8 Processors
	* 16 RAMs
	* 8 Hard Disks
	* 8 Cabinets
	
	The cost for one CPU including Raw Materials and Service Costs is 1,02,994 and the total cost for all CPUs is 8,23,952![sco items row qty rate](/files/sco-items-row-qty-rate.png)![]()
3. From a Subcontracting Order, select the raw materials to transfer to the subcontractor:

![se send to subcontractor](/files/se-send-to-subcontractor.gif)![]()
4. Once the Subcontracting Order is submitted, you can view the reserved quantity of the item from the item dashboard as well.

![item dashboard](/files/item-dashboard.png)![]()

### 1.4 Creating Stock Entry to Transfer Raw Materials

Now that the raw materials are reserved, make a Stock Entry and deliver the raw material Items to your Supplier.

In the Subcontracting Order, click on Transfer > Material to Supplier. Set the Source and Target Warehouses. The Stock Entry will be of type 'Send to Subcontractor' where you transfer from one Warehouse to another. Tick 'From BOM', select the BOM, enter the quantity, and click the Get Items button.

![se submitted](/files/se-submitted.png)![]()  


### 1.5 Creating a Subcontracting Receipt to receive the Finished and Scrap items

Receive the Items from your Supplier using a Subcontracting Receipt. You need to enter the Supplier Warehouse from where the raw materials will be taken and finished goods will be received in the Accepted Warehouse. Consider this like a backflush for subcontracting.

Click on Create > Subcontracting Receipt from the Subcontracting Order. Set the Accepted and Supplier Warehouses. Make sure to check the “Consumed Quantity” in the “Raw Materials” table so that the correct stock is maintained at the Supplier’s end. You need to select the Supplier's Warehouse where you'll receive the finished goods.

Scrap items are fetched from the chosen Bill of Materials (BOM) for Finished Goods within the Items table. The Qty is computed using the Qty of the Finished Good Item, while the Rate is determined by either the Valuation Rate or the Scrap Rate specified in the BOM.

![scr consumed items](/files/scr-consumed-items.png)![]()  


### 1.6 Creating a Purchase Receipt

Back to Purchase Order, click on Create > Purchase Receipt. There will be no effect on the Stock Ledger and Accounting Ledger since both the Stock and Accounting Ledger are updated when you Submit the Subcontracting Receipt. In case you have "Purchase Taxes and Charges" the Accounting Ledger will update accordingly.

### 1.7 Supplier Sourced Raw Material

While creating a BOM for subcontracting, there might be a few raw materials like nuts and bolts that the Suppliers will have to procure themselves.

While creating a Stock Entry for "Transfer" from a Subcontracting Order, these items can be excluded one by one, but it is impossible to do so if you have more than 100 items.

If some raw material is sourced by the Supplier directly, then such raw materials have to be included in the BOM.

* It will have zero value in BOM
* In the Subcontracting Order, this raw material will not appear in Supplied Items since it is not supplied
* Also, while creating a "Transfer", such items will be excluded from the Stock Entry

![bom items row sourced by supplier](/files/bom-items-row-sourced-by-supplier.png)![]()

However, the Supplier may choose to include the supplier-provided items in their Sales Order sent to you.

## 2. Notes

* Make sure that the “Rate” of the processed Item is the processing/service cost (excluding the raw material cost).
* ERPNext will automatically add the raw material rate for your valuation purpose when you receive the finished item in your stock.
* ERPNext will automatically default the 'Reserve Warehouse' in the Subcontracting Order from the BOM. If not found in the BOM, it would default it from the default Warehouse set in the Item. You can set the default Reserve Warehouse for all the Items in the Subcontracting Order from the 'Reserve Warehouse' field in the Raw Materials Supplied section.

## 3. Related Topics

1. [Purchase Order](/docs/en/buying/purchase-order)
2. [Purchase Receipt](/docs/en/stock/purchase-receipt)
3. [Quality Inspection](https://docs.erpnext.com/docs/user/manual/en/quality-inspection)



