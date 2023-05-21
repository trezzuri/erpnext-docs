# Restringir o usuário com base no registro filho



```
// restringe determinado armazém ao Gerente de Materiais
cur_frm.cscript.custom_validate = function(doc) {
    if(frappe.user_roles.indexOf("Gerenciador de Materiais")==-1) {

        var restrito_in_source = frappe.model.get_list("Detalhe de entrada de estoque",
            {parent:cur_frm.doc.name, s_warehouse:"Restricted"});

        var restrito_in_target = frappe.model.get_list("Detalhe de entrada de estoque",
            {parent:cur_frm.doc.name, t_warehouse:"Restricted"})

        if(restricted_in_source.length || restrito_in_target.length) {
            frappe.msgprint(__("Apenas o Gerente de Materiais pode fazer entrada no Armazém Restrito"));
            validado = falso;
        }
    }
}

```