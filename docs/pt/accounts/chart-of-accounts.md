# Plano de contas



**O plano de contas é o modelo das contas da sua organização.**


A estrutura geral do seu Plano de Contas é baseada em um sistema de dupla entrada
contabilidade que se tornou um padrão em todo o mundo para quantificar como um
a empresa está se saindo financeiramente.


Plano de contas é uma visualização em árvore dos nomes das contas (razões e
Grupos) que uma Empresa exige para gerenciar seus livros de contas. Conjuntos ERPNext
criar um plano de contas simples para cada empresa que você criar, mas você pode
modifique-o de acordo com suas necessidades e requisitos legais.


Para cada empresa, Plano de Contas significa a forma de classificar os lançamentos contábeis, principalmente
com base em requisitos legais (fiscais, de conformidade com regulamentações governamentais).


![CoA Tree](/files/chart-of-accounts-tree.png)


O Plano de contas ajuda você a responder perguntas como:


* Quanto vale a sua organização?
* Quanta dívida você contraiu?
* Quanto lucro você está obtendo (e, portanto, pagando impostos)?
* Quanto você está vendendo?
* Qual ​​é a divisão das suas despesas?


Como alguém que gerencia uma empresa, é muito valioso ver quão bem
sua empresa está indo.


> **Dica**: se você não consegue ler um Balanço Patrimonial, é uma boa oportunidade para começar a aprender sobre isso. Valerá a pena o esforço. Você também pode contar com a ajuda de seu contador para configurar seu plano de contas.


Para acessar a lista do Plano de Contas, acesse:
> Home > Contabilidade > Mestres de Contabilidade > Plano de Contas


## 1. Como criar/editar contas


ERPNext vem com um plano de contas padrão. Em vez de criar/modificar, você também pode usar a ferramenta [Importador de plano de contas](/docs/pt/setting-up/chart-of-accounts-importer). Observe que o plano de contas existente será substituído quando esta ferramenta for usada.


1. Vá para a lista Plano de contas.


Aqui você pode abrir contas de grupo que contenham outras contas. Existem opções para “Adicionar criança” em uma conta, Editar ou Excluir a conta.


![Plano de contas](/files/chart-of-accounts-add.gif)
2. A opção de criar uma conta infantil só aparecerá se você clicar em um tipo Grupo (pasta)
Conta.
3. Digite um nome para a conta.
4. Insira um número para a conta.
5. Marque 'É Grupo' se quiser que esta seja uma conta de grupo que possa conter outras contas.
6. Selecione o tipo de conta. Selecionar esta opção é importante porque alguns campos permitem selecionar apenas tipos específicos de contas.
7. Altere a moeda se esta conta for usada para transações com moedas diferentes. Por padrão, é a moeda da Empresa. Para saber mais, visite a página [Contabilidade multimoeda](/docs/pt/accounts/multi-currency-accounting).
8. Clique em **Criar novo**.


Normalmente, você pode querer criar contas para:


* Viagens, salários, telefone, etc. em **Despesas**.
* Imposto sobre Valor Agregado (IVA), Imposto sobre Vendas, Patrimônio Líquido, etc. no **Passivo Circulante**.
* Vendas de produtos, vendas de serviços, etc. em **Renda**.
* Construções, máquinas, móveis, etc. em **Ativos Fixos**.


![Plano de contas](/files/coa-root-accounts.png)


> Dica: contas com moedas diferentes são criadas quando você recebe ou efetua pagamentos de ou para moedas diferentes. Por exemplo, se você mora na Índia e faz transações com os EUA, pode ser necessário criar contas como 'Devedores dos EUA', 'Credores dos EUA', etc.


Vamos entender os principais grupos do Plano de Contas.


## 2. Tipos de conta


Os tipos de contas são classificados principalmente como receitas, despesas, ativos ou passivos.


### 2.1 Contas de balanço


As contas do balanço são 'Aplicação de Fundos (Ativos)' e 'Fontes de Fundos
(Passivo)' que significa o patrimônio líquido da sua empresa em um determinado momento.
Quando você inicia ou termina um período financeiro, todos os Ativos são iguais ao
Passivos.


