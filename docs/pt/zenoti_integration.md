# Integração Zenoti




> 
> Introduzido na versão 13.
> 
> 
> 


A integração Zenoti extrai os pedidos de compra e faturas de vendas do Zenoti e cria pedidos de compra e faturas de vendas contra eles no ERPNext.


Ao criar esses registros se o Cliente, Fornecedor ou Item estiver faltando no ERPNext, o sistema criará um novo Cliente, Fornecedor ou Item puxando os respectivos detalhes do Zenoti.


### Como configurar?


A integração Zenoti está disponível por meio de *Integrações de comércio eletrônico* no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).


### Instalação de aplicativo


* Se você estiver hospedando seu site ERPNext no Frappe Cloud, você pode instalar o aplicativo rapidamente acessando o Painel do seu site. O aplicativo está disponível no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).
* Se o seu site for hospedado pela Frappe, abra um ticket de suporte para instalar o aplicativo no seu site.
* Se você hospeda o ERPNext você mesmo pode instalar o aplicativo usando o banco Frappe. Consulte a [documentação do Bench](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) para instalar o Frappe Apps. `bench get-app ecommerce_integrations--branch main`


O repositório do aplicativo está hospedado no GitHub: <http://github.com/frappe/ecommerce_integrations/>.
### Pré-requisito


1. Para cada centro no Zenoti deverá haver um centro de custo e um armazém criado no ERPNext que será utilizado na tabela Centro de Custo e Mapeamento de Armazém nas Configurações do Zenoti no ERPNext.
2. Itens*(pelo menos aqueles que têm impacto no estoque)* devem ser criados. A importação de dados pode ser usada para isso.
3. As entradas de estoque iniciais devem ser criadas usando a Reconciliação de Estoque no ERPNext.
4. Os modelos de impostos de itens devem ser criados a partir de grupos de impostos no Zenoti com contas e taxas de impostos adequadas.
5. Crie uma conta para contabilizar a responsabilidade pelas vendas de cartões-presente ou pré-pagos e gorjetas. Ela deve ser definida como *Conta de renda de responsabilidade para reservar cartões-presente e pré-pagos* nas configurações do Zenoti.
6. Estabeleça contas apropriadas no modo de pagamento. Adicione também "Cartão", "Personalizado" e "Pontos" como forma de pagamento.
7. "Ativar inventário permanente" deve estar desmarcado no mestre da empresa.


### Detalhes importantes para configurar o Zenoti no ERPNext



> 
> Para acessar as configurações do Zenoti, vá para: Barra de pesquisa incrível > Configurações do Zenoti.
> 
> 
> 


![Página de configuração do Zenoti](/files/Zenoti Settings Screen.png)


1. **Última sincronização:** data e hora da última sincronização das faturas.
2. **Chave de API:** Chave de API do Zenoti. Se você não tiver uma chave de API, poderá gerá-la facilmente acessando a seção Admin > Configuração > API.
3. **Intervalo de sincronização:** duração em horas entre cada sincronização. As seguintes opções estão disponíveis *(1, 3, 6, 12, 24)*
4. **Armazém de Compra Padrão:** Armazém a ser definido para todos os Pedidos de Compra. Normalmente este é o centro principal em Zenoti, então coloque aquele que você criou como centro principal.
5. **Lista de Preços de Compra Padrão:** Isto é necessário no ERPNext para manter o preço dos Itens. Você pode criar um novo ou usar o existente *Compra Padrão* fornecido pelo ERPNext.
6. **Lista de Preços de Venda Padrão:** Isto é necessário no ERPNext para manter o preço dos Itens. Você pode criar um novo ou usar o existente *Venda Padrão* fornecido pelo ERPNext.
7. **Conta de renda passiva para reserva de gorjetas, cartões-presente e pré-pagos:** Adicione aqui a conta que você criou para reservar gorjetas e vendas de cartões-presente e pré-pagos.
8. **Grupo de clientes padrão:** se, na criação de um novo cliente durante a sincronização da fatura de vendas, um grupo de clientes específico for atribuído a eles, adicione-o aqui. Se nada for adicionado, o padrão *Todos os grupos de clientes* será definido para esses novos clientes.
9. **Grupo de fornecedores padrão:** se na criação de um novo fornecedor durante a sincronização do pedido de compra um grupo de fornecedores específico for atribuído a eles, adicione-o aqui. Se nada for adicionado, o padrão *Todos os grupos de fornecedores* será definido para esses novos fornecedores.
10. **Mapeamento de Centros de Custo e Armazéns:** Nesta tabela mapeie todos os Centros de Zenoti para seus Centros de Custo e Armazéns correspondentes no ERPNext.


