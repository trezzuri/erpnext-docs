# Permissões do usuário


**As permissões do usuário são uma forma de restringir o acesso do usuário a determinados documentos.**


As permissões baseadas em função permitem configurar o acesso completo (por padrão) a um tipo de documento (doctype) como fatura de vendas, pedidos, cotação etc. Isso significa que quando você atribui uma função de usuário de vendas a um usuário, ele pode acessar todas Pedidos de vendas e cotações.


As permissões do usuário podem ser usadas para restringir o acesso a documentos selecionados com base nos campos de link no documento. Por exemplo, considere que você faz negócios com vários territórios e deseja restringir o acesso de determinados Usuários de Vendas a Cotações/Pedido de Vendas pertencentes a um determinado território. Isso pode ser feito por meio de Permissões do usuário. As restrições podem ser definidas no Cliente, Fornecedor, Grupo de Clientes, Grupo de Fornecedores, etc.


A definição de permissões do usuário é particularmente útil quando você deseja restringir com base em:


1. Permitir que o usuário acesse dados pertencentes a uma empresa
2. Permitir que o usuário acesse dados relacionados a um cliente ou território específico


Para acessar as permissões do usuário, acesse:



> 
> Página inicial > Usuário e permissões > Permissões do usuário
> 
> 
> 


## 1. Como criar permissões de usuário


1. Vá para a lista de permissões do usuário, clique em Novo.
2. Selecione o usuário para o qual a regra deve ser aplicada.
3. Selecione o tipo de documento a ser permitido (por exemplo, "Empresa").
4. Em Valor, selecione o item específico que deseja permitir (o nome da "Empresa").
5. Se você marcar 'Is Default', o valor selecionado em 'For Value' será usado por padrão para quaisquer transações futuras deste usuário. Isto é, se a empresa 'Unico Plastics Inc.' for selecionado como 'For Value', esta empresa será definida como padrão para todas as transações futuras deste usuário.


![Criando uma nova permissão de usuário](/files/new-user-permission.png)



> 
> Observação: apenas uma única permissão de usuário pode ser definida como padrão para um determinado tipo de documento para um usuário específico.
> 
> 
>


## 2. Mais ações de permissão do usuário


### 2.1 Controle Avançado


No Controle Avançado, você pode ter um melhor controle sobre onde a Permissão do Usuário é aplicada.


### 2.1.1. Aplicável para


Você pode, opcionalmente, aplicar permissões de usuário apenas para um tipo de documento específico, definindo o Tipo de documento após desmarcar a caixa de seleção Aplicar a todos os tipos de documento.
Definir a opção **Aplicável a** tornará a permissão do usuário atual aplicável somente no mestre de Tipo de Documento selecionado.


![Aplicável para](/files/advanced-control.png)


Na Permissão do Usuário acima, o usuário poderá acessar apenas os Pedidos de Vendas da empresa selecionada.


**Observação:** se **Aplicável a** não estiver definido, a permissão do usuário será aplicada a todos os tipos de documentos relacionados.


### 2.1.2. Ocultar Descendentes


O valor de **Allow** pode ser um DocType com uma exibição em árvore, que terá registros com um relacionamento pai-filho ou ancestral-descendente.


Vamos assumir que **For Value**, 'Unico Plastics Inc.', tem uma empresa filha 'Unico Toys'. Quando uma Permissão de Usuário é criada para 'Unico Plastics Inc.', permissões para seus descendentes também são concedidas.


**Ocultar descendentes** é visível apenas ao selecionar um DocType de visualização em árvore. Ao ativar esta caixa de seleção, as permissões para descendentes de **For Value** não serão concedidas.


![Ocultar permissões descendentes](/files/hide-descendant-permissions.png)


Um usuário que pode visualizar registros de 'Unico Plastics Inc.' não poderá visualizar os de 'Unico Toys'.


### 2.2 Ignorando as permissões do usuário em determinados campos


Outra forma de permitir que os documentos sejam vistos por todos que foram restritos por permissões de usuário é marcar "Ignorar permissões de usuário" em um campo específico indo para **Personalizar formulário**.


Por exemplo, você não deseja que os Ativos sejam restritos a nenhum usuário, então selecione **Ativo** no tipo de formulário. Na tabela de campos, expanda o campo Empresa e marque "Ignorar permissões do usuário".


![Ignorar permissões de usuário em propriedades específicas](/files/ignore-user-permissions.png)


### 2.3 Permissões estritas


Isso restringe o acesso do usuário aos documentos de forma mais estrita.


Para saber mais, acesse a [página de configurações do sistema](/docs/pt/setting-up/settings/system-settings#14-permissions).< /p>
### 2.4 Verificando como as permissões do usuário são aplicadas


Finalmente, depois de criar seu modelo de permissão hermético, você deseja verificar como ele se aplica a vários usuários. Você pode vê-lo por meio do relatório **Documentos permitidos para o usuário**. Usando este relatório, você pode selecionar o **Usuário** e o tipo de documento e visualizar quais documentos um determinado usuário pode acessar.


Marcar a caixa de seleção Mostrar permissões mostrará a leitura/gravação/envio e outros níveis de acesso.


![Documentos permitidos para relatório do usuário](/files/permitted-documents.png)


Observação: Se você não puder acessar o Pedido de Vendas ou qualquer outro tipo de documento nesta lista, certifique-se de definir o [funções](/docs/pt/setting-up/users-and -permissions/role-based-permissions) corretamente.


Por exemplo, o usuário Bruce está restrito à empresa 'Unico Plastics Inc.'
![Usuário restrito à empresa](/files/user-restricted-to-company.png)


### 3. Tópicos Relacionados


1. [Adicionar usuários](/docs/pt/setting-up/users-and-permissions/adding-users)
2. [Função e perfil da função](/docs/pt/setting-up/users-and-permissions/role-and-role-profile)
3. [Permissões baseadas em funções](/docs/pt/setting-up/users-and-permissions/role-based-permissions)
4. [Permissão de função para página e relatório](/docs/pt/setting-up/users-and-permissions/role-permission-for-page-and-report)


