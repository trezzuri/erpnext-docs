# ERPNext para organização de serviços



**Pergunta:** O ERPNext parece projetado principalmente para comerciantes e fabricantes. O ERPNext é utilizado por empresas que oferecem serviços?


**Resposta:**


Cerca de 30% dos clientes do ERPNext são empresas de serviços. São empresas de desenvolvimento de software, serviços de certificação, consultores individuais e muito mais. Estando no ramo de serviços, usamos o ERPNext para gerenciar nossas operações de vendas, contabilidade, suporte e RH. Confira o vídeo a seguir para saber como o ERPNext usa o ERPNext.



### Configuração mestre


A configuração de uma empresa de serviços difere principalmente para itens. Eles não mantêm Estoque de Itens e portanto, não possuem Armazéns.


Para criar um item de serviço (sem estoque), no cadastro de itens, desmarque o campo "Manter estoque".


![Item de serviço](/files/service-item.png)


Ao criar Pedido de Vendas para os serviços, selecione Tipo de Pedido como **Manutenção**. O pedido de vendas do tipo manutenção precisa de menos detalhes em comparação com o pedido do item em estoque, como nota de entrega, depósito de itens, etc.


A empresa de serviços ainda pode adicionar itens de estoque para manter seus ativos fixos, como computadores, móveis e outros equipamentos de escritório.


### Ocultar recursos não obrigatórios


Como muitos módulos, como Fabricação e Estoque, não serão necessários para a empresa de serviços, você pode ocultar esses módulos de:


`Configuração > Permissões > Mostrar/ocultar módulos`


Os módulos desmarcados aqui ficarão ocultos para todos os usuários.


#### Permissões


ERPNext é o sistema controlado por permissão. Os usuários acessam o sistema com base nas permissões atribuídas a eles. Portanto, se não for atribuída ao usuário uma função relacionada ao módulo Estoque e Manufatura, ela ficará oculta para esse usuário. [Clique aqui para saber mais sobre gerenciamento de permissões.](/docs/pt/setting-up/users-and-permissions.html).


Você também pode consultar o vídeo de ajuda sobre configuração de usuários e permissões no ERPNext.








