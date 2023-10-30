# Desconto de livro permitido e recebido separadamente



Os descontos fazem parte do dia a dia dos negócios. Um desconto permitido é quando o fornecedor de bens ou serviços concede um desconto no pagamento a um cliente. Por outro lado, o desconto recebido é a situação inversa, onde o cliente recebe um desconto do fornecedor. 

  


Quando você é um fornecedor , e você conceder um desconto ao seu cliente, isso é tratado como uma espécie de Despesa, enquanto, se você receber um desconto do seu fornecedor, é considerado uma receita. 

  


No ERPNext, o desconto permitido ou recebido não é contabilizado separadamente. Normalmente é o valor final da fatura (após discount) que é reservado. Porém, se desejar reservar os descontos separadamente, você pode seguir os passos abaixo:

  


1) "Desconto Permitido" é um tipo de Despesa e "Desconto Recebido" é um tipo de Receita. Portanto, primeiro crie essas duas contas no Plano de Contas. 

  


![](/files/tE7sKIX.png)

  
  


2) Crie uma fatura, selecione o item. Agora, na tabela "Impostos e encargos sobre vendas/compra", selecione o cabeçalho da conta de desconto dependendo da transação e insira a taxa de desconto como um valor negativo. 

  


Por exemplo, se estivermos criando uma fatura de venda e estivermos dando um desconto de 10% ao cliente, o desconto de 10% é reservado em um conta separada com "Desconto permitido". Verifique a captura de tela abaixo para entender o mesmo.

  


![](/files/8QtX0DE.jpe)

  


Conforme visto na imagem acima, o valor total da fatura sem desconto é de Rs. 350. Ao aplicar o desconto de 10%, o valor total da fatura passa a ser de Rs. 315. O valor do desconto de Rs. 35 é contabilizado na conta Desconto Permitido, que é uma espécie de despesa do fornecedor. Verifique a captura de tela abaixo para entender como as contas são reservadas.

  


  


![](/files/IMAGE 2020-11-18 11:45:41.jpg)

3) Proceda ao pagamento final via Entrada de Pagamento conforme mostrado nas capturas de tela abaixo:

  
![](/files/18fssIO.png)

  


![](/files/rDzKNPb.png)

  


**Nota:** O mesmo processo pode ser seguido ao criar uma fatura de compra. Porém, neste caso, a conta selecionada na tabela Impostos e Encargos de Compra será "Desconto Recebido", que será uma conta de receita.

  








