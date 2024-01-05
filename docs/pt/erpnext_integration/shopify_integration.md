# Integração com Shopify



O Shopify Connector extrai os pedidos do Shopify e cria pedidos de vendas contra eles no ERPNext.


Ao criar o pedido de venda se o Cliente ou Item estiver faltando no ERPNext, o sistema criará um novo Cliente/Item extraindo os respectivos detalhes do Shopify.


### Como configurar o conector?


O Shopify Connector foi removido do ERPNext e está disponível por meio de um aplicativo Frappe no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)


#### Nota para usuários do antigo Shopify Connector


Se você não configurou o Shopify Connector em seu site ERPNext, você pode prosseguir para a próxima etapa.


Se você estiver usando a integração antiga do Shopify fornecida no ERPNext, você terá que desabilitar o conector antes de continuar. Depois de instalar o aplicativo, ele migrará os dados existentes, por exemplo. product\_id exclusivo para itens para separar o tipo de documento. Depois de configurar a nova integração, você poderá confirmar o status da migração acessando o tipo de documento "Registro de integração de comércio eletrônico".


#### Instalação de aplicativo


* Se você estiver hospedando seu site ERPNext no Frappe Cloud, você pode instalar o aplicativo rapidamente acessando o Painel do seu site. O aplicativo está disponível no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
* Se o seu site for hospedado pela Frappe, abra um ticket de suporte para instalar o aplicativo no seu site.
* Se você hospeda o ERPNext você mesmo pode instalar o aplicativo usando o banco Frappe. Consulte a [documentação do Bench](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) para instalar o Frappe Apps. `bench get-app ecommerce_integrations--branch main`


O repositório do aplicativo está hospedado no GitHub: <http://github.com/frappe/ecommerce_integrations/>


#### Crie um aplicativo personalizado no Shopify


1. Clique em Aplicativos na barra de menu
![Seção de menu](/files/app_menu.png)
2. Clique em **Desenvolver aplicativos para sua loja** para criar um aplicativo personalizado
![new app](/files/Screenshot 16/02/2022 às 11h36.57.png)
3. Criar novo aplicativo
![](/files/new_app.png)
4. Preencha os detalhes e crie o aplicativo. Cada aplicativo tem sua própria chave de API, senha e segredo compartilhado
![](/files/configure_admin_scope.png)
5. Permitir as seguintes permissões para o aplicativo.


	* Rascunhos de pedidos-Ler e escrever
	* Pedidos-Ler e Escrever
	* Localização-Leia
	* Clientes-Leia
	* Pedidos de atendimento atribuídos-leitura e gravação
	* Produtos-Ler e Escrever
	* Listagens de produtos: ler e escrever
	* Inventário-Ler e Escreverseus escopos administrativos finais devem ficar assim:


![](/files/final_admin_scopes.png)
6. Instale o aplicativo em seu site
![](/files/install.png)


#### Configurando o Shopify no ERPNext:-


Depois de criar um aplicativo privado no Shopify, configure as credenciais do aplicativo e outros detalhes nas configurações do Shopify no ERPNext.


> Para acessar as configurações do Shopify, acesse:
Barra de pesquisa incrível > Configuração do Shopify


1. Preencha o URL do site Shopify, o token de acesso e o segredo da API do aplicativo privado do Shopify.
![](/files/tokens.png)
![](/files/Screenshot 16/02/2022 às 11h57.34.png)
2. Definir configurações de cliente, empresa e estoque.
3. ![Página de configuração do Shopify](/files/main-settings.png)
4. Definir configurações de sincronização.
O sistema extrai pedidos do Shopify e cria pedidos de vendas no ERPNext. Você pode configurar o sistema ERPNext para capturar pagamentos e atendimentos de pedidos.
![Configuração de sincronização do Shopify para pedidos](/files/series-setting.png)
5. Configurar mapeador fiscal.
Prepare um mapeador de impostos e taxas de envio para cada taxa e taxa de envio aplicada na Shopify. Você pode encontrar o nome dos seus impostos na página de administração do Shopify.
![Mapeamento fiscal do Shopify](/files/tax-mapping.png)
![Encontrando nomes fiscais do Shopify](/files/Screenshot 2021/08/25 às 11/02/20 AM.png)


