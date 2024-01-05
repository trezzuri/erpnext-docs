# Problema



**Um problema é uma consulta recebida de um cliente, geralmente por e-mail ou na seção *Contato* do seu site.**



> 
> Dica: um endereço de e-mail de suporte dedicado é uma boa maneira de acompanhar as mensagens recebidas.
>  consultas. Por exemplo, você pode enviar consultas de suporte para o ERPNext em
>  support@erpnext.com e criará automaticamente um problema em nosso sistema.
> 
> 
> 


Para acessar a lista de problemas, vá para:



> 
> Página inicial > Suporte > Problemas > Problema
> 
> 
> 


![Issue](/files/issue.png)


## 1. Pré-requisitos


Antes de criar e usar problemas, é aconselhável criar primeiro o seguinte:


* [Cliente](/docs/pt/CRM/customer)
* [Conta de e-mail](/docs/pt/setting-up/email/email-account)


## 2. Como criar um problema


Os problemas serão criados automaticamente se você usar o **acrescentar ao recurso** em [Conta de e-mail](/docs/pt/setting-up/email/email-account#32-incoming-email-accounts).


Você também pode criar um problema manualmente. Para fazer isso:


1. Vá para a lista de problemas e clique em Novo.
2. Insira o assunto levantado por e uma descrição do problema.


### 2.1 Opções adicionais ao criar um problema


* **Status**: Quando um novo Issue é criado, seu status será "Aberto", quando for
respondeu, seu status se torna "Respondido".


	+ Aberto: o problema foi criado e ainda não foi respondido.
	+ Respondido: uma resposta foi enviada ao problema.
	+ Em espera: o problema está em espera por algum motivo.
	+ Resolvido: quando os usuários têm certeza razoável de que forneceram ao cliente uma solução para seu problema, mas não receberam uma confirmação do cliente sobre a resolução.
	+ Encerrado: o Cliente obteve uma resolução satisfatória que indicou com uma confirmação e o problema foi encerrado.Se o remetente responder ao tópico, o status se tornará "Aberto" novamente. O usuário pode "Fechar" o problema manualmente clicando no botão **Fechar** no canto superior direito.



> 
> Observação: se o SLA tiver sido configurado, o status de cumprimento do SLA será atualizado tanto no status **Fechado** quanto no status **Resolvido**.
> 
> 
> 


* **Cliente**: Se o e-mail foi enviado de um [Cliente](/docs/pt/CRM/customer) armazenado em sua conta ERPNext , um link do cliente aparecerá neste campo.
* **Prioridade**: A prioridade pode ser definida de acordo com os requisitos. Por padrão, existem três prioridades – Baixa, Média e Alta. Você pode excluí-los ou adicionar mais conforme necessário.
* **Tipo de problema**: um problema pode ser classificado usando Tipo de problema. Exemplos de tipos de problemas podem ser: 'Funcional', 'Técnico', 'Hardware', etc.
* **Levantado por (e-mail)**: o ID do e-mail do qual o problema foi enviado será mostrado aqui.


## 3. Recursos


### 3.1 Detalhes


* **Descrição**: Este é um campo de texto onde podem ser visualizados detalhes sobre o Problema. Também pode conter uma imagem ou uma tabela.


### 3.2 Acordo de nível de serviço


É um contrato entre um provedor de serviços e o usuário final que define o nível de serviço esperado do provedor de serviços.


O usuário pode selecionar o [Acordo de nível de serviço](/docs/pt/support/service-level-agreement) (SLA) na lista.


* Cada problema terá um tempo para resposta e um tempo para resolução dentro dos quais a equipe de suporte deverá responder e resolver o problema.
* A Prioridade pode ser alterada para escalar o problema. As prioridades precisam ser especificadas no Acordo de Nível de Serviço.
* Se necessário, o Acordo de Nível de Serviço pode ser redefinido clicando no botão **Redefinir Acordo de Nível de Serviço** em Problemas mostrados a seguir:


![SLA](/files/new-issue.gif)


### 3.3 Resposta


* **Minutos até a primeira resposta**: tempo em minutos desde a criação do problema até o envio da primeira resposta.
* **Primeira resposta em**: quando um membro da equipe de suporte responder ao problema pela primeira vez, a data e a hora da primeira resposta serão atualizadas.
* **Tempo Médio de Resposta**: O tempo médio necessário para responder ao Cliente. Isso é calculado tomando a média de todos os intervalos de tempo entre as comunicações recebidas e enviadas. Este campo será atualizado a cada resposta enviada ao cliente.


![Detalhes da resposta](/files/response.png)


### 3.4 Referência


O usuário pode filtrar os problemas com base nestes campos vinculados ao problema:


* Liderar
* Contato
* Conta de e-mail
* Projeto
* Empresa


### 3.5 Resolução


* **Data de abertura**: Quando o problema for criado ou registrado, a data será publicada.
* **Horário de abertura**: Quando o problema for criado ou registrado, o horário exato será publicado automaticamente.
* **Data da resolução**: quando o usuário resolver o problema, a data e a hora serão atualizadas neste campo.
* **Detalhes da resolução**: o usuário pode inserir os detalhes do problema assim que ele for resolvido. Este é um campo de texto. Além disso, o usuário pode fazer upload da imagem, inserir ou criar uma tabela.
* **Tempo de resolução**: tempo total necessário para fechar o ticket (desde a criação do problema até o fechamento).
* **Tempo de resolução do usuário**: Muitas vezes um usuário precisa esperar a resposta do cliente para resolver algum problema. Ao medir a produtividade do usuário, esse tempo de espera não deve ser levado em consideração. Portanto, o tempo de resolução do usuário é o tempo total que um usuário leva para fechar o ticket e pode ser calculado como:


*Tempo de resolução-Tempo total que o usuário teve que esperar pela resposta de um cliente*


As métricas Tempo de resolução e Tempo de resolução do usuário estão definidas em "Fechar". Essas métricas são redefinidas automaticamente quando o problema é reaberto ou dividido.


![Resolution](/files/resolution.png)


#### Através do Portal do Cliente


Se o Cliente que levanta o problema for um usuário do site (sem acesso aos módulos), esta caixa de seleção será marcada para indicar isso.


## 4. Depois de salvar


### 4.1 Adicionar comentários


Depois que o problema for registrado, os usuários da equipe de suporte poderão adicionar comentários sobre o problema. Este campo é editável. Os comentários nos Issues são para discussões internas e não ficarão visíveis para os Clientes.


### 4.2 Novo e-mail


Os usuários podem escrever um e-mail para a pessoa que levantou o problema. Todos os e-mails (recebidos e enviados) podem ser vistos em um tópico na edição.


### 4.3 Tópico de discussão


O tópico de discussão por e-mail em um problema mantém todos os e-mails enviados e recebidos em relação a esse problema no sistema para que você possa acompanhar o que aconteceu entre o remetente e a pessoa que respondeu.


* Quando um novo e-mail é enviado de sua caixa de correio, uma resposta automática é enviada ao remetente com sua mensagem e o número do ticket de suporte.
* O remetente pode enviar informações adicionais para este e-mail.
* Todos os e-mails subsequentes contendo este número de problema no assunto serão adicionados a este tópico de problema.
* O remetente também pode adicionar anexos ao e-mail.


### 4.4 Atribuindo problemas aos usuários



> 
> Os problemas podem ser atribuídos automaticamente entre os usuários usando a [Regra de atribuição](/docs/pt/automation/assignment-rule).
> 
> 
> 


Você pode atribuir um problema a um usuário específico clicando no recurso "Atribuir" na barra lateral esquerda. Isso adicionará uma nova tarefa ao usuário e também enviará uma mensagem indicando que este problema foi alocado.


![Atribuir problema](/files/issue-assign.png)


### 4.5 Fechamento


* Você pode fechar o problema manualmente clicando em 'Fechar' na barra de ferramentas.
* Se o remetente não responder em 7 dias, o problema será encerrado automaticamente.


### 5. Tópicos Relacionados


1. [Tipo e prioridade do problema](/docs/pt/support/issue-type-and-priority)



