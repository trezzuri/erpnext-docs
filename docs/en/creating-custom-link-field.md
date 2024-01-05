
# Creating Custom Link Field



Link fields are the ones linked to another document type. For example, Customer field is a Link Field in Sales Order. This field is linked to the Customer master.

You can insert Custom Link Field by following the steps below.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customize > Customize Form

#### Step 2: Select Form

In Customize Form, select Document Type (Quotation, Sales Order, Purchase Invoice Item etc.). Once fields are updated in the accompanying table below, open a field above the one you wish to insert your Custom Field. Then click on "Insert Above" to insert the new Custom Field.

![Select Docytpe](/files/customize-custom-link-field.gif)![]()

#### Step 4: Custom Field Values

To set field as Link, enter values as below.

1. Label: Desired label that user wishes to display in the form.
2. Type: Set as 'Link'
3. Name: Desired name for the field
4. Options: Enter the name of the DocType to which the field is linked

![Enter Values](/files/customize-creating-custom-link-fields.png)![]()  


## Adding Filters to Link Field

Frappe provides a user-friendly approach to apply filters on Link Fields using the Form Builder.

You'll notice an action icon on all Link Fields within a Doctype, which gives you the option to select the filters you want to apply.![1](/files/1.png "1.png")For example, in the case of "Company", clicking on the icon will open a dialogue box where you can choose your desired filters.

![2](/files/2.png "2.png")![]()  


Once you've made your selection and clicked on apply, the filtered results will be displayed accordingly.

![3](/files/3.png "3.png")![]()  


If you're customizing a form and decide to change the filters, a "Reset To Default" button will appear. Clicking on this will revert the filters back to their original state. **However, it's important to note that any filters in "Customize Form" will override the default filters**

![4](/files/4.png "4.png")![]()  


**Note:** Filters applied through **frm.set\_query,** will take precedence over filters applied via the User Interface (UI).

  





