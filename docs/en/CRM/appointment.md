
# Appointment



**An appointment is a prearranged meeting between a Lead and an Employee of your Company.**


Appointment document type can be used to schedule and manage interaction with a [Lead](/docs/en/CRM/lead) or an [Opportunity](/docs/en/CRM/opportunity).


To access Appointment list, go to:



> 
> Home > CRM > Sales Pipeline > Appointment
> 
> 
> 


## 1. Prerequisites


1. [Appointment Booking Settings](/docs/en/CRM/appointment-booking-settings)
2. [Holiday List](/docs/en/human-resources/holiday-list)
3. [Employee](/docs/en/human-resources/employee)
4. [Lead](/docs/en/CRM/lead)
5. [Email](/docs/en/setting-up/email/email-account)


## 2. How to create an Appointment


1. Go to Appointment list, click on New
2. Select scheduled time of the appointment
3. Enter customer details
4. In linked documents, if you have already created a Lead for the Customer you can set it here. Otherwise the system will automatically create a new lead with the customer details from previous step.
5. Save.
![New Appointment](/files/new-appointment.png)


### 2.1 Creating appointments via website


Your Customers/Leads can create appointment using the webpage `yoursitename.com/book_appointment`.


First they need to set a date, time.
![Appointment Webform](/files/appointment-webform.png)


Then, add more details:
![Appointment Details](/files/appointment-details.png)


It'll match the customer email with leads in the system and if one is found, it is linked with the document.
If no lead is found, the appointment is marked as "Unverified" and an email is sent to the customer to confirm their email


## 3. Features


### 3.1 Autoassign


Appointments are automatically assigned to employees as per the `Agents` list in [Appointment Booking Settings](/docs/en/CRM/appointment-booking-settings). The agent with the least number of assignments for the day of the appointment and who is free in the scheduled time is assigned to the appointment.


### 3.2 Email confirmation


If there is no matching lead in your system, an email will be sent to the email address in the appointment to confirm if the email address is valid. Upon confirmation, a new Lead will also be created in the system along with the Appointment.




