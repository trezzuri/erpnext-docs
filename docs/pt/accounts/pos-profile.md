# Perfil do Ponto de Venda


**No ERPNext, um perfil de PDV permite utilizar o recurso Ponto de Venda.**


O POS inclui recursos avançados para atender a diferentes funcionalidades, como
gerenciamento de estoque, CRM, finanças, armazenamento, etc., todos integrados ao
Software de PDV. Antes do POS moderno, todas essas funções eram feitas
de forma independente e exigia a redigitação manual de informações, o que poderia
levar a erros de entrada.


Se está no retalho, quer que o seu Ponto de Venda seja o mais rápido
e eficiente possível. Para fazer isso, você pode criar um perfil de PDV para um usuário.


Para acessar a lista de Perfil de PDV, acesse:



>
> Home > Varejo > Operações de Varejo > Perfil do Ponto de Venda
>
>
>


## 1. Como criar um Perfil PDV


1. Acesse o Perfil do Ponto de Venda e clique em Novo.
2. Digite um nome para o perfil.
3. Selecione uma [Série de nomenclatura](/docs/v13/user/manual/en/setting-up/settings/naming-series).
4. Defina uma Conta Baixa e um Centro de Custo Baixa no qual as transações serão registradas.
5. Configure as formas de pagamento na tabela, o padrão será em dinheiro se nada for definido aqui. Somente os modos definidos aqui estarão disponíveis ao usar o POS. Depois de adicionar modos de pagamento, defina um deles como o método de pagamento padrão marcando a caixa de seleção.


![Método de pagamento no perfil PDV](/files/payment-method-in-pos.png)
6. Defina os valores padrão para os métodos de pagamento (recomendado: 0).
7. Salve.


![Perfil POS](/files/pos-profile.png)


### 1.1 Opções adicionais ao criar um Perfil PDV


* **Cliente**: Os usuários podem vender produtos específicos para os clientes específicos do PDV adicionando grupos de itens e grupos de clientes no perfil do PDV.
* **Armazém**: As quantidades de estoque no Armazém selecionado serão afetadas pelas transações PDV com este Perfil PDV.
* **Campanha**: Uma [Campanha](/docs/v13/user/manual/en/CRM/campaign) de vendas pode ser vinculada aqui para rastrear o total de vendas em relação a ela.
* **Endereço da Empresa**: Se o balcão do PDV estiver configurado em uma filial da Empresa, o endereço pode ser selecionado aqui.
* **Atualizar Estoque**: Se habilitada, as quantidades de estoque serão afetadas quando as transações forem realizadas com o Perfil PDV. Ou seja, os Lançamentos no Razão de Estoque serão feitos quando você “Enviar” esta Nota Fiscal de Venda, eliminando assim a necessidade de uma Nota de Entrega separada.
* **Ignorar regra de preços**: Qualquer [regra de preços](/docs/v13/user/manual/en/accounts/pricing-rule) ativa será ignorada para este perfil de PDV.
* **Permitir exclusão**: No POS offline, os dados são armazenados em cache. Marcar esta caixa de seleção permitirá que o usuário exclua a fatura de vendas armazenada em cache no estágio de rascunho.
* **Permitir que o usuário edite a Taxa**: O usuário do Perfil PDV poderá editar a 'Taxa' dos Itens adicionados nas transações.
* **Permitir que o usuário edite o Desconto**: O usuário do Perfil PDV poderá editar o 'Desconto' dos Itens adicionados nas transações.
* **Permitir imprimir antes de pagar**: Isso permitirá que o usuário do PDV imprima uma fatura antes de efetuar o pagamento.
* **Mostrar Itens em Estoque**: A quantidade restante de Itens do Armazém selecionado será mostrada ao Usuário do PDV.


## 2. Características


### 2.1 Aplicável a Usuários


Por padrão, todos os Usuários de Vendas podem acessar os Perfis de PDV criados no ERPNext. No entanto, se você deseja que apenas determinados usuários acessem determinados perfis de PDV, você pode adicioná-los à tabela. Uma vez que até mesmo um usuário é definido no perfil POS, outros usuários não podem usar este perfil POS para transações de varejo.


