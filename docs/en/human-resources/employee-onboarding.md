
# Employee Onboarding



**In the process of hiring an Employee, there are set of standard activities which need to be executed. This feature helps you to maintain the masters of these activities, and create a set of tasks at the time of each Employee hiring.**


Employee Onboarding is created for a Job Application, who is approved for the hiring.


**Use Case:** Let's assume that following are the activities which need to be performed as soon as a job applicant is approved to be hired.


* Perform a legal and professional background check
* Create an Employee master
* Create an Email Account
* Create an identity card
* Allocate leaves


In Frappe HR, these standard activities can be tracked in the Employee Onboarding Template. To access Employee Onboarding, go to:


> Human Resources > Employee Lifecycle > Employee Onboarding


## 1. Prerequisites


Before creating an Employee Onboarding, it is advisable that you create the following documents:


* [Job Applicant](/docs/en/human-resources/job-applicant)
* [Employee](/docs/en/human-resources/employee)
* [Department](/docs/en/human-resources/department)
* [Designation](/docs/en/human-resources/designation)
* [Employee Grade](/docs/en/human-resources/employee-grade)


## 2. How to create an Employee Onboarding


1. Go to: Employee Onboarding > New.
2. Select the Job Applicant. once the Job Applicant is selected, the corresponding Employee will automatically get fetched.
3. Select the [Employee Onboarding Template](#31-employee-onboarding-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Onboarding Template).
4. Enter Date of Joining.
5. Save and Submit.


![Onboarding Template](/files/employee-onboarding1.png)


> Note 1: If an Employee Onboarding Template isn't created, you can directly fill the onboarding information in the Employee Onboarding doctype itself.


> Note 2: The 'Status' of the Employee Onboarding will change to Completed once all the associated Activities are complete.


## 3. Features


### 3.1 Employee Onboarding Template


The Employee Onboarding Template is a blueprint which contains a predefined list of Activities for Employee Onboarding. An Employee Onboarding Template can be created for a particular Department, Designation and Employee Grade.


To create a new Employee Onboarding Template:


1. Go to: Human Resources > Employee Lifecycle > Employee Onboarding Template > New.
2. Enter the Department, Designation and Employee Grade (optional).
3. Mention the Activities for onboarding. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
4. You can also schedule the Onboarding Activities by specifying the **Begin On (Days)** i.e. when the activity has to start and the **Duration (in Days)** for the same.


![Onboarding Template](/files/onboarding-template972e99.png)


### 3.2 Tasks and Assignments


On submission of the Employee Onboarding, a [Project](https://docs.erpnext.com/docs/v143/user/manual/en/projects/project) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v143/user/manual/en/projects/tasks) will also be created for each Activity.
If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.


You can view the created Projects and Tasks as shown below:


![Onboarding Template](/files/project-task.png)


Additionally, each Activity can be assigned weights based on its importance.


![Tasks and Assignments](/files/employee-onboarding3.png)


Based on the progress on the Tasks, progress can be updated in the Employee Onboarding process.


### 3.3 Employee Creation


You can directly create an Employee through the Employee Onboarding doctype (if not already created) once all the mandatory onboarding tasks are complete.


![Onboarding Template](/files/onboarding-employee.png)


## 4. Related Topics


1. [Employee Promotion](/docs/en/human-resources/employee_promotion)
2. [Employee Separation](/docs/en/human-resources/employee-separation)
3. [Employee Transfer](/docs/en/human-resources/employee_transfer)




