# Contabilidade multimoeda



**A transação em duas moedas diferentes é conhecida como contabilidade multimoeda.**


No ERPNext, você pode fazer lançamentos contábeis em múltiplas moedas. Por exemplo, se você tiver uma conta bancária em moeda estrangeira, poderá fazer transações nessa moeda e o sistema mostrará o saldo bancário apenas nessa moeda específica.


As contas bancárias em moeda estrangeira podem ser para outras filiais da sua própria empresa ou contas de Devedores/Credores para Clientes/Fornecedores estrangeiros.


## 1. Configuração


### 1.1 Definir moeda no plano de contas


Para começar a usar a contabilidade multimoeda, você precisa atribuir a moeda contábil no registro Conta. Você pode definir a moeda no [Plano de contas](/docs/pt/accounts/chart-of-accounts) ao criar uma conta.


![Definir moeda na conta](/files/set-default-currency-in-ledger.png)


### 1.2 Nova conta com moeda diferente


Você também pode atribuir/modificar a moeda abrindo registros de contas específicos para contas existentes.


![Atualizar moeda no razão](/files/update-currency-in-ledger.png)


### 1.3 Moeda para cliente/fornecedor


Para Cliente/Fornecedor (Parte), você também pode definir sua moeda de faturamento no registro da parte. Se a moeda contábil da parte for diferente da moeda da empresa, você deverá mencionar a conta a receber/a pagar padrão nessa moeda.


![Moeda de cobrança no cliente](/files/customer-billing-currency.png)


### 1.4 Após a configuração


Depois de definir a Moeda nas contas necessárias e selecionar as contas relevantes no registro da Parte, você estará pronto para fazer transações com elas. Se a moeda da conta da parte for diferente da moeda da Empresa, o sistema restringirá a realização de transações com essa parte.


Você precisa alterar a moeda para a moeda da parte na transação (Venda ou Ordem de Compra/Fatura). Se a moeda da conta da parte for igual à moeda da empresa, você poderá fazer transações para essa Parte em qualquer moeda. Mas os lançamentos contábeis (Lançamentos GL) serão sempre na moeda da conta do partido.



> 
> **Observação**: certifique-se de que a conta correta com a moeda esteja definida no campo "Débito para" ao fazer faturas/pagamentos.
> 
> 
> 


Você pode alterar a moeda contábil no registro da Parte/Conta antes de fazer qualquer transação contra ela. Depois de fazer lançamentos contábeis, o sistema não permitirá alterar a moeda dos registros de Parte/Conta. No caso de configuração multiempresa, a moeda contábil da parte deve ser a mesma para todas as empresas.


## 2. Taxas de câmbio


Ao lidar com múltiplas moedas, o ERPNext possui a página Câmbio para gerenciar taxas de câmbio. Ele permite que você salve as cotações de taxas de câmbio necessárias. Para saber mais, visite a página [Câmbio de moedas](/docs/pt/accounts/currency-exchange).


Para transações em moeda estrangeira, o ERPNext verifica as taxas de câmbio de:


1. Da Casa de Câmbio para qualquer registro correspondente (se criado por um usuário).
2. Se isso falhar, o ERPNext tentará obter a taxa de câmbio atual do mercado de [Frankfurter](https://www.frankfurter.app).
3. **NOTA**: A partir da versão 13.10.0 do ERPNext, o Frankfurter é substituído por um novo serviço chamado [exchangerate.host](https://exchangerate.host).
4. Se isso ainda falhar, a taxa de câmbio terá que ser inserida manualmente.


As taxas no mestre de câmbio de moeda são obtidas com base no fato de 'Permitir taxa de câmbio obsoleta' estar ativado nas configurações da conta. Para saber mais, visite a página [Configurações de contas](/docs/pt/accounts/accounts-settings).


## 3. Transações


### 3.1 Fatura de vendas


Em uma fatura de vendas, a moeda da transação deverá ser igual à moeda contábil do Cliente se a moeda contábil do Cliente for diferente da moeda da Empresa. Caso contrário, você poderá selecionar qualquer moeda em uma fatura de vendas. Ao selecionar o Cliente, o sistema buscará uma conta a Receber do Cliente/Empresa. A Moeda da conta a receber deve ser igual à moeda contábil do Cliente.


Agora, na fatura, o valor pago será inserido na moeda da transação, em vez da moeda anterior da empresa. O valor da baixa também será inserido na moeda da transação.


O Valor Pendente e o Valor Antecipado serão sempre calculados e mostrados na Moeda da Conta do Cliente. Os valores pagos serão refletidos na [Entrada de pagamento](/docs/pt/accounts/payment-entry):


![Multi-moeda na entrada de pagamento](/files/multi-currency-in-payment-entry.png)


### 3.2 Fatura de compra


Da mesma forma, em uma fatura de compra, os lançamentos contábeis serão feitos com base na moeda contábil do Fornecedor. O Valor Pendente e o Valor Antecipado também serão mostrados na moeda contábil do fornecedor. O valor da amortização agora será inserido na moeda da transação.


### 3.3 Lançamento de diário


No lançamento contábil manual, você pode fazer transações em diferentes moedas. Existe uma caixa de seleção 'Multi Moeda', para permitir entradas em várias moedas. Somente quando a opção 'Multi Moeda' for selecionada, você poderá selecionar contas com moedas diferentes.


![Várias moedas no lançamento contábil manual](/files/multi-currency-journal-entry.png)


Na tabela Contas, ao selecionar uma conta em moeda estrangeira, o sistema mostrará a seção Moeda e buscará a Moeda da Conta e a Taxa de Câmbio automaticamente. Você pode alterar/modificar a taxa de câmbio posteriormente manualmente. O valor do Débito/Crédito deve ser inserido na Moeda da Conta, o sistema calculará e mostrará o valor do Débito/Crédito na Moeda da Empresa automaticamente.


![Moeda da empresa e da transação no diário ENtry](/files/company-and-transaction-currency-in-journal-entry.png)


## 4. Relatórios


### 4.1 Razão Geral


No Razão Geral, o sistema mostra o valor de débito/crédito na moeda da parte **se for filtrado** por uma conta e se a moeda da conta for diferente da moeda da empresa.


![Várias moedas no General Ledger](/files/multi-currency-in-general-ledger.png)


### 4.2 Contas a receber/a pagar


No relatório Contas a Receber/Pagar, o sistema mostra todos os valores na Moeda da Parte/Conta.


![Multi-moeda em contas a receber](/files/multi-currency-in-accounts-receivable.png)


### 5. Tópicos Relacionados


1. [Reavaliação da taxa de câmbio](/docs/pt/accounts/exchange-rate-revaluation)
2. [Câmbio de moeda](/docs/pt/accounts/currency-exchange)
3. [Moeda](/docs/pt/accounts/currency)
4. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
5. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



