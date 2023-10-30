
# Fetching data from a linked master



**Question:** How to add terms and conditions in driver form?  
**Steps:**  
1. Go to the doctype where you want the to add the terms and conditions.
2. Go to Menu > Customize

![](/files/c6WTMJQ.png)  
1. You will see a table with a list of fields. These are the fields in your driver page.
2. Scroll down to the section/field after which you want to add terms and conditions.
3. Click on the small icon on the right side. This will expand the selected field.
4. You can add a new field above on below by clicking on *Insert Above/Below*.![](/files/AsJWH8L.png)
5. Add a new field as show below:![](/files/YGEuBrn.png)For more details on adding a custom link field, refer [this link](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/creating-custom-link-field).
6. Add a second field below this:![](/files/LoWglZL.png)How does this work? In Fetch from, we are adding the following details: doctype.field. In the Terms and Conditions doctype, the field where we add the terms is named *terms* and it is of type: Text Editor. For *fetch from*to work, the data must be in the following format: link*field*name.field*to*fetch
7. Once this is done, click on **Update**, and go back to your list. Click on Ctrl + Shift + R to reload.
8. When you select the terms template in the driver, the system will fetch the conditions from the selected template:![](/files/b7hVL7Y.png)





