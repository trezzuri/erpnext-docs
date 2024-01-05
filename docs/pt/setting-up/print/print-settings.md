# Configurações de impressão



**Em Configurações de impressão você pode definir suas preferências de impressão, como tamanho do papel, tamanho de texto padrão, se deseja imprimir como PDF ou HTML, etc.**


Como o ERPNext é um aplicativo baseado em navegador, o comando de impressão real é executado pelo navegador que você está usando.


Para editar as configurações de impressão, vá para:
> Página inicial > Configurações > Configurações de impressão


![Configurações de impressão](/files/print-settings.png)


Existem diversas configurações disponíveis nas Configurações de impressão. Vamos aprender sobre eles.


## 1. Configurações de PDF


### 1.1 PDF ou HTML


Quando você envia por e-mail qualquer documento (como Pedido de Venda/Fatura) do ERPNext, ele é enviado no formato PDF ou HTML. O arquivo é enviado em PDF por padrão. Caso queira enviar um documento no formato HTML, basta desmarcar a opção "Enviar Impressão como PDF".


### 1.2 Repetir cabeçalho e rodapé em PDF


O papel timbrado é um mestre onde você pode definir o Cabeçalho e Rodapé padrão que é anexado ao Formato de Impressão do documento. Se esta propriedade estiver habilitada, o Cabeçalho e o Rodapé serão adicionados a cada página. Se você não quiser que o cabeçalho e o rodapé se repitam em cada página, basta desativar esta configuração.


### Tamanho de página PDF 1,3


O tamanho padrão para impressão de páginas PDF é A4, e você pode escolher qualquer tamanho entre as opções definidas [aqui](https://doc.qt.io/archives/qt-4.8/qprinter.html#PaperSize-enum), incluindo dimensões personalizadas definidas em milímetros.


## 2. Configurações da página


### 2.1 Imprimir com papel timbrado


Ativar esta propriedade marcará automaticamente a opção Cabeçalho ao imprimir um documento. Observe que você precisa definir o papel timbrado como padrão ou selecionar um na transação para que ele apareça na visualização de impressão.


### 2.2 Impressão compacta de item


Transações como pedidos de vendas/faturas possuem uma tabela detalhando os itens comprados ou vendidos. Ele tem várias colunas como nome do item, descrição, UM, valor da taxa, etc. Se houver muitas colunas na tabela de itens, o formato de impressão parecerá um pouco confuso. Você pode melhorar a visualização da tabela ativando a Impressão de item compacto.


De acordo com esta configuração, haverá apenas quatro colunas no formato de impressão, a saber: Descrição, Quantidade, Taxa e Valor.


Os valores de outras colunas (como nome, descrição, imagem, números de série etc.) são concatenados na coluna Descrição.


Quando a caixa de seleção está desmarcada, o formato de impressão fica assim:
![Configurações de formato de impressão incompact](/files/incompact-print.png)


Esta é a aparência do formato de impressão compacto:
![Configurações de formato de impressão compacta](/files/compact-print.png)


### 2.3 Permitir impressão para rascunho


Os documentos (principalmente transações) possuem dois estágios de autenticação, Salvar e Enviar. Os documentos salvos são o primeiro rascunho e não são submetidos ao sistema. Portanto, a impressão é restrita para os documentos nesta fase. No entanto, se você deseja permitir que os usuários também imprimam documentos na fase Rascunho, marque esta caixa de seleção.


### 2.4 Sempre adicione o cabeçalho "Rascunho" para imprimir documentos de rascunho


Ativar esta configuração também imprime "Rascunho" no formato de impressão, indicando que o documento compartilhado ainda não está completamente autenticado.


### 2.5 Permitir quebra de página dentro da tabela


Se a descrição de um item ocupar mais espaço do que o normal de uma página, a ativação dessa configuração dividirá os detalhes do item para a próxima página. Portanto, uma quebra de página será inserida entre a Descrição do Item e o restante dos detalhes será empurrado para a próxima página.


### 2.6 Permitir impressão para cancelamento


Transações canceladas são aquelas que não têm impacto nos relatórios. Se você deseja permitir a impressão das transações canceladas, habilite esta configuração. Uma transação só pode ser cancelada depois de enviada.


### 2.7 Imprimir impostos com valor zero


Nas transações de vendas e compras, você pode adicionar vários impostos sobre o item. Por padrão, no formato de impressão, apenas os impostos que possuem algum valor calculado ficam visíveis. Se desejar imprimir também o imposto que não foi aplicado e tem valor de imposto zero, habilite esta configuração.


## 3. Impressora de rede/servidor de impressão


Você pode ativar o servidor de impressão preenchendo o IP e a porta do servidor de impressão. Em seguida, escolha a impressora padrão.


Antes de ativar este recurso você deve instalar a biblioteca `pycups`.


Você pode precisar primeiro instalar a biblioteca `cups` se ainda não estiver em seu sistema


Para a família de sistemas operacionais Debian:


`sudo apt-get install libcups2-dev`


Para a família Red Hat OS:


`sudo yum install cups-libs`


Depois disso, instale `pycups` no ambiente usando o comando:


`./env/bin/pip install pycups`


Isso é executado no diretório `frappe-bench`.


## 4. Impressão bruta


Você pode ativar a impressão bruta e imprimir em muitas impressoras térmicas suportadas. Leia [Impressão bruta](/docs/pt/setting-up/print/raw-printing) para saber mais.


### 5. Tópicos Relacionados


1. [Formato de impressão](/docs/pt/setting-up/print/print-format)
2. [Estilo de impressão](/docs/pt/setting-up/print/print-style)
3. [Imprimir cabeçalhos](/docs/pt/setting-up/print/print-headings)
4. [Traduções personalizadas](/docs/pt/setting-up/print/custom-translations)



