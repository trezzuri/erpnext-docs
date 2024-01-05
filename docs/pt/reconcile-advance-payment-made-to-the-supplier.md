# Conciliar pagamento antecipado feito ao fornecedor



**Ao migrar da aplicação *x* para o ERPNext, como reservar contas a pagar antecipadamente e conciliar com faturas futuras?** 

  


**Reserva antecipada de contas a pagar:** 

  


Crie um **Lançamento contábil** com o tipo **Lançamento de Abertura**, Debitar a*Conta do Credor* escolhendo o *Fornecedor* necessário e Creditar o *Temporário Abertura de conta*.

Expanda a linha do credor e selecione **Sim** para *É adiantado.* 

*Consulte o GIF que ilustra o mesmo:* 

  


![](/files/CsMRH40.gif)

  


O envio do lançamento contábil manual refletirá um saldo negativo em **Resumo de contas a pagar**:![](/files/FJeIj5k.png)**Conciliando com as faturas de compra:** 

  


Consulte **Contas a Pagar**  relatório *após* a criação de uma fatura de compra:

  


![](/files/cxZArKd.png) 

  


Atualmente, eles não estão reconciliados e são refletidos como **duas** **entradas separadas**, use o **Ferramenta de reconciliação de pagamentos** para reconciliar essas duas entradas, *consulte o GIF para ver as etapas:*

  


![](/files/jbj6LRc.gif)

  


Consulte o Relatório de Contas a Pagar após a reconciliação, ele *não* refletirá o **Lançamento no diário** e refletirá o (*Valor faturado-Valor antecipado)*: 

  


![](/files/vaXYQNc.png)



