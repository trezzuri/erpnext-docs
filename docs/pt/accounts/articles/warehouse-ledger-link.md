# Vinculando armazém de estoque e contas


O valor do estoque armazenado nos armazéns precisa ser rastreado.


Cada depósito está vinculado a um razão no plano de contas por meio do campo 'Conta' no depósito.


![Registro de Ativos de Estoque no Armazém](/files/stock-asset-ledger-in-warehouse.png)


Se o campo Conta estiver vazio em um depósito, a Conta mencionada no pai desse depósito será considerada. Se uma conta não puder ser determinada pelo rastreamento da hierarquia, a conta de estoque padrão mencionada no registro da empresa será considerada.


![Conta de estoque padrão na empresa](/files/default-inventory-account-in-company.png)


Quando uma empresa é criada, um livro chamado 'Estoque em Mão' é criado por padrão no Plano de Contas.


**Plano de contas > Ativos > Ativos circulantes > Ativos em estoque > Estoque em mãos.**


Se necessário, você pode criar livros adicionais no grupo 'Ativos de estoque'.


![Ledger de Ativos de Estoque no Plano de Contas](/files/stock-asset-ledger-in-coa.png)