# Adicionando usuários


Os usuários podem ser adicionados pelo gerente do sistema. Para adicionar usuários acesse:



>
> Início > Usuários e permissões > Usuário
>
>
>


Existem dois tipos principais de usuários:


**Usuários do site**: Clientes, Fornecedores, Alunos, etc., que têm acesso apenas ao portal e não a nenhum módulo.
**Usuários do Sistema**: Pessoas que utilizam o ERPNext na Empresa com acesso a módulos, dados da empresa, etc.


Leia mais sobre [diferença entre usuário do sistema e do site](/docs/v13/user/manual/en/setting-up/articles/difference-between-system-user-and-website-user).


Em Usuário, muitas informações podem ser inseridas. Por uma questão de usabilidade, as informações inseridas para os usuários da web são mínimas: Nome e e-mail.


Um endereço de e-mail é a chave exclusiva (ID) que identifica os usuários.


## 1. Como criar um novo usuário


1. Vá para a lista de usuários, clique em Novo.
2. Adicione um endereço de e-mail e o nome do usuário.
3. Salve.


![Adicionar detalhes do usuário](/files/add-user-details.png)


Detalhes como nome de usuário e idioma também podem ser alterados.


## 2. Características


### 2.1 Definindo funções


Depois de salvar, você verá uma lista de funções e caixas de seleção ao lado delas. Basta verificar as funções que deseja que o usuário tenha e salvar o documento. As funções têm permissões pré-definidas, para saber mais sobre funções, [clique aqui](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions). Você pode definir [Perfis de função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-and-role-profile) para usar como um modelo que seleciona várias funções juntas.


![Funções do usuário](/files/user-2.png)


### 2.2 Mais Informações


Mais informações sobre o funcionário podem ser definidas nesta seção:


* Gênero
* Telefone
* Celular Não
* Data de nascimento
* Localização
* Interesses
* Biografia
* Imagem do banner


Marcar 'Mute Sounds' irá silenciar os sons que tocam na interação com documentos. O usuário pode precisar fazer Configurações > Recarregar para que as alterações ocorram.


### 2.3 Alterar senha


* **Definir nova senha**: Como gerente do sistema, você pode definir uma nova senha para o usuário se ela precisar ser alterada.
* **Enviar notificação de atualização de senha**: envie uma notificação por e-mail ao usuário informando que sua senha foi alterada.
* **Sair de todos os dispositivos ao alterar a senha**: Ao alterar a senha do usuário, isso desconecta o usuário do PC e de qualquer dispositivo móvel ao qual ele possa ter feito login.


### 2.4 Acompanhamento do Documento


Com esta opção você pode acompanhar vários documentos no sistema e receber notificações por e-mail quando eles forem atualizados. Saiba mais [aqui](/docs/v13/user/manual/en/setting-up/email/document-follow).


### 2.5 Configurações de e-mail


* **Enviar notificações para tópicos de e-mail**: o usuário receberá notificações para conversas por e-mail que ocorrem em tipos de documento como Oportunidades.
* **Envie-me uma cópia dos e-mails enviados**: Envia ao usuário uma cópia dos e-mails enviados. Isso é útil para acompanhar se o e-mail foi enviado.
* **Permitido em menções**: Permita que o nome deste usuário apareça nas conversas do tópico para que ele possa ser mencionado usando '@'.
* **Assinatura de e-mail**: Adicionar uma assinatura de e-mail aqui irá defini-la como padrão para todos os e-mails enviados para o usuário. Isso é diferente de um rodapé que é definido no [mestre da empresa](/docs/v13/user/manual/en/setting-up/company-setup).


### 2.6 Caixa de entrada de e-mail


Inscrever o usuário em diferentes mailing lists de sua empresa a partir desta seção. Adicione uma nova linha e selecione a lista de discussão para atribuir este usuário. Por exemplo, listas de e-mail podem ser trabalhos, suporte, vendas, etc. Para saber mais sobre a caixa de entrada de e-mail, [clique aqui](/docs/v13/user/manual/en/setting-up/email/email-inbox).


### 2.7 Permitir Acesso ao Módulo


Os usuários terão acesso a todos os módulos para os quais possuem acesso baseado em função. Se você deseja restringir o acesso de determinados módulos para este usuário, desmarque os módulos desta lista.


![Módulo de Bloco de Usuário](/files/user-3.png)


