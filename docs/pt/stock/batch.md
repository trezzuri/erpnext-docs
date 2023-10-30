# Lote



**O recurso Lote no ERPNext permite que você agrupe múltiplas unidades de um Item e atribua a elas um valor/número/tag exclusivo chamado Nº do Lote.**


Isso é feito com base no Item. Se o Item estiver em lote, um número de lote deverá ser mencionado em cada transação de estoque. Os números de lote podem ser mantidos manualmente ou automaticamente. Este recurso é útil para definir a data de validade de vários itens ou movê-los juntos para diferentes armazéns.


Para acessar a lista Lote Não, acesse:
> Home > Estoque > Nº de série e lote > Lote


## 1. Pré-requisitos


Antes de criar e usar um lote, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* Ative 'Tem número de lote' no cadastro de itens
![Lote não ativado](/files/batch-no-enabled.png)


## 2. Como criar um novo lote


Para definir o item como um item de lote, o campo "Tem número de lote" deve ser verificado no Cadastro de itens. Se você não selecionou "Criar novo lote automaticamente" ao criar um item, você terá que criar lotes manualmente à medida que avança.


Para criar um novo número mestre de lote para um item, vá para:


1. Vá para a lista Lote e clique em Novo.
2. Defina o ID do lote.
3. Selecione o item.
4. Se alguma transação for feita com um item, o lote não poderá ser armado ou desarmado.
5. Salvar.


Quando os lotes estão habilitados para um item, a opção de [reter estoque de amostra](/docs/pt/stock/retain-sample-stock) também fica disponível. 


### 2.1 Criação automática em lote


Se desejar a criação automática do lote no momento do recebimento da compra, você deve marcar 'Criar novo lote automaticamente' no cadastro de itens:


![Configuração de item para lotes](/files/item_setup_for_batch.png)


## 3. Recursos


### 3.1 Divisão e movimentação de lotes


Ao abrir um lote, você verá todas as quantidades que pertencem a esse lote na página.


![Visualização em lote](/files/batch_view.png)


* Para mover o lote de um armazém para outro, você pode clicar no botão **Mover**.
* Você também pode dividir o lote em um lote menor clicando no botão **Dividir**. Isso criará um novo lote com base neste lote e as quantidades serão divididas entre os lotes.


![Dividir lote](/files/batch_split.png)
* Se você definir a data de validade, o lote mostrará 'Não expirado' até a data de validade, após a qual mostrará 'Expirado'. Se uma data não for definida, o lote mostrará 'Não definido'.


### 3.2 Transação de itens com lotes


Um lote mestre deve ser criado antes da criação do Recibo de Compra.
Portanto, toda vez que um recibo de compra ou ordem de serviço for feito para um item de lote,
você primeiro criará seu número de lote e depois selecioná-lo no pedido de compra ou entrada de estoque.


Em cada transação de estoque (Recibo de compra, Nota de entrega, Fatura) com um item em lote,
você deve fornecer o número do lote do item.


> Nota: Nas transações de estoque, os IDs dos lotes serão filtrados com base no Código do Item, Armazém,
Data de vencimento do lote (comparada com a data de lançamento de uma transação) e quantidade real no armazém.
Ao pesquisar o ID do lote sem valor no campo Armazém, o filtro Quantidade real não será aplicado.


### 4. Tópicos Relacionados


1. [Número de série](/docs/pt/stock/serial-no)
2. [Abrir entrada de saldo de estoque para serializados e em lote Artigo](/docs/pt/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
3. [Gerenciamento de inventário em lote](/docs/pt/stock/articles/managing-batch-wise-inventory)



