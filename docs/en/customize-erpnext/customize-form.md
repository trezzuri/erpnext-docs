
# Customize Form




**Customize Form is a tool which enables you to make changes to a Form Type or a Document Type (DocType) on the front-end.**


It allows you to insert [Custom Fields](/docs/en/customize-erpnext/custom-field) as per your requirement or customize the properties of standard fields.


Before we venture to learn the Form Customization tool, [click here](/docs/en/customize-erpnext/doctype) to understand the architecture of forms in ERPNext. It will help you in using the Customize Form tool more efficiently.


To access Customize Form, go to:


> Home > Customization > Form Customization > Customize Form


You can also go to the list view of any DocType and select Customize from the Menu options.


![Customize Option in List View](/files/customize-option-in-list-view.png)


## 1. How to Customize a Form


1. Click on Customize Form.
2. You will be redirected to a page wherein you will be asked to Enter Form Type.
3. Once you enter the Form Type in this field, the page further expands and you will be able to see multiple features.


![Select DocType in Customize Form](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. Options While Customizing a Form


1. **Change Label**: This field gets fetched via Custom Translation. You can change the name of the field to suit your industry/language. E.g., if you are a services business and you want to change the Label from 'Customer' to 'Consumer', the same can be done via [Custom Translation](/docs/en/setting-up/print/custom-translations) and the same shall be reflected here.


![Change Label](/files/customize-customize-form-label.png)
2. **Title Field**: This field can be used to generate the title while viewing the lists. Any "Data" type field can be set as the Title Field while viewing the forms in the list view. E.g., if you wish to view the list of all your employees with the Title field as the 'Employee Code' instead of Employee Name, the same can be configured here. Check our article on [Document title](/docs/en/customize-erpnext/document-title) for more information.


*Learn more about field types [here](/docs/en/customize-erpnext/articles/field-types.html).*
3. **Default Print Format**: For a single DocType, there could be multiple Print Formats. Here you can select the default Print Format for the selected DocType. For e.g., a company may have different Letter Heads for different purposes which can be configured through Print Formats. However, you can select two different Default Print Formats for a Sales Order and an Appointment Letter. Check [Custom Print Formats](/docs/en/customize-erpnext/print-format) for more information.
4. **Image Field**: You can select an "Attach Image" Field for your Image Field. This becomes the Image representing that particular DocType. E.g., the 'Image Field' for an Employee could be their photograph or a snapshot of their ID cards; the same can be configured here.


![Image Field in DocType](/files/customize-form-image-field.png)
5. **Max Attachments**: You can enter the maximum number of attachments that could be added to this DocType.
6. **Search Fields**: While creating any DocType, you may want to link a particular field to another DocType. For ease in selection, you can also ensure that you are able to see the value of another field of the latter DocType in the search result. For more information [click here](/docs/en/customize-erpnext/articles/search-record-by-specific-field).
7. **Sort Field**: Records in any DocType List are generated based on the Field that you set at the Sort Field over here. E.g., for Items, if you want your list to be generated as per Item Name, you can configure the same here.


![Sort Field](/files/customize-sort-field.png)
8. **Sort Order**: You can select whether you want the Sorting to be done in Ascending Order or Descending Order. To get more understanding on Sort Field and Sort Order, check out [Customizing Sorting Order in the List View](/docs/en/customize-erpnext/articles/customizing-sorting-order-in-the-list-view).
9. **Default Email Template**: For a single DocType, there could be multiple [Email Templates](/docs/en/setting-up/email/email-template). Here you can set the default Email Template for the selected DocType. For example, you can set a different Default Email Template for a Sales Order and an Appointment Letter.


### 1.3. More Properties


* **Hide Copy**: This box, when checked, restricts a User to create a 'Copy' of a particular Form.
* **Is Table**: This option is available only while customizing the Forms which are present in table forms in the system. For e.g., if you are creating an Item Table to be added into a Custom Form, you can enable this option. Check out [Child Table](/docs/en/customize-erpnext/articles/customizing-data-visibility-in-child-table) for more information.
* **Quick Entry**: Checking this box will allow you to create a 'Quick Entry' using a particular form. This means that whenever a user is creating this Form from another existing Form, a box will Pop Up which will allow the user to create the DocType by entering only the basic details. For example, check Quick Entry in [Journal Entry](/docs/en/accounts/journal-entry#11-quick-entry).
* **Track Changes**: Checking this box will ensure that any changes made by any of the users to this DocType will be tracked and displayed.


![Track Changes](/files/customize-track-changes.png)
* **Track Views**: This option will give you a trail of all the views towards this particular DocType.
* **Allow Auto-Repeat**: This option, if checked, will allow you to enable Auto Repetition of a DocType periodically. E.g., if there is a Sales Order which has to be made multiple number of times, you can enable this option and then [Set Up Auto Repeat](/docs/en/automation/auto-repeat) for any particular Sales Order.
* **Allow Import**: This option will allow the user to Import data from any files. Check out [Data Import Tool](/docs/en/setting-up/data/data-import) for more information.
* **Show Preview Popup**: This option was introduced in Version 12. If checked, a small popup will appear on hover of links of this document type (in list view and other link fields). This popup will contain the mandatory fields of the document and the fields for which `in_preview` is checked. Check out [Link Preview](https://erpnext.com/version-12/release-notes/features#link-preview) for more information.


Once you click Update, your Customizations will be updated to the Form.


### 1.2. Customizing the Fields


Every form in ERPNext has a standard set of fields. If you need to capture some information, but there is no standard field available for it, you can insert Custom Field in a form as per your requirement. Adding, editing or deleting of Fields can also be done here. You can also place the fields as per your requirement in the form by adding it below or above any other already present fields. [Click here](/docs/en/customize-erpnext/custom-field) for more information on Custom Fields.


## 2. Videos







