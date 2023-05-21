# Plano de contas


**O plano de contas é o modelo das contas da sua organização.**


A estrutura geral do seu Plano de Contas é baseada em um sistema de partidas dobradas
contabilidade que se tornou um padrão em todo o mundo para quantificar como um
empresa está financeiramente.


Plano de contas é uma exibição em árvore dos nomes das contas (razões e
Grupos) que uma Empresa requer para administrar seus livros contábeis. Conjuntos ERPNext
um plano de contas simples para cada empresa que você criar, mas você pode
modifique-o de acordo com suas necessidades e exigências legais.


Para cada empresa, Plano de Contas significa a forma de classificação dos lançamentos contábeis, principalmente
com base em requisitos estatutários (impostos, conformidade com regulamentos governamentais).


![CoA Tree](/files/chart-of-accounts-tree.png)


O Plano de Contas ajuda você a responder perguntas como:


* Quanto vale a sua organização?
* Quanta dívida você tomou?
* Quanto lucro você está obtendo (e, portanto, pagando impostos)?
* Quanto você está vendendo?
* Qual é a sua divisão de despesas?


Como alguém que gerencia um negócio, é muito valioso ver o quão bem
seu negócio está fazendo.



>
> **Dica**: Se você não sabe ler um Balanço é uma boa oportunidade para começar a aprender sobre isso. Valerá a pena o esforço. Você também pode contar com a ajuda de seu contador para configurar seu plano de contas.
>
>
>


Para acessar a lista Plano de Contas, acesse:



>
> Home > Contabilidade > Mestres em Contabilidade > Plano de Contas
>
>
>


## 1. Como criar/editar contas


O ERPNext vem com um Plano de Contas padrão. Em vez de criar/modificar, você também pode usar a ferramenta [Importador de plano de contas](/docs/v13/user/manual/en/setting-up/importador de gráfico de contas). Observe que o plano de contas existente será substituído quando esta ferramenta for usada.


1. Vá para a lista Plano de contas.


Aqui você pode abrir contas de grupo que contêm outras contas. Existem opções para “Adicionar filho” em uma conta, Editar ou Excluir a conta.


![Plano de contas](/files/plano de contas-add.gif)
2. A opção de criar uma conta infantil só aparecerá se você clicar em um tipo de grupo (pasta)
Conta.
3. Insira um nome para a conta.
4. Insira um número para a conta.
5. Marque 'Is Group' se você deseja que esta seja uma conta de grupo que pode conter outras contas.
6. Selecione o tipo de conta. Selecionar isso é importante, pois alguns campos permitem selecionar apenas tipos específicos de contas.
7. Altere a moeda se esta conta for usada para transações com moeda diferente. Por padrão, é a moeda da empresa. Para saber mais, visite a página [Contabilidade em várias moedas](/docs/v13/user/manual/en/accounts/contabilidade em várias moedas).
8. Clique em **Criar novo**.


Normalmente, você pode querer criar contas para:


* Viagens, salários, telefone, etc. em **Despesas**.
* Imposto sobre Valor Agregado (IVA), Imposto sobre Vendas, Capital, etc. em **Passivo Circulante**.
* Vendas de produtos, vendas de serviços, etc. em **Receita**.
* Edificações, máquinas, móveis, etc. no **Ativo Imobilizado**.


![Plano de contas](/files/coa-root-accounts.png)



>
> Dica: contas com moedas diferentes são criadas quando você recebe ou faz pagamentos de ou para moedas diferentes. Por exemplo, se você mora na Índia e faz transações com os EUA, pode ser necessário criar contas como 'Debtors US', 'Creditors US', etc.
>
>
>


Vamos entender os principais grupos do Plano de Contas.


## 2. Tipos de conta


Os tipos de contas são classificados principalmente como receita, despesa, ativo ou passivo.


### 2.1 Contas do Balanço


As contas do Balanço são 'Aplicação de Fundos (Ativos)' e 'Fontes de Fundos
(Passivos)' que significa o patrimônio líquido de sua empresa em um determinado momento.
Quando você começa ou termina um período financeiro, todos os Ativos são iguais ao
Passivos.



>
> **Uma observação sobre contabilidade**: se você é novo em contabilidade, deve estar se perguntando como pode
> Os ativos são iguais aos passivos? Isso significaria que a empresa não tem nada de seu
> próprio. Está correto! Todos os “investimentos” feitos na empresa para comprar ativos (como
> terrenos, móveis, máquinas) é feita pelos proprietários. Os proprietários são uma responsabilidade para com o
> empresa uma vez que os lucros pertencem aos proprietários.
>
>
>



