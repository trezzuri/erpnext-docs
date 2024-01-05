# Adicionando usuários



Usuários podem ser adicionados pelo Gerente do Sistema. Para adicionar usuários acesse:
> Página inicial > Usuários e permissões > Usuário


Existem dois tipos principais de usuários:


**Usuários do site**: Clientes, Fornecedores, Estudantes, etc., que têm acesso apenas ao portal e não a nenhum módulo.
**Usuários do Sistema**: Pessoas que usam o ERPNext na Empresa com acesso a módulos, dados da empresa, etc.


Leia mais sobre a [diferença entre o usuário do sistema e o usuário do site](/docs/pt/setting-up/articles/difference-between-system-user-and-website-user).


Em Usuário, muitas informações podem ser inseridas. Por uma questão de usabilidade, as informações inseridas para os usuários da web são mínimas: Nome e E-mail.


Um endereço de e-mail é a chave exclusiva (ID) que identifica os usuários.


## 1. Como criar um novo usuário


1. Vá para a lista de usuários e clique em Novo.
2. Adicione um endereço de e-mail e o nome do usuário.
3. Salvar.


![Adicionar detalhes do usuário](/files/add-user-details.png)


Detalhes como nome de usuário e idioma também podem ser alterados.


## 2. Recursos


### 2.1 Definindo funções


Depois de salvar, você verá uma lista de funções e caixas de seleção ao lado delas. Basta verificar as funções que você deseja que o usuário tenha e salvar o documento. As funções possuem permissões predefinidas, para saber mais sobre funções, [clique aqui](/docs/pt/setting-up/users-and-permissions/role-based-permissions). Você pode definir [Perfis de função](/docs/pt/setting-up/users-and-permissions/role-and-role-profile) para usar como modelo que seleciona várias funções juntas.


![Funções do usuário](/files/user-2.png)


### 2.2 Mais informações


Mais informações sobre o funcionário podem ser definidas nesta seção:


* Gênero
* Telefone
* Celular Não
* Data de nascimento
* Localização
* Interesses
* Biografia
* Imagem do banner


Marcar 'Silenciar sons' silenciará os sons reproduzidos ao interagir com documentos. O usuário pode precisar fazer Configurações > Recarregar para que as alterações ocorram.


### 2.3 Alterar senha


* **Definir nova senha**: como gerente do sistema, você pode definir uma nova senha para o usuário caso ela precise ser alterada.
* **Enviar notificação de atualização de senha**: envie uma notificação por e-mail ao usuário informando que sua senha foi alterada.
* **Sair de todos os dispositivos ao alterar a senha**: ao alterar a senha do usuário, isso desconecta o usuário do PC e de qualquer dispositivo móvel no qual ele possa estar conectado.


### 2.4 Acompanhamento de documento


Com esta opção você pode acompanhar diversos documentos no sistema e receber notificações por e-mail quando eles forem atualizados. Saiba mais [aqui](/docs/pt/setting-up/email/document-follow).


### 2.5 Configurações de e-mail


* **Enviar notificações para conversas por e-mail**: o usuário receberá notificações sobre conversas por e-mail que ocorrem em tipos de documentos como Oportunidades.
* **Envie-me uma cópia dos e-mails enviados**: envia ao usuário uma cópia dos e-mails enviados. Isso é útil para controlar se o e-mail foi enviado.
* **Menções permitidas**: permite que o nome deste usuário apareça nas conversas para que ele possa ser mencionado usando '@'.
* **Assinatura de e-mail**: adicionar uma assinatura de e-mail aqui irá defini-la como padrão para todos os e-mails enviados para o usuário. Isso é diferente de um rodapé definido no [mestre da empresa](/docs/pt/setting-up/company-setup).


### 2.6 Caixa de entrada de e-mail


Inscreva o usuário em diferentes mailing lists da sua empresa nesta seção. Adicione uma nova linha e selecione a lista de e-mails para atribuir este usuário. Por exemplo, listas de e-mail podem ser empregos, suporte, vendas, etc. Para saber mais sobre o Email Inbox, [clique aqui](/docs/pt/setting-up/email/email-inbox).


### 2.7 Permitir acesso ao módulo


Os usuários terão acesso a todos os módulos aos quais possuem acesso baseado em função. Se você deseja restringir o acesso de determinados módulos para este usuário, desmarque os módulos desta lista.


![Módulo de bloqueio de usuário](/files/user-3.png)


#### 2.7.1 Perfis de módulo


