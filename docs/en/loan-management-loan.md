
# Loan



> Introduced in Version 13


**Loan record is the loan account which contains all the information regarding a loan.**


Loan record acts as a loan account which contains all the applicant details, repayment schedule, and repayment info. All the loan related documents like [Loan Disbursement](/docs/en/loan-management/loan-disbursement), [Loan Repayment](/docs/en/loan-management/loan-repayment), etc are linked to a Loan.


To access the Loan List list, go to:
> Home > Loan Management > Loan > Loan


## 1. Prerequisites


Before creating and using a Loan, it is advised that you create the following first:


* [Loan Security Type](/docs/en/loan-management/loan-security-type)
* [Loan Security](/docs/en/loan-management/loan-security)
* [Loan Type](/docs/en/loan-management/loan-type)
* [Loan Application](/docs/en/loan-management/loan-application)
* [Loan Security Pledge](/docs/en/loan-management/loan-security-pledge)


## 2. How to Create a Loan


1. Go to Loan List, click on New.
2. Select Applicant Type.
3. Select the Applicant.
4. Select Loan Application if Loan Application is created against that Applicant. All the details in loan application will be automatically fetched in the Loan record.
5. Select Company.
6. Enter posting date.
7. If applicant type is Employee then check "Repay from Salary" if loan will be repaid from salary.


![Make Loan](/files/loan-details.png)
8. Enter Loan Type. All the loan accounts, mode of payment and other loan details like whether the loan is a term loan or demand loan will be automatically fetched from the loan type master. If loan is a term loan repayment schedule will be auto generated on saving the loan document.


![Make Loan](/files/loan-accounts.png)
![Make Loan](/files/loan-repayment-schedule.png)
9. Check 'Is Secured Loan' if the loan is a secured loan. Also select 'Loan Security Pledge' if the loan is a secured loan.
10. Click "Save" to save the draft of the Loan.
11. Click "Submit" to submit the Loan Security Pledge.
12. Once the Loan is submitted the loan amount is ready to be disbursed.


### 2.1. Other ways to create a Loan


You can also create a Loan from an approved Loan Application via the **Create** button on the top right.


![Loan Application](/files/create-loan.png)


## 3. Features


### 3.1 Creation Of Disbursement Entry


After submitting the Loan document, if the status is "Sanctioned" and "Repay from Salary" is unchecked, you can create [Loan Disbursement](/docs/en/loan-management/loan-disbursement) from the loan document via **Create** button on top right.


![Create Loan Disbursement](/files/create-loan-disbursement.png)


### 3.2 Creation Of Repayment Entry


If the loan is fully or partially disbursed and "Repay from Salary" is unchecked, you can create a [Loan Repayment](/docs/en/loan-management/loan-repayment) from the loan document via **Create** button on top right.


![Create Loan Repayment](/files/create-loan-repayment.png)


### 3.3 Loan Repayment Deduction from salary


To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip and a [Loan Repayment](/docs/en/loan-management/loan-repayment) record will also be automatically created for the it.


![Salary Slip Loan](/files/salary-slip-loan.png)




