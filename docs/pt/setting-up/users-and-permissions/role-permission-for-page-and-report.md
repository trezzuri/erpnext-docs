# Permissão de função para página e relatório


**O acesso a diferentes páginas e relatórios pode ser controlado em Permissão de Função para Página e Relatório.**


Os tipos de documentos são Pedido de Vendas, Cliente, Fornecedor, etc. Eles são um **tipo de documento**, o que significa que podem conter vários documentos desse tipo. Uma página é uma única página como [Configurações de venda](/docs/v13/user/manual/en/selling/selling-settings). Você não pode criar várias configurações de venda, mas pode criar vários pedidos de venda.


No ERPNext, o usuário pode criar uma interface de usuário personalizada usando Page e um relatório personalizado usando [Report Builder](/docs/v13/user/videos/learn/report-builder.html) ou [Query Report](https://frappe .io/docs/v13/user/en/guides/reports-and-printing/how-to-make-query-report). O ERPNext possui um [sistema de permissão baseado em função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions) onde você pode atribuir funções ao usuário. A mesma função pode ser atribuída à página e relatório para acessá-los.


Se o usuário habilitou o modo de desenvolvedor, ele pode adicionar as funções diretamente na página e registrar o relatório. Nesse caso, as permissões também serão refletidas no arquivo JSON da página/relatório. Considere que você deseja restringir as funções que podem acessar determinadas páginas e relatórios no ERPNext, isso pode ser feito por meio da Permissão de Função para Página e Relatório.


Para acessar a permissão de função para página e relatório, acesse:



>
> Início > Usuários e permissões > Permissão de função para página e relatório
>
>
>


## 1. Como usar a permissão de função para a ferramenta de página e relatório


Se o modo de desenvolvedor estiver desativado, o usuário pode atribuir as funções à página e ao relatório, usando a página "Permissão de função para página e relatório".


![Ferramentas para atribuir funções personalizadas à página](/files/role-permission-for-page-and-report.png)


### 1.1 Redefinir para os padrões


Usando o botão "Redefinir para os padrões", o usuário pode remover as permissões personalizadas aplicadas em uma página ou relatório. Em seguida, as permissões padrão serão aplicáveis ​​a essa página ou relatório.


![Redefinir as funções padrão](/files/reset-roles-permission-for-page-report.png)


## Definindo permissões de função da página/relatório como desenvolvedor


### Permissões de função para página


1. Vá para: Início > Desenvolvedor > Página.
2. Adicione uma linha e selecione quais outras funções podem acessar a página.


![Atribuir funções à página](/files/roles-for-page.png)


### Permissões de função para relatório


1. Vá para: Início > Desenvolvedor > Relatório.
2. Adicione linhas com funções que podem acessar o relatório.


![Atribuir funções ao relatório](/files/roles-for-report.png)


### 3. Tópicos Relacionados


1. [Perfil de Função e Função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-and-role-profile)
2. [Permissões com base na função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
3. [Permissões do usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)