# Personalizar formulário



**Personalizar formulário é uma ferramenta que permite fazer alterações em um tipo de formulário ou tipo de documento (DocType) no front-end.**


Ele permite que você insira [Campos personalizados](/docs/pt/customize-erpnext/custom-field) conforme sua necessidade ou personalize as propriedades dos campos padrão .


Antes de nos aventurarmos a aprender a ferramenta de Customização de Formulários, [clique aqui](/docs/pt/customize-erpnext/doctype) para entender a arquitetura de formulários no SOMA . Isso ajudará você a usar a ferramenta Personalizar formulário com mais eficiência.


Para acessar o Formulário Personalizado, acesse:



> 
> Página inicial > Personalização > Personalização de formulário > Personalizar formulário
> 
> 
> 


Você também pode ir para a exibição de lista de qualquer DocType e selecionar Personalizar nas opções do Menu.


![Personalizar opção na exibição de lista](/files/customize-option-in-list-view.png)


## 1. Como personalizar um formulário


1. Clique em Personalizar formulário.
2. Você será redirecionado para uma página na qual será solicitado a inserir o tipo de formulário.
3. Depois de inserir o tipo de formulário neste campo, a página se expande ainda mais e você poderá ver vários recursos.


![Selecionar tipo de documento no formulário personalizado](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. Opções ao personalizar um formulário


1. **Alterar rótulo**: este campo é obtido por meio da tradução personalizada. Você pode alterar o nome do campo para adequá-lo ao seu setor/idioma. Por exemplo, se você é uma empresa de serviços e deseja alterar o rótulo de 'Cliente' para 'Consumidor', o mesmo pode ser feito em [Tradução personalizada](/docs/pt/setting-up/ print/custom-translations) e o mesmo deve ser refletido aqui.


![Change Label](/files/customize-customize-form-label.png)
2. **Campo Título**: Este campo pode ser usado para gerar o título durante a visualização das listas. Qualquer campo do tipo "Dados" pode ser definido como o Campo de título durante a visualização dos formulários na exibição de lista. Por exemplo, se você deseja visualizar a lista de todos os seus funcionários com o campo Cargo como 'Código do Funcionário' em vez de Nome do Funcionário, o mesmo pode ser configurado aqui. Confira nosso artigo sobre [Título do documento](/docs/pt/customize-erpnext/document-title) para obter mais informações.


*Saiba mais sobre os tipos de campo [aqui](/docs/pt/customize-erpnext/articles/field-types.html).*
3. **Formato de impressão padrão**: para um único DocType, pode haver vários formatos de impressão. Aqui você pode selecionar o formato de impressão padrão para o DocType selecionado. Por exemplo, uma empresa pode ter diferentes cabeçalhos para diferentes finalidades que podem ser configuradas por meio de formatos de impressão. No entanto, você pode selecionar dois formatos de impressão padrão diferentes para um pedido de venda e uma carta de compromisso. Verifique [Formatos de impressão personalizados](/docs/pt/customize-erpnext/print-format) para obter mais informações.
4. **Campo de imagem**: você pode selecionar um campo "Anexar imagem" para seu campo de imagem. Isso se torna a imagem que representa esse DocType específico. Por exemplo, o 'Campo de Imagem' de um Funcionário pode ser sua fotografia ou um instantâneo de suas carteiras de identidade; o mesmo pode ser configurado aqui.


![Campo de imagem em DocType](/files/customize-form-image-field.png)
5. **Max Attachments**: você pode inserir o número máximo de anexos que podem ser adicionados a este DocType.
6. **Campos de pesquisa**: Ao criar qualquer DocType, você pode querer vincular um determinado campo a outro DocType. Para facilitar a seleção, você também pode garantir que poderá ver o valor de outro campo do último DocType no resultado da pesquisa. Para obter mais informações [clique aqui](/docs/pt/customize-erpnext/articles/search-record-by-specific-field).
7. **Campo de classificação**: Os registros em qualquer lista de DocType são gerados com base no campo que você definiu no campo de classificação aqui. Por exemplo, para itens, se você deseja que sua lista seja gerada de acordo com o nome do item, você pode configurar o mesmo aqui.


![Classificar campo](/files/customize-sort-field.png)
8. **Ordem de classificação**: você pode selecionar se deseja que a classificação seja feita em ordem crescente ou ordem decrescente. Para entender melhor o campo de classificação e a ordem de classificação, confira  [Personalizando a ordem de classificação na exibição de lista](/docs/pt/customize-erpnext/articles/customizing-sorting-order-in-the-list-view).
9. **Modelo de e-mail padrão**: para um único DocType, pode haver vários  [Modelos de e-mail](/docs/pt/setting-up/email/email-template). Aqui você pode definir o modelo de e-mail padrão para o DocType selecionado. Por exemplo, você pode definir um modelo de e-mail padrão diferente para um pedido de venda e uma carta de compromisso.


### 1.3. Mais propriedades


* **Ocultar cópia**: esta caixa, quando marcada, restringe um usuário a criar uma 'cópia' de um formulário específico.
* **É Tabela**: Esta opção está disponível apenas durante a personalização dos Formulários que estão presentes em formulários de tabela no sistema. Por exemplo, se você estiver criando uma Tabela de Itens para ser adicionada a um Formulário Personalizado, você pode habilitar esta opção. Confira [Tabela filha](/docs/pt/customize-erpnext/articles/customizing-data-visibility-in-child-table) para obter mais informações.
* **Entrada rápida**: marcar esta caixa permitirá que você crie uma 'Entrada rápida' usando um formulário específico. Isso significa que sempre que um usuário estiver criando este formulário a partir de outro formulário existente, aparecerá uma caixa pop-up que permitirá ao usuário criar o DocType inserindo apenas os detalhes básicos. Por exemplo, verifique Entrada rápida em [Entrada de diário](/docs/pt/accounts/journal-entry#11-quick-entry).
* **Rastrear alterações**: marcar esta caixa garantirá que quaisquer alterações feitas por qualquer um dos usuários neste DocType sejam rastreadas e exibidas.


![Track Changes](/files/customize-track-changes.png)
* **Rastrear visualizações**: esta opção fornecerá uma trilha de todas as visualizações para este DocType específico.
* **Permitir repetição automática**: esta opção, se marcada, permitirá que você habilite a repetição automática de um DocType periodicamente. Por exemplo, se houver um pedido de venda que deve ser feito várias vezes, você pode ativar esta opção e [Configurar Repetição Automática](/docs/pt/automation/auto-repeat) para qualquer Pedido de Venda específico.
* **Permitir importação**: esta opção permitirá ao usuário importar dados de qualquer arquivo. Confira [Ferramenta de importação de dados](/docs/pt/setting-up/data/data-import) para obter mais informações.
* **Mostrar pop-up de visualização**: essa opção foi introduzida na versão 12. Se marcada, um pequeno pop-up aparecerá ao passar o mouse sobre os links desse tipo de documento (na exibição de lista e em outros campos de link). Este pop-up conterá os campos obrigatórios do documento e os campos para os quais `in_preview` é verificado. Confira [Visualização do link](https://erpnext.com/version-12/release-notes/features#link-preview) para obter mais informações.


Depois de clicar em Atualizar, suas personalizações serão atualizadas no formulário.


### 1.2. Personalizando os Campos


Cada formulário no SOMA possui um conjunto padrão de campos. Se você precisa capturar alguma informação, mas não há um campo padrão disponível para isso, você pode inserir um Campo Personalizado em um formulário conforme sua necessidade. Adicionar, editar ou excluir campos também pode ser feito aqui. Você também pode colocar os campos conforme sua necessidade no formulário, adicionando-o abaixo ou acima de qualquer outro campo já presente. [Clique aqui](/docs/pt/customize-erpnext/custom-field) para obter mais informações sobre campos personalizados.


## 2. Vídeos




