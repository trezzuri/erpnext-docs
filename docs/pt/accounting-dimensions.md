# Dimensões contábeis




> 
> Introduzido na versão 12
> 
> 
> 


Contabilidade dimensional significa marcar cada transação com dimensões apropriadas, como filial, unidade de negócios, etc. Isso permite que você mantenha cada segmento separadamente, limitando assim a manutenção geral nas contas contábeis e seu plano de contas permanece puro.


Centro de Custo e Projeto são tratados como dimensões por padrão no ERPNext. Ao definir um campo na Dimensão Contábil, esse campo será adicionado nos relatórios de transações quando aplicável.


No ERPNext você pode criar dimensões contábeis configuráveis ​​e utilizá-las em transações e relatórios.


Para acessar a lista de Dimensões Contábeis, acesse:



> 
> Página inicial > Contabilidade > Configurações > Dimensões contábeis
> 
> 
> 


## 1. Como criar uma dimensão contábil no ERPNext.


1. Vá para a lista Dimensão Contábil e clique em Novo.
2. Selecione o Documento de Referência que deseja usar como dimensão personalizada. Por exemplo, se você selecionar Departamento como Documento de Referência, a dimensão será baseada no Departamento.
3. Insira o nome da dimensão (este nome aparecerá nas transações para as quais as dimensões são criadas).
4. Dentro da tabela Padrões de dimensão você pode mencionar dimensões padrão específicas da empresa, conforme mostrado na captura de tela abaixo. Essa dimensão será buscada automaticamente na transação dessa empresa específica.
5. Marque a caixa de seleção "Obrigatório" se desejar que a dimensão seja obrigatória nas transações.


![Criando dimensão contábil](/files/accounting-dimension.png)


## 2. Recursos


À medida que você cria a dimensão, os campos personalizados serão criados usando um trabalho em segundo plano para essa dimensão específica. Você pode vê-los na seção Dimensões Contábeis dentro das transações que têm impacto nos lançamentos contábeis (Entrada Contábil).


### 2.1 Usando dimensões em transações


Para marcar uma transação com uma dimensão, você pode selecionar a dimensão específica na seção Dimensões contábeis, conforme mostrado na captura de tela abaixo.


![Dimensão contábil na fatura de vendas](/files/accounting-dimension-in-invoice.png)


### 2.2 Filtrando relatórios com base em dimensões


Você também pode filtrar vários relatórios financeiros, como Demonstração de Lucros e Perdas, Balanço Patrimonial e Razão Geral, com base nessas dimensões.


![Dimensão contábil em relatórios](/files/report-dimensions.png)


### 2.3 Tornando as dimensões contábeis obrigatórias para contas "Lucros e Perdas" e "Balanço"


Lucros e perdas são o grupo de contas de receitas e despesas que representam suas transações contábeis durante um período.


As contas do Balanço Patrimonial são Aplicação de Fundos (Ativos) e Fontes de Fundos (Passivos) que significam o patrimônio líquido da sua empresa em um determinado momento.


Ao marcar as caixas de seleção 'Obrigatório para conta de lucros e perdas' ou 'Obrigatório para balanço patrimonial', você pode configurar suas dimensões para serem obrigatórias para 'Lucros e perdas' e 'Contas de balanço patrimonial'.


![Dimensão contábil obrigatória em transações](/files/dimension-mandatory.png)


### 2.4 Desativar dimensões contábeis quando não forem mais necessárias


Você também pode desativar as dimensões se não precisar mais delas. As transações antigas com dimensões contábeis permanecerão intactas.


![Desativar dimensão contábil](/files/dimension-disable.png)


### Tópicos Relacionados


1. [Centro de custos](/docs/pt/accounts/cost-center)
2. [Orçamento](/docs/pt/accounts/budgeting)
3. [Relatórios contábeis](/docs/pt/accounts/accounting-reports)



