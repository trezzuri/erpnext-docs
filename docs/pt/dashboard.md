# Painel




> 
> Introduzido na versão 12
> 
> 
> 


**O painel fornece uma visão rápida dos principais indicadores de desempenho relevantes para o processo de negócios.**


Cada painel consiste em um ou mais gráficos de painel, cada um deles configurado com uma fonte de dados conhecida como origem do gráfico de painel.


Para acessar o Dashboard, vá para,



> 
> Página inicial > Personalização > Painéis > Painel
> 
> 
> 


## 1. Como criar um novo painel


1. Vá para Lista de painéis e clique em Novo.
2. Insira o nome do módulo cujo painel você deseja ver.
3. Insira os gráficos do painel que você gostaria que fossem parametrizados para este painel.
4. Salvar.


Ao clicar em `Mostrar Painel`, você poderá ver o Painel com a representação gráfica de suas transações.


![Painel de contabilidade](/files/dashboard.png)


## 2. Adicionando gráficos ao painel


Adicione gráficos a este painel selecionando o `Gráfico do painel` existente ou criando novos.


![Adicionando painel aos gráficos](/files/dashboard-add-charts.png)


Salve as alterações e clique no botão `Mostrar painel` para ver o painel.


![Mostrar botão do painel](/files/dashboard-show-dashboard-button.png)


## 3. Criando um novo gráfico de painel


Para criar um novo gráfico de painel, acesse



> 
> Página inicial > Personalizações > Painéis > Gráfico do painel > Novo
> 
> 
> 


Forneça um nome para o gráfico, ele aparecerá no painel como o rótulo do gráfico, selecione o tipo de gráfico como `Personalizado` e selecione uma `Fonte do gráfico do painel` como os dados fonte deste gráfico.


**Observação:** a nova `fonte do gráfico do painel` só pode ser criada pelo usuário administrador no modo de desenvolvedor.


![Selecionar origem do gráfico do painel](/files/dashboard-chart-from-source.png)


Após definir o campo Fonte do Gráfico, será mostrada a tabela de filtros.


Clique na tabela para editar os filtros.


![Filtro de gráfico do painel](/files/dashboard-chart-filter.png)


Um modal será mostrado para definir filtros. Clique em `Definir` para definir filtros.
![Modal de filtro de gráfico de painel](/files/dashboard-chart-filter-modal.png)


Após definir o campo Fonte do gráfico, a tabela Filtros será atualizada com os valores de filtro selecionados.
![Filtro de gráfico do painel](/files/dashboard-chart-filter-updated.png)


No exemplo acima, criamos um `Dashboard Chart` personalizado para o qual já tínhamos uma `Dashboard Chart Source`. 


Você também pode criar gráficos básicos como Contagem/Soma/Média/Agrupar por de Tarefas com base na data de criação/modificação selecionando `Contagem/Soma/Média/Agrupar por` como `Tipo de gráfico` você também pode usar um relatório existente como fonte no campo `Nome do relatório` para criar um gráfico selecionando `Relatório` como `Tipo de gráfico`.


Para `Contagem`, você precisa selecionar o `Doctype` para o qual você precisa do gráfico no campo `Tipo de documento` e `Baseado em Campo Data` em `Série Temporal Baseada em`.


![Gráfico de painel de contagem](/files/dashboard-chart-count.png)


**Observação:** se você selecionar um tipo de documento de tabela filho em `Tipo de documento`, também deverá selecionar o tipo de documento pai para essa tabela filho em `Tipo de documento pai` code> (este campo só ficará visível quando você selecionar doctype da tabela filha no campo `Tipo de documento`).


![Tipo de documento pai do gráfico de painel](/files/dashboard-chart-parent-document-type.png)


Para `Soma` e `Average` você também deve selecionar o campo `Based On Value` em `Value Based On`. 


![Sum Dashboard Chart](/files/dashboard-chart-sum.png)


Para `Agrupar por` você pode selecionar `Agrupar por tipo` como Contagem/Soma/Média, `Agrupar por com base em` como Criado por/Modificado por e `Número de grupos`.


![Agrupar por gráfico de painel](/files/dashboard-chart-group-by.png)


## 4. Usando painéis


Cada gráfico será mostrado de acordo com os campos definidos no gráfico do painel correspondente. O resultado da origem do gráfico do painel é armazenado em cache para evitar consultas redundantes. Como os dados do gráfico podem ficar desatualizados, cada gráfico também mostrará a hora da última sincronização.


![Última sincronização do painel](/files/dashboard-last-synced.png)


Os filtros usados ​​para gerar os dados do gráfico também podem ser alterados clicando em `Definir filtros`. O gráfico será atualizado automaticamente de acordo com os filtros definidos recentemente.


![Filtros do painel](/files/dashboard-filters.png)


Para obter os dados mais recentes, cada gráfico deve ser atualizado vigorosamente clicando no botão **Forçar atualização** no menu suspenso.



