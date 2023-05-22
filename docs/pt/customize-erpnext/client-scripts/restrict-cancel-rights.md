# Restringir direitos de cancelamento


Adicione um manipulador ao evento `custom_before_cancel`:



```
cur_frm.cscript.custom_before_cancel = function(doc) {
    if (frappe.user_roles.indexOf("Usuário de Contas")!=-1 && frappe.user_roles.indexOf("Gerente de Contas")==-1
            && user_roles.indexOf("Gerenciador do Sistema")==-1) {
        if (flt(doc.grand_total) > 10000) {
            frappe.msgprint("Você não pode cancelar esta transação porque o total geral \
                é maior que 10000");
            frappe.validated = false;
        }
    }
}

```
