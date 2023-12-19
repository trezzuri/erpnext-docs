# Relatório de nível de estoque



O relatório de nível de estoque lista a quantidade de itens em estoque disponíveis em um determinado depósito.


Existem vários relatórios disponíveis onde você pode verificar o nível de estoque do item.


#### Relatório de quantidade projetada de estoque


Você pode acessar este relatório em `Estoque > Relatório principal > Quantidade projetada de estoque`


Este relatório lista o item em termos de nível de estoque no armazém de um item, considerando todas as transações de estoque. Com a Quantidade Real de um item, também fornece outros detalhes como:


1. Qtd Real: Quantidade disponível no armazém.
2. Qtd planejada: Quantidade para a qual a Ordem de Serviço foi levantada, mas está pendente de fabricação.
3. Quantidade solicitada: quantidade solicitada para compra, mas não solicitada.
4. Quantidade solicitada: quantidade solicitada para compra, mas não recebida.
5. Quantidade reservada: quantidade solicitada para venda, mas não entregue.
6. Quantidade do projeto: a quantidade do projeto é calculada como


Quantidade projetada = Quantidade real + Quantidade planejada + Quantidade solicitada + Quantidade solicitada-Quantidade reservada
O estoque projetado é usado pelo sistema de planejamento para monitorar o ponto de reabastecimento e determinar a quantidade de reabastecimento. A Quantidade projetada é utilizada pelo mecanismo de planejamento para monitorar os níveis de estoque de segurança. Esses níveis são mantidos para atender demandas inesperadas.


Ter um controle rígido do estoque projetado é crucial para determinar a escassez e calcular a quantidade correta do pedido.



