# Atualizar campo de data com base no valor de outro campo de data



O script abaixo definiria automaticamente o valor do campo de data, com base no valor de outro campo de data.


Exemplo: a data de vencimento da produção deve ser definida como dois dias antes da data de entrega. Suponhamos que a Data de Entrega de um projeto já tenha sido definida, e exista um Campo 'Data de Vencimento de Produção' como tipo de campo 'Data' já presente no formulário. A aplicação do script a seguir garantirá que a Data de Vencimento da Produção seja atualizada automaticamente para dois dias antes da data de entrega.



```
cur_frm.cscript.custom_delivery_date = function(doc, cdt, cd){
cur_frm.set_value("data_de_produção", frappe.datetime.add_days(doc.delivery_date,-2));
 }

```


