# Pendência


ToDo é uma lista de atividades que devem ser feitas por um indivíduo em particular.


**No ERPNext, um ToDo é uma ferramenta simples onde você pode definir as atividades a serem realizadas. A ToDo List listará todas as atividades atribuídas a você e por você.**


![ToDo](/files/using-to-do-1.png)


Um ToDo também é criado automaticamente quando qualquer outro documento é atribuído a você. Checkout [ToDo Auto Creation](/docs/v13/user/manual/en/using-erpnext/articles/todo-auto-creation)


Para acessar ToDo, vá para



>
> Início > Ferramentas > Tarefas
>
>
>


## 1. Como criar um ToDo


1. Vá para a lista de tarefas e clique em novo.
2. Você será redirecionado para uma entrada rápida para ToDo, onde será solicitado a inserir a descrição do ToDo.
3. Salve.


![ToDo](/files/using-to-do-2.gif)



>
> Nota: Ao criar um ToDo usando a Entrada rápida, o ToDo por padrão é atribuído ao criador. Para evitar o mesmo e atribuí-lo a outros usuários, certifique-se de editar o ToDo em Full Page.
>
>
>


### Notificação de Tarefas


Depois que um ToDo é criado, o usuário atribuído receberá uma notificação para o ToDo.


![ToDo](/files/using-todo-notification.png)


### 1.1. Opções adicionais ao criar um ToDo


1. **Status**: Você pode definir o status do ToDo. Durante a criação, o status do ToDo seria 'Aberto' por padrão. O usuário pode alterá-lo para 'Fechado' quando a atribuição for concluída.
2. **Prioridade**: Você pode definir a Prioridade desta tarefa como Baixa, Média ou Alta.
3. **Cor**: Você pode escolher atribuir uma cor a cada um dos seus ToDos. Por exemplo, um ToDo criado como um lembrete semanal para envio de relatórios pode ser atribuído à cor Roxo, enquanto todos os ToDos pessoais podem ser atribuídos à Cor Amarela.
4. **Due Date**: Você pode adicionar a data de vencimento a todos os ToDos.
5. **Alocated To**: Nos casos em que você está atribuindo uma ToDo a outro usuário do ERPNext, você pode fazê-lo aqui.


![ToDo](/files/using-to-do-3.png)


### 1.2. Referências


Cada documento no ERPNext tem uma opção chamada 'Atribuir a' na barra lateral. Usando esta opção, qualquer Dcoument pode ser atribuído ao usuário. O usuário receberia um ToDo simultaneamente.


1. **Tipo de Referência**: Quando um ToDo é criado a partir de outro documento, digamos uma Tarefa ou um Problema, o Tipo de Documento de Referência é vinculado ao ToDo aqui. Você também pode optar por adicionar um tipo de documento de referência manualmente.
2. **Reference Name**: Na atribuição por meio de outro DocType, o nome do Reference DocType também é vinculado aqui.
3. **Atribuição por**: quando você recebe uma Tarefa por meio de outro tipo de documento, o nome da pessoa que faz a atribuição também é marcado.


![ToDo](/files/using-to-do-4.png)


## 2. Status de Tarefas


ToDo tem 3 status, cada um descrevendo o estado atual de uma tarefa.


* **Aberto**: Um ToDo por padrão é marcado como Aberto quando é criado.
* **Fechado**: Quando uma atividade é concluída, o ToDo pode ser marcado como 'Fechado', 'Resolvido' ou 'Concluído'. Além disso, para condições como Problema resolvido ou tarefa concluída; o ToDo é fechado automaticamente. Ele também pode ser reaberto, se necessário.
* **Cancelado**: quando um usuário é removido da atribuição de uma Pendência/Tarefa/Problema, a Pendência vinculada a esse Documento é automaticamente 'Cancelada'.


![ToDo](/files/using-to-do-5.png)