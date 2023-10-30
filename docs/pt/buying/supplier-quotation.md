# Cotação do fornecedor



**Uma cotação de fornecedor é um documento elaborado por um fornecedor potencial que especifica o custo dos bens ou serviços que fornecerá dentro de um período especificado.**


Uma cotação de fornecedor também pode conter condições de venda, condições de pagamento e garantias. A aceitação da cotação pelo comprador pode ser considerada como um acordo vinculativo para ambas as partes.


![Fluxo de compra](/files/buying_flow_sq.png)


Para acessar a Cotação de Fornecedores, acesse:
> Home > Compras > Compras > Cotação de Fornecedores


## 1. Pré-requisitos


Antes de criar e usar uma Cotação de Fornecedor, é aconselhável que você crie primeiro o seguinte:


* [Fornecedor](/docs/pt/buying/supplier)
* [Item](/docs/pt/stock/item)


## 2. Como criar uma cotação de fornecedor


### 2.1 Cotação do fornecedor a partir da solicitação de material


Você pode fazer uma cotação de fornecedor a partir de uma Solicitação de Material:
![Cotação do fornecedor a partir do recebimento de material](/files/supplier-quotation-from-mr.png)


Ou:


Uma cotação de fornecedor pode ser criada a partir de um [mestre de fornecedores](/docs/pt/buying/supplier).


Ou:


O próprio fornecedor pode enviar uma cotação via ERPNext. Para saber mais sobre isso, consulte a seção, visite a [Solicitação para a página de cotação](/docs/pt/buying/request-for-quotation#4-creating-a-supplier-quotation-after-rfq).


### 2.2 Criando uma cotação de fornecedor manualmente


1. Você também pode fazer uma cotação de fornecedor diretamente de:


**Compra > Compras > Cotação do fornecedor > Novo**.
2. Selecione o fornecedor que lhe enviou a cotação.
3. O endereço e o contato serão obtidos se você os salvou no cadastro de fornecedores.
4. Insira o código do item e selecione a quantidade. A taxa será obtida se você tiver definido a taxa de compra padrão para o item em [Preço do item](/docs/pt/stock/item-price).
![Cotação do fornecedor](/files/supplier-quotation.png)


Se você tiver vários fornecedores que fornecem o mesmo item, você
geralmente envia uma [Solicitação de cotação](/docs/pt/buying/request-for-quotation) para vários fornecedores. Em
Em muitos casos, especialmente se você tiver compras centralizadas, convém registrar todas as cotações para que:


* Você pode comparar preços facilmente no futuro
* Auditar se todos os fornecedores tiveram a oportunidade de fazer cotações.


As cotações de fornecedores não são necessárias para a maioria das pequenas empresas. Sempre
avalie o custo da coleta de informações de acordo com o valor que ela realmente oferece!
Como recomendação, você pode fazer isso apenas para itens de alto valor.


## 3. Recursos


### 3.1 Impostos e Taxas


Se o seu fornecedor for cobrar impostos adicionais ou cobranças como frete ou seguro, você pode adicioná-los aqui. Isso o ajudará a monitorar seus custos com precisão. Além disso, se alguns desses encargos agregarem valor ao produto você deverá mencioná-los na tabela de Impostos. Você também pode usar modelos para seus impostos. Para obter mais informações sobre como configurar seus impostos, consulte o [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template).


### 3.2 Mais


Existem campos para Categoria de Imposto, Regra de Envio, Modelo de Impostos e Encargos de Compra, Desconto, Termos e Condições, Número de Cotação, Configurações de Impressão. Você pode preencher esses campos para seu registro. Visite a página [Cotação](/docs/pt/selling/quotation) para saber mais sobre essas seções. Observe que os detalhes como regra de envio, impostos, desconto, termos e condições, número de cotação, etc., são do seu fornecedor e podem ser registrados para um rastreamento preciso.


Observação:


* A categoria de imposto será obtida do mestre de fornecedores, se definida
* As configurações de impressão servem para fazer alterações na impressão da cotação do fornecedor
* Os Termos e Condições aqui são do seu fornecedor
* A cotação do fornecedor pode ser vinculada a uma solicitação de material usando o botão 'Link para solicitações de material'


### 3.3 Após o envio


Os seguintes registros podem ser criados após o envio de uma cotação de fornecedor:


* Ordem de Compra-Uma Ordem de Compra se você concordar com a cotação do fornecedor.
* Cotação-Uma cotação para seu cliente.
* Repetição automática-repete automaticamente a cotação do fornecedor em intervalos especificados.


### 4. Tópicos Relacionados


1. [Fornecedor](/docs/pt/buying/supplier)
2. [Grupo de fornecedores](/docs/pt/buying/supplier-group)
3. [Pedido de compra](/docs/pt/buying/purchase-order)
4. [Solicitação de cotação](/docs/pt/buying/request-for-quotation)



