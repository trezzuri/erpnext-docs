
# Item Variants



**An Item Variant is a version of an Item with different attributes like sizes or colors.**


Eg: Suppose t-shirt is an Item and it comes in different sizes and colors like small, medium, large and red, blue, green. In ERPNext the t-shirt will be considered as an Item template and each of the variations will be an Item Variant.


A *blue* t-shirt in size *small* rather than just a t-shirt. Item variants let you treat the *small*, *medium*, and *large* versions of a t-shirt as variations of one Item 't-shirt'.


Without Item variants, you would have to treat the *small*, *medium* and *large* versions of a t-shirt as three separate Items.


## 1. Using Item Variants


Variants can be based on two things:


1. Item Attributes
2. Manufacturers


> Tip: Once an item template is created, when you update this template, all the variants are also updated accordingly.


### 1.1 Creating the Item Variant Template


1. To use Item Variants in ERPNext, create an Item and tick 'Has Variants' under Variants.
2. The Item then shall be referred to as a so-called 'Template'. Such a Template is not identical to a regular 'Item' any longer. For example, it (the Template) cannot be used directly in any transaction (Sales Order, Delivery Note, Purchase Invoice) itself.
3. Only the Variants of the Item (*blue* t-shirt in size *small)* can be practically used. Therefore it would be ideal to decide whether an item 'Has Variants' or not directly when creating it.
![Has Variants](/files/item-has-variants.png)
4. On selecting 'Has Variants' a table will appear. Specify the variant attributes for the Item in the table. In case the attribute has Numeric Values, you can specify the range and create intervals based on the increment values.
![Valid Attributes](/files/item-attributes.png)
> Note: You cannot make Transactions against a 'Template'.


### 1.2 Creating the Item Variants Based on Item Attributes


To create 'Item Variants' against a 'Template' click on 'Create'. From there, choose whether to create a single variant or multiple. Single is simple where you create just one or more attributes and one Item will be created. When choosing multiple variants, tick the attributes and multiple items will be created. For example, if you choose Color: Red, Green and Size: Small, Medium, Large, 6 variants will be created.


Creating multiple variants in ERPNext:


![Make Variants](/files/make-multiple-variants.png)


To learn more about setting attributes check out [Item Attributes](/docs/en/stock/item-attribute)


### 1.3 Item Variants Based on Manufacturers


To setup variants based on Manufacturers, in your Item template, set "Variants Based On" as "Manufacturers"
In this case, to create variants, click on Create > Make Variant. The system will prompt you to select a Manufacturer. You can also optionally put in a Manufacturer Part Number.


![Setup Item Variant by Manufacturer](/files/select-mfg-for-variant.png)


The naming of the variant will be based on the name (ID) of the template Item with a number suffix. e.g. "Screwdriver" will have variant "Screwdriver-1".


## 2. Update Item Variants Based on Template


Go to: **Home > Stock > Items and Pricing > Item Variant Settings**. The fields displayed here will be copied over to the variants as well. By default, all fields are shown, delete any rows you don't want to be updated from the item template to the variants.


## 3. Video


### 3.1 Creating Item Variant one by one






### 3.2 Creating Item Variants in bulk






### 4. Related Topics


1. [Item Group](/docs/en/stock/item-group)
2. [Item Attribute](/docs/en/stock/item-attribute)
3. [Item Price](/docs/en/stock/item-price)
4. [Item Codification](/docs/en/stock/articles/item-codification)




