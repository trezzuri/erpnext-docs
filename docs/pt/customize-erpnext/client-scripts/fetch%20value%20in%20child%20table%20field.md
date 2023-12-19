# Buscar valor em um campo de tabela filho do Master



### Amostra de script para buscar o campo expiry\_date do tipo de documento em lote para a tabela de itens da fatura de vendas


Etapa 1: criar um script personalizado para o tipo de documento ***fatura de vendas*** (pai)


Etapa 2: Script conforme abaixo e salve



```
frappe.ui.form.on("Item da fatura de vendas", "batch_no", function(frm, cdt, cdn) {
    var d = locais[cdt][cdn];
        frappe.db.get_value("Lote", {"nome": d.batch_no}, "data_de expiração", function(valor) {
            d.data_de_expiração = valor.data_de_expiração;
        });
});

```


