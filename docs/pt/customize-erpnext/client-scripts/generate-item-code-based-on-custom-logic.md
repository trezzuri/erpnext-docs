# Gerar código de item com base na lógica personalizada


Adicione este Custom Script no script do **Item**, para que o novo Item Code seja
gerado logo antes de o item ser salvo.



```
cur_frm.cscript.custom_validate = function(doc) {
    // limpa item_code (o nome é de item_code)
    doc.item_code = "";

    // primeiros 2 caracteres baseados em item_group
    switch(doc.item_group) {
        caso "Teste A":
            doc.item_code = "TA";
            quebrar;
        caso "Teste B":
            doc.item_code = "TB";
            quebrar;
        padrão:
            doc.item_code = "XX";
    }

    // adiciona os próximos 2 caracteres com base na marca
    switch(doc.brand) {
        caso "Marca A":
            doc.item_code += "BA";
            quebrar;
        caso "Marca B":
            doc.item_code += "BB";
            quebrar;
        padrão:
            doc.item_code += "BX";
    }
}

```
