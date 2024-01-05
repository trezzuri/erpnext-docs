# Citação



**Uma cotação é um custo estimado dos produtos/serviços que você está vendendo ao seu cliente futuro/presente.**


Durante uma venda, um cliente pode solicitar uma observação sobre os produtos
ou serviços que você planeja oferecer junto com os preços e outros termos
de engajamento. Isto tem muitos nomes como "Proposta", Estimativa", "Pro Forma
Fatura" ou uma **Cotação**.


Para acessar a lista de cotações, acesse:



> 
> Home > Vendas > Vendas > Cotação
> 
> 
> 


Um fluxo de vendas típico é semelhante a:


![Fazer cotação a partir da oportunidade](/files/selling-flow-quo.png)


Uma cotação contém detalhes sobre:


* O destinatário da cotação
* Os itens e as quantidades que você está oferecendo.
* As taxas em que são oferecidas.
* Os impostos aplicáveis.
* Outras despesas (como frete, seguro), se aplicável.
* A validade do contrato.
* O momento da entrega.
* Outras condições.



> 
> Dica: as imagens ficam ótimas em citações. Certifique-se de que seus itens tenham uma imagem anexada.
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma cotação, é aconselhável que você crie primeiro o seguinte:


* [Cliente](/docs/pt/CRM/customer)
* [Líder](/docs/pt/CRM/lead)
* [Item](/docs/pt/stock/item)


## 2. Como criar uma cotação


1. Vá para a lista de cotações e clique em Novo.
2. Selecione se a cotação é para um cliente ou lead no campo "Cotação para".
3. Insira o nome do cliente/lead.
4. Insira uma data Válida até após a qual o valor cotado será considerado inválido.
5. O tipo de pedido pode ser Vendas, Manutenção ou Carrinho de compras. O carrinho de compras é para o carrinho de compras do site e não deve ser criado a partir daqui.
6. Adicione os Itens e suas quantidades na tabela de itens, os preços serão buscados automaticamente no Preço do Item. Você também pode buscar itens de uma oportunidade clicando em Obter itens de > Oportunidade.
7. Adicione impostos e cobranças adicionais, conforme aplicável.
8. Salvar.


Você também pode criar uma cotação a partir de uma oportunidade mostrada a seguir.


![Fazer cotação a partir da oportunidade](/files/make-quote-from-opp.png)


## 3. Recursos


### 3.1 Endereço e contato


Nesta seção há quatro campos:


* **Endereço do cliente:** este é o endereço de cobrança do cliente.
* **Endereço de envio:** Endereço para onde os itens serão enviados.
* **Pessoa de contato:** se seu cliente for uma organização, você poderá adicionar a pessoa para contato neste campo.
* **Território:** Região onde o cliente pertence. O padrão é Todos os Territórios.


### 3.2 Moeda e lista de preços


Você pode definir a moeda na qual a cotação/pedido de venda será enviada. Se você definir uma Lista de Preços, os preços dos itens serão obtidos dessa lista. Marcar Ignorar regra de preços ignorará as regras de preços definidas em Contas > Regra de preços.


Leia sobre as [listas de preços](/docs/pt/stock/price-lists)
e [transações em várias moedas](/docs/pt/accounts/articles/managing-transactions-in-multiple-currency)
para saber mais.


### 3.3 A tabela de itens


Esta tabela pode ser expandida clicando no triângulo invertido presente na extremidade direita da tabela.


* Ao selecionar o Código do Item, o seguinte será obtido automaticamente: nome do item, descrição, qualquer imagem se definida, quantidade padrão como 1, as taxas. Você pode adicionar descontos na seção Descontos e Margens.
* **Em Desconto e Margem** você pode adicionar margem extra para lucro ou dar um desconto. Ambos podem ser definidos com base em valor ou porcentagem. A taxa final será mostrada abaixo na seção Taxa. Você pode atribuir um modelo de imposto de item criado especificamente para um item.
* **Os pesos dos itens** serão obtidos se definidos no item mestre.
* Em **Armazém e Referência**, o armazém será buscado no Cadastro de itens, este é o armazém onde seu estoque está presente.
* Em **Planejamento** você pode ver a quantidade projetada e a quantidade real presente. Para saber mais sobre esses campos, [clique aqui](/docs/pt/stock/projected-quantity). Se você clicar no botão 'Saldo de estoque', você será direcionado para um tipo de documento onde poderá gerar um relatório de estoque para o item.
* **Carrinho de compras**, notas adicionais são para transações no site. Notas sobre o item serão obtidas aqui quando adicionadas por meio de um carrinho de compras. Por exemplo: torne a comida ainda mais picante. *Introduzido na v12*
* **Quebra de página** Criará uma quebra de página logo antes deste item durante a impressão.
* Você pode inserir linhas abaixo/acima, duplicar, mover ou excluir linhas nesta tabela.
* Dica: você também pode fazer download da tabela de itens em formato CSV e carregá-la em outra transação.


A quantidade total, taxa e peso líquido de todos os itens serão mostrados abaixo da tabela de itens. A taxa mostrada aqui é antes de impostos.


#### 3.3.1 Itens alternativos


Você pode adicionar itens manualmente e marcá-los como alternativos marcando a caixa de seleção **É alternativo** na linha da tabela de itens. Esses itens não serão contabilizados nos impostos e totais da Cotação.


