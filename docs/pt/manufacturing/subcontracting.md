# Subcontratação



**Na subcontratação, você emprega uma parte externa para realizar tarefas para sua organização, especialmente a manufatura.**

A subcontratação é um tipo de contrato de trabalho que busca terceirizar certos tipos de trabalho para outras empresas. Ele permite que o trabalho em mais de uma fase do projeto seja feito ao mesmo tempo, muitas vezes levando a uma conclusão mais rápida.

A subcontratação é praticada por vários setores. Por exemplo, fabricantes que fabricam vários produtos a partir de componentes complexos subcontratam determinados componentes e os embalam em suas instalações.

Se o seu negócio envolve a terceirização de determinados processos para um fornecedor terceirizado onde você fornece as matérias-primas e o terceiro parte faz o trabalho/produção, você pode acompanhar isso usando o recurso de subcontratação do ERPNext.

## 1. Como configurar a subcontratação

1. Criar um item de serviço (item sem estoque). Representa o custo do serviço da operação subcontratada.

![service itemb2929d](/files/service-itemb2929d.png)![]()
2. Criar itens separados para o produto não processado e o produto processado. Por exemplo, se você fornecer X sem pintura ao seu Fornecedor e o Fornecedor lhe devolver X, você poderá criar dois Itens: “X sem pintura” e “X”.
3. Crie um Armazém para o seu fornecedor para que você possa acompanhar os itens fornecidos. (Você pode fornecer itens para um mês de uma só vez).
4. Para o item processado, no cadastro de itens, habilite “Fornecer matéria-prima para compra”.

![fg item](/files/fg-item.png)![]()

### 1.1 Criando uma BOM

Faça uma [lista de materiais](/docs/pt/manufacturing/bill-of-materials) para o item processado, com os itens não processados ​​como sub-Unid. Vamos considerar um exemplo simples, onde você fabrica uma caneta. A caneta processada será nomeada na Lista de Materiais (BOM), enquanto a ponta, plástico, tinta, etc. serão categorizados como subitens.

Esta BOM estará sem Operações se todas o trabalho de produção é feito por terceiros. Vejamos com um exemplo simples de Assembly de CPU:

![bom items](/files/bom-items.png)![]()  


### 1.2 Criando um pedido de compra

 Faça um pedido de compra de subcontratação para o item de serviço e selecione o item de produto acabado, aquele para o qual você criou uma lista técnica.

1. Ative a opção "É subcontratado" desde este pedido de compra é para subcontratação.

![po is subcontracted](/files/po-is-subcontracted.png)![]()
2. Aqui o valor do campo Taxa da tabela Itens no Pedido de Compra será o custo do serviço que você concordou com o terceiro ou com o Fornecedor.

