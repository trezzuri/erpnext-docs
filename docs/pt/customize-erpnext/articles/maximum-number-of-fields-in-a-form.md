# Número máximo de campos em um formulário



Às vezes, ao criar campos personalizados, você pode ter recebido uma mensagem de erro semelhante a esta:



> 
> Tamanho da linha muito grande. O tamanho máximo de linha para o tipo de tabela usado, sem contar os BLOBs, é 65535. Isso inclui sobrecarga de armazenamento, verifique o manual. Você precisa alterar algumas colunas para TEXT ou BLOBs.
> 
> 
> 


### O que isso significa?


Em termos simples, significa que você atingiu o limite do número máximo de campos para o formulário/tipo de documento específico. Então, qual é o limite máximo de campos?


No MySQL, há um limite rígido de 4.096 colunas por tabela, mas o máximo efetivo pode ser menor para uma determinada tabela. O limite exato depende de vários fatores interativos.


Cada tabela (independentemente do mecanismo de armazenamento) tem um tamanho máximo de linha de 65.535 bytes. Os mecanismos de armazenamento podem impor restrições adicionais a esse limite, reduzindo o tamanho máximo efetivo da linha.


O tamanho máximo da linha restringe o número (e possivelmente o tamanho) de colunas porque o comprimento total de todas as colunas não pode exceder esse tamanho (65.535 bytes). Por exemplo, caracteres `utf8mb3` requerem até 3 bytes por caractere, portanto, para uma coluna `VARCHAR(140)`, o servidor deve alocar `140 × 3 = 420` bytes por valor. Conseqüentemente, uma tabela não pode conter mais de `65.535/420 = 156` tais colunas.


No framework Frappe, colunas do tipo `VARCHAR(140)` são criadas com base nos campos "Data", "Link", "Select", "Dynamic Link", "Password" e "Read Only" tipos. Portanto, você pode criar aproximadamente 156 dessas colunas no sistema.


### Solução:


Para adicionar mais campos ao sistema, você pode fazer algumas alterações.


1. Converta alguns dos campos para campos do tipo "Texto", "Texto Pequeno", "Editor de Texto" ou "Código". No MySQL, as colunas BLOB e TEXT contam de um a quatro mais oito bytes cada em direção ao limite de tamanho da linha porque seu conteúdo é armazenado separadamente do restante da linha. Portanto, a conversão para esses tipos de campo liberará alguns espaços e permitirá a adição de mais campos.
2. Defina um valor menor na propriedade "Comprimento" ao criar campos, o valor padrão é 140. O sistema define o comprimento de `VARCHAR` com base nesta propriedade e aloca o tamanho para essas colunas. Conseqüentemente, um comprimento menor leva à adição de mais campos.



