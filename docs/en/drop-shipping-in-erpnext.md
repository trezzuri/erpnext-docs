
# Drop Ship



**Drop shipping** is a supply chain management method in which the retailer does not keep goods in stock but instead transfers the customer orders and shipment details to either the manufacturer, another retailer, or a wholesaler, who then ships the goods directly to the customer.  
Drop shipping may also occur when a small retailer (that typically sells in small quantities to the general public) receives a single large order for a product. The retailer may arrange for the goods to be shipped directly to the customer from the manufacturer or distributor. Drop shipping is common with expensive products. No inventory is maintained by the retailer in any case, simply acting as a *middleman*. In this article, we will see how ERPNext provides a seamless drop-shipping experience.  
Consider a business dealing with Computer Monitors. Now, the retailer has received an order from a customer, ABC Inc. for 1000 DELL 24Inch Monitors.  
**Drop Shipping In Action:**  
**1. Item Configuration*** Setup Item with mandatory information keeping Maintain Stock disabled since there will be no stocking of this Item.
* Next, **enable** "Delivered By Supplier (Drop Ship)
* Set the Supplier with whom the Purchase Order will be raised for this orders fulfillment.

  
![](/files/RD6ip0k.png)  
**2. Sales Cycle:*** Create Sales Order with Customer, Item, Qty, Rate, Taxes and so on.

  
![](/files/oN2oubM.png)  
  
**3. Order Fulfillment:*** From the Sales Order Document itself, you can create the Purchase Order for this shipment, track delivery, and bill the customer accordingly.

  
![](/files/mSsoueP.gif)


