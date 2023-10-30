
# Payment Entry for Capital Account



**Question:** 
  
How to create a Payment Entry where a shareholder is investing capital. The amount should get added in the company's Bank Account.
  

**Answer:** 
  
You can create a Payment Entry for a Shareholder as well. Once you have added a Shareholder in ERPNext, you can select them in the Payment Entry on these lines.  
![](/files/Etxow8j.png)  
The only thing you will have to check with your CA would be Account Paid From. If you create this Entry from Payment Entry, which is designed to receive payment based on accruals, you will have to define a Debtor or Creditor account for selection in Account Paid From field.  
### Payment Entry via Journal Entry

  
If this doesn't help, you can very much create a Journal Entry to manage this scenario. A simple Journal Entry would be:
Cr. Shareholder's account................ XXXDr. Bank account ............................. XXX  
In the Journal Entry as well, you use the fields like Reference No. and Date for tracking cheque details of the customer.


