# Entrada de cheque pós-datado



Cheque pós-datado é um cheque datado em data futura. As partes geralmente dão cheque pós-datado, como adiantamento. Este cheque será compensado somente quando a data do cheque chegar.


No ERPNext, crie Entrada de Pagamento para cheque pós-datado.


#### Nova entrada de pagamento


Para abrir um novo comprovante de diário, acesse


`Explorar > Contabilidade > Entrada de pagamento > Novo`


#### Definir data de postagem


Supondo que a data do seu cheque seja 31 de dezembro de 2016 (ou qualquer data futura). Como resultado, esse lançamento em seu livro-razão bancário aparecerá na Data de lançamento atualizada.


![Data de lançamento na entrada de pagamento](/files/posting-date-in-payment-entry.png)


Observação: a data de referência de lançamento do pagamento deve ser igual ou inferior à data de lançamento.


#### Etapa 3: Salvar e enviar


Depois de inserir os detalhes necessários, salve e envie a entrada de pagamento.


#### Ajuste de entrada de cheque pós-datado


Você pode ajustar a entrada de pagamento pós-datado em relação a uma fatura por meio da [Ferramenta de reconciliação de pagamento](/docs/pt/accounts/payment-reconciliation).


Quando o cheque é compensado, ou seja, na data real do cheque, você pode atualizar sua data de compensação por meio da [Ferramenta de reconciliação bancária](/docs/pt/accounts/bank-reconciliation).


No Plano de Contas, você pode encontrar o valor desta Entrada de Pagamento já refletido na Conta bancária. Você deve verificar o **Extrato de Reconciliação Bancária**, um relatório no módulo de conta para saber a diferença entre o saldo bancário conforme o sistema e o saldo real no extrato bancário.




