# Gerenciando o nível de permissão no Gerenciador de permissões



O nível de permissão é uma forma de reduzir a quantidade de informações visíveis ou alteráveis ​​em um DocType específico para determinados grupos de usuários. Enquanto você pode definir a visibilidade ou a possibilidade de mudança para cada DocType personalizando a regra de permissões específica do DocType, com o nível de permissão você pode alterá-las para seções ou campos específicos.


Em cada documento, você pode agrupar campos por "níveis". Cada grupo de campos ou grupo de campos é indicado por um número único (0, 1, 2, 3 etc.). Um conjunto separado de regras de permissão pode ser aplicado a cada grupo de campos. Por padrão, todos os campos são de nível 0.


O nível de permissão (forma abreviada de nível de permissão) para um campo pode ser definido em [Personalizar formulário](/docs/pt/customize-erpnext/customize-form.html).


![Campo de nível de permissão](/files/perm-level-1.gif)


Se você precisar atribuir permissões diferentes de um campo específico a usuários diferentes, poderá fazê-lo por meio do Nível de permissão. Vamos considerar um exemplo para melhor compreensão.


A Nota de Entrega pode ser acessada tanto pelo Gerente de Estoque quanto pelo Usuário de Estoque. Você não deseja que o Usuário do Estoque acesse o campo relacionado ao Valor na Nota de Entrega, mas outro campo deve estar visível da mesma forma que está visível no Gerenciador de Estoque.


Para todos os campos relacionados, que não devem ser vistos, você pode definir o nível de permissão como (digamos) 2.


Para Gerentes de Estoque, eles terão permissão nos campos da Nota de Entrega com Nível de Permissão 2, enquanto um Usuário de Estoque não terá nenhuma permissão no Nível de Permissão 2 para Nota de Entrega, porque sua função não foi atribuída com uma regra que os permita ler ou escrever em campo com nível de permissão 2, conforme mostrado abaixo.


![Regra de nível de permissão](/files/perm-level-2.png)


Considerando o mesmo cenário, se você deseja que um usuário do Stock acesse um campo no Perm Nível 2, mas não deseja dar permissão para editá-lo, o usuário do Stock receberá permissão para poder ler apenas no Perm Nível 2, mas não para escrever/editar.


![Regra de nível de permissão 2](/files/perm-level-3.png)


Os níveis de permissão (1, 2, 3 ou 2, 1, 3 ou 3,2,1) não precisam estar em nenhuma ordem específica. Eles não implicam hierarquia. O nível de permissão é usado principalmente para agrupar vários campos e, em seguida, atribuir permissão às funções desse grupo. Portanto, você pode definir qualquer nível de permissão para um item e, em seguida, definir a permissão para ele.


Se quiser alterar as permissões de todos os campos de uma seção, basta alterar o nível de permissão do campo da seção e ele será aplicado a todos os campos da seção.




