
# Dunning



**A document to be sent as a persistent demand for debt payment.**


Dunning is a document to store and send as a persistent demand for debt payment against an unpaid Sales Invoice.


To access the Dunning list, go to:



> 
> Home > Accounting > Dunning
> 
> 
> 


## 1. Prerequisites


* [Sales Invoice](/docs/en/accounts/sales-invoice)


A Dunning can only be created against an overdue Sales Invoice.
* Dunning Type


A **Dunning Type** is used to pre-fill interest, fees and text blocks in a new **Dunning**.


## 2. How to create a Dunning


A Dunning is created against a list of overdue scheduled payments. You can create a dunning in two different ways:


### a) Create a new Dunning


1. Go to the **Dunning** list and click on "Add Dunning".
2. Select a **Customer** and click "Fetch Overdue Payments". This will show a list of overdue Sales Invoices for this customer. Select the ones you would like to fetch into this **Dunning** and click on "Get Items".


### b) Create a Dunning from an overdue Sales Invoice


1. Go to the **Sales Invoice** list and open any overdue **Sales Invoice**.
2. Click on "Create > Dunning". This will fetch all overdue payments from the invoice's payment schedule table into a new **Dunning**.


### Fill the remaining fields


1. Select a **Dunning Type** to fill interest, dunning fees and text blocks with predetermined values. Or you can set these values manually as well.
2. You can already set an income **Account** (for example, "Other interest and similar income") and **Cost Center** for the income generated from interest and dunning fees. These will be used once a **Payment Entry** is created from this **Dunning**.
3. Save and submit the **Dunning** before sending it to the **Customer**.


![Dunning example](/files/dunning9768a2.png)


### 2.1 What is a Dunning Type


Dunning Type stores default values for dunning fee, interest rate and text blocks to be included. For example, a Dunning Type "First Notice" will not have any fees, but Dunning Type "Second Notice" will have a dunning fee and interest charged on the outstanding amount.


![Dunning Type](/files/first_dunning.png)


### 2.2 Statuses


These are the statuses that are auto-assigned to Dunning.


* **Draft**: A draft is saved but yet to be submitted.
* **Unresolved**: The Dunning is unresolved when it is submitted but no payments have been received.
* **Resolved**: The Dunning is resolved when the outstanding payment has been received.
* **Cancelled**: A cancelled status is a cancelled Dunning document.


## 3. Payment


When you receive a full payment, including interest and fees, please open the unresolved **Dunning** and click on "Create > Payment". This will create a **Payment Entry** against the outstanding scheduled payments and record the interest and fees as "Payment Deductions or Loss". The **Payment Entry** will automatically set the **Dunning**'s status to resolved.


![Dunning Payment](/files/dunning_payment_entry.png)


## 4. Related Topics


1. [Payment Entry](/docs/en/accounts/payment-entry)
2. [Sales Invoice](/docs/en/accounts/purchase-invoice)