Os perfis de função atuam como um modelo para armazenar e selecionar o acesso a vários módulos. Este perfil de função pode então ser atribuído a um usuário. Por exemplo, os usuários de RH terão acesso a vários módulos, como RH, folha de pagamento, etc. Os perfis de função são úteis para fornecer acesso a vários módulos de uma vez ao adicionar vários usuários.


![Perfil do módulo](/files/module-profile.png)


### 2.8 Configurações de segurança


* **Sessões Simultâneas**: Sessões de login simultâneas permitidas ao usuário. Você pode usar o mesmo conjunto de credenciais para vários usuários permitindo mais sessões. Isso pode ser restrito nas [Configurações do sistema](/docs/pt/setting-up/settings/system-settings#15-security) globalmente. Para conta na nuvem, o número total de sessões simultâneas não pode exceder o número total de usuários inscritos.
* **Tipo de Usuário**: Se o usuário tiver qualquer função marcada além de Cliente, Fornecedor, Paciente ou Estudante, ele automaticamente se tornará um Usuário do Sistema. Este campo é somente leitura.
* **Login Depois, Login Antes**: Se desejar dar ao usuário acesso ao sistema apenas entre o horário comercial,
ou durante os finais de semana, especifique aqui. Por exemplo, se o horário comercial for das 10h às 18h, defina o horário de Login Depois e Login Antes como 10h e 18h.
* **Restringir IP**: Restrinja o login do usuário aos IPs especificados aqui. Isso pode ser usado para que o usuário possa fazer login apenas nos computadores do escritório. Vários IPs podem ser adicionados separados por vírgulas.


Esta seção também mostra outros detalhes, como Último login, Último IP e Horário da última atividade do usuário.


### 2.9 Autenticação de terceiros


Isso permitirá que os usuários usem o Facebook, o Google ou o GitHub para fazer login. Para usar esse recurso, inscreva-se em uma conta de desenvolvedor no Facebook, Google, GitHub etc. o URL de origem e o URL de retorno de chamada, copie o ID do cliente e as informações secretas do cliente aqui para começar a usar.


Para mais detalhes, acesse [esta página](https://frappe.io/docs/v13/user/en/guides/deployment/how-to-enable-social-logins).


### 2.10 Acesso à API


Você pode gerar chaves secretas de API nesta seção usando o botão Gerar chaves. Isso pode ser usado para acessar os dados da sua conta a partir de outro aplicativo, por exemplo, um sistema POS off-line.


### 2.11 Depois de salvar


Depois de salvar um usuário, esses botões serão vistos na área do painel do usuário mestre.


![Botões do painel do usuário](/files/user-after-save.png)


#### Permissões


* **Definir permissões do usuário**: levará você para  [Página de permissões do usuário](/docs/pt/setting-up/users-and-permissions/user-permissions) de Bruce, onde você pode restringir o acesso de Bruce aos documentos.
* **Visualizar documentos permitidos**: levará você ao relatório 'Documentos permitidos para o usuário' deste usuário. Aqui você pode ver a quais documentos Bruce tem acesso. Por exemplo, no pedido de vendas selecionado, será exibida a lista de pedidos de vendas aos quais Bruce tem acesso.


#### Senha


* **Redefinir senha**: um e-mail com instruções para redefinir a senha do usuário será enviado para o [Conta de e-mail](/docs/pt/setting-up/email/do usuário email-account).
* **Redefinir segredo OTP**: redefina o segredo OTP para fazer login por meio da autenticação de dois fatores.


Criar e-mail do usuário permitirá que você crie uma [Conta de e-mail](/docs/pt/setting-up/email/email-account) para o usuário com base no e-mail inserido no cadastro de usuários.


### 3. Métodos de login


Nas configurações do sistema, na seção Segurança, se você marcar a caixa de seleção "Permitir login usando número de celular", um número de celular também poderá ser usado para fazer login. Embora um número de celular seja exclusivo, ele não será tratado como um ID de usuário.


Login com e-mail:


![Login de e-mail](/files/user-login-email.png)


Login com e-mail ou celular:


![Celular sem login](/files/user-login-mobile.png)


Depois de adicionar esses detalhes, salve o usuário.


### 4. Tópicos Relacionados


1. [Permissões baseadas em função](/docs/pt/setting-up/users-and-permissions/role-based-permissions)
2. [Permissões do usuário](/docs/pt/setting-up/users-and-permissions/user-permissions)
3. [Acompanhamento de documento](/docs/pt/setting-up/email/document-follow)



