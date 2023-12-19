
# Accounting Dimensions Filters



> Introduced in Version 13


In ERPNext, you can control the tagging of various accounting dimensions against a specific account.
You can either allow or restrict certain accounting dimensions against an account using the accounting dimension filters


To access the Accounting Dimension Filter list, go to:
> Home > Accounting > Accounting Dimension Filters


## 1. How to create an Accounting Dimension Filter in ERPNext.


1. Go to the Accounting Dimension Filter list and click on New.
2. Select the Accounting Dimension on which restriction has to be applied.
3. Select "Allow" or "Restrict" in the Allow Or Restrict field based on the type of restriction you want to apply.
4. Add accounts on which restriction will be applied in the Accounts table. Optionally you can also check the "Is Mandatory" checkbox if the accounting dimension has to be made mandatory for any specific account.
5. Add dimension values in the Dimensions table that will be allowed or restricted for the mentioned accounts.


![Create accounting dimension filter](/files/accounting-dimension-filter.png)


## 2. Features


### 2.1 Filtering accounting dimensions in transactions


Based on the restrictions applied on the account, only allowed dimensions will be filtered and shown in the transactions.


![Accounting Dimension With Filters](/files/accounting-dimension-with-filters.png)


### 2.2 Validations for Invalid and Mandatory Dimensions


In case any mandatory dimension is missing or a restricted dimension is tagged against any applicable account, the system won't allow submitting that transaction until the correct accounting dimension is selected.


![Invalid Dimension](/files/invalid-dimension.png)
![Mandatory Dimension](/files/mandatory-dimension.png)


### Related Topics


1. [Cost Center](/docs/en/accounts/cost-center)
2. [Budgeting](/docs/en/accounts/budgeting)
3. [Accounting Dimensions](/docs/en/accounts/accounting-dimensions)




