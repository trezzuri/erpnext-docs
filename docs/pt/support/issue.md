# Emitir


**Um problema é uma consulta recebida de um cliente, geralmente por e-mail ou na seção *Contato* do seu site.**



>
> Dica: um endereço de e-mail de suporte dedicado é uma boa maneira de acompanhar as
> consultas. Por exemplo, você pode enviar consultas de suporte para ERPNext em
> support@erpnext.com e criará automaticamente um problema em nosso sistema.
>
>
>


Para acessar a lista de problemas, vá para:



>
> Início > Suporte > Problemas > Problema
>
>
>


![Problema](/files/issue.png)


## 1. Pré-requisitos


Antes de criar e usar problemas, é recomendável criar primeiro o seguinte:


* [Cliente](/docs/v13/user/manual/en/CRM/cliente)
* [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account)


## 2. Como criar um problema


Os problemas são criados automaticamente se você usar o recurso **acrescentar a** em [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account#32-incoming-email-accounts) .


Você também pode criar um problema manualmente, para fazer isso:


1. Vá para a lista de problemas, clique em Novo.
2. Insira o Assunto, Levantado por e uma descrição do problema.


### 2.1 Opções adicionais ao criar um problema


* **Status**: Quando um novo problema é criado, seu status será "Aberto", quando for
respondeu, seu status passa a ser "Respondido".


+ Abrir: o problema foi criado e ainda não foi respondido.
+ Respondido: Uma resposta foi enviada para o problema.
+ Espera: O problema está em espera por algum motivo.
+ Resolvido: quando os usuários têm certeza razoável de que forneceram ao cliente uma solução para seu problema, mas não receberam uma confirmação sobre a resolução do cliente.
+ Fechado: O Cliente obteve uma resolução satisfatória que indicou com um reconhecimento e o Problema foi encerrado. Se o remetente responder ao tópico, o status torna-se "Aberto" novamente. O usuário pode "Fechar" o problema manualmente clicando no botão **Fechar** no canto superior direito.



>
> Observação: se o SLA tiver sido configurado, o status de cumprimento do SLA será atualizado tanto no status **Fechado** quanto no status **Resolvido**.
>
>
>


* **Cliente**: Se o e-mail foi enviado de um [Cliente](/docs/v13/user/manual/en/CRM/cliente) armazenado em sua conta ERPNext, um link Cliente aparecerá neste campo.
* **Prioridade**: A prioridade pode ser definida de acordo com os requisitos. Por padrão, há três prioridades: Baixa, Média e Alta. Você pode excluí-los ou adicionar mais conforme necessário.
* **Tipo de problema**: um problema pode ser classificado usando o tipo de problema. Exemplos de tipos de problemas podem ser: 'Funcional', 'Técnico', 'Hardware', etc.
* **Raised By (Email)**: O ID do e-mail do qual o problema foi enviado será mostrado aqui.


## 3. Características


### 3.1 Detalhes


* **Descrição**: Este é um campo de texto no qual os detalhes sobre o problema podem ser vistos. Isso também pode conter uma imagem ou uma tabela.


### 3.2 Acordo de Nível de Serviço


É um contrato entre um provedor de serviço e o usuário final que define o nível de serviço esperado do provedor de serviço.


O usuário pode selecionar o [Contrato de Nível de Serviço](/docs/v13/user/manual/en/support/service-level-agreement) (SLA) na lista.


* Cada problema terá um tempo para resposta e um tempo para resolver dentro do qual a equipe de suporte deve responder e resolver o problema.
* A prioridade pode ser alterada para escalar o problema. As prioridades precisam ser especificadas no Acordo de Nível de Serviço.
* Se necessário, o Acordo de Nível de Serviço pode ser redefinido clicando no botão **Redefinir Acordo de Nível de Serviço** em Problemas mostrados a seguir:


![SLA](/files/new-issue.gif)


### 3.3 Resposta


* **Mins to First Response**: Tempo em minutos desde a criação do problema até o envio da primeira resposta.
* **Respondido pela primeira vez em**: quando um membro da equipe de suporte responder pela primeira vez ao problema, a data e a hora da primeira resposta serão atualizadas.
* **Tempo médio de resposta**: O tempo médio gasto para responder ao cliente. Isso é calculado tomando a média de todos os intervalos de tempo entre as comunicações recebidas e enviadas. Este campo será atualizado a cada resposta enviada ao cliente.


![Detalhes da resposta](/files/response.png)


### 3.4 Referência


O usuário pode filtrar os problemas com base nestes campos vinculados ao problema:


* Liderar
* Contato
* Conta de e-mail
* Projeto
* Empresa


### 3.5 Resolução


* **Data de Abertura**: Quando o problema for criado ou registrado, a data será postada.
* **Horário de Abertura**: Quando o problema for criado ou registrado, o horário exato será postado automaticamente.
* **Data da Resolução**: Quando o usuário resolver o problema, Data e Hora serão atualizadas neste campo.
* **Detalhes da resolução**: O usuário pode inserir os detalhes do problema, uma vez resolvido. Este é um campo de texto. Além disso, o usuário pode fazer upload da imagem, inserir ou criar uma tabela.
* **Resolution Time**: Tempo total gasto para fechar o ticket (desde a criação do problema até o fechamento).
* **Tempo de resolução do usuário**: Muitas vezes o usuário precisa aguardar a resposta do cliente para resolver algum problema. Ao medir a produtividade do usuário, esse tempo de espera não deve ser levado em consideração. Portanto, o tempo de resolução do usuário é o tempo total gasto por um usuário para fechar o ticket e pode ser calculado como:


*Tempo de resolução - Tempo total que o usuário teve que esperar pela resposta de um cliente*


As métricas Tempo de resolução e Tempo de resolução do usuário são definidas como "Fechar". Essas métricas são redefinidas automaticamente quando o problema é reaberto ou dividido.


![Resolução](/files/resolution.png)


#### Via Portal do Cliente


Se o cliente que levantou o problema for um usuário do site (sem acesso aos módulos), esta caixa de seleção será marcada para indicar isso.


## 4. Depois de Salvar


### 4.1 Adicionar comentários


Depois que o problema é registrado, os usuários da equipe de suporte podem adicionar comentários para o problema. Este campo é editável. Comentários em Problemas são para discussões internas e não serão visíveis para os Clientes.


### 4.2 Novo e-mail


Os usuários podem redigir um e-mail para a pessoa que levantou o problema. Todos os e-mails (recebidos e enviados) podem ser vistos em um tópico no Issue.


### 4.3 Tópico de Discussão


O encadeamento de discussão por e-mail em um problema mantém todos os e-mails enviados e recebidos nesse problema no sistema para que você possa rastrear o que aconteceu entre o remetente e a pessoa que está respondendo.


* Quando um novo e-mail é enviado de sua caixa de correio, uma resposta automática é enviada ao remetente com sua mensagem e o número do ticket de suporte.
* O remetente pode enviar informações adicionais para este e-mail.
* Todos os e-mails subsequentes contendo este número de problema no assunto serão adicionados a este tópico de problema.
* O remetente também pode adicionar anexos ao e-mail.


### 4.4 Atribuindo Problemas aos Usuários



>
> Os problemas podem ser atribuídos automaticamente entre os usuários usando a [Regra de atribuição](/docs/v13/user/manual/en/automation/assignment-rule).
>
>
>


Você pode atribuir um problema a um usuário específico clicando no recurso "Atribuir" na barra lateral esquerda. Isso adicionará um novo To Do ao usuário e também enviará uma mensagem indicando que esse problema está alocado.


![Atribuir problema](/files/issue-assign.png)


### 4.5 Encerramento


* Você pode fechar o problema manualmente clicando em 'Fechar' na barra de ferramentas.
* Se o remetente não responder em 7 dias, o problema será encerrado automaticamente.


### 5. Tópicos Relacionados


1. [Tipo de problema e prioridade](/docs/v13/user/manual/en/support/issue-type-and-priority)