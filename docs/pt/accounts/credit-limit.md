# Limite de crédito


**Limite de Crédito é o valor máximo de crédito que você está disposto a oferecer a um Cliente.**


Um Limite de Crédito é o valor máximo de crédito que uma instituição financeira ou
outro credor estenderá a um devedor para uma determinada linha de crédito. A partir de um
Na perspectiva do cliente, é a quantidade máxima de bens ou serviços que eles podem obter sem pagar antecipadamente.


Você pode definir o Limite de Crédito em Cliente, Grupo de Clientes e na Empresa.
Quando um Pedido de Venda ou uma Nota Fiscal de Venda for enviado, o Limite de Crédito será verificado.


A ordem de precedência para verificação do Limite de Crédito é a seguinte:


* Limite de Crédito definido no Cliente
* Limite de Crédito definido no Grupo de Clientes
* Limite de Crédito definido na Empresa


## 1. Como definir o limite de crédito


1. Acesse: **Venda > Vendas > Cliente > Cliente**.
2. Na seção Limite de Crédito e Condições de Pagamento, defina o Limite de Crédito.
3. Se deixar o Limite de Crédito como padrão, ou seja, 0, não tem efeito.
4. Salve.


![Limite de crédito do cliente](/files/customer-credit-limit.png)


## 2. Características


### 2.1 Controlador de Crédito


Você pode permitir que usuários com uma função específica substituam a validação do Limite de Crédito e enviem um Pedido de Venda ou Fatura de Venda mesmo quando o Limite de Crédito do Cliente for totalmente utilizado.


Para definir a função de Controlador de crédito:


1. Acesse: **Contabilidade > Configurações > Configurações de contas**
2. Defina a função no campo Credit Controller.


![Gerenciador de crédito](/files/credit-manager-role.png)


### 2.2 Ignorar verificação de limite de crédito para pedido de venda


Para clientes específicos, você pode definir o limite de crédito a ser verificado contra o valor acumulado das faturas de vendas pendentes e não dos pedidos de vendas. Você pode fazer isso marcando a caixa de seleção 'Ignorar verificação de limite de crédito no pedido de venda' na seção 'Limite de crédito e condições de pagamento' do cliente.


![Ignorar limite de crédito no pedido de venda](/files/customer-credit-limit-bypass.png)


### 2.3 Limite de Crédito para Grupos de Clientes


Para definir o limite de crédito no nível do grupo de clientes:


1. Acesse **Venda > Clientes > Grupo de clientes**.
2. Abra o Grupo de Clientes e defina o Limite de Crédito.


### 2.4 Limite de Crédito para Empresa


Ao definir o Limite de Crédito no nível da Empresa, todos os Clientes terão esse Limite de Crédito aplicado globalmente.


Para definir o Limite de Crédito no nível da Empresa:


1. Vá para **Contabilidade > Mestres e Contas > Empresa**.
2. Abra a Empresa e defina o Limite de Crédito.


### 3. Tópicos Relacionados


1. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
2. [Cliente](/docs/v13/user/manual/en/CRM/cliente)