
# Payment Order



**A Payment Order is an internal document to record bulk payments against Suppliers.**


In big corporations, the decision of making payment to Suppliers is done by someone like the Purchase Manager. The action of making the payments is done by an Accountant (Accounts User).


The Payment Order is the communication between the Purchase Manager and the Account notifying the Accountant to proceed with the Payment.


In ERPNext, using the Payment Order, you can fetch multiple Payment Requests created against a Supplier.


## 1. Prerequisites


Before creating and using the Payment Order, it is advisable to create the following first:


1. [Purchase Order](/docs/en/buying/purchase-order)


Or
2. [Purchase Invoice](/docs/en/accounts/purchase-invoice)


## 2. How to create a Payment Order


1. Go to the Payment Order list and click on New.
2. Select the Company bank account.
3. Click on the **Get from** button and select Payment Request. Apply filters if needed and select the Payment Requests.
![Payment Order Fetch](/files/payment-order-fetch.png)
4. The Payment Requests will be fetched into the Payment Order.
![Payment Order Fetch](/files/payment-order.png)
5. Save and Submit the Payment Order. Now, you'll see a button to make the Payment Entries in bulk.
![Payment Order Fetch](/files/payment-order-submit.png)




