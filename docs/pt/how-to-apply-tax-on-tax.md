# Aplicar imposto sobre outro imposto ou encargo



Considere que um cliente em potencial deseja aplicar imposto sobre um imposto. Vejamos um exemplo de imposto (NBT) que deve ser aplicado sobre o valor total líquido dos itens e, em seguida, aplicar outro imposto (IVA) sobre ele. No exemplo abaixo, o imposto NBT de 2% deve ser aplicado sobre a soma do valor dos itens e, em seguida, o imposto de IVA de 15%.  
![](/files/jll9vuX.png)  
No ERPNext, para mapear isso no Pedido de Venda/Fatura na tabela Impostos e Encargos sobre Vendas:1. Selecione o tipo de imposto como **Sobre o total líquido**
2. Selecione ou adicione novo imposto como  **NBT** e defina a alíquota em 2%.
3. Em seguida, adicione uma nova linha e selecione o tipo de imposto como **No total da linha anterior** e selecione ou adicione um novo imposto como **IVA** e defina a alíquota em 15%.

  
![](/files/XHtxDLI.png)  
Expanda a segunda linha e adicione a **Linha de referência #** a 1.  
![](/files/Bh9Vzqp.png)  
Depois de salvar o documento e veja a visualização da impressão, ela terá a seguinte aparência.  
![](/files/O2NF3ri.png)

