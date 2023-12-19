# Número de série



Conforme discutido na página [Item](/docs/pt/stock/item), se um **Item** for *serializado* , um
O registro do **Número de série** (Número de série) é mantido para cada quantidade desse
**Item**. Esta informação ajuda a rastrear a localização do Serial
Não, suas informações de garantia e fim de vida útil (validade).


Você também pode rastrear de qual **Fornecedor** você comprou o **Número de série** e
para qual **Cliente** você o vendeu. O status do **Número de série** informará
o status atual do inventário.


Se o seu item for *serializado* você terá que inserir os números de série no campo
coluna relacionada com cada número de série em uma nova linha.
Você pode manter unidades únicas de itens serializados usando o número de série.


Para acessar a lista de números de série, vá para:
> Home > Estoque > Nº de série e lote > Nº de série


## 1. Pré-requisitos


Antes de criar e usar um número de série, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* Ative 'Tem número de série' no cadastro de itens
![Serial No Enabled](/files/serial-no-enabled.png)


## 2. Como criar um número de série


Normalmente, os números de série são criados automaticamente quando as transações são feitas em um item serializado. Isso funciona apenas quando 'Tem número de série' está ativado e uma série está definida no item mestre.


Por exemplo, uma série foi definida para o seguinte item como 'PB2L.#####'. Em seguida, foi enviado um Registro de Estoque para recebimento do Item. Os números de série foram criados de acordo.


![Serial não criado](/files/serial-no-created.png)


No entanto, se você quiser criar um número de série *manualmente*, siga estas etapas:


1. Vá para a lista de números de série e clique em Novo.
2. Insira um número de série.
3. Insira o código do item e os detalhes serão obtidos.
4. Se qualquer transação for feita com um item, o número de série não poderá ser definido ou desmarcado.
5. Salvar.


O estoque de um item só pode ser afetado se o número de série for transacionado por meio de um
Transação de estoque (entrada de estoque, recibo de compra, nota de entrega, vendas
Fatura). Quando um novo Nº de Série é criado diretamente, seu Armazém não pode ser
definido.


![Número de série](/files/serial-no.png)


### 2.1 Notas sobre o número de série


* O status é definido com base na entrada de estoque.
* Somente números de série com status 'Disponível' podem ser entregues.
* Os números de série podem ser criados automaticamente a partir de uma entrada de estoque ou recibo de compra. Se você mencionar o número de série na coluna Números de série, esses números de série serão criados automaticamente.
* Se no Cadastro de Itens o Nº de Série da Série for mencionado, você pode deixar a coluna Nº de Série em branco em uma Entrada de Estoque/Recibo de Compra. Os números de série serão definidos automaticamente a partir dessa série.


## 3. Recursos


### 3.1 Detalhes de compra/fabricação


Será mostrado o documento a partir do qual o número de série foi criado. Se você comprou de um fornecedor, ele estará vinculado aqui.


### 3.2 Detalhes da entrega


Se o Número de Série foi gerado a partir de um Pedido de Venda, o Cliente será vinculado aqui.


### 3.3 Detalhes da garantia/AMC


Se o Item estiver sob garantia ou AMC (Contrato Anual de Manutenção), as datas de vencimento podem ser definidas.


### 3.4 Mais informações


Qualquer informação adicional sobre esta unidade de item específica pode ser definida em 'Série sem detalhes'.


## 4. Vídeo






### 5. Tópicos Relacionados


1. [Codificação de itens](/docs/pt/stock/articles/item-codification)
2. [Variantes de item](/docs/pt/stock/item-variants)
3. [Nomeação de números de série](/docs/pt/stock/articles/serial-no-naming)



