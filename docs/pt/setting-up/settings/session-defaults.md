# Padrões de Sessão


**Padrões de sessão são valores padrão configuráveis ​​definidos durante as sessões do usuário.**


Considere um cenário em que você tenha 8 empresas configuradas em sua conta e precise definir o campo 'Empresa' todas as vezes ao criar um novo pedido de venda. Este é um processo muito demorado quando você precisa lidar com vários pedidos de vendas diariamente.


## 1. Como criar padrões de sessão


### 1.1 Definir as configurações padrão da sessão


1. Vá para Configurações padrão da sessão. Lá você pode ver uma tabela para padrões de sessão.
2. Clique em 'Adicionar linha'.
3. Selecione o DocType para o qual você deseja definir os padrões de sessão.
4. Salve.


![Configurações de padrões de sessão](/files/session-defaults-settings.png)


### 1.2 Configurar os valores padrão da sessão


1. Clique no menu 'Configurações' na barra de ferramentas. Você encontrará uma opção 'Padrões de sessão' lá. Clique nisso.


![Menu de padrões de sessão](/files/session-defaults-menu.png)
2. Um prompt 'Padrões de Sessão' aparecerá. Defina os valores padrão para os respectivos campos e salve.


![Prompt de padrões de sessão](/files/session-defaults-prompt.png)


Depois de salvar, os valores padrão serão definidos em todos os lugares.


Você pode abrir um novo Pedido de Venda e verificar. O campo da empresa é definido como Empresa padrão.


![Configuração de padrões de sessão](/files/session-defaults-set-1.png)


Abra uma nova tarefa. O campo 'Projeto' é definido como o Projeto padrão.


![Configuração padrão da sessão](/files/session-defaults-set-2.png)


Abra um relatório, por exemplo, Razão Geral. O filtro da empresa é definido como a empresa padrão.


![Padrão da sessão](/files/session-defaults-set-3.png)


## 2. Características


### 2.1 Padrões apagados no logout


Os valores padrão são definidos para esse usuário específico para a sessão em andamento. Uma vez desconectado, esses valores padrão são apagados.


### 2.2 Visibilidade do botão 'Configurações'


O botão Configurações é visível apenas para o gerente do sistema ou para uma pessoa com permissão para acessar 'Configurações padrão da sessão'. Este botão o leva até as Configurações padrão da sessão, onde você pode adicionar ou remover os tipos de documento para os quais deseja definir os padrões da sessão.


![Prompt de padrões de sessão](/files/settings-button.png)


### 3. Tópicos Relacionados


1. [Padrões Globais](/docs/v13/user/manual/en/setting-up/settings/global-defaults)
2. [Configurações do sistema](/docs/v13/user/manual/en/setting-up/settings/system-settings)