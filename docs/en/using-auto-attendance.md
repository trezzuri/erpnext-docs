
# Using Auto Attendance



Our system allows to Mark Attendance Automatically depending upon Employee Checkin records. There are some things you need to know:


A. Create or import Employee Checkin:


![](/files/zTTsnRA.png)


1. Set the time carefully for log type **IN** and **OUT.**
2. For Log Type **IN** time should be greater than **Shift Type Start Time - Begin check-in before shift time**
3. For Log Type **OUT** time should be less Than **Shift Type End Time + Allow check-out after shift end time.**
4. Then only Shift would be mapped properly and your Checkin is valid.


B.Check your shift type:


![](/files/ant5ZYn.png)


1. Set **Process Attendance After** (Attendance will be marked Only after this date)
2. Set **Last Sync of Checkins** (It is the time before which all the checkin will be considered. Note: If it is less then shift end Time then it will not consider that day checkin because it means that shift is not over yet)


C.Click on Mark Auto Attendance to check whether it is working


Note: As our scheduler will run the process to mark attendance automatically every hour. But after upload or creating check-ins you need to check your **Process Attendance After and Last Sync of Checkins** in **Shift Type**.




