
# Employee Checkin



Employee Checkin is used to keep a log of all the check-ins and check-outs of an employee in the organization. Most organizations use this for attendance, shift management, and working hours calculations.

### 1. Prerequisites

To create an Employee Checkin, you need to first create:

* [Employee](/docs/en/human-resources/employee)

If you want shifts to be determined in employee checkins and want to process auto-attendance, then you need to create the following documents too:

* [Shift Type](/docs/en/human-resources/shift_type)
* [Shift Assignment](/docs/en/human-resources/shift_assignment) or set a default shift in Employee master.

### 2. How to create an Employee Checkin

#### 2.1 Creating logs manually

To create a new Employee Checkin go to:


> Human Resources > Attendance > Employee Checkin
> 
> 

1. Click on New.
2. Select the Employee.
3. Set the date and time for the log.
4. Set Log Type as IN/OUT.
5. Save.
6. If you have set up shifts and shift assignments, the Employee Checkin will set the appropriate shift in which the timestamp falls after saving.
7. You can enable *Skip Auto Attendance* to skip that record while marking attendance.
8. You can also capture the location from where the employee has checked in or the Biometric Device ID.

![Employee Checkin](/files/employee-checkin.png)

If auto attendance is enabled, the attendance record marked for a set of check-ins will be linked to the document later.

#### 2.2 Integrating Frappe HR with Biometric Devices

If you are using a Biometric Device to log employee check-ins and check-outs you can use it to create records in Frappe HR. You can read more about this [here](/docs/en/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices).




