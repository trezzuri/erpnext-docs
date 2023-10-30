# Erro no nível de permissão



Ao personalizar regras no [Gerenciador de permissões](/docs/pt/setting-up/users-and-permissions/role-based-permissions), você pode receber uma mensagem de erro dizendo:



> 
> Para Gerente de Sistema *(ou qualquer outra função)* no nível 2 *(ou outro nível)* em Cliente *(ou qualquer outro documento)* em linha 8: a permissão no nível 0 deve ser definida antes que níveis superiores sejam definidos.
> 
> 
> 


A mensagem de erro indica que o problema está na configuração de permissão existente para este documento.


Para qualquer função, antes de atribuir permissão no nível de permissão 1 ou 2 (e assim por diante), a permissão no nível de permissão 0 deve ser atribuída. A mensagem de erro informa que o gerente do sistema recebeu permissão nos níveis de permissão 1 e 2, mas não no nível 0. Primeiro, você deve corrigir a permissão para a função do gerente do sistema:


* Atribuindo permissão ao gerente do sistema no nível 0.


Ou
* Removendo a permissão nos níveis 1 e 2.


Depois de executar uma das etapas acima, você poderá adicionar com êxito novas regras de permissões no Role Permission Manager.




