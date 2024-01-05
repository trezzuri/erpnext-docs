# Desconto na fatura



**Desconto de fatura é a prática de usar faturas de vendas não pagas de uma empresa como garantia para um empréstimo de curto prazo, emitido por um banco ou empresa financeira.**


Para acessar a lista de descontos da fatura, acesse:



> 
> Home > Contabilidade > Bancos e Pagamentos > Desconto em faturas
> 
> 
> 


## 1. Pré-requisitos


Você precisa criar os seguintes livros-razão para lançar transações de desconto de fatura.


* **Empréstimo de curto prazo:** um livro-razão no grupo 'Passivo Circulante' > 'Empréstimos (Passivos)' para empréstimos.
* **Cobranças de contas bancárias:** um livro de despesas para cobranças cobradas pelo banco.
* **Conta de crédito de contas a receber:** uma conta de controle do tipo a receber.
* **Conta com desconto de contas a receber:** uma conta a receber para faturas que foram descontadas.
* **Conta não paga de contas a receber:** uma conta a receber para faturas que foram descontadas e permanecem não pagas mesmo após o término do período do empréstimo.


## 2. Como lançar uma transação com desconto na fatura


1. Vá para a lista Desconto na fatura e clique em Novo.
2. Insira a data de lançamento e a data de início do empréstimo. Insira o período do empréstimo em dias.
3. Selecione as faturas manualmente na tabela ou clicando no botão "Obter faturas" no canto superior direito.
4. Selecione Conta de Empréstimo de Curto Prazo, Conta Bancária e Conta de Encargos Bancários.
5. Selecione Conta de crédito de contas a receber, conta com desconto de contas a receber e conta não paga de contas a receber.
6. Clique em Salvar e em Enviar.
7. Após enviar o formulário de desconto na fatura, clique em **Desembolsar empréstimo**.


![Desembolsar empréstimo com desconto na fatura](/files/invoice-discounting.png)
8. Você será direcionado para uma tela de [Lançamento de diário](/docs/pt/accounts/journal-entry). Salve e envie o lançamento contábil manual.


![Lançamento diário](/files/invoice-discounting-journal-entry.png)


## 2. Recursos


### 2.1 Importar faturas


Clique no botão 'Obter faturas' para importar faturas. Você pode importar faturas filtrando determinados critérios.


* Faturas criadas para um cliente específico.
* Período entre o qual as faturas foram geradas.
* Valor mínimo e máximo.


Você também pode especificar vários dos filtros acima.


### 2.2 Fechando o empréstimo


Quando você reembolsar o empréstimo no final do período do empréstimo ou antes disso, você pode atualizá-lo clicando no botão 'Fechar Empréstimo'.
 ![Lançamento diário](/files/invoice-discounting-close-loan.png)
O sistema preparará o lançamento contábil manual. Revise e envie.


### 2.3 Atualização automática de livros contábeis no final do período do empréstimo


Se o empréstimo não for reembolsado no final do período do empréstimo, o sistema criará um lançamento contábil manual por meio de um trabalho agendado para mudar o valor de 'Conta com desconto de contas a receber' para 'Conta de contas a receber não paga'. Isso facilitará o rastreamento das faturas que foram descontadas e não foram pagas no final do período do empréstimo.



