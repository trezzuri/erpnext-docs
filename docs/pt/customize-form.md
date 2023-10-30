# Personalizar formulário




**Personalizar formulário é uma ferramenta que permite fazer alterações em um tipo de formulário ou tipo de documento (DocType) no front-end.**


Permite inserir [Campos personalizados](/docs/pt/customize-erpnext/custom-field) conforme sua necessidade ou personalizar as propriedades dos campos padrão .


Antes de nos aventurarmos a aprender a ferramenta de personalização de formulários, [clique aqui](/docs/pt/customize-erpnext/doctype) para entender a arquitetura dos formulários no ERPNext . Isso ajudará você a usar a ferramenta Personalizar formulário com mais eficiência.


Para acessar o Formulário Personalizado, acesse:


> Home > Personalização > Personalização de formulário > Personalizar formulário


Você também pode acessar a visualização de lista de qualquer tipo de documento e selecionar Personalizar nas opções do menu.


![Personalizar opção na visualização de lista](/files/customize-option-in-list-view.png)


## 1. Como personalizar um formulário


1. Clique em Personalizar formulário.
2. Você será redirecionado para uma página onde será solicitado que você insira o tipo de formulário.
3. Depois de inserir o tipo de formulário neste campo, a página se expandirá ainda mais e você poderá ver vários recursos.


