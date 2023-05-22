# Renomear botões na exibição de formulário


Em um pedido de venda enviado, você pode ver várias opções na opção 'Criar':


![Script personalizado](/files/customize-button-all.png)


Você pode usar este script personalizado para renomear os botões:



```
frappe.ui.form.on('Pedido de Venda', {
    on_submit: function(frm){
    // console.log('reloaded doc on submit')
        localização.recarregar()
    },
    onload_post_render: function(frm){
        var bt = ['Entrega', 'Ordem de Trabalho', 'Fatura', 'Solicitação de Material', 'Solicitação de Matéria-Prima', 'Ordem de Compra', 'Solicitação de Pagamento', 'Pagamento', 'Projeto', 'Assinatura' ]
        bt.forEach(função(bt){
            frm.page.remove_inner_button(bt, 'Criar')
            });
        frm.page.add_inner_button('Order Raw Materials', () => cur_frm.cscript.make_raw_material_request(), 'Create')
        }
    }
);

```

Usando este script, removemos/ocultamos os botões indesejados e renomeamos um deles:


![Script personalizado](/files/customize-button-rename.png)


**Observação:** para saber mais sobre as APIs JS, visite a [documentação do frappe](https://frappe.io/docs/v13/user/en/api/form) .


Para verificar o método que é chamado, você precisará verificar o arquivo JS para esse doctype. Neste exemplo, para renomear 'Request For Raw Materials', estamos nos referindo a [esta linha](https://github.com/frappe/erpnext/blob/782f45ae5f272173b5daadb493d40cf7ccf131b4/erpnext/selling/doctype/sales_order/sales_order.js# L167).

