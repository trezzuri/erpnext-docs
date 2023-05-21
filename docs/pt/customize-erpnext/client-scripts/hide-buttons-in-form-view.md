# Ocultar botões na exibição de formulário


Em um pedido de venda enviado, você pode ver botões como **Atualizar itens**, **Status**. Além disso, existem muitas opções no botão 'Criar'.


![Script personalizado](/files/sales_order_buttons.png)


Você pode escrever um script personalizado conforme mostrado abaixo para ocultar esses botões.



```
frappe.ui.form.on('Pedido de Venda', {
    atualizar(frm) {
    setTimeout(() => {
        frm.remove_custom_button('Atualizar itens');
        frm.remove_custom_button('Fechar', 'Status');
        frm.remove_custom_button('Ordem de Serviço', 'Fazer');
        }, 10);
    }
})

```