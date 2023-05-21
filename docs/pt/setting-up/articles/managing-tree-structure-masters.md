# Gerenciar mestres de estrutura de árvore


Alguns dos mestres do ERPNext são mantidos em estrutura de árvore. Os mestres estruturados em árvore permitem que você defina o mestre pai e os mestres filho sob esses pais. A configuração dessa estrutura permite criar relatórios inteligentes e acompanhar o crescimento em cada nível da hierarquia.


A seguir está a lista parcial de mestres que são mantidos na estrutura em árvore.


* Plano de contas
* Tabela de Centros de Custo
* Grupo de clientes
* Território
* Vendedor
* Grupo de itens


A seguir estão as etapas para gerenciar e criar registro no mestre estruturado em árvore. Vamos considerar o Territory master para entender o gerenciamento de tree masters.


#### Etapa 1: Vá para o Mestre


`Venda > Configuração > Território`


#### Etapa 2: Território pai


![Territórios Padrão](/files/territory-2.png)


Ao clicar em Território pai, você verá a opção de adicionar território filho abaixo dele. Todos os grupos de território padrão serão listados no grupo pai chamado "Todos os territórios". Você pode adicionar mais grupos de território pai ou filho sob ele.


#### Etapa 3: adicionar novo território


Ao clicar em Add Child, uma caixa de diálogo fornecerá dois campos.


**Nome do grupo de territórios**


O território será salvo com o nome do território fornecido aqui.


**Nó do Grupo**


Se o nó do grupo for selecionado como Sim, esse território será criado como pai, o que significa que você pode criar subterritórios sob ele. Se selecionar Não, ele se tornará o Território filho, que você poderá selecionar em outros mestres.


Somente grupos de territórios filhos são selecionáveis ​​em outros mestres e transações.
![Territórios Padrão](/files/territory-1.gif)


Veja a seguir como os territórios filhos serão listados em um território pai.


![Adicionando novos territórios](/files/territory-3.png)


Seguindo estes passos, você pode gerenciar outras árvores mestres também no ERPNext.