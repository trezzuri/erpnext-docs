
# Tax Withholding Category



**Tax Withholding Category is Tax Deducted at Source.**


According to this, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the govt wants the payers to deduct tax beforehand and deposit it with the government.


To access the Tax Withholding Category list, go to:



> 
> Home > Accounting > Taxes > Tax Withholding Category
> 
> 
> 


## 1. Prerequisites


Before creating and using a Tax Withholding Category, it is advised to create the following first:


1. [Supplier](/docs/en/buying/supplier)
2. [Customer](/docs/en/CRM/customer)


## 2. How to create a Tax Withholding Category


In ERPNext, Tax Withholding Categories for most cases are available by default, however, you can create more if needed.


1. Go to the Tax Withholding Category list and click on New.
2. Enter a unique name, eg: Section 194C Individual.
3. Enter a Category Name (Dividends, Professional Fees, etc,.).
4. Enter a Tax Withholding Rate against a [Fiscal Year](/docs/en/accounts/fiscal-year).
5. You can set the threshold for a single invoice or sum of all invoices.
6. Select an account against your Company to which tax will be credited.
7. Add more companies and accounts as needed.
8. Save.


![Tax withholding Category](/files/tax-withholding-category.png)


Under accounting details, the TDS account is added for each Company in the system.


### 2.1 Assigning Tax Withholding to Supplier


After saving, it can be assigned to a Supplier:


![Tax withholding Category in Supplier](/files/tax-withholding-category-in-supplier.png)


### 2.2 How does the threshold work?


Consider a Supplier on whom a Tax Withholding Category is applied.


For example, let's say a rate of 5% will be applicable on invoice where Single threshold is 20,000 and the Cumulative threshold is 30,000. If an invoice is created with a grand total of 20,000 then the single threshold will be triggered and a 5% tax would be charged.


But if the invoice amount totaled up to be 15,000 then no tax will be charged as it didn't cross the threshold. If again another invoice is created against the same supplier with a total of 15,000 then although it didn't cross the Single threshold, charges will be deducted since the sum of the last invoice and this invoice adds up to be 30,000 which is equal to the specified Cumulative threshold.


## 3. Using Tax Withholding


### 3.1 Use in Purchase Invoice


In the following example, we have selected 'TDS - 194C - Individual' which has a single threshold of 30,000, cumulative threshold of 1,00,000 and rate of 1%.


1. If the **Supplier** has the tax withholding field set, then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not.


![Tax Withholding Category in Purchase Invoice](/files/tax-withholding-category-in-purchase-invoice.png)


1. Let's create an invoice for 90,000. Saving the invoice automatically calculates tax and appends it in the taxes table.


![Tax Withholding Category in Purchase Invoice](/files/withheld-tax-calculation-in-purchase-invoice.png)
2. To see the effect of Cumulative threshold, let's create an invoice with of amount 10,000 and submit it.


![Tax Withholding Category Cumulative Threshhold](/files/tax-withholding-category-cumulative-threshold.png)


Although the invoice amount didn't cross the Single threshold (30,000), we see that tax has been charged. This is because the previous and the current invoice adds up to be 1,10,000 which exceeds the Cumulative threshold. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly.



> 
> Note: On submitting the invoice, three GL Entries are created:
> 
> 
> 



> 
> 1. First for debit from the expense head
> 2. Second for credit in Creditors account
> 3. Third for credit in the account selected in Tax Withholding Category.
> 
> 
> 


### 3.2 Deducting Tax at source on Advances


#### 3.2.1 Deduction Advance TDS against Purchase Order


1. Set up Tax Withholding Category against supplier and make a Purchase Order against the supplier. One point to remeber here is not to check "Apply Tax Withholding" check in the PO as the PO has to generated for the full amount
2. Create Payment Entry against that Purchase Order, In the Taxes and Charges section enable "Apply Tax Withholding" and enter other details and then save and submit the entry.


![Tax Withholding Payment Entry](/files/Tax-Withholding-Payment Entry.png)


3. Create a Purchase Invoice against this order and enable "Set Advances and Allocate(FIFO)" so that payment linked to the corresponsing order is automatically applied. No Tax will be withheld in the Purchase Invoice if the Tax paid on advance in more than or equal to the tax amount in Invoice. Tax Will be withheld only for the excess amount if applicable.


### 3.2.2 Deducting TDS against advances paid (Using Payment Entry)


1. Select "Payment Type" as "Pay"
2. Select "Party Type" as "Supplier" and the appropriate supplier
3. Enter paid amount, paid amount should be the amount before TDS deduction
4. Under the Taxes and Charges section check "Apply Tax Withholding Amount" and select Tax Withholding Category
5. Click on Save. TDS will be auto applied
6. Submit the entry
7. Same will also be visible in TDS payable monthly report


### 3.3 Setting up TCS - Section 20C(1H) for eligible customers


In the following example, we have create a Tax Withholding Category for [TCS - Section 20C(1H)](https://taxguru.in/income-tax/faqs-tcs-sales-goods-section-206c1h.html) and set it up against an eligble customer.


1. We will first create a Tax Withholding Category named **TCS - Section 20C(1H)** and we set cumulative threshold to 50 Lakhs as per the scheme.


![Tax Withholding Category For TCS](/files/tax-withholding-category-for-tcs.png)


1. If a **Customer** is expected to crosses the sales threshold of 50 Lakh in current Fiscal Year, then we can set the Tax Withholding Category of the customer to TCS - Section 20C(1H) for automatically calculation TCS on sale of goods against the customer's invoices.


![TCS in Customer](/files/tcs-eligible-customer.png)
2. Let's create an invoice for 50 Lakhs against the eligible customer. Saving the invoice automatically calculates tax and appends it in the taxes table.


![TCS Calculation in Sales Invoice](/files/tcs-invoice.png)


Since the invoice cross the Cumulative threshold (50 Lakhs), we see that tax has been charged. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly. Note that, as per the scheme, the TCS is calculated on the amount exceeding the threshold i.e 0.075 % of 10 Lakhs.


### 3.4 Advanced options in Tax Withholding Category


![Advance TDS Options](/files/tds-advance-options.png)


1. **Consider Entire Party Ledger Amount**: In many situations threshold has to be calculated on the entire party ledger amount instead of the sum of the net total of specific invoices. On enabling this check cumulative threshold will be checked against the sum of the grand total of all the invoices against a particular Supplier/Customer.
2. **Only Deduct Tax On Excess Amount**: On enabling this tax will be deducted only on the amount exceeding the threshold and not the entire amount. For example, if the cumulative threshold is 50000 and if the cumulative amount goes till 52000 the tax will be applied only on 2000 and not the entire 52000.
3. **Round Off Tax Amount**: Enabling this check will round off the calculated tax amount to the nearest integer value (Normal Rounding Method)


### 4. Related Topics


1. [Tax Rule](/docs/en/accounts/tax-rule)
2. [Supplier](/docs/en/buying/supplier)
3. [Customer](/docs/en/CRM/customer)




