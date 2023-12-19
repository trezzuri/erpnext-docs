# Criação automática de tarefas



Cada documento no ERPNext tem uma opção chamada 'Atribuir a' na barra lateral. Usando esta opção, qualquer documento pode ser atribuído ao usuário. O usuário receberia uma tarefa simultaneamente.


![Criação automática de tarefas](/files/using-todo-auto-assign-1.gif)


Sob tais condições, os três status de ToDo são definidos de acordo com as atualizações da tarefa.


Vamos considerar um cenário em que uma tarefa é atribuída por meio de um problema. Digamos que existam 2 níveis de suporte em uma organização, L1 e L2, e cada novo ticket de suporte seja considerado um problema de suporte L1 e atribuído aos membros relevantes da equipe. Nesse caso, os status do ToDo variariam da seguinte forma:


1. **Aberto**: quando um problema é criado e atribuído a um membro da equipe de suporte N1.
2. **Fechado**: um membro da equipe de suporte L1 identifica o problema e o resolve.
3. **Cancelado**: o membro da equipe de suporte L1 identifica o problema como um problema de nível de suporte L2 e o atribui ao membro relevante da equipe.


## Reabertura de tarefas encerradas


No mesmo cenário acima, digamos que o ticket de suporte foi marcado como fechado por um membro da equipe de suporte L1. No entanto, o problema será reaberto se o ticket for reaberto novamente ou se houver uma atividade neste problema


Simultaneamente, o ToDo associado ao Ticket de Suporte também será reaberto.


![ToDo](/files/using-to-do-6.png)



