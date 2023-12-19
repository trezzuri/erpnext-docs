# Manutenção do código do item do fornecedor no cadastro de itens



Para cada item, o código atribuído pode ser diferente do código fornecido pelo seu fornecedor para o mesmo item. O ERPNext permite rastrear o Código do Item do Fornecedor no cadastro de itens. Além disso, você pode buscar o Código do Item do Fornecedor em suas transações de compra, para que eles possam reconhecer facilmente o item referente ao seu Código do Item.


#### 1. Atualizando o código do item do fornecedor no item


No cadastro de itens, na seção Detalhes do fornecedor, insira o código do item conforme fornecido pelo fornecedor para este item.


![Código do item do fornecedor](/files/supplier-item-code.png)


#### 2. Código do item do fornecedor nas transações


Cada transação de compra possui um campo na tabela Item onde é buscado o Código do Item do Fornecedor. Este campo fica oculto no formulário e também no formato de impressão Padrão. Você pode torná-lo visível alterando a propriedade deste campo em [Personalizar formulário.](/docs/pt/customize-erpnext/customize-form.html)


Vá para a visualização de impressão, clique em Menu > personalizar, insira um novo nome para o formato de impressão, procure a tabela Itens, clique no botão **Selecionar colunas** nela. Você verá a seguinte tela. Agora marque a caixa de seleção "Número de peça do fornecedor".


![Formato de impressão da peça do item do fornecedor](/files/supplier-item-code-print-format.png)


O Código do Item do Fornecedor só será obtido na transação de compra, se tanto o Fornecedor quanto o Código do Item selecionados na transação de compra estiverem mapeados com o valor mencionado no Cadastro de Itens.


![Código do item do fornecedor na transação](/files/supplier-item-code-in-purchase-order.png)




