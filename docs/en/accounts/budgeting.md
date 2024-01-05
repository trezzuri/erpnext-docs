
# Budgeting



**Budgeting is a financial plan that helps controlling Company expenses.**


In ERPNext, you can set and manage budgets against a Cost Center or a Project. This is useful in controlling your expenses. With version 12, you can also create separate [Accounting Dimensions](/docs/en/accounts/accounting-dimensions) to tag transactions with different fields.


For example, if you are doing online sales, you can set a budget for search advertisements and configure ERPNext to stop or warn you from overspending beyond a set budget.


Budgets are also great for planning purposes. When you are making plans for the next Financial Year, you would typically target a revenue based on which you would set your expenses. Setting a budget will ensure that your expenses do not get out of hand at any point.


To access the Budget list, go to:
> Home > Accounting > Cost Center and Budgeting > Budget


## 1. How to Create a new Budget


1. Go to the Budget list and click on New.
2. Select what to budget against, Cost Center, Project, or an [Accounting Dimensions](/docs/en/accounts/accounting-dimensions).
3. In the accounts table, select an income/expense account for which a budget is to be set. Let's set a budget for telephone expenses for the year.
![Budget](/files/budget.png)
4. Enter the budget amount for that account.
5. Save and Submit.


## 2. Features


### 2.1 Monthly Distribution


You can also define a Monthly Distribution record to distribute the budget between months. If you don't set the monthly distribution, ERPNext will calculate the budget yearly or in equal proportion for every month.


![Monthly Distribution](/files/monthly-budget-distribution.png)


### 2.2 Control Actions (Alerts)


Control actions can be triggered when:


* A [Material Request](/docs/en/stock/material-request) is being submitted
* A [Purchase Order](/docs/en/buying/purchase-order) is being submitted
* When an actual expense is being posted (through a journal entry or a purchase invoice).


You can set a control action in the Budget based on Material Requests, Purchase Orders, or on actual expenses. Further, you can set a control action for annual or monthly budgets.


![Control Actions](/files/control-actions.png)


There are three types of control actions.


* **Stop**: This will not allow users to submit the transaction.
* **Warn**: This will show a warning message but lets the user submit the transaction.
* **Ignore**: This will neither prevent the user from submitting transactions nor show an error message.


You can set separate actions for monthly and annual budgets. If you exceed the budget, a warning will be shown:


![Budget Warning](/files/budget-warning.png)


Note that a similar warning will be triggered for any type of transactions set in the budget for the particular Account heads.


## 3. Budget Variance Report


At any point in time, you can check the Budget Variance Report to analyze the actual expense incurred vs budget allocated against a cost center or a project.


To check the Budget Variance report, go to:


> Home > Accounting > Cost Center and Budgeting > Budget Variance Report


![Budget Variance Report](/files/budget-variance-report.png)


## 4. Video


Here is a video demonstration:






## 5. Related Topics


1. [Cost Center](/docs/en/accounts/cost-center)
2. [Sales Invoice](/docs/en/accounts/sales-invoice)
3. [Purchase Invoice](/docs/en/accounts/purchase-invoice)