>
> Se uma empresa fechasse, precisaria vender todos os
> ativos e pagar todos os passivos (incluindo lucros) aos proprietários,
> deixando-se sem nada.
>
>
>


Todas as contas nas contas do Balanço representam um ativo de propriedade da empresa como "Banco
Conta", "Terrenos e Propriedades", "Móveis" ou um passivo (fundos que o
empresa deve a terceiros) como "Fundos dos proprietários", "Dívida" etc.


Duas contas especiais a serem observadas aqui são Contas a Receber (dinheiro que você precisa
cobrar de seus Clientes) e Contas a Pagar (dinheiro que você tem que pagar para
seus Fornecedores) em Ativos e Passivos, respectivamente.


### 2.2 Contas de Lucros e Perdas


Lucros e Perdas é o grupo de contas 'Receitas' e 'Despesas' que representam
suas transações contábeis durante um período.


Ao contrário das contas do Balanço, as contas de Lucros e Perdas (ou contas PL) não
não representam patrimônio líquido (ativos), mas representam a quantidade de dinheiro
gastos e arrecadados no atendimento aos clientes durante o período. Assim, ao
início e no final do ano fiscal, eles se tornam zero.


No ERPNext é fácil acompanhar Lucros e Perdas através do gráfico de Lucros e Perdas.


![Relatório de lucros e perdas](/files/profit-and-loss-report.png)


Observe que, no primeiro dia do ano, você não teve nenhum lucro ou prejuízo, mas você
ainda têm ativos, portanto, as contas do balanço nunca se tornam zero no
início ou fim de um período.


### 2.3 Grupos e Ledgers


Existem dois tipos principais de Contas no ERPNext - Grupo e Razão. Grupos podem
têm subgrupos e ledgers dentro deles, enquanto os ledgers são os nós folha de
seu gráfico e não pode conter mais contas neles.


As transações contábeis só podem ser feitas em contas contábeis (não em grupos)



>
> Informação: O termo "Ledger" significa uma página em um livro de contabilidade onde as entradas são
> feito. Geralmente, há um livro-razão para cada conta (como um cliente ou um
> Fornecedor).
>
>
>



>
> Nota: Uma conta “Ledger” também é às vezes chamada de Account “Head”.
>
>
>


![Grupos e Ledgers em CoA](/files/coa-group-and-ledger.png)


### 2.4 Outros tipos de conta


No ERPNext, você também pode especificar mais informações ao criar um novo
Conta, existe para ajudá-lo a selecionar essa conta específica em um cenário como 'Conta bancária' ou 'Conta fiscal' e não tem efeito no Gráfico
em si.


Explicação dos tipos de conta:


