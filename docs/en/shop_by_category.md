
# Shop by Category



ERPNext offers a **Shop by Category** (`/shop-by-category`) page out of the box, where users can navigate to relevant products based on their needs without having to use filters right away.


To set up the categories (in the tabs) for this page, head over to:



> 
> E Commerce Settings > Filters and Categories
> 
> 
> 


In the **Filters and Categories** section, make sure **Enable Field Filters (Categories)** is enabled. The categories are pulled from the Website Item Fields table. The field filters such as Item Group, Brand, etc. are reused as categories on this page.


Once this is done, you will accordingly see tabs on the **Shop by Category** page (`/shop-by-category`).
![Shop by Category](/files/shop-by-category.png)


Additionally you can add a slideshow to this page (as seen above) via the **Shop By Category** section in **E Commerce Settings**.


### Fetching records in categories


#### Item Groups


Item Groups are handled a little differently due to its tree structure. Item Group records are fetched if the following conditions are all satisfied:


* The **Show in Website** field is enabled in the Item Group
* Item Group is the **top most group node** (**Is Group** enabled and parent is 'All Item Groups') or **top-most leaf node** (**Is Group** disabled and parent is 'All Item Groups')


Each card links to the respective Item Group page.


#### Other Categories


The other categories' records are simply fetched irrespective. If you want to hide certain records here too (e.g. in **Brand**), you can add a custom **Show in Website** field and it will filter out those records that have this field disabled.



> 
> Custom doctypes **that are linked to Website Item via a link field** can also be included here along with Item Group, Brand, etc.
> 
> 
> 




