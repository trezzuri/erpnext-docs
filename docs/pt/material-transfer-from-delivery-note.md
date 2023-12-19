# Transferência de material da nota de entrega e recibo de compra



No ERPNext, você pode criar uma entrada de Transferência de Material a partir do documento [Entrada de Estoque](/docs/pt/stock/stock-entry.html). Porém, existem alguns cenários na Transferência de Material onde o mesmo precisa ser apresentado como Nota de Entrega e Recibo de Compra.


## Transferência de material da nota de entrega


### Cenários


1. Um dos exemplos é quando você transfere um Material de suas lojas para o local do projeto, porém, é necessário apresentá-lo como Nota de Entrega ao cliente.
2. Além disso, existem requisitos legais onde os impostos devem ser aplicados em cada transferência de Material. É mais fácil gerenciar em uma transação como Nota de Remessa, do que na Entrada de Estoque.


Considerando estes cenários, a disponibilização de Transferência de Material também foi adicionada na Nota de Remessa. A seguir estão as etapas para usar a Nota de Entrega para criar entrada de Transferência de Material.


### Etapas


#### Ativar o Target Warehouse


O tipo de documento do item da nota de entrega possui um campo oculto de Target Warehouse (anteriormente Customer Warehouse). Você pode ativá-lo em [Configurações de estoque](/docs/pt/stock/stock-settings) ativando "Permitir transferência de material da nota de entrega e fatura de venda".
Observe também que o cliente selecionado deve representar a mesma empresa. Para isso, habilite a opção ‘É Cliente Interno’ no formulário do cliente e selecione sua empresa no campo ‘Representa Empresa’.



### Selecionar armazéns


Ao criar uma Nota de Entrega para Transferência de Material, para um item selecione o Armazém de origem como Do Armazém.


No Armazém do Cliente, selecione um Armazém para onde o Material será transferido ou selecione um armazém de destino.


![Transferência de material da nota de entrega](/files/customer-warehouse-2.png)


Ao submeter uma Nota de Entrega, o stock do artigo será deduzido do “Armazém” e adicionado ao “Armazém do Cliente”.


## Transferência de material do recibo de compra


### Cenários


Existem requisitos legais onde os impostos devem ser aplicados em cada transferência de Material. É mais fácil gerenciar uma situação como esta em uma transação como o Recibo de Compra, do que no Lançamento de Estoque, pois os impostos não podem ser aplicados nas transferências de itens via Lançamento de Estoque


A seguir estão as etapas para usar o recibo de compra para criar entrada de transferência de material.


### Etapas


#### Ativar armazém do fornecedor


Semelhante ao Armazém do Cliente mostrado acima, a primeira etapa é ativar o Armazém do Fornecedor em [Configurações de estoque](/docs/pt/stock/stock-settings) conforme mostrado acima.


Observe também que o fornecedor selecionado deve representar a mesma empresa. Para isso, habilite a opção ‘É Fornecedor Interno’ no formulário Fornecedor e selecione sua empresa no campo ‘Representa Empresa’.



### Selecionar armazéns


Ao criar um Recibo de Compra para Transferência de Material, para um Item, selecione o Armazém de destino como Armazém Aceito.


É assim que você cria um recibo de compra interno a partir de uma nota de entrega interna:


![Transferência de material de recibo de compra](/files/supplier-warehouse-1.png)


No Armazém do Fornecedor, selecione um Armazém de onde o Material será transferido.


![Transferência de material de recibo de compra](/files/supplier-warehouse.png)


Ao enviar o Recibo de Compra, o estoque do item será deduzido do “Armazém do Fornecedor” e adicionado ao “Armazém Aceito”.





