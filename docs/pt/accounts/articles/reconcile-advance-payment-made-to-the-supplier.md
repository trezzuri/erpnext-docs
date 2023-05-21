# Conciliar o Adiantamento feito ao Fornecedor


**Durante a migração do aplicativo *x* para o ERPNext, como registrar contas a pagar antecipadamente e reconciliar com faturas futuras?**

  


**Reserva Antecipada de Contas a Pagar:**

  


Crie um **Registro de Diário** com o tipo **Registro de Abertura**, debite a *Conta do Credor* escolhendo o *Fornecedor* necessário e Credite a *Conta de Abertura Temporária*.

Expanda a Linha do Credor e selecione **Sim** para *É Adiantamento.*

*Consulte o GIF que ilustra o mesmo:*

  


![](/files/CsMRH40.gif)

  


O envio do lançamento contábil refletirá um saldo negativo no **Resumo de contas a pagar**:![](/files/FJeIj5k.png)**Reconciliando-o com as faturas de compra:**

  


Consulte o relatório **Contas a Pagar** *depois* de criar uma Fatura de Compra:

  


![](/files/cxZArKd.png)

  


Atualmente, eles não são reconciliados e são refletidos como **duas** **entradas separadas**, use a ferramenta **Reconciliação de pagamentos** para reconciliar essas duas entradas, *consulte o GIF para obter as etapas:*

  


![](/files/jbj6LRc.gif)

  


Consulte o Relatório de Contas a Pagar após a reconciliação, ele *não* refletirá mais o **Lançamento Diário** e refletirá o (*Valor Faturado - Valor Adiantado)*:

  


![](/files/vaXYQNc.png)