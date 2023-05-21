# configurações de contas


Existem várias configurações de conta no ERPNext para restringir e configurar ações no módulo Contabilidade.


## Configurações de transações


![Configurações de transações](/files/CleanShot 2021-08-26 às 11.56.43@2xff68e5.png)


### 1. Subsídio de sobrefaturamento (%)


A porcentagem pela qual você pode superfaturar as transações. Por exemplo, se o valor do pedido for $ 100 para um item e a porcentagem aqui for definida como 10%, você poderá cobrar $ 110.


### 2. Função permitida para superfaturamento


Os usuários com esta função têm permissão para faturar acima da porcentagem permitida.


### 3. Função permitida para contornar o limite de crédito


Selecione a função que tem permissão para enviar transações que excedam os limites de crédito definidos. O limite de crédito pode ser definido no formulário Cliente.


### 4. Verifique a unicidade do número da fatura do fornecedor


Quando marcado, não serão permitidas Notas Fiscais de Compra com o mesmo 'Nº da Fatura do Fornecedor'. Isso é útil para evitar entradas duplicadas.


### 5. Desvincular o Pagamento no Cancelamento da Fatura


Se marcado, o sistema desvinculará o pagamento da respectiva fatura. Por padrão, se uma entrada de pagamento for enviada, a fatura vinculada não poderá ser cancelada até que a entrada de pagamento também seja cancelada. Ao desvincular, agora você pode cancelar e alterar as faturas. Mas os pagamentos não podem ser vinculados e considerados como pagamentos antecipados.


### 6. Obtenha automaticamente as condições de pagamento do pedido


Ativar isso buscará automaticamente as condições de pagamento de um pedido de compra/venda para sua fatura de compra/venda vinculada.


### 7. Excluir entradas contábeis e de estoque ao excluir a transação


Habilitar isso permitirá a exclusão de entradas vinculadas do Razão Geral e do Razão de Estoque ao excluir faturas e recibos. Isso pode ser verificado se você não quiser perder a ID do documento após cancelá-lo. Agora você pode cancelar e excluir o documento para obter o mesmo ID de documento novamente.


### 8. Registrar entrada de depreciação de ativos automaticamente


Quando marcada, uma entrada automática para a depreciação de um ativo será criada com base na primeira data definida. Por exemplo, a depreciação anual de um item será agendada para os próximos 3/4 anos com base no número de depreciações registradas definido no mestre de ativos. Para mais detalhes, visite a página [Depreciação de ativos](/docs/v13/user/manual/en/asset/asset-depreciation).


### 9. Desvincular o Pagamento Antecipado no Cancelamento do Pedido


Semelhante à opção anterior, isso desvincula quaisquer pagamentos antecipados feitos contra Pedidos de Compra/Venda.


### 10. Habilitar Contabilidade de Parte Comum


Se marcada, uma entrada de diário de ajuste será lançada automaticamente na criação de faturas de vendas/compras contra clientes e fornecedores comuns. Para mais detalhes, visite [Common Party Accounting](/docs/v13/user/manual/en/accounts/articles/common_party_accounting)


### 11. Criar entradas de razão para alterar o valor


Se marcado, para uma fatura de Ponto de Venda, o sistema lançará lançamentos contábeis considerando o valor de alteração fornecido.


### 12. Habilitar Contabilidade de Desconto


Se marcada, as Contas de Desconto podem ser adicionadas na tabela de Itens das Notas Fiscais, o que permitirá contabilizar de forma mais eficiente os Descontos aplicados nos Itens. Também permite adicionar contas de desconto padrão para itens, que serão buscadas automaticamente quando o item for adicionado a uma fatura de venda.


## Configurações de impostos


![Configurações de impostos](/files/Tax_Settings_Revised.png)


### 1. Determinar a categoria de imposto de endereço de


[Categoria fiscal](/docs/v13/user/manual/en/accounts/tax-category) pode ser definido em Endereços. Um endereço pode ser um endereço de envio ou de cobrança. Defina qual endereço selecionar ao aplicar a categoria de imposto.


### 2. Adicionar impostos e cobranças automaticamente a partir do modelo de imposto do item


Habilitar isso preencherá a tabela de impostos nas transações se um [modelo de imposto de item](/docs/v13/user/manual/en/accounts/item-tax-template) for definido para um item e esse item for selecionado na transação.


### 3. Contabilizar Perda Fiscal sobre Desconto por Pagamento Antecipado


