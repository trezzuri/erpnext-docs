# Restrinja a finalidade da entrada de estoque



```
frappe.ui.form.on("Pedido de Material", "validar", function(frm) {
    if(frappe.user=="user1@example.com" && frm.doc.purpose!="Recibo de Material") {
        frappe.msgprint("Só é permitido Recibo de Material");
        frappe.throw(__("Não permitido"));
    }
}

```