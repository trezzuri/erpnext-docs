
# VAT/EXCISE Tax Implementation for UAE/KSA



### 1. Setting up Tax Registration No for customer, supplier and company


Set Tax Registration Number in the field, Tax ID for the Customer, Supplier, and Company.


1. For Customer
![TRN in Customer](/files/tax-id-customer.png)
2. For Company
![TRN in Company](/files/tax-id-company.png)


### 2. Setting up TAX Code for Products


Setup tax code in the item master, system will fetch same code in the sales/purchase invoice on selection of an item.


![Tax Code in Item](/files/tax-code-item.png)


### 3. Default Tax Templates


ERPNext provides you default tax template for vat(5%, zero, exempted) and excise(50%, 100%). You can create your own [tax template](/docs/en/setting-up/setting-up-taxes.html).


![Default Tax Template](/files/uae-tax-templates.png)


### 3. Making VAT Ready Invoices


If you have setup the TRN of your Customers and Suppliers, and your tax template, you are ready to go for making VAT Ready Invoices!


For **Sales Invoice**,


1. Select the correct Customer and Item and the address where the transaction will happen.
2. Check if the TRN of your Company and Supplier have been correctly set.
3. Check if the TAX Code has been set in the Item
4. Select the template that you have created based on the type of transaction
5. Save and Submit the Invoice


![VAT Invoice](/files/vat-invoice.gif)


### 4. Print Tax Invoice


ERPNext provides two default print format


1. Simplified Tax Invoice
![Simplified Tax Invoice](/files/simplified-invoice.png)
2. Detailed Tax Invoice
![Detailed Tax Invoice](/files/detailed-invoice.png)


### 5. Set-up VAT Accounts


Select the accounts that will be used for creating VAT invoices here.


![UAE VAT Account Settings](/files/uae-vat-account-settings.png)




