# Contabilidade em várias moedas


**A transação em duas moedas diferentes é conhecida como Contabilidade em várias moedas.**


No ERPNext, você pode fazer lançamentos contábeis em várias moedas. Por exemplo, se você tiver uma conta bancária em moeda estrangeira, poderá fazer transações nessa moeda e o sistema mostrará o saldo bancário apenas nessa moeda específica.


As contas bancárias em moeda estrangeira podem ser para outras sucursais da sua própria empresa ou conta de Devedores/Credores para Clientes/Fornecedores estrangeiros.


## 1. Configuração


### 1.1 Definir moeda no plano de contas


Para começar com a contabilidade em várias moedas, você precisa atribuir a moeda contábil no registro da conta. Você pode definir a moeda de [Plano de contas](/docs/v13/user/manual/en/accounts/plano de contas) ao criar uma conta.


![Definir moeda na conta](/files/set-default-currency-in-ledger.png)


### 1.2 Nova conta com moeda diferente


Você também pode atribuir/modificar a moeda abrindo registros de conta específicos para contas existentes.


![Atualizar moeda no razão](/files/update-currency-in-ledger.png)


### 1.3 Moeda para Cliente/Fornecedor


Para Cliente/Fornecedor (Parte), você também pode definir sua moeda de cobrança no registro da parte. Se a moeda contábil da parte for diferente da moeda da empresa, você deve mencionar a conta a receber/pagar padrão nessa moeda.


![Moeda de cobrança no cliente](/files/customer-billing-currency.png)


### 1.4 Após a configuração


Depois de definir a Moeda na(s) conta(s) necessária(s) e selecionar as contas relevantes no registro da Parte, você estará pronto para fazer transações com elas. Se a moeda da conta da parte for diferente da moeda da Empresa, o sistema impedirá a realização de transações com essa parte.


Você precisa alterar a moeda para a moeda da parte na transação (Venda ou Ordem de Compra/Fatura). Se a moeda da conta da parte for a mesma moeda da empresa, você poderá fazer transações para essa parte em qualquer moeda. Mas os lançamentos contábeis (entradas contábeis) sempre serão na moeda da conta da parte.



>
> **Observação**: Certifique-se de que a conta correta com a moeda esteja definida no campo 'Débito em' ao fazer faturas/pagamentos.
>
>
>


Você pode alterar a moeda contábil no registro da Parte/Conta antes de fazer qualquer transação contra eles. Depois de fazer os lançamentos contábeis, o sistema não permitirá que você altere a moeda para ambos os registros da Parte/Conta. No caso de configuração multiempresarial, a moeda contábil da parte deve ser a mesma para todas as empresas.


## 2. Taxas de câmbio


Ao lidar com várias moedas, o ERPNext possui a página Câmbio para gerenciamento das taxas de câmbio. Ele permite que você salve as cotações de taxa de câmbio que você precisa. Para saber mais, visite a página [Câmbios](/docs/v13/user/manual/en/accounts/currency-exchange).


Para transações em moeda estrangeira, o ERPNext verifica as taxas de câmbio de:


1. Da Câmbio para qualquer registro correspondente (se criado por um usuário).
2. Se isso falhar, o ERPNext tentará obter a taxa de câmbio do mercado atual de [Frankfurter](https://www.frankfurter.app).
3. **NOTA**: A partir da versão 13.10.0 do ERPNext, o Frankfurter foi substituído por um novo serviço chamado [exchangerate.host](https://exchangerate.host).
4. Se isso ainda falhar, a taxa de câmbio terá que ser inserida manualmente.


As taxas no mestre de câmbio de moeda são buscadas com base em se 'Permitir taxa de câmbio obsoleta' está ativado em Configurações de contas. Para saber mais, visite a página [Configurações de contas](/docs/v13/user/manual/en/accounts/accounts-settings).


## 3. Transações


### 3.1 Nota Fiscal de Venda


Em uma Fatura de Venda, a moeda da transação deve ser a mesma moeda contábil do Cliente se a moeda contábil do Cliente for diferente da moeda da Empresa. Caso contrário, você pode selecionar qualquer moeda em uma fatura de venda. Ao selecionar o Cliente, o sistema buscará uma Conta a Receber do Cliente/Empresa. A Moeda da conta a receber deve ser a mesma que a moeda contábil do Cliente.


Agora, na Fatura, o Valor Pago será inserido na moeda da transação, em vez da anterior Moeda da Empresa. O Valor Baixado também será inserido na moeda da transação.


O Valor Pendente e o Valor do Adiantamento sempre serão calculados e exibidos na Moeda da Conta do Cliente. Os valores pagos serão refletidos na [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry):


![Multi-moeda na entrada de pagamento](/files/multi-currency-in-payment-entry.png)


### 3.2 Fatura de compra


Da mesma forma, em uma Fatura de Compra, os lançamentos contábeis serão feitos com base na moeda contábil do Fornecedor. O valor pendente e o valor do adiantamento também serão mostrados na moeda contábil do fornecedor. O valor da baixa agora será inserido na moeda da transação.


### 3.3 Lançamento Diário


No lançamento contábil manual, você pode fazer transações em diferentes moedas. Há uma caixa de seleção 'Multi-moeda', para permitir entradas em várias moedas. Somente quando a opção 'Multi-moeda' for selecionada, você poderá selecionar contas com moedas diferentes.


![Multi-moeda na entrada do diário](/files/multi-currency-journal-entry.png)


Na tabela Contas, ao selecionar uma conta em moeda estrangeira, o sistema mostrará a seção Moeda e buscará automaticamente a Moeda da Conta e a Taxa de Câmbio. Você pode alterar/modificar a taxa de câmbio posteriormente manualmente. O valor do Débito/Crédito deve ser inserido na Moeda da Conta, o sistema irá calcular e mostrar o valor do Débito/Crédito na Moeda da Empresa automaticamente.


![Moeda da empresa e da transação no diário ENtry](/files/company-and-transaction-currency-in-journal-entry.png)


## 4. Relatórios


### 4.1 Razão Geral


No Razão Geral, o sistema mostra o valor de débito/crédito na moeda da parte **se filtrado** por uma Conta e essa Moeda da Conta é diferente da Moeda da Empresa.


![Multi-moeda na contabilidade geral](/files/multi-currency-in-general-ledger.png)


### 4.2 Contas a Receber/Pagar


No relatório Contas a Receber/Pagar, o sistema apresenta todos os valores na Moeda da Parte/Conta.


![Multi-moeda em contas a receber](/files/multi-currency-in-accounts-receivable.png)


### 5. Tópicos Relacionados


1. [Reavaliação da taxa de câmbio](/docs/v13/user/manual/en/accounts/exchange-rate-revaluation)
2. [Câmbio](/docs/v13/user/manual/en/accounts/currency-cchange)
3. [Moeda](/docs/v13/user/manual/en/accounts/currency)
4. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
5. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)