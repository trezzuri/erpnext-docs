# Integração WooCommerce




> Descontinuado na versão 15
> 
> 

Usando a integração WooCommerce, o sistema cria pedidos de vendas no ERPNext para os pedidos criados no WooCommerce usando o webhook WooCommerce.

 Ao criar um Pedido de Venda do WooCommerce, se o Cliente ou Item estiver faltando no ERPNext, o sistema criará um novo Cliente/Item usando os respectivos detalhes dos dados do pedido do WooCommerce. Também cria um Endereço vinculado ao Cliente usando os detalhes de envio dos dados do pedido.

## 1. Como configurar o WooCommerce?

### 1.1 Gerar chave de API e segredo de API

1. Na barra lateral do seu site WooCommerce, clique em Configurações.
2. Clique na guia "Avançado" e depois clique no link REST API.

![Woocommerce API](/files/wc-add-key.png)![]()

- Clique no botão "Adicionar chave". Forneça os detalhes necessários e clique no botão "Gerar chave de API".

![Woocommerce API Key](/files/wc-generate-keys.png)![]()

### 1.2 Configurações do Woocommerce

1. No seu site ERPNext, vá para: **Home > Integrações > Configurações > Configurações do Woocommerce**.
2. Cole a chave e o segredo da API gerados na etapa anterior nos campos "Chave do consumidor da API" e "Segredo do consumidor da API".
3. No campo "Woocommerce" URL do servidor" cole o URL do seu site WooCommerce.
4. Certifique-se de que "Ativar sincronização" esteja marcado.
5. Selecione o "Conta fiscal" e "Conta de frete e encaminhamento" na seção Detalhes da conta.
6. Selecione "Usuário de criação" na seção Padrões. Este usuário será utilizado para criar Clientes, Itens e Pedidos de Venda. Certifique-se de que o usuário tenha as permissões relevantes.
7. Selecione a "Empresa" que será usada para criar os Pedidos de Vendas.
8. Clique em Salvar.
9. Após salvar as configurações do Woocommerce, "Secret" e "Endpoint" são gerados automaticamente.

![Configurações de Woocommerce](/files/woocommerce-settings.png)![]()  


### 1.3 Configurações do Woocommerce Webhook

1. Agora, na barra lateral do seu site woocommerce, vá para Configurações.
2. Clique na guia "Avançado", clique no link Webhooks e depois clique no botão "Adicionar webhook".
3. Dê ao webhook um nome de sua preferência.
4. Clique no menu suspenso Status e selecione "Ativo".
5. Selecione o tópico como "Pedido criado".
6. Copie o tipo de documento "Endpoint" do tipo de documento "Configurações do Woocommerce" no seu site ERPNext e cole-o no campo "URL de entrega".
7. Copie "Secret" do tipo de documento "Woocommerce Settings" em seu site ERPNext e cole-o no campo "Secret".
8. Mantenha API VERSION como está é e clique em Salvar Webhook. Agora ele foi configurado com sucesso.

![Woocommerce Webhook](/files/wc-webhook.png)![]()  


Um GIF abaixo para mostrar todo o processo :

![Configuração do Woocommerce](/files/woocommerce-setup.gif)![]()  



> **Nota:** Na captura de tela acima e no GIF, no lugar da url de entrega no site woocommerce, você precisa colar a url que obterá após salvar as "Configurações do Woocommerce" no campo "Endpoint" da sua instância do ERPNext. Aqui outro URL foi colado enquanto localhost estava sendo usado.
> 
> 

### 1.4 Criação e sincronização de pedidos Woocommerce

1. No seu site Woocommerce, registre-se como um usuário na página Conta.
2. Agora clique na opção Endereços e forneça os detalhes necessários.
3. Clique em "Comprar" opção e os produtos disponíveis agora podem ser vistos.
4. Adicione os produtos desejados ao carrinho e clique em **Ver carrinho**.
5. No carrinho, depois de adicionar os produtos desejados, você pode clicar em "Prosseguir para Finalização da Compra".
6. Todos os detalhes de cobrança e detalhes do pedido podem ser visto agora. Quando estiver tudo bem, clique no botão **Fazer pedido**.
7. A mensagem "Pedido recebido" pode ser vista indicando que o pedido foi feito com sucesso .
8. Agora em sua instância do ERPNext, verifique os seguintes tipos de documentos: Cliente, Endereço, Item, Pedido de Venda. Eles serão buscados e criados a partir dos dados do webhook.
9. Caso os pedidos não estejam sincronizados, você pode verificar o erro em **Home > Configurações > Core > Log de Erros** .

![Configuração do Woocommerce](/files/woocommerce-order.gif)![]()  


## 2. Recursos

### 2.1 Padrões

Nas configurações do Woocommerce DocType:

* **Armazém**: Este armazém será usado para criar pedidos de vendas. O Armazém padrão é "Lojas".
* **Entrega Após (Dias)**: Este é o deslocamento padrão (dias) para a Data de Entrega em Pedidos de Vendas . O deslocamento padrão é de 7 dias a partir da data de colocação do pedido.
* **Série de pedidos de vendas**: você pode definir uma série separada para pedidos de vendas criados via woocommerce. A série padrão é "SO-WOO-".
* **UOM**: Esta é a UOM padrão usada para Itens e Pedidos de Vendas. A UOM padrão é "Nos".

![Woocommerce Defaults](/files/wc-defaults.png)![]()  


## 3. Tópicos relacionados

1. [Pedido de vendas](/docs/pt/selling/sales-order)
2. [Item](/docs/pt/stock/item)
3. [Cliente](/docs/pt/CRM/customer)
4. [Endereço](/docs/pt/CRM/address)


