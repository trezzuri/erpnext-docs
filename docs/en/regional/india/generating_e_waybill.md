
# Generating e-Waybill



e-Waybill is an electronic waybill required to be generated on [e-Waybill Portal](https://ewaybillgst.gov.in/) for the movement of goods. India Compliance offers multiple ways to manage your e-Waybill compliance.


### e-Waybill Settings


Get started with **GST Settings** and configure e-Waybill settings according to your requirements.


* **Enable e-Waybill Features**: Is e-Waybill applicable to your business? Are you a GST Registered business involved in the movement of goods? You should enable the e-Waybill features from here.
* **Enable e-Waybill Generation from Delivery Note**: Do you want to generate an e-Waybill from the delivery note? Do you transfer goods for Job Work or to your different warehouse? You should enable e-Waybill generation from Delivery Note if you use these features.



> 
> You should ideally generate an e-Waybill from the sales invoice. e-Waybill generation from delivery notes should be restricted only to the movement of goods without an Invoice (Say, for Job Work or Transfer of goods to different warehouses)
> 
> 
>
* **Invoice Value Threshold for e-Waybill Generation**: It's set to 50,000 by default, but you can change it as per applicable laws or ensure tighter internal controls. Applicability of e-Waybill for Sales Invoice is checked based on this setting.


Following are the additional API-specific settings:


* **Automatically Generate e-Waybill on Invoice Submission**: e-Waybill generation will be attempted if all required fields are present and e-Waybill is applicable.



> 
> e-Waybill applicability is checked based on the threshold limit set above. Also, at least one item with HSN of **goods** must be present.
> 
> 
>
* **Fetch e-Waybill Data After Generation**: On the generation of e-Waybill, complete data of e-Waybill (as per NIC Portal) is not available. However, this may be necessary to generate the e-Waybill Print Format as per the e-Waybill Portal. Additional API request is required to fetch the e-Waybill data. If enabled, it shall be updated in your logs.
* **Attach e-Waybill Print After Generation**: e-Waybill print will be attached to the invoice automatically on the generation of the e-Waybill (after fetching the data). It can be used for emails or records.


![e-Waybill Settings](/files/e_waybill_settings.png)


### How to Generate an e-Waybill?


You can generate the e-Waybill using the bulk generation facility or the APIs.


Steps to generate the e-Waybill using the bulk generation facility:


* Submit the relevant document (say Sales Invoice).
* If e-Waybill is applicable for the current document, you shall see the e-Waybill menu --> Select Generate.
* Generate e-Waybill dialog box shall appear.
* Update the transport fields and Download JSON.
* Login to your e-Waybill Account --> Select Generate Bulk e-Waybill --> Choose the JSON file and upload it --> Click Generate.
* e-Waybill shall be generated --> Update the e-Waybill number in your Sales Invoice / Delivery Note.


![Generate e-Waybill from JSON](/files/generate_e_waybill_from_json.gif)


Steps to generate e-Waybill JSON for more than one document (Only for Sales Invoices)


* Select the Invoices from the Sales Invoice List for which you want to generate an e-Waybill JSON.
* Click Actions --> download e-Waybill JSON.
* Upload to e-Waybill portal and generate e-Waybill.
>You shall not be able to update transport fields while you download e-Waybill JSON from the Sales Invoice List


Generating e-Waybill using the APIs


* On submitting the sales invoice, e-Waybill shall be automatically generated (if enabled in settings).
* You can manually trigger the generation of e-Waybill for Delivery Note or where all fields were not present (on submit). Go to the e-Waybill menu --> Generate dialog --> Update fields and click generate.


![Generating e-Waybill on Submit](/files/generating_e_waybill.gif)


### How would I know if only Part A of the e-Waybill will be generated?


Dialog for Generate e-Waybill fields have separate sections for Part A and Part B. Also, the Primary Action button will denote if only Part A can be generated.


### How to auto calculate the distance for e-Waybill?


If the distance is set to zero (0), e-Waybill Portal will suggest the distance between postal codes. We shall update it to your document where e-Waybill is generated using the APIs.



> 
> In some exceptional circumstances, where the distance between postal codes is unavailable with the e-Waybill database, you shall receive a prompt. Generate e-Waybill again after entering the distance as per your estimate.
> 
> 
> 


### Additional API Specific Features


Updating or cancelling e-Waybill is possible only within the validity period. These options will be visible only if you have generated the e-Waybill using API and the validity to do so is not expired.


* **Update Transporter Details**: Use this feature to update the GSTIN of the transporter to your e-Waybill. From e-Waybill menu --> Select Update Transporter --> Update appropriate information and click update.


![Update Transporter](/files/update_transporter.gif)


* **Update Vehicle Information**: Use this feature to update the vehicle information (say, vehicle number) to your e-Waybill. From e-Waybill menu --> Select Update Vehicle Info --> Update information in dialog and click update.



> 
> There is a checkbox in the dialogs above for `Update e-Waybill Print/Data`. If you check this, we shall update the attachments of e-Waybill or Data concerning e-Waybill as per your preference from GST settings for e-Waybill. If `Attach e-Waybill Print After Generation` is enabled from GST Settings, new attachments will replace old attachments.
> 
> 
>


![Update Vehicle Info](/files/update_vehicle_info.gif)


* **Print e-Waybill**: You can use this to print an e-Waybill if you prefer not to have attachments. It works similar to printing any other document in ERPNext. It will redirect you to the respective e-Waybill log print and fetch the latest e-Waybill data (from NIC Portal) for printing if it's not available.
* **Attach e-Waybill**: It is a manual trigger to attach an e-Waybill to a Sales Invoice. A new attachment will replace the old attachment if present.
* **Cancel e-Waybill**: If within validity, you shall be allowed to cancel the e-Waybill, from the e-Waybill menu. Specify the reason for cancelling in the dialog and click cancel to cancel the e-Waybill.



> 
> While you cancel the e-Waybill, the attachment of the old e-Waybill, shall be removed.
> 
> 
>


![Cancel e-Waybill](/files/cancel_e_waybill.gif)


* **e-Waybill Logs**: In this DocType, e-Waybill history is maintained. It is created after you generate an e-Waybill using the APIs. Any further updates to e-Waybill are added here as a comment.




