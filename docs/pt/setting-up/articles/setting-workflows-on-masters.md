# Configurando fluxos de trabalho em mestres


Os fluxos de trabalho geralmente são definidos em documentos submissíveis. Depois que o documento é aprovado, ele é enviado automaticamente de acordo com o fluxo de trabalho definido. No entanto, às vezes, as empresas têm casos de uso em que há necessidade de aprovação de mestres, como itens, preço do item, regra de preços etc.

  


No ERPNext , esses mestres não podem ser enviados. Assim, mesmo na rejeição, às vezes, eles ainda estão ativos e você pode usá-los em transações. Neste artigo, tomamos o exemplo do mestre de itens. Vamos definir um fluxo de trabalho simples no Item e torná-lo ativo somente quando for aprovado. Para fazer isso, siga as etapas abaixo:

  


1) Certifique-se de que o mestre no qual você definirá o fluxo de trabalho tenha uma caixa de seleção Ativar/Desativar. Se isso não estiver presente por padrão, você precisará criar um por meio do Formulário Personalizado e definir o valor padrão da seguinte forma:

1. 0 se a caixa de seleção for "Desativar"
2. 1 se a caixa de seleção for "Ativar"

No nosso caso, o mestre de itens possui uma caixa de seleção chamada "Desativado". Definimos o valor padrão como 1 no Formulário Personalizado do Item DocType, conforme mostrado abaixo.

  


![](/files/ubLZfPq.png)

  


Isso significa que toda vez que um novo item for criado, ele será desabilitado por padrão, a menos que seja aprovado (como visto na captura de tela abaixo). 

  


![](/files/yPOQ2fT.png)

  


   


2) Em seguida, defina o fluxo de trabalho.

  


Na tabela Estados, após a aprovação, certifique-se de atualizar o Caixa de seleção "Desativado" (ou Ativado) para 0 (ou 1 no caso de ativado) conforme mostrado abaixo.

  


  


![](/files/Qf3QXyo.png)

  


Isso garantirá que, sempre que o Item for aprovado, ele será ativado automaticamente e você poderá usá-lo em transações.

  


Confira o GIF abaixo para entender o fluxo de trabalho em detalhes:

  
 

![](/files/olzpAk2.gif)

