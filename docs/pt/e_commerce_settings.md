# Configurações de comércio eletrônico



As **configurações do carrinho de compras** e as **configurações dos produtos** herdadas agora estão consolidadas em uma única página de **configurações de comércio eletrônico**.


Para definir as **Configurações de comércio eletrônico**, pesquise:



> 
> **Configurações de comércio eletrônico** na barra incrível (barra de pesquisa)
> 
> 
> 


![Configurações de comércio eletrônico](/files/e_commerce_settings_overview.png)
*Configurações de comércio eletrônico*


### Produtos por página


Defina quantos produtos serão exibidos por página na lista de produtos na página **Todos os produtos** (`/all-products`).


### Filtros e categorias


![Filtros e categorias](/files/filters_and_categories.png)
*Filtros e categorias*


Você também pode adicionar filtros à sua listagem. Existem dois tipos de filtros:


1. **Filtros de campo**: marque a caixa de seleção **Filtros de campo** e adicione os campos com base
no qual você deseja ter filtros. Esses campos também serão usados ​​como categorias para a página **Comprar por categoria**.
2. **Filtros de atributos**: ative a caixa de seleção **Filtros de atributos** e adicione o
atributos com base nos quais você deseja ter filtros.


### Configurações de exibição


1. **Ocultar variantes**: mostre apenas modelos de itens de site na lista de produtos.
2. **Ativar seleção de variante**: mostra um botão de configuração se o item tiver variantes. Pode ser usado para restringir o item específico com base em atributos.
3. **Mostrar preço**: mostra o preço do item na página do produto.
4. **Mostrar disponibilidade de estoque**: mostra se o item está em estoque.
5. **Mostrar quantidade em estoque**: mostra o estoque disponível na página do produto.
6. **Permitir que itens que não estejam em estoque sejam adicionados ao carrinho**: permite que itens que não estejam em estoque sejam adicionados ao carrinho.
7. **Mostrar código de cupom aplicado**: provisão adicional para aplicar código de cupom na finalização da compra.
8. **Mostrar botão de contato**: mostra um botão de contato que os clientes podem usar para perguntar sobre o item. Isso criará um Lead no sistema.
9. **Mostrar Anexos Públicos**: Mostrar anexos públicos no Pedido de Venda gerado, após a finalização da compra, para os Clientes.



> 
> Você pode **ocultar variantes** somente quando os filtros de atributos estão desativados.
> 
> 
> 


### Carrinho de compras


1. **Empresa**: especifique a empresa para a qual a loja virtual está configurada.
2. **Lista de preços**: mencione a lista de preços a ser considerada ao buscar os preços dos itens.
3. **Ativar carrinho de compras**: adicione a opção para adicionar itens ao carrinho.
4. **Grupo de clientes padrão**: adicione o grupo de clientes padrão a ser definido durante a criação automática de clientes ao adicioná-los ao carrinho.


### Configurações de checkout


1. **Ativar finalização da compra**: se a finalização da compra estiver desativada, quando seus clientes adicionarem um item ao carrinho, eles poderão clicar
no botão **Solicitação de cotação** para obter um orçamento. Uma [Cotação](/docs/pt/selling/quotation)
é gerado no sistema. Se ativado, um [Pedido de vendas](/docs/pt/selling/sales-order) será gerado ao clicar no botão **Fazer pedido** em o carrinho.
2. **Conta de gateway de pagamento**: se o checkout estiver ativado, você deverá ter [Integração com PayPal](/docs/pt/erpnext_integration/paypal-integration)
ou [Integração Razorpay](/docs/pt/erpnext_integration/razorpay-integration).
3. **URL de sucesso do pagamento**: após a conclusão do pagamento, redirecione os usuários para a opção selecionada.
4. **Mostrar preço na cotação**: se a finalização da compra estiver desativada, você poderá escolher se deseja ou não mostrar os preços dos itens do site na cotação.
5. **Salvar cotações como rascunho**: Se o checkout estiver desabilitado, ao clicar no botão **Solicitar cotação**, você pode escolher se a cotação gerada automaticamente deve ser enviada automaticamente ou mantido no estado Rascunho.


### Complementos


1. **Ativar lista de desejos**: adiciona a opção para adicionar itens a uma lista de desejos
2. **Ativar comentários e classificações**: adicione a permissão para que **clientes** deixem comentários e classificações em itens do site.
3. **Ativar recomendações**: adicione a disposição para mostrar **itens recomendados** selecionados manualmente em um item do site.


### Comprar por categoria


A página **Comprar por categoria** é uma página pronta para uso que lista categorias vinculadas a itens do site. Essas categorias podem ser configuradas na tabela **Filtros de campo** da seção **Filtros e categorias**.


Você também pode selecionar uma apresentação de slides como banner da página.


### Configurações de exibição de convidados


1. **Ocultar preço para visitantes**: você pode mostrar ou ocultar preços em itens do site para usuários convidados (usuários que não estão logados).
2. **Redirecionar na ação**: se um usuário convidado tentar adicionar um item do site ao carrinho ou à lista de desejos, você poderá selecionar um URL para redirecioná-lo. Por padrão, os usuários convidados são redirecionados para a página `/login`. Em vez disso, você pode redirecioná-los para um formulário da Web personalizado de sua escolha, adicionando um URL aqui, por exemplo. `/entre em contato conosco`



