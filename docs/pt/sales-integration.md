# Integração do ciclo de vendas



Métodos e fluxos permitidos padrão para integração de sistema de gerenciamento de pedidos externos e ciclo de vendas usando API REST


### 1. Pedido de venda


O Frappe Framework gera [API REST](https://frappeframework.com/docs/v14/user/en/api/rest) para todos os DocTypes prontos para uso. Esta abordagem pode ser usada para criar o primeiro documento do ciclo de vendas. Caso você esteja iniciando com o Pedido de Venda você pode utilizar a solicitação POST da API REST padrão para gerar o Pedido. Um exemplo é mostrado abaixo, você pode incluir campos personalizados e outros detalhes de tipo de documento no corpo de acordo.



```
POST/api/resource/Pedido de vendas

# Corpo
{
    "doctype": "Pedido de Venda",
    "cliente": "Cliente de teste",
    "company_address": "Teste-Faturamento",
    "customer_address": "Test-Billing-3",
    "Unid": [{
        "item_code": "Exibição para celular",
        "quantidade": 10,
        "taxa": 2000,
        "data_entrega": "06/11/2022",
        "delivery_warehouse": "Lojas-GTPL"
    }]
}

```

### 2. Nota de entrega


Caso você esteja começando com uma Nota de Entrega, use o mesmo método mostrado acima para Pedido de Venda, apenas substitua o valor da chave doctype por **Nota de Entrega** em vez de **Pedido de Venda** . Caso queira fazer uma Nota de Entrega de um Pedido de Venda utilize o endpoint abaixo. O parâmetro `source_name` aqui é o ID do pedido de vendas.



```
POST/api/method/erpnext.selling.doctype.sales_order.sales_order.make_delivery_note

# Corpo
{"nome_fonte": "SO-2022-00001"}

```

O endpoint retorna um objeto JSON de nota de entrega como resposta com todos os itens pendentes no pedido a ser entregue.


### 3. Fatura de vendas


Novamente, se você estiver apenas fazendo uma fatura de vendas, a melhor abordagem será usar a API REST padrão. Para isso consulte o exemplo mencionado na seção Pedido de Venda.


Para fazer uma fatura de vendas a partir de um pedido de vendas, use o endpoint mencionado abaixo. O parâmetro `source_name` aqui é o ID do pedido de vendas.



```
POST/api/method/erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice

# Corpo
{"nome_fonte": "SO-2022-00001"}

```

Para fazer uma fatura de venda a partir de uma nota de entrega, use o endpoint mencionado abaixo. O parâmetro `source_name` aqui é o ID da nota de entrega.



```
POST/api/method/erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice

# Corpo
{"nome_fonte": "SO-2022-00001"}


```

Ambos os enpoints retornam um objeto JSON da fatura de vendas com todos os itens pendentes a serem cobrados.


### 4. Pagamento contra o pedido ou fatura


Para gerar uma entrada de pagamento em relação a um pedido de venda ou fatura, use o endpoint abaixo



```
POST/api/method/erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry

# Corpo
{
    "dt": "Fatura de Venda",
    "dn": "SI-2022-0001",
    "party_amount": 2000, # Passa se o documento não tiver um campo `outstanding_amount` (parâmetro opcional)
    "bank_account": "Nome do Banco-CAB", # Pass caso queira usar outro que não o padrão (parâmetro opcional)
    "bank_amount": 2000, # Valor pago ou recebido dependendo do tipo de entrada de pagamento (parâmetro opcional)
    "party_type": "Cliente", # Se a entrada do pagamento for contra um tipo de parte diferente de Cliente ou Fornecedor (parâmetro opcional)
    "payment_type": "Pay", # Pague ou receba (parâmetro opcional)

}

```


