# Adicione um botão personalizado



```
frappe.ui.form.on("Evento", "atualizar", function(frm) {
    frm.add_custom_button(__("Faça alguma coisa"), function() {
        // Quando este botão for clicado, faça isso

        var assunto = frm.doc.subject;
        var event_type = frm.doc.event_type;

        // faz algo com esses valores, como uma requisição ajax
        // ou chame uma função frappe do lado do servidor usando frappe.call
        $.ajax({
            url: "http://example.com/just-do-it",
            dados: {
                "assunto": assunto,
                "event_type": event_type
            }

            // leia mais sobre a sintaxe $.ajax em http://api.jquery.com/jquery.ajax/

        });
    });
});

```