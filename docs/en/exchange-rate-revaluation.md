
# Exchange Rate Revaluation



In ERPNext, you can make accounting entries in multiple currencies. For example, if you have a bank account in a foreign currency, you can make transactions in that currency and the system will show bank balance in that specific currency.

The purpose of Exchange Rate Revaluation master is to adjust the balance in General Ledger accounts according to any changes in the currency exchange rates. This is useful when you are closing your accounts books and want to update your Company's GL accounts by bringing in the money from other currency accounts.

***Note: From ERPNext v14, Exchange Rate Revaluation can handle Foreign Currency Accounts that have '0' balance in either Base or Account Currency. A Separate Journal of type 'Exchange Gain/Loss' will be created in draft status for them.***

To access the Exchange Rate Revaluation list, go to:


> Home > Accounting > Multi Currency > Exchange Rate Revaluation
> 
> 

## 1. How to set up currency in an account

1. To get started with multi currency accounting, you need to assign the accounting currency in an Account record.
2. You can define Currency from the Chart of Accounts while creating an account.

![Currency in Ledger](/files/currency-in-ledger.png)![]()
3. You can also assign/modify the currency for existing accounts by opening the specific Account record.
4. Click on the Account and Click on Edit.

![Set Account Currency](/files/update-currency-in-ledger.png)![]()

## 2. How to enable Exchange Rate Revaluation

Exchange Rate Revaluation feature is for dealing with the situation when you have accounts with different currencies in one Company's Chart of Accounts.

1. Go to: **Setup > Company > *select the company***.
2. Set the 'Unrealized Exchange Gain/Loss Account' field in Company DocType. This account is to balance the difference of total credit and total debit.

![Unrealized Exchange Gain/Loss Ledger in Company](/files/unrealized-exchange-gain-loss-ledger-in-company.png)![]()
3. Go to **Accounting > Setup > Exchange Rate Revaluation > New**.
4. Select the Company.
5. Click the 'Get Entries' button. It'll fetch the accounts which have currency different from the 'Default Currency' set in the Company.
6. This will fetch the new exchange rate automatically if not set in Currency Exchange DocType for that currency else it will fetch the 'Exchange Rate' set in the [Currency Exchange](/docs/en/accounts/currency-exchange) DocType. ![Exchange Rate Revaluation](/files/exchange-rate-revaluation.png)![]()
7. On Submitting, **Create Journal Entry** button will appear. ![Journal Entry Option After Submission](/files/exchange-rate-revaluation-submit.png)![]()
8. Clicking on this button will create a Journal Entry for the Exchange Rate Revaluation. ![Exchange Rate Revaluation Journal Entry](/files/exchange-rate-revaluation-journal-entry.png)![]()
9. On submitting the Journal Entry, the general ledger is affected as follows: ![Exchange Rate Revaluation GL](/files/exchange-rate-revaluation-gl.png)![]()

### 3. Automate Exchange Rate Revaluation Creation

Provision for Auto creation of Exchange Rate Revaluation is available in Company master under `**Exchange Rate Revaluation Settings**`

![Screenshot 2023-07-10 at 11.52.17 AM](/files/Screenshot 2023-07-10 at 11.52.17 AM.png "Screenshot 2023-07-10 at 11.52.17 AM.png")![]()  


### 4. Related Topics

1. [Inter Company Journal Entry](/docs/en/accounts/inter-company-journal-entry)
2. [Inter Company Invoices](/docs/en/accounts/inter-company-invoices)



