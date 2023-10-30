
# Migration Guide



Once you migrate to version-14, most probably you'll be using the India Compliance app to manage your GST compliances
This guide will help you with the changes that you might have to make in your GST and chart of accounts configuration 


### Scenario 1: You are using a single GST Account for all the types like Input and Output and your GST Settings in version 13 looks somewhat similar as shown below


![single account](/files/single-account.png)


While using the India Compliance app it is mandatory to setup separate accounts for each type so in case you are migrating from version 13 to version 14 you can update your accounts as follows.


You can use your current GST Accounts with type as "Output" and make new accounts for types "Input" and "Reverse Charge". Your new GST Settings should look as follows in this case.


![new settings](/private/files/new-settings.png)


Now in case you still want to see the net GST Balance in one single account a journal entry can be posted to move the balance to Input GST Account and the final balance will give you the payable GST.


### Scenario 2: You have multiple GST Accounts based on either rate or maybe states and your GST Settings looks as shown below


![multipe account](/files/multipe-account.png)


All your GST Accounts will have to merged into a single account, in case you are already using separate input and output accounts, merge the accounts for each type and update the GST Accounts against each type.


The "Output CGST 5%" and "Output CGST 9%" accounts will be merged into a single account "Output CGST", same goes for SGST and IGST accounts


In case you are using multiple accounts for rates or any other reason but same account for type "Input"(Purchase) and "Output"(Sales) then follow the process mentioned in Scenario 1 post merging all the accounts.




