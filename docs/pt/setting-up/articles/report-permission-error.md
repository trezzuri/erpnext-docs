# Problemas de erro de permissão


**Pergunta:** O usuário tem funções como Usuário da conta e Gerente da conta atribuídas. Ainda assim, ao acessar o relatório de contas a receber, o usuário recebe uma mensagem de erro de não permissão do mestre do território.


![Reportar erro de permissão](/files/report-permission-1.png)


**Resposta:**


De acordo com o sistema de permissões do ERPNext, para que o Usuário possa acessar um formulário ou relatório, ele(a) deverá ter no mínimo permissão de leitura em todos os campos de link desse formulário/relatório. Como Território é um campo de link no relatório de contas a receber, adicione uma regra de permissão para permitir que o usuário/gerente da conta tenha pelo menos permissão de leitura no mestre do território. Siga as etapas abaixo para resolver esse problema.


1. As funções atribuídas ao usuário são Usuário da conta e Gerente da conta.
2. Conforme indicado na mensagem de erro, o usuário não tinha permissão no mestre do território. De acordo com a permissão padrão, nenhuma das funções acima atribuídas a esse usuário tem permissão no mestre do território.
3. Para resolver esse problema, atribuí permissão de usuário da conta ao mestre de leitura do território.


![Permission Manager](/files/report-permission-2.png)


De acordo com esta atualização de permissão, o usuário deve ser capaz de acessar o relatório de contas a receber sem problemas.

