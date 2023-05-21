# Etapas fáceis para configurar o fluxo de trabalho


Quando uma empresa possui vários níveis de aprovação para um documento, um Workflow pode ser definido.
No ERPNext, você pode ir para a lista Workflow --> Criar Novo --> Nomear o workflow e definir:1. estados
2. Regras de transição.

  
1. Estados:

Quando um documento é repassado para diferentes níveis de aprovação, existem estados definidos em cada nível para a função do usuário.
![](/files/Y3TzzU2.png)
  
1. Regras de Transição:

Por exemplo: Um **usuário de Vendas** só pode criar uma **Cotação** e ela pode ser salva no estado **Rascunho**. Além disso, ela pode ser enviada ao **Gerente de vendas** para aprovação e o usuário com essa função pode ter permissão para **Aprovar** ou **Rejeitar** a cotação, após a qual ela pode ser enviada para o **Rascunho** Estado se **Rejeitado** ou final **Aprovado** Estado.
![](/files/xJUtkGy.png)
Mensagens de erro: **Um documento não pode ser cancelado antes de ser enviado.**
[Este é um erro típico enfrentado por usuários que definem o estado do documento cancelado antes de enviá-lo. Doc Status 1 define que o Documento será Enviado naquele Estado, portanto o Estado com Doc status 2 só deve ser definido na Transição após o Estado com Doc status 1. ]
Configure um fluxo de trabalho simples para começar e deixe-nos saber o que você pensa mais sobre fluxos de trabalho! Adoramos ver nossos usuários felizes!! ;)