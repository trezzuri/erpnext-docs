# Reivindicação de garantia


**Uma reivindicação de garantia é quando um cliente solicita reparos gratuitos dentro do período de garantia do item/serviço que você está fornecendo.**


Se você estiver vendendo itens sob garantia ou se você vendeu e estendeu o contrato de serviço como o Contrato de manutenção anual (AMC), seu cliente pode entrar em contato com você sobre um problema ou quebra do produto e fornecer o número de série deste item .


Para acessar a lista de reclamações de garantia, vá para:



>
> Início > Suporte > Garantia > Reivindicação de garantia
>
>
>


## 1. Pré-requisitos


Antes de criar e usar a Reivindicação de Garantia, é recomendável criar primeiro o seguinte:


* [Cliente](/docs/v13/user/manual/en/CRM/cliente)
* [Número de série](/docs/v13/user/manual/en/stock/serial-no)
* [Item](/docs/v13/user/manual/en/stock/item)


## 2. Como criar uma reivindicação de garantia


1. Vá para a lista Reivindicação de garantia, clique em Novo.
2. Selecione um cliente.
3. Selecione o número de série do item no qual a solicitação de garantia deve ser registrada. O sistema buscará automaticamente os detalhes do número de série e indicará se está na garantia ou no AMC.
4. Insira uma descrição do problema. O usuário pode fazer upload e imagem e criar uma tabela.
5. Salve.
![Reivindicação de garantia](/files/warranty-claim.png)


### 2.1 Opções adicionais ao criar uma reivindicação de garantia


* **Status**: Ao criar uma reivindicação de garantia, o status será definido como "Aberto". O usuário pode alterar o status para:
+ Trabalho em andamento: Correções/reparos estão sendo feitos no item.
+ Fechado: As reparações foram efectuadas e o Pedido de Garantia está encerrado.
+ Cancelado: A reclamação de garantia era inválida e a reclamação foi encerrada.
* **Data de Emissão**: Ao criar a Reivindicação de Garantia, a data atual será capturada. Este campo é editável.


## 3 Características


### 3.1 Detalhes do Item e da Garantia:


Uma vez que um número de série é selecionado, os seguintes detalhes sobre o item serão buscados:


* Código do item
* Nome do item
* Descrição do item


Os detalhes sobre Garantia/AMC serão obtidos de acordo com o Número de Série.


* **Warranty / AMC Status:** As opções possíveis são "Sob garantia", "Fora da garantia", "Sob AMC" ou "Fora da AMC". O status pode ser alterado para Fora da garantia/AMC se o item tiver sido adulterado ou se a garantia for anulada, dependendo dos seus termos de serviço.
* Data de vencimento da garantia
* Data de expiração do AMC


![Serial de garantia](/files/warranty-serial.png)


### 3.2 Resolução


* **Resolution Date:** Quando a garantia ou AMC estiver encerrada, a data e hora atuais serão buscadas no campo Data de resolução automaticamente. Este campo também é editável.
* **Resolvido por:** Defina o ID de e-mail do usuário que resolveu a reclamação de garantia. O ID do e-mail está vinculado ao [Usuário](/docs/v13/user/manual/en/setting-up/users-and-permissions/adding-users) criado no sistema.
* **Detalhes resolvidos:** Este é um campo de texto. O usuário pode inserir detalhes sobre a garantia ou reclamação AMC. Um usuário também pode fazer upload da imagem, inserir ou criar uma tabela.


![Resolução de garantia](/files/warranty-resolution.png)


### 3.3 Detalhes do Cliente


Os seguintes detalhes do [Cliente](/docs/v13/user/manual/en/CRM/cliente) serão obtidos:


* Nome do cliente
* Pessoa de contato
* Território
* Grupo de clientes
* Endereços do cliente


**Endereço do serviço:** O usuário pode inserir o Endereço do serviço se for diferente do Endereço do cliente.


![Cliente de Garantia](/files/warranty-customer.png)


### 3.4 Mais Informações


* **Empresa:** A Garantia ou AMC criada a partir da empresa será selecionada automaticamente.
* **Aumentado por:** O usuário pode inserir o Nome da pessoa que levantou a Garantia ou AMC caso o Cliente seja uma organização.
* **Da empresa:** O usuário pode inserir o nome da empresa da qual a garantia ou AMC foi criada.


Se for necessária uma visita ao cliente para resolver o problema, você pode criar uma nova
Registo de visita de manutenção a partir deste.


## 4. Tópicos Relacionados


1. [Problema](/docs/v13/user/manual/en/support/issue)
2. [Visita de manutenção](/docs/v13/user/manual/en/support/maintenance-visit)