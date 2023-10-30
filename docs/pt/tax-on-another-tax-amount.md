# Imposto sobre outro valor de imposto



**Caso de uso:** Necessidade de calcular o imposto sobre o valor do imposto anterior e não sobre o valor do item.   
Por exemplo, temos 5 itens e a Taxa de Serviço é calculada sobre o Total Líquido dos 5 itens. Adicionalmente, necessitamos de calcular 5% de IVA sobre a Taxa de Serviço dos Artigos e não sobre o Total Líquido da Factura. Neste caso, você precisa seguir os seguintes passos:  
1) Na fatura de vendas, na seção **Impostos e encargos sobre vendas**  você precisa definir o cálculo do imposto. Na linha 1, selecione o Tipo como **"Total Líquido"** e o Cabeçalho da Conta conforme necessário. Insira a Taxa se ainda não estiver definida.O valor para esse cabeçalho de conta específico é calculado na coluna Valor.  
2) Próximo , será necessário calcular o imposto sobre o valor da linha anterior (que é o valor do imposto). Para fazer isso, selecione o Tipo como **"Valor da linha anterior".** Defina o cabeçalho e a taxa da conta conforme necessário. Expanda a linha e defina o **número da linha de referência** conforme mostrado abaixo.  
![](/files/pOxAhCQ.png)  
  
O conjunto de seções de Impostos e Taxas sobre Vendas é o seguinte:  
![](/files/BkuU2h9.png)

