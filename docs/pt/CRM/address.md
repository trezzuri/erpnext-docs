# Endereço


Você pode registrar os endereços associados a um lead, cliente, fornecedor, acionista, parceiro de vendas ou depósito.


Você também pode adicionar um endereço como um registro autônomo sem vinculá-lo a nenhuma das entidades listadas acima.


Para acessar a lista de endereços, vá para:



> 
> Página inicial > CRM > Endereço
> 
> 
> 


## 1. Como criar um endereço


1. Vá para a lista de endereços e clique em Novo.
2. Selecione o tipo de endereço.
3. Insira os detalhes na Linha de Endereço 1, Linha de Endereço 2, Cidade/Cidade, Condado, Estado, País.
4. Insira o endereço de e-mail, telefone e fax.
5. Insira Link DocType e Link Name para vincular este endereço ao cliente, fornecedor etc.
6. Salvar.
![Contact](/files/address.png)


Você também pode adicionar um endereço do registro do cliente ou fornecedor clicando no botão "Novo endereço" conforme mostrado abaixo.


![Adicionar endereço do cliente](/files/add-address-from-customer.png)


Para importar vários endereços de uma planilha, use a [Ferramenta de importação de dados](/docs/pt/setting-up/data/data-import).




---


## 2. Recursos


### 2.1 Vincular um endereço a várias entidades


Um endereço pode estar vinculado a vários clientes ou fornecedores.


Um endereço também pode ser vinculado a clientes e fornecedores ao mesmo tempo.


![Link One Address to Multiple Entities](/files/link-address-to-multiple-entities.png)


### 2.2 Título do endereço


Se o endereço não estiver vinculado a nenhuma entidade, você precisará adicionar um título manualmente.


Se o endereço estiver vinculado a uma entidade como um cliente ou fornecedor, o título é gerado automaticamente no formato 'Nome da entidade-tipo de endereço'.


![Address Title](/files/address-title.png)


### 2.3 Endereço de cobrança e endereço de entrega preferido


Se você marcar 'Endereço de entrega preferencial', o endereço será adicionado automaticamente no Endereço de entrega nas transações de Pedido de venda, Fatura de venda e Nota de entrega.


Da mesma forma, se você marcar 'Endereço de cobrança preferencial', o endereço será adicionado automaticamente no Endereço de cobrança nas transações de Pedido de venda, Fatura de venda e Nota de entrega.


### 2.4 Localização GST para a Índia


Se o cliente ou fornecedor estiver registrado em GST, você pode inserir GSTIN e Estado GST em Endereço. Verifique se o GSTIN inserido está em um formato válido.
![Detalhes GST no endereço](/files/gst-details-in-address.png)


Nas transações de vendas junto com o endereço, o GSTIN também é obtido.


![Detalhes do GST no pedido de vendas](/files/gst-details-in-sales-order.png)


Você também pode adicionar os endereços das instalações da sua empresa. Marque 'Is Your Company Address', selecione Company in Link DocType e Company Name em Link Name para tais endereços e você pode selecioná-los na GST Sales Invoice para imprimir seu próprio endereço.


![Endereço da empresa](/files/company-address.png)



> 
> O GSTIN deve ser adicionado no Endereço e não no Cliente/Fornecedor, pois um Cliente/Fornecedor pode ter vários GSTIN (um para cada estado onde ele conduz seus negócios).
> 
> 
> 


### 3. Tópicos Relacionados


1. [Cliente](/docs/pt/CRM/customer)
2. [Fornecedor](/docs/pt/buying)
3. [Parceiro de vendas](/docs/pt/selling)


