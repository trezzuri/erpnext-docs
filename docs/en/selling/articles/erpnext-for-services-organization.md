
# ERPNext for Service Organization



**Question:** ERPNext looks primarily designed for the traders and manufacturers. Is ERPNext used by companies offering servies?


**Answer:**


About 30% of ERPNext customers are companies into services. These are companies into software development, certification services, individual consultants and many more. Being into service business ourselves, we use ERPNext to manage our sales, accounting, support and HR operations. Check following video to learn how ERPNext uses ERPNext.



### Master Setup


The setup for a Service company differs primarily for Items. They don't maintain the Stock for Items and thus, don't have Warehouses.


To create a Service (non-stock) Item, in the item master, uncheck "Maintain Stock" field.


![Service Item](/files/service-item.png)


When creating Sales Order for the services, select Order Type as **Maintenance**. Sales Order of Maintenance Type needs lesser details compared to stock item's order like Delivery Note, item warehouse etc.


Service company can still add stock items to mantain their fixed assets like computers, furniture and other office equipments.


### Hiding Non-required Features


Since many modules like Manufacturing and Stock will not be required for the services company, you can hide those modules from:


`Setup &gt; Permissions &gt; Show/Hide Modules`


Modules unchecked here will be hidden from all the User.


#### Permissions


ERPNext is the permission controlled system. Users access system based on permissions assigned to them. So, if user is not assigned Role related to Stock and Manufacturing module, it will be hidden from that User. [Click here to learn more about permission management.](/docs/en/setting-up/users-and-permissions.html).


You can also refer to help video on User and Permissions setting in ERPNext.









