# Recibo de compra



**Os recibos de compra são feitos quando você aceita itens do seu fornecedor, geralmente contra um pedido de compra.**


Você também pode aceitar recibos de compra diretamente, sem a necessidade de um pedido de compra. Para fazer isso, defina Ordem de compra
Obrigatório como “Não” nas configurações de compra.


Para acessar a lista de Recibos de Compra, acesse:
> Home > Estoque > Transações de estoque > Recibo de compra


![Fluxo de recibo de compra](/files/purchase-receipt-flow.png)


## 1. Pré-requisitos


Antes de criar e usar um recibo de compra, é aconselhável criar primeiro o seguinte:


* [Pedido de compra](/docs/pt/buying/purchase-order)


> Nota: A partir da versão 13 introduzimos o livro-razão imutável que altera as regras para cancelamento de entradas de estoque e lançamento de transações de estoque retroativas no ERPNext. [Saiba mais aqui](/docs/pt/accounts/articles/immutable-ledger-in-erpnext).


## 2. Como criar um recibo de compra


Um recibo de compra geralmente é criado a partir de um [pedido de compra](/docs/pt/buying/purchase-order). No Pedido de Compra, clique em Criar > Recibo de Compra.


Para criar um recibo de compra *manualmente* (não recomendado), siga estas etapas:


1. Vá para a lista de recibos de compra e clique em Novo.
2. O nome do Fornecedor e os Itens podem ser obtidos no Pedido de Compra clicando em 'Obter Itens de > Pedido de Compra'.
3. Você pode definir o Armazém Aceito para todos os itens neste Recibo de Compra. Isso é obtido se definido no pedido de compra.
4. Caso algum Itens apresente defeito, defina o Armazém Rejeitado onde esses Itens serão armazenados.
5. Selecione o Item e insira a quantidade na tabela Itens.
6. A taxa será obtida e o valor será calculado automaticamente.
7. Você pode expandir a linha do item para alterar o Armazém Aceito de um Item.
8. Salvar e enviar.


![Recibo de compra](/files/purchase-receipt.png)


Você também pode adicionar uma 'Nota de entrega do fornecedor' ao recibo de compra se o seu fornecedor tiver adicionado algumas notas.
Usando a caixa de seleção 'Editar data e hora de lançamento' você pode editar a hora e a data de lançamento do recibo de compra. Por padrão, a data e a hora são definidas quando você clica no botão Novo.


É Devolução: Marque esta caixa de seleção se estiver devolvendo itens que não foram aceitos em seu Armazém.


### 2.1 Status


Estes são os status em que um recibo de compra pode estar:


* **Rascunho**: um rascunho foi salvo, mas ainda precisa ser enviado ao sistema.
* **A faturar**: ainda será cobrado usando uma [fatura de compra](/docs/pt/accounts/purchase-invoice).
* **Concluído**: enviou e recebeu todos os itens.
* **Devolução emitida**: todos os itens foram devolvidos.
* **Cancelado**: cancelamento do recibo de compra.
* **Fechado**: O objetivo do Fechamento é gerenciar o fechamento a descoberto. Por exemplo, você pediu 20 unidades, mas fechou em 15 unidades. Os 5 restantes não serão recebidos nem cobrados.


## 3. Recursos


### 3.1 Moeda e lista de preços


A moeda do Recibo de Compra é mostrada nesta seção, ela é obtida no Pedido de Compra. Os preços dos itens serão obtidos na lista de preços definida. Marcar Ignorar regra de preços ignorará as regras de preços definidas em Contas > Regra de preços.


Como o item recebido afeta o valor do seu inventário, é importante convertê-lo em sua moeda base se você tiver feito o pedido em outra moeda. Você precisará atualizar a taxa de conversão de moeda, se aplicável.


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.2 Detalhes do armazém


O seguinte conjunto de Armazéns será aplicado a todos os Itens na tabela Itens do Recibo de Compra. Você pode alterar os armazéns de itens individuais por meio da tabela.


