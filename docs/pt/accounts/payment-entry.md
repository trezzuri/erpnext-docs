# Entrada de pagamento



**Um Registro de Pagamento é um registro que indica que o pagamento de uma fatura foi feito.**

O Registro de Pagamento pode ser feito nas seguintes transações.

 * Fatura de venda
* Fatura de compra
* Ordem de venda (pagamento antecipado)

* Ordem de compra (pagamento antecipado)
* Relatório de despesas
* Transferência interna

No ERPNext, existem duas opções através das quais o usuário pode capturar o pagamento:

* Entrada de pagamento (padrão)

* Lançamento do diário

Aqui estão diagramas para entender o fluxo:

Em Vendas: ![Vendas por pagamento](/files/pe-sales.png)![]()

Na compra: ![Payment Purchase](/files/pe-purchase.png)![]()  


Para acessar a lista de entrada de pagamento, vá para:


> Página inicial > Contabilidade > Contas a receber/a pagar > Entrada de pagamento
> 
> 

## 1. Pré-requisitos

Uma entrada de pagamento também pode ser criada diretamente e posteriormente vinculada a um pedido/fatura. Antes de criar e usar Entrada de Pagamento, é aconselhável criar primeiro o seguinte:

1. [Cliente](/docs/pt/CRM/customer)
2. [Fornecedor](/docs/pt/buying/supplier )
3. [Conta bancária](/docs/pt/accounts/bank-account)

Se você estiver seguindo o ciclo de vendas/compra, você precisaria do seguinte:

1. [Pedido de venda](/docs/pt/selling/sales-order) (pagamento antecipado)
2. [Ordem de compra](/docs/pt/buying/purchase-order ) (pagamento antecipado)
3. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
4. [Fatura de compra](/docs/pt/accounts/purchase-invoice)

Definir up:

1. [Plano de contas](/docs/pt/accounts/chart-of-accounts)
2. [Empresa](/docs/pt/setting-up/company-setup) (para contas padrão)

## 2. Como criar um Lançamento de Pagamento

Ao enviar um documento no qual o Lançamento de Pagamento pode ser feito, você encontrará a opção Pagamento no botão **Criar**.

 ![Entrada de pagamento da fatura de vendas](/files/payment-entry-button-in-sales-invoice.png)![]()  


1. Alterar a data de postagem.
2. O Tipo de Pagamento será definido com base na transação de origem. Os tipos são 'Receber', 'Pagar' e 'Transferência interna'.
3. O tipo de parte, parte e nome da parte serão obtidos automaticamente.
4. A conta paga para e a conta paga de serão obtidas conforme definido em [Formulário da empresa](/docs/pt/setting-up/company-setup).
5. O valor pago será obtido na fatura.
6. Salvar e enviar. ![Entrada de pagamento de SO](/files/payment-entry-from-invoice.gif)![]()

### 2.1 Criando um pagamento manualmente

Uma entrada de pagamento criada manualmente não terá nenhum pedido/fatura vinculado a ele. Os pagamentos efetuados serão registrados na conta do Cliente/Fornecedor e poderão ser reconciliados posteriormente usando o [Ferramenta de reconciliação de pagamentos](/docs/pt/accounts/payment-reconciliation).

1. Vá para a lista Entrada de pagamentos e clique em Novo.
2. Selecione o tipo de parte e o respectivo cliente/fornecedor.
3. Selecione a conta bancária/conta em dinheiro paga para e paga de. Insira o número do cheque e a data se for transferência bancária.
4. Insira o valor pago.
5. Salve e envie.

## 3. Recursos

### 3.1 Configuração do modo de pagamento

**Modo de pagamento**: inserir isso ajuda a classificar as entradas de pagamento com base no modo de pagamento usado. As formas de pagamento podem ser bancárias, em dinheiro, transferência bancária, etc.


> **Dica**: no [Modo de pagamento](/docs/pt/accounts/mode-of-payment) mestre, a conta padrão pode ser definida. Esta conta de pagamento padrão será buscada nas entradas de pagamento.
> 
> 

### 3.2 Pagamento de/para

