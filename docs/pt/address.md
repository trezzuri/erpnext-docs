# Endereço



Você pode registrar os endereços associados a um Lead, Cliente, Fornecedor, Acionista, Parceiro de Vendas ou Armazém.


Você também pode adicionar um endereço como um registro independente sem vinculá-lo a nenhuma das entidades listadas acima.


Para acessar a lista de endereços, vá para:



> 
> Página inicial > CRM > Endereço
> 
> 
> 


## 1. Como criar um endereço


1. Vá para a lista de endereços e clique em Novo.
2. Selecione o tipo de endereço.
3. Insira os detalhes na linha de endereço 1, linha de endereço 2, cidade/município, condado, estado, país.
4. Insira o endereço de e-mail, telefone e fax.
5. Insira Link DocType e Link Name para vincular este endereço ao cliente, fornecedor etc.
6. Salvar.
![Contato](/files/address.png)


Você também pode adicionar um endereço do registro de cliente ou fornecedor clicando no botão “Novo endereço”, conforme mostrado abaixo.


![Adicionar endereço do cliente](/files/add-address-from-customer.png)


Para importar vários endereços de uma planilha, use a [Ferramenta de importação de dados](/docs/pt/setting-up/data/data-import).

## 2. Recursos


### 2.1 Vincular um endereço a múltiplas entidades


Um endereço pode estar vinculado a vários clientes ou fornecedores.


Um endereço também pode ser vinculado a clientes e fornecedores ao mesmo tempo.


![Vincular um endereço a várias entidades](/files/link-address-to-multiple-entities.png)


### 2.2 Título do endereço


Se o endereço não estiver vinculado a nenhuma entidade, você precisará adicionar um título manualmente.


Se o endereço estiver vinculado a uma entidade como um cliente ou fornecedor, o título será gerado automaticamente no formato 'Nome da entidade-Tipo de endereço'.


![Address Title](/files/address-title.png)


### 2.3 Endereço de cobrança preferencial e endereço de entrega


Se você marcar 'Endereço de entrega preferencial', o endereço será adicionado automaticamente no endereço de entrega nas transações de pedido de venda, fatura de venda e nota de entrega.


Da mesma forma, se você marcar 'Endereço de cobrança preferencial', o endereço será adicionado automaticamente no endereço de cobrança nas transações de pedido de venda, fatura de venda e nota de entrega.


### 2.4 Localização GST para a Índia


Se o cliente ou fornecedor estiver registrado no GST, você poderá inserir GSTIN e Estado do GST em Endereço. Certifique-se de que o GSTIN inserido esteja em um formato válido.
![Detalhes GST no endereço](/files/gst-details-in-address.png)


Em transações de vendas junto com o endereço, o GSTIN também é buscado.


![Detalhes do GST no pedido de vendas](/files/gst-details-in-sales-order.png)


Você também pode adicionar endereços das instalações da sua própria empresa. Marque 'É o endereço da sua empresa', selecione Empresa no Link DocType e Nome da empresa no Nome do link para esses endereços e você pode selecioná-los na fatura de vendas GST para imprimir seu próprio endereço.


![Endereço da empresa](/files/company-address.png)



> 
> GSTIN deve ser adicionado em Endereço e não em Cliente/Fornecedor, pois um Cliente/Fornecedor pode ter vários GSTIN (um para cada estado onde conduz seus negócios).
> 
> 
> 


### 3. Tópicos Relacionados


1. [Cliente](/docs/pt/CRM/customer)
2. [Fornecedor](/docs/pt/buying)
3. [Parceiro de vendas](/docs/pt/selling)





