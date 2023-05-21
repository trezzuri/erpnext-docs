# Validação de Data



```
    frappe.ui.form.on("Tarefa", "validar", function(frm) {
        if (frm.doc.from_date < get_today()) {
            frappe.msgprint(__("Você não pode selecionar data passada em From Date"));
            frappe.validated = false;
        }
    });

```