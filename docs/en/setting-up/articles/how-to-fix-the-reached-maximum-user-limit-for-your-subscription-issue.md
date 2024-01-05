
# Maximum User Limit Issue



Your ERPNext subscription depends on the number of System Users you subscribe for. Once you cross that limit, the system will not let you create any further number of users. For example, you have subscribed for 10 users. If you already have already created 10 System Users in your account, the system wont let you create the 11th System User, and you will get the below message.

  


![](/files/oP3RzNx.png)

  


To fix this, you will either have to:

1) Buy new users or

2) Disable the current users

  


However, sometimes, you may still face this issue even when you have not exhausted the number of System Users as per your subscription plan. For example, you have a limit of 5 System Users and you have only created 3 users. Yet while creating the 4th user, you get the above message. The reason for this can be that for some of the uses, the field of "Simultaneous Sessions" is greater than 1.

  


Every simultaneous session is considered as 1 System User. For example, if you have created 3 users and one of them has "Simultaneous Session" set to 3, then you have a total of 5 users, i.e. 3 + 1 + 1 = 5 simultaneous sessions/system users.

  


To allow the system to let you create more users, you will have to reduce the simultaneous sessions of these users. To do so, go to the User's profile, under Security Settings, set/reduce the "Simultaneous Session" accordingly.

  


![](/files/YQQ8cHw.png)

  


**Note:** You will still be able to create Website Users as there is no limit for the same.




