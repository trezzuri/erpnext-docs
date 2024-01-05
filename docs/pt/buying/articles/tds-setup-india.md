# Configuração TDS para a Índia



Para configurar ***TDS*** no ERPNext siga os passos abaixo:  
* Primeiro você tem que definir categorias de retenção de impostos, por padrão 28 categorias já estão predefinidas de acordo com as conformidades legais indianas. Mas se quiser adicionar uma nova categoria, você pode criar a mesma clicando em "Novo" (botão no canto superior direito)

  
 ![](/files/Oq1mP48.png)  
  
* De acordo com a categoria, você deve definir a taxa de retenção de imposto junto com "Limite de transação única" e "Limite de transação cumulativa" para financeiro/fiscal ano.

  
  
![](/files/MELGDIu.png )  
* No mesmo tela, você encontrará outra seção de "Detalhes da conta" para definir a conta TDS a pagar da empresa.

  
  
 ![](/files/IIB6N8R.png)  
* Depois de concluir a configuração da retenção de impostos, vá para o mestre de fornecedores e atribua a categoria de retenção de impostos.

  
  
![](/files/aThoNuR.png)  
   
* Agora, quando você criar uma fatura de compra contra esse fornecedor, certifique-se de que "Aplicar valor retido na fonte" esteja marcado, então somente o sistema buscará automaticamente o valor do TDS a pagar na tabela "Impostos e encargos" com base no limite que você definiu .

  
  
![](/files/zyZdwsr.png)  
  
  
![](/files/XUJEgQ7.png)  
  
O relatório padrão também está disponível para verificar as contas a pagar mensalmente, basta pesquisar o relatório "TDS a pagar mensalmente" para o mesmo.

