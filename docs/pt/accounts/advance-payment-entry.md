# Entrada de Pagamento Antecipado


**O pagamento feito pelo Cliente/Fornecedor antes do envio da fatura é um Pagamento Antecipado.**


Geralmente, o pagamento antecipado é feito no caso de negócios de alto valor. Considere uma cliente - Jane D'souza fazendo um pedido de um item de mobília de luxo no valor de ₹ 24.000. Ela é solicitada a dar algum adiantamento antes que a casa de móveis comece a trabalhar em seu pedido. Ela dá a eles ₹ 10.000 em dinheiro.


No ERPNext, o lançamento de adiantamento é criado através de Entrada de Pagamento. Se existir um Pedido de Venda, você pode criar diretamente uma Entrada de Pagamento para o valor do adiantamento. Ou então, você também pode criar uma entrada de pagamento autônoma para o cliente. Da mesma forma, também é possível criar Entrada de Pagamento Antecipado para Fornecedor, via Pedido de Compra.


![Entrada de pagamento do pedido de venda](/files/payment-option-in-sales-order.png)



>
> Nota: Se o pagamento não estiver vinculado a uma fatura, é considerado um adiantamento. Os adiantamentos são refletidos nos relatórios de Contas a Receber e a Pagar.
>
>
>


## 1. Pré-requisitos


Para criar uma entrada de pagamento adiantado, eles precisam ser criados primeiro:


* Parte (Cliente/Fornecedor)
* Conta de Pagamento (Banco ou Conta de Dinheiro)


## 2. Como criar Entrada de Pagamento Antecipado


Depois que um pedido de venda ou pedido de compra for enviado, você encontrará uma opção para criar um pagamento contra ele. Você também pode criar uma nova Entrada de Pagamento e selecionar valores manualmente (como Parte e conta de pagamento). Aqui estão as etapas para criar o Pagamento Antecipado contra o Pedido de Vendas.


1. Vá para Pedido de venda e clique em **Efetuar > Entrada de pagamento**.
2. Defina/verifique as contas.
3. Salve e envie.


Qualquer Entrada de Pagamento que não esteja vinculada a uma Nota Fiscal é considerada como adiantamento pelo sistema ERPNext.


Se o Cliente tiver dado US$ 5.000 como adiantamento em dinheiro, isso será registrado como um
entrada de crédito contra a conta a receber do cliente. Para equilibrá-lo [conforme o Duplo
sistema de contabilidade], $ 5.000 são debitados da conta de caixa da Empresa.


### 2.2 Alocação de Adiantamento em Fatura


Ao criar uma fatura, você pode verificar se há um pagamento antecipado contra essa parte.


![Buscar pagamentos antecipados na fatura de vendas](/files/fetch-advance-payments-in-invoice.png)


Ao clicar no botão **Obter adiantamento recebido**, ele buscará as Entradas de adiantamento de pagamento encontradas para aquela parte. Depois que as entradas de pagamento antecipado forem obtidas, você poderá alocar o valor do adiantamento contra esta fatura. A alocação reduzirá imediatamente o Valor pendente dessa fatura.


Salve e envie a Fatura de Venda.


### 3. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Entrada de diário](/docs/v13/user/manual/en/accounts/journal-entry)
3. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)