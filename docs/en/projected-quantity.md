
# Projected Quantity



**Projected Quantity is the level of stock that is predicted for a particular Item based on the current stock levels and other requirements.**


It is the quantity of gross inventory that includes supply and demand in the past which
is done as part of the planning process.


The projected inventory is used by the planning system to monitor the reorder
point and to determine the reorder quantity. The projected Quantity is used by
the planning engine to monitor the safety stock levels. These levels are
maintained to serve unexpected demands.


Having tight control of the projected inventory is crucial to determine
shortages and to calculate the right order quantity.


![Projected Quantity](/files/projected_quantity.png)


The formula to calculate projected quantity is as follows:


*Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty - Reserved Qty for Production - Reserved Qty for Subcontracting - Reserved Qty for Production Plan*


* **Actual Qty**: Quantity available in the Warehouse. This is the actual physical stock you have.
* **Planned Qty**: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
* **Requested Qty**: Quantity requested via a [Material Request](/docs/en/stock/material-request). It is added on submission of Material Request and subtracted when Purchase Order/Work Order/Stock Entry is created against it based on the Material Request type.
* **Ordered Qty**: Quantity ordered for purchase ([Purchase Order](/docs/en/buying/purchase-order)), but not received (via a [Purchase Receipt](/docs/en/stock/purchase-receipt) or a [Purchase Invoice](/docs/en/accounts/purchase-invoice).
* **Reserved Qty**: Quantity ordered for sale by your Customer ([Sales Order](/docs/en/selling/sales-order)), but not delivered (via a [Delivery Note](/docs/en/stock/delivery-note)). This quantity increases when a Sales Order is submitted and decreases when a Delivery Note or Sales Invoice is created against that Sales Order is submitted.
* **Reserved Qty for Production**: Raw materials are reserved on submission of [Work Order](/docs/en/manufacturing/work-order) and is reduced when raw materials are transfered to Work in Progress warehouse via a Stock Entry.
* **Reserved Qty for Subcontracting**: Raw materials reserved when a subcontracting Purchase Order is submitted. When raw materials are transfered to Supplier Warehouse via a Stock Entry, this quantity reduces. To know more about subcontracting [click here](/docs/en/manufacturing/subcontracting).
* **Reserved Qty for Production Plan**: Raw materials are reserved when a Production Plan is submitted. When materials are reserved for the production against the work order then the system will reduce the "Reserved Qty for Production Plan" in the respective BIN. The system reduces the quantity if the work order was made against the production plan.


#### Related Topics


1. [Warehouse](/docs/en/stock/warehouse)
2. [Material Request](/docs/en/stock/material-request)




