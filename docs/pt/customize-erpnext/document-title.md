# Título do Documento


**Você pode personalizar o título dos documentos com base nas propriedades para ter informações significativas para as exibições de lista.**


Por exemplo, o título padrão em uma cotação é o nome do cliente, mas se você estiver lidando com apenas alguns clientes e enviando muitas cotações para cada cliente, você pode personalizar.


![Document Title](/files/document-title.png)


## Definindo campos de título


A partir da versão 6.0 do SOMA, todas as transações possuem uma propriedade 'Título'. Se não houver uma propriedade de título, você pode adicionar um **Campo personalizado** como título e definir o **Campo de título** por meio de **Personalizar formulário**.


Você pode definir o valor padrão dessa propriedade usando a formatação de string estilo Python em **Padrão** ou **Opções**


1. Para editar um título padrão, vá para Personalizar formulário
2. Selecione o formulário para o qual deseja alterar o campo de título.
3. Edite o **Campo do título** no formulário.


## Definindo títulos


Você pode definir o título definindo as propriedades do documento entre chaves `{}`. Por exemplo, se seu documento tiver os campos `customer_name`, você poderá especificá-los como o título do formulário.


![Definir título do documento](/files/set-document-title.gif)


Como alternativa, você também pode definir um campo específico como o 'Campo de título' em Personalizar formulário.


![Title Field](/files/title-field-in-view-settings.png) 


## Títulos fixos ou editáveis


Se o seu título for gerado como um título padrão, ele poderá ser editado pelo usuário clicando no título do documento.


![Título editável](/files/customize-document%20title.gif)


Se você deseja um título fixo, pode definir a regra na propriedade **Opções**. Desta forma, o título será atualizado automaticamente toda vez que o documento for atualizado.

