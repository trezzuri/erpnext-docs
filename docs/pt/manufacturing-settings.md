# Configurações de fabricação



As configurações de fabricação podem ser encontradas em:


> Home > Fabricação > Configurações > Configurações de Fabricação


![Configurações de fabricação](/files/manufacturing-settings-1.png)


### Planejamento de capacidade


[Planejamento de capacidade](/docs/pt/manufacturing/capacity-planning) é o processo no qual uma organização decide se aceita ou não os novos pedidos com base em os recursos e ordens de serviço existentes.


### Desativar planejamento de capacidade


Se marcada, o planejamento de capacidade não será realizado. Ativá-lo ajudará a decidir se aceita ou não os novos pedidos com base nos recursos e nas ordens de serviço existentes.


### Permitir horas extras


Se ativado, permitirá a criação de ordens de serviço, cartões de trabalho etc. fora do horário de trabalho da estação de trabalho.


### Permitir produção em feriados


Se ativado, permitirá atividades de produção mesmo nos dias marcados como feriados de acordo com a Lista de Feriados da organização. 


### Planejamento de capacidade para (dias)


O número de dias especificado aqui significa o número de dias de antecedência em que as atividades de planejamento de capacidade serão iniciadas para produção. 


### Tempo entre operações (minutos)


Isso especifica o intervalo de tempo que deve ser mantido entre duas operações em minutos. 


### Porcentagem de subsídio de produção excedente


Ao criar Ordens de Serviço em relação a um Pedido de Vendas, o sistema permitirá apenas que a quantidade de itens de produção seja menor ou igual à quantidade no Pedido de Vendas. Caso você queira permitir que Ordens de Serviço sejam levantadas em maior quantidade, você pode mencionar aqui o Percentual de Superprodução.


Exemplo: Em certos casos, uma Estação de Trabalho precisa fabricar 100 unidades para obter boa relação custo-benefício, mas a Ordem de Serviço pode ser de 50 unidades. Nesse caso, a porcentagem de subsídio de produção excessiva seria 100.


### Armazém de trabalho em andamento padrão


Este armazém será atualizado automaticamente no campo Armazém 'Trabalho em andamento' das Ordens de Serviço.


### Armazém de produtos acabados padrão


Este Armazém será atualizado automaticamente no campo 'Armazém Alvo' da Ordem de Serviço.


### Permitir consumo contínuo de material


Se ativado, os materiais podem ser consumidos sem fabricar imediatamente produtos acabados em uma única ordem de serviço. 


Isso é útil se um ou mais produtos demorados estiverem sendo fabricados. Por exemplo, um único produto leva um mês para ser fabricado e as matérias-primas são consumidas diariamente. Num cenário normal, isto não será viável com entradas de stock. Ativar esta opção permitirá criar entradas de estoque para **Consumo de material** sem precisar criar uma entrada para backflush. O resultado final é que você pode ver o estoque sendo consumido nos Armazéns e atualizar a entrada de fabricação final para produtos acabados posteriormente.


### Backflush de matérias-primas com base em


O método selecionado aqui será escolhido para backflushing de matérias-primas:
1. Material transferido para fabricação
2. BOM


### Adicionar custo de operação corretiva na avaliação de produto acabado


Se ativado, o custo de um tipo de operação corretiva também será incluído no cálculo da avaliação de produtos acabados 


### Atualizar custo da BOM automaticamente


Se marcado, o custo da lista técnica será atualizado automaticamente com base na Taxa de avaliação/Taxa da lista de preços/Taxa da última compra de matérias-primas.


### Permitir transferência de material em excesso


Se ativado, o botão **Transferência de material** ficará visível e permitirá que você transfira matérias-primas mesmo depois que o requisito de matéria-prima for atendido em um Cartão de Trabalho.


Isso é particularmente útil nos casos em que as matérias-primas transferidas estão danificadas e é necessário transferir matérias-primas adicionais para produzir a mesma quantidade de produtos acabados pretendida.


### Fazer número de série/lote da ordem de serviço


Se marcado, o sistema criará automaticamente os números de série/lotes para produtos acabados no envio da Ordem de Serviço 



