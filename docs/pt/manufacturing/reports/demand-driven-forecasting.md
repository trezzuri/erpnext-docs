# Previsão baseada na demanda



Para acessar o Relatório de Previsão, acesse:


> Home > Fabricação > Relatórios > Previsão


![Previsão de produção](/files/production-forecasting-using-sales-order.png)


Usando o método de suavização exponencial e dados anteriores de pedidos de vendas/notas de entrega/cotações, a previsão será calculada. A fórmula do método de suavização exponencial é a seguinte:


![Previsão de produção](/files/exponential-smoothing-formula.png)


Usando o método de suavização exponencial, o sistema prevê a previsão para cada período e os mesmos dados de previsão serão usados ​​para prever os dados do próximo período.


## Como funciona o método de suavização exponencial


![Previsão de produção](/files/exponential-smoothing-formula-explain.png)


No exemplo acima, usamos dados de pedidos de vendas de um ano todos os meses. A previsão do primeiro mês será calculada com base na média do total de pedidos. A partir do segundo mês, a diferença entre o valor total do pedido e o valor previsto do último mês será multiplicada pelo valor da constante de suavização (entre 0 e 1). O valor padrão da constante de suavização é 0,3, o que fornece dados de previsão eficientes. A diferença do valor total do pedido e do valor da previsão do último mês é chamada de erro de previsão e esse erro será adicionado no mesmo mês do valor da previsão para calcular a previsão do próximo mês.


## Como funcionam os filtros


1. **Empresa**:-o usuário pode fazer previsões para a empresa específica aplicando o filtro de empresa
2. **Data Inicial e Data Final**:-para este período o sistema fará a previsão, a data inicial padrão é a data atual e a data final será a data um ano à frente da data atual.
3. **Baseado no documento**:-por padrão, o sistema usa dados anteriores de pedidos de vendas para fazer previsões. O usuário pode selecionar outro documento, como nota de entrega/cotação, para prever os dados.
4. **Baseado em**:-com base na quantidade/quantidade, o sistema mostra os dados de previsão.
5. **Com base em dados (em anos)**:-para a previsão requer dados anteriores, este filtro ajuda o sistema a verificar os dados anteriores por número de anos.
6. **Periodicidade**:-os dados de previsão podem ser visualizados mensalmente/trimestralmente/semestralmente/anualmente, os dados de previsão antigos não podem ser exibidos no período mensal para melhor visualização.
7. **Constante de Suavização**-a Constante de Suavização será usada para prever os dados, o valor deve estar entre 0 e 1.



