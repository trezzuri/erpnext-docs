# Não é possível ativar o número de série e de lote



Às vezes é bem possível que você não queira começar a rastrear o inventário em lote e/ou serializado, mas queira começar a fazer isso posteriormente.   
O sistema, por padrão, não permite que você ative essas opções depois que as transações de estoque forem feitas.![](/files/a0VHlSB.png)Você pode ler mais sobre por que o mesmo está desativado [aqui](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html).  
Para ativar as opções novamente, você pode excluir todas as transações de estoque deste item ou, se isso não for uma opção, você pode duplicar o mesmo item e entrar no estoque com essas opções marcadas.  
**PASSOS:****﻿**1. Você terá que primeiro estocar o item atual usando a Ferramenta de reconciliação de estoque (zerar o estoque atual). Você também pode estocar o item fazendo um lançamento de estoque do tipo **Saída de material**.
2. Em seguida, usando o recebimento de material, entre no estoque serializado. Consulte o link a seguir para obter ajuda sobre o mesmo: [https://erpnext.org/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item](https://docs.erpnext.com/docs/pt/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
3. Desative os itens antigos para que não possam ser selecionados novamente nas transações.

  
**Nota:** Se quiser manter o mesmo código de item, você precisará renomear os itens existentes e, em seguida, criar o novo item de acordo com o código de item real. Caso contrário, você manterá o item com um novo código.

