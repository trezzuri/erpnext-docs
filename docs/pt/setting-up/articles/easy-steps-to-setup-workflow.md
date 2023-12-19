# Etapas fáceis para configurar o fluxo de trabalho



Quando uma empresa possui vários níveis de aprovação para um documento, um Workflow pode ser definido.   
No ERPNext, você pode ir para a lista de fluxo de trabalho--> Criar novo--> Nomear o fluxo de trabalho e definir:1. Estados
2. Regras de transição.

  
1. Estados:

Quando um documento é aprovado ativados para diferentes níveis de aprovação, existem estados definidos em cada nível para a função do usuário.   
![](/files/Y3TzzU2.png)  
   
1. Regras de transição:

Por exemplo: um **usuário de vendas** é apenas é permitido criar uma **Cotação** e ela pode ser salva no estado **Rascunho**. Além disso, ele pode ser enviado ao **Gerente de Vendas** para aprovação e o usuário com esta função pode ter permissão para **Aprovar** ou  **Rejeite** a Cotação, após a qual ela poderá ser enviada para o Estado **Rascunho** se for **Rejeitada** ou para o Estado **Aprovado** final.   
![](/files/xJUtkGy.png)  
 Mensagens de erro: **Um documento não pode ser cancelado antes de ser enviado.**   
[Esta é uma situação típica erro enfrentado pelos usuários que definem o estado do documento cancelado antes de enviá-lo. Doc Status 1 define que o Documento será Submetido naquele Estado, portanto o Estado com Doc status 2 só deverá ser definido na Transição após o Estado com Doc status 1. ]  
Configure um fluxo de trabalho simples para começar e diga-nos o que você acha mais sobre fluxos de trabalho! Adoramos ver nossos usuários felizes!! ;)   
  


