# Página inicial



**Uma página inicial é a página de destino padrão do seu site.**


O Módulo de Site do ERPNext gera uma landing page padrão para o seu site. Você
pode personalizá-lo na página inicial.


Para acessar a página inicial do ERPNext, vá para:



> 
> Página inicial > Site > Portal > Página inicial
> 
> 
> 


## 1. Como configurar a página inicial


1. Selecione a empresa.
2. Defina o título. Isso será mostrado na guia do navegador.
3. Configure a seção Hero conforme explicado na próxima seção.


![Homepage](/files/homepage.png)
*Página inicial*



> 
> Certifique-se de que sua 'Página inicial' padrão esteja definida como `home` nas configurações do site para
>  isso funcione.
> 
> 
> 


## 2. Seção Herói


Existem três maneiras de personalizar a aparência da seção Hero:


1. Tag Line e descrição (padrão).
2. Apresentação de slides da página inicial.
3. Seção de Herói Personalizado.


### 2.1 Slogan e descrição


Depois de definir seu slogan, descrição e imagem principal, você terá uma experiência decente
olhando a primeira página. Você também pode alterar o URL do botão Explorar em **URL de "Todos os produtos"**.


![Página inicial do site](/files/website-homepage.png)
*Página inicial do site*


### 2.2 Apresentação de slides da página inicial


Defina a **seção principal com base em** como **apresentação de slides** e a **apresentação de slides da página inicial**
aparecerá.


![Configuração da apresentação de slides da página inicial](/files/homepage-slideshow-setting.png)
*Configuração da apresentação de slides da página inicial*


Agora, selecione uma apresentação de slides existente ou crie uma nova conforme mostrado a seguir:


![Apresentação de slides do site](/files/website-slideshow.png)
*Apresentação de slides do site*



> 
> Para obter melhores resultados, certifique-se de que todas as imagens da apresentação de slides tenham a mesma altura e
>  a largura deles é maior que a altura.
> 
> 
> 


![Página inicial do site com apresentação de slides](/files/website-homepage-slideshow.gif)


### 2.3 Seção de herói personalizado


O terceiro tipo de seção Hero permite que você escreva seu próprio HTML.


Defina **Seção Hero baseada em** como **Seção Hero**.


Agora crie uma nova Seção de Herói. Defina **Seção baseada em** como **HTML personalizado**.
Escreva seu HTML personalizado no campo HTML da seção.


![Configurações da página inicial](/files/homepage-hero-custom.png)
*Configurações da página inicial*


Você pode escrever qualquer marcação [Bootstrap 4](https://getbootstrap.com/) válida aqui.


![Nova seção de herói](/files/hero-custom.png)
*Seção Novo Herói*


Será algo assim:
![Homepage Hero Custom](/files/website-homepage-custom.png)
*Herói da página inicial personalizado*


## 3. Produtos em destaque


Você também pode exibir produtos em destaque na sua página inicial adicionando-os à
Tabela de produtos.


![Tabela de produtos da página inicial](/files/homepage-featured-products.png)
*Tabela de produtos da página inicial*


Será algo assim:
![Produtos em destaque na página inicial](/files/website-featured-products.png)
*Produtos em destaque na página inicial*


## 4. Seção da página inicial


Você pode adicionar seções personalizadas à sua página inicial criando novas seções da página inicial.



> 
> Vá para Site > Portal > Seção da página inicial
> 
> 
> 


Uma seção da página inicial pode consistir em cartões ou HTML personalizado. Definir **seção baseada em**
para **Cartões**.


![Nova seção da página inicial](/files/new-homepage-section.png)
*Nova seção da página inicial*


Adicione detalhes para cada cartão, como Título, Subtítulo, Imagem, Conteúdo e Rota no
Tabela de cartões de seção.


Será algo assim:
![Seção da página inicial](/files/homepage-section.png)
*Seção da página inicial*


Você também pode controlar a ordem em que essas seções aparecem definindo o
**Ordem das seções**. 0 será mostrado primeiro, seguido por 1 e assim por diante.



> 
> Para adicionar seções com HTML personalizado, consulte [Seção de herói personalizado](#23-custom-hero-section).
> 
> 
> 


## 5. Página inicial personalizada


ERPNext permite que você tenha uma página inicial completamente diferente se você não quiser
use o padrão descrito acima.


Para configurar uma página inicial personalizada:


1. Crie uma [Página da Web](/docs/pt/website/web-page).
2. Vá para Site > Configuração > Configurações do site.
3. Defina a página inicial como a `rota` da sua página da web.
![](/files/custom-homepage.png)



