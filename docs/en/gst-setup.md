
# GST Features in ERPNext



### 1. Setting up Company and Masters


GST Law requires that you maintain the GSTIN details for all your customers and suppliers. In ERPNext, GSTIN is linked to both **Address** and **Parties**.


#### 1.1 Update GSTIN Information for your Company


Update the GST Details to the company. GST Validations will apply to all transactions for your company based on the GST Category set for your company.


Also, create or update your Company Address with appropriate GST Details.


![Company GST Details](/files/company_gst_details.gif)


#### 1.2 Create Customers and suppliers


In a very similar manner create or update your customers and suppliers with GSTIN Details. Also, they need to be updated in relevant addresses of the parties.


GST will be applied and validated to a specific transaction based on this master. GST Details will be first fetched from the Address. If the Address is not available in a transaction, it will be applied as per the Customer or Supplier.


![Create Party Quick Entry](/files/create_party_quick_entry.gif)


### 2. Pre-Packed Configurations


#### 2.1 HSN Codes


According to the GST Law, your itemised invoices must contain the HSN Code related to that Item. ERPNext comes pre-installed with all 12,000+ HSN Codes so that you can easily select the relevant HSN Code in your Item


![HSN in Item](/files/hsn-item.gif)


#### 2.2 Tax Accounts


With new installations, you get default GST Accounts created for your company.


![GST Ledgers](/files/gst-ledger.png)


#### 2.3 Tax Templates


Default Sales and Purchase Tax Templates are pre-configured for your company.


![GST Tax Template](/files/gst-tax-template.png)


#### 2.4 Item Tax Templates


For different tax rates, you get item tax templates preconfigured for your company. These are useful where you wish to have different item tax rates configured other than the ones configured in default Sales and Purchase Tax Templates.


![GST Item Tax Template](/files/gst_item_tax_template.png)


#### 2.5 GST Accounts in GST Settings


Where GST Accounts are auto-created, their settings are automatically updated for your company in GST Settings. This will ensure GST Validations and appropriate GST Reports.


![GST Settings for GST Account](/files/gst_settings_accounts.png)



> 
> Where you wish to have different default settings, you must configure them manually at all the above places.
> 
> 
> 


### 3. Making GST Ready Invoices


If you have set up the GSTIN of your Customers and Suppliers, and your tax template, you are ready to go for making GST Ready Invoices!


#### 3.1 Creating Sales Invoice


1. Select the Customer and Item.
2. Check if the GSTIN of your Company and Customer have been correctly set.
3. Check if the HSN Number has been set correctly in the Item.
4. Select **In State GST** or **Out of State GST** as a tax template.
5. Save and Submit the Invoice.


![GST Invoice](/files/gst-invoice.gif)


#### 3.2 Printing GST Tax Invoice


To print Tax Invoice as per GSTN guidelines, please select **GST Tax Invoice** print format. This print format includes company address, GSTIN numbers, HSN/SAC Code and item-wise tax breakup. And while printing select the correct value of the Invoice Copy field, to mention whether it is for the Customer, Supplier or Transporter.


![Sample GST Tax Invoice](/files/sample-gst-tax-invoice.png)


### 4. GST Transactions


#### 4.1 Reversal of Input Tax Credit


To book reversal of ITC go to Journal Entry doctype and follow the following steps


1. Select "Entry Type" as "Reversal Of ITC"
2. In "Reversal Type" select "As per rules 42 & 43 of CGST Rules" or "Others" based on the types of reversal
3. Select appropriate Company Address (GSTIN) for which ITC is being reversed
4. Fill the accounts and amounts in the Accounting Entries as shown below
5. Save and Submit


![Reversal of Input Tax Credit](/files/reversal-of-itc.png)


### 5. Setting up reverse charge and posting reverse charge purchase invoices


#### 5.1 Add reverse charge accounts in GST Settings


Add reverse charge accounts for GST as shown in the image below and check the "Is Reverse Charge Account" as shown in the image below. Instead of separate reverse charge account the Output GST tax account used for sales can also be marked as reverse charge account


![GST Reverse Charge Settings](/files/gst-reverse-charge-setting.png)


#### 5.2 Making purchase invoices liable to reverse charge


To make purchase invoices liable to reverse charge invoices please follow the following steps


* Select Supplier and add items to the invoice as usual
* Select "Reverse Charge Applicable as "Y" under GST Details Section
* If GST paid is eligible for input tax credit, in "Eligibility for ITC" select "ITC on Reverse Charge"
* "Add" taxes using the regular Input Tax account heads


![Reverse Charge](/files/reverse-charge-add.png)


* "Deduct" the same amount of taxes using the reverse charge accounts so that the net GST payable by the supplier is 0


![Reverse Charge](/files/reverse-charge-deduct.png)


* Save and Submit


In order to avoid manual selection of accounts and automate this process please follow below steps


* Create Tax Category for reverse charge


![Reverse Charge Tax Category](/files/reverse-charge-tax-category.png)


* Update tax category in the relevant supplier masters


![Supplier Tax Category](/files/supplier-tax-category.png)


* Create Purchase Taxes and Charges template for reverse charge


![Reverse Charge Template](/files/reverse-charge-template.png)


* Once this configuration is done, on selection of supplier appropriate Purchase Taxes and Charges Template will be applied


### 6. Reports


ERPNext comes with most of your reports you need to prepare your GST Returns. Go to Accounts > GST India head for the list.


![GST Reports](/files/gst-reports.png)


You can check the impact of your invoice in the **GST Sales Register** and **GST Itemised Sales Register**


![GST Itemised Sales Register](/files/gst-itemised-sales-register.png)




