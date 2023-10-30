
# Payment Reconciliation



**Payment Reconciliation is used to link payments with invoices.**

In complex scenarios, especially in the capital goods industry, sometimes there is no direct link between payments and invoices. For example, suppose a party is a customer, you send invoices to a customer and the customer sends you block payments or payments based on some schedule that is not linked to your invoices.

In such cases, you can match Payments with Invoices using Payment Reconciliation.

To access Payment Reconciliation, go to:


> Home > Accounting > Accounts Receivable > Payment Reconciliation
> 
> 

## 1. How to Match Payments with Invoices

1. Go to Payment Reconciliation.
2. Select a Company.
3. Select a Party Type and select the Party. The Receivable/Payable account will be selected automatically.
4. Select the Bank/Cash account against which the payments need to be reconciled.
5. If you want to filter the records, select a date range for the invoices or set minimum or maximum amount for invoices as well as payment transactions
6. Click on the **Get Unreconciled Entries** button.
7. This will fetch all un-linked invoices and payment transactions from that party in Invoices and Payments table resp.
8. You can either select any particular entries to be allocated or can click on **Allocate** button without selecting anything to allocate all the entries.
9. Allocation table will be populated based on FIFO or/and selection.
10. Allocated Amount is the amount you want to allocate for the reconciliation.
11. Click on **Reconcile** to reconcile allocated entries. You will get a message that says 'Successfully Reconciled'.

![Payment Reconciliation Tool](/files/payment_recon.gif)![]()

## 2. What happens on Payment Reconciliation

If the invoices are reconciled against: 

1. **Payment Entry** - A journal entry is not auto-created when reconciliation happens against a payment entry. This is because payment entries are associated with linked transactions.
2. **Credit/Debit Note** - A journal entry is auto-created to allocate a credit/debit note to an invoice that is being reconciled. This automatic creation of a journal entry is necessary since credit/debit notes do not have linked transactions. The journal entry resulting from the reconciliation indicates the adjustment of a particular credit/debit note with a specific invoice.

### 2. Related Topics

1. [Payment Request](/docs/en/accounts/payment-request)
2. [Sales Invoice](/docs/en/accounts/sales-invoice)
3. [Purchase Invoice](/docs/en/accounts/purchase-invoice)
4. [Semi-Auto Payment Reconciliation](/docs/en/accounts/semi-auto-payment-reconciliation)



