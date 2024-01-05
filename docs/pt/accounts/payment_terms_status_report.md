# Relatório de status das condições de pagamento



### Relatório de status das condições de pagamento


Relatório para calcular o status das condições de pagamento com base nas faturas criadas para esse pedido de vendas. O valor da fatura é dividido nas respectivas condições de pagamento em tempo de execução usando o método FIFO.
![](/files/payment term status.png)


##### Exemplo:


Considere um pedido de venda com valor total de 7.000$ e condições de pagamento de 50-50.
![](/files/Screenshot 2022-01-04 às 18h33.53.png)


Se uma fatura de vendas for feita em relação a esse SO no valor de 4.900$.
![](/files/pagamento termos fatura.png)


Em seguida, o relatório dividirá o valor da fatura em condições de pagamento no método FIFO e exibirá os status como 'Concluído' para os primeiros 50% e 'Parcialmente Pago' para os segundos 50%.
![](/files/Screenshot 2022-01-04 às 18h27.56.png)



