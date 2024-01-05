# Empréstimo



> Introduzido na versão 13


**O registro do empréstimo é a conta do empréstimo que contém todas as informações relacionadas a um empréstimo.**


O registro do empréstimo atua como uma conta de empréstimo que contém todos os detalhes do solicitante, cronograma de reembolso e informações de reembolso. Todos os documentos relacionados a empréstimos, como [Desembolso de empréstimo](/docs/pt/loan-management/loan-disbursement), [Reembolso de empréstimo](/docs/pt/loan-management/loan-repayment), etc. estão vinculados a um empréstimo.


Para acessar a lista da Lista de Empréstimos, acesse:
> Home > Gestão de Empréstimos > Empréstimo > Empréstimo


## 1. Pré-requisitos


Antes de criar e usar um empréstimo, é aconselhável que você crie primeiro o seguinte:


* [Tipo de título de empréstimo](/docs/pt/loan-management/loan-security-type)
* [Segurança de empréstimo](/docs/pt/loan-management/loan-security)
* [Tipo de empréstimo](/docs/pt/loan-management/loan-type)
* [Solicitação de empréstimo](/docs/pt/loan-management/loan-application)
* [Compromisso de segurança de empréstimo](/docs/pt/loan-management/loan-security-pledge)


## 2. Como criar um empréstimo


1. Vá para a lista de empréstimos e clique em Novo.
2. Selecione o tipo de candidato.
3. Selecione o candidato.
4. Selecione Solicitação de Empréstimo se a Solicitação de Empréstimo for criada para esse Solicitante. Todos os detalhes do pedido de empréstimo serão obtidos automaticamente no registro do Empréstimo.
5. Selecione a empresa.
6. Insira a data de postagem.
7. Se o tipo de candidato for Funcionário, marque "Reembolsar com salário" se o empréstimo for reembolsado com salário.


![Fazer empréstimo](/files/loan-details.png)
8. Insira o tipo de empréstimo. Todas as contas de empréstimo, modo de pagamento e outros detalhes do empréstimo, como se o empréstimo é um empréstimo a prazo ou à vista, serão obtidos automaticamente do mestre de tipos de empréstimo. Se o empréstimo for a prazo, o cronograma de reembolso do empréstimo será gerado automaticamente ao salvar o documento do empréstimo.


![Fazer empréstimo](/files/loan-accounts.png)
![Fazer empréstimo](/files/loan-repayment-schedule.png)
9. Marque 'É Empréstimo Garantido' se o empréstimo for garantido. Selecione também 'Compromisso de garantia de empréstimo' se o empréstimo for garantido.
10. Clique em "Salvar" para salvar o rascunho do empréstimo.
11. Clique em "Enviar" para enviar o compromisso de garantia do empréstimo.
12. Assim que o empréstimo for enviado, o valor do empréstimo estará pronto para ser desembolsado.


### 2.1. Outras maneiras de criar um empréstimo


Você também pode criar um empréstimo a partir de um pedido de empréstimo aprovado através do botão **Criar** no canto superior direito.


![Solicitação de empréstimo](/files/create-loan.png)


## 3. Recursos


### 3.1 Criação de entrada de desembolso


Após enviar o documento de Empréstimo, se o status for "Sancionado" e "Reembolsar do Salário" estiver desmarcado, você poderá criar [Desembolso do empréstimo](/docs/pt/loan-management/loan-desembolso) do documento do empréstimo por meio do botão **Criar** no canto superior direito.


![Criar desembolso de empréstimo](/files/create-loan-disbursement.png)


### 3.2 Criação de entrada de reembolso


Se o empréstimo for total ou parcialmente desembolsado e a opção "Reembolsar do salário" estiver desmarcada, você poderá criar um [Empréstimo Reembolso](/docs/pt/loan-management/loan-repayment) do documento de empréstimo através do botão **Criar** no canto superior direito.


![Criar reembolso de empréstimo](/files/create-loan-repayment.png)


### 3.3 Dedução de reembolso de empréstimo do salário


Para deduzir automaticamente o reembolso do empréstimo do salário, marque "Reembolsar do salário" em Empréstimo. Ele aparecerá como Reembolso de Empréstimo no Comprovante de Salário e um registro de [Reembolso de Empréstimo](/docs/pt/loan-management/loan-repayment) também será criado automaticamente para o isso.


![Empréstimo com comprovante de salário](/files/salary-slip-loan.png)



