
# Perpetual Inventory for Non-stock Item



  



**Question:**   

We have enabled Perpetual Inventory in the Company master. Still, in some Purchase Invoice, posting if done in the Expense Account.
  

**Answer:**
As per the perpetual inventory, when item is a stock item, then only it's value is booked under Stock-in-hand at the time of Purchase. In this case, the posting in the GL Entry for Purchase Invoice will be as follows.

|  |  |  |
| --- | --- | --- |
| **Account** | **Debit** | **Credit** |
| Creditors |  | 100 |
| Stock Received but not Billed | 90 |  |
| Tax | 10 |  |
|  |  |  |

Perpetual Inventory doesn't apply on the non-stock item, and expense is booked for them as soon as Purchase Invoice is submitted. The posting in General Ledger for in this scenario will look like:

|  |  |  |
| --- | --- | --- |
| **Account** | **Debit** | **Credit** |
| Creditors |  | 100 |
| COGS / Other Expense Account | 90 |  |
| Tax | 10 |  |
|  |  |  |






