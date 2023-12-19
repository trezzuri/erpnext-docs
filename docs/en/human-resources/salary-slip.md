
# Salary Slip



**A salary slip is a document issued to an employee. It contains a detailed description of the employee’s salary components and amounts.**

To access Salary Slip, go to: > Home > Human Resources > Payroll > Salary Slip

## 1. Prerequisites

Before creating Salary Slip, it is advised that you create the following first:

* [Employee](/docs/en/human-resources/employee)
* [Salary Structure](/docs/en/human-resources/salary-structure)
* [Salary Structure Assignment](/docs/en/human-resources/salary-structure-assignment)

## 2. How to create a Salary Slip

1. Go to Salary Slip, Click on New.
2. Select Employee. On selecting Employee all details of the Employee will be fetched from Salary Structure which is assigned to that Employee. This includes details such as Payroll Frequency, Earnings, Deductions, etc.
3. Select Start Date and End Date.
4. Save.

## 3. Feature

### 3.1. Salary Slip based on Attendance/Leave

HR users can create Salary Slip based on Attendance or leave. The Working days will calculated on basis of leave/Attendance, depending on the field **Calculate Payroll Working Days Based On** in [HR Settings](/docs/en/human-resources/hr-settings). If Payroll is based on Attendance then, the **Leave without pay** will be considered as absent and **half-day** will be considered as half-day absent.

### 3.2. Salary Slip based on Timesheet

For creating Salary Slip based on timesheet you need to create Salary Structure for Timesheets.

Frappe HR also provides an option to create Salary slip based on working hours based on [Timesheet](/docs/en/projects/timesheets). You can create Salary Slip after submitting the Timesheet by clicking directly on **Create Salary Slip** button on the top right.

![Create Salary Slip based on Timesheets](/files/create-salary-slip-based-on-timesheets.png)![]()

The Payment Amount is calculated based on Hour Rate defined in Salary Structure and is reflected in the Earnings table.

### 3.3 Year to Date and Month to Date

For every salary slip, 'Year to Date' and 'Month to Date' are computed.

![Year to Date and Month to Date](/files/ytd-and-mtd.png)![]()  


* **Year to Date**: Total salary booked for that particular employee from the beginning of the year (payroll period or fiscal year) up to the current salary slip's end date.
* **Month to Date**: Total salary booked for a particular employee from the beginning of the month (for which the payroll entry is created) up to the current salary slip's end date.

Year to Date is also computed for every component in the earnings and deduction tables. The "Salary Slip with Year to Date" print format is available with Year to Date and Month to Date computations.

![Year to Date for Salary Slip Components](/files/ytd-component.png)![]()  


### 3.4 Bulk Email Salary Slips

By default, the Payroll Entry sends salary slip emails to all the employees on salary slip submission if **Email Salary Slip to Employee** is enabled in Payroll Settings.

![](/files/2FG61KM.png)![]()  


But if there are a few employees who don't have an email ID set or the setup is incorrect during this action, you can use the bulk action in the Salary Slip list view to trigger sending emails to selected employees later.

![bulk](/files/bulk.png "bulk.png")![]()  


  





