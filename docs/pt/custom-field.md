# Campo personalizado



**Todo formulário no ERPNext possui um conjunto padrão de campos. Se você precisar capturar alguma informação, mas não houver um campo padrão disponível para isso, você pode inserir um campo personalizado em um formulário conforme sua necessidade.**


Você pode ir para [Personalizar formulário](/docs/pt/customize-erpnext/customize-form) e adicionar o campo em um formulário específico ou tipo de documento *(doravante denominado DocType)* .


Para acessar o campo personalizado, acesse:


> Home > Personalização > Personalização de formulário > Campo personalizado


Você também pode acessar a visualização de lista de qualquer tipo de documento e selecionar Personalizar nas opções do menu.


![Personalizar opção na visualização de lista](/files/customize-option-in-list-view.png)


## 1. Como criar um campo personalizado


1. Vá para a lista Campos personalizados e clique em Novo.
2. **Documento**: selecione o documento no qual você deseja adicionar o campo personalizado.
3. **Rótulo**: insira qual rótulo você gostaria de atribuir ao seu campo personalizado.
4. **Tipo de Campo**: O ERPNext já possui um conjunto de Tipos de Campo definidos que podem ser obtidos neste menu suspenso. Você pode selecionar o tipo do seu campo personalizado neste menu.
5. Atualizar.


![Novo campo personalizado](/files/new-custom-field.png)


*Saiba mais sobre os tipos de campo [aqui](/docs/pt/customize-erpnext/articles/field-types.html).* 


Você também pode acessar [Personalizar formulário](/docs/pt/customize-erpnext/customize-form) e adicionar, editar ou remover um campo em um determinado Formulário.


![Adicionar campo personalizado do formulário personalizado](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. Detalhes Adicionais


1. **Opções**: Este campo aparece quando você deseja que seus dados sejam específicos ou especifique os dados. Por exemplo, quando você selecionou o campo como 'Campo de seleção', será necessário inserir as opções de seleção aqui.


![Campo personalizado com Fieldtype como Select](/files/custom-field-with-select-fieldtype.png)
2. **Buscar de**: quando desejar que seu campo personalizado seja 'Campo de link', você deverá especificar o formulário ao qual esse campo será vinculado. Por exemplo, você deseja criar um campo personalizado 'Projeto' no DocType 'Item'. Você deverá especificar seu tipo de campo como 'Link' e inserir 'Projeto' no campo Buscar de para garantir que o campo seja atualizado com a lista de todos os DocTypes necessários.
3. **Buscar se vazio**: Esta caixa de seleção garantirá que este campo não será substituído com base em Buscar de se um valor já existir.
4. **Valor padrão**: Insira o valor padrão do campo que você deseja que seja buscado para este campo.
5. **Depende de**: Você pode definir aqui uma condição para que o Campo seja exibido. Por exemplo, no Item DocType, dois campos 'Categoria de Ativo' e 'Série de Nomenclatura de Ativos' só aparecerão se o campo 'É Ativo Fixo' estiver marcado. A condição de dependência aqui seria `is_fixed_asset`.


![Depende da opção](/files/custom-field-dpends-on.png)
6. **Descrição do campo**: você pode adicionar a descrição do campo aqui, que pode ser exibida abaixo deste campo.


![Descrição do campo personalizado](/files/custom-field-description.png)
7. **Nível de permissão**: Isso permitirá que você especifique quais funções em sua organização poderão editar este campo. Você pode consultar [Permissões baseadas em função](/docs/pt/setting-up/users-and-permissions/role-based-permissions) para obter mais compreensão sobre isso.
8. **Em visualização**: se [Mostrar pop-up de visualização](/docs/pt/customize-erpnext/customize-form#13-more-properties) para o tipo de documento estiver marcado, o Campo será incluído no pop-up que aparece ao passar o mouse sobre os links do tipo de documento (na visualização de lista e em outros campos de link).
9. **Largura**: definirá a largura alocada para este campo durante a visualização do formulário em grade.


### 1.2. Mais propriedades


* **É campo obrigatório**: Esta caixa pode ser marcada se você quiser tornar este campo obrigatório ao enviar um DocType.
* **Único**: Marque esta caixa quando desejar que o valor deste campo seja único. Isto pode ser feito nos casos em que o Campo Personalizado seja para um código ou um Número de Identificação. Por exemplo, código do item no caso do item, número do GST no caso do cliente.
* **Somente leitura**: quando você deseja que este campo seja somente leitura ou não editável. Neste caso, o valor do Campo deverá ser buscado automaticamente em outros campos.
* **Oculto**: marque este campo quando desejar que este campo fique oculto ou para ocultar um campo existente.
* **Imprimir Ocultar**: Nos casos em que você deseja que o botão Imprimir fique oculto no Formato de Impressão. Confira [Campos em formato de impressão](/docs/pt/customize-erpnext/articles/making-fields-visible-in-print-format) para obter mais informações. li>
* **Sem cópia**: marcar esta caixa restringirá a cópia deste campo no DocType.
* **Permitir ao enviar**: Isso permitirá que você faça alterações no campo mesmo depois de enviar o formulário. Confira [Editando valor no documento enviado](/docs/pt/customize-erpnext/articles/allow-fields-to-be-changed-after-submission) para obter mais informações .
* **Na visualização de lista**: isso tornará o campo visível na visualização de lista do DocType.
* **No filtro padrão**: o campo se tornará um filtro padrão na visualização de lista do documento.
* **Na Pesquisa Global**: Quando esta caixa está marcada, este campo pode ser pesquisado na Pesquisa Global.
* **Negrito**: Isso deixará este tipo de campo em negrito, agregando mais valor ao campo.
* **Ocultar relatório**: este campo não ficará visível nos relatórios quando você marcar esta caixa.
* **Ignorar filtro XSS**: Isso permitirá que você visualize este campo sem as tags HTML.
* **Traduzível**: quando esta caixa está marcada, ela se torna traduzível ao aplicar  [Traduções personalizadas](/docs/pt/setting-up/print/custom-translations) para isso.


## 2. Vídeos






