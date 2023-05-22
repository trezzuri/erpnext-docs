# Vinculação do armazém de estoque e contas


O valor do estoque armazenado nos armazéns precisa ser rastreado.


Cada depósito está vinculado a um razão no plano de contas por meio do campo 'Conta' no depósito.


![Ledger de ativos de estoque no armazém](/files/stock-asset-ledger-in-warehouse.png)


Se o campo Conta estiver vazio em um depósito, a Conta mencionada no pai desse depósito será considerada. Se uma conta não puder ser determinada pelo rastreamento da hierarquia, a conta de estoque padrão mencionada no registro da empresa será considerada.


![Conta de inventário padrão na empresa](/files/default-inventory-account-in-company.png)


Quando uma empresa é criada, um livro chamado 'Estoque em Mão' é criado por padrão no Plano de Contas.


**Plano de contas > Ativos > Ativos circulantes > Ativos de estoque > Estoque em mãos.**


Se necessário, você pode criar livros contábeis adicionais no grupo 'Ativos de estoque'.


![Ledger de ativos de estoque no plano de contas](/files/stock-asset-ledger-in-coa.png)

