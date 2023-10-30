# Campo Manter estoque congelado no cadastro de itens



No mestre de itens, você pode testemunhar que os valores nos campos a seguir serão congelados.


1. Manter estoque
2. Tem número de lote
3. Possui número de série


![Campo de item congelado](/files/maintain-stock-1.png)


Para um item, depois que a entrada no razão de estoque for criada, os valores nesses campos serão congelados. Isso evita que o usuário altere o valor, o que pode levar a uma incompatibilidade entre o estoque real e o nível de estoque no sistema de um item.


Para o item serializado, como seu nível de estoque é calculado com base na contagem de números de série disponíveis, definir o item como não serializado no meio interromperá a sincronização, e o nível de estoque do item mostrado no relatório não será preciso , portanto, o campo Has Serial No. está congelado.


Para tornar esses campos editáveis ​​novamente, você deve excluir todas as transações de estoque realizadas para este item. Para o item serializado e em lote, você também deve excluir o registro do número de série e do número do lote para este item.




