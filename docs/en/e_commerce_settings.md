
# E Commerce Settings



The legacy **Shopping Cart Settings** and **Products Settings** are now consolidated into a single **E Commerce Settings** page.


To configure **E Commerce Settings**, search for:



> 
> **E Commerce Settings** in the awesomebar (search bar)
> 
> 
> 


![E Commerce Settings](/files/e_commerce_settings_overview.png)
*E Commerce Settings*


### Products Per Page


Define how many products to show per page on the Product Listing in the **All Products** page (`/all-products`).


### Filters and Categories


![Filters and Categories](/files/filters_and_categories.png)
*Filters and Categories*


You can also add filters to your listing. There are two types of filters:


1. **Field Filters**: Enable the **Field Filters** checkbox and add the fields based
on which you want to have filters. These fields will also be used as categories for the **Shop by Category** page.
2. **Attribute Filters**: Enable the **Attribute Filters** checkbox and add the
attributes based on which you want to have filters.


### Display Settings


1. **Hide Variants**: Only show Website Item Templates on the Product Listing.
2. **Enable Variant Selection**: Show a configure button if the Item has variants. It can be used to narrow down the specific item based on Attributes.
3. **Show Price**: Show Item Price on the product page.
4. **Show Stock Availability**: Show whether the Item is in stock.
5. **Show Stock Quantity**: Show available stock on the product page.
6. **Allow items not in stock to be added to cart**: Allow items not in stock to be added to Cart.
7. **Show Apply Coupon Code**: Additional provision to apply coupon code at checkout.
8. **Show Contact Us Button**: Show a contact us button which customers can use to enquire about the Item. It will create a Lead in the system.
9. **Show Public Attachments**: Show public attachments in the Sales Order generated, after checkout, for Customers.



> 
> You can **Hide Variants** only when Attribute Filters are disabled.
> 
> 
> 


### Shopping Cart


1. **Company**: Specify the company that the web shop is set up for.
2. **Price List**: Mention Price List to consider while fetching Item Prices.
3. **Enable Shopping Cart**: Add the provision to add items to Cart.
4. **Default Customer Group**: Add the Default Customer Group to be set while auto creating customers on adding to Cart.


### Checkout Settings


1. **Enable Checkout**: If checkout is disabled, when your customers add an item to Cart, they can click
on the **Request for Quotation** button to get a quote for it. A [Quotation](/docs/en/selling/quotation)
is generated in the system. If enabled, a [Sales Order](/docs/en/selling/sales-order) is generated on clicking on the **Place Order** button in the Cart.
2. **Payment Gateway Account**: If checkout is enabled, you must have [PayPal Integration](/docs/en/erpnext_integration/paypal-integration)
or [Razorpay Integration](/docs/en/erpnext_integration/razorpay-integration).
3. **Payment Success Url**: After payment completion redirect users to the selected option.
4. **Show Price in Quotation**: If checkout is disabled, you can choose whether or not to show prices against Website Items in the Quotation.
5. **Save Quotations as Draft**: If checkout is disabled, on clicking on the **Request for Quotation** button, you can choose whether the auto-generated Quotation must be auto-submitted or kept in the Draft state.


### Add-ons


1. **Enable Wishlist**: Add the provision to add items to a Wishlist
2. **Enable Reviews and Ratings**: Add the privision for **customers** to leave reviews and ratings against Website Items.
3. **Enable Recommendations**: Add the provision to show manually selected **recommended items** against a Website Item.


### Shop By Category


The **Shop By Category** page is an out-of-the-box page that lists categories linked to Website Items. These categories can be configured in the **Filters and Categories** section's **Field Filters** table.


You can also select a slideshow as the banner of the page.


### Guest Display Settings


1. **Hide Price for Guest**: You can show or hide prices against Website Items for guest users (users who are not logged in).
2. **Redirect on Action**: If a guest user tries to add a Website Item to Cart or to the Wishlist, you can select a URL to redirect them to. By default, guest users are redirected to the `/login` page. You can instead redirect them to a custom Web Form of choice by adding a URL here e.g. `/contact-us`




