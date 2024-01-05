# Alocação de turnos de ativos



O recurso Alocação de turnos de ativos permite alterar os turnos de um ativo (com [depreciação de turno](https://docs.erpnext.com/docs/user/manual/en/asset-asset#3-1-depreciação:~:text=Depreciate%20based%20on%20shifts) habilitada) para um determinado período e os turnos restantes são ajustados automaticamente pelo sistema.

Vamos ver um exemplo.

A seguir está o cronograma de depreciação de um ativo com depreciação por turnos ativada, método de depreciação como linha reta, número total de depreciações como 12 e frequência de depreciação como 1. Todos os turnos eram únicos por padrão e as entradas de depreciação foram feitas para os primeiros 5 meses.

![](/files/00creuc.png)![]()

Aqui estão os fatores de mudança definidos:

![](/files/WXQYhRA.png)![ ]()  


Em seguida, iremos para o tipo de documento Alocação de turno de ativos, inseriremos o nome do ativo e salvaremos. O cronograma de depreciação atual é obtido para que possamos editar os turnos. Vamos alterar o deslocamento da 6ª linha para Triplo.

![](/files/HZDN3lo.png)![]()  


Quando você clica em salvar após alterar, observe que a última linha é removida automaticamente para preservar o número total de turnos.

![](/files/RgfAzrs.png)![]()  


Se você tivesse alterado o deslocamento na 6ª linha para Duplo, o deslocamento na última linha teria mudado para Metade.

Quando tiver certeza sobre o cronograma de depreciação criado, clique em enviar e um novo cronograma de depreciação será gerado para o ativo.



