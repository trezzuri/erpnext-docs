# Campo customizado


**Cada formulário no ERPNext possui um conjunto padrão de campos. Se você precisa capturar alguma informação, mas não há um campo padrão disponível para isso, você pode inserir um campo personalizado em um formulário de acordo com sua necessidade.**


Você pode ir para [Personalizar formulário](/docs/v13/user/manual/en/customize-erpnext/customize-form) e adicionar o campo em um determinado formulário ou tipo de documento *(doravante referido como DocType)* .


Para acessar o Campo Personalizado, acesse:



>
> Home > Personalização > Personalização de formulário > Campo personalizado
>
>
>


Você também pode ir para a exibição de lista de qualquer DocType e selecionar Personalizar nas opções do Menu.


![Personalizar opção na exibição de lista](/files/customize-option-in-list-view.png)


## 1. Como criar um campo personalizado


1. Vá para a lista Campo personalizado e clique em Novo.
2. **Documento**: Selecione o documento no qual você precisa adicionar o campo personalizado.
3. **Rótulo**: Digite qual Rótulo você gostaria de dar ao seu Campo Personalizado.
4. **Tipo de Campo**: O ERPNext já possui um conjunto de Tipos de Campo definidos que podem ser buscados neste menu drop-down. Você pode selecionar o tipo de seu campo personalizado neste menu.
5. Atualização.


![Novo campo personalizado](/files/new-custom-field.png)


*Saiba mais sobre os tipos de campo [aqui](/docs/v13/user/manual/en/customize-erpnext/articles/field-types.html).*


Você também pode ir para [Personalizar formulário](/docs/v13/user/manual/en/customize-erpnext/customize-form) e adicionar, editar ou remover um campo em um formulário específico.


![Adicionar campo personalizado a partir do formulário personalizado](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. detalhes adicionais


1. **Opções**: Este campo aparece quando você deseja que seus dados sejam específicos ou especifique os dados. Por exemplo, quando você selecionou o campo para ser um 'Selecionar campo', será necessário inserir as opções de seleção aqui.


![Campo personalizado com tipo de campo selecionado](/files/custom-field-with-select-fieldtype.png)
2. **Fetch From**: Quando você quiser que seu campo personalizado seja 'Link Field', será necessário especificar o formulário ao qual esse campo será vinculado. Por exemplo, você deseja criar um campo personalizado 'Projeto' no DocType 'Item'. Você deve especificar seu tipo de campo como 'Link' e inserir 'Projeto' no campo Buscar de para garantir que o campo seja atualizado com a lista de todos os DocTypes necessários.
3. **Fetch If Empty**: Esta caixa de seleção garantirá que este campo não seja substituído com base em Fetch From se um valor já existir.
4. **Valor Padrão**: Insira o valor padrão do Campo que você deseja que seja obtido para este Campo.
5. **Depende**: Aqui você pode definir uma condição para que o Campo seja exibido. Por exemplo, no Item TipoDoc, dois campos 'Categoria do Ativo' e 'Série de Nomenclatura do Ativo' só aparecerão se o Campo 'É Ativo Fixo' estiver marcado. A condição de dependência aqui seria `is_fixed_asset`.


![Depende da opção](/files/custom-field-dpends-on.png)
6. **Descrição do Campo**: Você pode adicionar a descrição do Campo aqui que pode ser exibida abaixo deste Campo.


![Descrição do campo personalizado](/files/custom-field-description.png)
7. **Nível de permissão**: Isso permitirá que você especifique quais funções dentro de sua organização poderão editar este campo. Você pode acessar [Permissões baseadas em função](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions) para entender melhor isso.
8. **Em visualização**: Se [Mostrar pop-up de visualização](/docs/v13/user/manual/en/customize-erpnext/customize-form#13-more-properties) para o tipo de documento estiver marcado, o Campo será incluído no pop-up que aparece ao passar o mouse sobre os links do tipo de documento (na exibição de lista e outros campos de link).
9. **Largura**: Isso definirá a largura alocada para este Campo durante a visualização do Formulário em uma Visualização em Grade.


### 1.2. Mais propriedades


* **É um campo obrigatório**: Esta caixa pode ser marcada se você deseja tornar este campo obrigatório ao enviar um DocType.
* **Único**: Marque esta caixa quando quiser que o valor deste Campo seja único. Isso pode ser feito nos casos em que o Campo Personalizado é para um código ou um Número de Identificação. Por exemplo, Código do Item no caso de Item, Número GST no caso de Cliente.
* **Read Only**: Quando você deseja que este campo seja somente leitura ou um campo não editável. Neste caso, o valor do Campo deve ser obtido automaticamente de outros campos.
* **Oculto**: Marque este Campo quando desejar que este Campo fique oculto ou para ocultar um Campo existente.
* **Imprimir Ocultar**: Nos casos em que você deseja que o botão de impressão fique oculto no Formato de impressão. Confira [Campos em formato de impressão](/docs/v13/user/manual/en/customize-erpnext/articles/making-fields-visible-in-print-format) para obter mais informações.
* **Sem cópia**: marcar esta caixa restringirá a cópia deste campo no DocType.
* **Permitir ao enviar**: Isso permitirá que você faça alterações no campo mesmo depois de enviar o formulário. Confira [Editando valor no documento enviado](/docs/v13/user/manual/en/customize-erpnext/articles/allow-fields-to-be-changed-after-submission) para obter mais informações.
* **Na exibição de lista**: Isso tornará o campo visível na exibição de lista do DocType.
* **No filtro padrão**: O campo se tornará um filtro padrão na exibição de lista do documento.
* **Na Pesquisa Global**: Quando esta caixa está marcada, este Campo pode ser pesquisado na Pesquisa Global.
* **Negrito**: Isso tornará o tipo de campo em negrito, isso agrega mais valor ao campo.
* **Report Hide**: Este campo não ficará visível nos relatórios quando você marcar esta caixa.
* **Ignorar filtro XSS**: Isso permitirá que você visualize este campo sem as tags HTML.
* **Traduzível**: Quando esta caixa está marcada, torna-se traduzível ao aplicar [Traduções Personalizadas](/docs/v13/user/manual/en/setting-up/print/custom-translations) para isso.


## 2. Vídeos