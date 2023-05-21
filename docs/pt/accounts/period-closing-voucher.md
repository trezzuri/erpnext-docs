# Voucher de Encerramento de Período


**Um comprovante de encerramento do período indica que o lucro/prejuízo de um período contábil foi equilibrado e os livros podem começar do zero.**


No final de cada ano ou (trimestralmente ou talvez até mensalmente), após a conclusão da auditoria, você pode fechar seus livros de contas. Isso significa que você faz todas as suas entradas especiais como:


* Depreciação
* Alteração no valor dos Ativos
* Adiar impostos e passivos
* Atualizar dívidas incobráveis


Em seguida, reserve seu Lucro ou Perda.


Ao fazer isso, seu saldo em suas contas de receitas e despesas torna-se zero. Você inicia um novo ano fiscal (ou período) com um balanço patrimonial equilibrado e uma nova conta de lucros e perdas. No ERPNext após realizar todos os lançamentos especiais via Lançamento Diário do exercício corrente, você deverá zerar todas as suas contas de Receitas e Despesas através de um Comprovante de Encerramento do Período.


Para acessar a lista de Vouchers de Encerramento de Período, acesse:



>
> Home > Contabilidade > Abertura e Encerramento > Voucher de Encerramento de Período
>
>
>


## 1. Como criar um Voucher de Encerramento de Período


1. Acesse a lista Comprovante de Encerramento do Período e clique em Novo.
2. Defina uma data de postagem.
3. Selecione a conta, geralmente é a conta 'Reservas e Excedentes'.
4. Insira quaisquer observações.
5. Salve e envie.
![Comprovante de fechamento de período](/files/period-closing-voucher.png)


### 1.2 Os campos explicados


* **Data da Transação** será a data de criação do Voucher de Fechamento do Período.
* **Data de postagem** será quando esta entrada deve ser executada. Se o seu ano fiscal terminar em 31 de dezembro, essa data deverá ser selecionada como Data de lançamento no comprovante de encerramento do período.
* **Fechamento do ano fiscal** será um ano para o qual você está fechando sua demonstração financeira.
* **Liberar lucros/perdas sábios do centro de custo** registrará os lançamentos de fechamento de acordo com o centro de custo dos lançamentos contábeis de receitas e despesas


### 1.3 O que acontece na submissão?


O Comprovante de Encerramento do Período fará os lançamentos contábeis (Entrada Contábil). Isso zerará todas as suas contas de receitas e despesas e transferirá o saldo de lucros/perdas para a conta de encerramento.


Você deve selecionar uma conta de passivo como Reservas e Excedentes, ou Qualquer conta de Reserva de Receita ou na conta de Capital do Proprietário como Conta de Fechamento.


![Registro de comprovante de fechamento de período](/files/period-closing-voucher-ledger.png)


Se **Liberar lucro/perda sábio do centro de custo** estiver ativado, o lucro e perda líquidos serão contabilizados de acordo com o centro de custo da transação individual. Abaixo está o lançamento final feito para duas transações de vendas com centros de custo diferentes.


![Comprovante de fechamento do período por centro de custo](/files/cost-center-wise-period-closing-voucher.png)



>
> **Observação:** Se os lançamentos contábeis forem feitos em um ano fiscal de encerramento, mesmo após a criação do comprovante de encerramento do período para esse ano fiscal, você deverá criar outro comprovante de encerramento do período. O comprovante posterior transferirá apenas o saldo de P&L pendente para o Cabeçalho da conta de fechamento.
>
>
>


### 2. Tópicos Relacionados


1. [Ano Fiscal](/docs/v13/user/manual/en/accounts/ano-fiscal)
2. [Categoria de retenção de impostos](/docs/v13/user/manual/en/accounts/tax-withholding-category)
3. [Período contábil](/docs/v13/user/manual/en/accounts/período contábil)