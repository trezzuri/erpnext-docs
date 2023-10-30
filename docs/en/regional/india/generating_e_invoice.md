
# Generating e-Invoice



e-Invoice is an electronic invoice required to be generated on [e-Invoice Portal](https://einvoice1.gst.gov.in/) for all invoices except for supplies made to unregistered customers. In order to comply with the same, India Compliance offers easy, quick and reliable solution to generate e-Invoice.



> 
> APIs would be needed to use these features. This is required for businesses with good volume of transactions, and hence it is recommended to use with APIs.
> 
> 
> 


### e-Invoice Settings


Get started with **GST Settings** and configure e-Invoice settings according to your requirements.



> 
> You need to first enable API to access e-Invoice Settings
> 
> 
> 


* **Enable e-Invoicing**: Is e-Invoicing applicable to you? You can enable e-Invoicing features from here.
* **Automatically Generate e-Invoice on Invoice Submission**: e-Invoice will be automatically generated, if applicable, on submission of Sales Invoice.



> 
> e-Invoice is automatically generated for all invoices except for supplies to Unregistered Person or Non-GST Supplies.
> 
> 
>
* **e-Invoice Applicable From**: e-Invoices will only be generated for invoice generated after this date. You can pre-configure this if its going to be applicable at a later date.


![e-Invoice Settings](/files/e_invoice_settings.png)


### Generating e-Invoice


e-Invoice would be generated automatically on submission of Invoice if its applicable to you.


In case you would like to manually trigger the generation, you can do so after submission of Invoice. e-invoice menu options will come up. Once you click on Generate button, e-Invoice generation will be triggered.


![Generating e-Invoice](/files/generating_e_invoice.gif)


### Cancelling e-Invoice


You can cancel e-Invoice from the e-Invoice menu options if its within the validity period.


Click on e-Invoice menu --> Click Cancel button --> Give reasons for cancellation in the dialog --> and confirm to cancel the e-Invoice.


![Cancelling e-Invoice](/files/cancelling_e_invoice.gif)


### e-Invoice and e-Waybill both are applicable to us. How do these settings interact with each other?


We have a seamless integration for you where both are applicable to you. Following points shall help you understand the same in detail.


* If `Automatically Generate e-Invoice on Invoice Submission` setting is enabled by you, `Automatically Generate e-Waybill on Invoice Submission` will be a mandatory setting for you.
* While generating e-Invoice, e-Waybill shall be generated automatically if applicable and required fields (Transport Details) are present. In case, data is not available, and e-Waybill is not generated or only Part A of e-Waybill is generated, you shall be able to generate or update e-Waybill from e-Waybill menu items.
* For cancellation of e-Invoice, e-Waybill needs to be cancelled first. We have got you covered here to. While you cancel the e-Invoice, and if e-Waybill is available and valid, both e-Invoice and e-Waybill will be cancelled simultaneously.


### What if we generate e-Waybill before the e-Invoice?


e-Invoice has been designed to automate your GSTR-1 and e-Waybill process. You should first create e-Invoice and then generate e-Waybill only if its not generated along with e-Invoice.


### What should we do if the validity of e-Invoice has expired and still we would like to cancel it?


e-Invoice is a legal record. Cancelling your invoice (although e-Invoice is not cancellable) for updates or errors or returns is not a good practice in such cases.


You should adjust the difference with a credit or debit note over and above this invoice.




