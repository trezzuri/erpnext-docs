# Aplicar imposto sobre outro imposto ou cobrança


Considere que um cliente em potencial deseja aplicar imposto sobre um imposto. Vamos pegar um exemplo de imposto (NBT) que deve ser aplicado sobre o valor líquido total dos itens e depois aplicar outro imposto (IVA) sobre ele. No exemplo abaixo, o imposto NBT 2% deve ser aplicado sobre a soma do valor dos itens e, em seguida, o imposto IVA 15%.
![](/files/jll9vuX.png)
No ERPNext, para mapear isso no Pedido de Venda/Fatura na tabela de Impostos e Encargos sobre Vendas:1. Selecione o tipo de imposto como **On Net Total**
2. Selecione ou adicione um novo imposto como **NBT** e defina a taxa em 2%.
3. Em seguida, adicione uma nova linha e selecione o tipo de imposto como **No total da linha anterior** e selecione ou adicione um novo imposto como **IVA** e defina a taxa em 15%.

  
![](/files/XHtxDLI.png)
Expanda a 2ª linha e adicione a **Reference Row #** a 1.
![](/files/Bh9Vzqp.png)
Depois de salvar o documento e visualizar a visualização da impressão, ele terá a seguinte aparência.
![](/files/O2NF3ri.png)