
# Gratuity



> This Feature is introduced in Version 13, which will be part of a separate Payroll Module.


**Gratuity is given by the employer to his/her employee for the services rendered by him/her during the period of employment. It is usually paid at the time of retirement but can be paid earlier, provided certain conditions are met.**


In Frappe HR you can manage Gratuity Payments of employee, based on different [Gratuity Rule](/docs/en/human-resources/gratuity-rule) which vary from region to region.


To access the Gratuity go to:


> Home > Payroll > Gratuity


## 1. Prerequisites


Before creating an Gratuity, it is advised to create the following:


1. [Employee](/docs/en/human-resources/employee)
2. [Gratuity Rule](/docs/en/human-resources/gratuity-rule)
3. [Salary Component](/docs/en/human-resources/salary-component)


## 2. How to create Gratuity


1. Got to Gratuity > New
2. Select Employee and Gratuity Rule. On selecting it will calculate Current Work Experience and Total Gratuity Amount based on Gratuity rule and relieving date.
3. Check checkbox Pay via Salary Slip. if you want gratuity payment through Salary Slip.
4. Save and Submit


![Gratuity](/files/gratuity.png)


## 3. Gratuity Payments Methods


In Frappe HR, we allow you to pay the amount via Salary Slip or Payment Entry.


### 3.1 Payment via Salary Slip


To pay the Gratuity amount via Salary Slip you need to check the checkbox **Pay via Salary Slip**. Select **Payroll Date** and **Salary Component**, which will appear on Check.


![payment conf via salary slip](/files/payment-conf-via-salary-slip.png)


On Submit, it will automatically create Additional Salary with respective Payroll Date and Salary Component.


![gratuity payment via salary slip](/files/gratuity-payment-via-salary-slip.png)


### Payment via Payment Entry


To pay the Gratuity amount via Payment Entry you need to make sure that checkbox **Pay via Salary Slip** is unchecked. After that, it will allow you to select **Payable Account**, **Expense Account**, and **Mode of Payment**.


![payment conf via payment entry](/files/payment-conf-via-payment-entry.png)


After Submitting the record click on the button "Create Payment Entry" which will redirect you to the Payment Entry Form fill in the details, save, and submit.


![gratuity payment via payment entry](/files/gratuity-payment-via-payment-entry.png)




