# Subcontratação no ERPNext



A subcontratação é uma modalidade de contrato de trabalho que busca **terceirizar** determinados tipos de trabalho para outras empresas. Ele permite que o trabalho em mais de uma fase do projeto seja realizado ao mesmo tempo, muitas vezes levando a uma conclusão mais rápida. É praticado por vários setores.

  


Por exemplo, os fabricantes que fabricam vários produtos a partir de componentes complexos subcontratam determinados componentes e os embalam em suas instalações.  


![](/files/Uqloysk.png)

  
Se o seu negócio envolve a terceirização de certos processos para um fornecedor terceirizado, onde você fornece as matérias-primas e o terceiro faz a mão de obra/produção, você pode acompanhar isso usando o recurso de subcontratação do ERPNext.  


**Como gerenciar a subcontratação no ERPNext?**

  


Para demonstrar a terceirização, estamos considerando o cenário abaixo:

Um fabricante de flores produz flores cruas e sem cor. Estas flores são embaladas em caixas (1 caixa = 1000 flores) e enviadas para coloração a um fornecedor externo.

  


1. No Cadastro de Itens do item subcontratado, certifique-se de ter habilitado a opção “Fornecer Matéria Prima para Compra”. Em nosso exemplo, o item é "Flor colorida RM-111"

  


![](/files/Dizzv7h.png)

  


2. Crie uma BOM (lista de materiais) para o item subcontratado e inclua as matérias-primas que você envia ao subcontratado para obter o produto acabado/semi-acabado. Não haverá operações nesta BOM, pois as atividades não são realizadas no final do fabricante. Em nosso exemplo, a lista técnica de RM-111-Colored-Flower é a seguinte:

  


![](/files/0r4KFFG.png) 

  


3. Agora, você precisa criar o Pedido de Compra para adquirir este Item do fornecedor/fornecedor externo. Certifique-se de selecionar "Sim" para o campo "Fornecer Matérias-Primas" e, em seguida, selecione o armazém do qual as matérias-primas serão transferidas para o fornecedor. Observe que este também pode ser um armazém virtual apenas para servir de espaço reservado para fazer a entrada de estoque ao transferir materiais para o fornecedor. Abaixo está o pedido de compra conforme nosso exemplo:

  


![](/files/NoFO0T4.png)

  


Nota: A taxa do Item inserido aqui será a sua taxa de Custo de Serviço.

  


4. Há também outra tabela secundária que mostra o status das matérias-primas a serem transferidas contra esta Ordem de Compra. Nessa tabela, é necessário selecionar o “Armazém Reserva” de onde as matérias-primas serão transferidas para o armazém virtual do fornecedor que selecionamos no passo anterior. Esta tabela também informa quantos itens já foram fornecidos, no nosso caso é zero, pois ainda não enviamos o pedido e fornecemos a matéria-prima.

  


![](/files/5gxQbu3.png)

  


5. Após o envio do Pedido de Compra, haverá um botão “Transferir” para criação do Lançamento de Estoque para transferência de matéria-prima para o fornecedor externo:

  


![](/files/SYPIUEq.png)

  


![](/files/aJ3pBPd.png)

  


![](/files/rQcvSYZ.png)

Depois que a entrada de estoque for enviada, a tabela filha no pedido de compra também será atualizada para refletir a quantidade transferida em "Quantidade fornecida"

  


![](/files/srrSyG5.png)

  


6. Assim como quando você recebe os produtos semiacabados/acabados do fornecedor, você pode criar um recibo de compra com base neste pedido de compra:

  


![](/files/xbWLQp2.png)

  


  


As próximas etapas para faturamento seguem o ciclo de compra normal.

Ordem de compra-> Recibo de compra-> Fatura de compra.

  


7. Fatura de compra criada para esta transação: (Visualização do formato de impressão)

  


![](/files/2b1Rvbr.png)

  


  


Para saber mais sobre o módulo Compras, consulte nossa documentação [aqui](https://erpnext.com/docs/usuário/manual/en/compra).