#### 2.7.1 Perfis do Módulo


Os perfis de função atuam como um modelo para armazenar e selecionar o acesso a vários módulos. Esse perfil de função pode ser atribuído a um usuário. Por exemplo, os usuários de RH terão acesso a vários módulos, como RH, folha de pagamento, etc. Os perfis de função são úteis para fornecer acesso a vários módulos ao mesmo tempo ao adicionar vários usuários.


![Perfil do Módulo](/files/module-profile.png)


### 2.8 Configurações de segurança


* **Sessões Simultâneas**: Sessões simultâneas de login ao usuário são permitidas. Você pode usar o mesmo conjunto de credenciais para vários usuários permitindo mais sessões. Isso pode ser restringido em [Configurações do sistema](/docs/v13/user/manual/en/setting-up/settings/system-settings#15-security) globalmente. Para conta na nuvem, o número total de sessões simultâneas não pode exceder o número total de usuários inscritos.
* **Tipo de usuário**: Se o usuário tiver qualquer função marcada além de Cliente, Fornecedor, Paciente ou Aluno, ele se tornará automaticamente um Usuário do Sistema. Este campo é só de leitura.
* **Login After, Login Before**: Caso deseje dar ao usuário acesso ao sistema somente entre o horário comercial,
ou durante os fins de semana, especifique aqui. Por exemplo, se o horário comercial for das 10h às 18h, defina o horário de login após, login antes como 10:00 e 18:00.
* **Restringir IP**: Restrinja o login do usuário aos IPs especificados aqui. Isso pode ser usado para que o usuário possa fazer login apenas nos computadores do escritório. Vários IPs podem ser adicionados separados por vírgulas.


Esta seção também mostra outros detalhes como Último Login, Último IP e Hora da Última Atividade para o usuário.


### 2.9 Autenticação de terceiros


Isso permitirá que os usuários usem o Facebook, Google ou GitHub para fazer login. Para usar esse recurso, inscreva-se em uma conta de desenvolvedor no Facebook, Google, GitHub etc. Crie um aplicativo em seu console, especifique um nome de aplicativo, o URL de origem e URL de retorno de chamada, copie o ID do cliente e as informações secretas do cliente aqui para começar a usar.


Para mais detalhes, vá para [esta página](https://frappe.io/docs/v13/user/en/guides/deployment/how-to-enable-social-logins).


### 2.10 Acesso à API


Você pode gerar chaves secretas de API nesta seção usando o botão Gerar chaves. Isso pode ser usado para acessar os dados da sua conta de outro aplicativo, por exemplo, um sistema POS offline.


### 2.11 Depois de salvar


Depois de salvar um usuário, esses botões serão vistos na área do painel do mestre do usuário.


![Botões do painel do usuário](/files/user-after-save.png)


#### Permissões


* **Definir permissões de usuário**: levará você à página [Permissões de usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions) página de Bruce de onde você pode restringir o acesso de Bruce aos documentos.
* **Exibir documentos permitidos**: levará você ao relatório 'Documentos permitidos para o usuário' desse usuário. Aqui você pode ver a quais documentos Bruce tem acesso. Por exemplo, no Pedido de venda selecionado, será exibida a lista de Pedidos de venda aos quais Bruce tem acesso.


#### Senha


* **Redefinir senha**: Um e-mail com instruções para redefinir a senha do usuário será enviado para a [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account) do usuário.
* **Redefinir Segredo OTP**: Redefinir Segredo OTP para fazer login via Autenticação de Dois Fatores.


Criar e-mail do usuário permitirá que você crie uma [conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account) para o usuário com base no e-mail inserido no mestre do usuário.


### 3. Métodos de Login


Em Configurações do sistema, na seção Segurança, se você marcar a caixa de seleção 'Permitir login usando número de celular', um número de celular também poderá ser usado para fazer login. Embora um número de celular seja exclusivo, ele não será tratado como um ID de usuário .


Entrar com e-mail:


![Login por e-mail](/files/user-login-email.png)


Entrar com e-mail ou celular:


![Mobile No Login](/files/user-login-mobile.png)


Depois de adicionar esses detalhes, salve o usuário.


### 4. Tópicos Relacionados


1. [Permissões com base na função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
2. [Permissões do usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)
3. [Document Follow](/docs/v13/user/manual/en/setting-up/email/document-follow)