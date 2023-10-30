
# Invoice rounding issue



  
**Question:**



In Sales Invoice, in-words in being printed with the rounding off even though it is disabled via Global Defaults.In the Global Defaults one can always Disable Rounded Total via the following checkbox:
![](/files/OkUOjHx.png)
  

**Answers:**


If this configuration hasn't done the trick for you, you need to also check the currency master once.
To do this, type **Currency** in the awesome bar (Ctrl/Cmd + G). In the currency master, open the currency for which you are facing the issue:
  

![](/files/l5TqjSq.png)
  

Here make sure that the rounding is set correctly. For example, the smallest fractional value for INR should be 0.01 and not 0.05. Update this value, and then update the transaction.


