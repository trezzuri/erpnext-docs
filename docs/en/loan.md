
# Loan



**Once the Loan Application is approved by the manager, a Loan record and repayment schedule can be created for the Applicant using the Loan.**

To access Loan, go to:

> Human Resources > Loans > Loan

## 1. Prerequisites

Before creating a Loan record, it is necessary that you create the following documents:

* [Loan Type](/docs/en/human-resources/loan-type)
* [Loan Application](/docs/en/human-resources/loan-application)
* [Chart of Accounts](https://docs.erpnext.com/docs/en/accounts/chart-of-accounts)

## 2. How to create a Loan record

1. Go to: Loan > New.
2. Select the Applicant name.
3. Select the Loan Application. Once selected, loan information such as Loan Type, Loan Amount, Rate of Interest, Repayment Method, Repayment Period in Months and Monthly Repayment Amount will be fetched.
4. Enter Repayment Start Date.

![Loan](/files/loan1.png)
5. Enter Account Information such as Mode of Payment, Payment Account, Loan Account and Interest Income Account.
6. Save. Once saved, a Repayment Schedule is automatically generated. The first repayment payment date would be set as per the "Repayment Start Date". The

![Repayment Schedule](/files/loan2.png)

> Note: Check "Repay from Salary" if the loan repayment will be deducted from the salary

You can alternatively create a Loan record directly from [Loan Application](/docs/en/human-resources/loan-application)

## 3. Features

### 3.1 Creation of Disbursement Entry

After submitting the Loan document, if the status is "Sanctioned", you can click on "Create Disbursement Entry" to create a Journal Entry of the Loan.

![Disbursement Entry](/files/disbursement-entry.png)

### 3.2 Loan repayment deduction from Salary

To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip.

![Salary Slip](/files/salary-slip-loan.png)

### 3.3 Extending the Loan

Loan amount is deducted from the salary. If the employee is on leave without pay for some period, the existing loan can be extended without the need for creating a new loan. This can be done be editing the Repayment Schedule table even after submitting the loan.

![Extending Loan](/files/change-loan-amount.gif)

## 4. Related Topics

1. [Journal Entry](https://docs.erpnext.com/docs/en/accounts/journal-entry)
2. [Payroll Entry](https://docs.erpnext.com/docs/en/accounts/payment-entry)



