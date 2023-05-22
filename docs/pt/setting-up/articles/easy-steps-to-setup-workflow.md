# Etapas fáceis para configurar o fluxo de trabalho


Quando uma empresa possui vários níveis de aprovação para um documento, um Workflow pode ser definido.   
No SOMA, você pode ir para a lista Workflow --> Criar Novo --> Nomear o workflow e definir:1. Estados
2. Regras de transição.

  
1. Estados:

Quando um documento é passado para diferentes níveis de aprovação, existem estados definidos em cada nível para a função do usuário.   
![](/files/Y3TzzU2.png)  
   
1. Regras de transição:

Por exemplo: Um **usuário de vendas** é apenas permissão para criar uma **Cotação** e ela pode ser salva no estado **Rascunho**. Além disso, pode ser enviado ao **Gerente de vendas** para aprovação e o usuário com esta função pode ter permissão para **Aprovar** ou  **Rejeitar** a Cotação após a qual ela pode ser enviada para o estado **Rascunho** se **Rejeitado** ou para o estado final **Aprovado**.   
![](/files/xJUtkGy.png)  
 Mensagens de erro: **Um documento não pode ser cancelado antes de ser enviado.**   
[Este é um típico erro enfrentado por usuários que definem o estado do documento cancelado antes de enviá-lo. Doc Status 1 define que o Documento será Enviado naquele Estado, portanto o Estado com Doc status 2 só deve ser definido na Transição após o Estado com Doc status 1. ]  
Configure um Fluxo de Trabalho Simples para começar e deixe-nos saber o que você pensa mais sobre Fluxos de Trabalho! Adoramos ver nossos usuários felizes!! ;)   
  
