# Entrada no diário



**Um lançamento contábil manual é um lançamento feito no razão geral e indica as contas afetadas.**


Um lançamento contábil manual é uma transação multifuncional onde as contas de débito e crédito podem ser selecionadas.


Todos os tipos de lançamentos contábeis, exceto transações de vendas e compras, são feitos usando o **Lançamento Diário**. Um **lançamento contábil** é uma transação contábil padrão que afeta diversas contas e a soma dos débitos é igual à soma dos créditos. Um lançamento contábil manual afeta o razão principal.


Os lançamentos contábeis manuais podem ser usados ​​para inserir despesas, abrir lançamentos, contra-lançamentos, pagamentos bancários, lançamentos de impostos especiais de consumo, etc. Por exemplo, registrar despesas correntes, despesas diretas como gasolina/transporte, despesas diversas, lançamentos de ajuste e ajuste do valor da fatura .



> 
> Nota: A partir da versão 13 introduzimos o livro razão imutável que muda a forma como o cancelamento de lançamentos contábeis funciona no ERPNext. [Saiba mais aqui](/docs/pt/accounts/articles/immutable-ledger-in-erpnext).
> 
> 
> 


Para acessar a lista de lançamentos contábeis manuais, vá para:



> 
> Página inicial > Contabilidade > Razão > Lançamento contábil manual
> 
> 
> 


## 1. Como criar um lançamento contábil manual


