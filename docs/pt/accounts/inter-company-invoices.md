# Faturas entre empresas


**Uma Nota Fiscal Interempresarial é feita entre organizações que pertencem ao mesmo grupo.**


Além de criar faturas de compra ou faturas de venda para uma única empresa, você pode criar faturas interligadas para várias empresas.


Por exemplo, você pode criar uma fatura de compra para uma empresa, digamos 'Empresa ABC', e criar uma fatura de venda contra esta fatura de compra para outra empresa, digamos 'Empresa XYZ' e vinculá-las.


## 1. Como criar faturas entre empresas


### 1.1 Configuração


1. Vá para: **Contas > Masters > Cliente**.
2. Selecione o cliente que você deseja escolher para a fatura interligada.
3. Ative a caixa de seleção, **É cliente interno** mostrado a seguir:


![Internal Customer](/files/inter-company-customer.png)


1. Adicione a empresa que o Cliente representa no campo **Represents Company**. Esta é a empresa para a qual a Nota Fiscal de Venda será criada.
2. Na tabela **Allowed To Transact With**, adicione a empresa para a qual você criará uma fatura de compra.
3. Agora, quando você criar uma Nota Fiscal de Compra contra a empresa A (o cliente é da empresa B, o vendedor é a empresa A), ela será vinculada à Nota Fiscal de Venda da empresa A criada usando este Cliente Interno da empresa B.< /li>
- Agora, você precisa seguir um procedimento semelhante para configurar um Fornecedor para faturas interligadas.
- Vá para: **Contas > Masters > *Selecione o Fornecedor***
- Marque em É fornecedor interno.
- No campo **Represents Company**, adicione a empresa que você adicionou na tabela **Allowed To Transact With** para o cliente.
- Na tabela **Allowed To Transact With** para o Fornecedor, adicione a empresa que o Cliente representa. Esta é a empresa contra a qual você fará uma Fatura de Compra interligada.
- Aqui está uma captura de tela da empresa fornecedora para evitar qualquer confusão:


![Inter Company Supplier](/files/inter-company-supplier.png)


### 1.2 Criação da fatura


1. Agora, crie uma nova [Fatura de venda](/docs/pt/accounts/sales-invoice), preencha os campos.
2. Lembre-se de selecionar o Cliente que é um cliente interno e a empresa da qual ele está comprando.
3. Salve e envie a fatura.


![Fatura entre empresas](/files/make-inter-company-invoice.png)


![](/docs/v13/assets/img/accounts/)
4. Antes de fazer uma *Fatura entre empresas*, você precisa fazer o seguinte:


	1. O preço de compra e venda entre as empresas deve estar sincronizado.
	2. Vá para **Estoque > Lista de preços**, crie uma nova Lista de preços para transações entre empresas.
	3. Marque Venda e Compra nesta nova Lista de Preços.
	4. Vá para **Comprar > Fornecedor > *fornecedor interno***, na seção moeda e lista de preços, defina a lista de preços para a nova recém-criada.
	5. Faça o mesmo para o cliente interno, ou seja, defina a tabela de preços para a nova.
	6. Agora você pode fazer uma Nota Fiscal de Compra ou Venda entre empresas.
5. Na lista suspensa do botão **Criar**, você encontrará um link **Fatura intercompanhia**, ao clicar no link, você será direcionado para uma nova página de formulário de Fatura de compra.< /li>
- Aqui, o fornecedor e a empresa serão buscados automaticamente, dependendo da empresa que você selecionou na Nota Fiscal.
> ***Lembre-se***: Só pode haver um único Fornecedor Interno ou Cliente por empresa.
- Envie a fatura, pronto! Agora, ambas as faturas estão interligadas. *Além disso, ao cancelar qualquer uma das faturas, o link também será interrompido.*



> 
> Observação: uma fatura entre empresas afetará apenas o livro-razão contábil e não o livro-razão de estoque. Isso ocorre porque as empresas pertencem ao mesmo grupo de empresas.
> 
> 
> 


Você pode seguir o mesmo processo para criar uma fatura de compra e, em seguida, uma fatura de venda interligada a partir da fatura de compra enviada.


### 2. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Entrada no diário da empresa](/docs/pt/accounts/inter-company-journal-entry)
