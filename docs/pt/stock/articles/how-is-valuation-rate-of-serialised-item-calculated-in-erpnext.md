# Cálculo da taxa de avaliação de itens serializados



No ERPNext, a**taxa de avaliação** do estoque do item é atualizada na criação da seguinte transação:  
1. Recibo de Compra
2. Entrada de Estoque do tipo Recibo de Material
3. Conciliação de Estoque realizada para atualização do saldo inicial do estoque

  
ERPNext suporta 2 tipos de avaliação: FIFO e Média Móvel.   
Você pode selecionar o método de avaliação com base no valor do item que será calculado. Ele pode ser definido por item individual, bem como globalmente para todos os itens nas configurações de estoque.  
![](/files/Ecw7uZV.png)  
  
As taxas de avaliação dos itens são calculadas de acordo com o método de avaliação definido para eles. Entretanto, no caso de **item serializado**, essas configurações são *ignoradas*. O item abaixo, "Macbook Pro", é um item serializado e sua taxa de avaliação não é obtida no item mestre. Em vez disso, a taxa de avaliação é atualizada a partir da *taxa de entrada de ações da primeira entrada*, RS 199,80. Consequentemente, ele é atualizado conforme as demais transações realizadas neste Item.  
Item Master:  
![](/files/SD7TwWD.png)  
![](/files/yhdnL5S.png)  
Lista de estoque:  
![](/files/cXFcuOu.png)  
Para saber mais sobre o módulo ERPNext Stocks, clique em [aqui](https://erpnext.com/docs/user/manual/en/stock)