### O que será sincronizado ou terá que ser criado manualmente


#### Item


Os itens terão que ser criados manualmente no ERPNext a partir do Zenoti uma vez no início. Em seguida, ele será criado com base na demanda ao sincronizar pedidos de vendas/compra.


#### Modelo de imposto de item


O modelo de imposto do item será criado manualmente com base nos grupos de impostos do zenoti.


#### Cliente


O cliente e o grupo de clientes serão criados sob demanda durante a sincronização das faturas de vendas. Se não houver grupos de clientes no Zenoti, será usado o “Grupo de clientes padrão” mencionado nas configurações do Zenoti. Se não for mencionado nas configurações do Zenoti, “Todos os grupos de clientes” será usado.


#### Fornecedor


O fornecedor e o grupo de fornecedores serão criados conforme a demanda durante a sincronização dos pedidos de compra. Se não houver grupos de fornecedores no Zenoti, será usado o “Grupo de fornecedores padrão” mencionado nas configurações do Zenoti. Se não for mencionado nas configurações do Zenoti, “Todos os grupos de fornecedores” será usado.


#### Armazém


Os Armazéns deverão ser criados no ERPNext manualmente e mapeados com os Centros do Zenoti via Centro de Custo e Tabela de Mapeamento de Armazéns nas Configurações do Zenoti.


#### Centro de Custo


Os Centros de Custo deverão ser criados no ERPNext manualmente e mapeados com os Centros do Zenoti via Centro de Custo e Tabela de Mapeamento de Armazém nas Configurações do Zenoti.


#### Funcionários


Os funcionários terão que ser criados manualmente no ERPNext a partir do Zenoti uma vez no início. Em seguida, ele pode ser criado com base na demanda ao sincronizar registros de vendas/compras. Para Colaboradores os campos “Data de Nascimento”, “Data de Ingresso” são obrigatórios. Portanto, ao criar um funcionário a partir de registros de vendas/compras, a "Data de adesão" será definida como o dia em que o funcionário foi criado e a "Data de nascimento" como 25 anos antes da "Data de adesão". Eles podem ser alterados posteriormente.


#### Pedido de compra


O pedido de compra será criado no Zenoti e sincronizado no ERPNext no final do dia.
Fornecedor e Item serão criados sob demanda, se novos.



> 
> Observação: a fatura de compra do pedido de compra deve ser criada manualmente.
> 
> 
> 


#### Nota de Débito


A nota de débito será criada automaticamente e permanecerá no modo Rascunho com base na ordem de compra de devolução no Zenoti.


#### Fatura de vendas


A fatura será criada automaticamente via API no intervalo determinado definido nas configurações do Zenoti.
O Cliente e o Item serão criados sob demanda, se novos.


#### Nota de crédito


A Nota de Crédito será criada automaticamente com base na Fatura de Devolução no Zenoti e conterá apenas produtos e não serviços.


#### Vendas de cartões-presente/pré-pagos


Cada cartão presente/pré-pago será tratado como item.
Cartões-presente/pré-pagos serão tratados como forma de pagamento para faturas futuras onde o pagamento for feito usando-os no Zenoti.


#### Reconciliação de estoque


No final do dia, o estoque será sincronizado por meio da Reconciliação de estoque.





