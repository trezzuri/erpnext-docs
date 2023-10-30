
# Employee Separation



**Employee Separation is a situation when the service agreement of an Employee with his/her organization comes to an end and the Employee leaves the organization.**


Employee Separation is created for an Employee who has resigned or terminated from the organization.


**Use Case:** Let's assume that following are the activities which need to be performed as soon as an Employee needs to be separated from the organization.


* Collect laptop
* Clear dues
* Delete Employee Email Account
* Collect identity card


In Frappe HR, these standard activities can be tracked in the Employee Separation Template. To access Employee Separation, go to:


> Human Resources > Employee Lifecycle > Employee Separation


## 1. Prerequisites


Before creating an Employee Separation, it is advisable that you create the following documents:


* [Employee](/docs/en/human-resources/employee)
* [Department](/docs/en/human-resources/department)
* [Designation](/docs/en/human-resources/designation)
* [Employee Grade](/docs/en/human-resources/employee-grade)


## 2. How to create an Employee Separation


1. Go to: Employee Separation > New.
2. Select the Employee. Once the Employee is selected, the corresponding Employee information such as Department, Designation and Employee Grade will automatically get fetched.
3. Select the [Employee Separation Template](#31-employee-separation-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Separation Template).
4. Enter the Resignation Letter Date.
5. Additionally, you can also enter the Exit Interview Summary.
6. Save and Submit.


![Separation Template](/files/employee-separation.png)


> Note 1: If an Employee Separation Template isn't created, you can directly fill the separation information in the Employee Separation doctype itself.


> Note 2: The 'Status' of the Employee Separation will change to Completed once all the associated Activities are complete.


## 3. Features


### 3.1 Employee Separation Template


The Employee Separation Template is a blueprint which contains a predefined list of Activities for Employee Separation. An Employee Separation Template can be created for a particular Department, Designation and Employee Grade.


To create a new Employee Separation Template:


1. Go to: Human Resources > Employee Lifecycle > Employee Separation Template > New.
2. Enter the Department, Designation and Employee Grade (optional).
3. Mention the Activities for separation. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
4. You can also schedule the Separation Activities by specifying the **Begin On (Days)** i.e. when the activity has to start and the **Duration (Days)** for the same.


![Separation Template](/files/separation-template.png)


### 3.2 Tasks and Assignments


On submission of the Employee Separation, a [Project](https://docs.erpnext.com/docs/v143/user/videos/learn/project-and-task) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v143/user/videos/learn/project-and-task) will also be created for each Activity.
If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.


You can view the created Projects and Tasks through View > Project/ Tasks.


Additionally, each Activity can be assigned weights based on its importance.


![Tasks and Assignments](/files/employee-sep1.png)


Based on the progress on the Tasks, progress can be updated in the Employee Separation process.


### 3.3 Employee Status


You can directly view the separated Employee through the Employee Separation doctype through View > Employee once the form is submitted.


## 4. Related Topics


1. [Employee Onboarding](/docs/en/human-resources/employee-onboarding)
2. [Employee Promotion](/docs/en/human-resources/employee_promotion)
3. [Employee Separation](/docs/en/human-resources/employee-separation)




