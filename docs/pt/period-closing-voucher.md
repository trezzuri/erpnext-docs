# Voucher de encerramento do período



**Um comprovante de encerramento do período indica que o lucro/perda de um período contábil foi equilibrado e os livros podem começar do zero.**


No final de cada ano ou (trimestralmente ou talvez até mensalmente), após concluir a auditoria, você pode encerrar seus livros contábeis. Isso significa que você faz todas as suas entradas especiais como:


* Depreciação
* Mudança no valor dos ativos
* Diferir impostos e obrigações
* Atualizar dívidas inadimplentes


Em seguida, registre seu lucro ou perda.


Ao fazer isso, seu saldo em suas contas de receitas e despesas se torna zero. Você inicia um novo ano fiscal (ou período) com um balanço patrimonial equilibrado e uma nova conta de lucros e perdas. No ERPNext depois de fazer todos os lançamentos especiais via Lançamento Contábil para o ano fiscal atual, você deve zerar todas as suas contas de Receitas e Despesas através de um Voucher de Encerramento de Período.


Para acessar a lista de Vouchers de Encerramento do Período, acesse:



> 
> Home > Contabilidade > Abertura e Fechamento > Voucher de Encerramento de Período
> 
> 
> 


## 1. Como criar um Voucher de Encerramento de Período


1. Vá para a lista de vouchers de encerramento do período e clique em Novo.
2. Defina uma data de postagem.
3. Selecione a conta, geralmente esta é a conta 'Reservas e Excedentes'.
4. Insira comentários.
5. Salvar e enviar.
![Voucher de encerramento do período](/files/period-closing-voucher.png)


### 1.2 Os campos explicados


* **Data da Transação** será a data de criação do Voucher de Encerramento do Período.
* **Data de Postagem** será quando esta entrada deverá ser executada. Se o seu Ano Fiscal terminar em 31 de dezembro, essa data deverá ser selecionada como Data de Lançamento no Voucher de Encerramento do Período.
* **Encerramento do Ano Fiscal** será um ano para o qual você está encerrando suas demonstrações financeiras.
* **Registrar Lucro/Perda Wise do Centro de Custo** registrará lançamentos de fechamento de acordo com o centro de custo dos lançamentos contábeis de receitas e despesas


### 1.3 O que acontece no envio?


O Comprovante de Fechamento de Período fará lançamentos contábeis (Lançamento Contábil). Isso zerará todas as suas contas de receitas e despesas e transferirá o saldo de lucros/perdas para a conta de encerramento.


Você deve selecionar uma conta de passivo como Reservas e Excedentes, ou Qualquer conta de Reserva de Receita ou na conta de Capital do Proprietário como Conta de Encerramento.


![Ledger de voucher de encerramento do período](/files/period-closing-voucher-ledger.png)


Se **Reservar lucro/perda inteligente do centro de custo** estiver ativado, o lucro e a perda líquidos serão contabilizados de acordo com o centro de custo da transação individual. Abaixo está o lançamento de fechamento feito para duas transações de vendas com centros de custo diferentes.


![Voucher de encerramento do período baseado no centro de custo](/files/cost-center-wise-period-closing-voucher.png)



> 
> **Observação:** Se os lançamentos contábeis forem feitos em um exercício fiscal de encerramento, mesmo após a criação do comprovante de encerramento do período para esse ano fiscal, você deverá criar outro comprovante de encerramento do período. O voucher posterior apenas transferirá o saldo de lucros e perdas pendente para o chefe da conta de encerramento.
> 
> 
> 


### 2. Tópicos Relacionados


1. [Ano fiscal](/docs/pt/accounts/fiscal-year)
2. [Categoria de retenção de imposto](/docs/pt/accounts/tax-withholding-category)
3. [Período contábil](/docs/pt/accounts/accounting-period)



