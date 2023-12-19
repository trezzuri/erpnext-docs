# Abrindo entrada de saldo de estoque para item serializado e em lote



Itens para os quais o número de série e o número do lote são mantidos, a abertura do saldo de estoque para eles é atualizada por meio de entrada de estoque. [Clique aqui para saber como o inventário serializado é gerenciado no ERPNext](/docs/pt/stock/serial-no.html).


**Pergunta:** Por que a entrada do saldo inicial para o item serializado e em lote não pode ser atualizada por meio da reconciliação de estoque?


No ERPNext, o nível de estoque de um item serializado é derivado com base na contagem dos números de série desse item. Portanto, a menos que sejam criados números de série para o item serializado, seu nível de estoque não será atualizado. Na Ferramenta de reconciliação de estoque, você só pode atualizar a quantidade inicial de um item, mas não o número de série e o número do lote.


### Saldo inicial do item serializado


A seguir estão as etapas para criar uma entrada de saldo de estoque inicial para o item serializado e em lote.


#### Etapa 1: Nova entrada de estoque


`Estoque > Entrada de estoque > Novo`


#### Etapa 2: Selecione a finalidade


O objetivo de entrada de estoque deve ser atualizado como `Recebimento de material`.


#### Etapa 3: Atualizar a data de postagem


A data de lançamento deve ser a data em que você deseja atualizar o saldo inicial de um item.


#### Etapa 4: atualizar o Target Warehouse


O Armazém Alvo será aquele em que o saldo inicial de um item será atualizado.


#### Etapa 5: selecionar itens


Selecione os itens cujo saldo inicial será atualizado.


#### Etapa 6: atualizar a quantidade de abertura


Para o item serializado, atualize a quantidade de acordo com o número de números de série.


Para o item serializado, mencione os números de série equivalentes à sua quantidade. Ou se os números de série estiverem configurados para serem criados com base no prefixo, não será necessário mencionar os números de série manualmente. Clique [aqui](/docs/pt/stock/articles/serial-no-naming.html) para saber mais sobre a nomenclatura do número de série.


Para um item de lote, forneça o ID do lote no qual o saldo inicial será atualizado. Mantenha o mestre do lote pronto e atualize-o para o item do lote. Para criar um novo lote, acesse:


`Estoque > Configuração > Lote > Novo`


[Clique aqui para saber como o inventário Batchwise é gerenciado no ERPNext.](/docs/pt/stock/articles/managing-batch-wise-inventory.html) 


#### Etapa 7: atualizar a taxa de avaliação do item


Atualize a taxa de avaliação, que será por valor unitário do item. Caso unidades diferentes dos mesmos itens tenham taxas de avaliação diferentes, elas deverão ser atualizadas em uma linha separada, com Taxas de Avaliação diferentes.


#### Etapa 8: conta de diferença


De acordo com o sistema de avaliação de estoque permanente, um lançamento contábil é criado para cada transação de estoque. O sistema de contabilidade de dupla entrada requer a correspondência do Débito Total com o Crédito Total em uma entrada. No momento da submissão do Lançamento de Estoque, o sistema debita a conta do Almoxarifado pelo valor total dos itens. Para equilibrar a mesma, usamos a conta de Abertura Temporária como Conta Diferença.


![Conta de diferença](/files/difference-account-1.png)


#### Etapa 9: Salvar e enviar entrada de estoque


No envio da entrada de estoque, o lançamento no razão de estoque será lançado e o saldo inicial será atualizado para os itens em uma determinada data de lançamento.










