
# Auto Attendance



Auto attendance marks the attendance for employees assigned to a shift based on the records in the [Employee Checkin](/docs/en/human-resources/employee_checkin) document and the [Auto Attendance Settings](/docs/en/human-resources/shift-type#2-auto-attendance-settings) of that shift.


> Note: [Shift Type](/docs/en/shift-type) needs to be set up and assigned to employees before creating 'Employee Checkin' records. Attendance will be marked by Auto Attendance only for check-in records that are created after setting up and assigning an employee to their shift type.
> 
> 

## Steps to Set Up Auto Attendance

You can set up Auto Attendance by following the steps mentioned below:

### 1. Define Shift Type with Auto Attendance Enabled

You will have to define a Shift Type with Auto Attendance enabled. Details can be found [here](/docs/v14/en/shift-type).

### 2. Assign these shifts to employees

Once you have set up a shift, you will have to assign this shift to the employees. You can assign this to an employee using one of the two methods given below:

* **Using the Shift Assignment**: You can use the [Shift Assignment](/docs/en/human-resources/shift_assignment) document to assign shifts to employees on a date to date basis.
* **Using the Default Shift field in the employee master**: Sometimes you would want to assign a shift for an employee for all the days. You can do this by setting the following field in the Employee: `> Employee > Attendance and Leave Details > Default Shift`


> Note: Setting Shift Assignment takes precedence over the Default Shift. i.e. if you have set up a shift assignment as well as a default shift for an employee, the system will consider the assigned shift over a default shift.
> 
> 

### 3. Setup Attendance Device ID field in Employee

Biometric systems usually have their own IDs for employees. But, the Employee Checkin in Frappe HR needs to be mapped to an employee.

To map the employee to their IDs in the Biometric system you need to set the following field with the appropriate value: `Employee > Attendance and Leave Details > Attendance Device ID (Biometric/RF tag ID)`

### 4. Import or sync Employee Checkins

Once you are done with the above steps you can import/sync the [Employee Checkin](/docs/en/human-resources/employee_checkin) and start generating attendance automatically.

Please refer to this article to know more about populating Employee Checkins from an external system: [Integrating Frappe HR With Biometric Attendance Devices](/docs/v14/en/integrating-frappehr-with-biometric-attendance-devices)

## Frequently Asked Questions

### 1. How are a shift's actual start and end timings determined?

Consider a Morning Shift:

* Start Time: 08:00:00
* End Time: 11:30:00
* Begin check-in before shift start time (in minutes): 60
* Allow check-out after shift end time (in minutes): 60

So the "Actual Start Time" of the shift = *Start Time - Begin check-in before shift start time* = 07:00:00

The "Actual End Time" of the shift = *End Time + Allow check-out after shift end time* = 12:30:00.

### 2. When is the attendance marked automatically for a particular shift?

Auto Attendance for every 'Shift Type' record is attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Auto Attendance' button in the Shift Type document.

Once the "**Last Sync of Checkin**" passes the shift's actual end time, all the employee checkins for that shift are processed for marking attendance.

For eg: Consider a Morning Shift:

* Start Time: 08:00:00
* End Time: 11:30:00
* Begin check-in before shift start time (in minutes): 60
* Allow check-out after shift end time (in minutes): 60

So the "Actual Start Time" of the shift is 07:00:00 and the actual end time of the shift is 12:30:00.

Once the "Last Sync of Checkin" timestamp passes 12:30:00, it indicates that all possible checkin records for that particular shift have been synced/captured and this is when attendance marking is attempted.

### 3. How does Auto Attendance determine shift for an Employee?

The shift of an Employee on a particular date is determined by the following steps:

* Shift assigned to an Employee on the given date in the 'Shift Assignment' document.
* If the above is not found, the shift is picked up from the 'Default Shift' field of the 'Employee' document.
* Finally, if a shift is not found in 'Employee' document also, then it is assumed that the Employee does not belong to any shift on the given date and no attendance is attempted to be marked by the Auto Attendance job.

### 4. How does Auto Attendance determine Holiday List for an Employee?

Holiday List for an employee is determined as follows:

* If the employee's determined 'Shift Type' has a holiday list, then this is considered.
* Otherwise, the holiday list is fetched from either the 'Holiday List' field in the Employee document or from the 'Default Holiday List' field in the Company document, in that order.

Note: The Holiday List is important to be determined correctly by the Auto Attendance to not mark the employee as 'Absent' on holidays.

### 5. Most Biometric devices don't return the exact Log Type. In such cases how will the auto attendance determine which log is IN/OUT and how does it calculate working hours?

This is determined by 2 fields in the Shift Type set up:

* Determine Check-in and Check-out
* Working Hours Calculation Based On

It has been explained in detail over [here](/docs/v14/en/shift-type#2-auto-attendance-settings).




