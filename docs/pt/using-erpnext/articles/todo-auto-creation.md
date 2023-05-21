# Criação Automática de Tarefas


Cada documento no ERPNext tem uma opção chamada 'Atribuir a' na barra lateral. Usando esta opção, qualquer documento pode ser atribuído ao usuário. O usuário receberia um ToDo simultaneamente.


![ToDo Auto Creation](/files/using-todo-auto-assign-1.gif)


Sob tais condições, os três status ToDo são definidos de acordo com as atualizações na atribuição.


Vamos considerar um cenário em que um ToDo é atribuído por meio de um problema. Digamos que haja 2 níveis de suporte em uma organização L1 e L2 e cada novo tíquete de suporte seja considerado um problema de suporte L1 e atribuído aos membros relevantes da equipe. Nesse caso, os status ToDo variariam da seguinte forma:


1. **Aberto**: Quando um problema é criado e atribuído a um membro da equipe de suporte L1.
2. **Fechado**: O membro da equipe de suporte L1 identifica o problema e o resolve.
3. **Cancelado**: o membro da equipe de suporte L1 identifica o problema como um problema de nível de suporte L2 e o atribui ao membro da equipe relevante.


## Reabertura de Atribuições Fechadas


No mesmo cenário acima, digamos que o ticket de suporte foi marcado por um membro da equipe de suporte L1. No entanto, o ISsue será reaberto se o ticket for reaberto novamente ou se houver uma atividade neste problema


Simultaneamente, o ToDo associado ao Support Ticket também será reaberto.


![ToDo](/files/using-to-do-6.png)