* **Armazém Aceito**: Este é o Armazém no qual você aceitará e armazenará os Itens recebidos. Normalmente, este é o Armazém das 'Lojas'.
* **Armazém Rejeitado:** Este é o Armazém onde você manterá os Itens rejeitados que estavam com defeito ou não estavam dentro da marca de qualidade.


#### Subcontratação


* **Matérias-Primas Consumidas**: Caso esteja subcontratando, selecione 'Sim' para consumir as Matérias-Primas do fornecedor. Leia [Subcontratação](/docs/pt/manufacturing/subcontracting) para saber mais.


### 3.3 Tabela de itens


* **Código de barras**: você pode rastrear itens usando [códigos de barras](/docs/pt/stock/articles/track-items-using-barcode) .
* **Ler código de barras**: você pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* O código do item, nome, descrição, imagem e fabricante serão obtidos no mestre de itens.
* **Recebido e Aceito**: Defina a quantidade recebida, aceita e rejeitada. A UM é obtida do mestre de itens. Você precisará atualizar o “Fator de conversão UOM” se o seu pedido de compra de um item estiver em uma unidade de medida (UOM) diferente daquela que você armazena (UOM de estoque).


![Tabela de itens de recibo de compra](/files/purchase-receipt-item.png)
* **Taxa**: A taxa é obtida se definida na [Lista de preços](/docs/pt/stock/price-lists) e o valor total é calculado.
* **Modelo de imposto de item**: você pode definir um modelo de imposto de item para aplicar um valor de imposto específico a este item específico. Para saber mais, visite [esta página](/docs/pt/accounts/item-tax-template).
* Os detalhes do Peso do Item por unidade e a UOM do Peso são obtidos se definidos no Cadastro de Itens.
* **Armazém e Referência**: Você pode definir os Armazéns aceitos e rejeitados e também adicionar uma Inspeção de Qualidade, veja a próxima seção.
* **Nº de série, nº de lote e BOM**: se o seu item for serializado ou em lote, você terá que inserir o número de série
e Lote na tabela Itens. Você tem permissão para inserir vários números de série
em uma linha (cada uma em uma linha separada) e você deve inserir o mesmo número de
Números de série como quantidade.


Existem campos separados para inserir números de série de itens aceitos e rejeitados aqui. Um número de lote também pode ser definido se você estiver armazenando um lote de medicamentos plásticos, por exemplo.


Marcar 'Permitir taxa de avaliação zero' permitirá o envio do recibo de compra mesmo que a taxa de avaliação do item seja 0. Este pode ser um item de amostra ou devido a um entendimento mútuo com seu fornecedor.
* Você pode vincular uma BOM aqui se o item estiver sendo [subcontratado](/docs/pt/manufacturing/subcontracting). Vincular a BOM aqui afetará o razão de estoque, ou seja, o estoque de matéria-prima será deduzido do Armazém do Fornecedor.


**Observação**: o item precisa ser serializado ou em lote para que esses recursos funcionem. Se o item for serializado, um pop-up aparecerá onde você poderá inserir os números de série.
* As Dimensões Contábeis ajudam a marcar cada transação com Dimensões diferentes sem a necessidade de criar novos Centros de Custo. Você precisa criar dimensões contábeis primeiro. Para saber mais, visite [esta página](/docs/pt/accounts/accounting-dimensions).
* A quebra de página criará uma quebra de página logo antes deste item durante a impressão.


### 3.4 Acompanhamento da inspeção de qualidade


Se para determinados Itens for obrigatório o registro de Inspeções de Qualidade (caso você tenha definido isso em seu Cadastro de Itens), será necessário atualizar o campo “Inspeção de Qualidade”. O sistema só permitirá que você “Envie” o
Recibo de compra se você atualizar a “Inspeção de Qualidade”.