![Parte do pagamento](/files/payment-from-to.png)![]()  


* **Tipo de parte**: seja cliente, fornecedor, funcionário, acionista, estudante ou membro de ONG.
* **Parte**: a parte específica para a qual o lançamento de pagamento é feito.
* **Nome da parte**: o nome da parte , isso será obtido automaticamente.
* **Conta bancária da empresa**: [Conta bancária](/docs/pt/accounts da sua empresa/conta bancária).
* **Conta bancária do partido**: A [Conta bancária](/docs/pt/accounts/bank-account).
* **Contato**: Se a Parte for uma organização, uma pessoa de contato pode ser armazenada aqui.

### 3.3 Contas

![Contas de pagamento](/files/payment-accounts.png)![]()  


* **Saldo da Parte**: o valor total a receber ou a pagar do Cliente ou Fornecedor das Faturas definidas na Entrada de Pagamento atual. Os valores pagos serão positivos e, se forem feitos pagamentos antecipados, serão negativos.
* **Conta paga de**: [Conta](/docs/pt/accounts/chart-of-accounts) da qual o valor será deduzido quando o pagamento for enviado.

* * **Conta paga para**: o [Conta CoA](/docs/pt/accounts/chart-of-accounts) da qual o valor será adicionado quando a entrada de pagamento for enviada.
* **Moeda da conta: as moedas dessas contas serão obtidas conforme definido em [Conta](/docs/pt/accounts/chart-of-accounts) e não pode ser editada aqui. Para saber mais sobre transações em diversas moedas, [visite esta página](/docs/pt/accounts/multi-currency-accounting) .**
* **Saldo da conta**: o saldo total de todas as faturas das contas selecionadas.

**Valor Pago**: O **valor total** pago pela Entrada de Pagamento atual é mostrado neste campo.


> **Observação**: Ao fazer lançamentos de pagamento, a conta bancária padrão será buscada na seguinte ordem, se definida:
> 
> 


> * Formulário da empresa
> * Conta padrão do modo de pagamento
> * Conta bancária padrão do cliente/fornecedor
> * Selecione manualmente em Entrada de Pagamento
> 

### 3.4 Referência

#### Buscando faturas pendentes

Isso pode ser usado para faça pagamentos para várias faturas de vendas usando uma entrada de pagamento. Ao criar uma nova Entrada de Pagamento, ao clicar no botão **Obter Faturas Pendentes** ou no botão **Obter Pedidos Pendentes**, todas as Faturas pendentes e Pedidos em aberto respectivamente serão buscados para o partido. Você precisa inserir o 'Valor Pago' para ver este botão. A partir daqui, um intervalo de datas e faturas a serem obtidas podem ser selecionados.

Se a Parte não tiver efetuado o pagamento integral, insira o valor pago no campo 'Alocado'.

Se estiver criando Entrada de Pagamento para um Cliente, o Valor do Pagamento será alocado em uma Fatura de Venda. Na mesma linha, ao criar um Lançamento de Pagamento para um Fornecedor, o Valor do Pagamento será alocado em uma Fatura de Compra.

#### Tabela de Referências de Pagamento

* **Tipo** : se o pagamento está sendo feito em relação a um pedido de venda, fatura de venda ou lançamento contábil manual.
* **Nome**: a transação específica O ID é buscado/selecionado aqui.
* **Valor total**: o valor total de uma fatura/lançamento contábil na linha.
* **Pendente**: o valor a receber/pagar por esta fatura.
* **Alocado**: Se o Valor Pago for menor que o valor da fatura apenas o valor pago será alocado na(s) fatura(s) buscada(s) no Lançamento de Pagamento. O pagamento poderá ser feito em parcelas, por exemplo, se houver três faturas de valores 20, 20, 20, o Valor Pago for 60 então esse Valor Pago será distribuído igualmente. [Termos de pagamento](/docs/pt/accounts/payment-terms) também podem estar envolvidos.

![payment_entry_get_outstanding_buttons](/files/payment_entry_get_outstanding_buttons.png "payment_entry_get_outstanding_buttons.png")![]()  


#### O que é valor não alocado?