Habilitar isso dividirá as deduções de desconto da Entrada de pagamento em Perda de receita e Perda de imposto se o documento contra a Entrada de pagamento tiver um [Desconto de pagamento antecipado](/docs/v14/user/manual/en/accounts/payment-terms#11-setting -up-discount-on-early-payments).


## Configurações de fechamento do período


![Configurações de fechamento de período](/files/Configurações de fechamento de período.png)


### 1. Contas congeladas até a data


Congele as transações contábeis até a data especificada, ninguém pode fazer/modificar a entrada, exceto a função especificada.


### 2. Função permitida para definir contas congeladas e editar entradas congeladas


Os usuários com esta função têm permissão para definir contas congeladas e criar/modificar lançamentos contábeis em relação a contas congeladas.


## Configurações de Contabilidade Diferida


![Deferred Accounting Settings](/files/Deferred Accounting Settings .png)


### 1. Registrar entradas diferidas com base em


O valor da receita diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é "Dias". Se "Dias" for selecionado, o valor da receita diferida será contabilizado com base no número de dias de cada mês e, se "Meses" for selecionado, será contabilizado com base no número de meses. **Por exemplo:** Se "Dias" for selecionado e a receita de US$ 12.000 tiver que ser adiada por um período de 12 meses, US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. Se "Meses" for selecionado, a receita diferida de US$ 1.000 será registrada a cada mês, independentemente do número de dias em um mês.


### 2. Processar entrada contábil diferida automaticamente


Essa configuração é habilitada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida terá que ser processada manualmente usando [Processar contabilidade diferida](/docs/v13/user/manual/en/accounts/process-deferred-accounting)


### 3. Registrar lançamentos diferidos por meio de lançamento contábil manual


Por padrão, as entradas do razão são lançadas diretamente para contabilizar receitas diferidas em relação a uma fatura. Para contabilizar esse lançamento de valor diferido por meio do lançamento contábil manual, essa opção pode ser habilitada.


### 4. Enviar entradas de diário


Esta opção é aplicável somente se os lançamentos contábeis diferidos forem lançados por meio do lançamento contábil manual. Por padrão, os lançamentos contábeis adiados são mantidos no estado Rascunho e o usuário precisa verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver habilitada, os lançamentos contábeis manuais serão enviados automaticamente sem qualquer intervenção do usuário. Esta opção só será exibida se a opção **Livrar lançamentos diferidos via lançamento contábil** estiver marcada.


## Configurações de impressão


![Configurações de impressão](/files/Print Settings.png)


### 1. Mostrar imposto inclusivo na impressão


Os impostos aplicados serão mostrados na visualização de impressão.


### 2. Mostrar cronograma de pagamento na impressão


A tabela Cronograma de pagamento é visível usando [Condições de pagamento](/docs/v13/user/manual/en/accounts/payment-terms). Ativar isso mostrará esta tabela na exibição de impressão.


## Configurações de câmbio


![Configurações de Câmbio](/files/Configurações de Câmbio .png)


### 1. Permitir taxas de câmbio obsoletas


Isso deve ser desmarcado se você deseja que o ERPNext verifique a idade dos registros buscados no Câmbio em transações em moeda estrangeira. Se estiver desmarcada, o campo da taxa de câmbio será somente leitura nos documentos.


Stale Days é o número de dias a ser usado ao decidir se um registro de Câmbio está obsoleto. Isso é válido quando 'Permitir taxas obsoletas' está **desativado**. Portanto, se Stale Days for definido como 10, serão permitidas taxas obsoletas de 10 dias. Se Permitir taxas obsoletas estiver ativado, não há limite de tempo para a idade das taxas obsoletas.


Se as taxas obsoletas estiverem habilitadas, a ordem de busca é:


* Taxa mais recente do formulário de câmbio
* Se nenhuma moeda de troca for encontrada, a taxa mais recente conforme o mercado é buscada automaticamente


Se as taxas obsoletas estiverem desativadas, a ordem de busca é:


* Taxa mais recente do formulário de câmbio até o número de dias definido em 'Dias obsoletos'
* Se nenhuma moeda de troca for encontrada, a taxa mais recente conforme o mercado é buscada automaticamente


## Configurações do relatório


![Configurações do relatório](/files/Report Settings.png)


### 1. Use o formato de fluxo de caixa personalizado


Você pode optar por usar Formatos de fluxo de caixa personalizados para personalizar a aparência do relatório de fluxo de caixa. Para saber mais, [visite esta página](/docs/v13/user/manual/en/accounts/articles/how-to-customize-cash-flow-report).