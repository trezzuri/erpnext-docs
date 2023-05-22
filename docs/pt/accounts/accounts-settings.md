# Configurações de contas


Existem várias configurações de conta no SOMA para restringir e configurar ações no módulo Contabilidade.


## Configurações de transações


![Transactions Settings](/files/CleanShot 2021-08-26 às 11.56.43@2xff68e5.png)


### 1. Subsídio de sobrefaturamento (%)


A porcentagem pela qual você pode superfaturar as transações. Por exemplo, se o valor do pedido for $ 100 para um item e a porcentagem aqui for definida como 10%, você poderá cobrar $ 110.


### 2. Função permitida para sobrefaturar


Usuários com esta função têm permissão para faturar acima da porcentagem permitida.


### 3. Função permitida para ignorar o limite de crédito


Selecione a função que tem permissão para enviar transações que excedam os limites de crédito definidos. O limite de crédito pode ser definido no formulário Cliente.


### 4. Verifique a singularidade do número da fatura do fornecedor


Quando marcado, Faturas de Compra com o mesmo 'Nº da Fatura do Fornecedor' não serão permitidas. Isso é útil para evitar entradas duplicadas.


### 5. Desvincular pagamento no cancelamento da fatura


Se marcada, o sistema desvinculará o pagamento da respectiva fatura. Por padrão, se uma entrada de pagamento for enviada, a fatura vinculada não poderá ser cancelada até que a entrada de pagamento também seja cancelada. Ao desvincular, agora você pode cancelar e alterar as faturas. Mas os pagamentos não podem ser vinculados e considerados como adiantamentos.


### 6. Obter automaticamente as condições de pagamento do pedido


Ativar isso buscará automaticamente as condições de pagamento de um pedido de compra/venda para sua fatura de compra/venda vinculada.


### 7. Excluir entradas contábeis e de estoque na exclusão da transação


Ativar isso permitirá a exclusão de entradas vinculadas do Razão Geral e do Razão de Estoque ao excluir faturas e recibos. Isso pode ser verificado se você não quiser perder a ID do documento após cancelá-lo. Agora você pode cancelar e excluir o documento para obter o mesmo ID de documento novamente.


### 8. Registrar entrada de depreciação de ativos automaticamente


Quando marcada, uma entrada automática para a depreciação de um ativo será criada com base na primeira data definida. Por exemplo, a depreciação anual de um item será agendada para os próximos 3/4 anos com base no número de depreciações registradas definido no mestre de ativos. Para obter mais detalhes, visite a página [Depreciação de ativos](/docs/pt/asset/asset-depreciation).


### 9. Desvincular o pagamento antecipado no cancelamento do pedido


Semelhante à opção anterior, isso desvincula quaisquer pagamentos antecipados feitos contra pedidos de compra/venda.


### 10. Habilitar Contabilidade de Parte Comum


Se marcada, uma entrada de diário de ajuste será lançada automaticamente na criação de faturas de vendas/compras contra clientes e fornecedores comuns. Para obter mais detalhes, visite [Contabilidade de partes comuns](/docs/pt/accounts/articles/common_party_accounting)


### 11. Criar entradas de razão para alterar o valor


Se marcado, para uma fatura de ponto de venda, o sistema lançará lançamentos contábeis considerando o valor da alteração fornecido.


### 12. Habilitar Contabilidade de Desconto


Se marcada, as Contas de Desconto podem ser adicionadas na tabela de Itens das Notas Fiscais, o que permitirá contabilizar os Descontos aplicados nos Itens com mais eficiência. Também permite adicionar contas de desconto padrão para itens, que serão buscadas automaticamente quando o item for adicionado a uma fatura de venda.


## Configurações de impostos


![Tax Settings](/files/Tax_Settings_Revised.png)


### 1. Determinar categoria de imposto de endereço de


[Categoria fiscal](/docs/pt/accounts/tax-category) pode ser definida em Endereços. Um endereço pode ser um endereço de envio ou de cobrança. Defina qual endereço selecionar ao aplicar a categoria fiscal.


### 2. Adicionar automaticamente impostos e cobranças do modelo de imposto do item


Ativar isso preencherá a tabela de impostos nas transações se um [Modelo de imposto de item](/docs/pt/accounts/item-tax-template) estiver definido para um Item e esse Item é selecionado na transação.


### 3. Contabilizar Perda Fiscal sobre Desconto de Pagamento Antecipado


