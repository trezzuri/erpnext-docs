# Configurações da conta



Existem várias configurações de conta no ERPNext para restringir e configurar ações no módulo Contabilidade.


## Configurações de transações


![Configurações de transações](/files/CleanShot 2021-08-26 at 11.56.43@2xff68e5.png)


### 1. Sobretaxa de faturamento (%)


A porcentagem pela qual você pode faturar a mais nas transações. Por exemplo, se o valor do pedido for US$ 100 para um item e a porcentagem aqui for definida como 10%, você poderá cobrar US$ 110.


### 2. Função com permissão para superfaturar


Os usuários com esta função podem faturar acima da porcentagem permitida.


### 3. Função com permissão para ignorar o limite de crédito


Selecione a função que tem permissão para enviar transações que excedam os limites de crédito definidos. O limite de crédito pode ser definido no formulário do Cliente.


### 4. Verifique a exclusividade do número da fatura do fornecedor


Quando marcada, não serão permitidas faturas de compra com o mesmo 'Nº da fatura do fornecedor'. Isso é útil para evitar entradas duplicadas.


### 5. Desvincular pagamento no cancelamento da fatura


Se marcado, o sistema desvinculará o pagamento da respectiva fatura. Por padrão, se um Lançamento de Pagamento for enviado, a fatura vinculada não poderá ser cancelada até que o Lançamento de Pagamento também seja cancelado. Ao desvincular, agora você pode cancelar e alterar as faturas. Mas os pagamentos não serão vinculados e considerados adiantamentos.


### 6. Buscar automaticamente as condições de pagamento do pedido


Ativar esta opção irá buscar automaticamente as condições de pagamento de um pedido de compra/venda para sua fatura de compra/venda vinculada.


### 7. Excluir entradas contábeis e contábeis de estoque ao excluir a transação


Ativar esta opção permitirá a exclusão de entradas vinculadas do Razão Geral e da Contabilidade de Estoque ao excluir faturas e recebimentos. Isso pode ser verificado se você não quiser perder o ID do documento após cancelar o documento. Agora você pode cancelar e excluir o documento para obter o mesmo ID do documento novamente.


### 8. Registrar entrada de depreciação de ativos automaticamente


Quando marcada, será criada uma entrada automática para uma depreciação de ativo com base na primeira data definida. Por exemplo, a depreciação anual de um item será programada para os próximos 3/4 anos com base no Número de depreciações registradas definido no cadastro de ativos. Para obter mais detalhes, visite a página [Depreciação de ativos](/docs/pt/asset/asset-depreciation).


### 9. Desvincular pagamento antecipado no cancelamento do pedido


Semelhante à opção anterior, isso desvincula quaisquer pagamentos antecipados feitos em relação a pedidos de compra/venda.


### 10. Ativar contabilidade de partes comuns


Se marcado, um lançamento contábil manual de ajuste será lançado automaticamente na criação de faturas de vendas/compra em relação a clientes e fornecedores comuns. Para obter mais detalhes, visite [Contabilidade de partes comuns](/docs/pt/accounts/articles/common_party_accounting)


### 11. Criar entradas contábeis para valor de alteração


Se marcada, para uma fatura de ponto de venda, o sistema lançará entradas no razão considerando o valor da alteração fornecido.


### 12. Ativar contabilidade de descontos


Se marcada, as Contas de Desconto poderão ser adicionadas na tabela de Itens das Faturas de Vendas, o que permitirá contabilizar os Descontos aplicados nos Itens de forma mais eficiente. Também permite adicionar contas de desconto padrão para itens, que serão buscadas automaticamente quando o item for adicionado a uma fatura de vendas.


## Configurações fiscais


![Configurações fiscais](/files/Tax_Settings_Revised.png)


### 1. Determinar a categoria de imposto de endereço de


[Categoria fiscal](/docs/pt/accounts/tax-category) pode ser definida em Endereços. Um endereço pode ser endereço de envio ou cobrança. Defina quais endereços selecionar ao aplicar a categoria fiscal.


### 2. Adicionar automaticamente impostos e cobranças do modelo de imposto de item


Ativar esta opção preencherá a tabela Impostos nas transações se um [Modelo de imposto de item](/docs/pt/accounts/item-tax-template) estiver definido para um Item e esse item é selecionado na transação.


### 3. Reservar prejuízo fiscal com desconto por pagamento antecipado


