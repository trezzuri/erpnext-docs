# Perfil do ponto de venda


**No ERPNext, um perfil de PDV permite usar o recurso Ponto de Venda.**


POS inclui recursos avançados para atender a diferentes funcionalidades, como
gerenciamento de estoque, CRM, finanças, armazenamento, etc., todos integrados ao
Software de PDV. Antes do POS moderno, todas essas funções eram feitas
de forma independente e exigia a redigitação manual de informações, o que poderia
levar a erros de entrada.


Se está no retalho, quer que o seu Ponto de Venda seja o mais rápido
e eficiente possível. Para fazer isso, você pode criar um Perfil de PDV para um usuário.


Para acessar a lista de perfis de PDV, acesse:



> 
> Página inicial > Varejo > Operações de varejo > Perfil do ponto de venda
> 
> 
> 


## 1. Como criar um perfil PDV


1. Vá para o Perfil do ponto de venda e clique em Novo.
2. Digite um nome para o perfil.
3. Selecione uma [Série de nomes](/docs/pt/setting-up/settings/naming-series).
4. Defina uma conta de baixa e um centro de custo de baixa para o qual as transações serão registradas.
5. Defina as formas de pagamento na tabela, o padrão será em dinheiro se nada for definido aqui. Somente os modos definidos aqui estarão disponíveis ao usar o POS. Depois de adicionar modos de pagamento, defina um deles como o método de pagamento padrão marcando a caixa de seleção.


![Método de pagamento no perfil PDV](/files/payment-method-in-pos.png)
6. Defina os valores padrão para as formas de pagamento (recomendado: 0).
7. Salvar.


![POS Profile](/files/pos-profile.png)


### 1.1 Opções adicionais ao criar um perfil PDV


* **Cliente**: os usuários podem vender produtos específicos para os clientes específicos do PDV adicionando grupos de itens, grupos de clientes no perfil do PDV.
* **Armazém**: as quantidades de estoque no Armazém selecionado serão afetadas pelas transações PDV com este Perfil PDV.
* **Campanha**: uma [Campanha](/docs/pt/CRM/campaign) de vendas pode ser vinculada aqui para rastrear o total de vendas em relação a ela .
* **Endereço da Empresa**: Se o balcão PDV estiver configurado em uma filial da Empresa, o endereço pode ser selecionado aqui.
* **Atualizar Estoque**: Se ativado, as quantidades de estoque serão afetadas quando as transações forem realizadas com o Perfil PDV. Ou seja, os Lançamentos no Razão de Estoque serão feitos quando você “Enviar” esta Fatura de Venda, eliminando assim a necessidade de uma Nota de Entrega separada.
* **Ignorar regra de preços**: qualquer [regra de preços](/docs/pt/accounts/pricing-rule) ativa será ignorada para isso Perfil PDV.
* **Permitir exclusão**: no PDV off-line, os dados são armazenados em cache. Marcar esta caixa de seleção permitirá que o usuário exclua a fatura de venda armazenada em cache no estágio de rascunho.
* **Permitir que o usuário edite a Taxa**: O usuário do Perfil PDV poderá editar a 'Taxa' dos Itens adicionados nas transações.
* **Permitir que o usuário edite o Desconto**: O usuário do Perfil PDV poderá editar o 'Desconto' dos Itens adicionados nas transações.
* **Permitir impressão antes do pagamento**: Isso permitirá que o usuário do PDV imprima uma fatura antes de efetuar o pagamento.
* **Exibir Itens em Estoque**: A quantidade restante de Itens do Armazém selecionado será mostrada ao Usuário PDV.


## 2. Recursos


### 2.1 Aplicável a usuários


Por padrão, todos os Usuários de Vendas podem acessar os Perfis PDV criados no ERPNext. No entanto, se você deseja que apenas determinados usuários acessem determinados perfis de PDV, você pode adicioná-los à tabela. Assim que um usuário for definido no perfil de PDV, outros usuários não poderão usar esse perfil de PDV para transações de varejo.


