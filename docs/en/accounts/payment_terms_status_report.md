
# Payment Terms Status Report



### Payment Terms Status Report


Report to calculate status of Payment Terms based on the invoices created against that Sales Order. Invoice amount is split into the respective payment terms at runtime using FIFO method.
![](/files/payment terms status.png)


##### Example:


Consider a Sales Order with total value of 7000₹ and a payment terms of 50-50.
![](/files/Screenshot 2022-01-04 at 6.33.53 PM.png)


If a Sales Invoice is made against that SO for 4900₹.
![](/files/payment terms invoice.png)


Then, the report will split the invoice amount into payment terms in FIFO method and display the statuses as 'Completed' for the first 50% and 'Partly Paid' for the second 50%.
![](/files/Screenshot 2022-01-04 at 6.27.56 PM.png)