Ativar esta opção dividirá as deduções de desconto da Entrada de Pagamento em Perda de Renda e Perda Fiscal se o documento da Entrada de Pagamento tiver um [Desconto por pagamento antecipado](/docs/pt/accounts/payment-terms#11-setting-up-discount-on-early-payments) definido.


## Configurações de encerramento do período


![Configurações de encerramento de período](/files/Configurações de encerramento de período.png)


### 1. Contas congeladas até a data


Congelar transações contábeis até a data especificada, ninguém pode fazer/modificar entradas, exceto a função especificada.


### 2. Função com permissão para definir contas congeladas e editar entradas congeladas


Os usuários com esta função têm permissão para definir contas congeladas e criar/modificar lançamentos contábeis em contas congeladas.


## Configurações de contabilidade diferida


![Configurações de contabilidade diferida](/files/Configurações de contabilidade diferida.png)


### 1. Reservar entradas diferidas com base em


O valor da receita diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é “Dias”. Se "Dias" for selecionado, o valor da receita diferida será contabilizado com base no número de dias de cada mês e se "Meses" for selecionado, então será contabilizado com base no número de meses. **Por exemplo:** se "Dias" for selecionado e a receita de US$ 12.000 tiver que ser diferida durante um período de 12 meses, então US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. dias. Se "Meses" for selecionado, a receita diferida de US$ 1.000 será reservada a cada mês, independentemente do número de dias do mês.


### 2. Processar automaticamente lançamento contábil diferido


Esta configuração está habilitada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida deverá ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)


### 3. Registrar lançamentos diferidos por meio de lançamento contábil manual


Por padrão, as entradas do razão são lançadas diretamente para contabilizar receitas diferidas em relação a uma fatura. Para contabilizar esse lançamento de valor diferido via lançamento contábil manual, esta opção pode ser habilitada.


### 4. Enviar entradas de diário


Essa opção é aplicável somente se os lançamentos contábeis diferidos forem lançados por meio do lançamento contábil manual. Por padrão, os lançamentos contábeis manuais para lançamento diferido são mantidos no estado Rascunho e o usuário deve verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver habilitada, os lançamentos contábeis manuais serão enviados automaticamente sem qualquer intervenção do usuário. Esta opção só será exibida se **Livrar Lançamentos Diferidos Via Lançamento Contábil** estiver marcado.


## Configurações de impressão


![Configurações de impressão](/files/Print Settings.png)


### 1. Mostrar imposto inclusivo impresso


Os impostos aplicados serão mostrados na visualização de impressão.


### 2. Mostrar cronograma de pagamento impresso


A tabela Cronograma de pagamento é visível usando [Termos de pagamento](/docs/pt/accounts/payment-terms). Ativar isso mostrará esta tabela na visualização de impressão.


## Configurações de câmbio


![Configurações do Câmbio](/files/Configurações do Câmbio.png)


### 1. Permitir taxas de câmbio obsoletas


Isso deve ser desmarcado se você quiser que o ERPNext verifique a idade dos registros obtidos do Câmbio em transações em moeda estrangeira. Se estiver desmarcado, o campo taxa de câmbio ficará somente leitura nos documentos.


Dias obsoletos é o número de dias a serem usados ​​para decidir se um registro de câmbio está obsoleto. Isso é válido quando 'Permitir taxas obsoletas' está **desativado**. Portanto, se os dias obsoletos forem definidos como 10, serão permitidas taxas obsoletas de 10 dias. Se a opção Permitir taxas obsoletas estiver ativada, não há limite de tempo para a idade das taxas obsoletas.


Se as taxas obsoletas estiverem ativadas, a ordem de busca será:


* Taxa mais recente do formulário de câmbio
* Se nenhuma casa de câmbio for encontrada, a taxa mais recente de acordo com o mercado será obtida automaticamente


Se as taxas obsoletas estiverem desativadas, a ordem de busca será:


* Taxa mais recente do formulário de câmbio até o número de dias definido em 'Dias obsoletos'
* Se nenhuma casa de câmbio for encontrada, a taxa mais recente de acordo com o mercado será obtida automaticamente


## Configurações do relatório


![Configurações do relatório](/files/Configurações do relatório.png)


### 1. Use formato de fluxo de caixa personalizado


Você pode optar por usar formatos de fluxo de caixa personalizados para personalizar a aparência do relatório de fluxo de caixa. Para saber mais, [visite esta página](/docs/pt/accounts/articles/how-to-customise-cash-flow-report).



