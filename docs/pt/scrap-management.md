# Gerenciamento de sucata de produção



Sucata significa resíduos que não têm valor econômico ou apenas o valor de seu conteúdo material batico recuperável por meio de reciclagem.


A sucata geralmente é aproveitada no final do processo de fabricação. Além disso, você pode encontrar alguns produtos que estão danificados ou inutilizáveis ​​devido ao prazo de validade ou por algum outro motivo, que precisam ser raspados.


No ERPNext, ao final do processo de fabricação, os itens de sucata são contabilizados nos armazéns de sucata.


## Sucata na lista de materiais


Você pode atualizar a quantidade estimada de refugo de um item na tabela BOM, Refugo. Se necessário, você pode selecionar novamente um item de matéria-prima como sucata.


![Sucata na lista técnica](/files/scrap-1.png)


## Sucata na entrada de fabricação


Quando a produção é concluída, a entrada de acabamento/fabricação é criada em uma ordem de produção. Nesta entrada, o item de sucata é buscado na tabela Item, com apenas o Target Warehouse atualizado para ele. Certifique-se de que a Taxa de avaliação esteja atualizada para este item para fins de lançamento nas contas.


![Sucata na entrada de fabricação](/files/scrap-2.gif)


> O refugo da BOM só funcionará se a Entrada de Fabricação for criada com base na BOM e não com base na Transferência de Material. Isso pode ser configurado nas Configurações de fabricação.


![Configurações de fabricação](/files/manufacturing-settings.png)



