# Buscar valores de tabelas filhas usando tags Jinja



O modelo Jinja pode ser usado para referenciar qualquer campo em qualquer DocType no ERPNext. Isso pode ser feito simplesmente chamando &lcub;&lcub;doc.field\_name}} em um formato de impressão, onde 'doc.name' é o nome da variável para um determinado campo.


No entanto, esta abordagem não funciona para tabelas filhas dentro de um DocType. Este artigo ajudará você a percorrer e exibir todas as linhas pertencentes a uma tabela filha dentro de qualquer DocType.


**Pré-requisitos**


Exigiríamos o nome da variável da tabela filha no DocType correspondente. Isso pode ser visualizado na seção 'Personalizar formulário' do DocType necessário. O mesmo é ilustrado abaixo


![](/files/f7Xxz1S.png)


Também exigiremos os nomes das variáveis ​​de todos os campos dentro da tabela filha que precisam ser referenciados. Isso pode ser obtido na seção 'Personalizar formulário' da tabela filho correspondente, conforme mostrado abaixo


![](/files/tzloEh2.png)


![](/files/wPB82f0.png)


![](/files/AV0308f.png)


![](/files/CW0oEUo.png)


**Método 1. Exibindo linhas de uma tabela filha em uma lista não ordenada**




{% para linha em doc.items %}

* Código do item: &lcub;&lcub; row.get\\_formatted("item\\_code", doc) }}

Quantidade: &lcub;&lcub; row.get\\_formatted("qty", doc) }}

Taxa: &lcub;&lcub; row.get\\_formatted("taxa", doc) }}

Valor: &lcub;&lcub; row.get\\_formatted("quantia", doc) }}


{% fim para %}



A saída em formato de impressão seria a seguinte


![](/files/lgLjE7u.png)


**Método 2. Exibindo linhas de uma tabela filha como uma tabela**


  


   


  


  


 


 

| Código do item | Quantidade | Taxa | Valor |
| --- | --- | --- | --- |
| &lcub;&lcub;item.item\_code }} | &lcub;&lcub;item.qty}} | &lcub;&lcub;item.rate}} | &lcub;&lcub;item.amount}} |




A saída em formato de impressão seria a seguinte


![](/files/GS00WlC.png)


Este modelo pode ser usado como referência. Quaisquer campos adicionais no campo da tabela filho podem ser obtidos de maneira semelhante, alterando o modelo Jinja.



