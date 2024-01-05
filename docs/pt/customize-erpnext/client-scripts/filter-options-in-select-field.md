# Opções de filtro no campo selecionado



Digamos que você tenha dois campos suspensos chamados Estado e Cidade. O estado tem dois valores Karnataka e Maharashtra e a cidade tem quatro valores, Bangalore, Mysore, Mumbai e Pune. Se desejar filtrar opções em Cidade com base no valor escolhido em Estado, você pode escrever um script personalizado conforme mostrado abaixo.



```
frappe.ui.form.on("Lead", "state", function(frm) {
  if(frm.doc.state == "Karnataka")
  {
    set_field_options("cidade", ["Bangalore","Mysore"])
  }
  senão if(frm.doc.state == "Maharashtra")
  {
    set_field_options("cidade", ["Mumbai","Pune"])
  }
  senão if(frm.doc.state == "")
  {
    set_field_options("cidade", ["","Bangalore","Mysore","Mumbai","Pune"])
  }
  });

```

![Abrindo conta](/files/filter_dropdown.gif)



