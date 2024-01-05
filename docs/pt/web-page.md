# Página da Web



**Conteúdo estático como sua página inicial, sobre nós, entre em contato conosco e páginas de termos pode ser
criado usando a página da Web.**


Para acessar a página da Web, vá para:


> Página inicial > Site > Site > Página da Web


## 1. Como criar uma página da Web


1. Vá para a lista de páginas da Web e clique em Novo.
2. Insira um título e adicione conteúdo na seção principal. A rota será gerada automaticamente
mas você pode mudar isso.
3. Clique em Salvar.
4. A página da web será publicada somente quando **Publicado** estiver marcado.


![Nova página da Web](/files/new-web-page.png)
*Nova página da web*


Visualize sua página da Web clicando em **Ver no site** na barra lateral.


![Página da Web](/files/web-page.png)
*Página da Web*


### 1.1 Dicas para criar uma boa página da web


#### Título


A primeira coisa a definir é o título da sua página. O título tem o máximo
peso para os mecanismos de pesquisa, então escolha um título que reflita as palavras-chave que você
estão direcionando para o seu público. A rota (URL) será gerada automaticamente a partir do
título, mas você pode alterá-lo.


#### Conteúdo


Você pode escrever seu conteúdo em Rich Text, Markdown ou HTML. Se você quiser fazer
páginas de conteúdo simples, Rich Text e Markdown são ótimas opções.


> Aprenda o markdown em alguns minutos em [Dominando o Markdown](https://guides.github.com/features/mastering-markdown/).


#### Imagens


Para conteúdo Rich Text, você pode incorporar imagens diretamente usando o editor. Para
Markdown e HTML, você deve primeiro anexar as imagens ao documento. Agora pegue o
URL da sua imagem clicando com o botão direito no anexo e copiando o endereço.


![Image Link](/files/get-image-link.png)


Agora, adicione-os ao seu Markdown ou HTML usando a sintaxe apropriada.



```

![Texto alternativo](/caminho/para/image-url.png)


![Alt Text](/path/to/image-url.png)

```

## 2. Recursos


### 2.1 Apresentação de slides


Você também pode adicionar uma apresentação de slides à sua página da web. Consulte como criar uma apresentação de slides
em [Apresentação de slides da página inicial](/docs/pt/website/homepage#22-homepage-slideshow)


### 2.2 Publicação agendada


Você pode agendar a publicação de suas páginas da Web se definir a data de início e de término
Data para sua página da web. Eles serão definidos conforme publicados dentro dos intervalos de datas e
a publicação fora do intervalo será cancelada automaticamente.


Páginas não publicadas gerarão um `Erro 404` quando forem visitadas.


### 2.3 Javascript e CSS


Você pode adicionar um script JS à sua página da Web na seção **Script**. Tenha certeza de
escreva seu script dentro do retorno de chamada `frappe.ready`.



```
frappe.ready(() => {
   //seu script aqui
});

```

Você pode adicionar estilo CSS à sua página da Web na seção **Estilo**. Inspecione o
elementos para ver quais classes estão disponíveis para estilo. Se você estiver usando HTML
Conteúdo, você pode usar suas próprias classes e estilizá-las aqui.


### 2.4 Barra lateral


Você pode adicionar uma barra lateral do site com links personalizados à sua página da web. No
A seção **Barra lateral e comentários** ativa **Mostrar barra lateral**. Selecione um existente
Barra lateral do site ou crie uma nova.


![Barra lateral da página da Web](/files/web-page-sidebar.png)
*Barra lateral da página da Web*


Adicione links e suas rotas na tabela Itens da barra lateral.
![Barra lateral do site](/files/new-website-sidebar.png)
*Barra lateral do site*


![Página da Web com barra lateral](/files/web-page-with-sidebar.png)
*Página da Web com barra lateral*


### 2,5 comentários


Você pode ativar comentários em sua página da Web, onde as pessoas podem deixar comentários com
seu nome e e-mail. Ative comentários na seção **Barra lateral e comentários**.


![Comentários da página da Web](/files/web-page-comments.gif)
*Comentários da página da Web*


### 2.6 Cabeçalho


Você pode adicionar um HTML personalizado para a seção de cabeçalho da página. Isso substituirá
o título da página da Web.


![Cabeçalho da página da Web](/files/web-page-header.png)
*Cabeçalho da página da Web*


![Página da Web com cabeçalho personalizado](/files/web-page-with-custom-header.png)
*Página da Web com cabeçalho personalizado*


### 2,7 pão ralado


Você pode adicionar uma lista de localização atual em sua página da Web. Eles serão mostrados no topo
antes do cabeçalho.


![Breadcrumbs da página da Web](/files/web-page-breadcrumbs.png)
*Localização atual da página da Web*


![Página da Web com localização atual](/files/web-page-with-breadcrumbs.png)
*Página da Web com localização atual*


### 2.8 Metatags


Você também pode adicionar meta tags à sua página da web. Você deve adicionar a chave da propriedade e
seu valor na tabela de metatags e gerará automaticamente `meta` tags HTML em
sua página da web.


![Meta tags da página da Web](/files/web-page-meta-tags.gif)
*Metatags de páginas da web*



