# Corrigindo erros do ano fiscal



Ao criar qualquer entrada, o sistema valida se as datas (como data de lançamento, data de transação etc.) pertencem ao ano fiscal selecionado. Caso contrário, o sistema receberá uma mensagem de erro dizendo:


`Data ##-##-#### fora do ano fiscal`


É mais provável que você receba esta mensagem de erro se o seu Ano Fiscal tiver alterações, mas o novo Ano Fiscal ainda não tiver definido um padrão. Para garantir que o novo ano fiscal seja atualizado automaticamente nas transações, você deve configurar seu mestre conforme as instruções abaixo.


#### Criar novo ano fiscal


Somente o usuário com função de gerente do sistema atribuída tem permissão para criar um novo ano fiscal. Para criar um novo ano fiscal, acesse:


`Contabilidade > Mestrado em Contabilidade > Ano Fiscal`


Leia [Ano fiscal](/docs/pt/accounts/fiscal-year) para saber mais.


#### Definir ano fiscal como padrão


Depois que o ano fiscal for salvo, você encontrará a opção de definir esse ano fiscal como padrão.


![Definir ano fiscal como padrão](/files/set-fiscal-year-as-default.png)


O Ano Fiscal Padrão também será atualizado na configuração Padrão Global. Você pode atualizar manualmente o ano fiscal padrão em:


`Configurações > Principal > Padrão global`


![Configuração do ano fiscal atual nos padrões globais](/files/current-fiscal-year-in-global-defaults.png)


Salve o padrão global e recarregue sua conta ERPNext. Em seguida, o ano fiscal padrão será atualizado automaticamente em suas transações.


Observação: nas transações, você pode selecionar manualmente o ano fiscal necessário na seção Mais informações.



