# Desconto na fatura


**Desconto de fatura é a prática de usar as faturas de vendas não pagas de uma empresa como garantia para um empréstimo de curto prazo, que é emitido por um banco ou financeira.**


Para acessar a lista de descontos da Nota Fiscal, acesse:



>
> Home > Contabilidade > Banca e Pagamentos > Desconto de Facturas
>
>
>


## 1. Pré-requisitos


Você precisa criar os seguintes livros contábeis para lançar transações de desconto de fatura.


* **Empréstimo de curto prazo:** Um livro-razão sob o grupo 'Passivo atual' > 'Empréstimos (passivo)' para empréstimo.
* **Cobranças de conta bancária:** um livro-razão de despesas para taxas cobradas pelo banco.
* **Conta de Crédito de Contas a Receber:** Uma conta controle do tipo recebível.
* **Conta de contas a receber com desconto:** Uma conta a receber para faturas que foram descontadas.
* **Conta de Contas a Receber Não Paga:** Conta a receber de faturas que foram descontadas e permanecem não pagas mesmo após o término do período do empréstimo.


## 2. Como Lançar uma Transação de Desconto de Fatura


1. Acesse a lista Desconto de Faturas, clique em Novo.
2. Insira a Data de Lançamento e a Data de Início do Empréstimo. Insira o Período do Empréstimo em dias.
3. Selecione as faturas manualmente na tabela ou clicando no botão 'Obter faturas' no canto superior direito.
4. Selecione Conta de Empréstimo de Curto Prazo, Conta Bancária e Conta de Encargos Bancários.
5. Selecione Contas a receber a crédito, Contas a receber com desconto e Contas a receber por pagar.
6. Clique em Salvar e em Enviar.
7. Após enviar o formulário de Desconto de Nota Fiscal, clique em **Desembolsar Empréstimo**.


![Desembolsar empréstimo no desconto da fatura](/files/invoice-discounting.png)
8. Você será levado para a tela [Entrada de diário](/docs/v13/user/manual/en/accounts/entrada de diário). Salve e envie a entrada de diário.


![Entrada de diário](/files/invoice-discounting-journal-entry.png)


## 2. Características


### 2.1 Faturas de Importação


Clique no botão 'Obter faturas' para importar faturas. Você pode importar faturas filtrando por determinados critérios.


* Faturas criadas contra um cliente específico.
* Intervalo de datas entre as quais as faturas foram levantadas.
* Valor mínimo e máximo.


Você também pode especificar vários dos filtros acima.


### 2.2 Fechamento do Empréstimo


Ao pagar o empréstimo no final do período do empréstimo ou antes disso, você pode atualizar o mesmo clicando no botão 'Fechar empréstimo'.
 ![Entrada de diário](/files/invoice-discounting-close-loan.png)
O sistema preparará a entrada do diário. Revise e envie-o.


### 2.3 Atualização Automática de Razões no final do Período do Empréstimo


Se o empréstimo não for reembolsado no final do período do empréstimo, o sistema criará um Lançamento Diário por meio de um trabalho agendado para mudar o valor de 'Contas a Receber com Desconto' para 'Contas a Receber Não Pagas'. Isso facilitará o rastreamento das faturas que foram descontadas e não foram pagas ao final do período do empréstimo.