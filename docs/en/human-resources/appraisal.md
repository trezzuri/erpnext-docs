
# Appraisal



**An appraisal is a process in which an employee's performance is documented and evaluated.**


To create an Appraisal Cycle, go to:



> 
> Home > Human Resources > Performance > Appraisal
> 
> 
> 


## 1. Prerequisites


Before creating an Appraisal, you should create the following:


* [Appraisal Template](/docs/en/human-resources/appraisal-template)
* [Appraisal Cycle](/docs/en/human-resources/appraisal-cycle)


## 2. How to create an Appraisal


Appraisals can be created in bulk from the [Appraisal Cycle](/docs/en/human-resources/appraisal-cycle). 


However, if you want to create an appraisal manually, here are the steps:


1. Go to the Appraisal list, and click on New.
2. Select the Employee
3. Select the Appraisal Cycle.
4. If the Appraisal Template for the employee is already set in the cycle's Employees child table, it will be auto-fetched. Else you can select a template for the employee. Save.


## 3. Features


### 3.1 KRA Evaluation


Based on the KRA Evaluation Method selected in the [Appraisal Cycle](/docs/en/human-resources/appraisal-cycle) one of the following processes would be applicable:


#### 3.1.1 Automated Based on Goal Progress


This is the default KRA Evaluation method. 


In this method you can create goals and sub-goals aligned to your KRAs. 


A KRA vs Goals table will be visible in your appraisal document.


* **KRA and weightage**: Fetched from the appraisal template
* **Goal Completion (%)**: Your goal completion percentage will be auto-calculated based on the **progress** of the goals linked to your KRAs.
* **Goal Score (weighted)**: Based on the weightage assigned to each KRA, the Goal Score will be computed from the completion percentage. For ex: In the screenshot below, the Development KRA has 30% weightage and the employee has completed 75% of the goals. So the goal score is 22.5 out of 30, and so on.


You will finally get a **Total Goal Score** (out of 5) based on the **Goal Score (%)**.


![kra vs goals](/files/kra-vs-goals.png)


#### 3.1.2 Manual Rating


You can choose to rate Goals/KRAs manually. This is the original evaluation method used until v13.


1. Based on the template selected, the KRAs will be fetched in the Goals section.
2. Enter the score (0-5) for each KRA.
3. Based on the weightage mentioned, the **Score Earned** will be calculated for each KRA.
4. Save.


Based on the Score Earned for each KRA, the system will calculate the Total Score (out of 5) for the Employee.


![manual rating](/files/manual-rating.png)


### 3.2 Feedback


Employee Performance Feedback is captured in the [Employee Performance Feedback](/docs/en/human-resources/employee-performance-feedback) DocType.


But to get an overview of the employee's performance, you can see the history of all the feedback employee has received in the cycle under the Feedback tab.


You can see the rating summary with the average feedback score, no of reviews, and the percentage distribution of the stars the employee has received.


![feedback history](/files/feedback-history.png)



> 
> Note: Only submitted feedback documents are visible in this history and the view is permission sensitive.
> 
> 
> 


In every review, you can see the reviewer, their designation, avg rating given to the employee, the feedback and the time when the feedback was given. You can also click on the link icon to see the entire Employee Performance Feedback document.


![feedback link](/files/feedback-link.png)


If you have the required permissions, you can submit the performance feedback right from this view by clicking on the **New Feedback** button.


![add feedback](/files/add-feedback.png)


### 3.3 Self Appraisal


Under the Self Appraisal tab, employees can rate themselves and add reflections on their performance. The Total Self Score is calculated based on the rating and the weightage against each Feedback Criteria.


![self appraisal](/files/self-appraisal.png)


### 3.4 Final Score Calculation


The Final Score is calculated as an average of your Goal Score, Avg Feedback Score, and Self Appraisal Score.


![final score](/files/final-score.png)


### 3.5 View Goals


You can view the Employee's goals linked to that Appraisal Cycle by clicking on the View Goals button:


![goals appraisal](/files/goals-appraisal.png)


### 3.6 Approvals for Appraisals


Finally, once you have captured all the feedback and updated goals and self appraisal in the Appraisal document, you can submit it.


You can also set up a [Workflow](https://docs.erpnext.com/docs/en/setting-up/workflows) for approvals before Appraisal submission.


## 4. Related Topics


1. [Goal](/docs/en/human-resources/goal)
2. [Employee Performance Feedback](/docs/en/human-resources/employee-performance-feedback)