Quando um pagamento O lançamento é feito no ERPNext e o Valor Pago é superior ao valor total da fatura, fica armazenado na conta do Cliente/Fornecedor. Este montante é, portanto, atualmente «Não atribuído». O valor não alocado pode ser usado em faturas futuras.

Por exemplo, você cria uma fatura de vendas totalizando 1.000 e o cliente paga 1.500. Quando outra fatura for criada para este Cliente no futuro no valor de 1.000 novamente, os 500 pagos anteriormente poderão ser usados.

### 3.5 Deduções ou Perdas

Quando uma Entrada de Pagamento é criada em relação a uma fatura , poderá haver alguma diferença no Valor Pago real e no valor pendente da fatura. Esta diferença pode dever-se a erros de arredondamento ou a alterações na taxa de câmbio. Você pode definir uma conta aqui onde esse valor de diferença será contabilizado.

As perdas/deduções podem ser amortizadas. Vejamos aqui um exemplo onde o valor pago é 25 mas o valor alocado é 30 já que 30 é o valor a ser cobrado conforme a fatura. O 'Valor da Diferença' será 5 neste caso. Esse valor de diferença pode ocorrer por conta de descontos ou câmbio. O Valor da Diferença precisa ser 0 para enviar a Entrada de Pagamento. Isto pode ser ajustado usando o botão **Fazer entrada de diferença**. O valor será ajustado na conta Write Off.

![Writing Off](/files/payment-write-off.gif)![]()  


### 3.6 Baixa

 A baixa acontece quando o valor pago é menor que o valor alocado. Ou seja o valor restante é considerado perdido em encargos diversos ou esse valor não será pago. Isso é considerado perda.

### 3.5 Após enviar

Salvar e enviar entrada de pagamento. No envio, o saldo pendente será atualizado nas faturas.

![Status da fatura atualizado para pago](/files/fatura-marked-paid-by-payment-entry.png)![]()  


Se Foi criado um lançamento de pagamento contra Pedido de Venda ou Pedido de Compra, o campo 'Antecipação Paga' será atualizado neles. Ao criar uma fatura com base nessas transações, o lançamento de pagamento será atualizado automaticamente nessa fatura para que você possa alocar o valor da fatura contra a entrada de pagamento antecipado.

Para pagamentos recebidos, o lançamento das contas será feito da seguinte maneira.

* Débito: conta bancária ou dinheiro
* Crédito: Cliente (Devedor)

 Para saída de pagamento:

* Débito: Fornecedor (Credor)
* Crédito: Conta bancária ou dinheiro

## 4. Outros casos

### 4.1 Entrada de pagamento multimoeda

Se você deseja manter uma conta a receber/a pagar em moeda estrangeira, crie contas com moeda estrangeira (diferente da moeda da empresa) e vincule-as na conta do partido. Por exemplo:

![Moeda não padrão em contas a receber no cliente](/files/non-standard-currency-receivable.png)![]()  


ERPNext permite manter contas e faturamento em [múltiplas moedas](/docs/pt/accounts/multi-currency-accounting). Se uma fatura for feita na moeda da parte, a Taxa de Câmbio entre a moeda base da Empresa e a moeda da parte também será inserida na fatura.


> Observação: uma conta separada de Devedor/Credor precisa ser criada e selecionado na Nota Fiscal/Pedido de Venda para que o câmbio funcione corretamente. Por exemplo, se o Cliente for dos EUA, crie uma conta a receber chamada 'Devedores dos EUA'.
> 
> 

Ao criar Entrada de Pagamento com base nessa fatura, a taxa de câmbio atual será obtida, mas você Você pode definir a taxa de câmbio no momento do pagamento para corresponder aos seus registros.

Clique no botão **Definir ganhos/perdas cambiais** para adicionar automaticamente uma linha para amortizar o valor da diferença. .

![Taxa de câmbio na entrada de pagamento](/files/exchange-rate-in-payment-entry.png)![]()  


Como a taxa de câmbio da moeda flutua o tempo todo, isso pode levar a uma diferença no valor do pagamento em relação ao total da fatura. Esse valor de diferença pode ser contabilizado no Valor de ganhos/perdas cambiais.

