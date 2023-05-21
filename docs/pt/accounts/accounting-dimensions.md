# Dimensões Contábeis



>
> Introduzido na versão 12
>
>
>


Contabilidade dimensional significa marcar cada transação com dimensões apropriadas, como Filial, Unidade de Negócios, etc. Isso permite que você mantenha cada segmento separadamente, limitando assim a manutenção geral nas contas contábeis e seu Plano de Contas permanece puro.


Centro de Custo e Projeto são tratados como dimensões por padrão no ERPNext. Ao definir um campo na Dimensão Contábil, esse campo será adicionado nos relatórios de transações quando aplicável.


No ERPNext você pode criar dimensões contábeis configuráveis ​​e utilizá-las em transações e relatórios.


Para acessar a lista Dimensão Contábil, acesse:



>
> Início > Contabilidade > Configurações > Dimensões de contabilidade
>
>
>


## 1. Como criar Dimensão Contábil no ERPNext.


1. Acesse a lista Dimensão Contábil e clique em Novo.
2. Selecione o documento de referência que deseja usar como uma dimensão personalizada. Por exemplo, se você selecionar Departamento como Documento de Referência, a dimensão será baseada no Departamento.
3. Insira o nome da dimensão (esse nome aparecerá nas transações para as quais as dimensões são criadas).
4. Dentro da tabela de Padrões de Dimensão, você pode mencionar as dimensões padrão específicas da empresa, conforme mostrado na captura de tela abaixo. Essa dimensão será buscada automaticamente na transação contra essa empresa específica.
5. Marque a caixa de seleção "Obrigatório" se desejar que a dimensão seja obrigatória nas transações.


![Criando Dimensão Contábil](/files/accounting-dimension.png)


## 2. Características


À medida que você cria a dimensão, os campos personalizados serão criados usando um trabalho em segundo plano para essa dimensão específica. Você pode vê-los na seção Dimensões contábeis dentro das transações que afetam os lançamentos contábeis (entrada contábil).


### 2.1 Usando dimensões em transações


Para marcar uma transação com uma dimensão, você pode selecionar a dimensão específica na seção Dimensões contábeis, conforme mostrado na captura de tela abaixo.


![Dimensão contábil na fatura de venda](/files/accounting-dimension-in-invoice.png)


### 2.2 Filtrando relatórios com base em dimensões


Você também pode filtrar vários relatórios financeiros, como Demonstração de Lucros e Perdas, Balanço, Razão Geral com base nessas dimensões.


![Dimensão contábil em relatórios](/files/report-dimensions.png)


### 2.3 Tornar as dimensões contábeis obrigatórias para as Contas de "Resultados e Perdas" e "Balanço"


Lucros e Perdas é o grupo de contas de Receitas e Despesas que representam suas transações contábeis durante um período.


As contas do Balanço são aplicações de fundos (ativos) e fontes de recursos (passivos) que representam o patrimônio líquido de sua empresa a qualquer momento.


Ao selecionar as caixas de seleção 'Obrigatório para Conta de Lucros e Perdas' ou 'Obrigatório para Balanço', você pode configurar suas dimensões para serem obrigatórias para 'Resultados e Perdas' e 'Contas de Balanço'.


![Dimensão contábil obrigatória na transação](/files/dimension-mandatory.png)


### 2.4 Desabilitar as dimensões contábeis quando não forem mais necessárias


Você também pode desativar as dimensões se não precisar mais delas. As antigas transações com dimensões contábeis permanecerão intactas.


![Desativar dimensão contábil](/files/dimension-disable.png)


### Tópicos relacionados


1. [Centro de custo](/docs/v13/user/manual/en/accounts/cost-center)
2. [Orçamento](/docs/v13/user/manual/en/accounts/orçamento)
3. [Relatórios de contabilidade](/docs/v13/user/manual/en/accounts/accounting-reports)