
# Payment Ledger


A Separate ledger to record transactions on receivable and payable accounts.


## Design


'Debit' and 'Credit' fields are replaced by 'Account Type' and 'Amount'(which can take both +ve and -ve values).
If Voucher,


* increases account balance - amount has +ve value
* decreases account balance - amount has -ve value


## Key Fields


* Account Type - Receivable/Payable
* Account - Account Name
* Party - Party Name
* Voucher No - Voucher affecting account balance
* Against Voucher No - Linked voucher
* Amount - Voucher amount


### Example:


A Sales Invoice of ₹1000 and a Payment Entry against that invoice will look like below.
![Screenshot 2022 05 18 at 11.13.28 AM](/files/Screenshot 2022-05-18 at 11.13.28 AM.png)


## Flowchart of Old and New Design


Old Design
![Payment Ledger.001](/files/Payment Ledger.001.jpeg)


New Design
![Payment Ledger.002](/files/Payment Ledger.002.jpeg)


## Advantage


Consider a scenario, where a payment is reconciled against a sales invoice. In the old design, this would require the Payment Entry's GL entries to be cancelled
and new GL entries with the link to sales invoice will be reposted.


With the new design, there is on need to touch GL Entry. Only Payment Ledger will be updated.


