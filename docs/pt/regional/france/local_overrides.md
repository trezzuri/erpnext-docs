# Transações de vendas e pagamentos



Para estar em conformidade com a mais recente lei financeira aplicável ao software POS, o ERPNext registra automaticamente todas as transações de vendas e pagamentos em um registro encadeado.


Se o seu país estiver definido como "França", a exclusão de transações de vendas e pagamentos também não será permitida, mesmo que as permissões apropriadas sejam concedidas ao usuário.


Observe que o ERPNext ainda não está totalmente em conformidade com a Lei Financeira de 2016.


# Relatório de log encadeado


Um relatório dedicado chamado "Relatório de registro de transações" está disponível para verificar se a cadeia registrada não foi quebrada.


Se o status da coluna "Chain Integrity" for "True", a cadeia não foi quebrada.
Isso significa que você pode consultar toda a cadeia de eventos que ocorreram no seu sistema.


Se o status da coluna "Integridade da Cadeia" for "Falso", significa que há uma discrepância na cadeia.
Neste caso, a linha anterior foi removida ou alterada no banco de dados. É um efeito provável de um comportamento fraudulento.



