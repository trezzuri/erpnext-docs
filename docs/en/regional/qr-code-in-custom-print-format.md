
# QR Code in custom print format



Once you upgrade from version-13 to version-14 e-Invoice QR codes in your custom print format won't work anymore. This guide will help you to add QR code in custom print formats.


### Step 1: Make a web template for QR Code


First you'll have to create a Web Template for the QR Code, to go to web template list search for Web Template in awesome bar and create a new Web Template. Give it a name something like "E-Invoice QR Code", type as "Component" and module as "Printing".


![web template naming](/private/files/web-template-naming.png)


After this copy paste the below mentioned code snippet in the template field



```
<img class="qrcode"/>

```

Once you add the template the last step is to add the fields, add label, fieldname and fieldtype as shown in the image below and save the web template


![web template fields](/private/files/web-template-fields.png)


### Step 2: Add web template to custom print format


Go to the custom print format where you wish to add the QR Code, replace the current QR Code image field with a custom HTML section and in that Custom HTML section past the code snippet mentioned below



```
{% if doc.irn %}
{% set e_invoice_log = frappe.db.get_value(
    "e-Invoice Log", doc.irn, ("invoice_data", "signed_qr_code"), as_dict=True
) %}

{%- set invoice_data = dict(json.loads(e_invoice_log.invoice_data)) -%}

<h5 class="section-heading"><b>Transaction Details</b></h5>
<div class="row section-break info-section">
<div class="col-xs-8 column-break">
    {%
        set transaction_details = {
            "IRN": invoice_data.Irn,
            "Ack. No": invoice_data.AckNo,
            "Ack. Date": frappe.utils.format_datetime(
                invoice_data.AckDt, "dd/MM/yyyy hh:mm:ss"
            ),
            "Category": invoice_data.TranDtls.SupTyp,
            "Document Type": invoice_data.DocDtls.Typ,
            "Document No": invoice_data.DocDtls.No,
        }
    %}
    {% for key, value in transaction_details.items() %}
        <div class="row data-field">
<div class="col-xs-4"><label>&lcub;&lcub; key }}</label></div>
<div class="col-xs-8 value">&lcub;&lcub; value }}</div>
</div>
    {% endfor %}
</div>
<div class="col-xs-4 column-break text-right">
    &lcub;&lcub; web_block('E-Invoice QR Code', values={'qr_text': e_invoice_log.signed_qr_code }) }}
</div>
</div>
<hr/>
{% endif %}

```

![print format](/private/files/print-format.png)


Note: Make sure the name mentioned in web\_block exactly matches the name of your Web Template which is "E-Invoice QR Code" here