![Exchange Gain Loss Ledger](/files/exchange-gain-loss-ledger.png)![]()  


Os pagamentos podem também se tornará independente de faturas criando uma nova entrada de pagamento.

Para saber mais sobre como gerenciar transações em diversas moedas [visite esta página](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency).

### 4.2 Transferência interna

Transferência interna é utilizado nos casos em que o dinheiro é transferido entre contas da mesma Empresa. Por exemplo, se um cliente dos EUA usa o PayPal, a transferência de dinheiro do PayPal para uma conta bancária pode ser considerada uma transferência interna.

As seguintes transferências internas podem ser gerenciadas na entrada de pagamento.

1. Banco-Dinheiro
2. Banco-Banco
3. Dinheiro-Dinheiro
4. Dinheiro-Banco

![Transferência interna via entrada de pagamento](/files/payment-entry-internal-transfer.png)![]()  


### 4.3 Gerenciando diferentes cenários de pagamento

Para uma fatura não paga, valor pendente = total geral. Ao criar Entradas de Pagamento, o valor do valor pendente será reduzido.

Na maioria dos casos, além das vendas no varejo, o faturamento e os pagamentos são atividades separadas. Existem diversas combinações em que esses pagamentos são feitos. Esses casos se aplicam a vendas e compras.

* Eles podem ser antecipados (100% adiantado).
* Pós-envio. Na entrega ou alguns dias após a entrega.
* Parte antecipada e parte na entrega ou após a entrega.
* Pagamentos podem ser feitos juntos para várias faturas.
* Os adiantamentos podem ser feitos juntos para várias faturas (e podem ser divididos entre faturas).
ERPNext permite gerenciar todos esses cenários. Todos os lançamentos contábeis (Lançamento Contábil) podem ser feitos em uma Fatura de Venda, Fatura de Compra ou Lançamento de Pagamento de adiantamento (em casos especiais, uma fatura também pode ser feita por meio de uma Fatura de Venda).

O total pendente o valor de uma fatura é a soma de todos os lançamentos contábeis feitos “contra” (ou vinculados a) essa fatura. Dessa forma, você pode combinar ou dividir pagamentos no Lançamento de Pagamento para gerenciar os cenários.

### 4.4 Diferença entre Lançamento de Pagamento e Lançamento Contábil

1. O uso do Lançamento Contábil requer um entendimento da qual a conta será debitada ou creditada. No Entrada de Pagamento, ele é gerenciado no backend, portanto mais simples para o Usuário.
2. O Entrada de Pagamento é mais eficiente no gerenciamento de pagamentos em moedas estrangeiras.
3. Os cheques podem ser impressos a partir de lançamentos de pagamento usando o formato de impressão de cheque.
4. Os lançamentos contábeis manuais ainda podem ser usados ​​para:


	+ Atualizando o saldo inicial em Contas.
	+ Lançamento de depreciação de ativos fixos.
	+ Para ajustar a nota de crédito em relação a Fatura de venda e nota de débito em relação à fatura de compra, caso não haja nenhum pagamento.

### 4.5 Pagamentos usando lançamento contábil manual

Para efetuar o pagamento usando o lançamento contábil manual, siga estas etapas:

1. Ative o pagamento via lançamento contábil manual. Vá para **Contabilidade > Mestre de Contabilidade > Configurações de Contas**, marque a caixa 'Efetuar Pagamento via Lançamento Contábil'. ![Ativar entrada de pagamento via entrada de diário](/files/enable-payment-entry-via-journal-entry.png)![]()
2. Ao enviar um documento no qual o lançamento contábil manual pode ser feito , você encontrará o Pagamento no botão **Criar**.
3. Salve e envie o lançamento contábil manual para registrar o pagamento na fatura

## 5. Tópicos relacionados

1. [Solicitação de pagamento](/docs/pt/accounts/payment-request)
2. [Condições de pagamento](/docs/pt/accounts/payment-terms)
3. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
4. [Fatura de compra](/docs/pt/accounts/purchase-fatura)


