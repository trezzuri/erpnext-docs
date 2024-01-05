# Item do site



As informações do site sobre um item agora são movidas para um novo DocType chamado **item do site**. Publicar um item agora é tão simples quanto clicar em um botão. Depois que um item tiver um item do site criado, ele será publicado com sucesso.


Os pré-requisitos aqui são [Itens](/docs/pt/stock/item).


### Publicando um item


O botão **Publicar no site** fica visível em todos os itens **não publicados** em **Ações**. Este botão criará um **item do site** e, assim, publicará o item no site.


![Publicar Item](/files/publish-item.gif)


Se você visitar `your-site-name/all-products` , verá o item do site recém-criado listado aqui.


> Para visualizar a página Item do site no site, clique no link **Ver no site** no canto superior esquerdo, logo acima da imagem do item no documento Item do site.


### Atualizando o item do site


![Página de item do site](/files/web-item-page-overview.png)
*Página de item do site*


Depois que um item do site for criado, você poderá atualizar as informações nele contidas que serão exibidas no site. Aqui estão os campos:


#### Geral


1. **Nome do item do site**: o título do item do site no site é escolhido neste campo.
2. **Rota**: é gerada automaticamente e apenas menciona a rota em que a visualização da página inteira do seu item estará disponível.
3. **Publicado**: se quiser ocultar ou remover seu item publicado, você pode desmarcar esta caixa de seleção.


#### Exibir imagens


1. **Imagem do site**: É preenchida automaticamente com a imagem do mestre de itens. Você também pode alterá-lo.
2. **Slideshow**: Se você adicionar um Slideshow, ele será mostrado na página do Item do Site. Se uma apresentação de slides estiver ausente, o padrão será mostrar a imagem do site (se houver).
3. **Descrição da imagem**: É um texto alternativo caso a imagem não apareça.


#### Informações sobre estoque


1. **Armazém do Site**: Selecione o Armazém que armazenará o estoque deste Item do Site. A disponibilidade do Item do Site será mostrada dependendo do estoque em saldo neste Armazém selecionado.
2. **Em espera**: Se ativado, será indicado que o item do site está disponível em ordem de espera e geralmente não está pré-estocado. **Disponível em pedidos pendentes** ficará visível em vez de **Esgotado** ou **Em estoque**.


> Observação: se o Armazém do site não estiver definido e 'Manter estoque' de um item estiver marcado, a página do produto listará o item como 'Não em estoque'.


#### Exibir informações


1. **Descrição resumida do site**: Este é um campo de texto onde você pode mencionar um breve resumo como uma descrição, para a **Visualização de lista**. Você também pode adicionar algum HTML aqui que aparecerá na visualização de lista. por exemplo, `Este item é **100%** puro!`
2. **Descrição do site**: Este é um campo de editor de rich text, onde você pode formatar a descrição do item do seu site para torná-lo atraente e informativo. A Descrição do Item é usada como alternativa se a Descrição do Site não for mencionada.
3. **Especificações do site**: você pode mencionar as especificações do item do site, como peso, fabricante, dimensões, material, etc. Você também pode adicionar especificações comuns no grupo de itens ao qual este item do site pertence e copiar aqui clicando em **Copiar do grupo de itens**. Essas informações estarão visíveis na seção **Detalhes do produto** na página do item do site.


#### Exibir informações adicionais


A seção **Detalhes do produto** também pode ser visualizada em uma seção com guias junto com outras informações. Para isso:


* Na seção **Exibir informações adicionais**, ative **Adicionar seção com guias**.
* Agora você pode adicionar guias na tabela **Guias** adicionando um rótulo e conteúdo a ela. O campo de conteúdo é um editor HTML onde você pode adicionar HTML avançado, para embelezar sua guia, ou um simples parágrafo.
* Esta seção com guias definirá **Detalhes do produto** como a primeira guia que conterá as **Especificações do site** indicadas acima (se presentes).
* Isso será seguido por guias da tabela **Guias**


![Detalhes do produto do item do site](/files/web-item-product-details.png)


#### Itens recomendados


Você pode mostrar **itens recomendados** em relação aos itens do site para incentivar os usuários a prestar atenção em um item intimamente relacionado. Isso pode ser ativado em **Configurações de comércio eletrônico** > **Complementos** > **Ativar recomendações**.


Você pode então adicionar itens recomendados a um item do site na seção **Itens recomendados** e adicionar os itens a serem recomendados. Eles aparecerão na página de itens do site.


![Itens recomendados](/files/recommended-items.png)


#### Ofertas


Os códigos de cupom podem ser adicionados na finalização da compra, mas os clientes devem saber sobre esses códigos. Para isso, **Ofertas** podem ser adicionadas ao Item do Site para exibição.


* Vá para a seção **Ofertas** no item do site.
* Adicione um título de oferta curto com uma/duas palavras no **Título da oferta**.
* Adicione um subtítulo um pouco mais longo, uma frase no **Subtítulo da oferta**.
* Adicione detalhes extensos sobre a oferta na **Descrição da oferta**. **Salvar**.


![Ofertas de itens do site](/files/web-item-offers.png)


#### Pesquisa e SEO


1. **Classificação**: atribua uma classificação ao item do site para ter controle sobre sua posição na lista de produtos. Os itens do site com classificação mais alta serão exibidos em uma posição mais alta.
2. **Definir meta tags**: as meta tags ajudam no SEO. Consulte [Página da Web](/docs/pt/website/web-page) para saber como adicioná-los.
3. **Grupos de itens do site**: nesta tabela você pode selecionar [Grupos de itens existentes ou criar novos](/docs/pt/stock/item-group) para classificar itens em seu site. O item do site ficará visível nas páginas de grupo de itens dos grupos de itens mencionados nesta tabela.


#### Conteúdo de exibição avançado


Você pode adicionar uma seção de estilo adicional usando a marcação Bootstrap 4 para a página Item do site.
![Exibição avançada do item do site](/files/web-item-advanced-display.png)


### Adicionando detalhes de preço


Os preços podem ser adicionados aos itens do site por meio do **Preço do item**. Antes de adicionar um preço de item, acesse **Configurações de comércio eletrônico** e certifique-se de que **Empresa, Lista de preços e Grupo de clientes padrão** estejam definidos.


Agora você pode prosseguir e criar um **Preço do item** para o item do site e selecionar a **Lista de preços** como aquela nas **Configurações de comércio eletrônico**. forte>.


Você também pode adicionar uma **Regra de preços** com uma **Porcentagem de desconto** ou um **Valor do desconto** no preço do item existente, para mostrar **marcado preços**.
![Preço fixado na página do item do site](/files/web-item-striked-price.png)



