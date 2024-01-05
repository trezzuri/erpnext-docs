# Criando relatórios personalizados



Existem três tipos de relatórios no ERPNext.


### 1. Criador de relatórios


Report Builder é uma ferramenta de personalização de relatórios embutida no ERPNext. Isto permite definir campos específicos do formulário que serão adicionados ao relatório. Além disso, você pode definir os filtros necessários, classificar e dar o nome preferido ao relatório.






### 2. Relatório de consulta


O Relatório de Consulta é escrito em SQL que extrai valores do banco de dados da conta e os exibe no relatório. Embora as consultas SQL possam ser escritas no front end, como HTML, elas foram restritas para usuários da nuvem ERPNext. Isso ocorre porque permite que usuários sem acesso a um relatório específico busquem dados diretamente do banco de dados.


Verifique o relatório Item do pedido de compra a ser recebido no módulo Estoque, por exemplo, um relatório de consulta. [Clique aqui](https://frappeframework.com/docs/user/en/desk/reports/query-report) para saber como criar um relatório de consulta.


### 3. Relatório de roteiro


Os relatórios de script são escritos em Python e armazenados no lado do servidor. São relatórios complexos que envolvem lógica e cálculo. Como esses relatórios são escritos no lado do servidor, não é possível personalizá-los a partir de uma conta hospedada.


Verifique o relatório Análise Financeira no módulo Contas para ver um exemplo de Relatório de Script. [Clique aqui](https://frappeframework.com/docs/user/en/desk/reports/script-report) para saber como criar um relatório de script.


> Observação: o **Filtro Dinâmico** está disponível em Relatórios de Script e Relatórios de Consulta; entretanto, não no Report Builder.




