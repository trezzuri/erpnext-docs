# Busca valores da tabela filho usando tags Jinja


O modelo Jinja pode ser usado para fazer referência a qualquer campo em qualquer DocType no ERPNext. Isso pode ser feito simplesmente chamando {{doc.field\_name}} em um formato de impressão, onde 'doc.name' é o nome da variável para um determinado campo.


No entanto, essa abordagem não funciona para tabelas filhas dentro de um DocType. Este artigo irá ajudá-lo a percorrer e exibir todas as linhas pertencentes a uma tabela filho dentro de qualquer DocType.


**Pré-requisitos**


Exigiríamos o nome da variável da tabela filha no DocType correspondente. Isso pode ser visualizado na seção 'Personalizar formulário' para o DocType necessário. O mesmo está ilustrado abaixo


![](/files/f7Xxz1S.png)


Também exigiremos os nomes das variáveis ​​de todos os campos dentro da tabela filho que precisam ser referenciados. Isso pode ser obtido na seção 'Personalizar formulário' da tabela filho correspondente, conforme mostrado abaixo


![](/files/tzloEh2.png)


![](/files/wPB82f0.png)


![](/files/AV0308f.png)


![](/files/CW0oEUo.png)


**Método 1. Exibição de linhas de uma tabela filha em uma lista não ordenada**




{% para linha em doc.items %}

* Código do item: {{ row.get\\_formatted("item\\_code", doc) }}

Quantidade: {{ row.get\\_formatted("qty", doc) }}

Taxa: {{ row.get\\_formatted("taxa", doc) }}

Valor: {{ row.get\\_formatted("amount", doc) }}


{% endfor %}



A saída em um formato de impressão seria a seguinte


![](/files/lgLjE7u.png)


**Método 2. Exibindo linhas de uma tabela filha como uma tabela**




| Código do artigo | Quantidade | Taxa | Quantidade |
| --- | --- | --- | --- |
  


{% para item em doc.items %}

| {{item.item\\_code }} | {{item.qty}} | {{item.rate}} | {{item.quantia}} |


{% endfor %}



A saída em um formato de impressão seria a seguinte


![](/files/GS00WlC.png)


Este modelo pode ser usado para referência. Quaisquer campos adicionais no campo da tabela filho podem ser obtidos de maneira semelhante, alterando o modelo Jinja.