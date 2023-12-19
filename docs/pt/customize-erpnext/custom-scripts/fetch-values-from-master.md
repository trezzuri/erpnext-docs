# Buscando valores do mestre



Para extrair o valor de um link na seleção, use o método `add_fetch`.



```
add_fetch(link_fieldname, source_fieldname, target_fieldname)

```

### Exemplo


Digamos que você criou um campo personalizado **ID do IVA** (`vat_id`) em **Cliente** e **Fatura de vendas** e deseja garantir que esse valor seja atualizado sempre que você selecionar um cliente em uma fatura de vendas.


Para configurar isso, no script personalizado da fatura de vendas, você pode adicionar esta linha:



```
cur_frm.add_fetch('cliente','vat_id','vat_id')

```


