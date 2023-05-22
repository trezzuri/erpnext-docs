# Corrigindo o erro do ano fiscal


Ao criar qualquer entrada, o sistema valida se as datas (como Data de Lançamento, Data de Transação, etc.) pertencem ao Ano Fiscal selecionado. Caso contrário, sistema através de uma mensagem de erro dizendo:


`Data ##-##-#### fora do ano fiscal`


É mais provável que você receba esta mensagem de erro se o seu ano fiscal tiver mudanças, mas o novo ano fiscal ainda não tiver definido um padrão. Para garantir que o novo ano fiscal seja atualizado automaticamente nas transações, você deve configurar seu mestre conforme as instruções abaixo.


#### Criar novo ano fiscal


Apenas o usuário com função de gerente de sistema atribuída tem permissão para criar um novo ano fiscal. Para criar um novo ano fiscal, acesse:


`Contabilidade > Contabilidade Mestre > Ano Fiscal`


Leia [Ano fiscal](/docs/pt/accounts/fiscal-year) para saber mais.


#### Definir ano fiscal como padrão


Após salvar o ano fiscal, você encontrará a opção de definir esse ano fiscal como padrão.


![Definir ano fiscal como padrão](/files/set-fiscal-year-as-default.png)


O ano fiscal padrão também será atualizado na configuração padrão global. Você pode atualizar manualmente o ano fiscal padrão em:


`Configurações > Núcleo > Padrão global`


![Configuração do ano fiscal atual em padrões globais](/files/current-fiscal-year-in-global-defaults.png)


Salve o padrão global e recarregue sua conta ERPNext. Em seguida, o ano fiscal padrão será atualizado automaticamente em suas transações.


Observação: em transações, você pode selecionar manualmente o ano fiscal necessário, na seção Mais informações.

