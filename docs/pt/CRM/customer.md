# Cliente


**Um cliente, que às vezes é conhecido como cliente, comprador ou comprador, é aquele
que recebe mercadorias, serviços, produtos ou ideias de um vendedor por um valor monetário
consideração.**


Cada cliente precisa receber um ID exclusivo. O próprio nome do cliente pode ser o id ou você pode definir uma série de nomenclatura para os IDs a serem gerados em [Configurações de venda](/docs/v13/user/manual/en/selling/selling-settings).


Para aceder à lista de Clientes, aceda a:



>
> Home > CRM > Pipeline de Vendas
>
>
>


Ou



>
> Home > Vendas > Clientes
>
>
>


## 1. Como criar um cliente


1. Vá para a lista Cliente e clique em Novo.
2. Digite o nome completo do cliente.
3. Selecione Individual se o cliente representar uma pessoa física ou Empresa se o cliente representar uma empresa no campo Tipo.
4. Selecione um [Grupo de clientes](/docs/v13/user/manual/en/CRM/grupo de clientes). Individual, Comercial, Sem fins lucrativos e Governamentais estão disponíveis por padrão. Você pode criar grupos adicionais se precisar.
5. Selecione o Território.
6. Se o cliente estiver sendo criado em um lead, você poderá selecionar o mesmo no campo Do lead.
7. Salve.


![Criando novo cliente](/files/create-customer.gif)


Você pode proibir ordens de venda e faturas de vendas contra um cliente clicando em 'Desativado'.



>
> Dica avançada: Se o cliente representa uma de suas próprias empresas, marque 'É cliente interno'. Verifique [Inter Company Invoices] (/docs/v13/user/manual/en/accounts/inter-company-invoices) para mais detalhes.
>
>
>


Você também pode enviar detalhes do cliente por meio da [Ferramenta de importação de dados](/docs/v13/user/manual/en/setting-up/data/data-import).


## 2. Características


O fluxo geral de transações para um cliente é o seguinte:


![Fluxograma de vendas](/files/customer-to-selling-flowchart.jpeg)



>
> Observação: Clientes são separados de Contatos e Endereços. Um cliente pode
> ter vários contatos e endereços.
>
>
>


### 2.1 Múltiplos Contatos e Endereços


[Contatos](/docs/v13/user/manual/en/CRM/contact) e [Endereços](/docs/v13/user/manual/en/CRM/address) são armazenados separadamente para que você possa
anexe vários contatos ou endereços ao cliente.


### 2.2 Permitir a criação de Nota Fiscal de Venda sem Pedido de Venda e Nota de Entrega


Se a opção "Nota de entrega obrigatória" ou "Pedido de venda obrigatório" estiver configurada como "Sim" em [Configurações de venda](/docs/v13/user/manual/en/selling/selling-settings), ela pode ser substituída por um cliente específico habilitando "Permitir Criação de Nota Fiscal Sem Pedido de Venda" ou "Permitir Criação de Nota Fiscal Sem Nota de Remessa" no Cadastro de Clientes.


![Configuração obrigatória do pedido de vendas](/files/customer-so-dn-required.png)


### 2.3 Definir Categoria de Retenção de Imposto


Você pode definir a Categoria de Retenção de Imposto para configurar o TCS contra clientes elegíveis. Para obter mais informações, visite a página [Categoria de retenção de impostos](/docs/v13/user/manual/en/accounts/tax-withholding-category).


### 2.4 Moeda Padrão e Lista de Preços


O ERPNext suporta [Várias Moedas](/docs/v13/user/manual/en/accounts/multi-currency-accounting) e [Listas de preços](/docs/v13/user/manual/en/stock/listas de preços).


Você pode definir a moeda padrão a ser usada para este cliente em pedidos de venda e faturas de venda selecionando a moeda apropriada em Moeda de cobrança.


Da mesma forma, você pode definir a lista de preços padrão a ser usada para esse cliente em pedidos de vendas e faturas de vendas selecionando a moeda apropriada na Lista de preços padrão.


### 2.5 Integração com Contas


Ao contrário de muitos softwares de contabilidade, você não precisa criar um livro contábil separado para cada cliente.
Por padrão, um livro-razão unificado chamado **Debtors** é criado.


No entanto, se você precisar especificamente de um livro-razão separado para um cliente, primeiro crie o livro-razão em
Contas a receber no [Plano de contas](/docs/v13/user/manual/en/accounts/chart-of-accounts.html) e, em seguida, adicione-o na seção CONTABILIDADE do cliente.



