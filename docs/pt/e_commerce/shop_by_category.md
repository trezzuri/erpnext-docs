# Compre por categoria



ERPNext oferece uma página **Comprar por categoria** (`/comprar por categoria`) pronta para uso, onde os usuários podem navegar até produtos relevantes com base em suas necessidades sem ter que para usar filtros imediatamente.


Para configurar as categorias (nas guias) desta página, acesse:



> 
> Configurações de comércio eletrônico > Filtros e categorias
> 
> 
> 


Na seção **Filtros e categorias**, certifique-se de que **Ativar filtros de campo (categorias)** esteja ativado. As categorias são extraídas da tabela Campos de itens do site. Os filtros de campo como Grupo de Itens, Marca, etc. são reutilizados como categorias nesta página.


Depois de fazer isso, você verá guias na página **Comprar por categoria** (`/shop-by-category`).
![Comprar por categoria](/files/shop-by-category.png)


Além disso, você pode adicionar uma apresentação de slides a esta página (como visto acima) através da seção **Comprar por categoria** em **Configurações de comércio eletrônico**.


### Buscando registros em categorias


#### Grupos de itens


Os grupos de itens são tratados de maneira um pouco diferente devido à sua estrutura em árvore. Os registros do grupo de itens serão buscados se todas as condições a seguir forem atendidas:


* O campo **Mostrar no site** está habilitado no Grupo de itens
* Grupo de itens é o **nó de grupo mais alto** (**O grupo** está ativado e o pai é 'Todos os grupos de itens') ou o **nó folha mais alto** > (**O grupo** está desativado e o pai é 'Todos os grupos de itens')


Cada cartão está vinculado à respectiva página do Grupo de Itens.


#### Outras categorias


Os registros das outras categorias são simplesmente buscados independentemente. Se você quiser ocultar determinados registros aqui também (por exemplo, em **Marca**), você pode adicionar um campo personalizado **Mostrar no site** e ele filtrará os registros que têm esse campo desativado .



> 
> Doctypes personalizados **que estão vinculados ao item do site por meio de um campo de link** também podem ser incluídos aqui junto com grupo de itens, marca, etc.
> 
> 
> 



