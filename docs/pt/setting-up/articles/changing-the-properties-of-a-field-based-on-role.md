# Gerenciamento de permissão em nível de campo


A restrição de um campo com base em Funções pode ser facilmente configurada usando o Perm Level, que é exigido pela maioria das organizações. Para definir um **Perm Level**, você pode acessar o respectivo formulário e personalizá-lo.


Vamos considerar um cenário em que a organização não deseja que seu funcionário (usuário de contas) edite a taxa do item ao criar uma **fatura** de **vendas**. Para fazer isso, podemos simplesmente tornar o campo **Item Rate** um *read-only*.


  



1. Para conseguir isso, vá para **Customize Form**, selecione DocType como **Sales Invoice** **Item**, role até o campo **Item Rate** e expanda-o.


![](/files/6eFVMRc.gif)


  



2. Pesquise o **Perm Level**, digite o número (0, 1, 2, 3, etc) e *Salve*.


![](/files/6VNnxII.png)


  



3. Uma vez salvo, clique em **Add a New Rule** no Role Permission Manager e selecione o Document Type e o Role, no nosso caso, *Accounts* *User*, defina o Perm Level como 2 e conceda o Employee Read acesso.


![](/files/jACnHrX.png)


  



É assim que o Gerenciador de Permissões de Função exibirá a Regra recém-criada com Nível de Perm como 2:


![](/files/qCYWDfK.png)


  
 


4. Agora, como você pode ver na Nota Fiscal de Venda, o usuário pode ler apenas o campo Taxa do item que será buscado automaticamente na Tabela de preços.


![](/files/86CqBf1.png)


  

Para saber mais sobre Perm Level, clique [aqui](https://erpnext.com/docs/user/manual/en/setting-up/articles/managing-perm-level/) e para qualquer assistência adicional, clique [aqui ](https://discuss.erpnext.com/).