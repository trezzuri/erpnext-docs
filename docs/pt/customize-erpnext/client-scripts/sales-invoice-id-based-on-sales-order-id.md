# ID da fatura de vendas com base no ID do pedido de vendas


O script fornecido abaixo permite aplicar séries de nomenclatura a uma Fatura de Venda, igual à da Ordem de Venda correspondente.
A fatura de venda usa um prefixo M-, mas o número se duplica a partir do nome do pedido de venda.


Exemplo: se o ID do pedido de vendas for SO-12345, o ID da fatura de vendas correspondente será definido como M-12345.



```
frappe.ui.form.on("Fatura de venda", "refresh", function(frm){
    var pedido_de_venda = frm.doc.items[0].pedido_de_venda.replace("M", "M-");
    if (!frm.is_new() && sales_order && frm.doc.name!==sales_order){
        frappe.call({
        método: 'frappe.model.rename_doc.rename_doc',
        argumentos: {
            doctype: frm.doctype,
            antigo: frm.docname,
            "novo": pedido_de_venda,
            "unir": falso
        },
    });
    }
});

```
