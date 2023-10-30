
# Production Scrap Management



Scrap means waste that either has no economic value or only the value of its basic material content recoverable through recycling.


Scrap is generally availed at the end of the manufacture process. Also you can find some products that are damaged or that are unusable due to expiry or for some other reason, which needs to be scraped.


In ERPNext, at the end of manufacturing process, scrap items are accounted in the scrap warehouses.


## Scrap in Bill of Materials


You can update estimated scrap quantity of an item in the BOM, Scrap table. If required, you can reselect a raw-material item as scrap.


![Scrap in BOM](/files/scrap-1.png)


## Scrap in Manufacture Entry


When production is completed, Finish / Manufacture Entry is created against a Production Order. In this entry, scrap item is fetched in the Item table, with only Target Warehouse updated for it. Ensure that Valuation Rate is updated for this item for the accounts posting purposes.


![Scrap in Manufacture Entry](/files/scrap-2.gif)


> Scrap from the BOM will only work if Manufacture Entry is created based on BOM, and not based on Material Transfer. This is configurable from Manufacturing Settings.


![Manufacturing Settings](/files/manufacturing-settings.png)