**Configurando o Perfil de PDV como padrão**: Ao marcar a caixa de seleção Padrão na tabela, o Perfil de PDV atual torna-se o Perfil de PDV padrão para aquele usuário. Assim, na próxima vez que o usuário fizer login no sistema, o perfil PDV será definido por padrão.


![POS User](/files/pos-profile-default.png)



> 
> Nota: Se você especificar um usuário em particular, a configuração do PDV será
>  aplicado apenas a esse usuário. Se a opção Usuário for deixada em branco, a configuração será
>  ser definido para todos os usuários. Para entender como o PDV funciona, visite a página [Ponto de venda](/docs/pt/accounts/point-of-sales).
> 
> 
> 


### 2.2 Grupo de itens de configuração e grupo de clientes


Ao configurar um Grupo de Itens/Grupo de Clientes em um Perfil PDV, o grupo será selecionado automaticamente ao fazer transações com o Perfil PDV.


![Filtros no perfil POS](/files/filters-in-pos-profile.png)


### 2.3 Configurações de impressão


![Configurações de impressão POS](/files/pos-profile-in-print-settings.png)


#### Formato de impressão para online


Você pode definir um Formato de impressão que decidirá como será o layout do documento impresso. Para saber mais, visite a página [Formato de impressão](/docs/pt/setting-up/print/print-format).


#### Papel timbrado


Você pode imprimir sua Fatura de Venda PDV em papel timbrado de sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).


#### Imprimir títulos


Os cabeçalhos da Fatura de Venda PDV também podem ser alterados ao imprimir o documento. Por exemplo, o título pode ser 'Fatura' ou 'Conta'. Você pode fazer isso selecionando um **Título de impressão**. Para criar novos cabeçalhos de impressão, vá para: Home > Configurações > Impressão > Cabeçalho de impressão. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).


#### Termos e Condições


Pode haver certos termos e condições no item que você está vendendo, eles podem ser aplicados aqui. Para saber como adicionar Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions).


### 2.4 Contabilidade


* **Lista de preços**: uma [Lista de preços](/docs/pt/stock/price-lists) armazena a [Preços dos itens]( /docs/pt/stock/item-price). Definir uma lista de preços aqui buscará os preços dos itens para o perfil de PDV atual dessa lista de preços.
* **Moeda**: Por padrão, isso será definido de acordo com a moeda padrão da empresa. No entanto, você pode alterá-lo. Caso altere a moeda, lembre-se de alterar as contas também.
* **Impostos e encargos**: selecionando um [Modelo de impostos e encargos sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template)  ou [Modelo de impostos e cobranças de compra](/docs/pt/buying/purchase-taxes-and-charges-template) aqui aplicará automaticamente os impostos e encargos para a transação de PDV.
* **Aplicar desconto em**: Aqui você pode definir se o desconto deve ser aplicado no Total geral (valor antes dos impostos) ou no Total líquido (valor após os impostos).
* **Categoria de imposto**: Ao selecionar uma [Categoria de imposto](/docs/pt/accounts/tax-category) aqui, as Regras de imposto associado à categoria de imposto será aplicado a cada transação realizada a partir deste perfil de PDV.


As seguintes contas podem ser definidas para que o razão geral seja atualizado de acordo:


* Conta para alterar o valor
* Cancelar conta
* Baixar Centro de Custo
* Conta de receita
* Conta de despesas


### 2.5 Dimensões contábeis


As Dimensões Contábeis permitem que você marque as transações com base em um Território, Filial, Cliente, etc. Isso ajuda a visualizar os extratos contábeis separadamente com base nos critérios selecionados. Para saber mais, visite a página [Dimensões contábeis](/docs/pt/accounts/accounting-dimensions).



> 
> Observação: o centro de custo é tratado como uma dimensão por padrão.
> 
> 
> 


## 3. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Ponto de vendas](/docs/pt/accounts/point-of-sales)
