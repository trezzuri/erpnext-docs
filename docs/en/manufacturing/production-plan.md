
# Production Plan



**A Production Plan helps in production and material planning for the Items planned for manufacturing. These production items can be committed via Sales Order (to Customers) or Material Requests (internally).**


Production Plan helps the user to plan production against multiple Sales Orders or the Material Requests. Also, it helps in Material Procurement planning for the raw material item, based on the quantity of finished products to be manufactured.


To access the Production Plan list, go to:


> Home > Manufacturing > Production > Production Plan


## 1. Prerequisites


Before creating and using a Production Plan, it is advised that you create the following first:


* [Item](/docs/en/stock/item)
* [Material Request](/docs/en/stock/material-request)
* [Sales Order](/docs/en/selling/sales-order)
* [Bill Of Materials](/docs/en/manufacturing/bill-of-materials)
* [Routing](/docs/en/manufacturing/routing)


## 2. How to Create a Production Plan


As mentioned earlier, a Production Plan can be used for planning the manufacture of Items against Sales Orders or Material Requests.


The common steps are:


1. Go to the Production Plan list, click on New.
2. Select whether to get items from a [Sales Order](/docs/en/selling/sales-order) or a [Material Request](/docs/en/stock/material-request).


A Production Plan can also be created manually where you can select the Items to manufacture.


### 2.1 Production Against Sales Orders


1. Select option as Sales Order from the 'Get Items From' drop-down list. The system will show the filters, using that you can pull the Sales Orders for the production. You don't need to use all these filters if you have only a few Sales Orders in a particular time frame.


![Production Plan fetch items](/files/pp_fetch_from.png)
2. Click on Get Sales Orders to fetch sales orders based on the above filters.


![Sales Order Filters](/files/sales_order_filter.png)
3. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched.
![Get items for Production Plan](/files/get_items_wo.png)
4. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process.
5. If "Consolidate Items" is ticked and saved, items with the same BOM are combined into a single item with the combined total planned quantity.
![Get items Combined for Production Plan](/files/get_items_combined_wo.png)


### 2.2 Production Against Material Requests


1. Select option as Material Request from the Get Items From drop-down list. The system will show the filters, using that we can pull the Material Requests for the production.


![Material Request Filters](/files/material_request_filter.png)
2. Click on 'Get Material Request' to fetch material requests based on the above filters.


![Material Requests](/files/material_requests.png)
3. Click on Get Items for Work Order to fetch the items from the above material requests.


![Material Request Item](/files/material_request_items.png)


### 2.3 Fetching Sub Assembly Items


Clicking on 'Get Sub Assembly Items' will fetch Sub Assembly Items from the BOM of the Finished Good Items, in the table above.
![Get Sub Assembly Items](/files/get-subassembly-items.png)


#### 2.3.1 Sub Assembly Items


User will get option to make In House (Work Order) / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type. 


![Manufacturing Type](/private/files/production_plan_sub_assembly.png)


If user wants to make Material Request for their Sub-assembly items as well their Final Raw Materials then they have to select the Manufacturing Type as "Material Request" for Sub-assembly items and then they have to click on the button "Get Raw Materials for Purchase" to fetch Sub-assembly items in the Material Request Plan Item table.


![Material Request Plan](/private/files/production_plan_material_request_items.png)


#### 2.3.2 Combining Sub Assembly Items


If there are Finished Goods that share the same Sub Assembly Item, the Sub Assembly Items can be combined. 
The criteria for combination would be to have the same Item, Warehouse, BOM and Manufacturing Type.


![Combine Sub Assemby Items](/files/consolidate-subassembly-items.png)


In this way a common Work Order can be made to bulk create Sub Assemblies for various Finished Goods.


#### 2.3.3 Skip Available Sub Assembly Items


If the Sub Assembly Items are available in the stock or will be available in the future through open Purchase Orders or open Work Orders and you don't want to manufacture them then you can enable the checkbox "Skip Available Sub Assembly Items". With this option the raw materials to manufacture sub-assembly items won't be consider while making the material requests. 


![Skip Available Sub Assembly Items](/private/files/skip_available_sub_assembly_items.png)


### 2.4 Planning for Material Requests


Clicking on the 'Get Raw Materials for Purchase' button will fetch the required raw material Items in the Material Request Plan table. For example, to manufacture 200 plastic canes, you need 100 raw plastic Nos but have only 20 in your Warehouse, then clicking this button will add a row with 80 in the Required Quantity column.


![Material Request Plan](/private/files/fetch_materials_for_material_request_purchase.png)


Use the following checkboxes to perform certain actions:


* **Include Non Stock Items**: To include non-stock items in the material request planning. i.e. Items for which 'Maintain Stock' checkbox is unticked. Refer the [Item page](/docs/en/stock/item#12-options-when-creating-an-item) for more details.
* **Include Subcontracted Items**: To add subcontracted Item's raw materials if include exploded items is disabled.
* **Ignore Existing Projected Quantity**: If enabled then the system will create the Material Request even if the user has already ordered or requested the respective items. For example if you need 100 quantity of raw material A and even if you already have 150, enabling this checkbox will add a request for 100 quantity of that raw material.
* **For Warehouse**: User can set the Warehouse for which they want to create the material request. When creating Stock Entries during the production process, the system will look for raw material stock in this Warehouse.


#### 2.4.1 Download Material Request Plan


![Download Material Request Plan](/private/files/download_material_request_plan.png)


On click of "Download Material Request Plan" button the User will get the Excel sheet with the raw materials that are needed to complete this Production Plan. User can select the Warehouse to check the available quantity in the respective Warehouse. On click of "Download Material Request Plan" a popup will open to select warehouses. If user wants to Run plan for multiple warehouses then they can select those warehouses in the Popup to download the plan in the excel sheet format. Excel sheet will look similar to:


![Material Request Plan](/files/material_request_excel.png)


### 2.5 After Submitting


Once the Production Plan is submitted, the User gets an option to make Work Orders for the production items and Material Requests for the raw materials. Users can also set the Status as **Closed** in the Production Plan.


![Menu](/private/files/menu_options_for_production_plan.png)


#### 2.5.1 Closing a Production Plan


There could be occurrences where a Production Plan is partially complete and is going to be discontinued. This could happen due to reasons such as:


* One of the items was independently produced outside the Production Plan.
* A change in plans occurred and pending items will not be produced.


In cases like these, Users can set the Production Plan status to **Closed**, so that no new Work Orders or Material Requests are created against it.


![Closing a Production Plan](/files/production_plan_status.gif)


The same can be **Re-opened**.


### 2.6 Making work order for the sub-assembly items


User will get option to make Work Order / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type. 


![Manufacturing Type](/private/files/production_plan_sub_assembly.png)


If user wants to make Work Order for sub-assembly items then select the Manufacturing Type as In House and submit it. After Submit you have to click on the button Create -> Work Order / Subcontract PO


![Sub Assembly Work Order](/private/files/make_wo_for_sub_assembly_items.png)


## 3. Related Topics


1. [Work Order](/docs/en/manufacturing/work-order)
2. [Job Card](/docs/en/manufacturing/job-card)




