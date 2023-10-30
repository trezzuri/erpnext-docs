# Permissões do usuário



**As permissões do usuário são uma forma de restringir o acesso do usuário a documentos específicos.**


As permissões baseadas em função permitem definir acesso completo (por padrão) a um tipo de documento (doctype), como fatura de vendas, pedidos, cotação, etc. Isso significa que quando você atribui uma função de usuário de vendas a um usuário, ele pode acessar todos os Pedidos de vendas e cotações.


As permissões do usuário podem ser usadas para restringir o acesso a documentos selecionados com base nos campos de link do documento. Por exemplo, considere que você faz negócios com vários territórios e deseja restringir o acesso de determinados usuários de vendas a cotações/pedidos de vendas pertencentes a um determinado território. Isso pode ser feito por meio de permissões de usuário. As restrições podem ser definidas para Cliente, Fornecedor, Grupo de Clientes, Grupo de Fornecedores, etc.


A definição de permissões do usuário é particularmente útil quando você deseja restringir com base em:


1. Permitir que o usuário acesse dados pertencentes a uma empresa
2. Permitir que o usuário acesse dados relacionados a um cliente ou território específico


Para acessar as permissões do usuário, vá para:
> Página inicial > Usuário e permissões > Permissões do usuário


## 1. Como criar permissões de usuário


1. Vá para a lista de permissões do usuário e clique em Novo.
2. Selecione o usuário ao qual a regra deve ser aplicada.
3. Selecione o tipo de documento a ser permitido (por exemplo "Empresa").
4. Em For Value, selecione o item específico que você deseja permitir (o nome da "Empresa").
5. Se você marcar 'É padrão', o valor selecionado em 'For Value' será usado por padrão para quaisquer transações futuras deste usuário. Isso se a empresa 'Unico Plastics Inc.' for selecionado como 'For Value', esta Empresa será definida como padrão para todas as transações futuras deste usuário.


![Criando uma nova permissão de usuário](/files/new-user-permission.png)


> Observação: somente uma permissão de usuário pode ser definida como padrão para um tipo de documento específico para um usuário específico.


## 2. Mais ações de permissão do usuário


### 2.1 Controle Avançado


No Controle Avançado, você pode controlar melhor onde a permissão do usuário é aplicada.


### 2.1.1. Aplicável para


Opcionalmente, você pode aplicar permissões de usuário apenas para um tipo de documento específico, definindo o Tipo de documento após desmarcar a caixa de seleção Aplicar a todos os tipos de documento.
Definir a opção **Aplicável para** tornará a permissão do usuário atual aplicável somente no tipo de documento mestre selecionado.


![Aplicável para](/files/advanced-control.png)


Na Permissão de Usuário acima, o usuário poderá acessar apenas os Pedidos de Vendas da empresa selecionada.


**Observação:** se **Aplicável para** não estiver definido, a permissão do usuário será aplicada a todos os tipos de documentos relacionados.


### 2.1.2. Ocultar descendentes


O valor de **Permitir** pode ser um DocType com uma visualização em árvore, que terá registros com um relacionamento pai-filho ou ancestral-descendente.


Vamos supor que **For Value**, 'Unico Plastics Inc.', tenha uma empresa filha, 'Unico Toys'. Quando uma permissão de usuário é criada para 'Unico Plastics Inc.', também são concedidas permissões para seus descendentes.


**Ocultar descendentes** fica visível somente ao selecionar um tipo de documento de exibição em árvore. Ao ativar esta caixa de seleção, as permissões para descendentes de **For Value** não serão concedidas.


![Ocultar permissões descendentes](/files/hide-descendant-permissions.png)


Um usuário que pode visualizar registros da 'Unico Plastics Inc.' não será possível visualizar os de 'Unico Toys'.


### 2.2 Ignorando permissões de usuário em determinados campos


Outra maneira de permitir que os documentos sejam vistos por todos que foram restringidos pelas permissões do usuário é marcar "Ignorar permissões do usuário" em um campo específico acessando **Personalizar formulário**.


Por exemplo, se você não quiser que os Ativos sejam restritos a nenhum usuário, selecione **Ativo** no tipo de formulário. Na tabela de campos, expanda o campo Empresa e marque "Ignorar permissões do usuário".


![Ignorar permissões do usuário em propriedades específicas](/files/ignore-user-permissions.png)


### 2.3 Permissões estritas


Isso restringe o acesso do usuário aos documentos de maneira mais rigorosa.


Para saber mais, acesse a [página Configurações do sistema](/docs/pt/setting-up/settings/system-settings#14-permissions).


### 2.4 Verificando como as permissões do usuário são aplicadas


Finalmente, depois de criar seu modelo de permissão hermético e desejar verificar como ele se aplica a vários usuários. Você pode ver isso no relatório **Documentos permitidos para o usuário**. Usando este relatório, você pode selecionar o **Usuário** e o tipo de documento e visualizar quais documentos um determinado usuário pode acessar.


Marcar a caixa de seleção Mostrar permissões mostrará a leitura/gravação/envio e outros níveis de acesso.


![Relatório de documentos permitidos para usuário](/files/permitted-documents.png)


Observação: se você não conseguir acessar o pedido de vendas ou qualquer outro tipo de documento nesta lista, certifique-se de ter definido o [funções](/docs/pt/setting-up/users-and-permissions/role-based-permissions) corretamente.


Por exemplo, o usuário Bruce está restrito à Empresa 'Unico Plastics Inc.'
![Usuário restrito à empresa](/files/user-restricted-to-company.png)


### 3. Tópicos Relacionados


1. [Adicionar usuários](/docs/pt/setting-up/users-and-permissions/adding-users)
2. [Função e perfil de função](/docs/pt/setting-up/users-and-permissions/role-and-role-profile)
3. [Permissões baseadas em função](/docs/pt/setting-up/users-and-permissions/role-based-permissions)
4. [Permissão de função para página e relatório](/docs/pt/setting-up/users-and-permissions/role-permission-for-page-and-report)



