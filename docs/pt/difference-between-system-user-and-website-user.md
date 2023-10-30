# Diferença entre usuário do sistema e usuário do site



**Pergunta:** adicionei meu funcionário como usuário e também atribuí funções a ele. Ainda assim, eles não conseguem visualizar o Dashboard no login.


**Resposta:**


Existem dois tipos de usuários no ERPNext.


* **Usuário do Sistema**: São Funcionários da sua empresa. Exemplos de funções atribuídas aos usuários do sistema são usuário de conta, gerente de vendas, usuário de compras, equipe de suporte etc.
* **Usuário do Site**: São partes (como Clientes e Fornecedores) de sua Empresa.


Exemplos de funções de usuário de site são Cliente e Fornecedores.


Como verificar se a função é para usuário do sistema ou usuário do site?


No mestre de funções, se o campo "Acesso à mesa" estiver marcado, essa função é para usuário do sistema. Se o campo Acesso ao balcão estiver desmarcado, então essa função é para o usuário do site.


![Permissão do Role Desk](/files/role-deskperm.png)



