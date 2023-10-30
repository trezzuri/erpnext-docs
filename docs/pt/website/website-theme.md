# Tema do site



ERPNext fornece recursos avançados de temas para personalizar a aparência de
seu site e faça com que ele corresponda à sua marca.



> 
> Página inicial > Site > Configuração > Tema do site
> 
> 
> 


## 1. Como criar um tema de site


1. Vá para a lista de temas do site e clique em Novo.
2. Insira um nome para o tema.
3. Personalize seu tema.
4. Clique em Salvar.



> 
> **Observação:** certifique-se de definir o tema do site nas configurações do site para o
>  tema a ser aplicado.
> 
> 
> 


![Selecione o tema do site nas configurações do site](/files/website-theme.png)


## 2. Recursos


### 2.1 Configuração do tema


A seção "Configuração do tema" existe para inicializar um tema batico. Aqui
você pode escolher o esquema de cores, a fonte e os estilos dos botões.


### 2.2 Folha de estilo


Se você conhece [SCSS](https://sass-lang.com/guide) e [Temas do Bootstrap 4](https://getbootstrap.com/docs/4.3/getting-started/theming/),
você pode escrever SCSS personalizado manualmente.


No campo "Substituições personalizadas" você pode sobrescrever as variáveis ​​definidas por qualquer
arquivo de tema do aplicativo. O conteúdo deste campo será incluído *antes* da importação
qualquer outro SCSS. Por exemplo, a variável `$spacer` é definida como `1rem` por padrão.
Basta redefini-lo para `$spacer: 2rem;` para tornar todos os espaços duas vezes maiores.


No campo "SCSS personalizado" você pode adicionar seus próprios estilos. Isso será incluído
*depois* de importar os temas do aplicativo. Você também pode substituir qualquer estilo específico.
Por exemplo, se você não gosta dos nossos botões, basta incluir o seguinte:



```
.btn-primary {
    cor de fundo: $teal;
    cor: $laranja;
}

```

### 2.3 Arquivos de tema incluídos


Se você der uma olhada no tema padrão gerado pela caixa de diálogo de configuração, ele
importa `frappe/public/scss/website` e `erpnext/public/scss/website`. Esses
são os arquivos de tema padrão para os aplicativos `frappe` e `erpnext`. Se você tiver qualquer outro
aplicativos instalados, eles também poderão fornecer seu próprio arquivo `website.scss`.


A seção "Arquivos de tema incluídos" lista todos os aplicativos instalados. Cada aplicativo pode trazer
é seu próprio arquivo de tema (`[app]/public/scss/website.scss`). Um tema pode estar completo,
fornecendo estilos para todo o site ou apenas um complemento. Por exemplo, pode
estilize apenas os elementos que ele introduz. Ao marcar as caixas você pode escolher quais
o tema deve ser incluído no seu site.


![Arquivos de tema incluídos](/files/website-theme-included-theme-files.gif)


### 2.4 JS personalizado


Você também pode escrever JavaScript personalizado que será executado quando seu tema for aplicado.
Use-o para adicionar/remover classes de elementos ou qualquer script que ajude você a alterar como
a aparência dos seus elementos.



