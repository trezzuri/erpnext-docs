# Problema de arredondamento de faturas



  
**Pergunta:**



Na Nota Fiscal de Venda, o texto é impresso com arredondamento mesmo estando desabilitado via Padrões Globais. Nos Padrões Globais sempre é possível Desabilitar Total Arredondado através da seguinte caixa de seleção:
![](/files/OkUOjHx.png)
  

**Respostas:**


Se esta configuração não funcionou para você, você também precisa verificar o mestre da moeda uma vez.
Para fazer isso, digite **Moeda**na barra incrível (Ctrl/Cmd + G). No mestre de moeda, abra a moeda com a qual você está enfrentando o problema:
  

![](/files/l5TqjSq.png)
  

Aqui certifique-se de que o arredondamento esteja definido corretamente. Por exemplo, o menor valor fracionário para INR deve ser 0,01 e não 0,05. Atualize esse valor e, em seguida, atualize a transação.

