
# Basics of Manufacturing



ERPNext comes batteries included for all requirements of a manufacturing business like maintaining Warehouses, Workstation / Machine, Operations, Finished Goods, Raw Materials, Bill of Materials tracking, Work Order planning and execution, procurement, and a lot more.


## 1. Master Data


The Manufacturing module in ERPNext helps you to maintain Warehouses(location), Workstations, Operations, Finished Goods, and Raw Materials. For manufacturing Operations and their respective Workstations are important, which can be configured based on the Finished Goods in the Bill of Materials. Warehouses are useful to store the Raw Materials and the Finished Goods. In ERPNext, users can create separate Warehouse to keep Raw Materials, and Finished Goods.


More details are as below:


1. [Warehouse](/docs/en/stock/warehouse)
2. [Workstation / Machine](/docs/en/manufacturing/workstation)
3. [Operation](/docs/en/manufacturing/operation)
4. [Raw Material / Finished Good](/docs/en/stock/item)
5. [Routing](/docs/en/manufacturing/routing)


## 2. Transaction Data


The Manufacturing module in ERPNext helps you to maintain a multilevel Bill of Materials (BOMs) for your Items. It helps in product costing, production planning, creating work orders for your manufacturing shop floors, creating job cards, and planning inventory by getting your material requirements via BOMs (also called [Material Requirements Planning or MRP](https://erpnext.com/blog/general/what-is-mrp-and-do-you-need-it)).


More details are as below:


1. [Bill Of Materials](/docs/en/manufacturing/bill-of-materials)
2. [Work Order](/docs/en/manufacturing/work-order)
3. [Job Card](/docs/en/manufacturing/job-card)
4. [Production Plan](/docs/en/manufacturing/production-plan)


## 3. Types of Production Planning


Broadly, there are three types of Production Planning Systems:


* **Make to Stock:** In these systems, production is planned based on a forecast and the Items are then sold to distributors or customers. All fast-moving consumer goods that are sold in retail shops like soaps, packaged water, etc. and electronics like phones are made to stock.
* **Make to Order:** In these systems, items are manufactured only after the customer places an order of a certain number according to the customer's requirement. For example, a wedding cake.
* **Engineer to Order:** In this case, each sale is a separate project and has to be designed and engineered to the requirements of the customer. Common examples of this are any custom business-like furniture, machine tools, specialty devices, metal fabrication, etc.


Most small and medium-sized manufacturing businesses are based on a make to order or engineer to order system and so is ERPNext.


For engineer to order systems, the Manufacturing module should be used along with the [Project module](/docs/en/projects).


## 4. Manufacturing impact on Inventory


Work order status is dependent upon the stock transactions made against it. In ERPNext, you can transfer the raw materials required to make finished goods from Store to Work In Progress Warehouse. From Work-In-Progress warehouse the raw materials can be consumed using the Stock Entry. You get the option to either bulk consume the raw materials and add the finished good or consumed the materials first and then add the finished good.


## 5. ERPNext Manufacturing Demo


Check out the following video to know about features in the manufacturing module.








