# Relatório de status das condições de pagamento


### Relatório de status das condições de pagamento


Relatório para calcular o status das condições de pagamento com base nas faturas criadas para esse pedido de venda. O valor da fatura é dividido nas respectivas condições de pagamento no tempo de execução usando o método FIFO.
![](/files/condições de pagamento status.png)


##### Exemplo:


Considere um pedido de venda com valor total de 7.000₹ e condições de pagamento de 50-50.
![](/files/Captura de tela 2022-01-04 às 6.33.53 PM.png)


Se uma fatura de venda for feita contra esse SO por 4900₹.
![](/arquivos/condições de pagamento fatura.png)


Em seguida, o relatório dividirá o valor da fatura em condições de pagamento no método FIFO e exibirá os status como 'Concluído' para os primeiros 50% e 'Pago Parcialmente' para os segundos 50%.
![](/files/Captura de tela 2022-01-04 às 6.27.56 PM.png)