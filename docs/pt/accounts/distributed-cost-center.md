# Centro de Custo Distribuído


**Um Centro de Custo Distribuído é um Centro de Custo no qual vários Centros de Custo são marcados com uma porcentagem apropriada.**


Se uma empresa possui um Centro de Custo mestre com Centros de Custo dependentes. Em cada transação do centro de custo mestre, é difícil atualizar o orçamento, lucro e perda para cada centro de custo dependente manualmente com a porcentagem alocada do centro de custo mestre. Esse recurso ajuda a automatizar o processo de entrada manual.


Por exemplo, na sua empresa, se os Centros de Custo 'B' e 'C' dependem do Centro de Custo 'A' em 20% e 80%. Então, você pode mencionar 'A' como Centro de Custo Distribuído. Ajuda a refletir receitas, despesas e orçamento de 'A' em 'B' e 'C' com porcentagens alocadas.


No ERPNext você pode criar Centros de Custos Distribuídos e utilizá-los em transações e relatórios.


## 1. Como criar um Centro de Custo Distribuído


1. Vá para a lista Centro de custo, clique em Novo.
2. Digite o nome do Centro de Custo.
3. Selecione o Centro de Custo pai.
4. Marque a caixa de seleção **Ativar Centro de Custo Distribuído**: Ao habilitar isso, a tabela de Centro de Custo Distribuído será exibida. Aqui, selecione os Centros de Custo e aloque a porcentagem correspondente.
5. Quando terminar, clique em Salvar.


![Centro de custo distribuído](/files/distributed-cost-centers.png)


Os seguintes relatórios serão atualizados automaticamente quando o filtro Centro de custo for adicionado:


* [Relatórios de contabilidade](/docs/v13/user/manual/en/accounts/accounting-reports)
+ Demonstrações Financeiras
+ Variação de orçamento
+ Razão Geral
* [Análise de lucratividade](/docs/v13/user/manual/en/accounts/articles/tracking-project-profitability-using-cost-center)


### 2. Tópicos Relacionados


1. [Centro de custo](/docs/v13/user/manual/en/accounts/cost-center)