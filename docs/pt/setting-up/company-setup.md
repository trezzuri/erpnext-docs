# Configuração da empresa



**Uma empresa é uma pessoa jurídica constituída por uma associação de pessoas para a realização de um empreendimento comercial ou industrial.**

No ERPNext, é criada a primeira Empresa quando uma conta ERPNext é configurada. Para cada empresa, você pode definir um domínio como manufatura, varejo ou serviços, dependendo da natureza de sua atividade comercial.

Se você tiver mais de uma empresa, poderá adicioná-las em:

 > Home > Contabilidade > Empresa

## 1. Como criar uma nova empresa

1. Vá para a lista de empresas, clique em Novo.
2. Insira o nome, abreviatura e moeda padrão da empresa.
3. Salvar.

A abreviatura da sua empresa é criada por padrão. Por exemplo, FT para Frappe Technologies. A abreviatura ajuda a diferenciar os ativos de uma empresa de outra.

A abreviatura também aparece em diversas contas, centros de custo, modelos de impostos, almoxarifados, etc, da sua empresa.

Você pode anexe também o logotipo da empresa e adicione uma descrição para a empresa.

![Company Master](/files/company-master.png)![]()

### 1.1 Estrutura Multiempresa

Vamos supor que você administre um grupo de empresas, algumas podem ser empresas maiores e outras menores, que fazem parte de empresas maiores.

No ERPNext, você pode configurar vários empresas. A estrutura da empresa pode ser paralela, ou seja, empresas irmãs, empresas-mãe ou uma combinação de ambas.

Uma empresa-mãe é uma organização maior que consiste em uma ou mais empresas-filhas. Uma empresa filha é uma subsidiária de uma empresa controladora.

A visualização em árvore da empresa exibe a estrutura geral de suas empresas.

![Árvore da empresa](/files/company-tree.png)![]()  
 

Depois de construir uma árvore de empresa, o ERPNext irá validar se as contas das empresas filhas correspondem às contas da empresa controladora. Todas as contas podem ser combinadas em um extrato consolidado do plano de contas.

### 1.2 Outras opções ao criar uma empresa

* **Domínio**: O domínio de trabalho em que a empresa está inserida. Ex: manufatura, serviços, etc. Escolha um ao configurar sua conta.
* **É Grupo**: se marcado, torna-se uma empresa controladora.
* **Empresa-mãe**: Se esta for uma empresa filha, defina a empresa-mãe neste campo, ou seja, selecione uma empresa do grupo à qual esta empresa pertence. Se uma empresa controladora for definida, o plano de contas da nova empresa que você está criando será criado com base na empresa controladora selecionada.

### 1.3 Plano de contas

Para cada Empresa, o mestre do Plano de Contas é mantido separadamente. Isso permite que você mantenha uma contabilidade separada para cada empresa de acordo com os requisitos legais. Você também pode importar plano de contas usando o  [Importador de Planos de Contas](/docs/pt/setting-up/chart-of-accounts-importer).

ERPNext localizou Plano de Contas prontamente disponível para alguns países. Ao criar uma nova empresa, você pode optar por configurar o plano de contas para ela a partir de uma das seguintes opções.

* Plano de contas padrão
* Com base no plano de contas existente da empresa

![Plano de contas da empresa](/files/new-company-coa-based-on.png)![]()  


Observe que, se a Controladora for selecionada ao criar uma nova Empresa, o Plano de Contas será criado com base na Controladora existente.

### 1.4 Padrões

No cadastro da empresa, você pode definir muitos dos valores padrão para cadastros e contas. Essas contas padrão irão ajudá-lo no rápido lançamento de transações contábeis, onde o valor da conta será obtido no cadastro da Empresa, se fornecido. Assim que a empresa é criada, um Plano de Contas e Centro de Custo padrão é criado automaticamente.

Os seguintes padrões podem ser definidos para uma empresa:

* Cabeçalho padrão
* Lista de feriados padrão
* Horário de trabalho padrão
* Termos e Condições Padrão
* País
* ID fiscal
* Data de Estabelecimento

## 2. Recursos

### 2.1 Meta mensal de vendas

Defina o número da meta mensal de vendas na moeda da empresa, por exemplo, US$ 10.000. O total de vendas mensais ficará visível assim que as transações forem feitas. Para saber mais [clique aqui](/docs/pt/setting-up/setting-company-sales-goal) .

### 2.2 Configurações da conta

Algumas das contas a seguir serão definidas por padrão quando você criar uma nova empresa, outras poderão ser criadas. As contas podem ser vistas no [Plano de contas](/docs/pt/accounts/chart-of-accounts). Esses valores podem ser alterados posteriormente, se necessário.

* Conta bancária padrão
* Conta em dinheiro padrão
* Conta a receber padrão
* Conta de arredondamento
* Centro de custo de arredondamento
* Baixar conta
* Conta com desconto permitido
* Conta com desconto recebido
* Conta de ganhos/perdas cambiais
* Conta de ganhos/perdas cambiais não realizados
* Padrão Conta a pagar
* Conta padrão de adiantamento de funcionário
* Conta padrão de custo de mercadorias vendidas
* Conta de receita padrão
* Conta de receita diferida padrão
* Conta de despesa diferida padrão
* Conta a pagar de folha de pagamento padrão
* Conta a pagar de relatório de despesas padrão
* Centro de custo padrão

* Limite de crédito
* Modelo de termos de pagamento padrão

### 2.3 Configurações de estoque

