# Título do documento



**Você pode personalizar o título dos documentos com base nas propriedades para ter informações significativas para as visualizações de lista.**


Por exemplo, o título padrão em uma cotação é o nome do cliente, mas se você estiver lidando com apenas alguns clientes e enviando muitas cotações para cada cliente, talvez você queira personalizar.


![Título do documento](/files/document-title.png)


## Definindo campos de título


A partir do ERPNext Versão 6.0, todas as transações possuem uma propriedade 'Título'. Se não houver uma propriedade de título, você poderá adicionar um **Campo personalizado** como título e definir o **Campo de título** por meio de **Personalizar formulário**.


Você pode definir o valor padrão dessa propriedade usando formatação de string no estilo Python em **Padrão** ou **Opções**


1. Para editar um título padrão, vá para Personalizar formulário
2. Selecione o formulário cujo campo de título você deseja alterar.
3. Edite o **campo de título** no formulário.


## Definindo títulos


Você pode definir o título definindo as propriedades do documento entre colchetes `{}`. Por exemplo, se o seu documento tiver campos `customer_name`, você poderá especificá-lo como o título do formulário.


![Definir título do documento](/files/set-document-title.gif)


Como alternativa, você também pode definir um campo específico como o 'Campo de título' em Personalizar formulário.


![Title Field](/files/title-field-in-view-settings.png) 


## Títulos fixos ou editáveis


Se o seu título for gerado como padrão, ele poderá ser editado pelo usuário clicando no cabeçalho do documento.


![Título editável](/files/customize-document%20title.gif)


Se quiser um título fixo, você pode definir a regra na propriedade **Opções**. Desta forma, o título será atualizado automaticamente sempre que o documento for atualizado.



