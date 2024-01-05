# Fornecedor



**Fornecedores são empresas ou indivíduos que fornecem produtos ou serviços.**


Para acessar a lista de Fornecedores, acesse:
> Home > Compra > Fornecedor > Fornecedor


## 1. Como criar um Fornecedor


1. Vá para a lista de fornecedores e clique em Novo.
2. Insira um nome para o fornecedor.
3. Selecione o grupo de fornecedores, seja Farmacêutico, Hardware, etc.
4. Salvar.
![Supplier Master](/files/supplier-master.png)


As opções para avisar solicitações de cotação, pedidos de compra, prevenir solicitações de cotação e pedidos de cotação estarão disponíveis assim que você criar um [Scorecard do fornecedor](/docs/pt/buying/supplier-scorecard) e as transações são feitas.


## 2. Recursos


Os campos em transações futuras serão preenchidos automaticamente se os campos "Padrão", como Conta bancária padrão, Modelo de condições de pagamento padrão etc., estiverem definidos no Fornecedor.


### 2.1 Detalhes fiscais


* **País**: Se o fornecedor for de outro país, você pode alterá-lo aqui.
* **Identificação Fiscal**: Número de identificação fiscal do fornecedor.
* **Categoria de imposto**: está vinculada à [Regra de imposto](/docs/pt/accounts/tax-rule). Se uma Categoria de Imposto for definida aqui, ao selecionar este fornecedor, o respectivo modelo de Impostos e Encargos de Compra será aplicado. Este modelo está vinculado à Regra Fiscal e a Regra Fiscal está vinculada a uma Categoria Fiscal. A Categoria de Imposto pode ser utilizada para agrupar fornecedores aos quais será aplicado o mesmo imposto. Por exemplo: governamental, comercial, etc.
* **Idioma de impressão**: o idioma no qual o documento será impresso.
* **Categoria de retenção de imposto**: para a Índia, categoria TDS para o fornecedor. Ao definir uma categoria aqui, ela será buscada na [Fatura de Compra](/docs/pt/accounts/purchase-invoice). Para obter mais informações, visite a página [Categoria de retenção de imposto](/docs/pt/accounts/tax-withholding-category).
* **Desativado**: Desativa o Fornecedor e ele não será mostrado na Lista de Fornecedores.
* **É transportador**: se o fornecedor estiver vendendo seus serviços de transporte, marque esta caixa. O campo 'GST Transporter ID' ficará visível se este campo estiver marcado.
* **Fornecedor Interno**: Se o fornecedor for de uma empresa irmã ou controladora, marque este campo e selecione a empresa que representa.


Para a Índia:


* **Categoria GST**: selecione uma categoria GST do fornecedor.
* **PAN**: para a Índia, detalhes do cartão PAN (número de conta permanente) do fornecedor.


### 2.2 Permitir a criação de fatura de compra sem pedido de compra e recibo de compra


Se a opção "Ordem de compra obrigatória" ou "Recibo de compra obrigatório" estiver configurada como "Sim" em [Configurações de compra](/docs/pt/buying/buying-settings), ele pode ser substituído para um determinado fornecedor ativando "Permitir criação de fatura de compra sem pedido de compra" ou "Permitir criação de fatura de compra sem recibo de compra" no Cadastro de fornecedores.


![Supplier Master](/files/supplier-po-pr-required.png)


### 2.3 Moeda e lista de preços


**Moeda de cobrança**: a moeda do seu fornecedor pode ser diferente da moeda da sua empresa. Se você escolher JPY como fornecedor, a moeda será preenchida como JPY e a taxa de câmbio será mostrada para futuras transações de compra.


![Moeda do fornecedor](/files/supplier-currency.gif)


Cada Fornecedor pode ter uma **Lista de Preços** padrão para que toda vez que você comprar um novo item deste fornecedor por preços diferentes, a lista de preços associada ao fornecedor também seja atualizada. Abaixo da lista de preços vem o preço do item, você pode ver os preços em Compra > Itens e Preços > Preço do Item.


Se você selecionar este fornecedor específico, a Lista de Preços associada será obtida nas transações de Compra.


### 2.4 Limite de crédito


* **Modelo de termos de pagamento padrão**: se um modelo de termos de pagamento for definido aqui, ele será selecionado automaticamente para futuras transações de compra.
* **Bloquear Fornecedor**: Você pode bloquear faturas, pagamentos ou ambos de um fornecedor até uma data específica. Escolha 'Tipo de espera', se você não selecionar um tipo de espera, o ERPNext irá configurá-lo para "Todos". Quando um fornecedor é bloqueado, seu status será mostrado como 'Em Espera'.


