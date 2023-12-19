
# Attendance



**Attendance is a record stating whether an Employee has been present on a particular day or not.**

In Frappe HR, you can mark and record attendance of an Employee on a daily basis using the Attendance doctype.

To access Attendance, go to:

> Home > Human Resources > Attendance

## 1. Prerequisites

Before creating an Attendance record, it is advised that you create the following first:

* [Employee](/docs/en/human-resources/employee)
* [Shift Type](/docs/en/human-resources/shift-management)

## 2. How to create an Attendance

1. Go to the Attendance list, click on New.
2. Select the Employee.
3. Select the Attendance Date.
4. Select the Shift (optional).
5. Select the Status (Present, Absent, On Leave, Half Day).
6. Save and Submit.

![Attendance](/files/attendance.png)

> **Note:** Attendance cannot be marked for future dates.

You can get a monthly report of your Attendance data by going to the **Monthly Attendance Details** report.

You can easily set attendance for Employees using the [Employee Attendance Tool](/docs/en/human-resources/employee-attendance-tool).

You can also bulk upload attendance using the [Upload Attendance](/docs/en/human-resources/upload-attendance).

## 3. Features

### 3.1 Marking Unmarked Attendance

In case the attendance for some employees is not marked, you can mark them as present, absent, or half-day.

#### How to Mark Attendance

1. Go to the Attendance list.
2. Click on the **Mark Attendance** button.
3. A dialog will appear.
4. Select the Employee and Month.
5. Select the Status whether Present, Absent, or Half Day.
6. If you want to exclude holidays while doing so, check *Exclude Holidays*.
7. Select the dates on which you want to mark attendance for a selected Employee.
8. Click on the **Mark Attendance** button and click on **Yes**.

![Attendance](/files/mark-attendance.gif)

## 4. Related Topics

1. [Employee Attendance Tool](/docs/en/human-resources/employee-attendance-tool)
2. [Shift Management](/docs/en/human-resources/shift-management)
3. [Auto Attendance](/docs/en/human-resources/auto-attendance)
4. [Upload Attendance](/docs/en/human-resources/upload-attendance)
5. [Attendance Request](/docs/en/human-resources/attendance-request)

It is also, possible to set up marking of attendance automatically based on check-in/check-out logs from Biometric/RFID Devices (or any other similar mechanisms that produce IN/OUT logs of the employee). Please refer to [Auto Attendance](/docs/en/human-resources/auto-attendance) feature for more information.




