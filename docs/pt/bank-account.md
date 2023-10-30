# Conta bancária



No ERPNext, Contas Bancárias podem ser criadas para uma Empresa, bem como para outras partes, como Clientes, Fornecedores, etc. Isso permite que você registre todas as transações bancárias corretamente para maior precisão contábil.


Você pode adicionar Contas Bancárias no ERPNext for Company. Fornecedor, Cliente ou qualquer outra parte com quem as transações sejam realizadas. Em seguida, a conta bancária pode ser escolhida em [Entradas de pagamento](/docs/pt/accounts/payment-entry) como um [Modo de pagamento](/docs/pt/accounts/mode-of-payment).


Para acessar a conta bancária, acesse:



> 
> Página inicial > Contabilidade > Extrato bancário > Conta bancária
> 
> 
> 


![Conta bancária](/files/bank-account.png)


## 1. Pré-requisitos


Antes de criar e usar uma conta bancária, é aconselhável criar primeiro o seguinte:


* [Banco](/docs/pt/accounts/bank)


## 2. Como criar uma conta bancária


1. Insira um nome de conta.
2. Vincule a conta contábil definida em 'Contas bancárias' no [Plano de contas](/docs/pt/accounts/chart-of-accounts).
3. Selecione um banco.
4. Salvar.


### 2.1 Opções adicionais ao criar uma conta bancária


* **É a conta padrão**: a ativação desta opção a usará como a conta bancária padrão para todas as transações do diário.
* **É conta corporativa**: ative se esta conta bancária for uma conta corporativa.
* Um tipo de conta e um subtipo de conta podem ser definidos para classificação adicional em relatórios, etc.


## 3. Recursos


### 3.1 Detalhes da festa


* **Tipo de grupo**: se esta não for uma conta corporativa, defina a quem esta conta pertence. As opções disponíveis são: Cliente, Funcionário, Membro, Acionista, Estudante e Fornecedor.
* **Parte**: Selecione o Cliente/Fornecedor específico, etc.


### 3.2 Detalhes da conta


Para referência, os seguintes detalhes sobre uma conta bancária podem ser armazenados no ERPNext:


* IBAN
* Número da conta bancária
* Código da filial
* Número SWIFT


### 3.3 Endereço e contato


* **Endereço**: Um banco pode ter vários na mesma localidade. O endereço da agência bancária pode ser definido aqui.
* **Contato**: Uma pessoa de contato pode ser vinculada aqui. Os bancos geralmente fornecem uma pessoa de contato dedicada para contas corporativas. Você pode adicionar o contato dessa pessoa aqui.
* **Site**: você pode adicionar o site do banco aqui.


### 3.4 Detalhes da integração


**Data da última integração**: se o seu banco suporta [Integração Plaid](/docs/pt/erpnext_integration/plaid_integration), defina uma data aqui irá sincronizar na data definida. Isso criará entradas de transações bancárias.



