# Lançamento de pagamento para conta de capital



**Pergunta:** 
  
Como criar um Registro de Pagamento onde um acionista está investindo capital. O valor deverá ser adicionado na conta bancária da empresa.
  

**Resposta:** 
  
Você também pode criar uma entrada de pagamento para um acionista. Depois de adicionar um Acionista no ERPNext, você pode selecioná-lo na Entrada de Pagamento nestas linhas.  
![](/files/Etxow8j.png )  
A única coisa que você terá que verificar com sua CA será Conta paga de. Se você criar esta Entrada a partir de Entrada de Pagamento, que é projetada para receber pagamentos com base em provisões, você terá que definir uma conta de Devedor ou Credor para seleção no campo Conta Paga De.  
### Lançamento de pagamento via lançamento contábil manual

  
Se isso não ajudar, você pode criar um lançamento contábil manual para gerenciar esse cenário. Uma simples entrada no diário seria:
Cr. Conta do acionista................ XXXDr. Conta bancária ............................ XXX  
 Também no lançamento contábil manual, você usa campos como Nº de referência e Data para rastrear detalhes do cheque do cliente.