Depois de ativar os critérios de inspeção no [formulário de item](/docs/pt/stock/item#216-inspection-criteria) para compra e anexar um modelo de inspeção de qualidade lá, as Inspeções de Qualidade podem ser registradas em Recibos de Compra.


Para saber mais, visite a página [Inspeção de qualidade](/docs/pt/stock/quality-inspection).


![Inspeção de qualidade](/files/quality-inspection.png)


### 3.5 Matérias-primas consumidas


* A tabela **Itens Consumidos** contém as Matérias-Primas consumidas pelo Fornecedor para receber o Item Acabado.
* O botão **Obter Estoque Atual** irá buscar o estoque atual dos Itens Consumidos no Armazém do Fornecedor.
![Recibo de compra](/files/purchase-receipt-consumed-items.png)


### 3.6 Impostos e avaliação


Os impostos e taxas serão obtidos no [Ordem de compra](/docs/pt/buying/purchase-order).


Acesse o [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template)página para saber mais sobre impostos.


O total de impostos e taxas será exibido abaixo da tabela.


Para adicionar impostos automaticamente por meio de uma categoria de imposto, visite [esta página](/docs/pt/accounts/tax-category).


Certifique-se de marcar todos os seus impostos na tabela Impostos e Encargos corretamente para obter uma avaliação precisa.


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


### 3.7 Desconto adicional


Quaisquer descontos adicionais para todo o pedido podem ser definidos nesta seção.
Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.8 Mais informações


O status do recibo de compra é mostrado aqui e na parte superior. Os vários status são: Rascunho, A faturar, Concluído, Cancelado e Fechado. Esta seção também mostra % do valor faturado, ou seja, a porcentagem do valor para o qual as [faturas de vendas](/docs/pt/accounts/sales-invoice) são criadas.


### 3.9 Configurações de impressão


#### Papel timbrado


Você pode imprimir seu recibo de compra em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados diversas vezes na tabela de itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


Os títulos do recibo de compra também podem ser alterados durante a impressão do documento. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


### 3.10 Após o envio


Uma entrada no razão de estoque é criada para cada item que adiciona o item no armazém
pela “Quantidade Aceita” Se você tiver rejeições, uma entrada no razão de estoque é
feito para cada rejeição. A “Quantidade Pendente” é atualizada no campo Compra
Encomende.


Após enviar o Recibo de Compra, poderá ser criado o seguinte:


* [Devolução de compra](/docs/pt/stock/purchase-return)
* [Entrada de estoque](/docs/pt/stock/stock-entry)
* [Fatura de compra](/docs/pt/accounts/purchase-invoice)
* [Retenção de estoque de amostra](/docs/pt/stock/retain-sample-stock)


![Envio de recibo de compra](/files/purchase-receipt-submit.png)


### 3.11 Devolução de um pedido de compra


Depois de receber um pedido de compra usando um recibo de compra, você pode criar uma entrada de devolução caso o item precise ser devolvido ao [Fornecedor](/docs/pt/buying/fornecedor). Para saber mais, visite a página [Devolução de compra](/docs/pt/stock/purchase-return).


### 3.12 Ignorando recibo de compra


Se você não quiser criar um recibo de compra após um pedido de compra e quiser criar diretamente uma fatura de compra, ative o recurso em [Configurações de compra](/docs/pt/buying/buying-settings#23-purchase-receipt-required).



#### Alterar o valor dos itens após o recibo de compra:


Às vezes, certas despesas que somam o total dos itens comprados são conhecidas
só depois de um tempo. Um exemplo comum é, se você estiver importando os itens, você
tomará conhecimento dos direitos aduaneiros, etc. somente quando o seu “Agente de compensação” enviar
você uma conta. Se você quiser atribuir esse custo aos itens comprados, você
terá que usar o [Voucher de custo final](/docs/pt/stock/landed-cost-voucher). Por que “custo final”? Porque representa os encargos que você pagou quando chegou à sua posse.


## 4. Tópicos Relacionados


1. [Nota de entrega](/docs/pt/stock/delivery-note)
2. [Pedido de compra](/docs/pt/buying/purchase-order)
3. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
4. [Fornecedor](/docs/pt/buying/supplier)
5. [Comprovante de custo final](/docs/pt/stock/landed-cost-voucher)



