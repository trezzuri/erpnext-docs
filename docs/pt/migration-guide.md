# Guia de migração



Depois de migrar para a versão 14, provavelmente você usará o aplicativo India Compliance para gerenciar sua conformidade com o GST
Este guia ajudará você com as alterações que talvez você precise fazer na configuração do GST e do plano de contas 


### Cenário 1: você está usando uma única conta GST para todos os tipos, como entrada e saída, e suas configurações de GST na versão 13 são um pouco semelhantes às mostradas abaixo


![conta única](/files/single-account.png)


Ao usar o aplicativo India Compliance, é obrigatório configurar contas separadas para cada tipo. Caso você esteja migrando da versão 13 para a versão 14, você pode atualizar suas contas da seguinte maneira.


Você pode usar suas contas GST atuais com o tipo "Saída" e criar novas contas para os tipos "Entrada" e "Cobrança reversa". Neste caso, suas novas configurações de GST deverão ter a seguinte aparência.


![new settings](/files/new-settings.png)


Agora, caso você ainda queira ver o saldo líquido do GST em uma única conta, um lançamento contábil manual pode ser lançado para mover o saldo para a conta GST de entrada e o saldo final lhe dará o GST a pagar.


###  Cenário 2: você tem várias contas GST com base na taxa ou talvez nos estados e suas configurações de GST são mostradas abaixo


![conta multipe](/files/multipe-account.png)


Todas as suas contas GST deverão ser mescladas em uma única conta. Caso você já esteja usando contas de entrada e saída separadas, mescle as contas para cada tipo e atualize as contas GST para cada tipo.


As contas "Saída CGST 5%" e "Saída CGST 9%" serão mescladas em uma única conta "Saída CGST", o mesmo vale para contas SGST e IGST


Caso você esteja usando várias contas para taxas ou qualquer outro motivo, mas a mesma conta para o tipo "Entrada"(Compra) e "Saída"(Vendas), siga o processo mencionado no Cenário 1 após mesclar todas as contas.



