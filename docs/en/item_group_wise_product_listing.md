
# Item Group-wise Product Listing



Similar to the [Product Listing](/docs/en/e_commerce/product-listing) at `/all-products`, ERPNext offers Product Listings that are Item Group-wise as well. You can link these pages on your landing page to direct users easily.


### Setting Up an Item Group Page


To provide a Product Listing page for an Item Group (e.g. Products), go to:



> 
> Item Group List > Products
> 
> 
> 


* Enable **Show in Website**.
* Scroll down to the **Website Filters** section and add field and attribute filters similar to E Commerce Settings.
* You can also add a description in the RichText Editor that will show above the product list as a banner.


Now if you click on the **See on Website** link, on the top left, above the image in the current document, you will be redirected to the **Products** Item Group's listing page.


#### Product Visibility


Consider the Item Group **Products** has child Item Groups **Mobile Services** and **Mobiles**. 


Website Items that will be visible on the **Products** page are:


* Those having **Products** as their Item Group
* Those having **Products** in their **Website Item Groups** table.


Website Items having their Item Groups as **Mobile Services** or **Mobiles** will be visible on their respective pages. These pages will be linked in the **Products** page.



> 
> Child Item Groups such as **Mobile Services** and **Mobiles** will be visible as pills above the search bar on the **Producst** page.
> 
> 
> 


![Item Group-wise Product Listing](/files/item-group-page.png)




