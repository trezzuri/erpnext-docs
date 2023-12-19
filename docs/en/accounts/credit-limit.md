
# Credit Limit



**Credit Limit is the maximum amount of credit you are willing to offer to a Customer.**


A Credit Limit is the maximum amount of credit that a financial institution or
other lender will extend to a debtor for a particular line of credit. From a
Customer's perspective, it is the maximum amount of goods or services they can get without paying money upfront.


You can set the Credit Limit in Customer, Customer Group, and in the Company.
When a Sales Order or a Sales Invoice is submitted, the Credit Limit will be checked.


The order of precedence for checking Credit Limit is as follows:


* Credit Limit set in Customer
* Credit Limit set in Customer Group
* Credit Limit set in Company


## 1. How to Set Credit Limit


1. Go to: **Selling > Sales > Customer > Customer**.
2. Under Credit Limit and Payment Terms section, set the Credit Limit.
3. If you leave the Credit Limit as the default, i.e., 0, it has no effect.
4. Save.


![Customer Credit Limit](/files/customer-credit-limit.png)


## 2. Features


### 2.1 Credit Controller


You can allow users with a specific role to override the Credit Limit validation and submit a Sales Order or Sales Invoice even when a Customer's Credit Limit is fully utilized.


To set the Credit Controller role:


1. Go to: **Accounting > Settings > Accounts Settings**
2. Set the role in Credit Controller field.


![Credit Manager](/files/credit-manager-role.png)


### 2.2 Bypass Credit Limit Check for Sales Order


For specific customers, you can set the credit limit to be checked against the cumulative amount of the outstanding sales invoices and not the sales orders. You can do so by ticking 'Bypass credit limit check at Sales Order' checkbox in 'Credit Limit and Payment Terms' section of the customer.


![Credit Limit Bypass in Sales Order](/files/customer-credit-limit-bypass.png)


### 2.3 Credit Limit for Customer Groups


To set Credit Limit at Customer Group Level:


1. Go to **Selling > Customers > Customer Group**.
2. Open the Customer Group and set the Credit Limit.


### 2.4 Credit Limit for Company


On setting Credit Limit at the Company level, all the Customers will have this Credit Limit applied globally.


To set Credit Limit at Company level:


1. Go to **Accounting > Masters and Accounts > Company**.
2. Open the Company and set the Credit Limit.


### 3. Related Topics


1. [Payment Entry](/docs/en/accounts/payment-entry)
2. [Customer](/docs/en/CRM/customer)




