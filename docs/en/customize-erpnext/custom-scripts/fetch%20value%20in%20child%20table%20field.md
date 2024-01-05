
# Fetch value in a child table field from Master



### Sample Script to fetch expiry\_date field from Batch doctype to Sales Invoice Item table


Step 1: Create Custom Script for ***Sales Invoice*** (parent) doctype


Step 2: Script as below & Save



```
frappe.ui.form.on("Sales Invoice Item", "batch_no", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        frappe.db.get_value("Batch", {"name": d.batch_no}, "expiry_date", function(value) {
            d.expiry_date = value.expiry_date;
        });
});

```



