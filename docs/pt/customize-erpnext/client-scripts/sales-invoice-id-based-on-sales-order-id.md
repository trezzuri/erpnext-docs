# ID da fatura de vendas com base no ID do pedido de vendas



O script abaixo permite que você aplique séries de nomenclatura a uma fatura de venda, igual à do pedido de venda correspondente.
A fatura de vendas usa um prefixo M-, mas o número se duplica a partir do nome do pedido de vendas.


Exemplo: se o ID do pedido de vendas for SO-12345, o ID da fatura de vendas correspondente será definido como M-12345.



```
frappe.ui.form.on("Fatura de Vendas", "refresh", function(frm){
    var pedido_venda = frm.doc.items[0].pedido_venda.replace("M", "M-");
    if (!frm.is_new() && pedido_venda && frm.doc.name!==pedido_venda){
        frappe.call({
        método: 'frappe.model.rename_doc.rename_doc',
        argumentos: {
            tipo de documento: frm.doctype,
            antigo: frm.docname,
            "novo": pedido_venda,
            "mesclar": falso
        },
    });
    }
});

```


