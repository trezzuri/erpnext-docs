# Variantes de itens



**Uma variante de item é uma versão de um item com diferentes atributos, como tamanhos ou cores.**


Ex: suponha que uma camiseta seja um item e venha em diferentes tamanhos e cores, como pequeno, médio, grande e vermelho, azul, verde. No ERPNext a camiseta será considerada como um modelo de Item e cada uma das variações será uma Variante de Item.


Uma camiseta *azul* em tamanho *pequeno* em vez de apenas uma camiseta. As variantes de item permitem que você trate as versões *pequena*, *média* e *grande* de uma camiseta como variações de uma 'camiseta' de item. 


Sem as variantes de item, você teria que tratar as versões *pequena*, *média* e *grande* de uma camiseta como três itens separados. 


## 1. Usando variantes de itens


As variantes podem ser baseadas em duas coisas:


1. Atributos do item
2. Fabricantes


> Dica: depois que um modelo de item é criado, quando você atualiza esse modelo, todas as variantes também são atualizadas de acordo.


### 1.1 Criando o modelo de variante de item


1. Para usar Variantes de Itens no ERPNext, crie um Item e marque 'Tem Variantes' em Variantes.
2. O Item será então chamado de 'Modelo'. Esse modelo não é mais idêntico a um 'item' normal. Por exemplo, ele (o modelo) não pode ser usado diretamente em nenhuma transação (pedido de venda, nota de entrega, fatura de compra).
3. Somente as Variantes do Item (camiseta *azul* no tamanho *pequeno)* podem ser utilizadas na prática. Portanto, seria ideal decidir se um item 'tem variantes' ou não diretamente ao criá-lo.
![Tem variantes](/files/item-has-variants.png)
4. Ao selecionar 'Tem variantes' aparecerá uma tabela. Especifique os atributos de variante do Item na tabela. Caso o atributo possua Valores Numéricos, pode-se especificar o intervalo e criar intervalos com base nos valores de incremento.
![Atributos válidos](/files/item-attributes.png)
> Observação: você não pode fazer transações em um 'modelo'.


### 1.2 Criando variantes de item com base em atributos de item


Para criar 'Variantes de item' em um 'Modelo', clique em 'Criar'. A partir daí, escolha se deseja criar uma variante única ou múltipla. Single é simples onde você cria apenas um ou mais atributos e um Item será criado. Ao escolher múltiplas variantes, marque os atributos e vários itens serão criados. Por exemplo, se você escolher Cor: Vermelho, Verde e Tamanho: Pequeno, Médio, Grande, serão criadas 6 variantes.


Criando múltiplas variantes no ERPNext:


![Make Variants](/files/make-multiple-variants.png)


Para saber mais sobre como definir atributos, consulte [Atributos de item](/docs/pt/stock/item-attribute)


### 1.3 Variantes de itens com base nos fabricantes


Para configurar variantes baseadas em fabricantes, no seu modelo de item, defina "Variantes baseadas em" como "Fabricantes"
Neste caso, para criar variantes, clique em Criar > Criar Variante. O sistema solicitará que você selecione um fabricante. Opcionalmente, você também pode inserir um número de peça do fabricante.


![Configurar variante do item por fabricante](/files/select-mfg-for-variant.png)


A nomenclatura da variante será baseada no nome (ID) do item do modelo com um sufixo numérico. por exemplo. "Chave de fenda" terá a variante "Chave de fenda-1".


## 2. Atualizar variantes de itens com base no modelo


Acesse: **Página inicial > Estoque > Itens e preços > Configurações de variantes de itens**. Os campos exibidos aqui também serão copiados para as variantes. Por padrão, todos os campos são mostrados. Exclua todas as linhas que você não deseja que sejam atualizadas do modelo de item para as variantes.


## 3. Vídeo


### 3.1 Criando variante de item uma por uma






### 3.2 Criando variantes de itens em massa






### 4. Tópicos Relacionados


1. [Grupo de itens](/docs/pt/stock/item-group)
2. [Atributo do item](/docs/pt/stock/item-attribute)
3. [Preço do item](/docs/pt/stock/item-price)
4. [Codificação de itens](/docs/pt/stock/articles/item-codification)



