# Buscar valor em um campo de tabela filho do Mestre


### Amostra de script para buscar o campo expiry\_date do lote de doctype para a tabela de itens da fatura de vendas


Etapa 1: Criar script personalizado para ***Fatura de vendas*** (pai) doctype


Etapa 2: Script conforme abaixo e Salvar



```
frappe.ui.form.on("Item da Fatura de Vendas", "batch_no", function(frm, cdt, cdn) {
    var d = locais[cdt][cdn];
        frappe.db.get_value("Batch", {"name": d.batch_no}, "expiry_date", function(value) {
            d.expiry_date = valor.expiry_date;
        });
});

```
