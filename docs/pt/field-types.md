# Tipos de campo



A seguir estão os tipos de campos que você pode definir ao criar novos ou ao alterar os campos padrão.


#### Link


O campo Link está conectado a outro mestre de onde busca dados. Por exemplo, no mestre de cotações, o campo Cliente é um link. Para saber mais, [clique aqui](/docs/pt/customize-erpnext/articles/creating-custom-link-field).


#### Link Dinâmico


O campo Link Dinâmico é aquele que pode pesquisar e reter o valor de qualquer documento/tipo de documento. [Clique aqui](/docs/pt/customize-erpnext/articles/dynamic-link-fields) para saber como funciona o campo de link dinâmico.


#### Verificar


Isso permitirá que você tenha uma caixa de seleção aqui.


![Verificar tipo de campo](/files/field-type-check.png)


#### Selecionar


Selecionar será um campo suspenso. Você pode adicionar vários resultados no campo Opção, separados por linha.


![Selecionar tipo de campo](/files/field-type-select.png)


#### Tabela


Uma tabela será uma espécie de campo Link que renderiza outro DocType dentro do formulário atual. Por exemplo, a Tabela de Itens no Pedido de Vendas é um campo de Tabela vinculado ao DocType do Item do Pedido de Vendas.


![Tipo de campo de tabela](/files/field-type-table.png)


#### Anexar


Anexar campo permite que você navegue em um campo do Gerenciador de Arquivos e anexe o mesmo aqui.


![Anexar tipo de campo](/files/field-type-attach.png)


#### Anexar imagem


Anexar imagem é um campo onde você poderá anexar imagens no formato jpeg, png, etc. Esta se torna a imagem que representa aquele DocType específico. Por exemplo, se você quiser a imagem de um item em seu DocType, você pode escolher seu campo para ser um campo de imagem anexado.


![Field Type Image](/files/field-type-image.png)


#### Editor de Texto


Editor de Texto é um campo de texto. Possui opções de formatação de texto. No ERPNext, este campo é geralmente usado para definir Termos e Condições.


![Editor de texto de tipo de campo](/files/field-type-text-editor.png)


#### Data


Este campo permitirá que você insira a data neste campo.


![Tipo de campo Data](/files/field-type-date.png)


#### Data e hora


Este campo fornecerá um seletor de data e hora. A data e a hora atuais (conforme fornecidas pelo seu computador) são definidas por padrão.


![Tipo de campo data e hora](/files/field-type-date-and-time.png)


#### Código de barras


Neste campo, você pode especificar o campo como Código de barras, o que permitirá inserir um número de código de barras. Depois de fazer isso, o código de barras será gerado automaticamente em relação ao número.


![Código de barras do tipo de campo](/files/field-type-barcode.png)


#### Botão


Este tipo de campo será um botão de ação, como Salvar, Enviar, etc.


![Botão de tipo de campo](/files/field-type-button.png)


#### Código


Se o tipo de campo for selecionado como código, você poderá inserir um código no campo.


![Código do tipo de campo](/files/field-type-code.png)


#### Cor


Você terá a opção de especificar a cor deste formulário.


![Cor do tipo de campo](/files/field-type-colour.png)


#### Quebra de coluna


Como o ERPNext possui vários layouts de coluna, usando Quebras de Coluna, você pode dividir um conjunto de campos em no máximo duas colunas.


![Quebra de coluna do tipo de campo](/files/field-type-column-break.png)


#### Moeda


O campo Moeda contém valores numéricos, como Preço do Item, Valor, etc. O campo Moeda pode ter valores de até seis casas decimais. Além disso, você pode exibir um símbolo de moeda no campo de moeda.


![Tipo de campo Moeda](/files/field-type-currency.png)


#### Dados


O campo de dados será um campo de texto simples. Ele permite inserir um valor de até 140 caracteres, tornando este o tipo de campo mais genérico. Para ativar validações para entradas de e-mail, nome ou número de telefone, defina as opções como "E-mail", "Nome", "Telefone" em Configurações > DocType.


![Dados do tipo de campo](/files/field-type-data.png)


#### Flutuante


O campo flutuante carrega um valor numérico, com até nove casas decimais. A precisão do campo flutuante é definida em [Definir precisão](/docs/pt/customize-erpnext/articles/set-precision)


> Configuração > Configurações > Configurações do sistema


