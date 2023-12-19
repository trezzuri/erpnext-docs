
# Shopify Integration



The Shopify Connector pulls the orders from Shopify and creates Sales Order against them in ERPNext.


While creating the sales order if Customer or Item is missing in ERPNext the system will create new Customer/Item by pulling respective details from Shopify.


### How to Setup Connector?


Shopify Connector is moved out from ERPNext and available through a Frappe App on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)


#### Note to users of old Shopify Connector


If you have not setup Shopify Connector on your ERPNext site you can proceed to next step.


If you are using old Shopify integration that's provided in ERPNext then you will have to disable the connector before proceeding. After installing the app, it will migrate existing data e.g. unique product\_id for items to separate doctype. Once you are done configuring new integration, you can confirm the status of migration by going to "Ecommerce Integration Log" doctype.


#### App Installation


* If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
* If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
* If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`


The repository for app is hosted on GitHub: <http://github.com/frappe/ecommerce_integrations/>


#### Create A Custom App in Shopify


1. Click on Apps in menu bar
![Menu Section](/files/app_menu.png)
2. Click on **Develop apps for your store** to create custom app
![new app](/files/Screenshot 2022-02-16 at 11.36.57 AM.png)
3. Create New app
![](/files/new_app.png)
4. Fill up the details and create app. The each app has its own API key, Password and Shared secret
![](/files/configure_admin_scope.png)
5. Allow following permissions to the app.


	* Draft Orders - Read and Write
	* Orders - Read and Write
	* Location - Read
	* Customers - Read
	* Assigned fulfillment orders - Read and Write
	* Products - Read and Write
	* Product listings - Read and Write
	* Inventory - Read and Writeyour final admin scopes should look like this:


![](/files/final_admin_scopes.png)
6. Install the app on your site
![](/files/install.png)


#### Setting Up Shopify on ERPNext:-


Once you have created a Private App on Shopify, setup App Credentials and other details in Shopify Settings in ERPNext.


> To access Shopify Settings, go to:
Awesome search bar > Shopify Setting


1. Fill-up Shopify site URL, Access Token and API Secret from Shopify's Private App.
![](/files/tokens.png)
![](/files/Screenshot 2022-02-16 at 11.57.34 AM.png)
2. Setup Customer, Company and Inventory configurations.
3. ![Shopify setting page](/files/main-settings.png)
4. Setup Sync Configurations.
The system pulls Orders from Shopify and creates Sales Order in ERPNext. You can configure ERPNext system to capture payment and fulfilments against orders.
![Shopify sync config for orders](/files/series-setting.png)
5. Setup Tax Mapper.
Prepare tax and shipping charges mapper for each tax and shipping charge you apply in Shopify. You can find name of your taxes from your Shopify Admin page.
![Shopify tax mapping](/files/tax-mapping.png)
![Finding Shopify Tax names](/files/Screenshot 2021-08-25 at 11.02.20 AM.png)


After setting up all the configurations, enable the Shopify sync and save the settings. This will register the API's to Shopify and the system will start Order sync between Shopify and ERPNext.


### Syncing Old Orders From Shopify


Once you are done with the Shopify configuration and have enabled Shopify Syncing, you also get a provision to sync your old orders from Shopify into ERPNext. This syncing will happen in background and can take few hours depending on number of orders you have.


1. Enable "Sync Old Shopify Orders"
2. Enter the From and To dates between which the orders need to be synced
![shopify sync old orders](/files/sync-old-orders.png)


### Inventory Sync


You can update your inventory with Shopify for items that are synced from Shopify. Inventory sync is done every hour with a scheduled job. Inventory levels of items that have changed since last sync are pushed to Shopify. Inventory levels of ERPNext warehouses are mapped 1 to 1 with Shopify locations.


1. To enable inventory sync click on the checkbox, this will show you a table to map ERPNext warehouse with Shopify Location.
2. Select sync frequency. 30 to 60 minutes is recommended frequency.
3. Click on "Fetch Shopify Locations" button to populate Shopify locations in the table.
4. Link each location with ERPNext warehouse.
5. Save the settings.


![Inventory sync with shopify](/files/inventory-sync.png)


> Note: This connector assumes that ERPNext is main source of information about inventory levels, any changes done to Shopify inventory levels will be overwritten by ERPNext if ERPNext inventory levels change.


> Note: Shopify does not support fractional quantity. If fractional quantity is found in ERPNext, the inventory level on Shopify will be set by rounding it down to nearest whole number.


### Item Sync


You can enable sync of new ERPNext items to Shopify by checking "Upload new ERPNext items to Shopify".


You can also update Shopify item upon updating ERPNext item.


Following fields are uploaded / updated:




| ERPNext Field | Shopify Field |
| --- | --- |
| Item Name | Title |
| Item Code | SKU |
| Description body | Description |
| Item Group | Product Type |
| Weight per Unit | Weight |
| Weight UOM | Weight UOM |


By default all items are marked as Draft on Shopify and not published in any store.


Purpose of providing this functionality is to sync items with Shopify. It's not possible to map every fields 1-to-1. Upon creation of item on Shopify using this method, it's linked with ERPNext, this eliminates possibility of duplication. You can modify items on Shopify later to add more details.


> Note: This feature is not supported in data import or for variant / template items.


### Cancellation of Orders


This connector handles various cancellation scenario in following manner:


1. If Order on Shopify is cancelled and it doesn't have invoice or Delivery note linked against it then ERPNext Sales Order is cancelled.
2. If ERPNext Sales Order does have any linked document, then status of order on Shopify is added to the respective document. Cancellation and preparation of appropriate documents has to be done by user based on this information.




