# Cliente



**Um cliente, às vezes conhecido como cliente, comprador ou comprador, é aquele
que recebe bens, serviços, produtos ou ideias de um vendedor por um valor monetário
consideração.**


Cada cliente precisa receber um ID exclusivo. O próprio nome do cliente pode ser o ID ou você pode definir uma série de nomenclatura para os IDs a serem gerados em [Configurações de venda](/docs/pt/selling/selling-settings). 


Para acessar a lista de Clientes, acesse:
> Página inicial > CRM > Pipeline de vendas


Ou


> Início > Vendas > Clientes


## 1. Como criar um cliente


1. Vá para a lista de clientes e clique em Novo.
2. Insira o nome completo do cliente.
3. Selecione Individual se o cliente representa um indivíduo ou Empresa se o cliente representa uma empresa no campo Tipo.
4. Selecione um [Grupo de clientes](/docs/pt/CRM/customer-group). Individual, Comercial, Sem Fins Lucrativos e Governamental estão disponíveis por padrão. Você pode criar grupos adicionais se precisar.
5. Selecione o território.
6. Se o cliente estiver sendo criado em relação a um lead, você poderá selecionar o mesmo no campo Do lead.
7. Salvar.


![Criando novo cliente](/files/create-customer.gif)


Você pode proibir pedidos de vendas e faturas de vendas de um cliente clicando em 'Desativado'.


>Dica avançada: Se o cliente representa uma de suas próprias empresas, marque 'É cliente interno'. Verifique [Faturas entre empresas](/docs/pt/accounts/inter-company-invoices) para obter mais detalhes.


Você também pode fazer upload de detalhes do cliente por meio da [ferramenta de importação de dados](/docs/pt/setting-up/data/data-import).


## 2. Recursos


O fluxo geral de transações de um cliente é o seguinte:


![Fluxograma de vendas](/files/customer-to sell-flowchart.jpeg)


> Observação: Clientes são separados de Contatos e Endereços. Um cliente pode
ter vários contatos e endereços.


### 2.1 Vários contatos e endereços


[Contatos](/docs/pt/CRM/contact) e [Endereços](/docs/pt/CRM/address) são armazenados separadamente para que você possa
anexe vários contatos ou endereços ao cliente.


### 2.2 Permitir a criação de fatura de venda sem pedido de venda e nota de entrega


Se a opção "Nota de entrega obrigatória" ou "Ordem de venda obrigatória" estiver configurada como "Sim" em [Configurações de venda](/docs/pt/selling/selling-settings), ele pode ser substituído para um cliente específico ativando "Permitir criação de fatura de venda sem pedido de venda" ou "Permitir criação de fatura de venda sem nota de entrega" no Cadastro de clientes.


![Configuração obrigatória de pedido de vendas](/files/customer-so-dn-required.png)


### 2.3 Definir categoria de retenção de imposto


Você pode definir a categoria de retenção de imposto para configurar o TCS contra clientes qualificados. Para obter mais informações, visite a página [Categoria de retenção de imposto](/docs/pt/accounts/tax-withholding-category).


### 2.4 Moeda padrão e lista de preços


ERPNext suporta [Múltiplas Moedas](/docs/pt/accounts/multi-currency-accounting) e [Listas de preços](/docs/pt/stock/price-lists).


Você pode definir a moeda padrão a ser usada para esse cliente em pedidos de vendas e faturas de vendas selecionando a moeda apropriada em Moeda de cobrança.


Da mesma forma, você pode definir a lista de preços padrão a ser usada para este cliente em pedidos de vendas e faturas de vendas selecionando a moeda apropriada em Lista de preços padrão.


### 2.5 Integração com contas


Ao contrário de muitos softwares de contabilidade, você não precisa criar um livro contábil separado para cada cliente.
Por padrão, um livro razão unificado chamado **Devedores** é criado.


No entanto, se você precisar especificamente de um razão separado para um cliente, primeiro crie o razão em
Contas a Receber no [Plano de Contas](/docs/pt/accounts/chart-of-accounts.html) e depois adicione-o na seção CONTABILIDADE do cliente.


