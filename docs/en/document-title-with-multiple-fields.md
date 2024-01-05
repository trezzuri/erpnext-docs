
# Document Title with multiple fields



Ever wondered about creating a document title with more than one field? For example, let's say your sales invoice should have the title of the customer name (which is present by default) and its tax ID.


How will you do this? Well, here's an interesting customisation ability of the framework which can do this without any need of scripting.


Here are the steps,


1. Make sure you have a field that is going to be referred to for creating the title of the document.
2. The basic setup ends by adding this field name in the view settings of the doctype for the title.
3. If you want to add more to it,
4. Add the field links in the **default** of the field in this format **{field\_name}**


***Here's an example of how it looks***


![](/files/Eb81KLe.png)


         b. This will result in a multifield title for the selected doctype.


This can be extended to creating a custom field with consolidated values of different fields and merging them to a completely new field. The best use case is creating addresses for custom doctypes easily without any custom scripting.


This is how the field configuration will look


![](/files/FXuN3dK.png)


Note: We are using options for adding values because it updates the field by changing its source fields. (Doest work with defaults)


Also, the field type should not be data. (Could be read-only or HTML)


Here's the output of the above configuration


![](/files/gHpmXZY.png)




