# Gerenciamento de permissões em nível de campo



A restrição de um campo com base em funções pode ser facilmente configurada usando o nível de permissão, que é exigido pela maioria das organizações. Para definir um **Nível de permissão**, você pode acessar o respectivo formulário e personalizá-lo.


Vamos considerar um cenário em que a organização não deseja que seu funcionário (usuário de contas) edite a taxa do item ao criar uma **fatura** de **vendas**. Para fazer isso, podemos simplesmente tornar o campo **Taxa de item** *somente leitura*.


  



1. Para conseguir isso, vá para **Personalizar Formulário**, selecione DocType como **Fatura de Vendas** **Item**, vá até o campo **Taxa de Item** e expanda-o.


![](/files/6eFVMRc.gif)


  



2. Procure o **Nível de permissão**, digite o número (0, 1, 2, 3, etc) e *Salve*.


![](/files/6VNnxII.png)


  



3. Depois de salvo, clique em **Adicionar uma nova regra** no Role Permission Manager e selecione o tipo de documento e a função, no nosso caso, *Contas* *Usuário*, defina o nível de permissão como 2 e conceda acesso de leitura ao funcionário.


![](/files/jACnHrX.png)


  



É assim que o Gerenciador de permissões de função exibirá a regra recém-criada com nível de permissão 2:


![](/files/qCYWDfK.png)


  
 


4. Agora, como você pode ver na Nota Fiscal de Venda o Usuário poderá apenas ler o campo Taxa do Item que será buscado automaticamente na Lista de Preços.


![](/files/86CqBf1.png)


  

Para saber mais sobre o Perm Level, clique [aqui](https://erpnext.com/docs/user/manual/en/setting-up/articles/managing-perm-level/) e para para obter mais assistência, clique [aqui](https://discuss.erpnext.com/).



