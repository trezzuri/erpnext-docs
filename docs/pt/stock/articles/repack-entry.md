# Reempacotar entrada



Repack Entry é criado para itens comprados a granel, que estão sendo embalados em pacotes menores. Por exemplo, um item comprado em toneladas pode ser reembalado em Kgs.


Notas:


1. O item comprado e reembalado terão códigos de item diferentes.
2. A entrada de reembalagem pode ser feita com ou sem BOM (lista de materiais).


Em uma entrada de reembalagem, pode haver um ou mais itens de reembalagem. Vamos verificar o cenário abaixo para entender isso melhor.


Suponha que estamos comprando caixas de tinta spray de uma cor específica (verde, azul etc). E posteriormente reagrupá-los para criar pacotes contendo várias cores de tinta spray (azul-verde, verde-amarelo etc.).


#### 1. Nova entrada de estoque


`Estoque > Documentos > Entrada de estoque > Nova entrada de estoque`


#### 2. Insira os itens


Selecione a finalidade como 'Entrada de reembalagem'.


Para item de matéria-prima/insumo, apenas o Armazém de Origem será fornecido.


Para itens reembalados/de saída, apenas o Target Warehouse será fornecido. Você terá que fornecer uma avaliação para os itens reembalados.


![Repack Entry](/files/repack-1.png)


Atualize a quantidade de todos os itens selecionados.


#### 3. Enviar entrada de estoque


Ao enviar a Entrada de Estoque, o estoque do item de entrada será reduzido no Armazém de Origem e o estoque do item reembalado/de saída será adicionado no Armazém de Destino.


![Reempacotar entrada de estoque](/files/repack-2.png)




