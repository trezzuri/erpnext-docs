# Formato de impressão



**Com o Formato de impressão, você pode definir a aparência dos tipos de documentos durante a impressão.**


Cada transação tem um formato de impressão padrão chamado 'Padrão'. Você pode alterar os formatos de impressão:


* Usando o formulário Formato de impressão
* Usando scripts Jinja/JS em formato de impressão
* Uso do [Criador de formato de impressão](/docs/pt/setting-up/print/print-format-builder) para criar formatos de impressão com a IU
* Usar formulário personalizado para ocultar/exibir campos


Para acessar o formato de impressão, vá para:


> Página inicial > Configurações > Formato de impressão


## 1. Como criar um formato de impressão


1. Vá para a lista de formatos de impressão e clique em Novo.
2. Digite um nome e selecione um DocType para o qual o formato de impressão será usado.
3. O módulo ao qual deve ser aplicado será selecionado automaticamente.


![Menu Formato de impressão](/files/print-format-menu.png)
4. Salvar.


Em Configurações de estilo, há opções para alterar as opções de estilo. Com essas opções, você pode alterar a fonte, alinhar os rótulos à esquerda ou à direita, adicionar títulos às seções, etc.


Para estilizar o formato de impressão usando Jinja/JS personalizado, clique em Formato personalizado. Se você selecionar esta opção, haverá uma caixa de seleção para impressão bruta. Para saber mais sobre impressão bruta, [clique aqui](/docs/pt/setting-up/print/raw-printing).


Se o modo de desenvolvedor estiver ativado, você poderá selecionar Padrão como sim para contribuir com um formato de impressão como formato de impressão padrão (predefinido) no sistema.


## 1.1 Usando Personalizar formulário para alterar os itens do formato de impressão


Os campos nas transações e suas tabelas filhas podem ser ocultados/exibidos usando Personalizar Formulário.
Por exemplo, se você deseja ocultar o 'Código do Item' ao imprimir uma Cotação, clique no ícone de impressão para entrar na tela de impressão.


Vá para Menu > Personalizar, selecione Item de cotação no campo 'Inserir tipo de formulário'.
![Personalizar formato de impressão](/files/print-format-customize1.png)


Para saber mais, visite a página [Personalizar formato de impressão](/docs/pt/customize-erpnext/print-format).


Na tabela de campos, expanda a linha 'Código do item', role para baixo e marque a caixa de seleção 'Imprimir Ocultar'.
![Formato de impressão Imprimir ocultar](/files/print-format-customize2.png)


Um formato de impressão recém-criado pode ser selecionado na tela de impressão de uma transação. A partir daí você pode ver como fica e prosseguir com a impressão.
![Selecionando um formato de impressão](/files/print-format-selection.png)


## 2. Vídeo






### 3. Tópicos Relacionados


1. [Estilo de impressão](/docs/pt/setting-up/print/print-style)
2. [Imprimir cabeçalhos](/docs/pt/setting-up/print/print-headings)
3. [Cabeçalho timbrado](/docs/pt/setting-up/print/letter-head)
4. [Modelo de impressão de cheque](/docs/pt/setting-up/print/cheque-print-template)
5. [Desativação de quebras de linha em seções de formato de impressão](/docs/pt/setting-up/articles/print-format-sections)



