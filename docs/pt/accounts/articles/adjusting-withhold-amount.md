# Ajustando o valor retido


Vamos supor que o saldo pendente de uma fatura de venda seja de 20.000. Quando o cliente fizer o pagamento, ele pagará apenas 19.600. O restante 400 precisa ser registrado na conta de retenção de impostos. Você pode gerenciar esse cenário conforme descrito abaixo.


## Etapa 1: configurar conta retida


[Crie uma conta retida](/docs/v13/user/manual/en/accounts/chart-of-accounts#1-how-to-createedit-accounts) em seu plano de contas.


## Etapa 2: entrada de pagamento


Para criar Entrada de Pagamento, vá para Fatura de Venda não paga e clique no botão Efetuar Pagamento.


### Etapa 2.1: Insira o valor do pagamento


Digite o valor do pagamento como 19.600.


![Valor pago na entrada de pagamento](/files/paid-amount-in-payment-entry.png)


### Passo 2.2: Alocar Contra Fatura de Vendas


Contra a fatura de vendas, aloque 20.000 (explicado no GIF abaixo).


### Etapa 2.3: adicionar conta de dedução/perda


Você pode notar que há uma diferença de 400 no Valor do Pagamento e no Valor Alocado contra a Nota Fiscal de Venda. Você pode reservar essa conta de diferença em Conta Retida.


![Ajuste de imposto retido na entrada de pagamento](/files/tax-withheld-adjustment-in-payment-entry.gif)


Seguindo as mesmas etapas, você também pode gerenciar a diferença aproveitada devido a ganhos/perdas de câmbio.