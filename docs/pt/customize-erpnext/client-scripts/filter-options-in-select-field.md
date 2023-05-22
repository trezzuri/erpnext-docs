# Opções de filtro em selecionar campo


Digamos que você tenha dois campos suspensos chamados Estado e Cidade. O estado tem dois valores Karnataka e Maharashtra e a cidade tem quatro valores, Bangalore, Mysore, Mumbai e Pune. Se você deseja filtrar as opções na cidade com base no valor escolhido no estado, pode escrever um script personalizado conforme mostrado abaixo.



```
frappe.ui.form.on("Lead", "state", function(frm) {
  if(frm.doc.state == "Karnataka")
  {
    set_field_options("cidade", ["Bangalore","Mysore"])
  }
  else if(frm.doc.state == "Maharashtra")
  {
    set_field_options("cidade", ["Mumbai","Pune"])
  }
  else if(frm.doc.state == "")
  {
    set_field_options("cidade", ["","Bangalore","Mysore","Mumbai","Pune"])
  }
  });

```

![Abrindo conta](/files/filter_dropdown.gif)

