# Entrada de cheque pós-datado


Cheque pós-datado é um cheque datado em data futura. A parte geralmente dá cheque pré-datado, como pagamento antecipado. Este cheque seria compensado somente quando a data do cheque chegasse.


No ERPNext, crie Entrada de Pagamento para cheque pré-datado.


#### Nova Entrada de Pagamento


Para abrir um novo comprovante de diário, vá para


`Explorar > Contabilidade > Entrada de pagamento > Novo`


#### Definir data de postagem


Supondo que a data do seu cheque seja 31 de dezembro de 2016 (ou qualquer data futura). Como resultado, esta postagem em seu livro-caixa aparecerá na data de lançamento atualizada.


![Data de lançamento na entrada de pagamento](/files/posting-date-in-payment-entry.png)


Observação: a Data de Referência de Entrada de Pagamento deve ser igual ou inferior à Data de Lançamento.


#### Etapa 3: salvar e enviar


Depois de inserir os detalhes necessários, salve e envie a entrada de pagamento.


#### Ajuste de entrada de cheque pós-datado


Você pode ajustar a entrada de pagamento pós-datado em relação a uma fatura por meio da [Ferramenta de reconciliação de pagamento](/docs/v13/user/manual/en/accounts/payment-reconciliation).


Quando o cheque é compensado, ou seja, na data real do cheque, você pode atualizar sua Data de Compensação por meio da [Ferramenta de Reconciliação Bancária](/docs/v13/user/manual/en/accounts/bank-reconciliation).


No Plano de Contas, você pode encontrar o valor desta Entrada de Pagamento já refletindo na Conta Bancária. Você deve verificar o **Extrato de reconciliação bancária**, um relatório no módulo de conta para saber a diferença do saldo bancário conforme o sistema e o saldo real no extrato do banco.