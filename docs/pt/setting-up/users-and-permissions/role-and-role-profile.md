# Função e perfil da função


**Uma função define as permissões para acessar vários documentos no ERPNext.**


As funções definem um conjunto de permissões que podem ser definidas no [Gerenciador de permissões de funções](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions). As funções mais utilizadas já estão definidas no ERPNext, você pode utilizar o sistema com elas. Se necessário, você pode adicionar mais funções. Por exemplo, se você atribuir a função de Usuário de vendas a um usuário, ele poderá acessar documentos como Cotações e Pedidos de venda, pois as permissões já estão definidas para a função de Usuário de vendas.


**Perfis de função armazenam diferentes funções para que várias funções possam ser atribuídas de uma só vez.**


Os perfis de função atuam como um modelo para armazenar e selecionar várias funções. Este perfil de função pode então ser atribuído a um [usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/adding-users). Por exemplo, um Supervisor de Vendas terá as funções Funcionário, Gerente de Vendas, Usuário de Vendas e Gerente Principal de Vendas. Os perfis de função são úteis para atribuir várias funções ao mesmo tempo ao adicionar vários funcionários.


Para acessar a função, vá para:



>
> Início > Usuários e permissões > Função
>
>
>


## 1. Como adicionar uma Função


1. Vá para a lista Função, clique em Novo.
2. Insira um nome para a função.
3. Escolha se a Função tem acesso à área de trabalho. Uma função que tem acesso de mesa pode acessar os módulos do ERPNext e os documentos da empresa. O nível de acesso depende das funções atribuídas ao usuário.
4. Salve.


Você pode adicionar autenticação de dois fatores para a função e também restringi-la a um domínio específico. A partir daqui, você pode ir para o [Roles Permission Manager](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions) e definir permissões para a função em diferentes DocTypes .


![Permissões para nova função](/files/role-permissions.png)


## 2. Como adicionar um perfil de função


Para acessar o perfil da função, acesse:



>
> Início > Usuários e permissões > Permissões > Perfil da função
>
>
>


1. Vá para a lista Perfil da Função, clique em Novo.
2. Insira um nome.
3. Selecione as funções que deseja atribuir a este perfil.
4. Salve.


![Perfil da função](/files/role-profile.png)


### 3. Tópicos Relacionados


1. [Permissões com base na função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
2. [Permissões do usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)
3. [Permissão de função para página e relatório](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report)