![Selecione DocType no formulário personalizado](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. Opções ao personalizar um formulário


1. **Alterar rótulo**: este campo é obtido por meio da tradução personalizada. Você pode alterar o nome do campo de acordo com seu setor/idioma. Por exemplo, se você é uma empresa de serviços e deseja alterar o rótulo de 'Cliente' para 'Consumidor', o mesmo pode ser feito via [Tradução Personalizada](/docs/pt/setting-up/print/custom-translations) e o mesmo será refletido aqui.


![Alterar rótulo](/files/customize-customize-form-label.png)
2. **Campo Título**: Este campo pode ser usado para gerar o título durante a visualização das listas. Qualquer campo do tipo "Dados" pode ser definido como Campo de Título durante a visualização dos formulários na visualização de lista. Por exemplo, se você deseja visualizar a lista de todos os seus funcionários com o campo Título como 'Código do Funcionário' em vez do Nome do Funcionário, o mesmo pode ser configurado aqui. Confira nosso artigo sobre [Título do documento](/docs/pt/customize-erpnext/document-title) para obter mais informações.


*Saiba mais sobre os tipos de campos [aqui](/docs/pt/customize-erpnext/articles/field-types.html).*
3. **Formato de impressão padrão**: para um único DocType, pode haver vários formatos de impressão. Aqui você pode selecionar o formato de impressão padrão para o DocType selecionado. Por exemplo, uma empresa pode ter diferentes papéis timbrados para diferentes finalidades, que podem ser configurados através de formatos de impressão. No entanto, você pode selecionar dois formatos de impressão padrão diferentes para um pedido de vendas e uma carta de compromisso. Verifique [Formatos de impressão personalizados](/docs/pt/customize-erpnext/print-format) para obter mais informações.
4. **Campo de imagem**: você pode selecionar um campo "Anexar imagem" para seu campo de imagem. Esta se torna a imagem que representa aquele DocType específico. Por exemplo, o 'Campo de Imagem' de um Funcionário pode ser a sua fotografia ou um instantâneo dos seus cartões de identificação; o mesmo pode ser configurado aqui.


![Campo de imagem em DocType](/files/customize-form-image-field.png)
5. **Max Attachments**: você pode inserir o número máximo de anexos que podem ser adicionados a este DocType.
6. **Campos de pesquisa**: ao criar qualquer DocType, você pode querer vincular um campo específico a outro DocType. Para facilitar a seleção, você também pode garantir que consegue ver o valor de outro campo do último DocType no resultado da pesquisa. Para obter mais informações, [clique aqui](/docs/pt/customize-erpnext/articles/search-record-by-specific-field).
7. **Classificar campo**: Os registros em qualquer lista DocType são gerados com base no campo que você definiu em Classificar campo aqui. Por exemplo, para Itens, se quiser que sua lista seja gerada de acordo com o Nome do Item, você pode configurar o mesmo aqui.


![Classificar campo](/files/customize-sort-field.png)
8. **Ordem de classificação**: Você pode selecionar se deseja que a classificação seja feita em ordem crescente ou decrescente. Para obter mais compreensão sobre classificação de campo e ordem de classificação, consulte  [Personalização da ordem de classificação na visualização de lista](/docs/pt/customize-erpnext/articles/customizing-sorting-order-in-the-list-view).
9. **Modelo de email padrão**: para um único DocType, pode haver vários  [Modelos de e-mail](/docs/pt/setting-up/email/email-template). Aqui você pode definir o modelo de email padrão para o DocType selecionado. Por exemplo, você pode definir um modelo de e-mail padrão diferente para um pedido de vendas e uma carta de agendamento.


### 1.3. Mais propriedades


* **Ocultar cópia**: esta caixa, quando marcada, restringe um usuário a criar uma 'Cópia' de um formulário específico.
* **É Tabela**: Esta opção está disponível apenas durante a personalização dos Formulários que estão presentes nos formulários tabela do sistema. Por exemplo, se você estiver criando uma Tabela de Itens para ser adicionada a um Formulário Personalizado, você pode ativar esta opção. Confira [Tabela-filho](/docs/pt/customize-erpnext/articles/customizing-data-visibility-in-child-table) para obter mais informações.
* **Entrada Rápida**: Marcar esta caixa permitirá que você crie uma 'Entrada Rápida' usando um formulário específico. Isso significa que sempre que um usuário criar este formulário a partir de outro formulário existente, uma caixa aparecerá que permitirá ao usuário criar o DocType inserindo apenas os detalhes baticos. Por exemplo, verifique Entrada rápida em [Entrada de diário](/docs/pt/accounts/journal-entry#11-quick-entry).
* **Rastrear alterações**: marcar esta caixa garantirá que quaisquer alterações feitas por qualquer um dos usuários neste DocType serão rastreadas e exibidas.


![Rastrear alterações](/files/customize-track-changes.png)
* **Rastrear visualizações**: esta opção fornecerá um rastreamento de todas as visualizações desse DocType específico.
* **Permitir repetição automática**: esta opção, se marcada, permitirá que você ative a repetição automática de um DocType periodicamente. Por exemplo, se houver um pedido de vendas que precisa ser feito várias vezes, você pode ativar esta opção e então [Configurar Repetição automática](/docs/pt/automation/auto-repeat) para qualquer pedido de vendas específico.
* **Permitir importação**: Esta opção permitirá ao usuário importar dados de qualquer arquivo. Confira a [Ferramenta de importação de dados](/docs/pt/setting-up/data/data-import) para obter mais informações.
* **Mostrar pop-up de visualização**: esta opção foi introduzida na versão 12. Se marcada, um pequeno pop-up aparecerá ao passar o mouse sobre links deste tipo de documento (na visualização de lista e em outros campos de link). Este pop-up conterá os campos obrigatórios do documento e os campos para os quais `in_preview` está marcado. Confira [Visualização do link](https://erpnext.com/version-12/release-notes/features#link-preview) para obter mais informações.


Depois de clicar em Atualizar, suas personalizações serão atualizadas no formulário.


### 1.2. Personalizando os campos


Todo formulário no ERPNext possui um conjunto padrão de campos. Caso precise capturar alguma informação, mas não exista um campo padrão disponível para isso, você pode inserir Campo Personalizado em um formulário conforme sua necessidade. Adicionar, editar ou excluir Campos também pode ser feito aqui. Você também pode colocar os campos conforme sua necessidade no formulário, adicionando-os abaixo ou acima de quaisquer outros campos já presentes. [Clique aqui](/docs/pt/customize-erpnext/custom-field) para obter mais informações sobre campos personalizados.


## 2. Vídeos






