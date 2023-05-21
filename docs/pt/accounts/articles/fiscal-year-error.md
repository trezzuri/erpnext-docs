# Consertando erro de ano fiscal


Ao criar qualquer entrada, o sistema valida se as datas (como Data de Lançamento, Data de Transação, etc.) pertencem ao Ano Fiscal selecionado. Caso contrário, sistema através de uma mensagem de erro dizendo:


`Data ##-##-#### não no ano fiscal`


É mais provável que você receba esta mensagem de erro se o seu ano fiscal tiver alterações, mas o novo ano fiscal ainda não tiver definido um padrão. Para garantir que o novo ano fiscal seja atualizado automaticamente nas transações, você deve configurar seu mestre conforme as instruções abaixo.


#### Criar novo ano fiscal


Somente o usuário com função de gerente de sistema atribuída tem permissão para criar um novo ano fiscal. Para criar um novo ano fiscal, acesse:


`Contabilidade > Mestrado em Contabilidade > Ano Fiscal`


Leia [Ano fiscal](/docs/v13/user/manual/en/accounts/fiscal-year) para saber mais.


#### Definir ano fiscal como padrão


Depois que o ano fiscal for salvo, você encontrará a opção de definir esse ano fiscal como padrão.


![Definir ano fiscal como padrão](/files/set-fiscal-year-as-default.png)


O ano fiscal padrão também será atualizado na configuração padrão global. Você pode atualizar manualmente o ano fiscal padrão de:


`Configurações > Núcleo > Padrão global`


![Configuração do ano fiscal atual em padrões globais](/files/current-fiscal-year-in-global-defaults.png)


Salve o padrão global e recarregue sua conta ERPNext. Em seguida, o ano fiscal padrão será atualizado automaticamente em suas transações.


Observação: nas transações, você pode selecionar manualmente o ano fiscal necessário, na seção Mais informações.