# Gerenciamento de permissões em nível de campo


A restrição de um campo com base em funções pode ser facilmente configurada usando o nível de permissão, que é exigido pela maioria das organizações. Para definir um **Nível de Perm**, você pode acessar o respectivo formulário e personalizá-lo.


Vamos considerar um cenário em que a organização não deseja que seu Funcionário (Usuário de contas) edite a Taxa do item ao criar uma **Venda** **Fatura**. Para fazer isso, podemos simplesmente tornar o campo **Taxa do item** um *somente leitura*.


  



1. Para conseguir isso, vá para **Personalizar formulário**, selecione DocType como **Fatura de vendas** **Item**, role até o campo **Taxa de item** e expanda-o.


![](/files/6eFVMRc.gif)


  



2. Procure o **Perm Level**, digite o número (0, 1, 2, 3, etc) e *Salve*.


![](/files/6VNnxII.png)


  



3. Uma vez salvo, clique em **Adicionar uma nova regra** no Gerenciador de Permissões de Função e selecione o Tipo de Documento e a Função, no nosso caso, *Contas* *Usuário*, defina o Perm Level como 2 e conceda o acesso Employee Read.


![](/files/jACnHrX.png)


  



É assim que o Gerenciador de Permissões de Função exibirá a Regra recém-criada com Nível de Perm como 2:


![](/files/qCYWDfK.png)


  
 


4. Agora, como você pode ver na Nota Fiscal, o usuário pode apenas ler o campo Taxa do item que será buscado automaticamente na Lista de preços.


![](/files/86CqBf1.png)


  

Para saber mais sobre Perm Level, clique [aqui](https://erpnext.com/docs/user/manual/en/setting-up/articles/managing-perm-level/) e para qualquer assistência adicional, clique [aqui](https://discuss.erpnext.com/).