![po items](/files/po-items.png)![]()
3. Depois de preencher os detalhes, salve e envie o [Ordem de compra](/docs/pt/buying/purchase-order#35-raw-materials-supplied).

### 1.3 Criando um pedido de subcontratação

Faça um pedido de subcontratação para o pedido de compra por clicando em Criar > Pedido de Subcontratação. Ao “Salvar”, na seção “Matérias Primas Fornecidas”, todos os seus Itens não processados ​​serão atualizados com base na sua Lista de Materiais. Você também pode selecionar o Armazém no qual as matérias-primas seriam reservadas para subcontratação em Armazém de Reserva.

![create sco from po](/files/create-sco-from-po.gif)![]()  


 1. Os custos envolvidos no processo de subcontratação deverão ser registrados no campo Taxa da tabela Itens no Pedido de Subcontratação mostrado a seguir:

![sco all item tabelas](/files/sco-all-item-tables.png)![]()
2. Na imagem anterior, estamos fornecendo ao subcontratado os seguintes itens:


	* 8 placas-mãe
	* 8 processadores
	* 16 RAMs
	* 8 discos rígidos
	* 8 gabinetes
	
	O custo de uma CPU incluindo matérias-primas e custos de serviço é 1.02.994 e o custo total para todas as CPUs é 8,23.952![sco itens row qty rate](/files/sco-items-row-qty-rate.png)![]()
3. Em um pedido de subcontratação, selecione as matérias-primas a serem transferidas para o subcontratado:

![se send to subcontractor](/files/se-send-to-subcontractor.gif)![]()
4. Depois que o pedido de subcontratação for enviado, você também poderá visualizar a quantidade reservada do item no painel de itens.

![item dashboard](/files/item-dashboard.png)![]()

### 1.4 Criando entrada de estoque para transferência de matéria-prima

Agora que a matéria-prima está reservada, faça uma entrada de estoque e entregue os itens da matéria-prima para seu Fornecedor.

No Pedido de Subcontratação, clique em Transferir > Material para Fornecedor. Defina os armazéns de origem e de destino. A Entrada de Estoque será do tipo ‘Enviar para Subcontratado’ onde você transfere de um Armazém para outro. Marque 'Da BOM', selecione a BOM, insira a quantidade e clique no botão Obter itens.

![se submit](/files/se-submitted.png)![]()  


### 1.5 Criando um recibo de subcontratação para receber os itens acabados e sucateados.

Receba os itens do seu fornecedor usando um recibo de subcontratação. Você precisa entrar no Armazém do Fornecedor de onde serão retiradas as matérias-primas e os produtos acabados serão recebidos no Armazém Aceito. Considere isso como um backflush para subcontratação.

Clique em Criar > Recibo de subcontratação do pedido de subcontratação. Defina os Armazéns Aceitos e do Fornecedor. Certifique-se de verificar a “Quantidade Consumida” na tabela “Matérias Primas” para que o estoque correto seja mantido no final do Fornecedor. Você precisa selecionar o Armazém do Fornecedor onde receberá os produtos acabados.

Os itens de sucata são obtidos da Lista de Materiais (BOM) escolhida para Produtos Acabados na tabela Itens. A Quantidade é calculada usando a Quantidade do Item de Produto Acabado, enquanto a Taxa é determinada pela Taxa de Avaliação ou pela Taxa de Sucata especificada na BOM.

![scr itens consumidos](/files/scr-consumed-items.png)![]()  


### 1.6 Criando um recibo de compra

De volta ao pedido de compra, clique em Criar > Recibo de compra. Não haverá efeito no Razão de Estoque e no Razão Contábil, pois tanto o Razão de Estoque quanto o Razão Contábil são atualizados quando você envia o Recibo de Subcontratação. Caso você tenha "Impostos e Encargos de Compra", o Razão Contábil será atualizado de acordo.

### 1.7 Matéria-prima de origem do fornecedor

Ao criar uma lista técnica para subcontratação, pode haver algumas matérias-primas como porcas e parafusos que os próprios Fornecedores terão que adquirir.

Ao criar uma Entrada de Estoque para "Transferência" de uma Ordem de Subcontratação, esses itens podem ser excluídos um por um, mas é impossível fazê-lo se você tiver mais de 100 itens.

Se alguma matéria-prima for adquirida diretamente pelo Fornecedor, então essa matéria-prima deverá ser incluída na lista técnica.

* Terá valor zero na BOM
* No Pedido de Subcontratação esta matéria-prima não aparecerá em Itens Fornecidos por não ser fornecida
* Além disso, ao criar uma "Transferência", tais itens serão excluídos da Entrada de Estoque

![bom items row originados pelo fornecedor](/files/bom-items-row-sourced-by-supplier.png)![]()

No entanto, o Fornecedor pode optar por incluir os itens fornecidos pelo fornecedor em seu Pedido de Venda enviado a você.

## 2. Notas

* Certifique-se de que a “Taxa” do Item processado seja o custo de processamento/serviço (excluindo o custo da matéria-prima).
* O ERPNext adicionará automaticamente a taxa de matéria-prima para fins de avaliação quando você receber o item acabado em seu estoque.
* O ERPNext irá automaticamente padronizar o 'Armazém Reserva' na Ordem de Subcontratação da BOM. Se não for encontrado na BOM, o padrão será o Armazém padrão definido no Item. Você pode definir o Armazém Reserva padrão para todos os Itens do Pedido de Subcontratação no campo 'Armazém Reserva' na seção Matérias-Primas Fornecidas.

## 3. Tópicos relacionados

1. [Ordem de compra](/docs/pt/buying/purchase-order)
2. [Recibo de compra](/docs/pt/stock/purchase-receipt)
3. [Inspeção de qualidade](https://docs.erpnext.com/docs/user/manual/en/quality-inspeção)