>
> Dica avançada: ERPNext suporta [Contabilidade multi-empresa](/docs/v13/user/manual/en/accounts/inter-company-journal-entry). Você pode usar os mesmos registros de clientes em várias empresas. Como um livro contábil é específico da empresa, você precisa selecionar a empresa e o livro razão correspondente na seção CONTABILIDADE se decidir ter um livro contábil separado para um cliente.
>
>
>


### 2.6 Limite de Crédito e Condições de Pagamento


Você pode definir o limite de crédito inserindo o valor no campo 'Limite de crédito'. Leia [Limite de crédito](/docs/v13/user/manual/en/accounts/limite de crédito) para obter mais detalhes.


Você pode selecionar as [Condições de pagamento](/docs/v13/user/manual/en/accounts/payment-terms) padrão a serem aplicadas em pedidos de vendas e faturas de vendas no campo 'Modelo de condições de pagamento padrão'.


### 2.7 Equipe de Vendas e Parceiro de Vendas


Se você tiver um ou mais [Vendedores](/docs/v13/user/manual/en/CRM/vendedor) para gerenciar as vendas para o cliente, você pode adicioná-los na seção EQUIPE DE VENDAS. Se vários vendedores estiverem envolvidos, você pode dividir a contribuição entre eles. Certifique-se de que a soma da contribuição de todos os vendedores seja igual a 100%.


Verifique [Vendedores em transações de vendas](/docs/v13/user/manual/en/selling/articles/sales-persons-in-the-sales-transactions) para obter mais detalhes.


Um [Parceiro de vendas](/docs/v13/user/manual/en/selling/sales-partner) é um distribuidor/revendedor/comissário terceirizado/
afiliado/revendedor que facilita a venda de seus produtos/serviços, por uma comissão.
Se você vende seus produtos/serviços ao cliente através de um parceiro de vendas, você pode definir isso no campo 'Parceiro de vendas' e mencionar a 'Taxa de comissão' para o cálculo da comissão.


### 2.8 Programa de Fidelidade


Se você deseja oferecer um [Programa de Fidelidade](/docs/v13/user/manual/en/accounts/programa de fidelidade) ao cliente, selecione o mesmo no campo Programa de Fidelidade.


### 2.9 Visualizar Razão Contábil e Contas a Receber


Clique no botão Razão de Contabilidade para visualizar todas as transações contábeis com o cliente.


Clique no botão Contas a Receber para visualizar os detalhes de todas as faturas pendentes.


### 2.10 Definir ID do cliente, grupo de clientes padrão, território e lista de preços


Você pode definir como um ID exclusivo deve ser gerado para cada cliente em [Configurações de venda](/docs/v13/user/manual/en/selling/selling-settings).


* **Série de nomenclatura**: Se você deseja que um ID exclusivo seja gerado para cada cliente com base na série de nomenclatura, selecione 'Série de nomenclatura' em Nomeação do cliente por.
* **Nome do cliente**: Se o próprio nome do cliente deve ser usado como um id, selecione 'Nome do cliente' em Nomeação do cliente por. Nesse caso, se você criar dois clientes com nomes idênticos, **- 1** será adicionado ao segundo cliente.


![ID do cliente](/files/cliente-com-nomes-idênticos.png)


Você pode definir o grupo de clientes padrão, território e lista de preços em [Configurações de venda](/docs/v13/user/manual/en/selling/selling-settings).


Você pode personalizar o Customer DocType usando a ferramenta [Customize Form](/docs/v13/user/manual/en/customize-erpnext/custom-field).



.embed-container { posição: relativa; padding-bottom: 56,25%; altura: 0; estouro: oculto; largura máxima: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { posição: absoluta; superior: 0; esquerda: 0; largura: 100%; altura: 100%; }
 





### 3. Tópicos Relacionados


1. [Grupo de clientes](/docs/v13/user/manual/en/CRM/customer-group)
2. [Cotação](/docs/v13/user/manual/en/selling/quotation)
3. [Lista de preços](/docs/v13/user/manual/en/stock/listas de preços)
4. [Contato](/docs/v13/user/manual/en/CRM/contato)
5. [Diferença entre Lead, Contato e Cliente](/docs/v13/user/manual/en/CRM/articles/difference_between_lead_contact_and_customer)