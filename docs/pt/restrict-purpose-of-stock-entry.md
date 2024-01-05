# Restringir a finalidade da entrada de ações




```
frappe.ui.form.on("Solicitação de Material", "validate", function(frm) {
    if(frappe.user=="user1@example.com" && frm.doc.purpose!="Recebimento de material") {
        frappe.msgprint("Só é permitido recebimento de material");
        frappe.throw(__("Não permitido"));
    }
}

```


