
# Manage Foreign Exchange Difference



In ERPNext, you can create transactions in the foriegn currency as well. When creating transaction in the foreign currency, system updates current exchanage rate with respect to customer/supplier's currency and base currency on your Company. Since Exchange Rate is always fluctuating, one might receive payment from the client on exchange rate different from one mentioned in the Sales/Purchase Invoice. Following is the instruction on how to manage different amount, availed in payment entry, due to exchange rate change.


## Add Expense Account


To manage currency difference, create Account **Exchange Gain/Loss**. This account is generally created on the Expense side of P&L statement. However, you can place it under another group as per your accounting requirement.


![Exchange Gain/Loss Ledger](/files/exchange-gain-loss-ledger.png)


## Book Payment Entry


![Auto Calculate Exchange Gain Loss](/files/exchange-gain-loss-auto-calculation.gif)




