# Restringir o usuário com base no registro filho


// restringe determinado armazém ao Gerente de Materiais
cur\_frm.cscript.custom\_validate = function(doc) {
 if(frappe.user\_roles.indexOf("Gerenciador de Materiais")==-1) {

 var restrito\_in\_source = frappe.model.get\_list("Detalhe de entrada de estoque",
 {parent:cur\_frm.doc.name, s\_warehouse:"Restricted"});

 var restrito\_in\_target = frappe.model.get\_list("Detalhe de entrada de estoque",
 {parent:cur\_frm.doc.name, t\_warehouse:"Restricted"})

 if(restricted\_in\_source.length || restrito\_in\_target.length) {
 frappe.msgprint(\_\_("Apenas o Gerente de Materiais pode fazer entrada no Armazém Restrito"));
 validado = falso;
 }
 }
}
