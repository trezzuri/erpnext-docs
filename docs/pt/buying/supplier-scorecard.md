# Cartão de pontuação do fornecedor



**Um Scorecard de Fornecedores é uma ferramenta de avaliação usada para avaliar o desempenho dos fornecedores.**


Os scorecards de fornecedores podem ser usados ​​para monitorar a qualidade dos itens, a entrega e a capacidade de resposta dos fornecedores durante longos períodos de tempo. Esses dados normalmente são usados ​​para ajudar nas decisões de compra.
Um Scorecard do Fornecedor é criado manualmente para cada fornecedor.


Para acessar o Scorecard do Fornecedor, acesse:
> Home > Compras > Scorecard do Fornecedor > Scorecard do Fornecedor


## 1. Pré-requisitos


Antes de criar e usar um Scorecard do Fornecedor, é aconselhável criar primeiro o seguinte:


* [Fornecedor](/docs/pt/buying/supplier)


## 1. Como criar Scorecard do Fornecedor


1. Vá para a lista Scorecard do fornecedor e clique em Novo.
2. Selecione um fornecedor para pontuar.
3. Selecione o período de avaliação: semanal, mensal ou anual.
4. Configure a função de pontuação (detalhes na próxima seção).
5. Um scorecard de fornecedor é criado para cada fornecedor individualmente. Apenas um scorecard de fornecedor pode ser criado para cada fornecedor.
![Ordem de compra](/files/supplier-scorecard.png)


## 2. Recursos


### 2.1 Configuração de pontuação


O scorecard do fornecedor consiste em um conjunto de períodos de avaliação, durante os quais o desempenho de um fornecedor é avaliado. Este período pode ser semanal, mensal ou anual. A pontuação atual é calculada a partir da pontuação de cada período de avaliação com base na função de ponderação. A fórmula padrão é ponderada linearmente nos 12 períodos de pontuação anteriores.
![Ordem de compra](/files/supplier-scorecard-weighing.png)
Esta fórmula é personalizável.


#### Classificação dos fornecedores


A classificação do fornecedor é usada para classificar rapidamente os fornecedores com base em seu desempenho. Eles são personalizáveis ​​para cada fornecedor.


A classificação do scorecard de um fornecedor também pode ser usada para impedir que os fornecedores sejam incluídos na Solicitação de Cotações ou na emissão de Pedidos de Compra. A tela a seguir pode ser vista ao expandir uma linha na tabela 'Classificação de pontuação', clicando na seta voltada para baixo.
![Ordem de compra](/files/supplier-scorecard-standing.png)


### 2.2 Configuração de critérios


Um fornecedor pode ser avaliado com base em vários critérios de avaliação individuais, incluindo (mas não se limitando a) tempo de resposta da cotação, qualidade do item entregue e pontualidade da entrega. Esses critérios são ponderados para determinar a pontuação final do período.


Para criar um novo Critério, acesse Compras > Scorecard de Fornecedores > Critérios de Scorecard de Fornecedores:
![Ordem de compra](/files/supplier-scorecard-criteria.png)


Observação: os pesos dos critérios para um scorecard devem somar 100.


### 2.3 Variáveis ​​do scorecard do fornecedor


A forma de cálculo de cada critério é determinada através do campo Fórmula de Critérios, que pode utilizar uma série de variáveis ​​pré-estabelecidas. Isso pode ser visto na captura de tela anterior.


O valor de cada uma dessas variáveis ​​é calculado durante o período de pontuação de cada fornecedor. Exemplos dessas variáveis ​​incluem:


* O número total de itens recebidos do fornecedor
* O número total de itens aceitos do fornecedor
* O número total de itens rejeitados do fornecedor
* O número total de entregas do fornecedor
* O valor total (em dólares) recebido de um fornecedor


![Variável do scorecard do fornecedor](/files/supplier-scorecard-variables.png)


As variáveis ​​são predefinidas e variáveis ​​adicionais podem ser adicionadas por meio de personalizações no servidor. Marque a caixa de seleção Personalizada se a variável que você está criando for para um campo personalizado.


A fórmula dos critérios deve ser customizada para avaliar os fornecedores em cada critério da forma que melhor atenda aos requisitos da empresa.


### 2.4 Fórmulas de avaliação


A fórmula de avaliação utiliza variáveis ​​pré-estabelecidas ou personalizadas para avaliar um aspecto do desempenho do fornecedor durante o período de pontuação. As fórmulas podem usar as seguintes funções matemáticas:


* adição: +
* subtração:-
* multiplicação: \*
* divisão:/
* min: min(x,y)
* máx: máx(x,y)
* se/else: (x) if (fórmula) else (y)
* menos que: <
* maior que:
* variáveis: {variable\_name}


É crucial que a fórmula seja solucionável para todos os valores de variáveis. Na maioria das vezes, isso é um problema se o valor for 0. Por exemplo:


`{total_accepted_items}/{total_received_items}`
Este exemplo resolveria para 0/0 em períodos onde não há itens recebidos e, portanto, deveria ter um cheque para proteger neste caso:


`({total_accepted_items}/{total_received_items})
se {total_received_items} > 0
mais 1.`
### 2.5 Avaliando o fornecedor


Uma avaliação é gerada para cada Período do Scorecard do Fornecedor clicando no botão "Gerar Períodos Faltantes do Scorecard". Pode ser visualizada a pontuação atual do fornecedor, bem como um gráfico visual que mostra o desempenho do fornecedor ao longo do tempo. Quaisquer ações contra o fornecedor também são anotadas aqui, incluindo avisos ao criar solicitações de cotação e pedidos de compra ou impedir completamente esses recursos para esse fornecedor.


### 3. Tópicos Relacionados


1. [Fornecedor](/docs/pt/buying/supplier)
2. [Cotação do fornecedor](/docs/pt/buying/supplier-quotation)



