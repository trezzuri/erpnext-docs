# Tipos de campo


A seguir estão os tipos de campos que você pode definir ao criar novos ou ao corrigir os padrões.


#### Link


O campo Link está conectado a outro mestre de onde busca os dados. Por exemplo, no mestre de cotações, o campo Cliente é um link. Para saber mais, [clique aqui](/docs/v13/user/manual/en/customize-erpnext/articles/creating-custom-link-field).


#### Link Dinâmico


O campo Dynamic Link é aquele que pode pesquisar e manter o valor de qualquer documento/doctype. [Clique aqui](/docs/v13/user/manual/en/customize-erpnext/articles/dynamic-link-fields) para saber como funciona o Dynamic Link Field.


#### Verificar


Isso permitirá que você tenha uma caixa de seleção aqui.


![Check Field TYpe](/files/field-type-check.png)


#### Selecione


Selecione será um campo suspenso. Você pode adicionar vários resultados no campo Opção, separados por linha.


![Selecione o tipo de campo](/files/field-type-select.png)


#### Mesa


Uma tabela será uma espécie de campo Link que renderiza outro DocType dentro do formulário atual. Por exemplo, a tabela de itens no pedido de venda é um campo de tabela vinculado ao tipo de documento do item do pedido de venda.


![Tipo de campo de tabela](/files/field-type-table.png)


#### Anexar


Anexar campo permite que você navegue em um campo do Gerenciador de Arquivos e anexe o mesmo aqui.


![Anexar tipo de campo](/files/field-type-attach.png)


#### Anexar Imagem


Anexar imagem é um campo no qual você poderá anexar imagens no formato jpeg, png, etc. Isso se torna a imagem que representa esse tipo de documento específico. Por exemplo, você deseja a imagem de um Item em seu DocType, você pode escolher seu campo para ser um campo Anexar imagem.


![Imagem do tipo de campo](/files/field-type-image.png)


#### Editor de texto


Editor de texto é um campo de texto. Possui opções de formatação de texto. No ERPNext, este campo geralmente é utilizado para definição de Termos e Condições.


![Editor de texto de tipo de campo](/files/field-type-text-editor.png)


#### Data


Este campo permitirá que você insira a Data neste campo.


![Data do tipo de campo](/files/field-type-date.png)


#### Data e hora


Este campo fornecerá um seletor de data e hora. A data e hora atuais (fornecidas pelo seu computador) são definidas por padrão.


![Data e hora do tipo de campo](/files/field-type-date-and-time.png)


#### Código de barras


Neste campo, você pode especificar o campo como Código de barras, o que permitirá inserir um número de código de barras. Depois de fazer isso, o código de barras seria gerado automaticamente em relação ao número.


![Código de barras do tipo de campo](/files/field-type-barcode.png)


#### Botão


Este tipo de campo será um botão de ação, como Salvar, Enviar, etc.


![Botão de tipo de campo](/files/field-type-button.png)


#### Código


Se o Tipo de campo for selecionado como código, você poderá inserir um Código no campo.


![Código do tipo de campo](/files/field-type-code.png)


#### Cor


Você terá a opção de especificar a cor para este Formulário.


![Cor do tipo de campo](/files/field-type-colour.png)


#### Quebra de Coluna


Como o ERPNext possui múltiplos layouts de colunas, utilizando Column Breaks, você pode dividir um conjunto de campos em no máximo duas colunas.


![Quebra de coluna do tipo de campo](/files/field-type-column-break.png)


#### Moeda


O campo Moeda contém valores numéricos, como Preço do Item, Valor, etc. O campo Moeda pode ter valores de até seis casas decimais. Além disso, você pode ter um símbolo de moeda sendo mostrado para o campo de moeda.


![Moeda do tipo de campo](/files/field-type-currency.png)


#### Dados


O campo de dados será um campo de texto simples. Ele permite inserir um valor de até 140 caracteres, tornando este o tipo de campo mais genérico. Para habilitar validações para entradas de e-mail, nome ou número de telefone, defina as opções para "E-mail", "Nome", "Telefone" em Configurações > Tipo de documento.


![Dados do tipo de campo](/files/field-type-data.png)


#### Flutuar


O campo float carrega um valor numérico, até nove casas decimais. A precisão do campo flutuante é definida por meio de [Definir precisão](/docs/v13/user/manual/en/customize-erpnext/articles/set-precision)



