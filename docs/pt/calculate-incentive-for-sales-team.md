# Calcular incentivo para equipe de vendas



Você pode calcular incentivos para a equipe de vendas usando scripts personalizados.


Pode ser usado em qualquer Transação de Vendas com a **Equipe de Vendas** Tabela:



```
cur_frm.cscript.custom_validate = function(doc) {
   //calcula incentivos para cada pessoa no negócio
    incentivo_total = 0
    $.each(wn.model.get("Equipe de Vendas", {parent:doc.name}), function(i, d) {

       //calcula o incentivo
        var incentivo_percent = 2;
        if(doc.grand_total > 400) incentivo_percent = 4;

       //incentivo real
        d.incentivos = flt(doc.grand_total) * incentivo_percent/100;
        total_incentivo += flt(d.incentivos)
    });

    doc.total_incentivo = total_incentivo;
}

```


