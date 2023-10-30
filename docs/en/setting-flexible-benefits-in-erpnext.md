
# Setting Flexible Benefits against a Benefit Claim



**Flexible benefit** plans allow employees to avail the **benefits** they want or need from a package of programs offered by an employer. They may include health insurance, pension plans, telephone expenses, etc.  
To set Flexible Benefits in ERPNext, follow the following steps:  
1) Go to Salary Component for which you want to set flexible benefits for and select the **"Is Flexible Benefit"** checkbox. Enter the Yearly **Max. Benefit Amount**. Select the **"Pay Against Benefit Claim**" checkbox to avail the flexible benefits via a Benefit Claim.  
![](/files/gpYJN0U.png)  
2) Set up a Salary Structure for the Employee with this Salary Component. Set the Amount to 0. Also, enter the Max Benefits Amount for this Salary Structure.  
![](/files/CoNsmqr.png)  
3) Assign the Salary Structure to the employee via Salary Structure Assignment.  
4) Create an Employee Benefit Claim for this employee. Select the Claim Date, Component and enter the Claimed Amount.  
![](/files/Qvfr4xl.png)  
5) Run the Payroll Entry. The amount will be fetched against the component in the Salary Slip as seen below.  
![](/files/Iyh0LJa.png)  
  
  
  



