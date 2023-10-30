
# Allocating Credit Note and Payment



**Question:** We have customers that return items after the invoice was paid. So, as usual, we create a credit note. But sometimes there are no other open invoices to which we can allocate the credit note to. So, in this case, we will need to pay customers back. How can I register this kind of transactions that we don't have negative credit on list invoices?

  


**Answer**

  


You should be able to manage this specific scenario by following the steps shared below.

  


1. First, create a Credit Note against an Invoice
2. Then create a Payment Entry for the return amount
3. Use payment reconciliation to knock-off Payment against the original Sales Invoice (and not the Credit Note itself).

  


  


**Note:** In case of a Purchase cycle, where you create a debit note in the system for a similar scenario, the steps would be as follows:

  


1. First, create a Debit Note in the system against the Purchase invoice
2. Then create a Payment entry for the return amount
3. Use payment reconciliation to knock-off Payment against the original Purchase Invoice (and not the Debit Note itself).



