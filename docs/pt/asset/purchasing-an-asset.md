# Comprar um ativo



Para comprar um novo recurso:


1. Criar uma categoria de recurso
2. Crie um item relacionado com 'É ativo fixo' ativado para criar o ativo.
3. Você também pode ativar a opção 'Criar ativos automaticamente na compra' para criar ativos automaticamente. (Opcional)


![Comprar ativo](/files/asset-auto-create.png)
4. Então, o [ciclo de compra](/docs/pt/buying/purchase-order) deve ser seguido para comprar um ativo.
5. Insira o local do ativo na tabela Itens do [Recibo de compra](/docs/pt/stock/purchase-receipt) ou [Fatura de compra](/docs/pt/accounts/purchase-invoice) através da qual você está recebendo o item.
6. Ao enviar um recibo de compra, com base na caixa de seleção de criação automática, os registros de ativos serão criados automaticamente. Você pode então inserir outros detalhes do Ativo manualmente no formulário do Ativo.


![Comprar ativo](/files/asset-auto-create-on-purchase.png)


Os seguintes lançamentos contábeis serão lançados no envio da entrada de recibo se a contabilidade do trabalho de capital em andamento estiver habilitada na categoria de ativo do ativo adquirido.


![Asset](/files/asset-purchase-receipt-gl-entries.png)


É perceptível aqui que, em vez da conta de ativos correspondente, foi debitado Capital Work in Progress (CWIP). Isso ocorre porque o ativo acabou de ser adquirido e ainda não está disponível para uso. Até que o ativo esteja disponível para uso, o valor do ativo é mantido nesta conta. No dia em que estiver disponível para uso, a conta CWIP será creditada e a conta do ativo correspondente será debitada.


No caso de 'Contabilidade de trabalho de capital em andamento' desativada na categoria de ativos, o lançamento do recebimento será feito nas contas de ativos correspondentes definidas na categoria de ativos.


O ERPNext também usa uma conta temporária "Ativo Recebido mas Não Faturado" (uma conta de passivo) que é creditada no envio da entrada do Recibo de Compra. Posteriormente, ao enviar a fatura de compra, esta conta é debitada/estornada.


#### Tópicos Relacionados


1. [Ativo](/docs/pt/asset/asset)
2. [Recibo de compra](/docs/pt/stock/purchase-receipt)
3. [Fatura de compra](/docs/pt/accounts/purchase-invoice)