>
> Configuração > Configurações > Configurações do sistema
>
>
>


A configuração será aplicável em todo o campo float.


![Field Type Float](/files/field-type-float.png)


#### Geolocalização


Use o campo Geolocation para armazenar GeoJSON [feature\_collection](https://tools.ietf.org/html/rfc7946#section-3.3). Armazena polígonos, linhas e pontos. Internamente, ele usa as seguintes propriedades personalizadas para identificar um círculo.


Leia [Campo de geolocalização](/docs/v13/user/manual/en/customize-erpnext/articles/geolocation-field) para entender melhor.


![Geolocalização do tipo de campo](/files/field-type-geolocation.png)


#### HTML


Você pode selecionar o campo para ser um campo HTML quando desejar que os dados sejam inseridos no formato HTML.


![Tipo de campo HTML](/files/field-type-html.png)


#### Imagem


O campo de imagem renderizará um arquivo de imagem selecionado em outro campo anexado.


Para o campo Imagem, em Opção (em Doctype), deve ser fornecido um nome de campo onde o arquivo de imagem está anexado. Ao referenciar o valor naquele campo, a imagem será uma referência no campo Imagem.


![Imagem do tipo de campo](/files/field-type-image2.png)


#### Int (Inteiro)


O campo inteiro contém valor numérico, sem casa decimal.


![Field Type Integer](/files/field-type-integer.png)


#### Texto Pequeno


O campo de texto pequeno contém conteúdo de texto e tem mais limite de caracteres do que o campo de dados.


![Field Type Small Text](/files/field-type-small-text.png)


#### Texto Longo


Você pode definir seu campo para um campo de texto longo quando desejar inserir dados com um limite de caracteres ilimitado.


![Field Type Long Text](/files/field-type-long-text.png)


#### Texto


Este tipo de campo permitiria que você adicionasse texto no campo. O limite de caracteres nos campos Texto Pequeno, Texto Longo e Texto será determinado com base no Sistema de Gerenciamento de Banco de Dados Relacional.


![Field Type Text](/files/field-type-text.png)


#### Editor de remarcações


Este campo permitirá que você adicione o texto em linguagem de marcação.


![Editor de markdown de tipo de campo](/files/field-type-markdown-editor.png)


#### Senha


O campo de senha terá um valor decodificado nele.


![Field Type Password](/files/field-type-password.png)


#### Porcentagem


Você pode definir o campo como um campo de Porcentagem que, em segundo plano, será calculado como uma porcentagem.


![Porcentagem do tipo de campo](/files/field-type-percent.png)


#### Avaliação


Você pode definir o campo como um campo Taxa que em segundo plano será calculado como Classificação.


![Classificação do tipo de campo](/files/field-type-rating.png)


#### Somente leitura


O campo Somente leitura carregará os dados obtidos de outro formulário que não serão editáveis. Você deve definir Somente leitura como tipo de campo se a origem do valor for predeterminada.


![Tipo de campo somente leitura](/files/field-type-read-only.png)


#### Quebra de seção


A quebra de seção é usada para dividir o formulário em várias seções.


![Quebra de seção de tipo de campo](/files/field-type-section-break.png)


#### Assinatura


Você pode definir o campo para ser um campo de assinatura no qual você pode adicionar a assinatura digital neste campo. Leia a documentação para [Campo de assinatura](/docs/v13/user/manual/en/customize-erpnext/articles/signature-field) para saber mais.


#### Seleção Múltipla de Mesa


Esta é uma combinação de campos do tipo 'Link' e do tipo 'Tabela'. Em vez de uma tabela filha com o botão 'Adicionar linha', vários valores podem ser selecionados em um campo.


![Field Type Table MultiSelect](/files/field-type-table-multiselect.png)


#### Tempo


Este é um campo de Hora onde você pode definir a Hora no campo.


![Field Type Time](/files/field-type-time.png)


#### Duração


Você pode usar o campo Duração se quiser definir um intervalo de tempo.


![Duração do tipo de campo](/files/field-type-duration.png)


Se você não deseja rastrear a duração em termos de dias ou segundos, pode ativar as opções "Ocultar dias" e "Ocultar segundos", respectivamente, em seu formulário.


![Opções de duração do tipo de campo](/files/field-type-duration-options.png)


É assim que o campo de duração fica após as alterações acima.


![Duração do tipo de campo](/files/field-type-duration2.png)