# Usuário Limitado



**O usuário terá acesso limitado ao sistema.**


Usuários limitados podem acessar apenas documentos específicos de módulos específicos. Certos usuários não usam todos os módulos e precisam apenas de módulos específicos. Por exemplo, na empresa, para registrar a frequência diária ou o pedido de licença, cada funcionário recebeu o acesso necessário ao sistema. Mas suponhamos que 500 pessoas trabalham na empresa, das quais apenas 100 utilizam todos os documentos e as restantes 400 necessitam apenas de documentos para presença diária ou pedidos de licença. Esses usuários são usuários limitados.


O documento User Type desempenha um papel importante para lidar com esse caso de uso. Existem tipos de usuário padrão, "Usuário do sistema" e "Usuário do site", o usuário do sistema pode acessar a mesa e o portal do site, enquanto o usuário do site só pode acessar o portal do site. Para lidar com o caso de acesso limitado de documentos para os funcionários por padrão, o ERPNext adicionou um novo tipo de usuário 'Employee Self Service'.


## Tipo de usuário


Para acessar o documento User Type, vá para:


> Usuários > Tipo de usuário


![User Type](/files/user-type.png)


Usuário do site e Usuário do sistema serão tipos de usuário padrão e não podem ser excluídos ou editados. No entanto, tipos de usuários não padrão (Personalizados) podem ser excluídos, criados e editados. Por padrão, os direitos de exclusão não são concedidos a nenhum usuário.


## Tipo de usuário não padrão


1) Para o tipo de usuário não padrão, o usuário deve selecionar a função personalizada, o documento ao qual deseja aplicar a permissão do usuário e o nome do campo do usuário.


![User Type](/files/user-type-role.png)


Na imagem acima, Funcionário possui o campo de link ID do usuário que está vinculado ao documento do usuário. Como a opção "Aplicar permissão do usuário em" foi definida como "Funcionário", o respectivo usuário do funcionário só poderá visualizar os documentos nos quais o respectivo campo do funcionário estiver vinculado. Por exemplo, o funcionário só pode visualizar o comprovante de salário que foi criado em relação ao seu ID de funcionário.


2) Tipos de documentos:


Os usuários do tipo de usuário não padrão só podem acessar os documentos mencionados no tipo de usuário.


![User Type](/files/user-type-document-type.png)


A tabela acima também atua como o Gerenciador de permissões de função para esse tipo de usuário específico (Autoatendimento para funcionários, em nosso caso). O Autoatendimento do funcionário como função não estará acessível no Gerenciador de permissões de função geral.


3) Tipos de documentos (somente permissões selecionadas):


Nesta tabela, você precisa listar todos os tipos de documentos aos quais deseja que o usuário do Employee Self Service tenha acesso SELECT. Não há limite para o número de doctypes que você pode adicionar aqui. Os usuários não poderão criar registros para os documentos aos quais têm acesso Select perm.


![User Type](/files/user-type-select-perm.png)


## Adicionando usuário não padrão


Ao adicionar o novo usuário, o usuário precisa selecionar o tipo de usuário. No caso de um tipo de usuário não padrão, o respectivo usuário deverá estar vinculado ao documento que foi definido no campo "Aplicar permissão de usuário em".


![User Type](/files/limited-access-user.png)



