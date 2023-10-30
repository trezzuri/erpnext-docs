# Noções baticas de fabricação



ERPNext vem com baterias incluídas para todos os requisitos de um negócio de manufatura, como manutenção de armazéns, estações de trabalho/máquinas, operações, produtos acabados, matérias-primas, rastreamento de lista de materiais, planejamento e execução de ordens de trabalho, compras e muito mais.
## 1. Dados mestre


O módulo de Manufatura no ERPNext ajuda você a manter Armazéns (localização), Estações de Trabalho, Operações, Produtos Acabados e Matérias-Primas. Para a fabricação são importantes as Operações e suas respectivas Estações de Trabalho, que podem ser configuradas com base nos Produtos Acabados da Lista de Materiais. Os armazéns são úteis para armazenar matérias-primas e produtos acabados. No ERPNext, os usuários podem criar Armazéns separados para manter Matérias-Primas e Produtos Acabados.


Mais detalhes estão abaixo:


1. [Armazém](/docs/pt/stock/warehouse)
2. [Estação de trabalho/máquina](/docs/pt/manufacturing/workstation)
3. [Operação](/docs/pt/manufacturing/operation)
4. [Matéria-prima/Produto acabado](/docs/pt/stock/item)
5. [Roteamento](/docs/pt/manufacturing/routing)


## 2. Dados de transação


O módulo de Manufatura no ERPNext ajuda você a manter uma lista de materiais (BOMs) multinível para seus itens. Ele ajuda no cálculo de custos de produtos, planejamento de produção, criação de ordens de serviço para o chão de fábrica, criação de cartões de trabalho e planejamento de estoque, obtendo suas necessidades de materiais por meio de BOMs (também chamadas de [Planejamento de Requisitos de Materiais ou MRP](https://erpnext.com/blog/general/what-is-mrp-and-do-you-need-it)).


Mais detalhes estão abaixo:


1. [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)
2. [Ordem de serviço](/docs/pt/manufacturing/work-order)
3. [Cartão de trabalho](/docs/pt/manufacturing/job-card)
4. [Plano de produção](/docs/pt/manufacturing/production-plan)


## 3. Tipos de Planejamento de Produção


Em termos gerais, existem três tipos de Sistemas de Planejamento de Produção:


* **Produzir para estoque:** Nestes sistemas, a produção é planejada com base em uma previsão e os itens são então vendidos a distribuidores ou clientes. Todos os bens de consumo de rápido movimento vendidos em lojas de varejo, como sabonetes, água engarrafada etc., e eletrônicos, como telefones, são feitos para estoque.
* **Fazer sob encomenda:** Nesses sistemas, os itens são fabricados somente depois que o cliente faz um pedido de um determinado número de acordo com a necessidade do cliente. Por exemplo, um bolo de casamento.
* **Engenheiro sob encomenda:** Neste caso, cada venda é um projeto separado e deve ser projetado e projetado de acordo com os requisitos do cliente. Exemplos comuns disso são móveis personalizados para empresas, máquinas-ferramentas, dispositivos especiais, fabricação de metal, etc.


A maioria das pequenas e médias empresas de manufatura são baseadas em um sistema de fabricação sob encomenda ou engenharia sob encomenda, assim como o ERPNext.


Para sistemas de engenharia sob encomenda, o módulo Manufatura deve ser usado junto com o [módulo Projeto](/docs/pt/projects).


## 4. Impacto da fabricação no estoque


O status da ordem de serviço depende das transações de estoque feitas com relação a ela. No ERPNext, você pode transferir as matérias-primas necessárias para fabricar produtos acabados da Loja para o Armazém de Trabalho em Andamento. Do armazém de Trabalho em Andamento as matérias-primas podem ser consumidas através da Entrada de Estoque. Você tem a opção de consumir a granel as matérias-primas e adicionar o produto acabado ou consumir os materiais primeiro e depois adicionar o produto acabado.


## 5. Demonstração de Manufatura ERPNext


Confira o vídeo a seguir para conhecer os recursos do módulo de fabricação.









