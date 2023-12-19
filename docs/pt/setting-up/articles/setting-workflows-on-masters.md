# Definindo fluxos de trabalho em mestres



Os fluxos de trabalho geralmente são definidos em documentos que podem ser enviados. Assim que o documento for aprovado, ele será enviado automaticamente de acordo com o fluxo de trabalho definido. No entanto, às vezes, as empresas têm casos de uso onde há necessidade de aprovação de mestres, como Itens, Preço do Item, Regra de Preço, etc.

  


No ERPNext , esses mestres não podem ser enviados. Assim, mesmo na rejeição, às vezes, eles ainda estão ativos e você pode utilizá-los em transações. Neste artigo, tomamos o exemplo do mestre de itens. Definiremos um fluxo de trabalho simples no Item e o tornaremos ativo somente quando for aprovado. Para fazer isso, siga as etapas abaixo:

  


1) Certifique-se de que o mestre no qual você definirá o fluxo de trabalho tenha uma caixa de seleção Ativar/Desativar. Se não estiver presente por padrão, você precisará criar um por meio do Formulário Personalizado e definir o valor padrão da seguinte forma:

1. 0 se a caixa de seleção estiver "Desativar"
2. 1 se a caixa de seleção for "Ativar"

No nosso caso, o item mestre possui uma caixa de seleção chamada "Desativado". Definimos o valor padrão como 1 no Formulário Personalizado do Item DocType conforme mostrado abaixo.

  


![](/files/ubLZfPq.png)

  


Isso significa que toda vez que um novo item for criado, ele será desabilitado por padrão, a menos que seja aprovado (como pode ser visto na imagem abaixo). 

  


![](/files/yPOQ2fT.png)

  


   


2) Em seguida, defina o Workflow.

  


Na tabela Estados, após aprovação, certifique-se de atualizar o caixa de seleção "Desativado" (ou Ativado) para 0 (ou 1 no caso de ativado), conforme mostrado abaixo.

  


  


![](/files/Qf3QXyo.png)

  


Isso garantirá que sempre que o item for aprovado, o item será automaticamente ativado e você poderá usá-lo em transações.

  


Confira o GIF abaixo para entender o fluxo de trabalho em detalhes:

  
 

![](/files/olzpAk2.gif)



