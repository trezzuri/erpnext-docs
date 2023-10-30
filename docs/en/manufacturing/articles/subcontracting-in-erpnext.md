
# Subcontracting in ERPNext



Subcontracting is a type of job contract that seeks to **outsource** certain types of work to other companies. It allows work on more than one phase of the project to be done at once, often leading to quicker completion. It is practiced by various industries.

  


For example, manufacturers who make a number of products from complex components subcontract certain components and package them at their facilities.

  


![](/files/Uqloysk.png)

  


If your business involves outsourcing certain processes to a third party Supplier where you supply the raw materials and the third party does the labor/production, you can track this by using the subcontracting feature of ERPNext.

  


**How to manage subcontracting in ERPNext?**

  


For demonstrating the outsourcing, we are considering below scenario:

A manufacturer of flowers produces raw, uncolored flowers. These flowers are packed in cartons (1 Carton = 1000 flowers) and sent for coloring to external vendor.

  


1. In Item Master of subcontracted item, ensure that you have enabled the option, "Supply Raw Materials for Purchase". In our example, the Item is "RM-111-Colored Flower"

  


![](/files/Dizzv7h.png)

  


2. Create a BOM (Bill of Material) for the subcontracted Item and include the raw materials that you send to the subcontractor so as to get the finished/semi-finished product. There will be no operations in this BOM since the activities are not done at manufacturer's end. In our example, the BOM of RM-111-Colored-Flower is as below:

  


![](/files/0r4KFFG.png)

  


3. Now, you need to create the Purchase Order for procuring this Item from the external party/vendor. Ensure that you select "Yes" for the field, "Supply Raw Materials" and then select the warehouse from which the raw materials will be transferred to the vendor. Note that this can also be a virtual warehouse just to stand as a placeholder for making the Stock Entry when transferring materials to the vendor. Below is the Purchase Order as per our example:

  


![](/files/NoFO0T4.png)

  


Note: The rate of the Item entered here will be your Service Cost rate.

  


4. There is also another child table that shows the status of the raw materials to be transferred against this Purchase Order. In that table, you need to select the "Reserve Warehouse" from which the raw materials will be transferred to the virtual vendor warehouse that we selected in previous step. This table also tells you how many items have been supplied already, in our case, it is zero since we are yet to submit the order and supply the raw materials.

  


![](/files/5gxQbu3.png)

  


5. After submission of the Purchase Order, there will be a button, "Transfer" for creating the Stock Entry to transfer raw materials to the external vendor:

  


![](/files/SYPIUEq.png)

  


![](/files/aJ3pBPd.png)

  


![](/files/rQcvSYZ.png)

Once the Stock Entry is submitted, the child table in the Purchase Order is also updated to reflect the transferred quantity under "Supplied Qty"

  


![](/files/srrSyG5.png)

  


6. As in when you receive the semi-finished/finished goods from the vendor, you can create Purchase Receipt against this Purchase Order:

  


![](/files/xbWLQp2.png)

  


  


The next steps for invoicing follow as per regular Buying Cycle.

Purchase Order -> Purchase Receipt -> Purchase Invoice.

  


7. Purchase Invoice created for this transaction: (Print Format Preview)

  


![](/files/2b1Rvbr.png)

  


  


To learn more about Buying module, please check out our documentation [here](https://erpnext.com/docs/user/manual/en/buying).