* **Depreciação Acumulada**: Para armazenar as informações de depreciação acumulada total dos Ativos da Empresa. A depreciação acumulada aparece no balanço.
* **Ativo Recebido Mas Não Faturado**: Conta do passivo temporário que contém o valor do Ativo recebido mas ainda não faturado.
* **Banco**: O tipo de conta sob a qual as contas bancárias serão criadas. Deve haver pelo menos uma conta de grupo do tipo "Banco" no CoA.
* **Caixa**: O tipo de conta sob a qual a conta caixa será criada. Deve haver pelo menos uma conta de grupo do tipo "Cash" no CoA.
* **Cobrável**: Cobranças adicionais aplicadas aos Itens podem ser armazenadas em contas desse tipo. Por exemplo, "Frete and Forwarding Charges".
* **Trabalho de Capital em Andamento**: As cobranças atuais ao criar Ativos Fixos são armazenadas em contas CWIP. Por exemplo, custos de construção ao construir um edifício. No ERPNext, os ativos são contabilizados em contas CWIP quando ainda não estão sendo usados.
* **Custo dos Produtos Vendidos**: Uma conta deste tipo é utilizada para contabilizar o total acumulado de todos os custos incorridos na fabricação/compra de um produto ou serviço, vendido por uma Empresa.
* **Depreciação**: A conta de despesas para registrar a depreciação dos ativos fixos. Isso aparece na demonstração de resultados.
* **Equity**: Este tipo de conta representa transações com pessoas que são donas do negócio, ou seja, os acionistas/proprietários.
* **Despesas Incluídas na Avaliação de Ativos**: A conta para contabilizar as despesas (além dos custos de material direto dos Ativos) incluídas no custo de importação de um Ativo.
* **Despesas Incluídas na Avaliação**: A conta para registrar as despesas (além dos custos diretos de material) incluídas no custo de importação de um item/produto, usado no Inventário Perpétuo.
* **Ativo Fixo**: A conta para manter os custos dos ativos fixos.
* **Conta de Receita**: Este tipo de conta representa qualquer fonte de receita ou receita contabilizada para a Empresa.
* **Pagável**: O tipo de conta representa o valor devido por uma empresa aos seus credores (Fornecedores).
* **Recebíveis**: O tipo de conta representa o valor devido a uma empresa por seus devedores (Clientes).
* **Arredondamento**: Em muitas Faturas pode haver algum [arredondamento](/docs/v13/user/manual/pt/contas/artigos/arredondamento-validação-de-conta) no valor final. Para um acompanhamento preciso, esses valores podem ser contabilizados em contas desse tipo.
* **Estoque**: O grupo de contas sob o qual [Contas de depósito](/docs/v13/user/manual/en/accounts/articles/round-off-account-validation) serão criadas.
* **Ajuste de estoque**: Uma conta de despesas para registrar qualquer entrada de ajuste de estoque/inventário. Geralmente vem no mesmo nível de Custo das Mercadorias Vendidas.
* **Estoque Recebido Mas Não Faturado**: Uma conta de passivo temporário que contém o valor do estoque recebido mas ainda não faturado e usado no Estoque Permanente.
* **Imposto**: todas as contas de impostos, como IVA, TDS, GST, etc., estão incluídas neste tipo.
* **Temporária**: Uma conta temporária é útil para equilibrar receitas, despesas e anulá-las ao mudar para o ERPNext no meio do ano com lançamentos contábeis pendentes.



>
> **Observação**: Ao fazer entradas de pagamento, a conta bancária padrão será buscada na seguinte ordem, se definida:
>
>
>



>
>
> ```
> * Formulário da empresa
> * Modo de pagamento conta padrão
> * Conta bancária padrão do cliente/fornecedor
> * Selecione manualmente em Entrada de pagamento
>
> ```
>
>


### 2.5 Demonstrações Financeiras


As demonstrações financeiras de sua empresa são facilmente visualizadas no ERPNext. Você pode visualizar as demonstrações financeiras
como Balanço Patrimonial, Demonstrativo de Lucros e Perdas e Demonstrativo de Fluxo de Caixa.


Um exemplo de várias demonstrações financeiras é dado abaixo:


1. Relatório de fluxo de caixa:


![Fluxo de caixa](/files/cash-flow.png)
2. Relatório de Lucros e Perdas:
![Relatório de lucros e perdas](/files/profit-and-loss-report.png)
3. Relatório do Balanço:


![Balanço](/files/balance-sheet.png)


### 2.6 Número da conta


Um plano de contas padrão é organizado de acordo com um sistema numérico. Cada categoria principal começará com um determinado número e, em seguida, as subcategorias dentro dessa categoria principal começarão com o mesmo número. Por exemplo, se os ativos forem classificados por números começando com o dígito 1.000, as contas em dinheiro podem ser rotuladas como 1.100, as contas bancárias podem ser rotuladas como 1.200, as contas a receber podem ser rotuladas como 1.300 e assim por diante. Uma lacuna entre os números de conta geralmente é mantida para adicionar contas no futuro.


Você pode atribuir um número ao criar uma conta na página Plano de contas. Você também pode editar um número do registro da conta, clicando no botão **Atualizar nome/número da conta**. Ao atualizar o número da conta, o sistema renomeia o nome da conta automaticamente para incorporar o número ao nome da conta.


![Número da conta](/files/update-account-number.png)


## 3. Vídeo








### 4. Tópicos Relacionados


1. [Saldo inicial](/docs/v13/user/manual/en/accounts/saldo inicial)
2. [Configurações de contas](/docs/v13/user/manual/en/accounts/accounts-settings)
3. [Entrada de diário](/docs/v13/user/manual/en/accounts/journal-entry)
4. [Entrada no diário da empresa](/docs/v13/user/manual/en/accounts/entrada do diário na empresa)
5. [Relatórios de contabilidade](/docs/v13/user/manual/en/accounts/accounting-reports)
6. [Contabilidade em várias moedas](/docs/v13/user/manual/en/accounts/contabilidade em várias moedas)