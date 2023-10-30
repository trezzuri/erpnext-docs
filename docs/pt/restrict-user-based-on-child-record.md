# Restringir usuário com base no registro infantil




```
//restringe determinado armazém ao Material Manager
cur_frm.cscript.custom_validate=função(doc){
    if(frappe.user_roles.indexOf("Gerenciador de Materiais")==-1) {

        var restrito_in_source = frappe.model.get_list("Detalhe de entrada de estoque",
            {parent:cur_frm.doc.name, s_warehouse:"Restrito"});

        var restrito_in_target = frappe.model.get_list("Detalhe de entrada de estoque",
            {pai:cur_frm.doc.name, t_warehouse:"Restrito"})

        if(restricted_in_source.length || restrito_in_target.length) {
            frappe.msgprint(__("Somente o Gerente de Materiais pode efetuar entrada no Armazém Restrito"));
            validado = falso;
        }
    }
}

```


