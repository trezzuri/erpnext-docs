# Objetivo de entrada de ações



O Stock Entry é uma transação de ações que pode ser usada para diversos fins. Vamos aprender mais sobre cada finalidade de entrada de ações abaixo.


#### 1.Objetivo: Problema material


A entrada de saída de material é criada para retirar itens de um depósito. No envio da Emissão de Material, o estoque do item é deduzido do Armazém de Origem.


A emissão de material geralmente é feita para itens consumíveis de baixo valor, como material de escritório, consumíveis de produtos, etc. Você também pode criar uma emissão de material para reconciliar o estoque de itens serializados e em lote.


![Material Issue](/files/stock-entry-issue.png)


#### 2.Finalidade: Recebimento de Material


A entrada de recebimento de material é criada para o estoque interno de itens em um depósito. Este tipo de entrada de estoque pode ser criado para atualizar o saldo inicial de itens serializados e em lote. Além disso, itens comprados sem Ordem de Compra podem ser recebidos na entrada de Recibo de Material.


Para efeito de avaliação de estoque, desde que Avaliação de Item se torne um campo obrigatório no registro de Recebimento de Material.


![Recibo de material](/files/stock-entry-receipt.png)


#### 3.Objetivo: Transferência de Material


A entrada de transferência de materiais é criada para a transferência de materiais entre armazéns.


![Material Transfer](/files/stock-entry-transfer.png)


#### 4. Objetivo: Transferência de material para fabricação


No processo de fabricação, as matérias-primas são enviadas das lojas para o departamento de produção (geralmente armazém WIP). Esta entrada de Transferência de Material é criada a partir da Ordem de Serviço. Os itens nesta entrada são obtidos da lista técnica do item de produção, conforme selecionado na ordem de serviço.


![Transferência para fabricação](/files/stock-entry-manufacture-transfer.gif)


#### 4.Finalidade: Fabricação


A fabricação é criada a partir da ordem de serviço. Nesta entrada, tanto o item de matéria-prima quanto o item de produção são buscados na BOM, selecionada na Ordem de Serviço. Para os itens de matéria-prima, apenas o Armazém de Origem (geralmente armazém WIP) é mencionado. Para o item de produção, somente o armazém de destino mencionado na Ordem de Serviço é atualizado. No envio, o estoque de itens de matéria-prima é deduzido do Armazém de Origem, o que indica que os itens de matéria-prima foram consumidos no processo de fabricação. O Item de Produção é adicionado ao Armazém Alvo marcando a conclusão do ciclo de produção.


![Manufacture](/files/stock-entry-manufacture.gif)


#### 5. Objetivo: Reembalar


A entrada de reembalagem é criada quando itens comprados a granel são reembalados em pacotes menores. [Verifique esta página para saber mais sobre a entrada Repack.](/docs/pt/stock/articles/repack-entry.html)


#### 6.Objetivo: Subcontratar


A transação de subcontratação envolve a transferência da empresa de itens de matéria-prima para o armazém do subcontratado. Isto requer também a adição de um armazém para o subcontratado. A entrada do subcontrato transfere o estoque do armazém da empresa para o armazém do subcontratado. [Verifique esta página para saber mais sobre subcontratação](/docs/pt/manufacturing/subcontracting.html).


![Subcontract](/files/stock-entry-subcontract.gif)




