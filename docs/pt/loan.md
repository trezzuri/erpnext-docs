# Empréstimo



**Depois que o pedido de empréstimo for aprovado pelo gerente, um registro de empréstimo e um cronograma de reembolso poderão ser criados para o solicitante usando o empréstimo.**

Para acessar o empréstimo, vá para:

> Recursos Humanos > Empréstimos > Empréstimo

## 1. Pré-requisitos

Antes de criar um registro de Empréstimo, é necessário que você crie os seguintes documentos:

* [Tipo de empréstimo](/docs/pt/human-resources/loan-type)
* [Solicitação de empréstimo](/docs/pt/human-resources/loan-application)
* [Plano de contas](https://docs.erpnext.com/docs/pt/accounts/chart-of-accounts)

## 2. Como criar um registro de empréstimo

1. Acesse: Empréstimo > Novo.
2. Selecione o nome do solicitante.
3. Selecione o pedido de empréstimo. Depois de selecionado, serão obtidas informações do empréstimo, como tipo de empréstimo, valor do empréstimo, taxa de juros, método de reembolso, período de reembolso em meses e valor de reembolso mensal.
4. Insira a data de início do reembolso .

![Loan](/files/loan1.png)
5. Insira as informações da conta, como forma de pagamento, Conta de Pagamento, Conta de Empréstimo e Conta de Receita de Juros.
6. Economizar. Depois de salvo, um Cronograma de Reembolso é gerado automaticamente. A data de pagamento do primeiro reembolso seria definida de acordo com a "Data de início do reembolso". O

![Cronograma de Reembolso](/files/loan2.png)

> Observação: marque "Reembolsar de Salário" se o reembolso do empréstimo for deduzido do salário

Como alternativa, você pode criar um registro de Empréstimo diretamente em [Solicitação de empréstimo](/docs/pt/human-resources/loan-application)

## 3. Características

### 3.1 Criação de Lançamento de Desembolso

Após enviar o documento do Empréstimo, se o status for "Sancionado", você pode clicar em "Criar Lançamento de Desembolso" para criar um Lançamento Contábil do Empréstimo.

![Disbursement Entry](/files/disbursement-entry.png)

### 3.2 Dedução do reembolso do empréstimo do salário

Para deduzir automaticamente o reembolso do empréstimo do salário, marque "Reembolsar do salário" em Empréstimo. Ele aparecerá como Reembolso de empréstimo no recibo de salário.

![Salary Slip](/files/salary-slip-loan.png)

### 3.3 Estendendo o Empréstimo

O valor do empréstimo é deduzido do salário. Caso o funcionário esteja afastado sem remuneração por algum período, o empréstimo existente poderá ser prorrogado sem a necessidade de criação de um novo empréstimo. Isso pode ser feito editando a tabela Cronograma de Reembolso mesmo após o envio do empréstimo.

![Extending Loan](/files/change-loan-amount.gif)

## 4. Tópicos relacionados

1. [Entrada de diário](https://docs.erpnext.com/docs/pt/accounts/journal-entry)
2. [Lançamento da folha de pagamento](https://docs.erpnext.com/docs/pt/accounts/payment-entry)


