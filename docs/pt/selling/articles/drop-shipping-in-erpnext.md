# Envio direto



**Drop Shipping** é um método de gerenciamento da cadeia de suprimentos no qual o varejista não mantém as mercadorias em estoque, mas em vez disso transfere os pedidos do cliente e os detalhes da remessa para o fabricante, outro varejista ou atacadista, que em seguida, envia a mercadoria diretamente ao cliente.  
O envio direto também pode ocorrer quando um pequeno varejista (que normalmente vende em pequenas quantidades para o público em geral) recebe um único grande pedido de um produto. O varejista pode providenciar que as mercadorias sejam enviadas diretamente ao cliente pelo fabricante ou distribuidor. O transporte direto é comum com produtos caros. Em qualquer caso, nenhum estoque é mantido pelo varejista, simplesmente agindo como um *intermediário*. Neste artigo, veremos como o ERPNext oferece uma experiência perfeita de envio direto.  
Considere uma empresa que lida com monitores de computador. Agora, o varejista recebeu um pedido de um cliente, ABC Inc., de 1.000 monitores DELL de 24 polegadas.  
**Drop Shipping em ação:**   
**1. Configuração do Item*** Configure o Item com informações obrigatórias mantendo Manter Estoque desabilitado, pois não haverá estocagem deste Item.
* Em seguida, **habilitar** "Entregue pelo Fornecedor (Drop Ship)
* Defina o Fornecedor com quem o Pedido de Compra será levantado para o atendimento deste pedido.

  
![](/files/RD6ip0k.png)  
**2. Ciclo de vendas:*** Criar pedido de vendas com cliente, item, quantidade, taxa, impostos e assim por diante.

  
![](/files/oN2oubM.png)  
  
**3. Atendimento do pedido:*** No próprio documento do pedido de vendas, você pode criar o pedido de compra para esta remessa, rastrear a entrega e cobrar o cliente de acordo.

   
![](/files/mSsoueP.gif)

