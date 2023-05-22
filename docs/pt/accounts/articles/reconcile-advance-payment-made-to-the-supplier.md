# Reconciliar o adiantamento feito ao fornecedor


**Ao migrar do aplicativo *x* para o ERPNext, como reservar contas a pagar antecipadamente e reconciliar com faturas futuras?** 

  


**Agendamento de contas a pagar:** 

  


Criar um **Entrada de Diário** com o tipo **Abertura**, Debitar a *Conta do Credor* escolhendo o *Fornecedor* necessário e Creditar a *Temporária Abertura de conta*.

Expanda a Linha do credor e selecione **Sim** para *É adiantado.* 

*Consulte o GIF que ilustra o mesmo:* 

  


![](/ files/CsMRH40.gif)

  


Enviar o lançamento contábil manual refletirá um saldo negativo no **Resumo de contas a pagar**:![](/files/FJeIj5k.png)**Conciliação com as Faturas de Compra:** 

  


Consulte **Contas a Pagar**  relatório *após* criar uma Fatura de Compra:

  


![](/files/cxZArKd.png) 

  


Atualmente, eles não são reconciliados e são refletidos como **dois** **entradas separadas**, use o **Payment Reconciliation** ferramenta para reconciliar essas duas entradas, *consulte o GIF para as etapas:*

  


![](/files/jbj6LRc.gif)

  


Consulte o Relatório de contas a pagar após a reconciliação, ele *não* refletirá o **Entrada de diário** e refletirá o (*Valor faturado - Valor do adiantamento)*: 

  


![](/files/vaXYQNc.png)

