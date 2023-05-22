# Imposto sobre outro valor de imposto


**Caso de uso:** Necessidade de calcular o imposto sobre o valor do imposto anterior e não sobre o valor do item.   
Por exemplo, temos 5 itens e a Taxa de Serviço é calculada sobre o Total Líquido dos 5 itens. Além disso, precisamos calcular IVA de 5% sobre a Taxa de Serviço dos Itens e não sobre o Total Líquido da Fatura. Neste caso, você precisa seguir os seguintes passos:  
1) Em Fatura de Venda, na seção **Taxas e Cobranças de Vendas**  você precisa definir o cálculo do imposto. Na linha 1, selecione o Tipo como **"No total líquido"** e Cabeçalho da conta, conforme necessário. Insira a Taxa se ainda não tiver definido.O valor para esta cabeça de conta específica é calculado na coluna Valor.  
2) Próximo , você precisa calcular o imposto sobre o valor da linha anterior (que é o valor do imposto). Para fazer isso, selecione o Tipo como **"No valor da linha anterior".** Defina o cabeçalho e a taxa da conta conforme necessário. Expanda a linha e defina a **Reference Row #** conforme mostrado abaixo.  
![](/files/pOxAhCQ.png)  
  
O conjunto de seções de impostos e cobranças sobre vendas é o seguinte:< br/>![](/files/BkuU2h9.png)