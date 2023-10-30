
# Balance in Temporary Account



**Question:**


We used Temporary Opening Account for updating opening balance. After having update balance in all the Balance Sheet account, there is still some balance in Temporary Account? What is the cause of this balance, and how to make balance in this account to zero?


**Answer:**


When updating an opening balances in ERPNext, you have to first ensure that Balance Sheet in the previous system is tallying (Asset = Liability).


Then you start updating the opening balances for above statement, using Temporary Opening as an account to balance the entry. In the end, when opening is updated for all Asset and Liability accounts, the Temporary account's balance becomes zero automatically.


If you still have balance in the Temporary Account, it could be for one of the two (or both) the reasons.


1. The Balance Sheet followed for updating opening balance was not closed properly and it's Asset and Liability value was not tallying.
2. When updated opening balance in ERPNext, the Temporary Opening Account was not used consistently.


Kindly review the above points as they could be the cause of balance left in the Temporary Opening Account.




