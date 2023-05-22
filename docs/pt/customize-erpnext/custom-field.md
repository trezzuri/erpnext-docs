# Campo personalizado


**Cada formulário no SOMA possui um conjunto padrão de campos. Se você precisa capturar alguma informação, mas não há um campo padrão disponível para isso, você pode inserir um campo personalizado em um formulário conforme sua necessidade.**


Você pode ir para [Personalizar formulário](/docs/pt/customize-erpnext/customize-form) e adicionar o campo em um determinado formulário ou tipo de documento *(doravante referido como DocType)* .


Para acessar o campo personalizado, acesse:



> 
> Página inicial > Personalização > Personalização de formulário > Campo personalizado
> 
> 
> 


Você também pode ir para a exibição de lista de qualquer DocType e selecionar Personalizar nas opções do Menu.


![Personalizar opção na exibição de lista](/files/customize-option-in-list-view.png)


## 1. Como criar um campo personalizado


1. Vá para a lista Campo personalizado e clique em Novo.
2. **Documento**: selecione o documento no qual você precisa adicionar o campo personalizado.
3. **Rótulo**: insira o rótulo que você gostaria de dar ao seu campo personalizado.
4. **Tipo de Campo**: O SOMA já possui um conjunto de Tipos de Campo definidos que podem ser obtidos a partir deste menu suspenso. Você pode selecionar o tipo de seu campo personalizado neste menu.
5. Atualizar.


![Novo campo personalizado](/files/new-custom-field.png)


*Saiba mais sobre os tipos de campo [aqui](/docs/pt/customize-erpnext/articles/field-types.html).* 


Você também pode ir para [Personalizar formulário](/docs/pt/customize-erpnext/customize-form) e adicionar, editar ou remover um campo em um determinado Formulário.


![Adicionar campo personalizado a partir do formulário personalizado](/files/customize-erpnext-custom-field-from-customize-form.gif)


### 1.1. Detalhes Adicionais


1. **Opções**: Este campo aparece quando você deseja que seus dados sejam específicos ou especifique os dados. Por exemplo, quando você selecionou o campo como 'Selecionar campo', será necessário inserir as opções de seleção aqui.


![Campo personalizado com tipo de campo selecionado](/files/custom-field-with-select-fieldtype.png)
2. **Buscar de**: Quando você quiser que seu campo personalizado seja 'Campo de link', será necessário especificar o formulário ao qual esse campo será vinculado. Por exemplo, você deseja criar um campo personalizado 'Projeto' no DocType 'Item'. Você deve especificar seu tipo de campo como 'Link' e inserir 'Projeto' no campo Buscar de para garantir que o campo seja atualizado com a lista de todos os DocTypes necessários.
3. **Fetch If Empty**: esta caixa de seleção garantirá que este campo não seja substituído com base em Fetch From se um valor já existir.
4. **Valor Padrão**: Insira o valor padrão do Campo que você deseja que seja obtido para este Campo.
5. **Depende de**: Você pode definir aqui uma condição para que o Campo seja exibido. Por exemplo, no Item TipoDoc, dois campos 'Categoria do Ativo' e 'Série de Nomenclatura do Ativo' só aparecerão se o Campo 'É Ativo Fixo' estiver marcado. A condição de dependência aqui seria `is_fixed_asset`.


![Depends On Option](/files/custom-field-dpends-on.png)
6. **Descrição do Campo**: Você pode adicionar a descrição do Campo aqui que pode ser exibida abaixo deste Campo.


![Descrição do campo personalizado](/files/custom-field-description.png)
7. **Nível de permissão**: Isso permitirá que você especifique quais funções em sua organização poderão editar este campo. Você pode acessar [Permissões baseadas em funções](/docs/pt/setting-up/users-and-permissions/role-based-permissions) para entender melhor isso.
8. **Em visualização**: se [Mostrar pop-up de visualização](/docs/pt/customize-erpnext/customize-form#13-more-properties) para o tipo de documento estiver marcado, o campo será incluído no pop-up que aparece ao passar o mouse sobre os links do tipo de documento (na exibição de lista e outros campos de link).
9. **Largura**: Isso definirá a largura alocada para este Campo ao visualizar o Formulário em uma Visualização em Grade.


### 1.2. Mais propriedades


* **É um campo obrigatório**: Esta caixa pode ser marcada se você quiser tornar este campo obrigatório ao enviar um DocType.
* **Exclusivo**: marque esta caixa quando desejar que o valor deste campo seja exclusivo. Isso pode ser feito nos casos em que o Campo Personalizado é para um código ou um Número de Identificação. Por exemplo, código do item no caso de item, número GST no caso de cliente.
* **Somente leitura**: quando você deseja que este campo seja somente leitura ou um campo não editável. Nesse caso, o valor do campo deve ser obtido automaticamente de outros campos.
* **Oculto**: marque este campo quando quiser que este campo fique oculto ou para ocultar um campo existente.
* **Ocultar impressão**: nos casos em que você deseja que o botão de impressão fique oculto no formato de impressão. Confira [Campos em formato de impressão](/docs/pt/customize-erpnext/articles/making-fields-visible-in-print-format) para obter mais informações.
* **Sem cópia**: marcar esta caixa restringirá a cópia deste campo no DocType.
* **Permitir ao enviar**: Isso permitirá que você faça alterações no campo mesmo depois de enviar o formulário. Confira [Editando valor no documento enviado](/docs/pt/customize-erpnext/articles/allow-fields-to-be-changed-after-submission) para obter mais informações .
* **Na exibição de lista**: isso tornará o campo visível na exibição de lista do DocType.
* **No filtro padrão**: o campo se tornará um filtro padrão na exibição de lista do documento.
* **Na pesquisa global**: quando esta caixa está marcada, este campo pode ser pesquisado na pesquisa global.
* **Negrito**: Isso tornará o tipo de campo em negrito, agregando mais valor ao campo.
* **Ocultar relatório**: este campo não ficará visível nos relatórios quando você marcar esta caixa.
* **Ignorar filtro XSS**: Isso permitirá que você visualize este campo sem as tags HTML.
* **Traduzível**: quando esta caixa está marcada, torna-se traduzível ao aplicar  [Traduções personalizadas](/docs/pt/setting-up/print/custom-translations) para isso.


## 2. Vídeos