Os tipos de retenção são os seguintes:


	+ Faturas: O ERPNext não permitirá a criação de Faturas de Compra ou Pedidos de Compra para o fornecedor
	+ Pagamentos: O ERPNext não permitirá a criação de Lançamentos de Pagamento para o Fornecedor
	+ Todos: ERPNext aplicará ambos os tipos de retenção acimaSe você não definir uma data de lançamento, o ERPNext irá reter o Fornecedor **indefinidamente**.


### 2.5 Contas a pagar padrão


Adicione a conta padrão a partir da qual as faturas deste fornecedor serão pagas. Adicione linhas adicionais para mais empresas. Você pode selecionar apenas uma conta por empresa.


Você pode **integrar** um fornecedor a uma conta. Para todos os Fornecedores, a conta "Credor" é definida como conta a pagar padrão. Quando a fatura de compra é criada, o valor a pagar ao fornecedor é contabilizado na conta "Credores".


Se desejar personalizar a conta a pagar para o fornecedor, você deve primeiro adicionar uma conta a pagar no Plano de contas e, em seguida, selecionar essa conta a pagar no cadastro do fornecedor.


![Supplier Master](/files/supplier-payable-account.png)


Se você não quiser personalizar a conta a pagar e continuar com a conta a pagar padrão "Credor", não atualize nenhum valor na tabela da Conta do fornecedor padrão.


> Dica: A conta a pagar padrão é definida no cadastro da empresa. Se você quiser definir outra conta como Conta padrão para contas a pagar em vez de Conta de credores, vá para o mestre da empresa e defina essa conta como "Conta a pagar padrão".


Dependendo do seu [plano](https://erpnext.com/pricing), você pode adicionar várias empresas em sua instância do ERPNext. Um fornecedor pode ser usado em várias empresas. Nesse caso, você deve definir a Conta a Pagar da Empresa para o Fornecedor na tabela "Contas a Pagar Padrão", ou seja, adicionar várias linhas.


### 2.6 Mais informações


Você pode adicionar o site do fornecedor e quaisquer detalhes adicionais sobre ele nesta seção. Se você congelar um fornecedor com a opção 'Está Congelado', os lançamentos contábeis do fornecedor serão congelados. Neste caso, o único usuário cujas entradas ultrapassarão o 'congelamento' é a função atribuída em 'Função permitida para definir contas congeladas e editar entradas congeladas' em Contabilidade > Configurações > Configurações de contas. Isto é útil quando o nome do fornecedor ou os dados bancários estão sendo alterados.


### 2.7 Endereço e contatos


Contatos e Endereços no ERPNext são armazenados separadamente para que você possa criar vários Contatos e Endereços para um Fornecedor. Assim que o Fornecedor for salvo, você encontrará a opção de criar Contato e Endereço para esse Fornecedor.


![Supplier Master](/files/supplier-new-address-contact.png)


> Dica: quando você seleciona um fornecedor em qualquer transação, o contato para o qual o ID do campo "É principal" está marcado, ele buscará automaticamente os detalhes do fornecedor.


### 2.8 Depois de salvar


Depois que todos os dados necessários forem preenchidos, salve o documento. Ao salvar, as opções para criar o seguinte serão vistas no Painel:


* **Solicitação de cotação**: uma solicitação de cotação contra este fornecedor.
* **Cotação do fornecedor**: quaisquer cotações que o fornecedor lhe enviou e você enviou ao sistema.
* **Pedido de compra**: pedidos de compra que você fez contra este fornecedor.
* **Recibo de compra**: recibos de compra fornecidos por este fornecedor que você salvou no sistema.
* **Fatura de compra**: faturas de compra que você fez contra este fornecedor.
* **Lançamento de pagamento**: Lançamentos de pagamento para as faturas de compra deste fornecedor.
* **Regra de preços**: quaisquer regras de preços vinculadas a este fornecedor. Consulte a seção *2.2 Moeda e lista de preços* para saber como funciona.


![Salvar fornecedor](/files/supplier-save.png)


Ao clicar no botão Visualizar, você pode visualizar o Razão Contábil ou Contas a Pagar diretamente deste fornecedor.


Há um botão para 'Enviar lembrete de atualização de GST' ao fornecedor. Você precisa ter uma [conta de e-mail](/docs/pt/setting-up/email/email-account) configurada primeiro.


## 3. Vídeo








### 4. Tópicos Relacionados


1. [Cotação do fornecedor](/docs/pt/buying/supplier-quotation)
2. [Cartão de pontuação do fornecedor](/docs/pt/buying/supplier-scorecard)
3. [Manutenção do código do item do fornecedor no cadastro de itens](/docs/pt/buying/articles/maintaining-suppliers-part-no-in-item)



