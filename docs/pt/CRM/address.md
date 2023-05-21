# Endereço


Você pode registrar os endereços associados a um Lead, Cliente, Fornecedor, Acionista, Parceiro de Vendas ou Armazém.


Você também pode adicionar um endereço como um registro autônomo sem vinculá-lo a nenhuma das entidades listadas acima.


Para acessar a lista de endereços, vá para:



>
> Início > CRM > Endereço
>
>
>


## 1. Como criar um Endereço


1. Vá para a lista de endereços e clique em Novo.
2. Selecione Tipo de endereço.
3. Digite os detalhes na Linha de Endereço 1, Linha de Endereço 2, Cidade/Cidade, Condado, Estado, País.
4. Digite o endereço de e-mail, telefone e fax.
5. Digite Link DocType e Link Name para vincular este endereço ao cliente, fornecedor etc.
6. Salve.
![Contato](/files/address.png)


Você também pode adicionar um endereço do registro do cliente ou fornecedor clicando no botão "Novo endereço" conforme mostrado abaixo.


![Adicionar endereço do cliente](/files/add-address-from-customer.png)


Para importar vários endereços de uma planilha, use a [Ferramenta de importação de dados](/docs/v13/user/manual/en/setting-up/data/data-import).




---


## 2. Características


### 2.1 Vincular um endereço a várias entidades


Um endereço pode estar vinculado a vários clientes ou fornecedores.


Um endereço também pode ser vinculado a clientes e fornecedores ao mesmo tempo.


![Link One Address to Multiple Entities](/files/link-address-to-multiple-entities.png)


### 2.2 Título do Endereço


Se o endereço não estiver vinculado a nenhuma entidade, você precisará adicionar um título manualmente.


Se o endereço estiver vinculado a uma entidade como um cliente ou fornecedor, o título é gerado automaticamente no formato 'Nome da Entidade-Tipo de Endereço'.


![Título do endereço](/files/address-title.png)


### 2.3 Endereço de Cobrança Preferido e Endereço de Entrega


Se você marcar 'Endereço de entrega preferencial', o endereço será adicionado automaticamente no Endereço de entrega nas transações de Pedido de venda, Fatura de venda e Nota de entrega.


Da mesma forma, se você marcar 'Endereço de cobrança preferencial', o endereço será adicionado automaticamente no Endereço de cobrança nas transações de Pedido de venda, Fatura de venda e Nota de entrega.


### 2.4 Localização GST para a Índia


Se o cliente ou fornecedor estiver registrado no GST, você pode inserir GSTIN e GST State em Address. Verifique se o GSTIN inserido está em um formato válido.
![Detalhes GST no endereço](/files/gst-details-in-address.png)


Nas transações de vendas junto com o endereço, o GSTIN também é obtido.


![Detalhes do GST no pedido de venda](/files/gst-details-in-sales-order.png)


Você também pode adicionar endereços das instalações da sua própria empresa. Marque 'Is Your Company Address', selecione Company in Link DocType e Company Name em Link Name para esses endereços e você pode selecioná-los na GST Sales Invoice para imprimir seu próprio endereço.


![Endereço da empresa](/files/company-address.png)



>
> O GSTIN deve ser adicionado em Endereço e não em Cliente/Fornecedor, pois um Cliente/Fornecedor pode ter vários GSTIN (um para cada estado onde atua).
>
>
>


### 3. Tópicos Relacionados


1. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
2. [Fornecedor](/docs/v13/user/manual/en/buying)
3. [Parceiro de vendas](/docs/v13/user/manual/en/selling)