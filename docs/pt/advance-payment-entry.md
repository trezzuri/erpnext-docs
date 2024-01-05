# Entrada de pagamento antecipado



**O pagamento feito pelo Cliente/Fornecedor antes do envio da fatura é um Pagamento Antecipado.**


Geralmente, o pagamento antecipado é feito no caso de negócios de alto valor. Considere uma cliente-Jane D'souza fazendo um pedido de um item de mobília de luxo no valor de ₹ 24.000. Ela é solicitada a dar algum adiantamento antes que a casa de móveis comece a trabalhar em seu pedido. Ela dá a eles ₹ 10.000 em dinheiro.


No ERPNext, a entrada de pagamento antecipado é criada usando Entrada de Pagamento. Caso exista um Pedido de Venda, você poderá criar diretamente um Lançamento de Pagamento para o valor do adiantamento. Ou então, você também pode criar uma entrada de pagamento independente para o cliente. Da mesma forma, você também pode criar um Lançamento de Pagamento antecipado para Fornecedor, via Pedido de Compra.


![Entrada de pagamento do pedido de vendas](/files/payment-option-in-sales-order.png)



> 
> Nota: Se o pagamento não estiver vinculado a uma fatura, será considerado um adiantamento. Os adiantamentos são refletidos nos relatórios de Contas a Receber e a Pagar.
> 
> 
> 


## 1. Pré-requisitos


Para criar uma entrada de pagamento antecipado, estes precisam ser criados primeiro:


* Parte (Cliente/Fornecedor)
* Conta de pagamento (conta bancária ou dinheiro)


## 2. Como criar entrada de pagamento antecipado


Depois que um pedido de venda ou pedido de compra for enviado, você encontrará uma opção para criar um pagamento em relação a ele. Você também pode criar um novo lançamento de pagamento e selecionar valores manualmente (como parte e conta de pagamento). Aqui estão as etapas para criar um pagamento antecipado em relação ao pedido de vendas.


1. Acesse Pedido de Venda e clique em **Efetuar > Entrada de Pagamento**.
2. Definir/verificar as contas.
3. Salvar e enviar.


Qualquer Lançamento de Pagamento que não esteja vinculado a uma fatura é considerado como adiantamento pelo sistema ERPNext.


Se o Cliente tiver dado US$ 5.000 como adiantamento em dinheiro, isso será registrado como um
lançamento de crédito contra a conta a receber do cliente. Para equilibrar [de acordo com o Double
sistema de contabilidade], US$ 5.000 são debitados da conta de caixa da Empresa.


### 2.2 Alocação de pagamento antecipado na fatura


Ao criar uma fatura, você pode verificar se há um Adiantamento contra essa Parte.


![Obter pagamentos antecipados na fatura de vendas](/files/fetch-advance-payments-in-invoice.png)


Ao clicar no botão **Obter recebimento antecipado**, serão buscadas as entradas de pagamento antecipado encontradas para aquela parte. Depois que as entradas de pagamento antecipado forem obtidas, você poderá alocar o valor do adiantamento nesta fatura. A alocação reduzirá imediatamente o valor pendente dessa fatura.


Salve e envie a fatura de vendas.


### 3. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Lançamento de diário](/docs/pt/accounts/journal-entry)
3. [Entrada de pagamento](/docs/pt/accounts/payment-entry)



