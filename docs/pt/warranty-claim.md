# Reivindicação de garantia



**Uma reivindicação de garantia ocorre quando um cliente solicita reparos gratuitos dentro do período de garantia do item/serviço que você está fornecendo.**


Se você estiver vendendo itens sob garantia ou se tiver vendido e estendido um contrato de serviço, como o Contrato de Manutenção Anual (AMC), seu Cliente poderá entrar em contato com você sobre um problema ou avaria do produto e fornecer-lhe o Número de Série deste item.


Para acessar a lista de solicitações de garantia, acesse:



> 
> Página inicial > Suporte > Garantia > Reivindicação de garantia
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar a reivindicação de garantia, é aconselhável criar primeiro o seguinte:


* [Cliente](/docs/pt/CRM/customer)
* [Número de série](/docs/pt/stock/serial-no)
* [Item](/docs/pt/stock/item)


## 2. Como criar uma reivindicação de garantia


1. Vá para a lista de solicitações de garantia e clique em Novo.
2. Selecione um cliente.
3. Selecione o número de série do item no qual a reivindicação de garantia será registrada. O sistema irá então buscar automaticamente os detalhes do número de série e indicar se ele está na garantia ou AMC.
4. Insira uma descrição do problema. O usuário pode fazer upload de uma imagem e criar uma tabela.
5. Salvar.
![Reivindicação de garantia](/files/warranty-claim.png)


### 2.1 Opções adicionais ao criar uma reivindicação de garantia


* **Status**: Ao criar uma reivindicação de garantia, o status será definido como "Aberto". O usuário pode alterar o status para:
	+ Trabalho em andamento: consertos/reparos estão sendo feitos no item.
	+ Fechado: Os reparos foram feitos e a reivindicação de garantia está encerrada.
	+ Cancelado: a reivindicação de garantia era inválida e a reivindicação foi encerrada.
* **Data de emissão**: Ao criar a reivindicação de garantia, a data atual será capturada. Este campo é editável.


## 3 recursos


### 3.1 Detalhes do item e da garantia:


Depois que um Número de Série for selecionado, os seguintes detalhes sobre o Item serão obtidos:


* Código do item
* Nome do item
* Descrição do item


Os detalhes sobre Garantia/AMC serão obtidos de acordo com o Número de Série.


* **Garantia/Status AMC:** As opções possíveis são "Sob garantia", "Fora de garantia", "Sob AMC" ou "Fora de AMC". O status pode ser alterado para Fora da garantia/AMC se o item tiver sido adulterado ou a garantia for anulada, dependendo dos seus termos de serviço.
* Data de expiração da garantia
* Data de expiração do AMC


![Série de garantia](/files/warranty-serial.png)


### 3.2 Resolução


* **Data de resolução:** Quando a garantia ou AMC for encerrada, a data e a hora atuais serão buscadas automaticamente no campo Data de resolução. Este campo também é editável.
* **Resolvido por:** Defina o ID de e-mail do usuário que resolveu a reclamação de garantia. O ID do e-mail está vinculado ao [Usuário](/docs/pt/setting-up/users-and-permissions/adding-users) criado no sistema.
* **Detalhes resolvidos:** Este é um campo de texto. O usuário pode inserir detalhes sobre a reclamação de garantia ou AMC. Um usuário também pode fazer upload da imagem, inserir ou criar uma tabela.


![Resolução de garantia](/files/warranty-resolution.png)


### 3.3 Detalhes do cliente


Os seguintes detalhes do [Cliente](/docs/pt/CRM/customer) serão obtidos:


* Nome do cliente
* Pessoa de contato
* Território
* Grupo de clientes
* Endereços de clientes


**Endereço do Serviço:** o usuário pode inserir o Endereço do Serviço se for diferente do Endereço do Cliente.


![Cliente de garantia](/files/warranty-customer.png)


### 3.4 Mais informações


* **Empresa:** A Garantia ou AMC criada a partir da empresa será selecionada automaticamente.
* **Levantado por:** o usuário pode inserir o nome da pessoa que levantou a garantia ou AMC caso o cliente seja uma organização.
* **Da Empresa:** o usuário pode inserir o nome da empresa da qual a garantia ou AMC foi criada.


Se for necessária uma visita ao cliente para resolver o problema, você poderá criar um novo
Registro de visita de manutenção deste.


## 4. Tópicos Relacionados


1. [Problema](/docs/pt/support/issue)
2. [Visita de manutenção](/docs/pt/support/maintenance-visit)



