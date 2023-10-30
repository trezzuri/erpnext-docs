# Faturas entre empresas



**Uma fatura diária entre empresas é feita entre organizações que pertencem ao mesmo grupo.**


Além de criar faturas de compra ou faturas de vendas para uma única empresa, você pode criar faturas interligadas para várias empresas.


Por exemplo, você pode criar uma fatura de compra para uma empresa, diga 'Empresa ABC', e criar uma fatura de vendas em relação a esta fatura de compra para outra empresa, diga 'Empresa XYZ', e vinculá-las.


## 1. Como criar faturas entre empresas


### 1.1 Configuração


1. Acesse: **Contas > Mestres > Cliente**.
2. Selecione o Cliente que você deseja escolher para a fatura interligada.
3. Ative a caixa de seleção **É cliente interno** mostrada a seguir:


![Cliente Interno](/files/inter-company-customer.png)


1. Adicione a empresa que o Cliente representa no campo **Representa a Empresa**. Esta é a empresa para a qual a fatura de vendas será criada.
2. Na tabela **Permissão para transações com**, adicione a empresa para a qual você criará uma fatura de compra.
3. Agora, quando você criar uma fatura de compra para a empresa A (o cliente é da empresa B, o vendedor é a empresa A), ela será vinculada à fatura de venda da empresa A criada usando esse cliente interno da empresa B.
4. Agora, você precisa seguir um procedimento semelhante para configurar um fornecedor para faturas interligadas.
5. Acesse: **Contas > Mestres > *Selecione o Fornecedor***
6. Marque É fornecedor interno.
7. No campo **Representa a empresa**, adicione a empresa que você adicionou na tabela **Permissão para transações** para o cliente.
8. Na tabela **Permissão para transações** do Fornecedor, adicione a empresa que o Cliente representa. Esta é a empresa contra a qual você emitirá uma fatura de compra interligada.
9. Aqui está uma captura de tela da empresa fornecedora para evitar qualquer confusão:


![Fornecedor entre empresas](/files/inter-company-supplier.png)


### 1.2 Criando a fatura


1. Agora, crie uma nova [Fatura de vendas](/docs/pt/accounts/sales-invoice), preencha os campos.
2. Lembre-se de selecionar o Cliente que é cliente interno e empresa da qual está comprando.
3. Salve e envie a fatura.


![Fatura entre empresas](/files/make-inter-company-invoice.png)


![](/docs/v13/assets/img/accounts/)
4. Antes de fazer uma *fatura entre empresas* você precisa fazer o seguinte:


	1. O preço de venda e compra entre as empresas deve estar sincronizado.
	2. Vá para **Estoque > Lista de Preços** e crie uma nova Lista de Preços para transações entre empresas.
	3. Marque Venda e Compra nesta nova Lista de Preços.
	4. Vá para **Compras > Fornecedor > *fornecedor interno***, na seção de moeda e lista de preços, defina a lista de preços para a nova que acabou de ser criada.
	5. Faça o mesmo para o cliente interno, ou seja, defina a lista de preços para a nova.
	6. Agora você pode fazer uma fatura de compra ou venda entre empresas.
5. No menu suspenso do botão **Fazer**, você encontrará um link **Fatura entre empresas**. Ao clicar no link, você será direcionado para uma nova página de formulário de fatura de compra.
6. Aqui, o fornecedor e a empresa serão buscados automaticamente dependendo da empresa que você selecionou na Nota Fiscal de Venda.
> ***Lembre-se***: Só pode haver um único fornecedor ou cliente interno por empresa.
7. Envie a fatura, pronto! Agora, ambas as faturas estão interligadas. *Além disso, ao cancelar qualquer uma das faturas, o link também será quebrado.*


> Observação: uma fatura entre empresas afetará apenas o razão contábil e não o razão de estoque. Isso ocorre porque as empresas pertencem ao mesmo grupo de empresas.


Você pode seguir o mesmo processo para criar uma fatura de compra e, em seguida, uma fatura de vendas interligada a partir da fatura de compra enviada.


### 2. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Lançamento contábil entre empresas](/docs/pt/accounts/inter-company-journal-entry)



