# Integração xadrez



ERPNext oferece a possibilidade de sincronizar suas contas bancárias através de um serviço chamado [Plaid](https://plaid.com/). Verifique [as Perguntas frequentes sobre o Plaid](https://support-my.plaid.com/hc/en-us) para ver se o seu país é compatível.


Se sua instância estiver conectada ao Plaid, você poderá sincronizar as transações da sua conta bancária sem precisar importar manualmente um arquivo CSV ou XLSX.


## Configurações


Para dar acesso ao ERPNext ao Plaid, você precisa adicionar os três parâmetros a seguir ao seu arquivo `site_config.json`.


* `plaid_env`
* `plaid_public_key`
* `plaid_secret`


## Ativação


Para ativar o Plaid em uma instância, clique no botão "Ativar" nas configurações do Plaid DocType.


![Ativar Plaid](/files/plaid_enable.gif)


Depois de ativada, você poderá criar uma nova conta diretamente no painel de reconciliação bancária.


## Criação de conta bancária


Para vincular uma de suas contas bancárias existentes ao ERPNext, clique em "Vincular uma nova conta bancária" e siga os passos propostos pela Plaid.


![Vincule sua conta bancária](/files/new_account_creation.gif)


## Sincronização bancária


Para sincronizar uma conta bancária com o ERPNext, selecione uma conta e clique no botão "Ação" para selecionar "Sincronizar esta conta".


![Sincronize sua conta bancária](/files/plaid_synchronization.gif)


A sincronização é baseada na "Data da última integração" disponível no tipo de documento "Conta bancária".


Se, por algum motivo, você quiser refazer uma sincronização, poderá alterar esta data e sincronizar a conta novamente.
Como todas as transações bancárias são marcadas com um ID de transação específico, a sincronização será apenas incremental.


## Sincronização Automática


Você pode permitir que o Plaid sincronize sua conta bancária com o ERPNex a cada hora selecionando "Sincronizar todas as contas a cada hora" nas configurações do Plaid.



