# Permissões baseadas em funções


**A permissão para diferentes documentos pode ser controlada usando permissões baseadas em funções.**


O ERPNext possui um sistema de permissão baseado em função. Isso significa que você pode atribuir funções aos usuários e as permissões podem ser definidas nas funções. O Gerenciador de permissões de função permite definir quais funções podem acessar quais documentos e com quais permissões (ler, escrever, enviar, etc.).


Depois que as funções são atribuídas a um usuário, seu acesso pode ser limitado a documentos específicos. A estrutura de permissão permite definir diferentes regras de permissão para diferentes campos usando um conceito chamado **Nível de permissão** de um campo.


## 1. Como usar o Gerenciador de Permissões de Função


Para começar a usar o Role Permission Manager, acesse:



>
> Início > Usuários e permissões > Gerente de permissões de função
>
>
>


![Gerencie o acesso de leitura, gravação, criação, envio e alteração usando o gerenciador de permissões de função](/files/setting-up-permissions-leave-application.png)


As permissões são aplicadas em uma combinação de:


* **Roles:** Como vimos anteriormente, Roles são atribuídos aos usuários e é sobre esses Roles que as regras de permissão são aplicadas. Por exemplo, um usuário de vendas pode receber as funções de Funcionário e Usuário de vendas.


Exemplos de Funções incluem Gerente de Contas, Funcionário, Usuário de RH, etc.
* **Tipos de documento:** cada tipo de documento, principal ou transação, tem uma lista separada de permissões baseadas em função, conforme visto na captura de tela anterior.


Exemplos de Tipos de Documentos são Fatura de Venda, Pedido de Licença, Entrada em Estoque, etc.
* **Níveis de permissão:** Em cada documento, você pode agrupar os campos por "níveis". Cada grupo de campos é indicado por um número único (0 a 9). Um conjunto separado de regras de permissão pode ser aplicado a cada grupo de campos. Por padrão, todos os campos são de nível 0.


Permissão "Nível" conecta campos com nível X a uma regra de permissão com nível X. Para saber mais clique [aqui](/docs/v13/user/manual/en/setting-up/articles/managing-perm-level).
* **Estágios do documento:** As permissões são aplicadas em cada estágio do documento, como Criação, Salvamento, Envio, Cancelamento e Alteração. Uma função pode ter permissão para imprimir, enviar por e-mail, importar ou exportar dados, acessar relatórios ou definir permissões de usuário.
* **Permissões de Usuário:** Usando Permissões de Usuário no ERPNext, um usuário pode ser restrito a acessar apenas Documentos específicos para aquele Tipo de Documento. Ex: Apenas um Território de todos os Territórios. As permissões do usuário definidas para outros tipos de documento também são aplicadas se estiverem relacionadas ao tipo de documento atual por meio de campos de link.


Por exemplo, um Cliente é um campo de link em um Pedido de Venda ou Cotação. No Gerenciador de permissões de função, as permissões do usuário podem ser definidas usando o botão 'Definir permissões do usuário'.


Para definir permissões de usuário com base em documentos/campos, acesse:



>
> Início > Usuários e permissões > Permissões > [Permissões do usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)
>
>
>
* **Adicionar uma nova regra**: No Gerenciador de permissões de função, para adicionar uma nova regra, clique no botão **Adicionar uma nova regra** e uma caixa pop-up solicitará que você selecione uma função e uma permissão Nível. Depois de selecionar isso e clicar em 'Adicionar', isso adicionará uma nova linha à sua tabela de regras.


## 2. Como funcionam as permissões com base na função


O Pedido de Licença é um bom exemplo que abrange todas as áreas de um Sistema de Permissão.


* Deve ser criado por um Funcionário.
Para isso, a função do funcionário deve receber permissões de leitura, gravação e criação.


![Concedendo permissões de leitura, gravação e criação ao funcionário para solicitação de licença](/files/setting-up-permissions-employee-role.png)
* Um **Funcionário** só deve ser capaz de acessar seu Formulário de Licença.
Portanto, o registro de permissões do usuário deve ser criado para cada combinação de usuário-funcionário.


![Limitando o acesso para deixar aplicativos para um usuário com função de funcionário por meio do Gerenciador de permissões do usuário](/files/setting-up-permissions-employee-user-permissions.png)
* Se você deseja que um **Empregado** selecione apenas um documento em outro documento e não tenha acesso de leitura a esse documento como um todo, conceda apenas permissão de seleção à função Funcionário.


![Limitando o acesso para deixar aplicativos para um usuário com função de funcionário por meio do Gerenciador de permissões do usuário](/files/setting-up-select-permissions-employee.png)
* **Gerente de RH** deve ser capaz de ver todos os pedidos de licença.
Crie uma regra de permissão para gerente de RH no nível 0, com permissões de leitura. Aplicar permissões de usuário deve ser desativado.


![Concedendo permissões de Enviar e Cancelar ao Gerente de RH para Pedidos de Licença. 'Aplicar permissões de usuário' está desmarcado para dar acesso total.](/files/setting-up-permissions-hr-manager-role.png)
* O **Aprovador de Licença** deve ser capaz de ver e atualizar os Pedidos de Licença de funcionários subordinados a ele.
O Aprovador de Licença recebe acesso de Leitura e Gravação no Nível 0. Os Documentos Relevantes do Funcionário devem ser incluídos nas Permissões do Usuário dos Aprovadores de Licença. (Esse esforço é reduzido para os Aprovadores de Licença mencionados nos Documentos do Funcionário, criando programaticamente registros de Permissão do Usuário).


![Concedendo permissões de leitura, gravação e envio para o aprovador de saída para aplicativos de licença. 'Aplicar permissões de usuário' está marcado para limitar o acesso com base no funcionário.](/files/setting-up-permissions-leave-approver-role.png)
* Deve ser Aprovado/Rejeitado apenas pelo Usuário de RH ou Aprovador de Licença.
O campo Status de um Pedido de Licença é definido no Nível 1. O Usuário de RH e o Aprovador de Licença recebem permissões de Leitura e Gravação para o Nível 0, enquanto todos os outros (Todos) recebem permissão de Leitura para o Nível 1.


![Limitando o acesso de leitura para um conjunto de campos a determinadas funções](/files/setting-up-permissions-level-1.png)
* **Usuário de RH** deve poder delegar Pedidos de Licença a seus subordinados.
O usuário de RH tem o direito de definir permissões de usuário. Um usuário com função de usuário de RH seria capaz de definir permissões de usuário no aplicativo de licença para outros usuários.


![Deixe o usuário de RH delegar acesso para sair de aplicativos marcando 'Definir permissões de usuário'. Isso permitirá que o usuário de RH acesse o Gerenciador de permissões de usuário para 'Sair do aplicativo'](/files/setting-up-permissions-hr-user-role.png)


Caso você tenha atribuído as funções corretamente, mas ainda esteja recebendo erros ao acessar os documentos, consulte [esta página](/docs/v13/user/manual/en/setting-up/articles/report-permission-error).


### 3. Tópicos Relacionados


1. [Permissões com base na função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
2. [Permissões do usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)
3. [Permissão de função para página e relatório](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report)