> **Uma observação sobre contabilidade**: Se você é novo em contabilidade, deve estar se perguntando: como pode
Os ativos são iguais aos passivos? Isso significaria que a empresa não tem nada de seu
ter. Está correto! Todos os “investimentos” feitos na empresa para comprar ativos (como
terrenos, móveis, máquinas) é feita pelos proprietários. Os proprietários são uma responsabilidade perante o
empresa, já que os lucros pertencem aos proprietários.


> Se uma empresa fechasse, precisaria vender todos os
ativos e pagar todos os passivos (incluindo lucros) aos proprietários,
ficando sem nada.


Todas as contas do Balanço Patrimonial representam um ativo de propriedade da empresa, como "Banco
Conta", "Terreno e Propriedade", "Móveis" ou um passivo (fundos que o
empresa deve a terceiros), como "Fundos dos proprietários", "Dívida" etc.


Duas contas especiais a serem observadas aqui são Contas a Receber (dinheiro que você precisa
cobrar de seus clientes) e Contas a Pagar (dinheiro que você tem que pagar para
seus fornecedores) em Ativos e Passivos, respectivamente.


### 2.2 Contas de lucros e perdas


Lucros e Perdas é o grupo de contas de 'Receitas' e 'Despesas' que representam
suas transações contábeis durante um período.


Ao contrário das contas de balanço, as contas de lucros e perdas (ou contas PL)
não representam o patrimônio líquido (Ativos), mas sim a quantidade de dinheiro
gastos e arrecadados no atendimento aos clientes durante o período. Portanto, ao
início e final do seu ano fiscal, eles se tornam zero.


No ERPNext é fácil acompanhar os lucros e perdas através do gráfico de lucros e perdas.


![Relatório de lucros e perdas](/files/profit-and-loss-report.png)


Observe que, no primeiro dia do ano, você não obteve nenhum lucro ou prejuízo, mas
ainda têm ativos, portanto, as contas do balanço nunca se tornam zero no
início ou fim de um período.


### 2.3 Grupos e Razões


Existem dois tipos principais de Contas no ERPNext-Grupo e Razão. Os grupos podem
têm subgrupos e livros-razão dentro deles, enquanto os livros-razão são os nós folha de
seu gráfico e não pode conter mais contas nele.


As transações contábeis só podem ser feitas em contas contábeis (não em grupos)


> Informações: O termo "Ledger" significa uma página de um livro contábil onde os lançamentos são
feito. Geralmente há um razão para cada conta (como um Cliente ou um
Fornecedor).


> Observação: um “razão” de conta às vezes também é chamado de “chefe” da conta.


![Grupos e livros contábeis no CoA](/files/coa-group-and-ledger.png)


### 2.4 Outros tipos de conta


No ERPNext, você também pode especificar mais informações ao criar um novo
Conta, existe para ajudá-lo a selecionar essa conta específica em um cenário como 'Conta bancária' ou 'Conta fiscal' e não tem efeito no gráfico
em si.


Explicação dos tipos de conta:


