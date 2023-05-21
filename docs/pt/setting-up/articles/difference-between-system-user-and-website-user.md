# Diferença entre usuário do sistema e usuário do site


**Pergunta:** Adicionei meu funcionário como usuário e também atribuí funções a ele. Ainda assim, eles não conseguem visualizar o Dashboard no login.


**Responder:**


Existem dois tipos de Usuários no ERPNext.


* **Usuário do Sistema**: São Funcionários da sua empresa. Exemplo de funções atribuídas aos usuários do sistema são: usuário da conta, gerente de vendas, usuário de compras, equipe de suporte, etc.
* **Usuário do Site**: São as partes (como Cliente e Fornecedores) de sua Empresa.


Exemplos de funções de usuário do site são Cliente e Fornecedores.


Como verificar se a função é para usuário do sistema ou usuário do site?


No mestre de funções, se o campo "Acesso à mesa" estiver marcado, essa função é para o usuário do sistema. Se o campo Acesso à área de trabalho estiver desmarcado, essa função é para o usuário do site.


![Permissão do Role Desk](/files/role-deskperm.png)