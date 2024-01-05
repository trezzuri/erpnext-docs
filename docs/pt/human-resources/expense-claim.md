# Relatório de despesas



**A declaração de despesas é feita quando os funcionários fazem despesas do próprio bolso em nome da empresa.**


Por exemplo, se eles levarem um cliente para almoçar, poderão fazer uma solicitação de reembolso por meio do formulário de reembolso de despesas.


Para acessar um relatório de despesas, acesse:


> Recursos Humanos > Relatórios de Despesas > Relatório de Despesas


## 1. Pré-requisitos


1. [Funcionário](/docs/pt/human-resources/employee)
2. [Departamento](/docs/pt/human-resources/department)
3. [Plano de contas](/docs/pt/accounts/chart-of-accounts)


## 2. Como criar um relatório de despesas


1. Acesse: Relatório de despesas > Novo.
2. Selecione o nome do funcionário no campo 'Do funcionário'.
3. Selecione o aprovador de despesas.
4. Insira a data da despesa, o tipo de relatório de despesas e o valor.
5. Além disso, você também pode inserir os impostos e taxas de despesas.
6. Em Detalhes contábeis, selecione a conta a pagar padrão da empresa.
7. Salvar e enviar.


![Reclamação de despesas](/files/expense_claim.png)


Defina o ID do funcionário, a data, a lista de despesas e os impostos correspondentes que serão reivindicados e “Envie” o registro.


![Reivindicação de despesas](/files/expense-claim-expenses.png)


Fluxo de trabalho do relatório de despesas






### Aprovação de despesas


O aprovador do relatório de despesas é selecionado pelo próprio funcionário. O funcionário pode escolher na lista de usuários configurados como *Aprovadores de despesas* para seu [Departamento](/docs/pt/human-resources/department).


Quando um novo relatório de despesas é criado, se o aprovador de despesas selecionado não tiver acesso a ele, o documento é compartilhado com o aprovador com permissão de "envio".


Depois de salvar o relatório de despesas, o funcionário deve [atribuir o documento ao aprovador](https://docs.erpnext.com/docs/pt/using-erpnext/assignment) . Na atribuição, o usuário aprovador também receberá uma notificação por e-mail. Para automatizar a notificação por e-mail, você também pode configurar o Alerta por e-mail


O Aprovador de Reclamações de Despesas pode atualizar os “Valores Sancionados” em relação ao Valor Reivindicado de um Funcionário. Se for enviado, o Status de aprovação deverá ser enviado para Aprovado ou Rejeitado. Se aprovado, o relatório de despesas será enviado. Se rejeitado, os comentários do aprovador de despesas poderão ser adicionados na seção Comentários explicando por que a reivindicação foi aprovada ou rejeitada.


### Reservando a despesa


Ao enviar o relatório de despesas, o sistema registra uma despesa na conta de despesas e na conta do funcionário
![Relatório de despesas](/files/expense_claim_book.png)


O usuário pode visualizar o relatório de despesas não pagas usando o relatório "Relatórios de despesas não reclamadas"
![Relatório de despesas](/files/unclaimed_expense_claims.png)


### Pagamento para relatório de despesas


Para efetuar o pagamento do relatório de despesas, o usuário deve clicar em Criar > Pagamento.


#### Relatório de despesas


![Criar pagamento](/files/expense_claim_create_payment.png)


#### Entrada de pagamento


> Nota: Este valor não deve ser adicionado ao Salário porque o valor será tributado ao Funcionário.


![Expense Claim](/files/expense_claim_payment_entry.png)


Como alternativa, um lançamento de pagamento pode ser feito para um funcionário e todos os relatórios de despesas pendentes serão incluídos.


> Contabilidade > Entrada de pagamento > Nova entrada de pagamento


Defina o Tipo de Pagamento como "Pagar", o Tipo de Parte como Funcionário, a Parte para o funcionário que está sendo pago e a conta que está sendo paga. Todas as declarações de despesas pendentes serão retiradas e os valores dos pagamentos poderão ser alocados para cada despesa.


### Vinculando com tarefa e projeto


* Para vincular o relatório de despesas a uma tarefa ou projeto, especifique a tarefa ou o projeto ao fazer um relatório de despesas


![Relatório de despesas-Link do projeto](/files/project-expense-claim-1.png)


Isso atualizará o custo do projeto com os valores do relatório de despesas


![Relatório de despesas-Link do projeto](/files/project-expense-claim-2.png)



