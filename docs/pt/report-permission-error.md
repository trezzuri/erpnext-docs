# Problemas de erros de permissão



**Pergunta:** o usuário tem funções atribuídas como usuário da conta e gerente da conta. Ainda assim, ao acessar o relatório de contas a receber, o usuário recebe uma mensagem de erro informando que o mestre do território não tem permissão.


![Erro de permissão de relatório](/files/report-permission-1.png)


**Resposta:**


De acordo com o sistema de permissão do ERPNext, para que o Usuário possa acessar um formulário ou relatório, ele(a) deve ter pelo menos permissão de leitura em todos os campos de link desse formulário/relatório. Como Território é um campo de link no relatório de contas a receber, adicione uma regra de permissão para permitir que o usuário/gerente da conta tenha pelo menos permissão de leitura no mestre de território. Siga as etapas abaixo para resolver esse problema.


1. As funções atribuídas ao usuário são usuário da conta e gerente da conta.
2. Conforme indicado na mensagem de erro, o usuário não tinha permissão no mestre de território. De acordo com a permissão padrão, nenhuma das funções acima atribuídas a esse usuário tem permissão no mestre do território.
3. Para resolver esse problema, atribuí a permissão de usuário da conta ao mestre de leitura do território.


![Gerenciador de permissões](/files/report-permission-2.png)


De acordo com esta atualização de permissão, o usuário deverá ser capaz de acessar o relatório de contas a receber sem problemas.



