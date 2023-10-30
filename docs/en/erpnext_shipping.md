
# ERPNext Shipping



> Introduced in version 13


**The ERPNext Shipping app helps you compare shipping rates being offered by multiple service providers, generate labels, and track your shipments' status.**


Integration with the following service providers is available:


1. [Packlink](https://www.packlink.com/en-GB/)
2. [LetMeShip](https://www.letmeship.com/en/)
3. [SendCloud](https://www.sendcloud.com)


> To avail these features, the **ERPNext Shipping** app will have to be installed on your site. You can the avail the app [on GitHub](https://github.com/frappe/erpnext-shipping/tree/master), [on Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/shipping) or you can contact your hosting platform.


## 1. Setting Up


For the app to work smoothly, you will have to generate an API key from **at least one** of the platforms listed above. Here is a guide to set them up:


### 1.1 Packlink API


1. Register on [Packlink PRO](https://auth.packlink.com/en-GB/pro/register?platform=PRO&platform_country=UN).
2. Follow [these steps](https://support-pro.packlink.com/hc/en-gb/articles/213431749-How-to-generate-an-API-key-on-PRO) to generate an **API Key**.
3. Search for **Packlink** in the awesomebar.
4. Add the **API Key** to the Packlink DocType, check the 'Enabled' field.
5. Save.


![Packlink API](/files/packlink_api.png)


### 1.1 Sendcloud API


1. Register on [Sendcloud](https://panel.sendcloud.sc/accounts/signup/).
2. Follow [these steps](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) to generate a **Public Key** and a **Secret Key**.
3. Search for **SendCloud** in the awesomebar.
4. Add the **Public Key** in the 'API Key' field and the **Secret Key** in the 'API Secret' field of the SendCloud DocType.
5. Check the **Enabled** field.
6. Save.


![Sendcloud API](/files/sendcloud_api.png)


### 1.1 LetMeShip API


1. Register on [LetMeShip](https://www.letmeship.com/en/).
2. Follow [these steps](https://www.letmeship.com/en-de/shipping-api/) to generate an **API ID** and **API Password**.
3. Search for **LetMeShip** in the awesomebar.
4. Add the **API ID** and **API Password** to the LetMeShip DocType. Check the **Enabled** field.
5. Save.


![LetMeShip API](/files/letmeship_api.png)


## 2. Features


### 2.1 Comparison of Shipping Rates


Once a [Shipment](/docs/en/stock/shipment) is submitted, if the app is installed, the button **Fetch Shipping Rates** will appear. On clicking, you will get a list of services along with their service providers and rates.


![Fetch Rates](/files/fetch_rates.png)


You can also add frequently used services to your **Preferred Services** using **Parcel Service Type**:


1. Assuming the highlighted service is our frequently used service, let us add it to our **Preferred Services**


![Highlight Service](/files/service_highlight.png)
2. Go to **Parcel Service Type** > **New**. Create a new **Parcel Service**. In our case, it is 'TNT'.
3. Add a **Parcel Service Type**. In our case, it will be 'Economy'.
4. Add 'Economy' to the **Parcel Service Type Alias** table as well.
5. Add a description (optional).
6. Enable the **Show in Preferred Services List** field. Save.


Now when you click on the **Fetch Shipping Rates** button, you will always see the previously highlighted service under **Preferred Services**.


![Preferred Service](/files/preferred_service.png)


### 2.2 Creation of Shipment


After comparing rates, you can proceed with any one of the services by clicking **Select** against the appropriate service row. On clicking, a Shipment is automatically created on your service provider's platform.


You will notice that the **Shipment Information** section is updated automatically, based on the Shipment created.


![Shipment Creation](/files/create_shipment.gif)


You can also search for your transaction on your service provider's platform using the **Shipment ID** field.


![Packlink Shipment](/files/packlink_shipment.png)


### 2.3 Printing Labels


To avail the **Print Shipping Label** button, the **Shipment ID** must be generated in the current record.


![Print Label Button](/files/print_label_button.png)


You can then click on it and generate your shipping label.


![Dummy Shipping Label](/files/dummy_shipping_label.png)


You can also track your shipment's status by clicking on **View** > **Track Status**.


> **Note** : The currently integrated platforms may not serve your region. Please visit the links attached against them to know more.




