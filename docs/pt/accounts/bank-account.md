# Conta bancária


No ERPNext, as Contas Bancárias podem ser criadas para uma Empresa, bem como para outras partes, como Clientes, Fornecedores, etc. Isso permite que você registre todas as transações bancárias corretamente para precisão contábil.


Você pode adicionar Contas Bancárias no ERPNext para Empresa. Fornecedor, Cliente ou qualquer outra parte com quem as transações são realizadas. Então a Conta Bancária pode ser escolhida em [Entradas de Pagamento](/docs/v13/user/manual/en/accounts/payment-entry) como [Modo de Pagamento](/docs/v13/user/manual/en/accounts /modo de pagamento).


Para acessar a Conta Bancária, acesse:



>
> Home > Contabilidade > Extrato Bancário > Conta Bancária
>
>
>


![Conta bancária](/files/bank-account.png)


## 1. Pré-requisitos


Antes de criar e usar a Conta Bancária, é recomendável criar primeiro o seguinte:


* [Banco](/docs/v13/user/manual/pt/contas/banco)


## 2. Como criar uma conta bancária


1. Digite um nome de conta.
2. Vincule a conta do Razão Geral definida em 'Contas Bancárias' no [Plano de Contas](/docs/v13/user/manual/en/accounts/plano de contas).
3. Selecione um banco.
4. Salve.


### 2.1 Opções adicionais ao criar uma conta bancária


* **É a conta padrão**: habilitar isso usará isso como a conta bancária padrão para todas as transações de diário.
* **É Conta Corporativa**: Habilite se esta Conta Bancária for uma conta Corporativa.
* Um tipo de conta e um subtipo de conta podem ser definidos para classificação posterior em relatórios, etc.


## 3. Características


### 3.1 Detalhes da Parte


* **Tipo de grupo**: Se esta não for uma conta corporativa, defina a quem pertence esta conta. As opções disponíveis são: Cliente, Colaborador, Integrante, Acionista, Aluno e Fornecedor.
* **Parte**: Selecione o Cliente/Fornecedor específico, etc.


### 3.2 Detalhes da conta


Para referência, os seguintes detalhes sobre uma Conta Bancária podem ser armazenados no ERPNext:


* IBAN
* Número da conta bancária
* Código da Agência
* Número rápido


### 3.3 Endereço e Contato


* **Endereço**: Um banco pode ter múltiplas na mesma localidade. O endereço da agência bancária pode ser definido aqui.
* **Contato**: Uma pessoa de contato pode ser vinculada aqui. Os bancos geralmente fornecem uma pessoa de contato dedicada para contas corporativas, você pode adicionar o contato dessa pessoa aqui.
* **Site**: Você pode adicionar o site do banco aqui.


### 3.4 Detalhes da Integração


**Última data de integração**: Se o seu banco suportar [Plaid Integration](/docs/v13/user/manual/en/erpnext_integration/plaid_integration), definir uma data aqui sincronizará na data definida. Isso criará entradas de transações bancárias.