**Definindo o Perfil de PDV como padrão**: Ao marcar a caixa de seleção Padrão na tabela, o Perfil de PDV atual torna-se o Perfil de PDV padrão para aquele usuário. Assim, na próxima vez que o usuário fizer login no sistema, o Perfil PDV será definido por padrão.


![Usuário PDV](/files/pos-profile-default.png)



>
> Nota: Se você especificar um usuário específico, a configuração do POS será
> aplicado apenas a esse usuário. Se a opção Usuário for deixada em branco, a configuração será
> ser definido para todos os usuários. Para entender como o PDV funciona, visite a página [Ponto de venda](/docs/v13/user/manual/en/accounts/point-of-sales).
>
>
>


### 2.2 Grupo de itens de configuração e grupo de clientes


Ao definir um Grupo de Artigos/Grupo de Clientes num Perfil PDV, o grupo será automaticamente selecionado ao fazer transações com o Perfil PDV.


![Filtros no Perfil POS](/files/filters-in-pos-profile.png)


### 2.3 Configurações de impressão


![Configurações de impressão POS](/files/pos-profile-in-print-settings.png)


#### Formato de Impressão para Online


Você pode definir um Formato de impressão que decidirá como será o layout do documento impresso. Para saber mais, visite a página [Formato de impressão](/docs/v13/user/manual/en/setting-up/print/print-format).


#### Papel timbrado


Você pode imprimir sua Fatura de Venda PDV em papel timbrado de sua Empresa. Saiba mais [aqui](/docs/v13/user/manual/en/setting-up/print/letter-head).


#### Cabeçalhos de impressão


Os cabeçalhos da Nota Fiscal de Venda PDV também podem ser alterados ao imprimir o documento. Por exemplo, o título pode ser 'Fatura' ou 'Conta'. Você pode fazer isso selecionando **Print Heading**. Para criar novos cabeçalhos de impressão, vá para: Home > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/v13/user/manual/en/setting-up/print/print-headings).


#### Termos e Condições


Pode haver certos termos e condições no item que você está vendendo, eles podem ser aplicados aqui. Para saber como adicionar Termos e Condições, [clique aqui](/docs/v13/user/manual/en/setting-up/print/terms-and-conditions).


### 2.4 Contabilidade


* **Lista de preços**: Uma [Lista de preços](/docs/v13/user/manual/en/stock/listas de preços) armazena os [Preços dos itens](/docs/v13/user/manual/en/stock /Preço do item). Definir uma lista de preços aqui buscará os preços do item para o perfil de PDV atual dessa lista de preços.
* **Moeda**: Por padrão, será definido de acordo com a moeda padrão da empresa. No entanto, você pode alterá-lo. Caso troque a moeda, lembre-se de trocar as contas também.
* **Taxes and Charges**: selecionando um [Sales Taxes and Charges Template](/docs/v13/user/manual/en/selling/sales-taxes-and-charges-template) ou [Purchase Taxes and Charges Template] (/docs/v13/user/manual/en/buying/purchase-taxes-and-charges-template) aplicará automaticamente os impostos e cobranças à transação do PDV.
* **Aplicar desconto em**: Aqui você pode definir se o desconto será aplicado no Total geral (valor antes do imposto) ou no Total líquido (valor após o imposto).
* **Categoria de imposto**: Ao selecionar uma [Categoria de imposto](/docs/v13/user/manual/en/accounts/tax-category) aqui, as Regras de imposto associadas à Categoria de imposto serão aplicadas a cada transação realizada deste Perfil de PDV.


As seguintes contas podem ser definidas para que o razão geral seja atualizado de acordo:


* Conta para o valor da alteração
* Cancelar conta
* Baixa Centro de Custo
* Conta de Renda
* Conta de despesa


### 2.5 Dimensões Contábeis


As Dimensões Contábeis permitem que você marque as transações com base em um Território, Filial, Cliente etc. Isso ajuda a visualizar os extratos contábeis separadamente com base nos critérios selecionados. Para saber mais, visite a página [Dimensões contábeis](/docs/v13/user/manual/en/accounts/accounting-dimensions).



>
> Observação: Centro de custo é tratado como uma dimensão por padrão.
>
>
>


## 3. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)
3. [Ponto de vendas](/docs/v13/user/manual/en/accounts/point-of-sales)