# Função e perfil da função



**Uma função define as permissões para acessar vários documentos no ERPNext.**


As funções definem um conjunto de permissões que podem ser definidas na [Permissão de funções Gerente](/docs/pt/setting-up/users-and-permissions/role-based-permissions). As funções mais comumente usadas já estão definidas no ERPNext, você pode usar o sistema com elas. Se necessário, você pode adicionar mais funções. Por exemplo, se você atribuir a função de usuário de vendas a um usuário, ele poderá acessar documentos como cotações e pedidos de vendas, pois as permissões já estão definidas para a função de usuário de vendas.


**Os perfis de função armazenam diferentes funções para que várias funções possam ser atribuídas ao mesmo tempo.**


Os perfis de função funcionam como um modelo para armazenar e selecionar diversas funções. Este perfil de função pode então ser atribuído a um [Usuário](/docs/pt/setting-up/users-and-permissions/adding-users). Por exemplo, um Supervisor de Vendas terá as funções Funcionário, Gerente de Vendas, Usuário de Vendas e Gerente Mestre de Vendas. Os perfis de função são úteis para atribuir várias funções ao mesmo tempo ao adicionar vários funcionários.


Para acessar a Função, acesse:



> 
> Página inicial > Usuários e permissões > Função
> 
> 
> 


## 1. Como adicionar uma função


1. Vá para a lista Função e clique em Novo.
2. Insira um nome para a função.
3. Escolha se a função tem acesso à mesa. Uma função que tenha acesso à mesa pode acessar os módulos do ERPNext e os documentos da empresa. O nível de acesso depende das funções atribuídas ao usuário.
4. Salvar.


Você pode adicionar autenticação de dois fatores para a função e também restringi-la a um domínio específico. A partir daqui, você pode acessar o [Gerenciador de permissões de funções](/docs/pt/setting-up/users-and-permissions/role-based-permissions) e definir permissões para a função em diferentes DocTypes.


![Permissões para nova função](/files/role-permissions.png)


## 2. Como adicionar um perfil de função


Para acessar o perfil da função, acesse:



> 
> Página inicial > Usuários e permissões > Permissões > Perfil de função
> 
> 
> 


1. Vá para a lista Perfil da função e clique em Novo.
2. Digite um nome.
3. Selecione as funções que deseja atribuir a este perfil.
4. Salvar.


![Role Profile](/files/role-profile.png)


### 3. Tópicos Relacionados


1. [Permissões baseadas em função](/docs/pt/setting-up/users-and-permissions/role-based-permissions)
2. [Permissões do usuário](/docs/pt/setting-up/users-and-permissions/user-permissions)
3. [Permissão de função para página e relatório](/docs/pt/setting-up/users-and-permissions/role-permission-for-page-and-report)



