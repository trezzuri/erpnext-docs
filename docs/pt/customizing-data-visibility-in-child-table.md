# Visibilidade de dados em tabelas filhas



No ERPNext, existe um recurso chamado grade editável. Isso permite que o usuário adicione valores na tabela filho sem abrir uma caixa de diálogo/formulário para cada linha.


É assim que a tabela Item de Cotação renderiza o valor quando a Grade Editável está habilitada. Terá no máximo quatro colunas na tabela.


![Tabela-filho](/files/customize-child-table-5.png)


De acordo com a configuração padrão, apenas quatro colunas são listadas na tabela filha. Veja a seguir como você pode adicionar mais colunas na própria Grade Editável.


Para que o campo seja adicionado como uma coluna na tabela, insira um valor no campo Coluna. Além disso, certifique-se de que a propriedade "Is List View" esteja marcada para esse campo.


![Tabela-filho](/files/customize-child-table-2.png)


Com base no valor do campo Coluna, colunas serão adicionadas à tabela filha. Certifique-se de que o valor total adicionado no campo Coluna não exceda 10. Com base no valor da Coluna, a largura dessa coluna será definida.


![Tabela-filho](/files/customize-child-table-3.png)


**Mudar para grade não editável**


Para que mais valores sejam mostrados na visualização da tabela Item de cotação, você pode desativar a Grade editável para o DocType do item de cotação. Etapas abaixo.


![Tabela-filho](/files/customize-child-table.gif)


Depois que a Grade Editável estiver desabilitada para o Item de Cotação, os valores serão renderizados em uma visualização da tabela Item de Cotação da seguinte maneira:


![Tabela-filho](/files/customize-child-table-4.png)


Para que o valor de um campo específico seja mostrado na visualização, certifique-se de que para esse campo, na ferramenta Personalizar formulário, a propriedade "Na visualização em lista" esteja marcada.


![Tabela-filho](/files/customize-child-table-1.png)



