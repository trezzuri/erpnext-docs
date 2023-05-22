# Configuração da empresa


**Empresa é a pessoa jurídica constituída pela associação de pessoas para o exercício de um empreendimento comercial ou industrial.**


No ERPNext, a primeira Empresa é criada quando uma conta ERPNext é configurada. Para cada empresa, você pode definir um domínio como manufatura, varejo ou serviços, dependendo da natureza da sua atividade comercial.


Se você tiver mais de uma empresa, poderá adicioná-las de:



> 
> Início > Contabilidade > Empresa
> 
> 
> 


## 1. Como criar uma nova empresa


1. Vá para a lista de empresas, clique em Novo.
2. Insira o nome, a abreviação e a moeda padrão da empresa.
3. Salvar.


A abreviação da sua empresa é criada por padrão. Por exemplo, FT para Frappe Technologies. A abreviação ajuda a diferenciar os ativos de uma empresa de outra.


A abreviatura também aparece em várias contas, centros de custos, modelos de impostos, armazém, etc, da sua empresa.


Você também pode anexar um logotipo da empresa e adicionar uma descrição para a empresa.


![Company Master](/files/company-master.png)


### 1.1 Estrutura de várias empresas


Vamos supor que você administre um grupo de empresas, algumas podem ser empresas maiores e outras menores que fazem parte da(s) empresa(s) maior(is).


No ERPNext, você pode configurar várias empresas. A estrutura da empresa pode ser paralela, ou seja, empresas irmãs, empresas controladoras ou uma combinação de ambas.


Uma empresa matriz é uma organização maior que consiste em uma ou mais empresas filhas. Uma empresa filha é uma subsidiária de uma empresa controladora.


A exibição em árvore da empresa exibe a estrutura geral de suas empresas.


![Company Tree](/files/company-tree.png)


Uma vez construída a árvore da empresa, o ERPNext irá validar se as contas das empresas filhas correspondem às contas da empresa mãe. Todas as contas podem ser combinadas em um extrato consolidado do plano de contas.


### 1.2 Outras opções ao criar uma empresa


* **Domínio**: o domínio de trabalho em que a empresa está inserida. Por exemplo: manufatura, serviços, etc. Escolha um ao configurar sua conta.
* **Is Group**: Se marcado, torna-se uma empresa controladora.
* **Empresa controladora**: Se esta for uma empresa filha, defina a empresa pai neste campo, ou seja, selecione uma empresa do grupo a que esta empresa pertence. Se uma empresa controladora for definida, o plano de contas da nova empresa que você está criando será criado com base na empresa controladora selecionada.


### 1.3 Plano de contas


Para cada Empresa, o mestre do Plano de Contas é mantido separadamente. Isso permite que você mantenha uma contabilidade separada para cada empresa de acordo com os requisitos legais. Você também pode importar planos de contas usando o [Importador de planos de contas](/docs/pt/setting-up/chart-of-accounts-importer).


O ERPNext possui Plano de Contas localizado prontamente disponível para alguns países. Ao criar uma nova empresa, você pode optar por configurar o plano de contas para ela a partir de uma das seguintes opções.


* Plano de contas padrão
* Com base no plano de contas da empresa existente


![Plano de contas da empresa](/files/new-company-coa-based-on.png)


Observe que, se a Matriz for selecionada ao criar uma nova Empresa, o Plano de Contas será criado com base na Matriz existente.


### 1.4 Padrões


No mestre da empresa, você pode definir muitos dos valores padrão para mestres e contas. Essas contas padrão irão ajudá-lo no lançamento rápido de transações contábeis, onde o valor da conta será buscado no mestre da empresa, se fornecido. Assim que a empresa é criada, um plano de contas padrão e um centro de custos são criados automaticamente.


Os seguintes padrões podem ser definidos para uma empresa:


* Cabeçalho Padrão
* Lista de feriados padrão
* Horário de trabalho padrão
* Termos e condições padrão
* País
* Identificação fiscal
* Data de estabelecimento


## 2. Recursos


### 2.1 Meta de vendas mensal


Defina o número da meta de vendas mensal na moeda da empresa, por exemplo, US$ 10.000. O total de vendas mensais ficará visível assim que as transações forem feitas. Para saber mais [clique aqui](/docs/pt/setting-up/setting-company-sales-goal).


### 2.2 Configurações da conta


Algumas das contas a seguir serão definidas por padrão quando você criar uma nova empresa, outras podem ser criadas. As contas podem ser vistas no [Plano de contas](/docs/pt/accounts/chart-of-accounts). Esses valores podem ser alterados posteriormente, se necessário.


* Conta bancária padrão
* Conta de caixa padrão
* Conta a receber padrão
* Arredondar conta
* Centro de custos arredondados
* Cancelar conta
* Conta com desconto permitido
* Conta recebida com desconto
* Conta de ganho/perda de câmbio
* Conta de ganho/perda de troca não realizada
* Conta a pagar padrão
* Conta padrão de adiantamento de funcionário
* Conta padrão de custo de mercadorias vendidas
* Conta de receita padrão
* Conta de receita diferida padrão
* Conta de despesas diferidas padrão
* Conta de folha de pagamento padrão
* Conta a pagar de reembolso de despesas padrão
* Centro de custo padrão
* Limite de crédito
* Modelo de condições de pagamento padrão


### 2.3 Configurações de estoque


