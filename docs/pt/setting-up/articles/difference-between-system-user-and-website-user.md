# Diferença entre usuário do sistema e usuário do site


**Pergunta:** Adicionei meu funcionário como usuário e também atribuí funções a ele. Ainda assim, eles não conseguem visualizar o painel no login.


**Resposta:**


Existem dois tipos de usuários no ERPNext.


* **Usuário do Sistema**: São Funcionários da sua empresa. Exemplo de funções atribuídas a usuários do sistema: usuário da conta, gerente de vendas, usuário de compras, equipe de suporte, etc.
* **Usuário do site**: são as partes (como Cliente e Fornecedores) de sua Empresa.


Exemplos de funções de usuário do site são Cliente e Fornecedores.


Como verificar se a função é para usuário do sistema ou usuário do site?


No mestre de função, se o campo "Acesso à mesa" estiver marcado, essa função é para o usuário do sistema. Se o campo Desk Access estiver desmarcado, essa função é para o usuário do site.


![Permissão do Role Desk](/files/role-deskperm.png)

