# Pesquisa de comércio eletrônico



Todas as páginas de listagem de produtos contêm uma **barra de pesquisa** que permite aos usuários pesquisar rapidamente itens do site ou grupos de itens. Ele também armazena pesquisas recentes nas quais você pode clicar e reutilizar.


![Search](/files/e-commerce-search.png)


## RediSearch



> 
> **Experimental**: requer Redis 6+
> 
> 
> 


Por padrão, o ERPNext executa uma pesquisa simples no banco de dados, mas você pode **opcionalmente** optar por usar o [RediSearch](https://redis.com/modules/redis-search/) para uma pesquisa super rápida. Você pode consultar a [documentação de instalação](/docs/pt/e_commerce/articles/installing_redisearch_to_enable_super_fast_e_commerce_search).



> 
> Vá para > **Configurações de comércio eletrônico** > **Configurações de pesquisa de item** > Marque **Ativar nova pesquisa**
> 
> 
> 


![Configurações de pesquisa de itens com RediSearch](/files/item-search-settings-enabled.png)


#### Configurações sem RediSearch


Se o RediSearch não estiver instalado, as **Configurações de pesquisa de itens** ficarão assim:
![Configurações de pesquisa de item sem RediSearch](/files/item-search-settings.png)


#### Campos Configuráveis


Juntamente com a pesquisa rápida, você tem a opção de configurar os campos que deseja que a pesquisa considere. Adicione campos separados por vírgula na caixa de texto **Campos de índice de pesquisa** para torná-los pesquisáveis.


Ex. Adicionar **marca** a esses campos torna-os pesquisáveis. Digitando uma marca, por ex. 'Apple' deve dar resultados onde a marca é 'Apple'.


Os resultados serão baseados nos valores de todos os campos mencionados na caixa de texto **Campos de índice de pesquisa**.



> 
> Campos dos tipos foll.g são suportados: **Link**, **Table MultiSelect**, **Data**, **Small Text** , **Editor de texto**
> 
> 
> 



