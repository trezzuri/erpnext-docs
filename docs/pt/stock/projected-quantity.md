# Quantidade projetada



**Quantidade projetada é o nível de estoque previsto para um item específico com base nos níveis de estoque atuais e outros requisitos.**


É a quantidade de estoque bruto que inclui oferta e demanda no passado que
é feito como parte do processo de planejamento.


O estoque projetado é usado pelo sistema de planejamento para monitorar o novo pedido
ponto e para determinar a quantidade de reabastecimento. A quantidade projetada é usada por
o mecanismo de planejamento para monitorar os níveis de estoque de segurança. Esses níveis são
mantido para atender demandas inesperadas.


Ter um controle rígido do estoque projetado é crucial para determinar
escassez e calcular a quantidade correta do pedido.


![Quantidade projetada](/files/projected_quantity.png)


A fórmula para calcular a quantidade projetada é a seguinte:


*Quantidade projetada = Quantidade real + Quantidade planejada + Quantidade solicitada + Quantidade solicitada-Quantidade reservada-Quantidade reservada para produção-Quantidade reservada para subcontratação-Quantidade reservada para plano de produção*


* **Qtd Real**: Quantidade disponível no Armazém. Este é o estoque físico real que você possui.
* **Qtd planejada**: Quantidade para a qual a Ordem de Serviço foi levantada, mas está pendente de fabricação.
* **Quantidade solicitada**: quantidade solicitada por meio de uma [Solicitação de material](/docs/pt/stock/material-request). Ele é adicionado no envio da Solicitação de Material e subtraído quando a Ordem de Compra/Ordem de Trabalho/Entrada de Estoque é criada com base no tipo de Solicitação de Material.
* **Quantidade encomendada**: Quantidade solicitada para compra ([Pedido de compra](/docs/pt/buying/purchase-order)), mas não recebido (por meio de um [Recibo de compra](/docs/pt/stock/purchase-receipt) ou um [Fatura de compra](/docs/pt/accounts/purchase-invoice).
* **Quantidade reservada**: quantidade encomendada para venda pelo seu cliente ([Pedido de vendas](/docs/pt/selling/sales-order)), mas não entregue (por meio de uma [Nota de entrega](/docs/pt/stock/delivery-note)). Essa quantidade aumenta quando um pedido de vendas é enviado e diminui quando uma nota de entrega ou fatura de vendas é criada em relação a esse pedido de vendas.
* **Quantidade reservada para produção**: as matérias-primas são reservadas mediante envio da [Ordem de serviço](/docs/pt/manufacturing/work-order) e é reduzido quando as matérias-primas são transferidas para o armazém de Trabalho em Andamento através de uma Entrada de Estoque.
* **Quantidade Reservada para Subcontratação**: Matérias-primas reservadas quando uma Ordem de Compra de subcontratação é enviada. Quando as matérias-primas são transferidas para o Armazém do Fornecedor através de uma Entrada de Estoque, esta quantidade diminui. Para saber mais sobre subcontratação [clique aqui](/docs/pt/manufacturing/subcontracting).
* **Quantidade Reservada para Plano de Produção**: As matérias-primas são reservadas quando um Plano de Produção é submetido. Quando os materiais são reservados para a produção contra a ordem de serviço o sistema reduzirá a “Qtd Reservada para Plano de Produção” no respectivo BIN. O sistema reduz a quantidade se a ordem de serviço foi feita de acordo com o plano de produção.


#### Tópicos Relacionados


1. [Armazém](/docs/pt/stock/warehouse)
2. [Solicitação de material](/docs/pt/stock/material-request)



