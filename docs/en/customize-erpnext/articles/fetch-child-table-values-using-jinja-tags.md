
# Fetch child table values using Jinja tags



Jinja templating can be used to reference any field on any DocType in ERPNext. This can simply be done by calling &lcub;&lcub;doc.field\_name}} on a print format, where 'doc.name' is the variable name for a certain field.


However this approach does not work for Child Tables inside a DocType. This article will help you traverse and display all rows pertaining to a child table inside any DocType.


**Pre Requisites**


We would require the variable name of the child table on the corresponding DocType. This can be viewed from the 'Customize Form' section for the required DocType. The same is illustrated below


![](/files/f7Xxz1S.png)


We will also require the variable names of all the fields inside the child table which need to be referenced. This can be obtained from the 'Customize Form' section of the corresponding child table as shown below


![](/files/tzloEh2.png)


![](/files/wPB82f0.png)


![](/files/AV0308f.png)


![](/files/CW0oEUo.png)


**Method 1. Displaying rows of a Child Table on an unordered list**




{% for row in doc.items %}

* Item Code: &lcub;&lcub; row.get\\_formatted("item\\_code", doc) }}

Quantity: &lcub;&lcub; row.get\\_formatted("qty", doc) }}

Rate: &lcub;&lcub; row.get\\_formatted("rate", doc) }}

Amount: &lcub;&lcub; row.get\\_formatted("amount", doc) }}


{% endfor %}



The output on a print format would be as follows


![](/files/lgLjE7u.png)


**Method 2. Displaying rows of a Child Table as a table**


  


   


  


  


 


 

| Item Code | Quantity | Rate | Amount |
| --- | --- | --- | --- |
| &lcub;&lcub;item.item\_code }} | &lcub;&lcub;item.qty}} | &lcub;&lcub;item.rate}} | &lcub;&lcub;item.amount}} |




The output on a print format would be as follows


![](/files/GS00WlC.png)


This template can be used for reference. Any additional fields on the child table field can be fetched in a similar manner, by amending the Jinja template.




