# Configuração da Empresa


**Empresa é a pessoa jurídica constituída pela associação de pessoas para o exercício de um empreendimento comercial ou industrial.**


No ERPNext, a primeira Empresa é criada quando uma conta ERPNext é configurada. Para cada empresa, você pode definir um domínio como manufatura, varejo ou serviços, dependendo da natureza da sua atividade comercial.


Se você tiver mais de uma empresa, poderá adicioná-las de:



>
> Home > Contabilidade > Empresa
>
>
>


## 1. Como criar uma nova empresa


1. Vá para a lista Empresa, clique em Novo.
2. Digite o nome, a abreviação e a moeda padrão da empresa.
3. Salve.


A abreviação da sua empresa é criada por padrão. Por exemplo, FT para Frappe Technologies. A abreviação ajuda a diferenciar os ativos de uma empresa de outra.


A abreviação também aparece em diversas contas, centros de custo, templates de impostos, almoxarifado, etc, da sua empresa.


Você também pode anexar um logotipo da empresa e adicionar uma descrição para a empresa.


![Company Master](/files/company-master.png)


### 1.1 Estrutura Multiempresarial


Vamos supor que você administre um grupo de empresas, algumas podem ser empresas maiores e outras menores que fazem parte da(s) empresa(s) maior(is).


No ERPNext, você pode configurar várias empresas. A estrutura da empresa pode ser paralela, ou seja, empresas irmãs, empresas-mãe-filhas ou uma combinação de ambas.


Uma empresa-mãe é uma organização maior que consiste em uma ou mais empresas filhas. Uma empresa filha é uma subsidiária de uma empresa controladora.


A exibição em árvore da empresa exibe a estrutura geral de suas empresas.


![Árvore da Empresa](/files/company-tree.png)


Uma vez construída a árvore da empresa, o ERPNext validará se as contas das empresas filhas coincidem com as contas da empresa mãe. Todas as contas podem ser combinadas em um extrato consolidado do plano de contas.


### 1.2 Outras opções ao criar uma empresa


* **Domínio**: O domínio de trabalho da empresa. Ex: manufatura, serviços, etc. Escolha um ao configurar sua conta.
* **Is Group**: Se marcado, torna-se uma empresa controladora.
* **Empresa controladora**: Se for uma empresa filha, defina a empresa pai neste campo, ou seja, selecione uma empresa do grupo a que esta empresa pertence. Se uma empresa-mãe for definida, o plano de contas da nova empresa que você está criando será criado com base na empresa-mãe selecionada.


### 1.3 Plano de Contas


Para cada Empresa, o mestre do Plano de Contas é mantido separadamente. Isso permite que você mantenha uma contabilidade separada para cada empresa de acordo com os requisitos legais. Você também pode importar planos de contas usando o [Importador de planos de contas](/docs/v13/user/manual/en/setting-up/chart-of-accounts-importer).


O ERPNext localizou o Plano de Contas prontamente disponível para alguns países. Ao criar uma nova Empresa, você pode optar por configurar o Plano de Contas para ela a partir de uma das opções a seguir.


* Plano de contas padrão
* Com base no plano de contas da empresa existente


![Plano de contas da empresa](/files/new-company-coa-based-on.png)


Observe que, se a Matriz for selecionada ao criar uma nova Empresa, o Plano de Contas será criado com base na Matriz existente.


### 1.4 Padrões


No mestre da empresa, você pode definir muitos dos valores padrão para mestres e contas. Essas contas padrão irão ajudá-lo no lançamento rápido de transações contábeis, onde o valor da conta será buscado no mestre da empresa, se fornecido. Assim que a empresa é criada, um Plano de Contas e Centro de Custo padrão é criado automaticamente.


Os seguintes padrões podem ser definidos para uma empresa:


* Cabeçalho Padrão
* Lista de feriados padrão
* Horário de trabalho padrão
* Termos e condições padrão
* País
* CPF
* Data de Estabelecimento


## 2. Características


### 2.1 Meta Mensal de Vendas


Defina o número da meta de vendas mensal na moeda da empresa, por exemplo, US$ 10.000. O total de vendas mensais ficará visível assim que as transações forem feitas. Para saber mais [clique aqui](/docs/v13/user/manual/en/setting-up/setting-company-sales-goal).


### 2.2 Configurações da conta


Algumas das contas a seguir serão definidas por padrão quando você criar uma nova empresa, outras podem ser criadas. As contas podem ser vistas no [Plano de Contas](/docs/v13/user/manual/pt/contas/plano de contas). Esses valores podem ser alterados posteriormente, se necessário.


* Conta Bancária Padrão
* Conta de caixa padrão
* Conta a receber padrão
* Arredondar Conta
*Centro de Custo Arredondado
* Cancelar conta
* Conta com desconto permitido
*Desconto Recebido na Conta
* Conta de ganho/perda de câmbio
* Conta de ganho/perda cambial não realizada
* Conta a pagar padrão
* Conta Antecipada do Funcionário Padrão
* Conta padrão de custo de mercadorias vendidas
* Conta de receita padrão
* Conta de receita diferida padrão
* Conta de Despesas Diferidas Padrão
* Conta de folha de pagamento padrão
* Conta a pagar de reembolso de despesas padrão
* Centro de custo padrão
* Limite de crédito
* Modelo de condições de pagamento padrão


### 2.3 Configurações de Estoque


O recurso de Inventário Perpétuo faria com que as transações de estoque afetassem os livros contábeis da empresa. Saiba mais [aqui](/docs/v13/user/manual/en/stock/perpetual-inventory). Ele é ativado por padrão.


