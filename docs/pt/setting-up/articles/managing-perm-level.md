# Gerenciando o nível de permissão no gerenciador de permissões


Perm Level é uma maneira de reduzir a quantidade de informações visíveis ou alteráveis ​​em um DocType específico para determinados grupos de usuários. Enquanto você pode definir visibilidade ou capacidade de alteração para cada DocType personalizando a regra de permissões específica do DocType, com o nível de permissão, você pode alterá-los para seções ou campos específicos.


Em cada documento, você pode agrupar campos por "níveis". Cada grupo de campos ou grupo de campos é indicado por um número único (0, 1, 2, 3 etc.). Um conjunto separado de regras de permissão pode ser aplicado a cada grupo de campos. Por padrão, todos os campos são de nível 0.


O nível de permissão (forma abreviada de nível de permissão) para um campo pode ser definido em [Personalizar formulário< /a>.](/docs/pt/customize-erpnext/customize-form.html)


![Perm Level Field](/files/perm-level-1.gif)


Se você precisar atribuir diferentes permissões de determinado campo a diferentes usuários, poderá fazê-lo por meio do Perm Level. Vamos considerar um exemplo para melhor compreensão.


A Nota de Entrega está acessível tanto para o Gerente de Estoque quanto para o Usuário de Estoque. Você não deseja que o Usuário do Estoque acesse o campo relacionado ao Valor na Nota de Entrega, mas outro campo deve estar visível da mesma forma que está visível no Gerenciador de Estoque.


Para todos os campos relacionados, que não devem ser vistos, você pode definir Perm Level como (digamos) 2.


Para Gerentes de Estoque, eles terão permissão nos campos da Nota de Entrega com Perm Nível 2, enquanto um Usuário de Estoque não terá nenhuma permissão no Perm Nível 2 para Nota de Entrega, porque sua função não foi atribuída com uma regra que os permita para ler ou escrever no Campo com Nível Perm de 2, conforme mostrado abaixo.


![Perm Level Rule](/files/perm-level-2.png)


Considerando o mesmo cenário, se você deseja que um Usuário do Stock acesse um campo no Perm Nível 2, mas não deseja dar permissão para editá-lo, o Usuário do Stock receberá permissão para ler apenas no Perm Nível 2, mas não para escrever/editar.


![Perm Level Rule 2](/files/perm-level-3.png)


Os níveis permanentes (1, 2, 3 ou 2, 1, 3 ou 3,2,1) não precisam estar em nenhuma ordem específica. Não implicam hierarquia. O nível de permissão é usado principalmente para agrupar o número de campos e, em seguida, atribuir permissão a funções para esse grupo. Portanto, você pode definir qualquer nível de permissão para um item e, em seguida, fazer a configuração de permissão para ele.


Se você quiser alterar as permissões para todos os campos em uma seção, basta alterar o nível de perm para o campo da seção e ele será aplicado a todos os campos da seção.


