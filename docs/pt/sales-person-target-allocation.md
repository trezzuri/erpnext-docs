# Alocação alvo do vendedor



**É a atribuição de Vendedores a um item ou território.**


Juntamente com o gerenciamento de Vendedores, o ERPNext também permite que você atribua Vendedores alvo com base no Grupo de Itens e Território. Com base na meta alocada e nas vendas reais reservadas pelo vendedor, você receberá o Relatório de variação desejada para o vendedor.


## 1. Vendedor-Alocação de Meta


### 1.1 Mestre do vendedor aberto


Para alocar o destino, você precisa abrir um cadastro de vendedor específico.


**Vendas > Parceiros de vendas e território > Vendedor > Editar**


### 1.2 Alocar destino


No cadastro do Vendedor, você encontrará uma tabela chamada Metas do Vendedor.


![Vendedor alvo](/files/Screenshot 2021-09-09 às 2h22.30.png)


Nesta tabela, você deve selecionar Grupo de Itens, Ano Fiscal, Território, Quantidade Alvo, Valor Alvo e Distribuição Alvo.


Você pode fornecer uma meta em valor ou quantidade, ou ambos. Grupo de Itens ou Território também pode ser deixado em branco. Nesse caso, o sistema calculará a meta com base em Todos os Grupos de Itens ou Todos os Territórios, respectivamente.


**Distribuição alvo**


Você pode distribuir a meta por meses. Para isso crie uma nova distribuição mensal, você pode ver a opção ao clicar no campo Target Distribution na tabela Targets. Por exemplo, uma meta de venda de 1.000 unidades para o primeiro trimestre do ano fiscal de 2019-2020, conforme mostrado na captura de tela anterior.


![Target Distribution](/files/sales-person-target-distribution.png)


### 1.3 Relatório-Variação desejada do vendedor


Para verificar este relatório, acesse:


**Vendas > Outros relatórios > Variação desejada do vendedor**


Este relatório fornecerá a variação entre o desempenho alvo e real do vendedor. Este relatório é baseado no relatório de pedidos de vendas.


Aqui, de acordo com o relatório, a meta alocada ao vendedor era de aproximadamente 83 em quantidade por um mês, mas ele atingiu a meta de 80 quando o relatório está sendo visualizado, portanto, o relatório de variação é mostrado de acordo.

 >
![Grupo de itens de destino](/files/sales_person_target_variance_report.png)


**Observação:** para que o relatório reflita os detalhes corretos, você precisa vincular um Vendedor a um Pedido de Vendas. Ele está presente na seção Equipe de Vendas do Pedido de Vendas. O Pedido de Venda também deve estar em fase de envio.



## 2. Vendedor-Alocação de meta por território


Para alocar metas por território ao vendedor, selecione o vendedor específico no cadastro de território. Este Vendedor é inserido apenas para referência. Os detalhes do vendedor não são atualizados no relatório de variação da alocação de metas por território.


### 2.1 Ir para o território mestre


**Vendas > Configurações > Território > (Editar território específico)**


No Território selecionado, você encontrará um campo para selecionar Territory Manager. Este campo está vinculado ao cadastro "Vendedor".


![Gerente de território de vendedor](/files/sales-person-territory-manager.png)


### 2.2 Alocando alvo


A alocação de meta no cadastro de Território é semelhante à do cadastro de Vendedores. Você pode seguir as mesmas etapas fornecidas na seção *1.2 Alocar item de destino em grupo* para especificar o destino também no mestre de território.


### 2.3 Relatório-Item de variação de destino do território em grupo


Este relatório fornecerá a variação entre o desempenho real e desejado das vendas em um determinado território. Este relatório é baseado no relatório de Pedidos de Vendas. Embora o Vendedor esteja definido no cadastro de Território, seus detalhes não são extraídos do relatório.


**Observe** que o Território do Cliente/Clientes deve ser definido adequadamente para que este relatório funcione. Por exemplo, na captura de tela a seguir, a meta era de aproximadamente oito unidades e cinco foram alcançadas, portanto a variação é três.


![Relatório de território do vendedor](/files/sales-person-territory-report.png)



## 3. Distribuição alvo


Para criar uma nova Distribuição Mensal, acesse:
**Contabilidade > Distribuição Mensal**


O documento Distribuição de metas permite dividir as metas alocadas em vários meses. Se seus produtos e serviços forem sazonais, você poderá distribuir a meta de vendas de acordo. Por exemplo, se você estiver no ramo de guarda-chuvas, a meta alocada na estação das monções será maior do que nos outros meses.


![Target Distribution](/files/target-distribution.png)


Você pode vincular a Distribuição Mensal enquanto aloca metas no Vendedor e no Território mestre.


### 4. Tópicos Relacionados


1. [Vendedores nas transações de vendas](/docs/pt/selling/articles/sales-persons-in-the-sales-transactions)
2. [Usar vendedores em transações](/docs/pt/selling/articles/sales-persons-in-the-sales-transactions)



