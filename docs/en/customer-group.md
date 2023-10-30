
# Customer Group



**Customer Group is an aggregation of customers that are similar in some way.**


Customer groups allow you to organize your customers. Typically Customers are grouped by market segment based on the domain in which a business operates. Customer Groups are created in hierarchical manner in ERPNext. You can create a main customer group and add sub customer groups under it.


You can define a price a list which will be automatically applied to all customers belonging to that group. You can also get trend analysis for each group. Individual, Commercial and Government customer groups are created by default. You can add your own customer groups based on your requirement like retail, wholesale etc.


### 1. How to Create a Customer Group


1. Go to **CRM > Settings > Customer Group**.
2. Click on a parent customer group like 'All Customer Groups'.
3. Click on 'Add Child'.
4. Enter 'Customer Group Name'.
5. Tick 'Group Node' if you would like to add sub customer groups under this.
6. Click on 'Create New'.


![Customer Group](/files/customer-group.png)



> 
> Tip: If you think all this is too much effort, you can leave it at “Default
>  Customer Group”. But all this effort, will pay off when you start getting
>  reports. An example of a sample report is given below:
> 
> 
> 


![Sales Analytics Customer Group](/files/sales-analytics-customer-group.gif)


### 2. Features


#### 2.1 Assign Credit Limit, Default Price List, and Default Payment Terms Template


You can assign the credit limit, [Price List](/docs/en/stock/price-lists), and [Payment Terms](/docs/en/accounts/payment-terms) and they will be automatically applied when a customer belonging to the customer group is selected in sales transactions like [Sales Order](/docs/en/selling/sales-order) and [Sales Invoice](/docs/en/accounts/sales-invoice).


#### 2.2 Default Receivable Account


You need not create a separate accounting ledger for each customer in ERPNext. Read [Common Receivable Account](/docs/en/accounts/articles/common-receivable-account) for more details.


If you need a separate receivable account for a customer, you can add the same in 'Default Receivable Account' section.


#### 3. Related Topics


1. [Customer](/docs/en/CRM/customer)
2. [Price List](/docs/en/stock/price-lists)
3. [Payment Terms](/docs/en/accounts/payment-terms)