* Conta de inventário padrão
* Conta de Ajuste de Estoque
* Estoque Recebido Mas Não Faturado
* Despesas Incluídas na Avaliação


![Configurações de estoque na empresa](/files/company-stock-settings.png)


### 2.4 Padrões de Ativos Fixos


Para gerenciar ativos fixos em uma empresa, são necessárias as seguintes contas. A maioria deles será criada por padrão. Eles podem ser vistos no [Plano de contas](/docs/v13/user/manual/pt/contas/plano de contas).


* Conta de Depreciação Acumulada
* Conta de Despesas de Depreciação
* Série para entrada de depreciação de ativos (lançamento de diário)
* Despesas Incluídas na Avaliação de Ativos
* Conta de Ganhos/Perdas na Alienação de Ativos
* Centro de Custo de Depreciação de Ativos
* Conta de Trabalho de Capital em Andamento
* Ativo recebido, mas não faturado


![Padrões de Ativos Fixos](/files/Padrões de Ativos Fixos.png)


Se você deseja registrar suas entradas contábeis em diferentes [Livros financeiros](/docs/v13/user/manual/en/accounts/finance-book), marque a caixa Ativar livros financeiros e defina um Livro financeiro padrão.


### 2.5 Configurações de HRA


Defina o componente padrão para os seguintes componentes salariais.



>
> Para o usuário indiano, definir o valor padrão nesta seção ajudará nos cálculos da declaração de imposto do funcionário, especialmente para o valor de isenção HRA.
>
>
>


* Componente Básico
* Componente HRA
* Componente Atrasado


### 2.6 Configurações de Remessa Bancária


*Apenas para a Índia.*


Através da funcionalidade Ordem de Pagamento (em Contas), pode dar um único documento de transferência para várias transferências bancárias. A atualização do valor nos campos a seguir ajudará você a gerar a Remessa Bancária em um formato que possa ser aceito e também possa ser carregado no portal do banco.


A ordem de pagamento permite ao utilizador combinar vários lançamentos/pedidos de pagamento num único documento. O Bank Remittance permite que um usuário envie **aquele** único documento para o banco como formato de texto, este formato de texto pode ser carregado manualmente para a plataforma de pagamentos bancários Kotak.


O Código do Cliente e o Código do Produto são códigos fornecidos pelo banco a você. Isso deve ser adicionado ao arquivo de texto de acordo com o formato especificado pelo banco Kotak.


### 2.7 Orçamento


Função de aprovador de orçamento de exceção: A função selecionada aqui pode ignorar o orçamento definido para aprovar despesas.


### 2.8 Informações da Empresa


Para referência, os seguintes detalhes da sua empresa podem ser salvos no ERPNext:


* Data de incorporação
* Telefone não
* Fax
* E-mail
* Local na rede Internet
* Endereço
* Dados de registro



>
> Observação: ao definir o endereço aqui, é importante marcar a caixa de seleção 'É o endereço da sua empresa'.
>
>
>


![Endereço da empresa](/files/company-address.png)


**Para a Índia**, diferentes endereços podem ser adicionados com diferentes números GSTIN se a empresa tiver vários locais. Por exemplo, se sua empresa tiver escritórios em Mumbai, Delhi e Bangalore, você terá que adicionar diferentes endereços com diferentes números GSTIN.


**Detalhes de registro**: Aqui você pode salvar vários números de impostos/cheques/bancos para referência.


### 2.9 Exclusão de todas as transações da empresa


Você pode excluir todas as transações (pedidos, faturas) de uma empresa. *Use com cautela*, as transações uma vez excluídas não podem ser recuperadas.


#### Requisitos


* O usuário tem que ser um gerente de sistema
* O Usuário deve ser o criador da Empresa


#### Passos


1. Clique no botão **Excluir transações** em **Gerenciar**
2. Verifique sua senha
3. Insira o nome da empresa para confirmação
![Empresa após salvar](/files/company-delete-transactions.png)


E pronto. Os dados mestre como Item, Conta, Empregado, BOM etc. permanecerão como estão.


#### O que é afetado?


* Pedidos de venda/compra/faturas, recibos/notas serão excluídos
* As vendas mensais e o histórico de vendas serão apagados
* Todas as notificações serão apagadas
* Endereços de Leads aos quais a Empresa está vinculada serão excluídos
* Todas as comunicações vinculadas à Empresa serão excluídas
* Todas as séries de nomenclatura serão redefinidas
* As entradas de estoque vinculadas a um depósito desta empresa serão excluídas



>
> Introduzido na versão 13.
>
>
>


### 2.10 Alteração da Matriz


Você pode alterar a empresa-mãe de uma empresa existente. Acesse o campo Matriz, selecione a Empresa na lista e salve o formulário.
![Alterar empresa matriz](/files/parent_company.gif)


### 3. Tópicos Relacionados


1. [Configuração de impostos](/docs/v13/user/manual/en/setting-up/setting-up-taxes)
2. [Configurações do sistema](/docs/v13/user/manual/en/setting-up/settings/system-settings)
3. [Importador de planos de contas](/docs/v13/user/manual/en/setting-up/importador de gráficos de contas)
4. [Usuários e permissões](/docs/v13/user/manual/en/setting-up/users-and-permissions)
5. [Adicionando usuários](/docs/v13/user/manual/en/setting-up/users-and-permissions/adding-users)
6. [Cabeçalho](/docs/v13/user/manual/en/setting-up/print/letter-head)
7. [Conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account)
8. [Administrador](/docs/v13/user/manual/en/setting-up/users-and-permissions/administrator)