# Erro de nível de permissão


Ao personalizar regras no [Gerenciador de permissões](/docs/pt/setting-up/users-and-permissions/role-based-permissions), você pode receber uma mensagem de erro dizendo:



> 
> Para Gerente de Sistema *(ou qualquer outra função)* no nível 2 *(ou outro nível)* em Cliente *(ou qualquer outro documento)* em linha 8: A permissão no nível 0 deve ser definida antes que os níveis mais altos sejam definidos.
> 
> 
> 


A mensagem de erro indica que o problema está na configuração de permissão existente para este documento.


Para qualquer função, antes de atribuir permissão no Perm Level 1 ou 2 (e assim por diante), a permissão no Perm Level 0 deve ser atribuída. A mensagem de erro informa que o gerente do sistema recebeu permissão nos níveis de Perm 1 e 2, mas não no nível 0. Você deve primeiro corrigir a permissão para a função do gerente do sistema:


* Atribuindo permissão ao System Manager no nível 0.


Ou
* Ao remover a permissão nos níveis 1 e 2.


Depois de executar uma das etapas acima, você poderá adicionar com êxito novas regras de permissão no Gerenciador de permissões de função.


