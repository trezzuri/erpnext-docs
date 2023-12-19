# Tornar somente leitura após salvar



Use o método `cur_frm.set_df_property` para atualizar a exibição do campo.


Neste script também utilizamos a propriedade `__islocal` do DocType para verificar se o
o documento foi salvo pelo menos uma vez ou nunca foi salvo. Se `__islocal` for `1`,
então o documento nunca foi salvo.



```
frappe.ui.form.on("MyDocType", "refresh", function(frm) {
   //use o método is_new do frm, para verificar se o documento está salvo ou não
    frm.set_df_property("meucampo", "somente leitura", frm.is_new() ? 0 : 1);
}

```


