# Fatura de compra



**Uma fatura de compra é uma fatura que você recebe de seus fornecedores e pela qual você precisa efetuar o pagamento.**


A Fatura de Compra é exatamente o oposto da sua Fatura de Venda. Aqui vocÊ
acumular despesas para o seu fornecedor. Fazer uma fatura de compra é muito semelhante a
fazendo um pedido de compra.


Para acessar a lista de faturas de compra, acesse:



> 
> Página inicial > Contabilidade > Contas a pagar > Fatura de compra
> 
> 
> 


![PI Flow](/files/pi-flow.png)


## 1. Pré-requisitos


Antes de criar e usar uma fatura de compra, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Fornecedor](/docs/pt/buying/supplier)
* [Pedido de compra](/docs/pt/buying/purchase-order)
* [Recibo de compra](/docs/pt/stock/purchase-receipt) (opcional)


## 2. Como criar uma fatura de compra:


Uma fatura de compra geralmente é criada a partir de um pedido de compra ou de um recibo de compra. Os detalhes do Item do Fornecedor serão inseridos na Fatura de Compra. No entanto, você também pode criar uma fatura de compra diretamente.


Para obter os detalhes automaticamente em uma fatura de compra, clique em **Obter itens de**. Os detalhes podem ser obtidos em um pedido de compra ou recibo de compra.


Para criação manual, siga estas etapas:


1. Vá para a lista Fatura de compra e clique em Novo.
2. Selecione o fornecedor.
3. A data e hora da postagem serão definidas como atuais. Você pode editar depois de marcar a caixa de seleção abaixo de Horário da postagem.
4. Defina a data de vencimento do pagamento.
5. Adicione itens e quantidades na tabela Itens.
6. A Taxa e o Valor serão obtidos.
7. Salvar e enviar.


![Fatura de compra](/files/purchase-invoice.png)


### 2.1 Opções adicionais ao criar uma fatura de compra


* **É pago**: você pode marcar 'É pago' se o valor já tiver sido pago por meio de um [Entrada de pagamento antecipado](/docs/pt/accounts/advance-payment-entry). Deve ser assinalado se houver pagamento total ou parcial.
* **É Devolução (Nota de Débito)**: Marque esta opção se o cliente devolveu os Itens. Para saber mais detalhes, visite a página [Nota de Débito](/docs/pt/accounts/debit-note).
* **Aplicar valor de retenção de imposto**: Se o fornecedor selecionado tiver uma categoria de retenção de imposto definida, esta caixa de seleção estará habilitada. Para obter mais informações, visite a página [Categoria de retenção de imposto](/docs/pt/accounts/tax-withholding-category).


### 2.2 Status


* **Rascunho**: um rascunho foi salvo, mas ainda precisa ser enviado ao sistema.
* **Devolução**: Os Itens foram devolvidos ao Fornecedor.
* **Nota de débito emitida**: os itens foram devolvidos e uma [Nota de débito](/docs/pt/accounts/debit-note) foi emitido contra a fatura.
* **Enviada**: a fatura de compra foi enviada ao sistema e o razão geral foi atualizado.
* **Pago**: o fornecedor recebeu integralmente o valor da fatura e as [entradas de pagamento foram enviados.](/docs/pt/accounts/payment-entry)
* **Parcialmente pago**: o fornecedor recebeu uma parte do valor da fatura e o [pagamento correspondente As inscrições](/docs/pt/accounts/payment-entry) foram enviadas.
* **Não paga**: a fatura de compra ainda não foi paga.
* **Atrasado**: o prazo para pagamento já passou.
* **Cancelada**: a fatura foi cancelada por algum motivo.


## 3. Recursos


### 3.1 Dimensões contábeis


As Dimensões Contábeis permitem marcar transações com base em um Território, Filial, Cliente específico, etc. Isso ajuda a visualizar os demonstrativos contábeis separadamente com base nos critérios selecionados. Para saber mais, visite a página [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions).



> 
> Observação: Projeto e Centro de Custo são tratados como dimensões por padrão.
> 
> 
> 


### 3.2 Retenção da fatura


Às vezes, pode ser necessário impedir o envio de uma fatura.


**Reter fatura**: marque esta caixa de seleção para suspender a fatura de compra. Isso só pode ser feito antes do envio da fatura. Depois que a opção "Reter fatura" for ativada e a fatura de compra for enviada, o status mudará para "Temporariamente em espera".


![Fatura de compra em espera](/files/purchase-invoice-on-hold.png)


Depois que a fatura de compra for enviada e você desejar alterar a 'Data de lançamento', você poderá usar o botão 'Reter fatura', que está disponível no canto superior direito.


