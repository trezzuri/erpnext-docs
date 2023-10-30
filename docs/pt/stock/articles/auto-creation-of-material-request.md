# Criação automática de solicitação de material



Para evitar rupturas de estoque, você pode acompanhar o nível de novo pedido do item. Quando o nível de estoque fica abaixo do nível de novo pedido, o gerente de compras é notificado e instruído a iniciar o processo de compra do item.


No ERPNext, você pode atualizar o Nível de Reordenamento e a Quantidade de Reordenamento do item no Cadastro de Itens. Se o mesmo item tiver níveis de reabastecimento diferentes, você também poderá atualizar o nível de reabastecimento do armazém e a quantidade de reabastecimento.


![reorder level](/files/reorder-request-1.png)


Com o nível de reordenamento, você também pode definir qual deve ser a próxima ação. Nova compra ou transferência de outro armazém. Com base na configuração no cadastro de itens, a finalidade também será atualizada na Solicitação de Material.


![próxima ação do nível de reordenação](/files/reorder-request-2.png)


Quando o estoque do item atinge o nível de novo pedido, a Solicitação de Material é criada automaticamente. Você pode ativar esse recurso em:


`Estoque > Configuração > Configurações de estoque`


![solicitação de material automático ativo](/files/reorder-request-3.png)


Uma solicitação de material separada será criada para cada item. O usuário com função de gerente de compras receberá alertas por e-mail sobre essas solicitações de materiais.


Se a criação automática da solicitação de material falhar, o usuário com função de gerente de compras será informado sobre a mensagem de erro. Uma das mensagens de erro mais encontradas é:


**Ocorreu um erro para determinados itens ao criar solicitações de materiais com base no nível de novo pedido.**
**Data 01/04/2016 não pertencente a nenhum exercício fiscal.**


Um dos motivos do erro também pode ser o ano fiscal. Clique [aqui](/docs/pt/accounts/articles/fiscal-year-error.html) para saber mais sobre isso.




