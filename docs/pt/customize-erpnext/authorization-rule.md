# Regra de autorização



**A regra de autorização permite configurar uma autorização/aprovação personalizada em um documento, com base nas condições definidas.**


Exemplo: se o total geral de um pedido de vendas exceder US$ 1.000, ele deverá ser verificado/enviado apenas pelo gerente de vendas, mesmo que o usuário de vendas tenha permissão para "Enviar".


Na mesma linha, você pode definir a Regra de Autorização com base em campos como Total Líquido, Total Geral, % de Desconto e especificar quem seria o aprovador do documento se a condição de autorização for atendida.


![Regra de autorização](/files/authorization-rule.png)


Vamos considerar um exemplo detalhado de uma regra de autorização para aprender melhor.


Suponha que o Gerente de Vendas precise autorizar Pedidos de Vendas somente se o valor do Total Geral exceder 10.000. Se o valor do Pedido de Vendas for inferior a 10.000, até mesmo o Usuário de Vendas poderá enviá-lo. Isso significa que a permissão de envio do usuário de vendas será restrita apenas até pedidos de vendas com total geral inferior a 10.000.


## 1. Como criar uma regra de autorização


1. Vá para a lista de regras de autorização e clique em Novo.
2. Selecione a transação na qual a Regra de Autorização será aplicável. Esta funcionalidade está disponível apenas para transações limitadas.
3. Insira o valor autorizado, etc. Isso depende do campo selecionado em Baseado em.
4. Selecionar com base em. A regra de autorização será aplicada com base no valor selecionado neste campo.
5. Selecione a função aplicável. Esta é a função à qual esta Regra de Autorização será aplicável. Conforme o exemplo, será Usuário de Vendas.
6. Para ser mais específico, você também pode selecionar Aplicável ao usuário se desejar aplicar a regra a um usuário de vendas específico e não a todos os usuários de vendas.
7. Selecione Função de aprovação. Esta é a função que pode aprovar formulários acima do valor Autorizado. Conforme nosso exemplo, é o Gerente de Vendas.
8. Você também pode selecionar um gerente de vendas específico.
9. Salvar.


![Regra de autorização](/files/new-authorization-rule.png)


Se o Usuário de Vendas tentar enviar o Pedido de Venda de valor superior a 10.000, ele receberá uma mensagem de erro.


![Mensagem de validação de regra de autorização](/files/authorization-rule-validation-message.png)



> 
> Se desejar restringir o envio de pedidos de vendas pelo usuário de vendas, em vez de criar uma regra de autorização, você deverá remover o privilégio de envio do usuário de vendas de [Gerenciador de permissões de função](/docs/pt/setting-up/users-and-permissions/role-based-permissions).
> 
> 
> 


### Documentos nos quais a regra de autorização pode ser aplicada


1. Pedido de venda
2. Pedido de compra
3. Cotação
4. Nota de entrega
5. Fatura de vendas
6. Fatura de compra
7. Recibo de compra
8. Avaliação


### Campos nos quais a condição de autorização pode ser baseada


1. Total geral
2. Desconto médio
3. Desconto para o cliente
4. Desconto por item



