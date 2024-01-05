
# Manufacturing Settings



Manufacturing Settings can be found at:


> Home > Manufacturing > Settings > Manufacturing Settings


![Manufacturing Settings](/files/manufacturing-settings-1.png)


### Capacity Planning


[Capacity planning](/docs/en/manufacturing/capacity-planning) is the process in which an organization decides whether or not to accept the new orders based on the resources and existing work orders.


### Disable Capacity Planning


If checked, capacity planning won't be done. Enabling it will help to decide whether or not to accept the new orders based on the resources and existing work orders.


### Allow Overtime


If enabled it'll allow creating work orders, job cards etc. outside workstation working hours.


### Allow Production on Holidays


If enabled, it'll allow production activities even on those days that are marked as holidays as per the Holiday List of the organization. 


### Capacity Planning For (Days)


The number of days specified here means the number of days in advance when the capacity planning activities will be initiated for production. 


### Time Between Operations (Mins)


This specifies the time span that should be kept between two operations in minutes. 


### Over Production Allowance Percentage


While making Work Orders against a Sales Order, the system will only allow production item quantity to be lesser than or equal to the quantity in the Sales Order. In case you wish to allow Work Orders to be raised with greater quantity, you can mention the Over Production Allowance Percentage here.


Example: In certain cases, a Workstation has to manufacture 100 units for cost effectiveness but the Work Order could be for 50 units. In this case, the Over Production Allowance Percentage would be 100.


### Default Work In Progress Warehouse


This Warehouse will be auto-updated in the 'Work In Progress' Warehouse field of Work Orders.


### Default Finished Goods Warehouse


This Warehouse will be auto-updated in the 'Target Warehouse' field of Work Order.


### Allow Continuous Material Consumption


If enabled, materials can be consumed without immediately manufacturing finished goods in a single Work Order. 


This is useful if one or more time consuming products are being manufactured. For example a single product takes a month to manufacture and the raw materials are consumed daily. In a regular scenario, this won't be feasible with stock entries. Enabling this option will allow you to create stock entries for **Material Consumption** without having to create an entry to backflush. End result is that you can see the stock being consumed in the Warehouses and can update the final manufacture entry for finished goods at a later stage.


### Backflush raw materials based on


The method selected here will be chosen for backflushing raw materials : 
1. Material Transferred for Manufacture 
2. BOM


### Add Corrective Operation Cost in Finished Good Valuation


If enabled then the cost for a corrective operation type will also be included while calculating finished goods valuation 


### Update BOM Cost Automatically


If ticked, the BOM cost will be automatically updated based on Valuation Rate / Price List Rate / last purchase rate of raw materials.


### Allow Excess Material Transfer


If enabled, the **Material Transfer** button will be visible and will allow you to transfer raw materials even if after the raw material requirement is fulfilled against a Job Card.


This is particularly useful in cases where the transferred raw materials are damaged and additional raw materials need to be transferred to produce the same amount of finished goods as intended.


### Make Serial No/Batch from Work Order


If checked, system will automatically create the serial numbers / batches for finished goods on submission of Work Order 




