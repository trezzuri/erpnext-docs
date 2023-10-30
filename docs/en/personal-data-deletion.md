
# Personal Data Deletion



As a part of GDPR compliance, ERPNext has Personal Data Deletion.


Personal data deletion tool enables a user to delete their account and anonymize all the personally identifiable data a user has generated while using ERPNext. That is, personally identifiable information will be randomized. This includes personally identifiable data from your user account like: username, full name, birth date, phone numbers, mobile numbers, location, interests, bio, email signature, Email, Contact, Address, Communication, etc. It also includes data from Leads and Opportunities, the details you have saved like phone numbers, mobile numbers, fax, website, and name.


However, this excludes data that is required by law to be maintained by a business.


## 1. How to request account deletion


1. To begin deleting users account and personally identifiable data, you need to visit [host-name]/request-for-account-deletion (e.g. example.erpnext.com/request-for-account-deletion) in the URL field.


![Request for Account Deletion](/files/Screenshot 2021-12-01 at 8.53.14 PM.png)


2. Enter the email associated with your ERPNext account. After submitting your request, you will receive a success response.


![Deletion Request Success](/files/deletion-request-success.png)
3. This will send an email with a verification link to delete data to the email address associated with the user.


![Verification Email](/files/verification-email.png)
4. Once the user clicks on the verification link. A confirmation message will be displayed.
![Confirmed Verification](/files/confirmed-verification.png)


## 2. How deleting user's personal data works


The request to delete data is recorded in the doctype "Personal Data Deletion Request".


![Personal Data Download Request Doctype](/files/personal-data-deletion-request-doctype.png)


This doctype maintains three states of status to complete the process of removal of user data.


### 2.1 Pending Verification


This status indicates that the user has requested data deletion via the web-form. However, verification of this request is still pending. Search for Personal Data Deletion Request from the search bar.


![Pending Verification](/files/pending-verification.png)


### 2.2 Pending Approval


This indicates that the user has verified the request via email. This enables the option of "Delete Data" for System Managers.


![Pending Approval](/files/pending-approval.png)


### 2.3 Deleted


This indicates that the System Manager has clicked on the "Delete Data" button. This means that the user's personally identifiable data has been anonymized.


![Deleted User](/files/deleted-user.png)


### 3. Setting SLA for Personal Data Deletion Request.


You can also set an SLA for Personal Data Deletion Request through Website Settings. This will appear on the web form description.


* Go to Website Settings
* Scroll to the section called Account Deletion Settings
* In the **Account Deletion SLA (Days)** field set the number of days within which users request for Account Deletion will be fulfilled.
* If you enable **Show Account Deletion link in My Account page**, the form link will be visible to users on the My Account Page of the website


![Account Deletion Settings](/files/Screenshot 2021-12-01 at 8.50.39 PM.png)


### 4. Related Topics


1. [Personal Data Download](/docs/en/setting-up/personal-data-download)