Habilitar isso dividirá as deduções de desconto da Entrada de pagamento em Perda de receita e Perda de imposto se o documento contra a Entrada de pagamento tiver um [Desconto de pagamento antecipado](/docs/pt/accounts/payment-terms#11 -setting-up-discount-on-early-payments) definido.


## Configurações de fechamento do período


![Configurações de fechamento de período](/files/Configurações de fechamento de período.png)


### 1. Contas congeladas até a data


Congelar as transações contábeis até a data especificada, ninguém pode fazer/modificar a entrada, exceto a função especificada.


### 2. Função com permissão para definir contas congeladas e editar entradas congeladas


Os usuários com esta função têm permissão para definir contas congeladas e criar/modificar lançamentos contábeis em relação a contas congeladas.


## Configurações de contabilidade diferida


![Deferred Accounting Settings](/files/Deferred Accounting Settings .png)


### 1. Reservar entradas diferidas com base em


O valor da receita diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é "Dias". Se "Dias" for selecionado, o valor da receita diferida será contabilizado com base no número de dias de cada mês e, se "Meses" for selecionado, será contabilizado com base no número de meses. **Por exemplo:** Se "Dias" for selecionado e a receita de US$ 12.000 tiver que ser adiada por um período de 12 meses, então US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. Se "Meses" for selecionado, a receita diferida de US$ 1.000 será registrada a cada mês, independentemente do número de dias em um mês.


### 2. Processar entrada contábil diferida automaticamente


Esta configuração é habilitada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida terá que ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)


### 3. Registrar lançamentos diferidos por meio de lançamento no diário


Por padrão, as entradas do razão são lançadas diretamente para contabilizar receita diferida em relação a uma fatura. Para contabilizar esse lançamento de valor diferido por meio do lançamento contábil manual, essa opção pode ser habilitada.


### 4. Enviar entradas de diário


Esta opção é aplicável apenas se os lançamentos contábeis diferidos forem lançados por meio do lançamento contábil manual. Por padrão, os lançamentos contábeis adiados são mantidos no estado Rascunho e o usuário precisa verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver habilitada, os lançamentos contábeis manuais serão enviados automaticamente sem qualquer intervenção do usuário. Esta opção só será exibida se a opção **Livrar lançamentos diferidos via lançamento contábil manual** estiver marcada.


## Configurações de impressão


![Configurações de impressão](/files/Print Settings.png)


### 1. Mostrar imposto inclusivo na impressão


Os impostos aplicados serão mostrados na visualização de impressão.


### 2. Mostrar cronograma de pagamento na impressão


A tabela Cronograma de pagamento está visível usando [Condições de pagamento](/docs/pt/accounts/payment-terms). Ativar isso mostrará esta tabela na visualização de impressão.


## Configurações de câmbio


![Configurações de câmbio](/files/Configurações de câmbio de moeda .png)


### 1. Permitir taxas de câmbio obsoletas


Esta opção deve ser desmarcada se você deseja que o SOMA verifique a idade dos registros obtidos do Câmbio em transações em moeda estrangeira. Se estiver desmarcado, o campo de taxa de câmbio será somente leitura em documentos.


Stale Days é o número de dias a ser usado ao decidir se um registro de Câmbio está obsoleto. Isso é válido quando 'Permitir taxas obsoletas' está **desativado**. Portanto, se Stale Days for definido como 10, serão permitidas taxas obsoletas de 10 dias. Se Permitir taxas obsoletas estiver ativado, não há limite de tempo para a idade das taxas obsoletas.


Se as taxas obsoletas estiverem habilitadas, a ordem de busca é:


* Última taxa do formulário de câmbio
* Se nenhuma moeda de troca for encontrada, a taxa mais recente conforme o mercado é buscada automaticamente


Se as taxas obsoletas estiverem desativadas, a ordem de busca é:


* Última taxa do formulário de câmbio até o número de dias definido em 'Stale Days'
* Se nenhuma moeda de troca for encontrada, a taxa mais recente conforme o mercado é buscada automaticamente


## Configurações de relatório


![Report Settings](/files/Report Settings.png)


### 1. Use o formato de fluxo de caixa personalizado


Você pode optar por usar formatos de fluxo de caixa personalizados para personalizar a aparência do relatório de fluxo de caixa. Para saber mais, [visite esta página](/docs/pt/accounts/articles/how-to-customise-cash-flow-report).

