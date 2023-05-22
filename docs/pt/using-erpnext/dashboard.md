# Painel



> 
> Introduzido na versão 12
> 
> 
> 


**O painel fornece uma visão rápida dos principais indicadores de desempenho relevantes para o processo de negócios.**


Cada painel consiste em um ou mais gráficos do painel, cada um configurado com uma fonte de dados conhecida como fonte do gráfico do painel.


Para acessar o Painel, acesse,



> 
> Página inicial > Personalização > Painéis > Painel
> 
> 
> 


## 1. Como criar um novo painel


1. Vá para a lista de painéis e clique em Novo.
2. Digite o nome do módulo para o qual deseja ver o painel.
3. Insira os gráficos do painel que você deseja parametrizar para este painel.
4. Salvar.


Ao clicar em `Mostrar Dashboard`, você poderá ver o Dashboard dando a representação gráfica de suas transações.


![Painel de contabilidade](/files/dashboard.png)


## 2. Adicionando gráficos ao painel


Adicione gráficos a este painel selecionando `Dashboard Chart` existente ou criando novos.


![Adicionar painel a gráficos](/files/dashboard-add-charts.png)


Salve as alterações e clique no botão `Mostrar painel` para ver o painel.


![Mostrar botão do painel](/files/dashboard-show-dashboard-button.png)


## 3. Criando um novo gráfico de painel


Para criar um novo gráfico de painel, acesse



> 
> Página inicial > Personalizações > Painéis > Gráfico do painel > Novo
> 
> 
> 


Forneça um nome para o gráfico, ele aparecerá no painel como o rótulo do gráfico, selecione o tipo de gráfico como `Custom` e selecione uma `Dashboard Chart Source` como os dados fonte para este gráfico.


**Observação:** a nova `origem do gráfico do painel` só pode ser criada pelo usuário administrador no modo de desenvolvedor.


![Selecione a origem do gráfico do painel](/files/dashboard-chart-from-source.png)


Depois de definir o campo Chart Source, a tabela de filtros será exibida.


Clique na tabela para editar os filtros.


![Dashboard Chart Filter](/files/dashboard-chart-filter.png)


Um modal será mostrado para definir os filtros. Clique em `Definir` para definir os filtros.
![Modal de filtro de gráfico de painel](/files/dashboard-chart-filter-modal.png)


Após definir o campo Origem do gráfico, a tabela Filtros será atualizada com os valores de filtro selecionados.
![Dashboard Chart Filter](/files/dashboard-chart-filter-updated.png)


No exemplo acima, criamos um `Dashboard Chart` personalizado para o qual já tínhamos uma `Dashboard Chart Source`. 


Você também pode criar gráficos básicos como Count/Sum/Average/Group By de ToDo com base na data de criação/modificação selecionando `Count/Sum/Average/Group By` como `Chart Type< /code> você também pode usar um relatório existente como fonte no campo `Nome do relatório` para criar um gráfico selecionando `Relatório` como `Tipo de gráfico`.< /p>
Para `Contagem`, você precisa selecionar o `Doctype` para o qual você precisa do gráfico no campo `Document Type` e `Based On Campo de data` em `Série temporal baseada em`.


![Count Dashboard Chart](/files/dashboard-chart-count.png)


**Observação:** Se você selecionar um doctype de tabela filho em `Document Type`, também deverá selecionar o doctype pai para essa tabela filho em `Parent Document Type` (este campo só ficará visível quando você selecionar doctype da tabela filha no campo `Tipo de documento`).


![Dashboard Chart Parent Document Type](/files/dashboard-chart-parent-document-type.png)


Para `Sum` e `Average` você também deve selecionar o campo `Based On Value` em `Value Based On`. 


![Sum Dashboard Chart](/files/dashboard-chart-sum.png)


Para `Agrupar por`, você pode selecionar `Agrupar por tipo` como Contagem/Soma/Média, `Agrupar por com base em` como Criado por/Modificado por e `Número de grupos`.


![Group By Dashboard Chart](/files/dashboard-chart-group-by.png)


## 4. Usando painéis


Cada gráfico será mostrado de acordo com os campos definidos no Gráfico do Painel correspondente. O resultado da origem do gráfico do painel é armazenado em cache para evitar consultas redundantes. Como os dados do gráfico podem estar desatualizados, cada gráfico também mostrará o último horário sincronizado.


![Dashboard Last Synced](/files/dashboard-last-synced.png)


Os filtros usados ​​para gerar os dados do gráfico também podem ser alterados clicando em `Definir filtros`. O gráfico será atualizado automaticamente de acordo com os filtros definidos recentemente.


![Dashboard Filters](/files/dashboard-filters.png)


Para obter os dados mais recentes, cada gráfico deve ser atualizado vigorosamente clicando no botão **Forçar atualização** no menu suspenso.`

