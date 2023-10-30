# Integração Amazon SP-API



O Amazon Connector extrai produtos e pedidos de vendas do mercado Amazon.

## Como configurar o Amazon SP-API Connector?

O Amazon Connector foi removido do ERPNext e está disponível por meio de um aplicativo Frappe no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)

 ### Instalação do aplicativo

* Se você estiver hospedando seu site ERPNext no Frappe Cloud, você pode instalar o aplicativo rapidamente acessando o painel do seu site. O aplicativo está disponível no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
* Se o seu site for hospedado pela Frappe, abra um ticket de suporte para instalar o aplicativo em seu site.
* Se você for auto-hospedado ERPNext você pode instalar o aplicativo usando o banco Frappe. Consulte a [documentação do Bench](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) para instalar aplicativos Frappe. `bench get-app ecommerce_integrations--branch main`

O repositório do aplicativo está hospedado no GitHub: <http://github.com/frappe/ecommerce_integrations/>

### Configurando credenciais no ERPNext

Você pode solicitar as credenciais de desenvolvedor do Amazon Seller Central assim que for um vendedor registrado no site deles. Para obter mais detalhes sobre o mesmo, clique [aqui](https://developer.amazonservices.com/).

####  1. Configure credenciais SP-API

Insira o ARN do IAM, o token de atualização, o ID do cliente, o segredo do cliente, a chave de acesso da AWS, a chave secreta da AWS e o país. ![Credentials](/files/Credentials.png "Credentials.png")  
  
 

#### 2. Configurar detalhes do pedido

Configurar empresa, armazém, grupo de itens pai, lista de preços, grupo de clientes, território, tipo de cliente e grupo de contas. O Grupo de Contas é usado para armazenar comissões, impostos, etc. que a Amazon cobra. ![setup](/files/Screenshot from 2023-07-31 13-51-36.png "setup.png")  
  


#### 3. Definir configurações de sincronização

Usando a data posterior, você pode sincronizar pedidos criados após uma data específica. Caso você esteja importando muitos dados históricos, sugere-se iniciar na ordem cronológica inversa da data posterior e importar os dados em pequenos pedaços. ![Syncing](/files/Screenshot from 2023-07-31 13-45-15.png "Syncing.png")Após a configuração todas as configurações, clique em Está Ativo e salve as configurações. Agora você está pronto para usar a integração.

#### 4. Amazon-Mapeamento de itens ERPNext

Tanto ASIN quanto SellerSKU podem ser utilizados para mapear itens Amazon com itens ERPNext correspondentes. Por exemplo, se você tiver itens pré-existentes em seu sistema, criados por meio de outras integrações, poderá estabelecer um campo personalizado no Cadastro de Itens usando o recurso Personalizar Formulário e definindo o ASIN/SellerSKU como o valor.

Durante o processo de sincronização de pedidos da Amazon, o sistema tentará encontrar o Código do Item utilizando o campo configurado para encontrar o Código do Item na tabela Amazon-Mapeamento de Item ERPNext. Se o item não for encontrado na tabela de mapeamento, você terá a opção de criar um novo item marcando a caixa **Criar item se não existir**.

![Screenshot de 31/07/2023 13-52-50](/files/Screenshot de 31/07/2023 13-52-50.png "Screenshot de 2023-07-31 13-52-50.png")![]()  


#### 5. Sincronizar pedidos

Clique neste botão para sincronizar pedidos de vendas. Assim que isso for bem-sucedido, você deverá ver seus pedidos da Amazon como pedidos de vendas no ERPNext. Você também pode configurar um agendador para sincronizar pedidos automaticamente.


> Caso sua conta de desenvolvedor não tenha acesso a informações de identificação pessoal. O nome do cliente seria armazenado como uma combinação de BuyerName +  ou ID de e-mail do Marketplace.
> 
> 

![Pedido de venda](/files/Sales Order.png "Sales Order.png")  
  


### Nota

O conector não suporta o cancelamento do pedido. Se você cancelar qualquer pedido na Amazon, então manualmente você terá que cancelar o respectivo Pedido de Venda e outros documentos no ERPNext.



