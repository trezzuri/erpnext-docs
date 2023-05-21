# Entrada de Pagamento para Conta de Capital


**Pergunta:**
  
Como criar uma Entrada de Pagamento onde um acionista está investindo capital. O valor deve ser adicionado na conta bancária da empresa.
  

**Responder:**
  
Você também pode criar uma Entrada de Pagamento para um Acionista. Depois de adicionar um Acionista no ERPNext, você pode selecioná-lo no Lançamento de Pagamentos nestas linhas.
![](/files/Etxow8j.png)
A única coisa que você terá que verificar com sua autoridade de certificação seria Conta paga de. Se você criar esta Entrada de Entrada de Pagamento, que é projetada para receber pagamento com base em acréscimos, você terá que definir uma conta de Devedor ou Credor para seleção no campo Conta Paga de.
### Entrada de Pagamento via Lançamento Diário

  
Se isso não ajudar, você pode criar uma entrada de diário para gerenciar esse cenário. Uma entrada de diário simples seria:
Cr. Conta de acionista................ XXXDr. Conta bancária ...................... XXX
Também no Lançamento do diário, você usa os campos como Nº de referência e Data para rastrear os detalhes do cheque do cliente.