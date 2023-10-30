# Solicitação de material



**Uma Solicitação de Material é um documento simples que identifica um requisito de um conjunto de Itens (produtos ou serviços) por um motivo específico.**


Uma Solicitação de Material pode ter as seguintes finalidades:


* **Compra**: se o material solicitado for adquirido.
* **Transferência de Material**: Se o material solicitado for transferido de um Armazém para outro.
* **Emissão de material**: se o material solicitado for emitido para alguma finalidade, como fabricação.
* **Fabricação:** se o material solicitado for produzido.
* **Fornecido pelo Cliente**: se o material solicitado for fornecido pelo Cliente. Para saber mais sobre isso, visite a página [Item fornecido pelo cliente](/docs/pt/manufacturing/articles/customer-provided-items).


![Material Request](/files/material-request-flowchart.png)


Para acessar a lista de Solicitação de Materiais, acesse:
> Home > Estoque > Transações de estoque > Solicitação de materiais


## 1. Como criar uma Solicitação de Material


1. Vá para a lista de Solicitação de Material e clique em Novo.
2. Insira a data exigida.
3. Selecione uma das finalidades listadas acima.
4. Você pode buscar itens de uma lista técnica, pedido de vendas ou pacote de produtos.
![MR fetch from](/files/mr-fetch-from.png)
5. Selecione o item e defina a quantidade.
6. Selecione o armazém para o qual os itens são necessários.
7. Você pode alterar a data Obrigatória até para itens individuais nesta tabela.
8. Salvar e enviar.


### 1.1 Formas alternativas de criar uma solicitação de material


Uma Solicitação de Material pode ser gerada automaticamente:


* De um [Pedido de venda](/docs/pt/selling/sales-order). Ao criar MR, o usuário pode optar por ignorar ou incluir a Quantidade Projetada. Conseqüentemente, os itens do pedido de vendas são buscados no MR.
* Quando a quantidade projetada de um item nas lojas (armazéns) atinge um determinado nível.
* Em seu [Plano de produção](/docs/pt/manufacturing/production-plan) para planejar suas atividades de fabricação.


Se seus Itens forem itens de estoque, você também deverá mencionar o Armazém onde espera que esses Itens sejam entregues. Isso ajuda a controlar a [Quantidade projetada](/docs/pt/stock/projected-quantity) para este item.


> Informações: Solicitação de Material não é obrigatória. É ideal se você centralizou
comprando para que você possa coletar essas informações de vários departamentos.


### 1.2 Status


Estes são os status em que uma Solicitação de Material pode estar:


* **Rascunho**: um rascunho foi salvo, mas ainda precisa ser enviado ao sistema.
* **Enviado**: o documento é enviado ao sistema.
* **Parado**: Se não forem necessários mais materiais, a Solicitação de Material poderá ser interrompida.
* **Cancelado**: os materiais não são necessários e a solicitação é cancelada.
* **Pendente**: A Compra/Fabricação está pendente para conclusão da Solicitação de Material.
* **Encomendado Parcialmente**: Pedidos de compra para alguns itens da Solicitação de Material são feitos e alguns estão pendentes.
* **Encomendados**: Todos os Itens na Solicitação de Material são encomendados por meio de Pedidos de Compra.
* **Emitido**: os materiais são emitidos usando uma entrada de estoque de emissão de material.
* **Transferido**: Os materiais necessários são transferidos de um armazém para outro usando uma entrada de estoque.
* **Recebido**: Os materiais foram encomendados e recebidos em seu Armazém através de um Recibo de Compra.


## 2. Recursos


### 2.1 Tabela de itens


* **Código de barras**: você pode rastrear itens usando [códigos de barras](/docs/pt/stock/articles/track-items-using-barcode) .
* O código do item, nome, descrição, imagem e fabricante serão obtidos no mestre de itens.
* **Ler código de barras**: você pode adicionar itens na tabela Itens lendo seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* A unidade de medida, o fator de conversão e o valor serão obtidos. Você altera o Armazém para o qual o material está sendo solicitado.
* Detalhes contábeis como conta de despesas e dimensões contábeis podem ser definidos para os itens.
* A quebra de página criará uma quebra de página logo antes deste item durante a impressão.


### 2.2 Configurando armazéns


* **Definir Armazém**: Opcionalmente, você pode definir o Armazém onde os Itens solicitados chegarão. Isso será obtido nos campos 'Para armazém' nas linhas da tabela de itens.


### 2.3 Mais informações


No campo 'Solicitado para', você pode definir uma Referência de onde a Solicitação de Material foi gerada.


### 2.4 Detalhes de impressão


#### Papel timbrado


Você pode imprimir sua Solicitação de Material em papel timbrado da sua empresa.
Leia a [documentação sobre papel timbrado](/docs/pt/setting-up/print/letter-head) para saber mais.


#### Imprimir títulos


Os títulos do recibo de compra também podem ser alterados durante a impressão do documento. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


### 2.5 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 2.6 Após o envio


Você pode criar os seguintes documentos:


* [Solicitação de cotação](/docs/pt/buying/request-for-quotation)
* [Pedido de compra](/docs/pt/buying/purchase-order)
* [Cotação do fornecedor](/docs/pt/buying/supplier-quotation)


![Material Request](/files/material-request.png)


### 2.7 Gerar solicitações de materiais automaticamente


As solicitações de materiais podem ser geradas automaticamente ativando a configuração em [Configurações de estoque](/docs/pt/stock/stock-settings#9-automatic-material-request) e definir o nível no [formulário de item](/docs/pt/stock/item#34-automatic-reordering). Quando o nível de estoque cai abaixo de uma determinada quantidade, definir um novo pedido criará automaticamente solicitações de material para o item.


## 3. Vídeo








### 4. Tópicos Relacionados


1. [Item](/docs/pt/stock/item)
2. [Criação automática de solicitação de material](/docs/pt/stock/articles/auto-creation-of-material-request)
3. [Lista de seleção](/docs/pt/stock/pick-list#23-create-pick-list-from-material-request)
4. [Solicitação de cotação](/docs/pt/buying/request-for-quotation)
5. [Pedido de compra](/docs/pt/buying/purchase-order)
6. [Cotação do fornecedor](/docs/pt/buying/supplier-quotation)



