# Usuário limitado


**O usuário terá acesso limitado ao sistema.**


Usuários limitados podem acessar apenas documentos específicos dos módulos específicos. Certos usuários não utilizam todos os módulos e precisam apenas de módulos específicos. Por exemplo, na empresa, para registrar o comparecimento diário ou aplicativo de licença, todos os funcionários receberam o acesso necessário ao sistema. Mas suponha que 500 pessoas estejam trabalhando na empresa, das quais apenas 100 usam todos os documentos e as 400 restantes precisam apenas de documentos para comparecimento diário ou pedidos de licença. Esses usuários são usuários limitados.


O documento User Type desempenha um papel importante para lidar com este caso de uso. Existem tipos de usuário padrão, "Usuário do sistema" e "Usuário do site", o usuário do sistema pode acessar a mesa e o portal do site, enquanto o usuário do site só pode acessar o portal do site. Para lidar com o caso de acesso limitado de documentos para os funcionários por padrão, o SOMA adicionou um novo tipo de usuário 'Autoatendimento do funcionário'.


## Tipo de usuário


Para acessar o documento User Type, acesse:



> 
> Usuários > Tipo de usuário
> 
> 
> 


![User Type](/files/user-type.png)


O usuário do site e o usuário do sistema serão tipos de usuário padrão e não podem ser excluídos ou editados. No entanto, tipos de usuário não padrão (Personalizados) podem ser excluídos, criados e editados. Por padrão, os direitos de exclusão não são concedidos a nenhum usuário.


## Tipo de usuário não padrão


1) Para o tipo de usuário não padrão, o usuário deve selecionar a função personalizada, o documento no qual deseja aplicar a permissão do usuário e o nome do campo do usuário.


![User Type](/files/user-type-role.png)


Na imagem acima, Funcionário tem o campo de link User ID que está vinculado ao documento do usuário. Como "Aplicar permissão do usuário em" foi definido como "Empregado", o usuário do respectivo funcionário só pode visualizar os documentos nos quais o respectivo campo do funcionário está vinculado. Por exemplo, o funcionário só pode visualizar o recibo de salário que foi criado em relação ao seu ID de funcionário.


2) Tipos de documento:


Os usuários do tipo de usuário não padrão só podem acessar os documentos que foram mencionados no tipo de usuário.


![User Type](/files/user-type-document-type.png)


A tabela acima também atua como Gerente de permissão de função para esse tipo de usuário específico (Autoatendimento do funcionário em nosso caso). Autoatendimento do funcionário como uma função não estará acessível no Gerenciador de permissão de função geral.


3) Tipos de documentos (somente permissões selecionadas):


Nesta tabela, você precisa listar todos os tipos de documento aos quais deseja que o usuário do Employee Self Service tenha acesso SELECT. Não há limite para o número de doctypes que você pode adicionar aqui. Os usuários não poderão criar os registros para os documentos aos quais eles têm acesso perm Select.


![User Type](/files/user-type-select-perm.png)


## Adicionando usuário não padrão


Ao adicionar o novo usuário, o usuário precisa selecionar o tipo de usuário. No caso de um tipo de usuário não padrão, o respectivo usuário deve ser vinculado ao documento que foi definido no campo "Aplicar permissão de usuário em".


![Tipo de usuário](/files/limited-access-user.png)