* **Depreciação Acumulada**: Para armazenar as informações de depreciação total acumulada dos Ativos da Empresa. A depreciação acumulada aparece no balanço patrimonial.
* **Ativo recebido mas não faturado**: uma conta de passivo temporário que contém o valor do ativo recebido, mas ainda não faturado.
* **Banco**: o tipo de conta sob a qual as contas bancárias serão criadas. Deve haver pelo menos uma conta de grupo do tipo "Banco" no CoA.
* **Dinheiro**: o tipo de conta sob a qual a conta em dinheiro será criada. Deve haver pelo menos uma conta de grupo do tipo "Dinheiro" no CoA.
* **Cobrável**: Cobranças adicionais aplicadas a Itens podem ser armazenadas em contas deste tipo. Por exemplo, "Encargos de frete e expedição".
* **Trabalho de capital em andamento**: Os encargos atuais ao criar Ativos Fixos são armazenados em contas CWIP. Por exemplo, custos de construção na construção de um edifício. No ERPNext, os ativos são contabilizados em contas CWIP quando ainda não estão sendo usados.
* **Custo dos Produtos Vendidos**: Uma conta deste tipo é usada para contabilizar o total acumulado de todos os custos incorridos durante a fabricação/compra de um produto ou serviço vendido por uma Empresa.
* **Depreciação**: A conta de despesas para contabilizar a depreciação dos ativos fixos. Isso aparece na demonstração de resultados.
* **Patrimônio**: esse tipo de conta representa transações com pessoas que possuem o negócio, ou seja, os acionistas/proprietários.
* **Despesas incluídas na avaliação de ativos**: a conta para registrar as despesas (exceto os custos diretos de material dos ativos) incluídas no custo final de um ativo.
* **Despesas incluídas na avaliação**: A conta para registrar as despesas (exceto os custos diretos de materiais) incluídas no custo final de um item/produto, usado no estoque permanente.
* **Ativo Fixo**: A conta para manter os custos dos ativos fixos.
* **Conta de Receita**: Este tipo de conta representa qualquer fonte de receita ou receita contabilizada para a Empresa.
* **A pagar**: O tipo de conta representa o valor devido por uma empresa aos seus credores (Fornecedores).
* **Recebíveis**: O tipo de conta representa o valor devido a uma empresa por seus devedores (Clientes).
* **Arredondamento**: em muitas faturas pode haver algum [arredondamento desligado](/docs/pt/accounts/articles/round-off-account-validation)no valor final. Para um rastreamento preciso, esses valores podem ser reservados para contas desse tipo.
* **Estoque**: o grupo de contas sob o qual [contas de armazém](/docs/pt/accounts/articles/round-off-account-validation) será criado.
* **Ajuste de estoque**: uma conta de despesas para registrar qualquer entrada de ajuste de estoque/estoque. Geralmente vem no mesmo nível de Custo dos Produtos Vendidos.
* **Estoque recebido, mas não faturado**: uma conta de responsabilidade temporária que contém o valor do estoque recebido, mas ainda não faturado e usado no estoque permanente.
* **Imposto**: todas as contas fiscais, como IVA, TDS, GST, etc., enquadram-se neste tipo.
* **Temporária**: Uma conta temporária é útil para equilibrar receitas, despesas e anulá-las ao mudar para o ERPNext no meio do ano com lançamentos contábeis pendentes.


> **Observação**: Ao fazer lançamentos de pagamento, a conta bancária padrão será buscada na seguinte ordem, se definida:


> \* Formulário da empresa
> \* Conta padrão de modo de pagamento
> \* Conta bancária padrão do cliente/fornecedor
> \* Selecione manualmente em Entrada de Pagamento


### 2.5 Demonstrações financeiras


As demonstrações financeiras da sua empresa são facilmente visualizadas no ERPNext. Você pode visualizar demonstrações financeiras
como Balanço Patrimonial, Demonstração de Lucros e Perdas e Demonstração de Fluxo de Caixa.


Um exemplo de várias demonstrações financeiras é fornecido abaixo:


1. Relatório de fluxo de caixa:


![Fluxo de caixa](/files/cash-flow.png)
2. Relatório de lucros e perdas:
![Relatório de lucros e perdas](/files/profit-and-loss-report.png)
3. Relatório de balanço patrimonial:


![Balance Sheet](/files/balance-sheet.png)


### 2.6 Número da conta


Um Plano de Contas padrão é organizado de acordo com um sistema numérico. Cada categoria principal começará com um determinado número e, em seguida, as subcategorias dentro dessa categoria principal começarão todas com o mesmo número. Por exemplo, se os activos são classificados por números que começam com o dígito 1000, então as contas de caixa podem ser rotuladas como 1100, as contas bancárias podem ser rotuladas como 1200, as contas a receber podem ser rotuladas como 1300, e assim por diante. Geralmente, é mantida uma lacuna entre os números das contas para adicionar contas no futuro.


Você pode atribuir um número ao criar uma conta na página Plano de contas. Você também pode editar um número do registro da conta clicando no botão **Atualizar nome/número da conta**. Ao atualizar o número da conta, o sistema renomeia o nome da conta automaticamente para incorporar o número no nome da conta.


![Número da conta](/files/update-account-number.png)


## 3. Vídeo








### 4. Tópicos Relacionados


1. [Saldo inicial](/docs/pt/accounts/opening-balance)
2. [Configurações de contas](/docs/pt/accounts/accounts-settings)
3. [Lançamento de diário](/docs/pt/accounts/journal-entry)
4. [Lançamento contábil entre empresas](/docs/pt/accounts/inter-company-journal-entry)
5. [Relatórios contábeis](/docs/pt/accounts/accounting-reports)
6. [Contabilidade multimoeda](/docs/pt/accounts/multi-currency-accounting)



