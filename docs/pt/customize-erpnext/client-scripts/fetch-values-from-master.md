# Buscando valores do mestre


Para extrair um valor de um link na seleção, use o método `add_fetch`.



```
add_fetch(link_fieldname, source_fieldname, target_fieldname)

```

### Exemplo


Digamos que você criou um campo personalizado **ID do IVA** (`vat_id`) em **Cliente** e **Fatura de vendas** e deseja garantir que esse valor seja atualizado toda vez que você selecionar um cliente em uma fatura de venda.


Para configurar isso, no script personalizado de fatura de vendas, você pode adicionar esta linha:



```
cur_frm.add_fetch('customer','vat_id','vat_id')

```
