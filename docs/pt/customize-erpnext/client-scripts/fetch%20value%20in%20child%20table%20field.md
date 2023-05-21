# Busca valor em um campo da tabela filho do Master


### Script de amostra para buscar o campo expiração\_data do tipo de documento do lote para a tabela de itens da fatura de vendas


Etapa 1: criar um script personalizado para o tipo de documento ***Fatura de vendas*** (pai)


Etapa 2: script como abaixo e salve



```
frappe.ui.form.on("Item de Fatura de Vendas", "batch_no", function(frm, cdt, cdn) {
    var d = locais[cdt][cdn];
        frappe.db.get_value("Batch", {"name": d.batch_no}, "expiry_date", function(value) {
            d.expiry_date = valor.expiry_date;
        });
});

```