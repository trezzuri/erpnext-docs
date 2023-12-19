# Perfil do ponto de venda



**No ERPNext, um perfil POS permite usar o recurso Ponto de Venda.**


O PDV inclui recursos avançados para atender a diferentes funcionalidades, como
gerenciamento de estoque, CRM, finanças, armazenamento, etc., todos integrados ao
Software de PDV. Antes do PDV moderno, todas essas funções eram realizadas
de forma independente e exigia a redigitação manual das informações, o que poderia
levar a erros de entrada.


Se você atua em operações de varejo, deseja que seu ponto de venda seja o mais rápido
e eficiente possível. Para fazer isso, você pode criar um perfil de PDV para um usuário.


Para acessar a lista de perfis de PDV, acesse:



> 
> Página inicial > Varejo > Operações de varejo > Perfil do ponto de venda
> 
> 
> 


## 1. Como criar um perfil PDV


1. Acesse o perfil do ponto de venda e clique em Novo.
2. Digite um nome para o perfil.
3. Selecione uma [Série de nomenclatura](/docs/pt/setting-up/settings/naming-series).
4. Defina uma conta de baixa e um centro de custos de baixa nos quais as transações serão registradas.
5. Configure as formas de pagamento na tabela, o padrão será dinheiro se nada for definido aqui. Somente os modos definidos aqui estarão disponíveis ao usar o POS. Depois de adicionar formas de pagamento, defina uma delas como forma de pagamento padrão marcando a caixa de seleção.


![Método de pagamento no perfil do PDV](/files/payment-method-in-pos.png)
6. Defina os valores padrão para as formas de pagamento (recomendado: 0).
7. Salvar.


![Perfil PDV](/files/pos-profile.png)


### 1.1 Opções adicionais ao criar um perfil de PDV


* **Cliente**: os usuários podem vender produtos específicos para clientes específicos no PDV adicionando grupos de itens e grupos de clientes no perfil do PDV.
* **Armazém**: As quantidades de estoque no Armazém selecionado serão afetadas para transações de PDV com este Perfil de PDV.
* **Campanha**: uma [campanha](/docs/pt/CRM/campaign) de vendas pode ser vinculada aqui para acompanhar o total de vendas em relação a ela .
* **Endereço da Empresa**: Se o balcão do PDV estiver configurado em uma filial da Empresa, o endereço poderá ser selecionado aqui.
* **Atualizar Estoque**: Se ativado, as quantidades de estoque serão afetadas quando as transações forem realizadas com o Perfil POS. Ou seja, os lançamentos no razão de estoque serão feitos quando você “enviar” esta fatura de vendas, eliminando assim a necessidade de uma nota de entrega separada.
* **Ignorar regra de precificação**: qualquer [regra de precificação](/docs/pt/accounts/pricing-rule) ativa será ignorada para isso Perfil PDV.
* **Permitir exclusão**: no PDV off-line, os dados são armazenados em cache. Marcar esta caixa de seleção permitirá que o usuário exclua a fatura de vendas armazenada em cache na fase Rascunho.
* **Permitir que o usuário edite a taxa**: O usuário do perfil POS terá permissão para editar a 'taxa' dos itens adicionados nas transações.
* **Permitir que o usuário edite o Desconto**: O usuário do Perfil PDV terá permissão para editar o 'Desconto' dos Itens adicionados nas transações.
* **Permitir impressão antes do pagamento**: Isso permitirá que o usuário do PDV imprima uma fatura antes do pagamento ser efetuado.
* **Exibir Itens em Estoque**: A quantidade restante de Itens do Armazém selecionado será mostrada ao Usuário do PDV.


## 2. Recursos


### 2.1 Aplicável a usuários


Por padrão, todos os usuários de vendas podem acessar os perfis POS criados no ERPNext. No entanto, se desejar que apenas determinados usuários acessem determinados perfis de PDV, você poderá adicioná-los à tabela. Depois que um usuário for definido no perfil de PDV, outros usuários não poderão usar esse perfil de PDV para transações de varejo.


**Definindo o perfil POS como padrão**: Ao marcar a caixa de seleção Padrão na tabela, o perfil POS atual se torna o perfil POS padrão para aquele usuário. Assim, na próxima vez que o Usuário efetuar login no sistema, o Perfil PDV estará definido por padrão.


![Usuário PDV](/files/pos-profile-default.png)



> 
> Nota: Se você especificar um usuário específico, a configuração do PDV será
>  aplicado apenas a esse usuário. Se a opção Usuário for deixada em branco, a configuração será
>  ser definido para todos os usuários. Para entender como funciona o PDV, visite a página [Ponto de Venda](/docs/pt/accounts/point-of-sales).
> 
> 
> 


### 2.2 Definindo grupo de itens e grupo de clientes


Ao definir um Grupo de Itens/Grupo de Clientes em um Perfil PDV, o grupo será selecionado automaticamente ao fazer transações com o Perfil PDV.


![Filtros no perfil PDV](/files/filters-in-pos-profile.png)


### 2.3 Configurações de impressão


![Configurações de impressão de PDV](/files/pos-profile-in-print-settings.png)


#### Formato de impressão para online


Você pode definir um formato de impressão que decidirá como será o layout do documento impresso. Para saber mais, visite a página [Formato de impressão](/docs/pt/setting-up/print/print-format).


#### Papel timbrado


Você pode imprimir sua Nota Fiscal de Vendas no PDV em papel timbrado da sua Empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


#### Imprimir títulos


Os títulos da fatura de vendas do PDV também podem ser alterados durante a impressão do documento. Por exemplo, o título pode ser 'Fatura' ou 'Fatura'. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Página inicial > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


#### Termos e Condições


Pode haver certos termos e condições para o item que você está vendendo. Eles podem ser aplicados aqui. Para saber como adicionar Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions).


### 2.4 Contabilidade


* **Lista de preços**: uma [Lista de preços](/docs/pt/stock/price-lists) armazena a [Preços dos itens](/docs/pt/stock/item-price). Definir uma lista de preços aqui irá buscar os preços dos itens para o perfil de PDV atual dessa lista de preços.
* **Moeda**: Por padrão, será definida de acordo com a moeda padrão da Empresa. No entanto, você pode alterá-lo. Caso você altere a moeda, lembre-se de alterar as contas também.
* **Impostos e encargos**: seleção de um [Modelo de impostos e encargos sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template)  ou [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template) aqui aplicarão automaticamente os impostos e cobranças na transação de PDV.
* **Aplicar desconto em**: aqui você pode definir se o desconto será aplicado ao total geral (valor antes dos impostos) ou ao total líquido (valor após os impostos).
* **Categoria de imposto**: ao selecionar uma [Categoria de imposto](/docs/pt/accounts/tax-category) aqui, as Regras fiscais associado à categoria de imposto será aplicado a cada transação realizada a partir deste perfil de PDV.


As seguintes contas podem ser definidas para que o razão geral seja atualizado adequadamente:


* Conta para valor da alteração
* Baixar conta
* Baixar Centro de Custo
* Conta de receitas
* Conta de despesas


### 2.5 Dimensões contábeis


As Dimensões Contábeis permitem marcar transações com base em um Território, Filial, Cliente específico, etc. Isso ajuda a visualizar os demonstrativos contábeis separadamente com base nos critérios selecionados. Para saber mais, visite a página [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions).



> 
> Observação: o centro de custo é tratado como uma dimensão por padrão.
> 
> 
> 


## 3. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Ponto de vendas](/docs/pt/accounts/point-of-sales)



