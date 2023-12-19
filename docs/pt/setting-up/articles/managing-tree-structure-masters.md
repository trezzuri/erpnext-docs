# Gerenciar mestres de estrutura de árvore



Alguns dos mestres no ERPNext são mantidos em estrutura de árvore. Os mestres estruturados em árvore permitem que você defina mestres Pai e mestres Filhos sob esses Pais. A configuração dessa estrutura permite criar relatórios inteligentes e acompanhar o crescimento em cada nível da hierarquia.


A seguir está a lista parcial de mestres que são mantidos na estrutura em árvore.


* Plano de contas
* Tabela de centros de custo
* Grupo de clientes
* Território
* Vendedor
* Grupo de itens


A seguir estão as etapas para gerenciar e criar registros no mestre estruturado em árvore. Vamos considerar o mestre de território para entender o gerenciamento de árvores mestres.


#### Etapa 1: Vá para o Master


`Venda > Configuração > Território`


#### Etapa 2: Território pai


![Territórios padrão](/files/territory-2.png)


Ao clicar em Território pai, você verá a opção de adicionar território filho abaixo dele. Todos os grupos de territórios padrão serão listados no grupo pai denominado "Todos os territórios". Você pode adicionar mais grupos de território pai ou filho nele.


#### Etapa 3: adicionar novo território


Ao clicar em Adicionar filho, uma caixa de diálogo fornecerá dois campos.


**Nome do grupo de território**


O território será salvo com o nome do território fornecido aqui.


**Nó do grupo**


Se o Nó do Grupo for selecionado como Sim, então este Território será criado como Pai, o que significa que você pode criar ainda mais subterritórios sob ele. Se selecionar Não, ele se tornará um território filho que você poderá selecionar em outros mestres.


Apenas grupos de territórios filhos podem ser selecionados em outros mestres e transações.
![Territórios padrão](/files/territory-1.gif)


Veja a seguir como os Territórios Filhos serão listados em um Território Pai.


![Adicionando novos territórios](/files/territory-3.png)


Seguindo estes passos, você também pode gerenciar outras árvores mestres no ERPNext.




