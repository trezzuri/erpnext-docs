# Filtros de Dimensões Contábeis



> 
> Introduzido na versão 13
> 
> 
> 


No ERPNext, você pode controlar a marcação de várias dimensões contábeis em uma conta específica.
Você pode permitir ou restringir determinadas dimensões contábeis em uma conta usando os filtros de dimensão contábil


Para acessar a lista de filtros de dimensão contábil, acesse:



> 
> Página inicial > Contabilidade > Filtros de dimensão contábil
> 
> 
> 


## 1. Como criar um Filtro de Dimensão Contábil no ERPNext.


1. Vá para a lista Filtro de Dimensão Contábil e clique em Novo.
2. Selecione a Dimensão Contábil na qual a restrição deve ser aplicada.
3. Selecione "Permitir" ou "Restringir" no campo Permitir ou Restringir com base no tipo de restrição que deseja aplicar.
4. Adicione contas nas quais a restrição será aplicada na tabela Contas. Opcionalmente, você também pode marcar a caixa de seleção "É obrigatório" se a dimensão contábil precisar ser obrigatória para qualquer conta específica.
5. Adicione valores de dimensão na tabela Dimensões que serão permitidos ou restritos para as contas mencionadas.


![Criar filtro de dimensão contábil](/files/accounting-dimension-filter.png)


## 2. Recursos


### 2.1 Filtragem de dimensões contábeis em transações


Com base nas restrições aplicadas à conta, apenas as dimensões permitidas serão filtradas e mostradas nas transações.


![Dimensão contábil com filtros](/files/accounting-dimension-with-filters.png)


### 2.2 Validações para dimensões inválidas e obrigatórias


Caso alguma dimensão obrigatória esteja faltando ou uma dimensão restrita seja marcada em qualquer conta aplicável, o sistema não permitirá o envio dessa transação até que a dimensão contábil correta seja selecionada.


![Invalid Dimension](/files/invalid-dimension.png)


![Dimensão obrigatória](/files/mandatory-dimension.png)


### Tópicos relacionados


1. [Centro de custo](/docs/pt/accounts/cost-center)
2. [Orçamento](/docs/pt/accounts/budgeting)
3. [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions)
