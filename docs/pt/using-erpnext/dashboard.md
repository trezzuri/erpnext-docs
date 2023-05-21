# Painel



>
> Introduzido na versão 12
>
>
>


**O painel fornece uma visão rápida dos principais indicadores de desempenho relevantes para o processo de negócios.**


Cada Dashboard consiste em um ou mais de um Dashboard Charts, cada um dos quais configurado com uma fonte de dados conhecida como Dashboard Chart Source.


Para acessar o Painel, vá para,



>
> Home > Personalização > Painéis > Painel
>
>
>


## 1. Como criar um novo painel


1. Vá para Lista de Painéis e clique em Novo.
2. Insira o Nome do Módulo para o qual deseja ver o Painel.
3. Informe os Gráficos do Dashboard que deseja que sejam parametrizados para este Dashboard.
4. Salve.


Ao clicar em `Mostrar Dashboard`, você poderá ver o Dashboard dando a representação gráfica de suas transações.


![Painel de contabilidade](/files/dashboard.png)


## 2. Adicionando gráficos ao painel


Adicione gráficos a este painel selecionando `Dashboard Chart` existente ou criando novos.


![Adicionando painel aos gráficos](/files/dashboard-add-charts.png)


Salve as alterações e clique no botão `Mostrar painel` para ver o painel.


![Mostrar botão do painel](/files/dashboard-show-dashboard-button.png)


## 3. Criando um novo gráfico de painel


Para criar um novo Dashboard Chart, vá para



>
> Início > Personalizações > Painéis > Gráfico do painel > Novo
>
>
>


Forneça um nome para o gráfico, ele aparecerá no painel como o rótulo do gráfico, selecione o tipo de gráfico como `Personalizado` e selecione uma `Fonte do gráfico do painel` como fonte de dados para este gráfico.


**Observação:** A nova `fonte do gráfico do painel` só pode ser criada pelo usuário administrador no modo de desenvolvedor.


![Selecione a origem do gráfico do painel](/files/dashboard-chart-from-source.png)


Após definir o campo Chart Source, a tabela de filtros será mostrada.


Clique na tabela para editar os filtros.


![Filtro do gráfico do painel](/files/dashboard-chart-filter.png)


Um modal será mostrado para definir filtros. Clique em `Definir` para definir os filtros.
![Modal de filtro de gráfico de painel](/files/dashboard-chart-filter-modal.png)


Após definir o campo Origem do gráfico, a tabela Filtros será atualizada com os valores de filtro selecionados.
![Filtro do gráfico do painel](/files/dashboard-chart-filter-updated.png)


No exemplo acima, criamos um `Dashboard Chart` personalizado para o qual já tínhamos uma `Dashboard Chart Source`.


Você também pode criar gráficos básicos como Contagem/Soma/Média/Agrupar por ToDo com base na data de criação/modificação selecionando `Contagem/Soma/Média/Agrupar por` como `Tipo de gráfico`. Você também pode usar um relatório existente como fonte no campo `Nome do relatório` para criar um gráfico selecionando `Relatório` como `Tipo de gráfico`.


Para `Contagem`, você precisa selecionar o `Doctype` para o qual você precisa do gráfico no campo `Document Type` e no campo `Based On Date` em `Time Series Based On`.


![Gráfico do painel de contagem](/files/dashboard-chart-count.png)


**Observação:** Se você selecionar um doctype de tabela filho em `Document Type`, você também deve selecionar o doctype pai para essa tabela filho em `Parent Document Type` (este campo só ficará visível quando você selecionar o doctype da tabela filho em campo `Tipo de Documento`).


![Tipo de documento principal do gráfico do painel](/files/dashboard-chart-parent-document-type.png)


Para `Sum` e `Average`, você também deve selecionar o campo `Based On Value` em `Value Based On`.


![Gráfico de painel de soma](/files/dashboard-chart-sum.png)


Para `Agrupar por`, você pode selecionar `Agrupar por tipo` como Contagem/Soma/Média, `Agrupar por baseado em` como Criado por/Modificado por e `Número de grupos`.


![Grupo por gráfico do painel](/files/dashboard-chart-group-by.png)


## 4. Usando painéis


Cada gráfico será mostrado de acordo com os campos definidos no Gráfico do Painel correspondente. O resultado da origem do gráfico do painel é armazenado em cache para evitar consultas redundantes. Como os dados do gráfico podem estar desatualizados, cada gráfico também mostrará o último horário sincronizado.


![Painel sincronizado pela última vez](/files/dashboard-last-synced.png)


Os filtros usados ​​para gerar os dados do gráfico também podem ser alterados clicando em `Definir filtros`. O gráfico será atualizado automaticamente de acordo com os filtros definidos recentemente.


![Filtros do painel](/files/dashboard-filters.png)


Para obter os dados mais recentes, cada gráfico deve ser atualizado vigorosamente clicando no botão **Forçar atualização** no menu suspenso.