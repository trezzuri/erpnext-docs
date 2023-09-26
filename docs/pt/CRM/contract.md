# Contrato


**Um contrato é um acordo juridicamente vinculativo entre um Fornecedor e um Cliente sobre a venda de produtos ou serviços.**


Um contrato é legalmente executável porque atende aos requisitos e à aprovação da lei. Um acordo normalmente envolve a troca de bens, serviços, dinheiro ou promessas de qualquer um deles.


Para acessar a lista de contratos, acesse:



> 
> Página inicial > Pipeline de vendas > Contrato
> 
> 
> 


## 1. Como criar um contrato


1. Vá para a lista de Contratos e clique em Novo.
2. Escolha o cliente.
3. Digite os termos do contrato. Um modelo também pode ser criado para obter facilmente os termos.
4. Salvar.
![Contract](/files/contract.png)


**Party User**: O funcionário da sua empresa que está em contato com o cliente.


### 1.1 Status


* **Não assinado**: O Contrato ainda não foi assinado pelo Cliente.
* **Ativo**: O Contrato foi assinado e está ativo durante o Período do Contrato.
* **Inativo**: O Contrato está fora do Período do Contrato e não é mais válido.


## 2. Recursos


### 2.1 Período do contrato


A data inicial e final dentro da qual o contrato é válido.


### 2.2 Detalhes do signatário


Esta seção aparecerá quando a caixa de seleção 'Assinado' estiver marcada para indicar que o Cliente assinou e aceitou o Contrato.


![Signee do contrato](/files/contract-signee.png)


* **Signee**: Insira o nome da pessoa que assinou o Contrato.
* **Assinado em**: a data em que o Contrato foi assinado.


### 2.3 Detalhes do contrato


Digite os termos do Contrato no campo Termos do contrato. Você pode criar um modelo de contrato e o modelo pode ser selecionado para buscar os termos do contrato.


### 2.4 Detalhes do processamento


Se o Contrato exigir algum cumprimento por parte do Fornecedor (seu), seus detalhes podem ser registrados na tabela de Termos de Cumprimento.


![Contract Fulfilment](/files/contract-fulfilment.png)


* **Requisito**: insira um requisito que precisa ser atendido. Por exemplo, 'instalação'.
* **Observações**: quaisquer observações sobre o requisito podem ser inseridas aqui.


### 2.5 Modelo de contrato


Um modelo de contrato é um esboço padronizado de um contrato sem os detalhes envolvidos. Você pode criar um novo modelo acessando:



> 
> Página inicial > CRM > Modelo de contrato
> 
> 
> 


Você pode criar modelos usando Jinja. Ex.:



```
As partes celebram este contrato em &lcub;&lcub; start_date }}.

```

Ao criar um novo contrato usando este modelo, o `&lcub;&lcub; start_date }}` é substituído pela data inserida no campo com o mesmo nome.


![Modelo de contrato](/files/contract-template-jinja.gif)


### 2.6 Referências


Se o Contrato pode ser vinculado a uma transação no SOMA. Selecione o tipo de transação e a transação específica. Os documentos que podem ser vinculados são:


* Cotação
* Projeto
* Pedido de venda
* Pedido de compra
* Fatura de venda
* Fatura de compra


![Contract References](/files/contract-reference.png)


### 3. Tópicos Relacionados


1. [Cotação](/docs/pt/selling/quotation)
2. [Pedido de compra](/docs/pt/buying/purchase-order)
3. [Pedido de venda](/docs/pt/selling/sales-order)
4. [Recibo de compra](/docs/pt/stock/purchase-receipt)
5. [Nota de entrega](/docs/pt/stock/delivery-note)
6. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
7. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
