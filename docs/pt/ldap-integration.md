# Configurando LDAP



O Lightweight Directory Access Protocol (LDAP) é um sistema de controle de acesso centralizado usado por muitas organizações de pequeno e médio porte.


Ao configurar o serviço LDAP, você poderá fazer login na conta ERPNext usando credenciais LDAP.


## 1. Pré-requisitos


Para usar o LDAP, primeiro você precisa instalar o módulo `ldap3` Python. Para fazer isso, abra uma sessão de terminal no seu servidor que hospeda a instância do ERPNext. Vá para o diretório `frappe-bench`.
execute o comando: `./env/pip install ldap3`


Agora você está pronto para ativar o serviço LDAP no ERPNext.


## 2. Configurando LDAP


Para configurar o LDAP, vá para



> 
> Página inicial > Integrações > Configurações LDAP
> 
> 
> 


Muitos parâmetros são obrigatórios para permitir que o ERPNext se conecte ao LDAP. São eles:


* URL do servidor LDAP: Este é o URL do seu servidor LDAP. Deve estar no formato `ldap://yourserver:port` ou `ldaps://yourserver:port`
* Nome distinto batico (DN): Este é o nome distinto do usuário que tem permissão para procurar detalhes do usuário em seu servidor LDAP. Este deve ser um usuário que tenha apenas permissões somente leitura em seu servidor LDAP.
* Senha para DN Base: Esta é a senha do usuário acima, usada para procurar detalhes do usuário em seu servidor LDAP.
* Unidade Organizacional de Usuários: Este é o DN da Unidade Organizacional da qual todos os usuários em seu servidor LDAP devem fazer parte para poder fazer login no ERPNext.
* Função padrão na criação: Quando o usuário é criado no ERPNext, ele receberá esta função padrão na primeira vez que efetuar login.
* String de pesquisa LDAP: Este campo permite que o ERPNext corresponda o usuário/e-mail digitado na tela de login do ERPNext, com o Servidor LDAP. Por exemplo, você pode usar endereço de e-mail ou nome de usuário, dependendo de sua preferência.


Deve ser inserido no formato: `LDAPFIELD={0}`


Exemplo de nome de usuário do Active Directory: `sAMAccountName={0}`


Exemplo de nome de usuário LDAP aberto: `uid={0}`
* Campo de e-mail LDAP: especifica o campo LDAP que contém o endereço de e-mail do usuário.


Exemplo de Active Directory e Open LDAP: `mail`
* Campo de nome de usuário LDAP: especifica o campo LDAP que contém o nome de usuário do usuário.


Exemplo do Active Directory: `sAMAccountName`


Exemplo de LDAP aberto: `uid`
* Campo de nome LDAP: especifica o campo LDAP que contém o nome do usuário.


Exemplo do Active Directory: `givenName`


Exemplo de LDAP aberto: `sn`


Existem muitos outros campos não obrigatórios que você pode usar para mapear seus campos de usuário LDAP para os campos de usuário ERPNext. São eles:


* Nome do meio
* Telefone
* Celular


Depois que suas configurações estiverem corretas, você pode clicar na caixa de seleção `Ativado` na parte superior. Ao tentar habilitar o LDAP, o ERPNext tentará se conectar ao servidor LDAP para garantir que as configurações estejam corretas. Se falhar, você não conseguirá ativar o LDAP e receberá uma mensagem de erro.


A mensagem de erro indicará o problema que precisa ser resolvido para continuar.


Após configurar a ativação do LDAP, na tela de login, o sistema habilita a opção **Login via LDAP**.


### 2.1 Segurança LDAP


Na seção Segurança LDAP, você tem muitas opções para se conectar com segurança ao seu servidor LDAP.


* ##### Modo SSL/TLS


Especifica se você deseja iniciar uma sessão TLS na conexão inicial com o servidor LDAP.
* ##### Exigir certificado confiável


Especifica se você precisa de um certificado confiável para se conectar ao servidor LDAP


Se estiver especificando um certificado confiável, você precisará especificar os caminhos para seus arquivos de certificado. Esses arquivos devem ser colocados no seu servidor ERPNext, e os campos a seguir devem ser um caminho absoluto para os arquivos no seu servidor.
 Os campos do certificado são:
* Caminho para arquivo de chave privada
* Caminho para o certificado do servidor
* Caminho para o arquivo de certificados CA


### 2.2 Mapeamentos de grupos LDAP


O ERPNext também permite mapear automaticamente vários grupos LDAP para as funções ERPNext apropriadas.
Por exemplo, você pode querer que todos os seus funcionários de contabilidade tenham automaticamente a função de usuário de contas.


Certifique-se de preencher o campo Grupo LDAP para permitir isso. Este é o campo LDAP encontrado em um objeto de usuário no LDAP, que contém todos os grupos dos quais o usuário é membro.


Para Active Directory e Open LDAP, este campo deve ser definido como `memberOf`.


Open LDAP pode precisar que este campo esteja habilitado em seu servidor LDAP. Consulte exemplos na Internet para obter mais detalhes.



> 
> Observe que todas as funções do ERPNext serão verificadas cada vez que um usuário fizer login e serão removidas ou adicionadas às permissões do usuário.
> 
> 
> 


Na área Configurações LDAP, há dois menus suspensos.
1. Modo SSL/TLS-defina como **StartTLS** para conectar-se ao seu servidor LDAP usando StartTLS. Se o seu servidor LDAP não suportar StartTLS, definir isso como StartTLS resultará em um erro `StartTLS não é suportado`. Verifique a configuração do seu servidor LDAP se receber este erro.
2. Exigir certificado confiável-se você alterar para **Sim** então o certificado fornecido pelo servidor LDAP deverá ser confiável pelo servidor Frappe/ERPNext. Se você preferir usar o StartTLS com um certificado autoassinado (não confiável), defina como **Não**. Se você não usar StartTLS, essa configuração será ignorada.



