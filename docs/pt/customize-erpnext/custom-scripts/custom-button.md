# Adicionar um botão personalizado




```
frappe.ui.form.on("Evento", "atualizar", function(frm) {
    frm.add_custom_button(__("Faça algo"), function() {
       //Quando este botão for clicado, faça isso

        var assunto = frm.doc.subject;
        var event_type = frm.doc.event_type;

       //faça algo com esses valores, como uma solicitação ajax
       //ou chame uma função frappe do lado do servidor usando frappe.call
        $.ajax({
            url: "http://example.com/just-do-it",
            dados: {
                "assunto": assunto,
                "tipo_evento": tipo_evento
            }

           //leia mais sobre a sintaxe $.ajax em http://api.jquery.com/jquery.ajax/

        });
    });
});

```


