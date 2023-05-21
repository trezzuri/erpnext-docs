# Faturas entre empresas


**Uma Nota Fiscal Interempresarial é feita entre organizações que pertencem ao mesmo grupo.**


Juntamente com a criação de faturas de compra ou faturas de venda para uma única empresa, você pode criar faturas interligadas para várias empresas.


Por exemplo, você pode criar uma Fatura de Compra para uma empresa, digamos 'Empresa ABC', e criar uma Fatura de Vendas contra esta Fatura de Compra para outra empresa, digamos 'Empresa XYZ' e vinculá-las.


## 1. Como criar Faturas Entre Empresas


### 1.1 Configuração


1. Acesse: **Contas > Masters > Cliente**.
2. Selecione o Cliente que deseja escolher para a fatura interligada.
3. Ative a caixa de seleção **É cliente interno** mostrada a seguir:


![Cliente Interno](/files/inter-company-customer.png)


1. Adicione a empresa que o Cliente representa no campo **Represents Company**. Esta é a empresa para a qual a Nota Fiscal de Venda será criada.
2. Na tabela **Allowed To Transact With**, adicione a empresa contra a qual você criará uma fatura de compra.
3. Agora, ao criar uma Nota Fiscal de Compra contra a empresa A (o cliente é da empresa B, o vendedor é a empresa A), ela será vinculada à Nota Fiscal de Venda da empresa A criada a partir deste Cliente Interno da empresa B.
4. Agora, você precisa seguir um procedimento semelhante para configurar um Fornecedor para faturas interligadas.
5. Acesse: **Contas > Masters > *Selecione o Fornecedor***
6. Marque É Fornecedor Interno.
7. No campo **Represents Company**, adicione a empresa que você adicionou na tabela **Allowed To Transact With** para o cliente.
8. Na tabela **Allowed To Transact With** para o Fornecedor, adicione a empresa que o Cliente representa. Esta é a empresa contra a qual você fará uma Nota Fiscal de Compra interligada.
9. Aqui está uma captura de tela da empresa fornecedora para evitar qualquer confusão:


![Fornecedor entre empresas](/files/inter-company-supplier.png)


### 1.2 Criação da Fatura


1. Agora, crie uma nova [Fatura de venda](/docs/v13/user/manual/pt/accounts/fatura-de-venda), preencha os campos.
2. Lembre-se de selecionar o Cliente que é cliente interno e empresa da qual está comprando.
3. Salve e envie a fatura.


![Fatura entre empresas](/files/make-inter-company-invoice.png)


![](/docs/v13/assets/img/accounts/)
4. Antes de fazer uma *Fatura entre empresas*, você precisa fazer o seguinte:


1. O preço de compra e venda entre as empresas deve estar sincronizado.
2. Vá para **Estoque > Lista de Preços**, crie uma nova Lista de Preços para transações entre empresas.
3. Marque Vendendo e Comprando nesta nova Lista de Preços.
4. Vá para **Compras > Fornecedor > *fornecedor interno***, na seção lista de moedas e preços, defina a lista de preços para a nova que acabou de ser criada.
5. Faça o mesmo para o cliente interno, ou seja, configure a tabela de preços para a nova.
6. Agora, você pode fazer uma Nota Fiscal de Compra ou Venda entre empresas.
5. Abaixo do botão **Fazer**, você encontrará um link **Inter Company Invoice**, ao clicar no link, você será direcionado para uma nova página de formulário de Compra de Fatura.
6. Aqui, o fornecedor e a empresa serão buscados automaticamente, dependendo da empresa que você selecionou na Nota Fiscal.
> ***Lembre-se***: Só pode haver um único Fornecedor ou Cliente Interno por empresa.
7. Envie a nota fiscal, pronto! Agora, ambas as faturas estão interligadas. *Além disso, ao cancelar qualquer uma das faturas, o link também será interrompido.*



>
> Observação: Uma fatura entre empresas afetará apenas o livro-razão contábil e não o livro-razão de estoque. Isso ocorre porque as empresas pertencem ao mesmo grupo de empresas.
>
>
>


Você pode seguir o mesmo processo para criar uma fatura de compra e, em seguida, uma fatura de venda interligada a partir da fatura de compra enviada.


### 2. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)
3. [Entrada no diário da empresa](/docs/v13/user/manual/en/accounts/inter-company-journal-entry)