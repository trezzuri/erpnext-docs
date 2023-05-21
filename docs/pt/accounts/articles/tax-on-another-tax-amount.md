# Imposto sobre outro valor de imposto


**Caso de uso:** É necessário calcular o imposto sobre o valor do imposto anterior e não sobre o valor do item.
Por exemplo, temos 5 itens e a Taxa de Serviço é calculada sobre o Total Líquido dos 5 itens. Além disso, precisamos calcular IVA de 5% sobre a Taxa de Serviço dos Itens e não sobre o Total Líquido da Fatura. Neste caso, você precisa seguir os seguintes passos:
1) Em Fatura de vendas, na seção **Taxas e encargos sobre vendas**, você precisa definir o cálculo do imposto. Na linha 1, selecione o Tipo como **"Total Líquido"** e Cabeçalho da Conta conforme necessário. Insira a Taxa, se ainda não estiver definida. O valor para este cabeçalho de conta específico é calculado na coluna Valor.
2) Em seguida, você precisa calcular o imposto sobre o valor da linha anterior (que é o valor do imposto). Para fazer isso, selecione o Tipo como **"No valor da linha anterior".** Defina o Cabeçalho da conta e a Taxa conforme necessário. Expanda a linha e defina a **Reference Row #** conforme mostrado abaixo.
![](/files/pOxAhCQ.png)
  
O conjunto de seções de Impostos e Encargos sobre Vendas tem a seguinte aparência:
![](/files/BkuU2h9.png)