# Atualizar campo de data com base no valor em outro campo de data


O script fornecido abaixo definiria automaticamente o valor para o campo de data, com base no valor em outro campo de data.


Exemplo: A Data de Vencimento da Produção deve ser definida como dois dias antes da Data de Entrega. Vamos supor que a Data de Entrega de um projeto já tenha sido definida, e que exista um Campo 'Data de Vencimento da Produção' como um campo do tipo 'Data' já presente no formulário. A aplicação do script a seguir deve garantir que a Data de Vencimento da Produção seja atualizada automaticamente para dois dias antes da data de entrega.



```
cur_frm.cscript.custom_delivery_date = function(doc, cdt, cd){
cur_frm.set_value("production_due_date", frappe.datetime.add_days(doc.delivery_date, -2));
 }

```