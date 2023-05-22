# Dimensões Contábeis



> 
> Introduzido na versão 12
> 
> 
> 


Contabilidade dimensional significa marcar cada transação com dimensões apropriadas, como Filial, Unidade de Negócios, etc. Isso permite que você mantenha cada segmento separadamente, limitando assim a manutenção geral das contas contábeis e seu Plano de Contas permanece puro.


Centro de Custo e Projeto são tratados como dimensões por padrão no ERPNext. Ao definir um campo na Dimensão Contábil, esse campo será adicionado nos relatórios de transações quando aplicável.


No ERPNext você pode criar dimensões contábeis configuráveis ​​e utilizá-las em transações e relatórios.


Para acessar a lista Dimensão Contábil, acesse:



> 
> Página inicial > Contabilidade > Configurações > Dimensões contábeis
> 
> 
> 


## 1. Como criar Dimensão Contábil no ERPNext.


1. Vá para a lista Dimensão Contábil e clique em Novo.
2. Selecione o documento de referência que você deseja usar como uma dimensão personalizada. Por exemplo, se você selecionar Departamento como Documento de Referência, a dimensão será baseada no Departamento.
3. Digite o nome da dimensão (esse nome aparecerá nas transações para as quais as dimensões são criadas).
4. Na tabela de Padrões de Dimensão, você pode mencionar as dimensões padrão específicas da empresa, conforme mostrado na captura de tela abaixo. Essa dimensão será buscada automaticamente na transação dessa empresa específica.
5. Marque a caixa de seleção "Obrigatório" se desejar que a dimensão seja obrigatória nas transações.


![Criando dimensão contábil](/files/accounting-dimension.png)


## 2. Recursos


Conforme você cria a dimensão, os campos personalizados serão criados usando um trabalho em segundo plano para essa dimensão específica. Você pode vê-los na seção Dimensões contábeis dentro das transações que afetam os lançamentos contábeis (entrada contábil).


### 2.1 Uso de dimensões em transações


Para marcar uma transação com uma dimensão, você pode selecionar a dimensão específica na seção Dimensões contábeis, conforme mostrado na captura de tela abaixo.


![Dimensão contábil na fatura de vendas](/files/accounting-dimension-in-invoice.png)


### 2.2 Filtragem de relatórios com base em dimensões


Você também pode filtrar vários relatórios financeiros, como Demonstração de Lucros e Perdas, Balanço, Razão Geral com base nessas dimensões.


![Dimensão contábil em relatórios](/files/report-dimensions.png)


### 2.3 Tornar as dimensões contábeis obrigatórias para as contas "Lucros e perdas" e "Balanço"< /h3>
Lucros e perdas são o grupo de contas de receitas e despesas que representam suas transações contábeis durante um período.
As contas do Balanço são aplicações de fundos (ativos) e fontes de fundos (passivos) que representam o patrimônio líquido de sua empresa a qualquer momento.
Ao selecionar as caixas de seleção 'Obrigatório para Conta de Lucros e Perdas' ou 'Obrigatório para Balanço', você pode configurar suas dimensões para serem obrigatórias para 'Resultados e Perdas' e 'Contas de Balanço'.
Dimensão contábil obrigatória na transação
2.4 Desativar as dimensões contábeis quando não forem mais necessárias
Você também pode desativar as dimensões se não precisar mais delas. As transações antigas com dimensões contábeis permanecerão intactas.
Desativar dimensão contábil
Tópicos relacionados
1. [Centro de custo](/docs/pt/accounts/cost-center)
2. [Orçamento](/docs/pt/accounts/budgeting)
3. [Relatórios contábeis](/docs/pt/accounts/accounting-reports)

