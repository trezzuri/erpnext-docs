
# Employee Referral




> 
> Introduced In Version 13
> 
> 
> 


Internal Recruitment is one of the best processes for recruitment, and it also saves effort and capital.
The Employee Referral is a process where existing employees refer a suitable candidate from their network for a vacant designation/position.


In Frappe HR, you can manage Employee Referrals.


To access Employee Referral, go to:



> 
> Human Resources > Recruitment > Employee Referral
> 
> 
> 


## 1. Prerequisites


1. [Employee](/docs/en/human-resources/employee)
2. [Additional Salary](/docs/en/human-resources/additional-salary)
3. [Job Applicant](/docs/en/human-resources/job-applicant)


## 2. How to create Employee Referral


1. Go to Employee Referral > Add Employee Referral.
2. Fill in basic details of the person you want to refer like First Name, Last Name, Email, etc.
3. Select Employee under Referrer.
4. Save and Submit.


![employee referral doc](/files/employee-referral-doc.png)


## 3. Features


### 3.1 Creating Job Applicant and auto-syncing status from Job Applicant


When you submit an employee referral document the initial status will be "Pending". After submitting the document, the "Create Job Applicant" button will appear at the top right corner.


Clicking this button will create a new **Job Applicant** with the status "Open". The status of the **Employee Referral** document will change to "In Process"


![Create Job Applicant](/files/create-job-applicant.png)


When someone changes the status of the **Job Applicant** to "Hold" or "Replied", the status of the **Employee Referral** will remain "In Process". If the status of the **Job Applicant** changes to "Accepted" or "Rejected", the status of the **Employee Referral** document will also change to "Accepted" or "Rejected" respectively.


### 3.2 Managing referral bonus


Many companies provide bonuses to their employees for such referrals. Frappe HR allows you to track the payment of the bonus to the employee for their referral.


For the Referral bonus, you need to check the "Is applicable for referral bonus" checkbox before submitting the document. After submitting the document, the "Create Additional Salary" button will appear at the top right corner, if the status is "Accepted".


![Referral Bonus](/files/referral-bonus.png)


On Click, It will redirect you to the Additional salary form where you need to select Salary component and Payroll date and after that, you need to save and submit the document.


![Create Referral Bonus](/files/create-referral-bonus.png)




