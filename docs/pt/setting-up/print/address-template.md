# Modelo de endereço


**O modelo de endereço pode armazenar diferentes formatos de endereços com base na região.**


Cada região tem sua forma de definir endereços. Para gerenciar vários formatos de endereço para seus documentos (como cotações, faturas de compra, etc.), você pode criar **Modelos de endereço** por país.


Para acessar o modelo de endereço, acesse:



>
> Página inicial > Configurações > Modelo de endereço
>
>
>


Um modelo de endereço padrão é criado quando você configura o sistema. Você pode editá-lo ou criar um novo modelo. Este modelo padrão será aplicado a todos os países que não possuem um modelo específico.


Considere um cliente dos Estados Unidos onde 'County' faz parte do endereço. Se você definir o condado no modelo de endereço para os Estados Unidos, ele aparecerá no campo de endereço e, portanto, na visualização da impressão. Campos como código PIN podem ser alterados para serem exibidos como CEP e campos como município podem ser adicionados usando modelos de endereço.



>
> O modelo de endereço verifica o campo 'País' no mestre de endereços para aplicar diferentes modelos de endereço às transações.
>
>
>


## 1. Como criar um modelo de endereço


1. Vá para a lista de modelos de endereço e clique em Novo.
2. Selecione um país.
3. Altere o CSS e o Jinja, se necessário.
4. Salve.


### 1.1 Modelagem Jinja


O mecanismo de modelagem é baseado em HTML e no sistema [Jinja Templating](https://jinja.palletsprojects.com/). Todos os campos (incluindo os campos personalizados) estarão disponíveis para a criação do modelo.


Aqui está o modelo Jinja padrão:



```
{% raw %}{{ address_line1 }}<br>
{% if address_line2 %}{{ address_line2 }}<br>{% endif -%}
{{ cidade }}<br>
{% if estado %}{{ estado }}<br>{% endif -%}
{% if pincode %}PIN: {{ pincode }}<br>{% endif -%}
{{ país }}<br>
{% if phone %}Telefone: {{ phone }}<br>{% endif -%}
{% if fax %}Fax: {{ fax }}<br>{% endif -%}
{% if email_id %}E-mail: {{ email_id }}<br>{% endif -%}{% enddraw %}

```

Aqui está um exemplo:


![Print Heading](/files/address-format.png)


### 2. Tópicos Relacionados


1. [Modelo de termos e condições](/docs/v13/user/manual/en/setting-up/print/terms-and-conditions)
2. [Modelo de impressão de cheque](/docs/v13/user/manual/en/setting-up/print/cheque-print-template)