# Preço do item



**Preço do item é o registro no qual você pode registrar a taxa de venda e compra de um item.**


## 1. Como criar o preço do item


1. Existem duas maneiras de acessar um novo formulário de Preço de Item:


**Venda/Compra/Estoque > Itens e preços > Preço do item > Novo**.


Ou


**Estoque > Item > Clique em "+" ao lado do Preço do item**.
2. Selecione o item. O nome, UM e descrição serão obtidos.
3. Selecione a Lista de Preços, seja preço de Venda/Compra ou qualquer outra lista de preços que você possa ter criado.
4. Insira a taxa real no campo Taxa.
5. Salvar.
![Lista de preços do item](/files/item-price-1.png)


### 1.1 Selecionando a lista de preços


Você pode criar múltiplas Listas de Preços para um Item no ERPNext para rastrear o Preço de Venda e Compra de um Item separadamente. Além disso, se os preços de venda do item mudarem com base no território ou devido a outros critérios, você poderá criar várias listas de preços de venda para ele.


Ao selecionar a Lista de Preços, também serão buscadas sua moeda e aplicabilidade, seja para venda/compra ou ambas. Para obter o preço do item na transação de venda ou compra, você deve selecionar 'Lista de preços' na transação em Moeda e lista de preços.


Para verificar todos os preços dos itens juntos, acesse:


**Estoque > Relatórios de estoque > Preço do item Estoque**


Acesse a página [Listas de preços](/docs/pt/stock/price-lists) para saber mais.


## 2. Recursos


### 2.1 Unidade de medida (UOM)


O usuário pode adicionar preços de itens específicos da UOM se um item for vendido em UOMs diferentes. Por exemplo: digamos que um item Arroz é vendido em pacotes de 1 KG e 500 gramas então os usuários podem mencionar a UOM nos preços dos itens e com base na UOM selecionada na transação o preço do item será aplicado


### 2.2 Unidade de embalagem


Esta é a quantidade que deve ser comprada ou vendida por unidade de medida. Por exemplo, se a Unidade de Embalagem for dois e a UOM for um, serão transacionados dois itens em quantidade. O padrão é 0, você pode usar UM não inteiro, como 1,5 kg de aveia para 1 unidade de embalagem. Se você deixar como 0, isso não afetará nenhuma transação.


### 2.3 Quantidade mínima


Essa é a quantidade mínima de itens a serem transacionados para que esse preço seja aplicável e atualizado na lista de Preços de Itens.


### 2.4 Aplicando lista de preços a um cliente/fornecedor específico


Se você selecionar uma lista de Preço de Venda, aparecerá um campo de cliente onde você poderá atribuir este Preço de Item a um cliente específico. Da mesma forma, se você selecionar uma Lista de Preços de Compra, aparecerá um campo Fornecedor onde você poderá selecionar um Fornecedor específico


### 2.5 Aplicando lista de preços a um lote específico


Você também pode vincular um lote específico a um Preço do Item e, ao selecionar esse lote na transação, o preço do item para esse lote específico será aplicado.


### 2.6 Validade


Existem dois campos aqui: 'Válido desde' e 'Válido até'. Válido desde é definido como a data em que você criou o Preço do Item. Você também pode definir a data Válido até em que o Preço do Item irá expirar.


### 2,7 Prazo de entrega em dias


O número aproximado de dias que o produto leva para chegar ao armazém. Você pode definir preços de itens diferentes com base em quanto tempo o mesmo produto chegará até você de diferentes fornecedores.


### 2.8 Nota


Você pode adicionar qualquer observação sobre o preço do item neste campo.


## 3. Vídeo



.embed-container {posição: relativa; preenchimento inferior: 56,25%; altura: 0; estouro: oculto; largura máxima: 100%; } .embed-container iframe, .embed-container objeto, .embed-container embed {posição: absoluto; superior: 0; esquerda: 0; largura: 100%; altura: 100%; }





### 4. Tópicos Relacionados


1. [Item](/docs/pt/stock/item)
2. [Aplicar desconto](/docs/pt/selling/articles/applying-discount)



