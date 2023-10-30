
# Payment Terms Template



**Payment Terms Template allow you to club multiple payment terms together and fetch in transactions.**

After creation, the Payment Terms Table can be set to a specific Customer/Supplier. On selecting the Customer/Supplier in a transaction, the Payment Terms Template will be fetched automatically into the transaction.

For example:

If you receive payment in the slab of 30-70, then you can define Payment Term for each slab, i.e. 30% and 70%.

In the Payment Terms Template, you can select all the Payment Terms and define a template which can be easily applied in the sales and purchase transactions.

![Payment Terms Template](/files/payment-terms-template.png)  


## 1. Prerequisites

Before creating and using Payment Request, it is advisable to create the following first:

1. [Payment Terms](/docs/en/accounts/payment-terms)

## 2. How to create a Payment Terms Template

A Payment Terms Template tells ERPNext how to populate the table in the 'Payment Terms Schedule' section of the sales/purchase document.

You should use it if you have a set of standard Payment Terms or for ease of use.

1. Go to the Payment Term Template list and click on New.
2. Enter a name for the template.
3. Add the created Payment Terms in the table rows.
4. Make sure that the total Invoice Portion adds up to 100.
5. Save.

## 3. Video

### 4. Term based Payment Allocation

If 'Allocate Payment Based On Payment Terms' is enabled on a template, Payments made against the Invoice through Create->Payment will have allocation based on the Terms.

1. Template with 'Allocate Payment Based on Payment Terms' enabled. ![Screenshot 2023-08-01 at 10.30.32 AM](/files/Screenshot 2023-08-01 at 10.30.32 AM.png "Screenshot 2023-08-01 at 10.30.32 AM.png")
2. Invoice made with above template. ![Screenshot 2023-08-01 at 10.32.01 AM](/files/Screenshot 2023-08-01 at 10.32.01 AM.png "Screenshot 2023-08-01 at 10.32.01 AM.png")
3. Payment created against above invoice. ![Screenshot 2023-08-01 at 10.32.31 AM](/files/Screenshot 2023-08-01 at 10.32.31 AM.png "Screenshot 2023-08-01 at 10.32.31 AM.png")



