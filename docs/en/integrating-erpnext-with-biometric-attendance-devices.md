
# Integrating ERPNext With Biometric Attendance Devices



## Background


The Attendance punch logs from the biometric device are check-in and check-out logs of an employee. ERPNext has a provision to store these logs in a document called Employee Checkin.


Attendance can then be marked based on the [Employee Checkin](/docs/en/human-resources/employee_checkin) records and the [Shift Type](/docs/en/human-resources/shift_type) of the employee by using [Auto Attendance](/docs/en/human-resources/auto-attendance)


Hence, integrating your Biometric Device (*or any access control system that collects IN/OUT logs*), can be done using the following steps:


### 1. Setting up Auto Attendance to mark attendance from the Employee Checkin


Before you import/sync employees' Check-in and Check-out logs into your ERPNext system, you will have to set up the employees and their shifts to be able to generate attendance using the Auto Attendance feature in ERPNext.


Please refer to the following link to set up Auto Attendance: [Set up Auto Attendance](/docs/en/human-resources/auto-attendance)


Once you have set up the employee master and assigned shifts to the employees, you are now ready to proceed to the next step.


### 2. Populating the Biometric Punch Logs into ERPNext's Employee Checkin


Depending on your biometric system and its features, there can be a lot of ways you can populate the Punch logs into ERPNext:


1. **Use ERPNext's Data Import Tool**:


	* The simplest possible solution (in terms of implementation complexity) would be to generate an Excel/CSV of the Check-in/Check-out and use the built-in data import tool in ERPNext to periodically import the logs to your Employee Checkin Document
	* Please refer to [ERPNext's Documentation on Data Import Tool](/docs/en/setting-up/data/data-import) for more on how to do this.
2. **API Integration**:


	* You can automate the process of syncing the Biometric Punch Logs by integrating it with the available API in ERPNext.
	* This method requires some technical knowledge and you should probably get in touch with your ERPNext implementor or Biometric system vendor.
	* Steps:
		1. You will first need to create a [user](/docs/en/setting-up/users-and-permissions/adding-users#1-how-to-create-a-new-user) in your ERPNext instance that would be used for creating logs since this API method requires login. Make sure this user has all the required permissions to create Employee Checkin.
		2. [Generate API Key and API Secret](/docs/en/setting-up/users-and-permissions/adding-users#210-api-access) for the user which will be used for authentication.
		3. Make sure you have set the [Attendance Device ID (Biometric/RF tag ID)](/docs/en/human-resources/auto-attendance#3-setup-attendance-device-id-field-in-employee) for the employees based on your Biometric Device.
		4. The API implementation details can be found [here](https://github.com/frappe/erpnext/blob/develop/erpnext/hr/doctype/employee_checkin/employee_checkin.py#L49-L78) and the API can be accessed at: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
		5. You can write a script to send a POST request to the API. This endpoint finds the relevant Employee using the employee field value and creates an Employee Checkin. Details of the API endpoint:
			+ URL: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
			+ Method: `POST`
			+ Params:
				- `employee_field_value`: The value to look for in the employee field. This will be the Attendance Device ID found in your biometric logs and also set in the employee record.
				- `timestamp`: The timestamp of the Log. Currently expected in the following format as a string: '2022-04-08 10:48:08.000000'
				- `device_id`: (optional) Location / Device ID. A short string is expected.
				- `log_type`: (optional) Direction of the punch if available (IN/OUT).
				- `skip_auto_attendance`: (optional) Skip auto attendance field will be set for this log (0/1)
				- `employee_fieldname`: (Default: `attendance_device_id`) Name of the field in Employee DocType based on which employee lookup will happen.
			+ Response: Returns an Employee Checkin document object which was inserted.
3. **Set up a python script on your computer to integrate ZKTeco or similar devices**:


	* This method works only for ZKTeco or similar devices that use the ZKProtocol to communicate over TCP/IP.
	* This script is available at: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
	* Please follow the instructions given on the script page to set it up on your computer.
	* This Script pulls biometric logs from a supported device and uses the API mentioned in the above step to push the data into ERPNext.


## Frequently Asked Questions


### 1. How do I select a Biometric Device which is compatible with ERPNext?


If you are using method 1 or 2, you don't need to worry about compatibility. 


However, for the third method, the push biometric app internally uses a script that is compatible with the devices listed over [here](https://github.com/fananimi/pyzk#compatible-devices). Typically, any ZKTeco or similar device that uses the ZKProtocol to communicate over TCP/IP should work. As far as buying the device is concerned, we suggest you opt for a device trial with the vendor if possible, where the device can be tested with the sync tool, as it's dependent on multiple factors when it comes to compatibility.


### 2. How do I know which method to use for integrating my biometric device with ERPNext?


Method 1 is feasible in any situation but requires you to manually import logs periodically. Methods 2 and 3 need some monitoring and work for a one-time setup for the log syncing to be automated.


**For a single location set up:**


In the Push Biometric Device approach, the tool needs to be able to communicate with your biometric device via TCP/IP. So, it is usually the case that it needs to run on the same LAN Network as the biometric device. To sync these fetched logs to your ERPNext instance it uses API access. This works best when you have a single location set up.


**For a multi-location set up:**


In this case, we usually recommend method 2 where most biometric vendors provide services to sync the biometric device logs from multiple locations to ERPNext via API access. Method 3 (push biometric attendance tool) can also work in this case if you have some networking knowledge.




