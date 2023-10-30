
# Zenoti Integration




> 
> Introduced in version 13.
> 
> 
> 


Zenoti Integration pulls the purchase orders and sales invoices from Zenoti and creates Purchase Order and Sales Invoice against them in ERPNext.


While creating these records if Customer, Supplier or Item is missing in ERPNext the system will create new Customer, Supplier or Item by pulling respective details from Zenoti.


### How to Setup?


Zenoti Integration is available through *Ecommerce Integrations* on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).


### App Installation


* If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).
* If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
* If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`


The repository for app is hosted on GitHub: <http://github.com/frappe/ecommerce_integrations/>.


### Prerequisite


1. For each center in Zenoti there should be a cost center and a warehouse created in ERPNext which will be used in Cost Center and Warehouse Mapping table in Zenoti Settings in ERPNext.
2. Items*(alteast those having stock impact)* have to be created. Data import can be used for this.
3. Opening stock entries have to be created using Stock Reconciliation in ERPNext.
4. Item Tax Templates have to be created from Tax Groups in Zenoti with proper accounts and tax rates.
5. Create an account to book liability for the sales of gift or prepaid cards and tips, this is to be set as *Liability Income Account to book Gift & Prepaid cards* in Zenoti Settings.
6. Set appropriate accounts in the mode of payments. Also add "Card", "Custom" and "Points" as Mode of Payment.
7. "Enable Perpetual Inventory" should be unchecked in Company Master.


### Important details for setting up Zenoti on ERPNext



> 
> To access Zenoti Settings, go to: Awesome search bar > Zenoti Settings.
> 
> 
> 


![Zenoti setting page](/files/Zenoti Settings Screen.png)


1. **Last Sync:** Date and time of when the invoices were synced last.
2. **API Key:** API Key from Zenoti. If you do not have an API Key, you can easily generate one by going to Admin > Setup > API section.
3. **Sync Interval:** Duration in hours between each syncing. Following options are avaliable *(1, 3, 6, 12, 24)*
4. **Default Purchase Warehouse:** Warehouse to be set for all the Purchase Orders. Usually this is the main center in Zenoti so put the one you created for main center.
5. **Default Buying Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Buying* provided by ERPNext.
6. **Default Selling Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Selling* provided by ERPNext.
7. **Liability Income Account to book Tips, Gift & Prepaid cards:** Add here the account you created to book Tips and sales of Gift & Prepaid cards.
8. **Default Customer Group:** If on creation of new customer while syncing sales invoice a specific customer group is to be assigned to them then add that here. If nothing is added then the default *All Customer Group* will be set for those new customer.
9. **Default Supplier Group:** If on creation of new supplier while syncing purchase order a specific supplier group is to be assigned to them then add that here. If nothing is added then the default *All Supplier Group* will be set for those new supplier.
10. **Cost Center and Warehouse Mapping:** In this table map all the Centers of Zenoti to their corresponding Cost Centers and Warehouses in ERPNext.


### What will be synced or will have to be created manually


#### Item


Items will have to be created manually into ERPNext from Zenoti one time at the start. Then it will be created on a demand basis when syncing sales /purchase orders.


#### Item Tax Template


Item Tax Template will be created manually based on Tax Groups on zenoti.


#### Customer


Customer and Customer Group will be created on demand basis while syncing sales invoices. If there are no customer groups in Zenoti, “Default Customer Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Customer Groups” will be used.


#### Supplier


Supplier and Supplier Group will be created on demand basis while syncing purchase orders. If there are no supplier groups in Zenoti, “Default Supplier Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Supplier Groups” will be used.


#### Warehouse


Warehouses will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.


#### Cost Center


Cost Centers will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.


#### Employees


Employees will have to be created manually into ERPNext from Zenoti one time at the start. Then it can be created on a demand basis when syncing sales/purchase records. For Employees fields "Date of Birth", "Date of Joining" are mandatory. Hence when creating employee from sales/purchase records "Date of Joining" will be set as the day the employee is created and "Date of Birth" as 25 years before "Date of Joining". These can be changed later on.


#### Purchase Order


Purchase Order will be created in Zenoti and sync into the ERPNext at the end of the day.
Supplier and Item will be created on demand basis if new.



> 
> Note: Purchase Invoice from the Purchase Order have to be created manually.
> 
> 
> 


#### Debit Note


Debit Note will be created automatically and remain in Draft mode based for Return Purchase Order in Zenoti.


#### Sales Invoice


Invoice will be created automatically via API on the given interval set in Zenoti Settings.
Customer and Item will be created on demand basis if new.


#### Credit Note


Credit Note will be created automatically based on Return Invoice in Zenoti and will only contain products and not services.


#### Gift/Prepaid Card Sales


Each Gift/Prepaid card will be treated as Items.
Gift/Prepaid Cards will be treated as mode of payment for future invoices where the payment was done using these in Zenoti.


#### Stock Reconciliation


At the end of the day, stock will be synced via Stock Reconciliation.




