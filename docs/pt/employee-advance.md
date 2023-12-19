# Adiantamento de funcionário



**Às vezes, os funcionários saem para trabalhar na empresa e a empresa paga antecipadamente alguma quantia pelas despesas. É quando o funcionário pode criar um formulário de adiantamento de funcionário onde detalhes como a finalidade da despesa e o valor da despesa podem ser registrados.**


Depois que o adiantamento do funcionário for criado pelo funcionário, o aprovador de despesas poderá enviar o registro do adiantamento após a verificação. Após o envio do adiantamento do funcionário, o contador libera o pagamento e faz o lançamento do pagamento.


Para acessar o Employee Advance, acesse:


> Recursos Humanos > Relatórios de Despesas > Adiantamento de Funcionário


## 1. Pré-requisitos


1. [Funcionário](/docs/pt/human-resources/employee)
2. [Departamento](/docs/pt/human-resources/department)
3. [Plano de contas](/docs/pt/accounts/chart-of-accounts)


## 2. Como criar um adiantamento de funcionário


1. Acesse: Adiantamento de Funcionário > Novo.
2. Selecione o funcionário a quem você deseja dar o adiantamento.
3. Insira a finalidade e o valor do adiantamento.
4. Selecione a conta antecipada e a forma de pagamento.
5. Salvar.


![Reclamação de despesas](/files/employee-advance.png)


> Nota: O Funcionário só pode Salvar o Adiantamento do Funcionário, mas não pode Submetê-lo. Só pode ser enviado pelo aprovador de despesas.


### 2.1 Status


Estes são os status definidos automaticamente para o Adiantamento de Funcionário.


* **Rascunho**: um rascunho foi salvo, mas ainda não foi enviado.
* **Pago**: o adiantamento foi pago ao funcionário e uma [entrada de pagamento](/docs/pt/accounts/payment-entry) foi enviado.
* **Não pago**: O adiantamento ainda não foi pago ao funcionário. Uma entrada de pagamento não é criada contra o adiantamento.
* **Reivindicado**: após o pagamento do adiantamento, o funcionário reivindicou todo o *valor pago* via [Declaração de despesas](/docs/pt/recursos humanos/declaração de despesas).
* **Devolvido**: após o pagamento do adiantamento, o funcionário devolveu todo o *Valor Pago* e uma declaração de devolução é enviada por meio de Entrada de Pagamento/Lançamento Diário.
* **Reivindicado parcialmente e devolvido**: após o pagamento do adiantamento, o funcionário reivindicou parcialmente o *valor pago* por meio do relatório de despesas e devolveu o valor restante por meio de uma entrada de pagamento enviada/Lançamento de diário.
* **Cancelado**: O Adiantamento é cancelado por qualquer motivo.


## 3. Recursos


### 3.1 Envio antecipado do funcionário


O registro de adiantamento de funcionário pode ser criado por qualquer funcionário, mas ele não pode enviar o registro.


Depois de salvar o adiantamento do funcionário, o funcionário deve [atribuir o documento ao aprovador](https://docs.erpnext.com/docs/pt/using-erpnext/assignment) . Na atribuição, o usuário aprovador também receberá uma notificação por e-mail. Para automatizar a notificação por e-mail, você também pode configurar [Alerta por e-mail](/docs/pt/setting-up/notifications.html).


Após a verificação, o aprovador de despesas pode enviar (aceitar) o formulário de adiantamento do funcionário ou rejeitar a solicitação.


### 3.2 Efetuar entrada de pagamento


##### Adiantamento de funcionário via entrada de pagamento


Após o envio do registro de adiantamento do funcionário, o usuário da conta poderá criar uma [Entrada de pagamento](/docs/pt/accounts/payment-entry) usando o ' Botão Criar'.


A entrada de pagamento terá a seguinte aparência:


![Pagamento antecipado de funcionário via entrada de pagamento](/files/employee-advance-payment-entry.png)


#### Pagamento antecipado do funcionário via lançamento contábil manual


Como alternativa, um [Lançamento de Diário](/docs/pt/accounts/journal-entry) também pode ser criado em relação ao Adiantamento do Funcionário.


![Pagamento antecipado de funcionário via lançamento contábil manual](/files/employee-advance-journal-entry1.png)


> Nota: Certifique-se de que o Tipo de Parte esteja selecionado como Funcionário e o Tipo de Referência esteja selecionado como Funcionário
Avançar.


![Pagamento antecipado de funcionário via lançamento contábil manual](/files/employee-advance-journal-entry2.png)


#### O adiantamento do funcionário é pago


Ao enviar o Registro de Pagamento/Lançamento Diário, o valor pago e o status serão atualizados no registro de Adiantamento do Funcionário.


### 3.3 Ajustar adiantamentos sobre declaração de despesas


Mais tarde, quando o funcionário reivindicar a despesa, um registro antecipado poderá ser obtido no [Relatório de Despesas](/docs/pt/human-resources/expense-claim) e vinculado ao registro da reivindicação.


### 3.4 Valor de devolução


Quando o adiantamento é pago a um Colaborador, existem três situações:


* O valor pode não ser utilizado
* Tudo isso pode ser usado
* Alguma parte pode ser usada


Crie o Adiantamento do Funcionário, crie uma entrada de pagamento para indicar que o valor foi pago.


* Se o valor não for utilizado, clique no botão **Devolver** para devolver o valor adiantado pago
![Botão Voltar](/files/advance-return-button.png)
* Se todo o adiantamento for usado, isso será refletido no campo Valor reivindicado
* Se apenas uma parte do valor for reivindicada e o restante for devolvido, o valor devolvido será mostrado no campo 'Valor Devolvido'.
![Valor adiantado de devolução](/files/advance-returned-amount.png)


## 4. Tópicos Relacionados


1. [Relatório de despesas](/docs/pt/human-resources/expense-claim)



