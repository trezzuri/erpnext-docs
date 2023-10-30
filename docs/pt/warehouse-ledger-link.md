# Vinculando depósito de estoque e contas



O valor do estoque armazenado nos armazéns precisa ser rastreado.


Cada armazém está vinculado a um razão no plano de contas através do campo 'Conta' no armazém.


![Registro de ativos de estoque no armazém](/files/stock-asset-ledger-in-warehouse.png)


Se o campo Conta estiver vazio em um armazém, então será considerada a Conta mencionada no pai desse armazém. Se uma conta não puder ser determinada traçando a hierarquia, será considerada a conta de estoque padrão mencionada no registro da empresa.


![Conta de estoque padrão na empresa](/files/default-inventory-account-in-company.png)


Quando uma empresa é criada, um livro-razão denominado 'Estoque em mãos' é criado por padrão no Plano de contas.


**Plano de contas > Ativos > Ativo circulante > Ativos em estoque > Estoque em mãos.**


Se necessário, você pode criar livros-razão adicionais no grupo "Ativos de Estoque".


![Lista de ativos de estoque no plano de contas](/files/stock-asset-ledger-in-coa.png)