>Dica Avançada: ERPNext suporta [Contabilidade Multiempresa](/docs/pt/accounts/inter-company-journal-entry). Você pode usar os mesmos registros de clientes em diversas empresas. Como um razão contábil é específico da empresa, você precisa selecionar a empresa e o razão correspondente na seção CONTABILIDADE se decidir ter um razão contábil separado para um cliente.


### 2.6 Limite de crédito e condições de pagamento


Você pode definir o limite de crédito inserindo o valor no campo 'Limite de crédito'. Leia [Limite de crédito](/docs/pt/accounts/credit-limit) para obter mais detalhes.


Você pode selecionar as [Condições de pagamento](/docs/pt/accounts/payment-terms) padrão a serem aplicadas em pedidos de vendas e faturas de vendas em 'Pagamento padrão Campo Modelo de termos.


### 2.7 Equipe de vendas e parceiro de vendas


Se você tiver um ou mais [Vendedores](/docs/pt/CRM/sales-person) para gerenciar as vendas ao cliente, você poderá adicioná-los na seção EQUIPE DE VENDAS. Se vários vendedores estiverem envolvidos, você poderá dividir a contribuição entre eles. Certifique-se de que a soma da contribuição de todos os vendedores seja igual a 100%.


Verifique [Vendedores em transações de vendas](/docs/pt/selling/articles/sales-persons-in-the-sales-transactions) para obter mais detalhes. 


Um [Parceiro de vendas](/docs/pt/selling/sales-partner) é um distribuidor/revendedor/agente comissionado terceirizado/
afiliado/revendedor que facilita a venda de seus produtos/serviços, mediante pagamento de comissão.
Se você vende seus produtos/serviços ao cliente através de um parceiro de vendas você pode configurá-lo no campo ‘Parceiro de Vendas’ e mencionar a ‘Taxa de Comissão’ para cálculo da comissão.


### 2.8 Programa de fidelidade


Se você quiser oferecer um [Programa de Fidelidade](/docs/pt/accounts/loyalty-program) ao cliente, selecione-o no campo Programa de Fidelidade. 


### 2.9 Visualizar razão contábil e contas a receber


Clique no botão Razão Contábil para visualizar todas as transações contábeis com o cliente.


Clique no botão Contas a Receber para visualizar os detalhes de todas as faturas pendentes.


### 2.10 Definir ID do cliente, grupo de clientes padrão, território e lista de preços


Você pode definir como um ID exclusivo deve ser gerado para cada cliente em [Configurações de venda](/docs/pt/selling/selling-settings).


* **Série de nomenclatura**: se desejar que um ID exclusivo seja gerado para cada cliente com base na série de nomenclatura, selecione 'Série de nomenclatura' em Nomeação do cliente por.
* **Nome do cliente**: se o próprio nome do cliente deve ser usado como um ID, selecione 'Nome do cliente' em Nomeação do cliente por. Neste caso, se você criar dois clientes com nomes idênticos, **-1** será sufixado ao segundo cliente.


![ID do cliente](/files/customer-with-identical-names.png)


Você pode definir o grupo de clientes padrão, o território e a lista de preços em [Configurações de venda](/docs/pt/selling/selling-settings).


Você pode personalizar o DocType do cliente usando a ferramenta [Personalizar formulário](/docs/pt/customize-erpnext/custom-field).



.embed-container {posição: relativa; preenchimento inferior: 56,25%; altura: 0; estouro: oculto; largura máxima: 100%; } .embed-container iframe, .embed-container objeto, .embed-container embed {posição: absoluto; superior: 0; esquerda: 0; largura: 100%; altura: 100%; }
 





### 3. Tópicos Relacionados


1. [Grupo de clientes](/docs/pt/CRM/customer-group)
2. [Cotação](/docs/pt/selling/quotation)
3. [Lista de preços](/docs/pt/stock/price-lists)
4. [Contato](/docs/pt/CRM/contact)
5. [Diferença entre lead, contato e cliente](/docs/pt/CRM/articles/difference_between_lead_contact_and_customer)



