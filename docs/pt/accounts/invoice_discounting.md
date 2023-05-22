# Desconto na fatura


**Desconto de fatura é a prática de usar as faturas de vendas não pagas de uma empresa como garantia para um empréstimo de curto prazo, emitido por um banco ou financeira.**


Para acessar a lista de descontos na fatura, acesse:



> 
> Página inicial > Contabilidade > Bancos e pagamentos > Desconto em faturas
> 
> 
> 


## 1. Pré-requisitos


Você precisa criar os seguintes livros contábeis para lançar transações de desconto de fatura.


* **Empréstimo de curto prazo:** um livro-razão sob o grupo 'Passivo atual' > 'Empréstimos (passivo)' para empréstimo.
* **Cobranças de conta bancária:** um livro de despesas para cobranças cobradas pelo banco.
* **Contas a Receber Conta de Crédito:** Uma conta controle do tipo a receber.
* **Conta com desconto de contas a receber:** uma conta a receber para faturas que foram descontadas.
* **Contas a receber não pagas:** uma conta a receber de faturas que foram descontadas e permanecem não pagas mesmo após o término do período do empréstimo.


## 2. Como lançar uma transação de desconto na fatura


1. Vá para a lista de Desconto de Fatura, clique em Novo.
2. Digite a Data de Lançamento e a Data de Início do Empréstimo. Insira o período do empréstimo em dias.
3. Selecione as faturas manualmente na tabela ou clicando no botão 'Obter faturas' no canto superior direito.
4. Selecione Conta de Empréstimo de Curto Prazo, Conta Bancária e Conta de Encargos Bancários.
5. Selecione Contas a receber a crédito, Contas a receber com desconto e Contas a receber não pagas.
6. Clique em Salvar e em Enviar.
7. Depois de enviar o formulário de Desconto de Fatura, clique em **Desembolsar Empréstimo**.


![Desembolsar empréstimo no desconto da fatura](/files/invoice-discounting.png)
8. Você será levado a uma tela de [Entrada de diário](/docs/pt/accounts/journal-entry). Salve e envie a entrada do diário.


![Journal Entry](/files/invoice-discounting-journal-entry.png)


## 2. Recursos


### 2.1 Importar faturas


Clique no botão 'Obter faturas' para importar faturas. Você pode importar faturas filtrando determinados critérios.


* Faturas criadas contra um cliente específico.
* Intervalo de datas entre as quais as faturas foram geradas.
* Valor mínimo e máximo.


Você também pode especificar vários dos filtros acima.


### 2.2 Fechamento do empréstimo


Ao pagar o empréstimo no final do período do empréstimo ou antes disso, você pode atualizar o mesmo clicando no botão 'Fechar empréstimo'.
 ![Journal Entry](/files/invoice-discounting-close-loan.png)
O sistema preparará a entrada do diário. Revise e envie-o.


### 2.3 Atualização automática de livros contábeis no final do período do empréstimo


Se o empréstimo não for reembolsado no final do período do empréstimo, o sistema criará um lançamento contábil por meio de um trabalho agendado para mudar o valor de 'Contas a receber com desconto' para 'Contas a receber não pagas'. Isso facilitará o rastreamento das faturas que foram descontadas e não foram pagas no final do período do empréstimo.