O recurso de inventário permanente faria com que as transações de estoque afetassem os livros contábeis da empresa. Saiba mais [aqui](/docs/pt/stock/perpetual-inventory). Ele é ativado por padrão.


* Conta de inventário padrão
* Conta de ajuste de estoque
* Estoque recebido, mas não faturado
* Despesas incluídas na avaliação


![Configurações de estoque na empresa](/files/company-stock-settings.png)


### 2.4 Padrões de ativos fixos


Para gerenciar ativos fixos em uma empresa, são necessárias as seguintes contas. A maioria deles será criada por padrão. Eles podem ser vistos no [Plano de contas](/docs/pt/accounts/chart-of-accounts).


* Conta de depreciação acumulada
* Conta de Despesas de Depreciação
* Série para lançamento de depreciação de ativos (registro de diário)
* Despesas incluídas na avaliação de ativos
* Conta de ganho/perda na alienação de ativos
* Centro de custo de depreciação de ativos
* Conta de trabalho de capital em andamento
* Recurso recebido, mas não cobrado


![Padrões de ativos fixos](/files/Padrões de ativos fixos.png)


Se você deseja registrar suas entradas contábeis em diferentes [Livros financeiros](/docs/pt/accounts/finance-book), marque a caixa Ativar livros financeiros e defina um livro financeiro padrão.


### 2.5 Configurações de HRA


Defina o componente padrão para os seguintes componentes salariais.



> 
> Para o usuário indiano, definir o valor padrão nesta seção ajudará nos cálculos da declaração de imposto do funcionário, especialmente para o valor de isenção HRA.
> 
> 
> 


* Componente básico
* Componente HRA
* Componente Atrasado


### 2.6 Configurações de remessa bancária


*Apenas para a Índia.*


Através da funcionalidade Ordem de Pagamento (em Contas), pode dar um único documento de transferência para várias transferências bancárias. A atualização do valor nos campos a seguir ajudará você a gerar Remessa Bancária em um formato aceito e também pode ser carregado no portal do banco.


A ordem de pagamento permite ao utilizador combinar vários lançamentos/pedidos de pagamento num único documento. Remessa bancária permite que um usuário envie **aquele** documento único para o banco como formato de texto, este formato de texto pode ser carregado manualmente para a plataforma de pagamentos bancários Kotak.


Código do cliente e Código do produto são códigos fornecidos pelo banco a você. Isso deve ser adicionado ao arquivo de texto de acordo com o formato especificado pelo banco Kotak.


### 2.7 Orçamento


Função de aprovador de orçamento de exceção: a função selecionada aqui pode ignorar o orçamento definido para aprovar despesas.


### 2.8 Informações da empresa


Para referência, os seguintes detalhes da sua empresa podem ser salvos no ERPNext:


* Data de Constituição
* Nº de telefone
* Fax
* E-mail
* Site
* Endereço
* Detalhes do registro



> 
> Observação: ao definir o endereço aqui, é importante marcar a caixa de seleção 'É o endereço da sua empresa'.
> 
> 
> 


![Endereço da empresa](/files/company-address.png)


**Para a Índia**, diferentes endereços podem ser adicionados com diferentes números GSTIN se a empresa tiver vários locais. Por exemplo, se sua empresa tiver escritórios em Mumbai, Delhi e Bangalore, você terá que adicionar diferentes endereços com diferentes números GSTIN.


**Detalhes de registro**: Aqui você pode salvar vários números de impostos/cheques/bancos para referência.


### 2.9 Exclusão de todas as transações da empresa


Você pode excluir todas as transações (pedidos, faturas) de uma empresa. *Use com cuidado*, as transações uma vez excluídas não podem ser recuperadas.


#### Requisitos


* O usuário deve ser um gerente de sistema
* O Usuário deve ser o criador da Empresa


#### Passos


1. Clique no botão **Excluir transações** em **Gerenciar**
2. Verifique sua senha
3. Digite o nome da empresa para confirmação
![Empresa após salvar](/files/company-delete-transactions.png)


E pronto. Os dados mestre como Item, Conta, Empregado, BOM etc. permanecerão como estão.


#### O que é afetado?


* Pedidos de venda/compra/faturas, recibos/notas serão excluídos
* As vendas mensais e o histórico de vendas serão apagados
* Todas as notificações serão apagadas
* Os endereços de leads aos quais a empresa está vinculada serão excluídos
* Todas as comunicações vinculadas à Empresa serão excluídas
* Todas as séries de nomenclatura serão redefinidas
* As entradas de estoque vinculadas a um depósito desta empresa serão excluídas



> 
> Introduzido na versão 13.
> 
> 
> 


### 2.10 Alterar empresa controladora


Você pode alterar a empresa-mãe de uma empresa existente. Acesse o campo Matriz, selecione a Empresa na lista e salve o formulário.
![Change Parent Company](/files/parent_company.gif)


### 3. Tópicos Relacionados


1. [Configuração de impostos](/docs/pt/setting-up/setting-up-taxes)
2. [Configurações do sistema](/docs/pt/setting-up/settings/system-settings)
3. [Importador de planos de contas](/docs/pt/setting-up/chart-of-accounts-importer)
4. [Usuários e permissões](/docs/pt/setting-up/users-and-permissions)
5. [Adicionar usuários](/docs/pt/setting-up/users-and-permissions/adding-users)
6. [Cabeçalho](/docs/pt/setting-up/print/letter-head)
7. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
8. [Administrador](/docs/pt/setting-up/users-and-permissions/administrator)
