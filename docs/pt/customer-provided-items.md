# Itens fornecidos pelo cliente



Na Fabricação por Contrato, em alguns casos, o Cliente fornece itens específicos como um ou alguns dos componentes da BOM. Estes itens não podem ser recebidos através de um 'Ciclo de Compra', pois isso significará tornar o Cliente como Fornecedor ao mesmo tempo. Ele também passará por cada tipo de documento do ciclo.


Neste recurso, o Item Fornecido pelo Cliente é recebido através de 'Entrada de Estoque' com o tipo 'Recebimento de Material' de uma 'Solicitação de Material' com o tipo 'Fornecido pelo Cliente'. Esse recurso é usado quando alguém subcontrata você o processo de fabricação e fornece as matérias-primas.


![Solicitação de material fornecido pelo cliente](/files/material-request-customer-provided.png)


Aqui estão as etapas sobre como configurar um item 'Fornecido pelo cliente'.


1. Acesse [Item Doctype](/docs/pt/stock) e adicione um novo item 'Fornecido pelo cliente'.


> Página inicial > Estoque > Itens e preços > Item
2. Na seção 'Detalhes de compra e reabastecimento', marque 'O cliente
Fornecido' e defina um Cliente padrão. Observe que a opção "É item de compra" precisa estar desmarcada para usar esse recurso.


![Detalhes da compra do item](/files/item-customer-provided.png)


Como receber um item 'fornecido pelo cliente'?


1. Se um 'Plano de Produção' for usado, a 'Solicitação de Material' para este item poderá ser criada automaticamente. Ou seja, o item a ser fabricado é buscado primeiro via Pedido de Venda ou Solicitação de Material, os itens são buscados para a Ordem de Serviço através do botão 'Obter Itens para Ordem de Serviço', em seguida clique no botão 'Obter Matéria Prima para Produção'.


![Solicitação de material no plano de produção](/files/material-request-production-plan.png)
2. Depois que um componente em uma BOM for definido como 'Fornecido pelo cliente' e a 'Solicitação de material' for criada a partir de um 'Plano de produção', ele criará 'Solicitação de material' com o tipo 'Compra' e 'Fornecido pelo cliente '. A partir daí, pode ser criado um 'Entrada de Estoque' com finalidade 'Recebimento de Material'.


![Entrada de estoque da solicitação de material](/files/create-mr-from-production-plan.png)
3. Uma 'Solicitação de Material' pode ter múltiplas 'Entradas em Estoque'-Recebimento de Material. Isto
refletirá isso no status.
4. O cliente poderá acompanhar suas 'Solicitações de Materiais' em um Portal da Web
'Solicitações de Materiais'. O portal é filtrado para mostrar apenas a 'Solicitação de Material' do cliente.




