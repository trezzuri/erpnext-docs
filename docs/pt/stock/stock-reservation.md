# Reserva de estoque




> Introduzida na versão 15
> 
> 

A reserva de estoque, também conhecida como reserva de estoque, refere-se à prática de reservar uma quantidade específica de estoque ou estoque para um determinado propósito ou cliente.

### 1. Pré-requisitos

* Ativar reserva de estoque nas configurações de estoque. ![stock-settings](/files/stock-settings.png)![]()

### 2. Reserva de estoque contra pedido de venda

* Crie um pedido de venda. ![sales-order](/files/sales-ordere027b8.png)![]()
* Verifique o estoque de reserva dos itens que deseja reservar. ![sales-order-item](/files/sales-order-item.png)![]()
* Clique em **Reserva de estoque** e selecione **Reservar** . Escolha o armazém e a quantidade e clique no botão **Reservar Estoque**. ![sales-order-reserve](/files/sales-order-reserve.gif)![]()
* As entradas de reserva de estoque são criadas em relação aos itens do pedido de venda. ![stock-reservation-entries](/files/stock-reservation-entriesb9a114.gif)![]()

### 3. Reserva de estoque da lista de seleção

* Crie um pedido de vendas.
* Crie uma lista de seleção para o pedido de vendas.
* Na lista de seleção, clique em **Reserva de estoque** e selecione **Reserva**. As entradas de reserva de estoque serão criadas na lista de seleção. ![sales-order-pick-list-reserve](/files/sales-order-pick-list-reserve.gif) ![]()

### 4. Reserva automática de estoque na compra

* Navegue até Configurações de estoque e ative **Reserva automática de estoque para pedido de venda na compra**.
* Crie um pedido de vendas.
* Crie um recebimento de material para o pedido de vendas.
* Crie um pedido de compra de Recibo de material.
* Conclua o processo criando um recibo de compra para o pedido de compra. O estoque será automaticamente reservado mediante envio do Recibo de Compra.

### 5. Cancelamento de reserva de estoque

Existem duas maneiras de cancelar a reserva do estoque.

1. Cancelamento de reserva de estoque do pedido de vendas ou lista de seleção:


	* Abra um documento e clique no botão **Reserva de estoque > Cancelar reserva**, as entradas de reserva de estoque listadas serão canceladas. ![sales-order-unreserve](/files/sales-order-unreserve.gif)![]()
2. Desreservar o estoque do DocType de entrada de reserva de estoque: 


	* 2.1 Abra uma entrada de reserva de estoque e cancele-a clicando no botão **Cancelar**. ![stock-reservation-entry-cancel](/files/stock-reservation-entry-cancel.gif)![]()
	* 2.2 Vá para a lista de entradas de reserva de estoque, selecione as entradas desejadas cancelar e clique em **Ações > Cancelar**. ![stock-reservation-entries-cancel](/files/stock-reservation-entries-cancel.gif)![]()

### 6. Tópicos relacionados

1. [Ordem de venda](/docs/pt/selling/sales-order)
2. [Lista de seleção](/docs/pt/stock/pick-list)


