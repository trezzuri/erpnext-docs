# Desconto de livro permitido e recebido separadamente


Os descontos fazem parte do dia a dia das empresas. Um desconto permitido é quando o fornecedor de bens ou serviços concede um desconto de pagamento a um cliente. Por outro lado, um desconto recebido é a situação inversa, em que o cliente recebe um desconto do fornecedor.

  


Quando você é um fornecedor e concede um desconto ao seu cliente, isso é tratado como uma espécie de Despesa, enquanto que, se você receber um desconto do seu fornecedor, é considerado uma receita.

  


No ERPNext, o desconto concedido ou recebido não é contabilizado separadamente. Normalmente, é o valor final da fatura (após o desconto) que é contabilizado. No entanto, se você deseja reservar os descontos separadamente, siga as etapas abaixo:

  


1) "Desconto Permitido" é um tipo de Despesa e "Desconto Recebido" é um tipo de Receita. Portanto, primeiro crie essas duas contas no Plano de Contas.

  


![](/files/tE7sKIX.png)

  


  


2) Crie uma fatura, selecione o item. Agora, na tabela "Impostos e encargos sobre vendas/compras", selecione o título da conta de desconto, dependendo da transação, e insira a taxa de desconto como um valor negativo.

  


Por exemplo, se estamos a criar uma Nota Fiscal de Venda e estamos a dar um desconto de 10% ao cliente, o desconto de 10% é registado numa conta separada "Desconto Permitido". Verifique a captura de tela abaixo para entender o mesmo.

  


![](/files/8QtX0DE.jpe)

  


Conforme visto na captura de tela acima, o valor total da fatura sem desconto é de Rs. 350. Ao aplicar 10% de desconto, o valor total da fatura agora cai para Rs. 315. O valor do desconto de Rs. 35 é registrado na conta Desconto permitido, que é um tipo de despesa para o fornecedor. Verifique a captura de tela abaixo para entender como as contas são registradas.

  


  


![](/files/IMAGE 2020-11-18 11:45:41.jpg)

3) Prossiga para fazer o pagamento final via Entrada de Pagamento, conforme mostrado nas capturas de tela abaixo:

  


![](/files/18fssIO.png)

  


![](/files/rDzKNPb.png)

  


**Observação:** O mesmo processo pode ser seguido ao criar uma fatura de compra. Porém neste caso, a conta selecionada na tabela Impostos e Encargos de Compras será "Desconto Recebido" que será uma conta de receita.