Se quiser reter a fatura de compra enviada, você pode reter usando a opção 'Bloquear fatura' e se quiser desbloquear novamente, use a opção 'Desbloquear fatura'.


![Bloquear PI](/files/purchase-invoice-block.png)


Esta é a retenção no nível da fatura. Os fornecedores podem ser colocados em espera. [Saiba mais aqui](/docs/pt/buying/supplier#23-credit-limit).


### 3.3 Detalhes da fatura do fornecedor


* **Número da Fatura do Fornecedor**: O Fornecedor poderá identificar este pedido com um número próprio. Isto é para referência.
* **Data da fatura do fornecedor**: A data em que o fornecedor fez/confirmou seu pedido.


### 3.4 Endereço e contato


* **Endereço do fornecedor:** este é o endereço de cobrança do fornecedor.
* **Pessoa de Contato**: Se o Fornecedor for uma Empresa, a pessoa a ser contatada é buscada neste campo se definida no [Formulário de fornecedor](/docs/pt/compra/fornecedor).
* **Endereço de envio:** Endereço para onde os itens serão enviados.


Para a Índia, os seguintes detalhes podem ser registrados para fins de GST:


* Fornecedor GSTIN
* Local de fornecimento
* GSTIN da empresa


### 3.5 Lista de moedas e preços


Você pode definir a moeda na qual o pedido da fatura de compra será enviado. Isso é obtido no pedido de compra. Se você definir uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar 'Ignorar regra de preços' irá ignorar as [Regras de preços](/docs/pt/accounts/pricing-rule) definidas em Contas > Regra de preços.


![Lista de preços da fatura de compra](/files/purchase-invoice-price-list.png)


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.6 Subcontratação ou 'Fornecimento de matérias-primas'


Definir a opção 'Fornecer matérias-primas' é útil para subcontratação onde você fornece as matérias-primas para a fabricação de um item. Para saber mais, visite a [página de subcontratação](/docs/pt/manufacturing/subcontracting).


### 3.7 Tabela de itens


* **digitalizar código de barras**: você pode adicionar itens na tabela Itens digitalizando seus códigos de barras se tiver um leitor de código de barras. Leia a documentação sobre [rastreamento de itens usando código de barras](/docs/pt/stock/articles/track-items-using-barcode) para saber mais.
* O código do item, nome, descrição, imagem e fabricante serão obtidos no [Mestre de itens](/docs/pt/stock/item) .
* **Fabricante**: Se o item for fabricado por um fabricante específico, ele poderá ser adicionado aqui. Isso será obtido se definido no item mestre.
* **Quantidade e Taxa**: Ao selecionar o código do item, seu nome, descrição e UOM serão buscados. O 'Fator de conversão UOM' é definido como 1 por padrão, você pode alterá-lo dependendo da UOM recebida do vendedor, mais na próxima seção.


'Taxa da lista de preços' será obtida se uma taxa de compra padrão for definida. 'Taxa da última compra' mostra a taxa do item do seu último pedido de compra. A taxa é obtida se definida no cadastro de itens. Você pode anexar um modelo de imposto de item para aplicar uma taxa de imposto específica ao item.
* **Os pesos dos itens** serão obtidos se definidos no item mestre, caso contrário, serão inseridos manualmente.
* **Desconto na tarifa da lista de preços**: Você pode aplicar um desconto em itens individuais em termos percentuais ou no valor total do item. Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.
* **Peso do item**: os detalhes do Peso do item por unidade e UDM do peso são obtidos se definidos no Cadastro de itens, caso contrário, insira-os manualmente.
* **Detalhes da conta**: a conta de despesas pode ser alterada aqui conforme desejar.
* **Despesa Diferida**: Se a despesa deste item for cobrada em partes nos próximos meses, marque 'Ativar Despesa Diferida'. Para saber mais, visite a [página Despesas diferidas](/docs/pt/accounts/deferred-expense).
* **Permitir Taxa de Avaliação Zero**: Marcar 'Permitir Taxa de Avaliação Zero' permitirá o envio do Recibo de Compra mesmo que a Taxa de Avaliação do Item seja 0. Este pode ser um item de amostra ou devido a um entendimento mútuo com seu fornecedor.
* **BOM**: se houver uma [lista de materiais](/docs/pt/manufacturing/bill-of-materials) criado para o Item, ele será buscado aqui. Isso é útil para referência ao [subcontratação](/docs/pt/manufacturing/subcontracting).
* **Modelo de imposto de item**: você pode definir um modelo de imposto de item para aplicar um valor de imposto específico a este item específico. Para saber mais, visite [esta página](/docs/pt/accounts/item-tax-template).
* **Quebra de página** criará uma quebra de página logo antes deste item durante a impressão.


#### Atualizar estoque



> 
> Nota: A partir da versão 13 introduzimos o livro-razão imutável que altera as regras para cancelamento de entradas de estoque e lançamento de transações de estoque retroativas no ERPNext. [Saiba mais aqui](/docs/pt/accounts/articles/immutable-ledger-in-erpnext).
> 
> 
> 


A caixa de seleção **Atualizar Estoque** deve ser marcada se você deseja que o ERPNext atualize automaticamente seu inventário. Consequentemente, não haverá necessidade de Nota de Entrega.


### 3.8 Impostos e encargos


Os Impostos e Taxas serão obtidos no [Ordem de Compra](/docs/pt/buying/purchase-order) ou [Recibo de compra](/docs/pt/stock/purchase-receipt).


![Imposto da fatura de compra](/files/purchase-invoice-tax.png)


Acesse a página [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template) para saber mais sobre impostos. 


O total de impostos e taxas será exibido abaixo da tabela.


Para adicionar impostos automaticamente por meio de uma categoria de imposto, visite [esta página](/docs/pt/accounts/tax-category).


Certifique-se de marcar todos os seus impostos na tabela Impostos e Encargos corretamente para obter uma avaliação precisa.


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


### 3,9 Desconto adicional


Quaisquer descontos adicionais para toda a fatura podem ser definidos nesta seção. Este desconto pode ser baseado no total geral, ou seja, após impostos/encargos, ou no total líquido, ou seja, antes de impostos/encargos. O desconto adicional pode ser aplicado como uma porcentagem ou um valor.


![Desconto na fatura de compra](/files/purchase-invoice-additional-discount.png)


Acesse a página [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.10 Pagamento Antecipado


Para itens de alto valor, o vendedor pode solicitar um pagamento antecipado antes de processar o pedido. O botão **Obter Adiantamentos Recebidos** abre um popup onde você pode buscar os pedidos onde o pagamento antecipado foi feito. Para saber mais, visite a página [Entrada de pagamento antecipado](/docs/pt/accounts/advance-payment-entry).


### 3.11 Termos de pagamento


O pagamento de uma fatura poderá ser feito em parcelas dependendo do seu entendimento com o Fornecedor. Isso é obtido se definido no pedido de compra.


![Termos de pagamento da fatura de compra](/files/purchase-invoice-payment-terms.png)


Para saber mais, visite a página [Condições de pagamento](/docs/pt/accounts/payment-terms).


### 3.12 Baixa


A baixa ocorre quando o Cliente paga um valor inferior ao valor da fatura. Esta pode ser uma pequena diferença como 0,50. Em vários pedidos, isso pode resultar em um grande número. Para maior precisão contábil, esse valor de diferença é “baixado”. Para saber mais, visite a página [Condições de pagamento](/docs/pt/accounts/payment-entry#25-deductions-or-loss).


### 3.13 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 3.14 Configurações de impressão


#### Papel timbrado


Você pode imprimir sua fatura de compra em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados diversas vezes na tabela Itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


Os títulos da fatura de compra também podem ser alterados durante a impressão do documento. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


Existem caixas de seleção adicionais para imprimir a Nota Fiscal de Compra sem o valor, isso pode ser útil quando o Item for de alto valor. Você também pode agrupar os mesmos itens em uma linha ao imprimir.


### 3.15 Detalhes do GST (para a Índia)


Os seguintes detalhes podem ser definidos para o GST:


* Categoria GST
* Cópia da fatura
* Cobrança reversa
* GSTIN de comércio eletrônico
* Elegibilidade para ITC
* Imposto integrado de TIC disponível
* Imposto Central ITC Aproveitado
* Imposto estadual/UT do ITC disponível
* Taxa ITC disponível


### 3.16 Mais informações


* **É uma entrada de abertura**: se esta for uma entrada de abertura que afetará suas contas, selecione 'Sim'. ou seja, se você estiver migrando de outro ERP para o ERPNext no meio do ano, você pode querer usar uma Entrada de Abertura para atualizar os saldos das contas no ERPNext.
* **Observações**: Quaisquer observações adicionais sobre a fatura de compra podem ser adicionadas aqui.


### 3.17 Após o envio


Ao enviar uma fatura de compra, os seguintes documentos podem ser criados:


1. [Lançamento de diário](/docs/pt/accounts/journal-entry)
2. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
3. [Solicitação de pagamento](/docs/pt/accounts/payment-request)
4. [Comprovante de custo final](/docs/pt/stock/landed-cost-voucher)
5. [Ativo](/docs/pt/asset/asset)


![PI Submit](/files/purchase-invoice-post-submit.png)


## 4. Mais


### 4.1 Impacto contábil


Semelhante a uma fatura de venda, em uma fatura de compra você deve inserir uma conta de despesa ou ativo para
cada linha da tabela Itens. Isso ajuda a indicar se o item é um ativo
ou uma despesa. Você também pode alterar o Centro de Custo. Eles também podem ser definidos no
Mestre de itens. O Centro de Custo pode ser definido no nível da Empresa.


A fatura de compra afetará suas contas da seguinte forma:


* Lançamentos contábeis (entrada GL) para uma típica “compra” de dupla entrada:
* Débitos:
	+ Despesa ou Ativo (totais líquidos, excluindo impostos)
	+ Impostos (/ativos se for tipo IVA ou despesa novamente)
* Créditos:
	+ Fornecedor


![Lista de fatura de compra](/files/purchase-invoice-ledger.png)


### 4.2 Contabilidade quando **É pago** é verificado


Se **Está Pago** estiver marcado, o ERPNext também fará o seguinte
lançamentos contábeis:


Débitos:


* Fornecedor


Créditos:


* Conta bancária/dinheiro


Para ver as entradas na sua fatura de compra após “Enviar”, clique em “Ver
Razão”.


### 4.3 A compra é uma “despesa” ou um “ativo”?


Se o Item for consumido imediatamente após a compra, ou se for um serviço, então
a compra passa a ser uma “Despesa”. Por exemplo, uma conta telefónica ou uma conta de viagem
a conta é uma “Despesa”-já foi consumida.


Para itens de estoque, que possuem valor, essas compras ainda não são “Despesas”,
porque eles ainda têm valor enquanto permanecem em seu estoque. Eles são
"Ativos". Se forem matérias-primas (utilizadas num processo), tornar-se-ão
“Despesas” no momento em que são consumidas no processo. Se eles forem vendidos
para um Cliente, eles se tornam “Despesas” quando você os envia ao Cliente.


### 4.4 Dedução de impostos na fonte


Em muitos países, a lei pode exigir que você deduza impostos, enquanto paga seus
fornecedores. Esses impostos poderiam ser baseados em uma taxa padrão. Neste tipo de esquemas, normalmente se um Fornecedor ultrapassar um determinado limite de pagamento, e
se o tipo de produto for tributável, poderá ter que deduzir algum imposto (que você
reembolsar ao seu governo, em nome do seu fornecedor).


Para fazer isso, você terá que criar uma nova Conta Fiscal em “Passivos Fiscais” ou
semelhante e creditar nesta conta a porcentagem que você deve deduzir
cada transação.


### 4.5 Reter pagamentos de uma fatura de compra


Há duas maneiras de suspender uma fatura de compra:


* Período de espera
* Retenção explícita


#### Retenção explícita


A retenção explícita retém a fatura de compra indefinidamente.
Para isso, na seção “Reter fatura” do formulário da fatura de compra, basta marcar a caixa de seleção “Reter fatura”. No campo de texto "Motivo da suspensão", digite um comentário explicando por que a fatura deve ser suspensa.


Se você precisar reter uma fatura enviada, clique no botão "Criar"
e clique em “Bloquear fatura”. Além disso, adicione um comentário explicando por que a fatura deve ser suspensa na caixa de diálogo exibida e clique em "Salvar".


#### Retenção de período de data


A retenção de período retém a fatura de compra até uma data especificada. Para isso, na seção “Reter fatura” do formulário da fatura de compra, marque a caixa de seleção “Reter fatura”. Em seguida, insira a data de lançamento na caixa de diálogo que aparece e clique em “Salvar”. A data de lançamento é a data
que a retenção do documento expira.


Depois que a fatura for salva, você poderá alterar a data de lançamento clicando no botão suspenso "Reter fatura" e depois em "Alterar data de lançamento". Esta ação fará com que uma caixa de diálogo apareça.


![Fatura de compra em espera](/files/purchase-invoice-hold.png)


Selecione a nova data de lançamento e clique em "Salvar". Você também deve inserir um comentário
no campo "Motivo para colocar em espera".


Observe o seguinte:


* Todas as compras que foram suspensas não serão incluídas na tabela de referências de uma entrada de pagamento
* A data de lançamento não pode estar no passado.
* Você só pode bloquear ou desbloquear uma fatura de compra se ela não for paga.
* Você só poderá alterar a data de liberação se a fatura não estiver paga.


### 5. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Tributação baseada em itens](/docs/pt/accounts/item-tax-template)
3. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
4. [Solicitação de pagamento](/docs/pt/accounts/payment-request)
5. [Solicitação de cotação](/docs/pt/buying/request-for-quotation)
6. [Pedido de compra](/docs/pt/buying/purchase-order)
7. [Recibo de compra](/docs/pt/stock/purchase-receipt)



