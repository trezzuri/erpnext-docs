# Personalizar formato de impressão


**Formatos de impressão são os layouts gerados quando você deseja imprimir ou enviar uma transação por e-mail.**


Este recurso é útil para todas as transações no ERPNext, como todas as transações de compra e venda, documentos de RH e muito mais.


No ERPNext, existem três tipos de formatos de impressão, ou seja, formato de impressão padrão, formato de impressão personalizado e formato de impressão HTML.


## Formato de impressão padrão


Cada Tipo de Documento Imprimível no ERPNext terá seu próprio Formato de Impressão Padrão que é gerado pelo Frappe Framework. A colocação dos campos nos Formatos de impressão padrão dependerá da posição dos respectivos campos no documento.


![Formato de impressão padrão](/files/customize-standard-print-format.png)


Quaisquer alterações feitas no Formato de Impressão Padrão deverão ser feitas usando um Formulário Personalizado. Você também pode verificar [adicionar campos em formatos de impressão](/docs/pt/customize-erpnext/articles/making-fields-visible-in-print-format).< /p>
## Formato de impressão personalizado


Você também pode criar seus próprios formatos de impressão personalizados usando uma ferramenta chamada [Construtor de formatos de impressão< /a>. Esta ferramenta irá ajudá-lo a criar um formato de impressão personalizado simples, arrastando e soltando os campos em um formato conforme sua preferência.](/docs/pt/setting-up/print/print-format-builder)


![Personalizar formato de impressão](/files/customize-print-format.gif)


Para criar formatos de impressão personalizados, o ERPNext vem com vários modelos predefinidos em três estilos, a saber, Moderno, Monocromático e Clássico.


Para criar suas versões, abra um modelo existente em:



> 
> Construir > Visualizações > Formato de impressão
> 
> 
> 


## Configurações de impressão


Para editar/atualizar suas configurações de impressão e PDF, acesse:



> 
> Configurações > Configurações de impressão
> 
> 
> 


![Configurações de impressão](/files/print-settings.png)


## Formato de impressão HTML


Para criar um formato de impressão HTML, você precisa de algum conhecimento de HTML, CSS e Python. Aqui está um exemplo de como um formato de impressão pode ser projetado com um formato muito específico.


![Formato de impressão HTML](/files/customize-custom-print-format-1.png)


Formatos de impressão são fornecidos no lado do servidor usando a [Jinja Templating Language](https://jinja.palletsprojects.com/en/3.0.x/templates/). Todos os formulários têm acesso ao objeto doc que contém informações sobre o documento que está sendo formatado. Você também pode acessar utilitários comuns por meio do módulo frappe. Para obter suporte ao criar um formato de impressão baseado em HTML, você pode consultar [Fórum da comunidade ERPNext](https://discuss.erpnext.com/) ou iniciar uma nova postagem para sua consulta.< /p>
Para estilizar, o [Bootstrap CSS Framework](http://getbootstrap.com/) é fornecido e você pode aproveitar toda a gama de classes.


#### Referências


1. [Linguagem de modelagem Jinja: referência](https://jinja.palletsprojects.com/en/3.0.x/templates/)
2. [Bootstrap CSS Framework](http://getbootstrap.com/)


#### Exemplo



```
 {% raw %}### {{ doc.select\_print\_heading or "Invoice" }}


    
 Nome do cliente
 {{ doc.customer\_name }}
 
    
 Data
 {{ doc.get\_formatted("invoice\_date") }}
 

            {%- para linha em doc.items -%}

            {%- endfor -%}
        


 | Sr | Nome do item | Descrição | Quantidade | Taxa | Valor |
| {{ row.idx }} | 
 {{ row.item\_name }}
 {% if row.item\_code != row.item\_name -%}
 Código do item: {{ row.item\_code}}
 {%- fim se %}
  | {{ row.description }} | {{ row.qty }} {{ row.uom or row.stock\_uom }} | {{
 row.get\_formatted("rate", doc) }} | {{
 row.get\_formatted("amount", doc) }} |

 
{% enddraw %}

```

## Notas


1. Para obter valores formatados de data e moeda, use `doc.get_formatted("fieldname")`
2. Para strings traduzíveis, use `{{ '{{ _("This string is translate") }}' }}`




