# Excluir transações da empresa



**Você pode excluir todos os dados de transação, como faturas de vendas e pedidos de vendas associados a uma empresa, e começar do zero, mantendo intactos os outros dados mestre, como clientes, itens e listas técnicas.**Freqüentemente, os usuários configuram todos os dados mestre e depois criam alguns registros fictícios. Então eles querem excluir os registros fictícios e a empresa e começar tudo de novo. Isto pode ser feito de duas maneiras:

## 1. Ferramenta de exclusão de transações

Este recurso permite excluir todos os registros associados à empresa especificada, exceto aqueles pertencentes aos DocTypes listados na tabela **DocTypes excluídos**.

Tenha cuidado ao usar isso-os registros, uma vez excluídos com isso, nunca poderão ser recuperados. Mas se tiver certeza de que deseja recomeçar, siga estas etapas:

1. Crie um novo documento "Registro de exclusão de transação".
2. Insira o nome da empresa cujos registros você deseja excluir.
3. Modifique a tabela "Tipos de documentos excluídos", se necessário.
4. Salvar e enviar.

E pronto, sua empresa está como nova.

![Transaction Deletion Record](/files/Transaction Deletion Recordeea199.png)![]()

A tabela **Resumo** exibe os nomes dos DocTypes cujos registros foram excluídos, bem como o número de registros que foram excluídos.

## 2. Excluir transações

1. Vá para **Home > Contabilidade > Empresa** e encontre sua empresa.
2. No no canto superior direito, você encontrará o botão **Excluir transações** em **Gerenciar**.
3. Digite sua senha.
4. Insira o nome da empresa para confirmar.

![Excluir transações](/files/Delete Transactions.png)![]()  


Isso enviará um registro no DocType do registro de exclusão de transação.

![Mensagem de exclusão bem-sucedida](/files/Exclusão bem-sucedida Message.png)![]()  


### Observação:

 Para realizar esta ação, o usuário deve ter a função de Gerente do Sistema.





