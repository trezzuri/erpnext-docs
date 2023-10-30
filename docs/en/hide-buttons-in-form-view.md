
# Hide Buttons in Form View



In a submitted Sales Order, you can see buttons like **Update Items**, **Status**. Also there are many options under 'Create' button.


![Custom Script](/files/sales_order_buttons.png)


You can write custom script as shown below to hide these buttons.



```
frappe.ui.form.on('Sales Order', {
    refresh(frm) {
    setTimeout(() =&gt; {
        frm.remove_custom_button('Update Items');
        frm.remove_custom_button('Close', 'Status');
        frm.remove_custom_button('Work Order', 'Make');
        }, 10);
    }
})

```