1. Vá para a lista de lançamentos contábeis manuais e clique em Novo.
2. O tipo de entrada padrão será 'Lançamento de diário'. Este é um tipo de entrada de uso geral. Visite a [seção 3](/docs/pt/accounts/journal-entry#3-journal-entry-types) para saber mais sobre os tipos de entrada.
3. Você pode alterar a data de postagem.
4. Expanda a tabela e selecione uma conta da qual o valor será debitado.
5. Os detalhes acima podem ser adicionados a partir de um [Modelo de entrada de diário](/docs/pt/accounts/journal-entry-template) também com o 'Do modelo' campo.
6. Selecione o Tipo de Parte e a Parte se for uma entrada de Devedor.
7. Adicione uma linha onde o valor será creditado.
8. Observe que, no final, os valores totais de débito e crédito devem ser iguais.
9. Salvar e enviar.


![Lançamento de diário](/files/journal-entry.png)


**Livro Financeiro**: você pode postar esta entrada em um [Livro Financeiro](/docs/pt/accounts/finance-book) específico . Ao deixar este campo em branco, este Lançamento Contabilístico aparecerá em todos os Livros Financeiros. Este campo só estará visível se a opção 'Ativar livros financeiros' na seção Padrões de ativos fixos do cadastro da empresa estiver marcada.


### 1.1 Entrada Rápida


Ao criar um lançamento contábil manual, um botão de **Entrada Rápida** pode ser visto no canto superior direito. Isso torna a criação do lançamento contábil manual um pouco mais fácil. Insira o valor, selecione as contas, adicione um comentário. Isso preencherá a tabela 'Lançamentos contábeis' com os detalhes selecionados.


![Entrada rápida](/files/quick-journal-entry.png)


## 2. Recursos


### 2.1 Lançamentos contábeis


1. **Dimensões Contábeis**: Um Projeto ou Centro de Custo pode ser vinculado aqui para rastrear o custo separadamente. Para saber mais, [visite esta página](/docs/pt/accounts/accounting-dimensions). ![Dimensão contábil](/files/journal-entry-accounting-dimension.png)
2. **Número da conta bancária**: se você adicionou uma [Conta bancária](/docs/pt/accounts/bank-account), o número associado a essa conta bancária será obtido.
3. **Tipo de Referência**: Se este Lançamento Contábil estiver associado a outra transação, ele poderá ser referenciado aqui. Selecione o Tipo de Referência e selecione o documento específico. Por exemplo, se você estiver criando um lançamento contábil manual em relação a uma fatura de vendas específica. Vincule este lançamento contábil manual à fatura. O valor “pendente” dessa fatura será afetado.
4. ![Reference](/files/journal-entry-reference.png)


A seguir estão os documentos que podem ser selecionados no lançamento contábil manual em Tipo de referência:


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. Lançamento do diário
4. [Ordem de vendas](/docs/pt/selling/sales-order)
5. [Pedido de compra](/docs/pt/buying/purchase-order)
6. [Relatório de despesas](/docs/pt/human-resources/expense-claim)
7. [Ativo](/docs/pt/asset/asset)
8. [Empréstimo](/docs/pt/loan-management/loan)
9. [Lançamento da folha de pagamento](/docs/pt/human-resources/payroll-entry)
10. [Avanço do funcionário](/docs/pt/human-resources/employee-advance)
11. [Reavaliação da taxa de câmbio](/docs/pt/accounts/exchange-rate-revaluation)
12. [Desconto na fatura](/docs/pt/accounts/invoice_discounting)
13. **É Adiantamento**: Se este for um pagamento antecipado de um Cliente, defina esta opção como 'Sim'. Isto é útil quando você vincula um formulário 'Tipo de referência' a este lançamento contábil manual. Selecionar “Sim” vinculará este lançamento contábil manual à transação selecionada no campo 'Nome de referência'. Para saber mais, visite a página [Entrada de pagamento antecipado](/docs/pt/accounts/advance-payment-entry).
14. **Observação do usuário**: quaisquer comentários adicionais sobre a entrada podem ser adicionados neste campo.


### 2.2 Lançamento reverso no diário


Em qualquer Lançamento Contábil enviado, há um botão dedicado para reverter o Lançamento Contábil. Ao clicar no botão 'Reverter lançamento contábil manual', o sistema cria um novo lançamento contábil revertendo o valor do débito e do crédito nas respectivas contas.


![Reverse Journal Entry](/files/reverse-journal-entry.png)


### 2.3 Entrada de diferença


A “Diferença” é a diferença que resta após a soma de todos os valores de débito e crédito.


De acordo com o sistema de contabilidade de partidas dobradas, o débito total deve ser igual ao crédito total.


Deve ser zero se o Lançamento Contábil for “Enviado”. Caso esse número não seja zero, você pode clicar em “Fazer lançamento de diferença” e o sistema adicionará automaticamente uma nova linha com o valor necessário para zerar o total. Selecione a conta para debitar/crédito e prossiga.


![Make Difference](/files/journal-entry-make-difference-entry.png)


### 2.4 Referenciação


Um número de referência pode ser inserido manualmente e uma data de referência pode ser definida. Ao inserir um Número de Referência aqui, uma 'Observação' será vista, por exemplo:



> 
> Nota: fornecedor
> 
> 
> 



> 
> Referência nº 2321 datada de 30/09/2019 ₹ 1.000,00 em relação à fatura de vendas ACC-SINV-2019-00064
> 
> 
> 


Na seção Referência, os seguintes campos podem ser inseridos manualmente se a conta foi registrada offline e não no sistema ERPNext. Isto é apenas para fins de referência.


1. Número da fatura
2. Data da fatura
3. Data de vencimento


### 2.5 Entradas em múltiplas moedas


Se as contas selecionadas estiverem em moedas diferentes, marque a caixa de seleção 'Multimoedas'. Se esta caixa de seleção não estiver ativada, você não poderá selecionar nenhuma moeda estrangeira no lançamento contábil manual. Isto irá mostrar a moeda diferente e obter a 'Taxa de Câmbio'. Para saber mais, visite a página [Contabilidade multimoeda](/docs/pt/accounts/multi-currency-accounting).


![Multi-moeda](/files/multi-currency-journal-entry.png)


### 2.6 Modelo de entrada de diário


Campo **Do modelo**: selecionar uma opção carregará os detalhes de um modelo de lançamento contábil manual.


Ele buscará e adicionará os seguintes detalhes à entrada:


1. Tipo de entrada
2. Empresa
3. Série
4. Contas em lançamentos contábeis
5. Está abrindo


Para saber mais, acesse a página [Modelo de entrada de diário](/docs/pt/accounts/journal-entry-template).


### 2.7 Configurações de impressão


![Configurações de impressão do diário](/files/journal-entry-print-settings.png)


**Pagar para/Recebido de**: O nome inserido aqui aparecerá na fatura de vendas. Isto é útil para imprimir cheques. Vá para a visualização de impressão no lançamento contábil manual e selecione o 'Formato de impressão de cheque'.


#### Papel timbrado


Você pode imprimir seu lançamento contábil manual em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


#### Imprimir títulos


As entradas do diário também podem ter títulos diferentes para fins de impressão. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos títulos de impressão, vá para:


Página inicial > Configurações > Impressão > Cabeçalho de impressão


Leia [Imprimir cabeçalhos](/docs/pt/setting-up/print/print-headings) para saber mais.


### 2.7 Mais informações


1. **Modo de pagamento**: se o pagamento foi feito por transferência bancária, cheque bancário, cartão de crédito, cheque ou dinheiro. Novas formas de pagamento também podem ser criadas. Se uma conta bancária estiver definida como forma de pagamento, ela será obtida aqui quando a forma de pagamento for selecionada.
2. **Está abrindo**: Se o Lançamento Contábil for do tipo 'Lançamento de Abertura' este campo será definido como 'Sim'. Para saber mais, visite a página [Saldo inicial](/docs/pt/accounts/opening-balance).
3. **Do modelo**: quando um modelo é selecionado, a tabela 'Entradas contábeis' será esvaziada primeiro, antes de carregar as contas do modelo. Você pode adicionar mais entradas de conta depois disso.


## 3. Tipos de lançamento contábil manual


Vamos dar uma olhada em alguns dos lançamentos contábeis comuns que podem ser feitos através do lançamento contábil manual no ERPNext.


### 3.1 Lançamento de diário


Este é um tipo de entrada de uso geral que pode ser usado para diferentes propósitos. Vejamos alguns exemplos.


#### Despesas (não acumuladas)


Muitas vezes pode não ser necessário acumular uma despesa, mas ela pode ser contabilizada diretamente em uma conta de despesas no momento do pagamento. Por exemplo, um subsídio de viagem ou uma conta de telefone. Você pode debitar diretamente as despesas telefônicas (em vez da companhia telefônica) e creditar seu banco no momento do pagamento.


1. Débito: conta de despesas (como despesas de telefone).
2. Crédito: conta bancária ou em dinheiro.


#### Crédito de salários


Para creditar salários de funcionários, é usado o tipo 'Lançamento Diário'. Neste caso,


1. Débito: os componentes do salário.
2. Crédito: a conta bancária.


### 3.2 Lançamento contábil entre empresas


Se uma transação ocorrer entre uma empresa controladora e uma empresa filha, ou empresas irmãs, ou duas empresas pertencentes ao mesmo grupo, esta opção poderá ser usada para fazer um lançamento contábil entre empresas.


Para saber mais, visite a página [Lançamento contábil entre empresas](/docs/pt/accounts/inter-company-journal-entry).


### 3.3 Entrada bancária


Use esse tipo ao efetuar ou receber um pagamento usando uma [Conta bancária](/docs/pt/accounts/bank-account). Por exemplo, pagar despesas de entretenimento, etc., usando a conta bancária da Empresa.


### 3.4 Entrada em dinheiro


É o mesmo que 'Entrada Bancária', mas o pagamento é feito através de Conta em Dinheiro.


### 3.5 Entrada de cartão de crédito


Este é um tipo de entrada para identificar facilmente todas as entradas de cartão de crédito.


### 3.6 Nota de Débito


Este é um documento enviado por um cliente (sua Empresa) a um fornecedor (seu Fornecedor) ao devolver mercadorias/itens.


Você também pode criar uma nota de débito diretamente de uma fatura de compra.


A "Nota de Débito" é feita para um Fornecedor contra uma Fatura de Compra ou aceita como uma nota de crédito do Fornecedor quando uma empresa devolve mercadorias. Quando uma Nota de Débito é emitida, a Empresa pode receber um pagamento do Fornecedor ou ajustar o valor em outra fatura.


1. Débito: Conta do Fornecedor.
2. Crédito: conta de devolução de compra.


Para saber mais, [visite esta página](/docs/pt/accounts/debit-note).


### 3.7 Nota de crédito


Este é um documento enviado por um fornecedor a um cliente ao devolver mercadorias/itens.


A "Nota de Crédito" é emitida para um Cliente contra uma Fatura de Venda quando a empresa precisa ajustar um pagamento por mercadorias devolvidas. Quando uma Nota de Crédito é emitida, o vendedor pode efetuar um pagamento ao cliente ou ajustar o valor em outra fatura.


1. Débito: conta de devolução de vendas.
2. Crédito: Conta do Cliente.


Para saber mais, [visite esta página](/docs/pt/accounts/credit-note).



> 
> Uma nota de débito/crédito geralmente é emitida pelo valor das mercadorias devolvidas ou inferior.
> 
> 
> 


### 3.8 Contraentrada


Uma Contra Entrada é registrada quando a transação é registrada dentro da mesma Empresa dos tipos:


1. Dinheiro em dinheiro
2. De banco para banco
3. Dinheiro para banco
4. Banco para dinheiro


Isso é usado para registrar saques ou depósitos de dinheiro de uma conta bancária. Quando esta entrada é utilizada, o dinheiro não sai da empresa a menos que seja novamente usado para pagar alguma coisa.


### 3.9 Entrada de impostos especiais de consumo


Quando uma Empresa compra mercadorias de um Fornecedor, a empresa paga impostos especiais de consumo sobre essas mercadorias ao Fornecedor. E quando uma empresa vende estes produtos aos Clientes, recebe impostos especiais de consumo. A empresa deduzirá o imposto especial de consumo a pagar e o saldo do depósito no governo. conta.


Quando uma empresa compra mercadorias com impostos especiais de consumo:


1. Débito: conta de compra, conta de impostos especiais de consumo.
2. Crédito: Conta do Fornecedor.


Quando uma empresa vende mercadorias com impostos especiais de consumo:


1. Débito: Conta do Cliente.
2. Crédito: conta de vendas, conta de impostos especiais de consumo.



> 
> Observação: aplicável na Índia, pode não ser aplicável em seu país. Verifique os regulamentos do seu país.
> 
> 
> 


### 3.10 Baixas ou dívidas incobráveis


Se você estiver baixando uma fatura como uma dívida inadimplente, poderá criar um comprovante contábil semelhante a um pagamento, exceto que, em vez de debitar seu banco, você poderá debitar uma conta de despesas chamada Dívidas incobráveis.


1. Débito: dívidas incobráveis ​​anuladas
2. Crédito: Cliente



> 
> Observação: pode haver regulamentações em seu país antes que você possa amortizar dívidas incobráveis.
> 
> 
> 


### 3.11 Inscrição de Abertura


Esta entrada é útil ao mudar de outro software para o ERPNext durante qualquer época do ano. Suas contas pendentes, ações, etc. podem ser registradas no ERPNext usando este tipo de entrada. Selecionar o tipo irá buscar as contas do Balanço Patrimonial.


### 3.12 Depreciação


A depreciação ocorre quando você baixa determinado valor de seus ativos como despesa. Por exemplo, se você tiver um computador que usará por, digamos, 5 anos, poderá distribuir suas despesas ao longo do período e passar um lançamento contábil manual no final de cada ano, reduzindo seu valor em uma determinada porcentagem.


1. Débito: Depreciação (Despesa).
2. Crédito: Ativo (a conta sob a qual você registrou o ativo a ser depreciado).


Para saber mais, visite a página [Depreciação de ativos](/docs/pt/asset/asset-depreciation).



> 
> Observação: pode haver regulamentos em seu país que definam o valor que você pode depreciar uma classe de ativos.
> 
> 
> 


### 3.13 Reavaliação cambial


Se o seu Plano de Contas possui contas com múltiplas moedas, um Lançamento Contábil do tipo 'Reavaliação Cambial' ajuda a lidar com esta situação. Esta entrada deve ser criada a partir de um formulário de Reavaliação da Taxa de Câmbio. Para saber mais [visite a página Reavaliação da Taxa de Câmbio](/docs/pt/accounts/exchange-rate-revaluation).


### 4. Tópicos Relacionados


1. [Lançamento contábil entre empresas](/docs/pt/accounts/inter-company-journal-entry)
2. [Nota de crédito](/docs/pt/accounts/credit-note)
3. [Nota de débito](/docs/pt/accounts/debit-note)
4. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
5. [Botão de entrada de diferenças](/docs/pt/accounts/articles/difference-entry-button)
6. [Livro de finanças](/docs/pt/accounts/finance-book)



