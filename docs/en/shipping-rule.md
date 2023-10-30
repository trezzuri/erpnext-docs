
# Shipping Rule



Shipping Rule master helps in defining a rule based on which shipping charge is applied on a sales transactions.


Most of the companies (mainly retail) have shipping charge applied based on the invoice total. If invoice value is above certain value, then shipping charge applied are lesser. If invoice value is less, then shipping charges applied are bit more than high shipping charges applied on a high value invoice. You can setup Shipping Rule to address the requirement of varying shipping charge based on the Net Total of sales transaction.


To setup Shipping Rule, go to:


`Selling > Setup > Shipping Rule` or `Accounts > Setup > Shipping Rule`


#### Shipping Rule Conditions


![Shipping Rule Conditions](/files/shipping-rule-conditions.png)


Referring above, you will notice that shipping charges are reducing as value is increasing. This shipping charge will only be applied if transaction total falls under one of the above range.


#### Valid for Countries


You can set Shipping Charges valid for all the countries, or specify specific Country. If specific countries mentioned, then Shipping Charges will be applied only if Customer's country matches Country mentioned in the Shipping Rule.


![Country Specific Shipping Rules](/files/country-specific-shipping-rules.gif)


#### Shipping Account


If shipping charges are applied based on Shipping Rule, then more values like Shipping Account, Cost Center will be needed as well to add row in the Taxes and Other Charges table of transaction. Hence these details are tracked as well in the Shipping Rule.


![Shipping Account](/files/shipping-account.png)


#### Shipping Rule Application


Following is an example of how shipping charges is auto-applied on Sales Order based on Shipping Rule.


![Shipping Rule in Sales Order](/files/shipping-rule-in-sales-order.gif)




