# Reivindicação de garantia


**Uma reivindicação de garantia é quando um cliente solicita reparos gratuitos dentro do período de garantia do item/serviço que você está fornecendo.**


Se você estiver vendendo itens sob garantia ou se tiver vendido e estendido o contrato de serviço, como o Contrato de manutenção anual (AMC), seu cliente poderá entrar em contato com você sobre um problema ou avaria do produto e fornecer o número de série deste item.


Para acessar a lista de reclamações de garantia, vá para:



> 
> Página inicial > Suporte > Garantia > Reivindicação de garantia
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar a Reivindicação de Garantia, é recomendável criar primeiro o seguinte:


* [Cliente](/docs/pt/CRM/customer)
* [Número de série](/docs/pt/stock/serial-no)
* [Item](/docs/pt/stock/item)


## 2. Como criar uma reivindicação de garantia


1. Vá para a lista Reivindicação de garantia, clique em Novo.
2. Selecione um cliente.
3. Selecione o número de série do item no qual a reivindicação de garantia deve ser registrada. O sistema buscará automaticamente os detalhes do número de série e indicará se está na garantia ou AMC.
4. Insira uma descrição do problema. O usuário pode enviar uma imagem e criar uma tabela.
5. Salvar.
![Reivindicação de garantia](/files/warranty-claim.png)


### 2.1 Opções adicionais ao criar uma reivindicação de garantia


* **Status**: ao criar uma reivindicação de garantia, o status será definido como "Aberto". O usuário pode alterar o status para:
	+ Trabalho em andamento: consertos/reparos estão sendo feitos no item.
	+ Fechado: os reparos foram feitos e a reclamação de garantia está encerrada.
	+ Cancelada: a reivindicação de garantia era inválida e a reivindicação foi encerrada.
* **Data de emissão**: ao criar a reivindicação de garantia, a data atual será capturada. Este campo é editável.


## 3 recursos


### 3.1 Detalhes do item e da garantia:


Assim que um número de série for selecionado, os seguintes detalhes sobre o item serão obtidos:


* Código do item
* Nome do item
* Descrição do item


Os detalhes sobre Garantia/AMC serão obtidos de acordo com o Número de Série.


* **Garantia / Status AMC:** As opções possíveis são "Sob garantia", "Fora da garantia", "Sob AMC" ou "Fora da AMC". O status pode ser alterado para Fora da garantia/AMC se o item tiver sido adulterado ou se a garantia for anulada, dependendo dos seus termos de serviço.
* Data de vencimento da garantia
* Data de validade do AMC


![Warranty Serial](/files/warranty-serial.png)


### 3.2 Resolução


* **Data da resolução:** quando a garantia ou o AMC for encerrado, a data e hora atuais serão buscadas no campo Data da resolução automaticamente. Este campo também é editável.
* **Resolvido por:** Defina o ID de e-mail do usuário que resolveu a reclamação de garantia. O ID do e-mail está vinculado ao [Usuário](/docs/pt/setting-up/users-and-permissions/adding-users) criado no sistema.
* **Detalhes resolvidos:** Este é um campo de texto. O usuário pode inserir detalhes sobre a garantia ou reclamação AMC. Um usuário também pode fazer upload da imagem, inserir ou criar uma tabela.


![Resolução da garantia](/files/warranty-resolution.png)


### 3.3 Detalhes do cliente


Os seguintes detalhes do [Cliente](/docs/pt/CRM/customer) serão obtidos:


* Nome do cliente
* Pessoa de contato
* Território
* Grupo de clientes
* Endereços do cliente


**Endereço do serviço:** o usuário pode inserir o endereço do serviço se for diferente do endereço do cliente.


![Cliente de garantia](/files/warranty-customer.png)


### 3.4 Mais informações


* **Empresa:** a Garantia ou AMC criada a partir da empresa será selecionada automaticamente.
* **Aumentado por:** O usuário pode inserir o Nome da pessoa que levantou a Garantia ou AMC caso o Cliente seja uma organização.
* **Da empresa:** o usuário pode inserir o nome da empresa da qual a garantia ou AMC foi criada.


Se for necessária uma visita ao cliente para resolver o problema, você pode criar uma nova
Registro de visita de manutenção a partir disso.


## 4. Tópicos Relacionados


1. [Problema](/docs/pt/support/issue)
2. [Visita de manutenção](/docs/pt/support/maintenance-visit)
