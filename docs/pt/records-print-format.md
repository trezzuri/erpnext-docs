# Personalizar formato de impressão



**Formatos de impressão são os layouts gerados quando você deseja imprimir ou enviar uma transação por e-mail.**


Este recurso é útil para todas as transações no ERPNext, como todas as transações de vendas e compras, documentos de RH e muito mais.


No ERPNext, existem três tipos de Formatos de Impressão, nomeadamente, Formato de Impressão Padrão, Formato de Impressão Personalizado e Formato de Impressão HTML.


## Formato de impressão padrão


Cada tipo de documento imprimível no ERPNext terá seu próprio formato de impressão padrão que é gerado pelo Frappe Framework. A colocação dos campos nos Formatos de Impressão Padrão dependerá da posição dos respectivos campos no documento.


![Formato de impressão padrão](/files/customize-standard-print-format.png)


Quaisquer alterações feitas no formato de impressão padrão deverão ser feitas usando um formulário personalizado. Você também pode verificar [adicionando campos em formatos de impressão](/docs/pt/customize-erpnext/articles/making-fields-visible-in-print-format).


## Formato de impressão personalizado


Você também pode criar seus próprios formatos de impressão personalizados usando uma ferramenta chamada [Print Format Builder](/docs/pt/setting-up/print/print-format-builder). Esta ferramenta irá ajudá-lo a criar um formato de impressão personalizado simples, arrastando e soltando campos em um formato de sua preferência.


![Personalizar formato de impressão](/files/customize-print-format.gif)


Para criar Formatos de Impressão Personalizados, o ERPNext vem com vários modelos pré-definidos em três estilos, nomeadamente, Moderno, Monocromático e Clássico.


Para criar suas versões, abra um modelo existente em:


> Construir > Visualizações > Formato de impressão


## Configurações de impressão


Para editar/atualizar suas configurações de impressão e PDF, acesse:


> Configurações > Configurações de impressão


![Configurações de impressão](/files/print-settings.png)


## Formato de impressão HTML


Para criar um formato de impressão HTML, você precisará de algum conhecimento de HTML, CSS e Python. Aqui está um exemplo de como um formato de impressão pode ser criado com um formato muito específico.


![Formato de impressão HTML](/files/customize-custom-print-format-1.png)


Os formatos de impressão são fornecidos no lado do servidor usando a [Jinja Templating Language](https://jinja.palletsprojects.com/en/3.0.x/templates/). Todos os formulários têm acesso ao objeto doc que contém informações sobre o documento que está sendo formatado. Você também pode acessar utilitários comuns através do módulo frappe. Para obter suporte ao criar um formato de impressão baseado em HTML, você pode consultar o [fórum da comunidade ERPNext](https://discuss.erpnext.com/) ou iniciar uma nova postagem para sua consulta.


Para estilização, o [Bootstrap CSS Framework](http://getbootstrap.com/) é fornecido e você pode aproveitar toda a gama de classes.


#### Referências


1. [Linguagem de modelagem Jinja: referência](https://jinja.palletsprojects.com/en/3.0.x/templates/)
2. [Estrutura CSS Bootstrap](http://getbootstrap.com/)


#### Exemplo



```
 {% raw %}### &lcub;&lcub; doc.select\_print\_heading ou "Fatura" }}



```


Nome do cliente
&lcub;&lcub; doc.customer\_name }}


Data
&lcub;&lcub; doc.get\_formatted("invoice\_date") }}


```
 {%-para linha em doc.items-%}

            {%-endfor-%}
        



```

| Sr. | Nome do item | Descrição | Quantidade | Taxa | Valor |
| --- | --- | --- | --- | --- | --- |
| &lcub;&lcub; row.idx }} | 
 &lcub;&lcub; row.item*nome }}
 {% if row.item*code != row.item*nome-%}
 Código do item: &lcub;&lcub; row.item*code}}
 {%-fim se %}
  | &lcub;&lcub; row.description }} | &lcub;&lcub; row.qty }} &lcub;&lcub; row.uom ou row.stock*uom }}* | &lcub;&lcub;
 row.getformatted("taxa", doc) }} | &lcub;&lcub;
 row.get\_formatted("quantia", doc) }} |



{% sacar %}

## Notas


- Para obter valores formatados em data e moeda, use `doc.get_formatted("fieldname")`

- Para strings traduzíveis, use `&lcub;&lcub; '&lcub;&lcub; _("Esta string está traduzida") }}' }}`