A configuração será aplicável a todos os campos flutuantes.


![Tipo de campo Float](/files/field-type-float.png)


#### Geolocalização


Use o campo Geolocalização para armazenar GeoJSON [feature\_collection](https://tools.ietf.org/html/rfc7946#section-3.3). Armazena polígonos, linhas e pontos. Internamente, ele usa as seguintes propriedades personalizadas para identificar um círculo.


Leia o [campo de geolocalização](/docs/pt/customize-erpnext/articles/geolocation-field) para entender melhor.


![Geolocalização do tipo de campo](/files/field-type-geolocation.png)


#### HTML


Você pode selecionar o campo como HTML quando quiser que os dados sejam inseridos no formato HTML.


![Tipo de campo HTML](/files/field-type-html.png)


#### Imagem


O campo de imagem renderizará um arquivo de imagem selecionado em outro campo de anexo.


Para o campo Imagem, em Opção (no Doctype), deverá ser fornecido um nome de campo onde o arquivo de imagem está anexado. Ao referir-se ao valor nesse campo, a imagem será uma referência no campo Imagem.


![Field Type Image](/files/field-type-image2.png)


#### Int (Inteiro)


O campo inteiro contém valor numérico, sem casa decimal.


![Tipo de campo inteiro](/files/field-type-integer.png)


#### Texto pequeno


O campo Texto pequeno contém conteúdo de texto e tem mais limite de caracteres do que o campo Dados.


![Tipo de campo Texto pequeno](/files/field-type-small-text.png)


#### Texto longo


Você pode definir seu campo como um campo de texto longo quando desejar inserir dados com um limite ilimitado de caracteres.


![Tipo de campo Texto longo](/files/field-type-long-text.png)


#### Texto


Este tipo de campo permite adicionar texto no campo. O limite de caracteres nos campos Texto Pequeno, Texto Longo e Texto será determinado com base no Sistema de Gerenciamento de Banco de Dados Relacional.


![Tipo de campo Text](/files/field-type-text.png)


#### Editor de Markdown


Este campo permitirá que você adicione o texto em linguagem de marcação.


![Editor de marcação de tipo de campo](/files/field-type-markdown-editor.png)


#### Senha


O campo de senha terá um valor decodificado.


![Senha do tipo de campo](/files/field-type-password.png)


#### Porcentagem


Você pode definir o campo como um campo Porcentagem que, em segundo plano, será calculado como uma porcentagem.


![Porcentagem de tipo de campo](/files/field-type-percent.png)


#### Classificação


Você pode definir o campo como um campo Taxa que, em segundo plano, será calculado como Classificação.


![Classificação do tipo de campo](/files/field-type-rating.png)


#### Somente leitura


O campo Somente leitura carregará dados obtidos de outro formulário que não serão editáveis. Você deve definir Somente leitura como tipo de campo se a origem do valor for predeterminada.


![Tipo de campo somente leitura](/files/field-type-read-only.png)


#### Quebra de seção


A quebra de seção é usada para dividir o formulário em várias seções.


![Quebra de seção do tipo de campo](/files/field-type-section-break.png)


#### Assinatura


Você pode definir o campo como um campo de Assinatura onde você pode adicionar a Assinatura Digital neste campo. Leia a documentação do [Campo de assinatura](/docs/pt/customize-erpnext/articles/signature-field) para saber mais.


#### Multisseleção de tabela


Esta é uma combinação de campos do tipo 'Link' e do tipo 'Tabela'. Em vez de uma tabela secundária com o botão 'Adicionar linha', vários valores podem ser selecionados em um campo.


![Tabela de tipo de campo MultiSelect](/files/field-type-table-multiselect.png)


#### Tempo


Este é um campo Hora onde você pode definir a Hora no campo.


![Field Type Time](/files/field-type-time.png)


#### Duração


Você pode usar o campo Duração se quiser definir um intervalo de tempo.


![Duração do tipo de campo](/files/field-type-duration.png)


Se não quiser monitorar a duração em termos de dias ou segundos, você pode ativar as opções "Ocultar dias" e "Ocultar segundos", respectivamente, em seu formulário.


![Opções de duração do tipo de campo](/files/field-type-duration-options.png)


Esta é a aparência do campo de duração após as alterações acima.


![Duração do tipo de campo](/files/field-type-duration2.png)



