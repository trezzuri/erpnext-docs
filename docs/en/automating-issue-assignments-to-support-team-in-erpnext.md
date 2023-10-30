
# Automating Issue Assignments in ERPNext



Modern support automation tools demonstrably improve customer service. Automating the assignment of support issues ensure that every issue ticket has been assigned a product expert and the customer seeks resolution to their queries faster. Assignment Rule has been introduced in v12 and here's how you can automate your support team's troubles away.  
First, we need to setup an email account that appends the incoming emails received there into the "Issue" DocType of ERPNext.**1) Create an Email Account:**You need to update email domain and setup your support email address in ERPNext's Email Account. To learn about email setup, please check out [this link](https://www.youtube.com/watch?v=ChsFbIuG06g&t=122s)  
![](/files/NPp14kS.png)  
**2) Append to Issue:**The checkbox, "Enable Incoming" has to be selected to allow emails sent on this email address to be received here. We need to capture them in a DocType, which is mentioned under "Appends To". In this case, we want to append all incoming emails to Issue  
![](/files/STAm8ko.png)  
This is a one-time configuration and you won't have to worry about it unless you require to change the password of that email address via third party apps. The Issue List will get populated with the emails that are sent here. With the use of Assignment Rules, we can organise the customer support team's schedule and ensure timely resolution for all open support tickets.  
**3) Setting an Assignment Rule:**  
![](/files/5q4HvOT.gif)  
**4) Based on the rule defined in step (3), the assignments will be done automatically**These are done as in when an Issue is created or updated. Check out below GIF to see automation in action when an issue ticket's status is *updated*:  
![](/files/Qb0kAzo.gif)  
Note: If needed, the rule can also be disabled/updated:  
![](/files/PZbCDuu.png)  
Similarly, you can automate the Sales process in ERPNext for assigning leads to your Sales team and ensure more conversion rates!! Thanks for reading this article! If you need further assistance with this, please reach our community [here](https://discuss.erpnext.com/)


