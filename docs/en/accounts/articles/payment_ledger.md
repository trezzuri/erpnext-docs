
# Payment Ledger



A Separate Ledger that only records transactions on **Receivable** and **Payable** accounts. Account type should be set to `Receivable` or `Payable` for transactions to be recorded in Payment Ledger.

#### **Ex:**

A Sales Invoice of ₹1000 and a Payment Entry against that invoice will look like below. ![Screenshot 2022 05 18 at 11.13.28 AM](/files/Screenshot 2022-05-18 at 11.13.28 AM.png)![]()

### Usage

#### Reports

Accounts Receivable, Account Receivable Summary, Account Payable and Account Payable Summary uses Payment Ledger as its source.

#### Tools

[Payment Reconciliation](https://docs.erpnext.com/docs/user/manual/en/payment-reconciliation) and its extension [Semi-Auto Payment Reconciliation](https://docs.erpnext.com/docs/user/manual/en/semi-auto-payment-reconciliation) tools uses Payment Ledger to calculate outstanding Invoices. Reconciliation process only updates Payment Ledger.




