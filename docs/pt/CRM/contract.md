# Contrato


**Um contrato é um acordo juridicamente vinculativo entre um Fornecedor e um Cliente sobre a venda de produtos ou serviços.**


Um contrato é legalmente executável porque atende aos requisitos e à aprovação da lei. Um acordo normalmente envolve a troca de bens, serviços, dinheiro ou promessas de qualquer um deles.


Para acessar a lista de Contratos, acesse:



>
> Home > Pipeline de Vendas > Contrato
>
>
>


## 1. Como Criar um Contrato


1. Vá para a lista Contrato e clique em Novo.
2. Escolha o Cliente.
3. Insira os termos do contrato. Um modelo também pode ser criado para buscar facilmente os termos.
4. Salve.
![Contrato](/files/contract.png)


**Party User**: O funcionário da sua Empresa que está em contato com o Cliente.


### 1.1 Situações


* **Unsigned**: O Contrato ainda não foi assinado pelo Cliente.
* **Ativo**: O Contrato foi assinado e está ativo durante o Período do Contrato.
* **Inativo**: O Contrato está fora do Período Contratual e não é mais válido.


## 2. Características


### 2.1 Período do Contrato


As datas de Início e Fim dentro das quais o Contrato é válido.


### 2.2 Detalhes do Signatário


Esta seção aparecerá quando a caixa de seleção 'Assinado' estiver marcada para indicar que o Cliente assinou e aceitou o Contrato.


![Assinante do Contrato](/files/contract-signee.png)


* **Signee**: Informe o nome da pessoa que assinou o Contrato.
* **Assinado em**: A data em que o Contrato foi assinado.


### 2.3 Detalhes do Contrato


Insira os termos do Contrato no campo Termos do Contrato. Você pode criar um modelo de contrato e o modelo pode ser selecionado para buscar os termos do contrato.


### 2.4 Detalhes de Cumprimento


Se o Contrato exigir algum cumprimento por parte do Fornecedor (seu), seus detalhes podem ser registrados na tabela de Termos de Cumprimento.


![Cumprimento do contrato](/files/contract-fulfilment.png)


* **Requisito**: Insira um requisito que precisa ser cumprido. Por exemplo, 'instalação'.
* **Observações**: Qualquer observação sobre o requisito pode ser inserida aqui.


### 2.5 Modelo de Contrato


Um modelo de contrato é um esboço padronizado de um contrato sem os detalhes envolvidos. Você pode criar um novo modelo acessando:



>
> Home > CRM > Modelo de contrato
>
>
>


Você pode criar modelos usando Jinja. Por exemplo:



```
As partes celebram este contrato em {{ start_date }}.

```

Ao criar um novo contrato usando este modelo, o `{{ start_date }}` é substituído pela data inserida no campo de mesmo nome.


![Modelo de contrato](/files/contract-template-jinja.gif)


### 2.6 Referências


Se o Contrato pode ser vinculado a uma transação no ERPNext. Selecione o tipo de transação e a transação específica. Os documentos que podem ser vinculados são:


* Cotação
* Projeto
* Pedido de venda
* Ordem de Compra
* Nota Fiscal de Venda
* Nota fiscal de compra


![Referências do contrato](/files/contract-reference.png)


### 3. Tópicos Relacionados


1. [Cotação](/docs/v13/user/manual/en/selling/quotation)
2. [Pedido de compra](/docs/v13/user/manual/en/buying/purchase-order)
3. [Pedido de venda](/docs/v13/user/manual/en/selling/pedido de venda)
4. [Recibo de compra](/docs/v13/user/manual/en/stock/compra-recibo)
5. [Nota de entrega](/docs/v13/user/manual/en/stock/nota de entrega)
6. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
7. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)