![Cotação com itens alternativos e totais](/files/quotation-with-alternatives-and-totals.png)



> 
> É importante manter a ordem correta, ou seja, as linhas de itens alternativos devem seguir uma linha de itens não alternativos (o item ao qual são alternativas). O agrupamento será feito nesta base.
> 
> 
> 


FSH-ROD-001, FSH-ROD-002 e FSH-ROD-003 são tratados como um grupo para seleção. Desta forma, você pode fornecer alternativas ao seu cliente/lead e ele pode selecionar entre elas.


A seleção dos itens a serem seguidos ocorre após o envio da Cotação. Visite a seção [Selecionando alternativas](#selecting-alternatives) desta página para saber mais.


### 3.4 Impostos e Taxas


Para adicionar impostos à sua cotação, você pode selecionar um [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template) ou adicione os impostos manualmente na tabela Impostos e Encargos sobre Vendas.


O total de impostos e taxas será exibido abaixo da tabela. Clicar em Tax Breakup mostrará todos os componentes e valores.


![Impostos na cotação](/files/quotation-taxes.png)


Para adicionar impostos automaticamente por meio de uma categoria de imposto, visite [esta página](/docs/pt/accounts/tax-category).


#### Regra de envio


Uma regra de envio ajuda a definir o custo de envio de um item. O custo geralmente aumenta com a distância do envio. Para saber mais, visite a página [Regras de envio](/docs/pt/selling/shipping-rule).


### 3,5 desconto adicional


Além de oferecer desconto por item, você pode adicionar um desconto a toda a cotação nesta seção. Este desconto pode ser baseado no total geral, ou seja, após impostos/encargos, ou no total líquido, ou seja, antes de impostos/encargos. O desconto adicional pode ser aplicado como uma porcentagem ou um valor.


Leia [Aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.6 Condições de pagamento


Às vezes o pagamento não é feito de uma só vez. Dependendo do acordo, metade do pagamento poderá ser feito antes do envio e a outra metade após o recebimento da mercadoria/serviço. Você pode adicionar um modelo de condições de pagamento ou adicionar os termos manualmente nesta seção.


![Condições de pagamento na cotação](/files/quotation-payment-terms.png)


Leia as [Condições de pagamento](/docs/pt/accounts/payment-terms) para saber mais.


### 3.7 Termos e Condições


Em transações de Vendas/Compras pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)


### 3.8 Configurações de impressão


#### Papel timbrado


Você pode imprimir sua cotação/pedido de venda em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


'Agrupar os mesmos itens' agrupará os mesmos itens adicionados diversas vezes na tabela de itens. Isso pode ser visto quando você imprimir.


#### Imprimir títulos


As cotações também podem ser intituladas como “Fatura Proforma” ou “Proposta”.
Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


### 3.9 Mais informações


* **Campanha:** Uma campanha de vendas pode ser associada à cotação. Um conjunto de cotações pode fazer parte de uma campanha de vendas.
* **Fonte:**Um tipo de Fonte de Lead pode ser vinculado se estiver citando um lead, seja de uma campanha, de um fornecedor, de uma exposição etc. Selecione Cliente existente se estiver fazendo uma cotação para um cliente.
* **Cotação do fornecedor:** Uma cotação do fornecedor pode ser vinculada para comparação com sua cotação atual para um comprador. Você pode ter uma ideia do lucro/perda comparando os dois.


### 3.10 Envio da cotação


A cotação é uma transação “submissível”. Ao clicar em Salvar, um rascunho é salvo; ao enviar, ele é enviado permanentemente. Desde que você envia esta cotação para
seu Cliente ou Lead, você deverá congelá-lo para que não sejam feitas alterações após
você envia a cotação.


Ao enviar, você pode criar um Pedido de Venda ou uma Assinatura a partir da Cotação usando o botão Criar. No Dashboard presente na parte superior, você pode acessar o Pedido de Venda vinculado a esta Cotação. Caso não dê certo, você pode definir a cotação como perdida clicando no botão 'Definir como perdida'.


![Cotação enviada](/files/submitted-quotation.png)


#### 3.10.1 Selecionando alternativas


Se a cotação contiver itens alternativos, você será solicitado a selecionar uma das alternativas ao criar um pedido de venda a partir da cotação.


![Selecionar entre alternativas de cotação para pedido de vendas](/files/select-alternatives-from-quotation56df70.png)


Como você pode ver, FSH-ROD-002 e FSH-ROD-003 são alternativas ao FSH-ROD-001 que são oferecidas ao Cliente.


Um deles será acordado e selecionado, após o qual o item selecionado será mapeado.
![pedido de venda a partir de cotação com alternativas](/files/sales-order-from-quotation-with-alternatives.png)


Se estiverem envolvidos itens simples (sem alternativas), eles serão mapeados normalmente.



> 
> A possibilidade de selecionar itens alternativos antes do mapeamento só está disponível durante a criação de pedidos de vendas a partir de **cotações individuais**.
>  Se 'Obter itens de' for usado em um pedido de venda ou fatura de venda para buscar itens de cotação, somente itens não alternativos serão buscados e nenhuma seleção de item será solicitada.
> 
> 
> 


### 4. Tópicos Relacionados


1. [Aplicar desconto](/docs/pt/selling/articles/applying-discount)