O recurso Estoque Perpétuo faria com que as transações de estoque impactassem os livros contábeis da empresa. Saiba mais [aqui](/docs/pt/stock/perpetual-inventory). Ela está habilitada por padrão.

* Conta de inventário padrão
* Conta de ajuste de estoque
* Estoque recebido mas não faturado
* Despesas incluídas na avaliação

![Configurações de estoque na empresa](/files/company-stock-settings.png)![]()

### 2.4 Padrões de ativos fixos

Para gerenciar ativos fixos em uma empresa, são necessárias as seguintes contas. A maioria deles será criada por padrão. Eles podem ser vistos no [Plano de contas](/docs/pt/accounts/chart-of-accounts) .

* Conta de depreciação acumulada
* Conta de despesas de depreciação
* Série para Lançamento de depreciação de ativos (lançamento diário)
* Despesas incluídas na avaliação de ativos
* Conta de ganhos/perdas na alienação de ativos

* Centro de custos de depreciação de ativos
* Conta de capital em andamento
* Ativo recebido Mas não faturado

![Fixed Asset Defaults](/files/Fixed Asset Defaults.png)![]()

Se você deseja contabilizar seus lançamentos contábeis em diferentes [Livros Financeiros](/docs/pt/accounts/finance-book), marque a caixa Ativar Livros Financeiros e defina um Livro financeiro padrão.

### 2.5 Configurações de HRA

Defina o componente padrão para os seguintes componentes salariais.

> Para o usuário indiano, definir o valor padrão neste ajudará nos cálculos da Declaração de Imposto de Funcionário, especialmente para o valor de isenção de HRA.

* Componente Básico
* Componente HRA
* Componente de atraso

### 2.6 Configurações de remessa bancária

*Somente para a Índia.*

Usando o recurso Ordem de Pagamento (em Contas), você pode fornecer um único documento de transferência para múltiplas transferências bancárias. A atualização do valor nos campos a seguir ajudará você a gerar remessa bancária em um formato que possa ser aceito e também carregado no portal do banco.

A ordem de pagamento permite que um usuário combine várias entradas/solicitações de pagamento em um único documento. A Remessa Bancária permite que um usuário envie **aquele** documento único ao banco em formato de texto. Esse formato de texto pode ser carregado manualmente na plataforma de pagamentos bancários Kotak.

O Código do Cliente e o Código do Produto são códigos fornecidos pelo banco a você. Isso deve ser adicionado ao arquivo de texto de acordo com o formato especificado pelo banco Kotak.

### 2.7 Orçamento

Função de Aprovador de Orçamento de Exceção: A função selecionada aqui pode ignorar o orçamento definido para aprovar despesas.

### 2.8 Informações da Empresa

Para referência, os seguintes detalhes da sua empresa podem ser salvos no ERPNext:

* Data de Incorporação
* Telefone
* Fax
* E-mail

* * Site
* Endereço
* Detalhes do registro
> Observação: ao definir o endereço aqui, é importante marcar a caixa de seleção 'É o endereço da sua empresa'.

![Endereço da empresa](/files/company-address.png)![]()  


**Para a Índia**, endereços diferentes podem ser adicionados com números GSTIN diferentes se a empresa tiver vários locais. Por exemplo, se sua empresa tiver escritórios em Mumbai, Delhi e Bangalore, você terá que adicionar endereços diferentes com números GSTIN diferentes.

**Detalhes do registro**: aqui você pode salvar vários números de imposto/cheque/banco para referência.

### 2.9 Excluindo todas as transações da empresa

Você pode excluir todas as transações (pedidos, faturas) de uma empresa. *Use com cautela*, uma vez excluídas as transações não poderão ser recuperadas.

#### Requisitos


	+ O usuário deve ser um gerente de sistema
	
	+ O Usuário deve ser o criador da Empresa#### Etapas


	1. Clique no botão **Excluir transações** em **Gerenciar**
	2. Verificar sua senha
	3. Insira o nome da empresa para confirmação ![Empresa após salvar](/files/company-delete-transactions.png)![]()E pronto. Os dados mestres como Item, Conta, Funcionário, BOM etc. permanecerão como estão.

#### O que é afetado?


	+ Vendas/Pedidos de Compra/Recebimentos de Faturas/Notas serão excluídas
	+ As vendas mensais e o histórico de vendas serão apagados
	+ Todas as notificações serão apagadas
	
	+ Os endereços dos leads aos quais a Empresa está vinculada serão excluídos
	+ Todas as comunicações vinculadas à Empresa serão excluídas
	+ Todas as séries de nomenclatura serão redefinidas
	+ As entradas de estoque vinculadas a um armazém desta empresa serão excluídas> Introduzido na versão 13.

### 2.10 Alterar empresa controladora

Você pode alterar a empresa controladora de uma empresa existente. Vá para o campo Controladora, selecione a Empresa na lista e salve o formulário. ![Alterar empresa controladora](/files/parent_company.gif)![]()  


### 3. Tópicos relacionados


	1. [Configurando impostos](/docs/pt/setting-up/setting-up-taxes)
	2. [Configurações do sistema](/docs/pt/setting-up/settings/system-settings )
	3. [Importador de gráficos de contas](/docs/pt/setting-up/chart-of-accounts-importer)
	4. [Usuários e permissões](/docs/pt/setting-up/users-and-permissions)
	5. [Adicionando usuários](/docs/pt/setting-up/users-and-permissions/adding-users)
	6. [Cabeçalho](/docs/pt/setting-up/print/letter-head)
	7. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
	8. [Administrador](/docs/pt/setting-up/users-and-permissions/administrator)


