# Permissão de função para página e relatório



**O acesso a diferentes páginas e relatórios pode ser controlado em Permissão de função para página e relatório.**


Os tipos de documento são Pedido de Venda, Cliente, Fornecedor, etc. Eles são um **tipo de documento**, o que significa que podem conter vários documentos desse tipo. Uma página é uma página única como [Configurações de venda](/docs/pt/selling/selling-settings). Você não pode criar várias configurações de venda, mas pode criar vários pedidos de vendas.


No ERPNext, o usuário pode criar uma interface de usuário personalizada usando Page e um relatório personalizado usando o [Report Builder](https://docs.erpnext.com/docs/v13/user/videos/learn/report-builder.html) ou [Relatório de consulta](https://frappe.io/docs/v13/user/en/guides/reports-and-printing/how-to-make-query-report). ERPNext tem um [sistema de permissão baseado em funções](/docs/pt/setting-up/users-and-permissions/role-based-permissions) onde você pode atribuir funções para o usuário. A mesma função pode ser atribuída à página e ao relatório para acessá-los.


Se o usuário tiver ativado o modo de desenvolvedor, ele poderá adicionar as funções diretamente na página e no registro do relatório. Nesse caso, as permissões também serão refletidas no arquivo JSON da página/relatório. Considere que você deseja restringir os papéis que podem acessar determinadas páginas e relatórios no ERPNext, isso pode ser feito através da Permissão de Papel para Página e Relatório.


Para acessar a permissão de função para página e relatório, acesse:
> Página inicial > Usuários e permissões > Permissão de função para página e relatório


## 1. Como usar a permissão de função para a ferramenta de página e relatório


Se o modo de desenvolvedor estiver desativado, o usuário poderá atribuir as funções à página e ao relatório, usando a página "Permissão de função para página e relatório".


![Ferramentas para atribuir funções personalizadas à página](/files/role-permission-for-page-and-report.png)


### 1.1 Redefinir para os padrões


Usando o botão "Redefinir para padrões", o usuário pode remover as permissões personalizadas aplicadas em uma página ou relatório. Então, as permissões padrão serão aplicáveis ​​nessa página ou relatório.


![Redefinir as funções padrão](/files/reset-roles-permission-for-page-report.png)


## Definindo permissões de função da página/relatório como desenvolvedor


### Permissões de função para página


1. Acesse: Página inicial > Desenvolvedor > Página.
2. Adicione uma linha e selecione quais outras funções podem acessar a página.


![Atribuir funções à página](/files/roles-for-page.png)


### Permissões de função para relatório


1. Acesse: Página inicial > Desenvolvedor > Relatório.
2. Adicione linhas com funções que podem acessar o relatório.


![Atribuir funções ao relatório](/files/roles-for-report.png)


### 3. Tópicos Relacionados


1. [Função e perfil de função](/docs/pt/setting-up/users-and-permissions/role-and-role-profile)
2. [Permissões baseadas em função](/docs/pt/setting-up/users-and-permissions/role-based-permissions)
3. [Permissões do usuário](/docs/pt/setting-up/users-and-permissions/user-permissions)



