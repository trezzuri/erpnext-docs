# Pedido de compra



**Um Pedido de Compra é um contrato vinculativo com seu Fornecedor no qual você promete comprar um conjunto de itens sob determinadas condições.**


É semelhante a um pedido de vendas, mas em vez de enviá-lo para uma parte externa, você o mantém em registros internos.


> Home > Compra > Compra > Pedido de Compra


![Fluxo de compra](/files/buying_flow_po.png)


## 1. Pré-requisitos


Antes de criar e usar um Pedido de Compra, é aconselhável que você crie primeiro o seguinte:


* [Fornecedor](/docs/pt/buying/supplier)
* [Item](/docs/pt/stock/item)


## 2. Como criar um pedido de compra


Um pedido de compra pode ser criado automaticamente a partir de uma solicitação de material ou cotação de fornecedor.


1. Vá para a lista Pedido de compra e clique em Novo.
2. Selecione o Fornecedor, exigido por data.
3. Na tabela de itens, selecione o item por código, você pode alterar a data exigida para cada item.
4. Defina a quantidade e o preço será obtido automaticamente se definido no cadastro de itens.
5. Definir impostos.
6. Salvar e enviar.
![Pedido de compra](/files/purchase-order.png)


### 2.1 Configurando armazéns


* **Definir Armazém Alvo**: Opcionalmente, você pode definir o Armazém alvo padrão onde os Itens comprados serão entregues. Isso será buscado nas linhas da tabela Item.


### 2.2 Buscando itens de solicitações de materiais abertas


Os itens podem ser inseridos no pedido de compra automaticamente a partir de [Solicitações de materiais](/docs/pt/stock/material-request) abertas. Para que isso funcione, as seguintes etapas precisam ser executadas:


1. Selecione um fornecedor no pedido de compra.
2. Defina o fornecedor padrão no formulário Item em [Padrões de item](/docs/pt/stock/item#39-item-defaults).
3. Uma [Solicitação de material](/docs/pt/stock/material-request) precisa estar presente do tipo 'Compra'.
4. Clique no botão **Obter itens de solicitações de materiais abertas** abaixo do nome do fornecedor. Agora aparecerá uma caixa de diálogo com Solicitações de Materiais contendo Itens cujo Fornecedor padrão é o mesmo selecionado no Pedido de Compra. Ao selecionar as Solicitações de Materiais e clicar em **Obter Itens**, os Itens serão buscados nas Solicitações de Materiais.
![Obter itens de solicitações de material abertas](/files/get-items-from-open-mr.png)


> **Observação:** o botão **Obter itens de solicitações de materiais abertas** fica visível enquanto a tabela Itens estiver vazia.


## 3. Recursos


### 3.1 Endereço e contato


* **Selecionar endereço do fornecedor**: o endereço de cobrança do fornecedor.
* **Selecionar endereço de entrega**: o endereço de entrega do fornecedor de onde os itens serão enviados.
* Endereço, endereço de entrega, contato, e-mail de contato serão obtidos se salvos no cadastro de fornecedores.


Para a Índia:


* **GSTIN do fornecedor e da empresa**: o número de identificação GST do seu fornecedor e da sua empresa.
* **Local de Fornecimento**: Para GST, o Local de Fornecimento é necessário. Consiste no nome e número do estado.


### 3.2 Moeda e lista de preços


Você pode definir a moeda na qual o pedido de compra será armazenado. Se você definir uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar Ignorar regra de preços ignorará as regras de preços definidas em Contas > Regra de preços.


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.3 Subcontratação ou 'Fornecimento de matérias-primas'


Definir a opção 'Fornecer Matérias-Primas' é útil para subcontratação onde você fornece as matérias-primas para a fabricação de um item. Para saber mais, visite a [página de subcontratação](/docs/pt/manufacturing/subcontracting).


### 3.4 A tabela de itens


* **Ler código de barras**: você pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* **Quantidade e Taxa**: Ao selecionar o código do item, seu nome, descrição e UOM serão obtidos. O 'Fator de conversão UOM' é definido como 1 por padrão, você pode alterá-lo dependendo da UOM recebida do vendedor, mais na próxima seção.


'Taxa da lista de preços' será obtida se uma taxa de compra padrão for definida. 'Taxa da última compra' mostra a taxa do item do seu último pedido de compra. A taxa é obtida se definida no cadastro de itens. Você pode anexar um modelo de imposto de item para aplicar uma taxa de imposto específica ao item.
* **Os pesos dos itens** serão obtidos se definidos no item mestre, caso contrário, serão inseridos manualmente.
* **Armazém**: O armazém onde os itens serão entregues será preenchido automaticamente se 'Definir Armazém Alvo' tiver sido definido no Pedido de Compra. Através do pedido de cobertura, um pedido de cobertura pode ser vinculado. Para saber mais, [clique aqui](/docs/pt/selling/blanket-order). Um 'Projeto' pode ser vinculado para acompanhar o progresso. Uma 'BOM' ou lista de materiais também pode ser vinculada para acompanhar o progresso.
* 'Qtd conforme UOM de estoque' mostrará o estoque atual de acordo com a UOM definida no Cadastro de itens. A 'Quantidade recebida' será atualizada quando os itens forem cobrados.
* **Detalhes contábeis**: esta seção é preenchida automaticamente para um pedido de compra. 'Conta de despesas' é a conta na qual o pedido de compra é cobrado e Centro de custo é o CC no qual o pedido de compra é cobrado.


Uma data “Exigida até” em cada item: se você estiver esperando uma entrega parcial, seu fornecedor saberá a quantidade a ser entregue em qual data. Isso o ajudará a evitar o excesso de oferta. Também o ajudará a acompanhar o desempenho do seu fornecedor em termos de pontualidade.


**Permitir Taxa de Avaliação Zero**: Marcar 'Permitir Taxa de Avaliação Zero' permitirá o envio do Recibo de Compra mesmo que a Taxa de Avaliação do Item seja 0. Este pode ser um item de amostra ou devido a um entendimento mútuo com seu fornecedor.


### 3.6 Matérias-primas fornecidas


Esta seção aparece quando 'Fornecer Matérias-Primas' fornecidas está definido como 'Sim'. Esta seção apresenta uma tabela com os Itens a serem fornecidos ao Fornecedor para o processo de subcontratação.


* **Definir Armazém Reserva**: Quando [Subcontratação](/docs/pt/manufacturing/subcontracting), as matérias-primas podem ser reservadas em um Armazém separado. Ao selecionar o Armazém Reservado aqui, ele será buscado nas linhas de Item da tabela Matérias-Primas Fornecidas.


#### Tabela de itens fornecidos


* **Quantidade necessária**: a contagem de itens necessários para concluir a subcontratação conforme especificado na [BOM](/docs/pt/manufacturing/bill-of-materials).
* **Quantidade Fornecida**: Será atualizado quando você criar Entradas de Estoque para transferir materiais do Armazém de Reserva para o Armazém do Fornecedor usando o botão **Transferir**.
![Material de transferência de subcontrato](/files/subcontract-transfer-materials.gif)


### 3.7 UOM de compra e conversão de UOM de estoque


Você pode alterar sua UOM de acordo com suas necessidades de estoque no pedido de compra.


Por exemplo, se você comprou sua matéria-prima em grandes quantidades com UOM-caixas, e deseja estocá-la em UOM-Nos; você pode fazer isso enquanto faz seu pedido de compra.


1. Armazene UOM como Nos no cadastro de itens. Observe que a UDM no Cadastro de itens é a UDM do estoque.
2. No Pedido de Compra mencione UOM como Caixa. (Desde que o material chegue em Caixas)
3. Na seção Armazém e Referência, a UOM será extraída como Nos (do formulário Item):


![Ordem de compra-UOM](/files/purchase-order-uom.png)
4. Mencione o fator de conversão UOM. Por exemplo, (1); Se uma caixa tiver 1 quilo.
5. Observe que a quantidade em estoque será atualizada de acordo.


![Ordem de compra-UOM](/files/po-stock-uom.png)


### 3.8 Impostos e Taxas


Se o seu fornecedor for cobrar impostos adicionais ou cobrar como um
taxa de envio ou seguro, você pode adicioná-la aqui. Isso irá ajudá-lo a
acompanhe com precisão seus custos. Além disso, se alguns desses encargos aumentarem o valor
do produto você deverá mencioná-los na tabela de Impostos.


Acesse a página [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template) para saber mais sobre impostos. 


O total de impostos e taxas será exibido abaixo da tabela.


Para adicionar impostos automaticamente por meio de uma categoria de imposto, visite [esta página](/docs/pt/accounts/tax-category).


Certifique-se de marcar todos os seus impostos na tabela Impostos e Encargos corretamente para obter uma avaliação precisa.


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


![Impostos sobre pedidos de compra](/files/po-taxes.png)


Por exemplo, você compra itens no valor de X e os vende por 1,3X. Então seu cliente
paga 1,3 vezes o imposto que você paga ao seu fornecedor. Como você já pagou imposto
ao seu fornecedor por X, o que você deve ao seu governo é apenas o imposto de 0,3X.


Isso é muito fácil de rastrear no ERPNext já que cada cabeça fiscal também é uma conta.
Idealmente deverá criar duas Contas para cada tipo de IVA que paga e cobra,
“Compra VAT-X” (ativo) e “Sales VAT-X” (passivo), ou algo parecido
efeito.


### 3,9 Desconto adicional


Além de registrar o desconto por item, você pode adicionar um desconto a todo o pedido de compra nesta seção. Este desconto pode ser baseado no total geral, ou seja, após impostos/encargos, ou no total líquido, ou seja, antes de impostos/encargos. O desconto adicional pode ser aplicado como uma porcentagem ou um valor.


Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.10 Condições de pagamento


Às vezes o pagamento não é feito de uma só vez. Dependendo do acordo, metade do pagamento poderá ser feito antes do envio e a outra metade após o recebimento da mercadoria/serviço. Você pode adicionar um modelo de condições de pagamento ou adicionar os termos manualmente nesta seção.


Leia as [Condições de pagamento](/docs/pt/accounts/payment-terms) para saber mais.


### 3.11 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 3.12 Configurações de impressão


#### Papel timbrado


Você pode imprimir sua solicitação de cotação/pedido de compra em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados diversas vezes na tabela de itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


Os títulos dos seus documentos podem ser alterados. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


O desconto adicional, os termos de pagamento, os termos e condições do vendedor podem ser registrados em seu pedido de compra.


### 3.13 Mais informações


Esta seção mostra o status do Pedido de Compra, percentual de itens recebidos e percentual de itens faturados. Se este for um pedido entre empresas, o pedido de venda poderá ser vinculado aqui.


### 3.14 Após o envio


Depois de “enviar” seu pedido de compra, você pode acionar ações como estas:


* Você pode adicionar, atualizar e excluir itens do pedido de compra clicando no botão **Atualizar itens**. No entanto, você não pode excluir itens que já foram recebidos.
* Status: depois de enviado, você pode reter um pedido de compra ou fechá-lo.
* Criar: A partir de um pedido de compra enviado, você pode criar o seguinte:


	+ [Recibo de compra](/docs/pt/stock/purchase-receipt)-Um recibo indicando que você recebeu os itens.
	+ [Fatura de compra](/docs/pt/accounts/purchase-invoice)-Uma fatura/fatura do pedido de compra.
	+ [Entrada de pagamento](/docs/pt/accounts/payment-entry)-Uma entrada de pagamento indica que o pagamento foi feito em relação a um pedido de compra.
	+ [Lançamento contábil](/docs/pt/accounts/journal-entry)-Um lançamento contábil manual é registrado no razão geral.![Ordem de compra após envio](/files/po-after-submit.png)


### 4. Tópicos Relacionados


1. [Solicitação de cotação](/docs/pt/buying/request-for-quotation)
2. [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template)
3. [Compras em unidades diferentes](/docs/pt/buying/articles/purchasing-in-Different-Unit)
4. [Alteração do pedido de compra após o envio](/docs/pt/buying/articles/amending-purchase-order-after-submit)



