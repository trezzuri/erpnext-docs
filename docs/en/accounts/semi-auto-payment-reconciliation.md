
# Semi-Auto Payment Reconciliation



If there are large no of Invoices that needs be reconciled quickly without manual allocation, `Process Payment Reconciliation` doctype can be used.


## Steps:


1. First this feature must be enabled through Accounts Setting. Enable `Auto Reconcile Payments` in Accounts Settings. ![Screenshot 2023 04 21 at 7.45.58 PM](/private/files/Screenshot 2023-04-21 at 7.45.58 PM.png)
2. Navigate to `Process Payment Reconciliation` doctype
3. Select Company, Party and Receivable/Payable Account for which Reconciliation has to be done. Save and Submit
4. Document will be `Queued` status. ![Screenshot 2023 04 21 at 7.14.42 PM](/private/files/Screenshot 2023-04-21 at 7.14.42 PM.png)
5. A Background Job that runs every 15 mins will pick up `Queued` docs and will start reconciliation. If needed, the Job can triggered immediately using `Start / Resume` button.
6. This will create a `Process Payment Reconciliation Log` record with details on the Total No of Allocations that will be processed and the successfully reconciled entries. ![Screenshot 2023 04 21 at 7.54.12 PM](/private/files/Screenshot 2023-04-21 at 7.54.12 PM.png)


## Related Topics


1. [Payment Reconciliation](/docs/en/accounts/payment-reconciliation)




