
# Stock Balance and Stock Account Balance Syncing



**Question:** When creating a transaction, getting validation message as follows. What is the cause of this error and how to resolve it.  
![](/files/kh7A7Gv.png)  
**Answer:** Since [Perpetual inventory](https://erpnext.com/docs/user/manual/en/stock/perpetual-inventory) is enabled in the your Company master, it requires the syncing of Stock Ledger and Stock Accounts (ledger) balance. The error message indicates that there is a mis-match in the stock and accounts balance due to previous entries  
To proceed forward, you can easily sync the stock balance and stock accounts balance by creating a Journal Entry. Click on “Create a Journal Entry Button“ in the validation message, update relevant accounts and submit Journal Entry.  
![](/files/dd0SQji.gif)