Depois de definir todas as configurações, ative a sincronização do Shopify e salve as configurações. Isso registrará as APIs no Shopify e o sistema iniciará a sincronização do pedido entre o Shopify e o ERPNext.


### Sincronizar pedidos antigos do Shopify


Depois de concluir a configuração do Shopify e ativar o Shopify Syncing, você também terá a possibilidade de sincronizar seus pedidos antigos do Shopify com o ERPNext. Essa sincronização acontecerá em segundo plano e poderá levar algumas horas, dependendo do número de pedidos que você tiver.


1. Ative "Sincronizar pedidos antigos do Shopify"
2. Insira as datas inicial e final entre as quais os pedidos precisam ser sincronizados
![shopify sincronizar pedidos antigos](/files/sync-old-orders.png)


### Sincronização de inventário


Você pode atualizar seu inventário com a Shopify para itens sincronizados da Shopify. A sincronização do inventário é feita a cada hora com um trabalho agendado. Os níveis de estoque de itens que foram alterados desde a última sincronização são enviados para o Shopify. Os níveis de estoque dos armazéns ERPNext são mapeados 1 para 1 com os locais do Shopify.


1. Para ativar a sincronização de inventário, clique na caixa de seleção, isso mostrará uma tabela para mapear o armazém ERPNext com o Shopify Location.
2. Selecione a frequência de sincronização. A frequência recomendada é de 30 a 60 minutos.
3. Clique no botão "Buscar locais do Shopify" para preencher os locais do Shopify na tabela.
4. Vincule cada local ao armazém ERPNext.
5. Salve as configurações.


![Sincronização de estoque com shopify](/files/inventory-sync.png)


> Nota: Este conector assume que o ERPNext é a principal fonte de informações sobre os níveis de estoque. Quaisquer alterações feitas nos níveis de estoque do Shopify serão substituídas pelo ERPNext se os níveis de estoque do ERPNext mudarem.


> Observação: Shopify não oferece suporte a quantidade fracionada. Se a quantidade fracionária for encontrada no ERPNext, o nível de estoque no Shopify será definido arredondando-o para o número inteiro mais próximo.


### Sincronização de itens


Você pode ativar a sincronização de novos itens do ERPNext para o Shopify marcando "Carregar novos itens do ERPNext para o Shopify".


Você também pode atualizar o item do Shopify ao atualizar o item do ERPNext.


Os seguintes campos são carregados/atualizados:




| ERPNext Field | Campo Shopify |
| --- | --- |

| Nome do item | Título |

| Código do item | SKU |

| Corpo da descrição | Descrição |

| Grupo de itens | Tipo de produto |

| Peso por unidade | Peso |

| UOM de peso | UOM de peso |



Por padrão, todos os itens são marcados como Rascunho na Shopify e não publicados em nenhuma loja.


O objetivo de fornecer essa funcionalidade é sincronizar itens com o Shopify. Não é possível mapear todos os campos 1 para 1. Ao criar um item no Shopify através deste método, ele é vinculado ao ERPNext, eliminando a possibilidade de duplicação. Você pode modificar itens na Shopify posteriormente para adicionar mais detalhes.


> Observação: esse recurso não é compatível com importação de dados ou itens de variante/modelo.


### Cancelamento de pedidos


Este conector lida com vários cenários de cancelamento da seguinte maneira:


1. Se o pedido no Shopify for cancelado e não tiver fatura ou nota de entrega vinculada a ele, o pedido de vendas do ERPNext será cancelado.
2. Se o Pedido de Vendas do ERPNext tiver algum documento vinculado, então o status do pedido no Shopify é adicionado ao respectivo documento. O cancelamento e a preparação dos documentos apropriados devem ser feitos pelo usuário com base nessas informações.




