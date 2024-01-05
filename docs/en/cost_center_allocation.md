
# Cost Center Allocation



## Cost Center Allocation


Cost Center Allocation is a feature using which the general ledger entry against a cost center can be split against multiple cost centers. In the Cost Center Allocation document, you can define allocation percentages of the child cost centers.


In a growing business, it becomes a necessity to analyse the income/expenses against each business unit of the organisation. And to do that, we need to treat each businees unit as a cost center and book income/expenses against the cost center. But if we need to split it every time at the transaction level manually, it becomes very difficult. That's when this Cost Center Allocation feature comes to the rescue.


In ERPNext, we just need to define the allocation between multiple cost centers (business units) against a specific master/main cost center. Then whenever we book an invoice or expense transaction against the main cost center, the system automatically split it based on allocation and posts gl entries against each child cost center.


### 1. How to create a Cost Center Allocation?


1. Go to Cost Center Allocation list view and create a new Cost Center Allocation.
2. Enter the **Main Cost Center** which will be used in the transaction.
3. Enter **Valid From** and **Valid Upto** to track the validity of the allocation.
4. In the child table, enter **child cost centers and their percentage**
5. Save and Submit the document.


![Cost Center Allocation](/files/cost-center-allocation5d3d2d.png)


### 2. GL Entries against Transaction


While booking any transaction against the main cost center, the system automatically split the GL Entry against it and posts multiple gl entries based on the applicable cost center allocation record.



![GL Entry based on Cost Center Allocation](/files/general-ledger-based-on-cost-center-allocation.png)
(GL Entries against a Sales Invoice has been splitted based on Cost Center Allocation)





