# Envio



**Uma Remessa é um documento que rastreia Remessas reais criadas em uma Nota de Entrega ou de forma independente.**


> Introduzido na versão 13


As remessas são particularmente úteis para remetentes que desejam rastrear todas as informações da remessa, como número AWB, status da remessa, transportadora, etc. dentro do ERPNext.


Para acessar a lista de Remessas, acesse:
> Home > Estoque > Transações de estoque > Remessa


## 1. Pré-requisitos


Antes de criar e usar uma Remessa, é aconselhável que você crie primeiro o seguinte:


* Empresa e cliente [Endereço](/docs/pt/CRM/address) com código postal, endereço de e-mail e número de telefone definidos.
* Cliente [Contato](/docs/pt/CRM/contact).


## 2. Como criar uma remessa


Uma Remessa pode ser criada manualmente ou a partir de uma Nota de Entrega:


### 2.1. Envio Manual


Para criar uma Remessa manualmente, siga estas etapas:


1. Vá para a lista de Remessas e clique em Novo.


![Remessa não salva](/files/unsaved-shipment.png)
2. Selecione uma opção no campo **Retirar em**. Ao selecionar uma das três opções, você será solicitado a selecionar uma Empresa/Fornecedor/Cliente com base em sua seleção.
3. Se você selecionar 'Empresa' no campo **Retirada em**, juntamente com o Endereço, você também deverá selecionar uma **Pessoa de contato para coleta** que será um usuário da sua organização, no ERPNext. Certifique-se de que o sobrenome, o endereço de e-mail e o número de telefone estejam definidos para este usuário.
4. Você também pode preencher a seção **Entrega para**.
5. Adicione informações do pacote de remessa na tabela **Pacote de remessa**.
6. Preencha o valor das mercadorias.
7. Selecione uma data de retirada.
8. Adicione uma descrição do conteúdo desta remessa.
9. Opcionalmente, você pode preencher a seção Informações da Remessa se estiver rastreando as Remessas manualmente.
10. Salvar e enviar.


![Remessa enviada](/files/shipment-submitted.png)


### 2.1. Remessa da Nota de Entrega


Para criar uma remessa a partir de uma nota de entrega:


1. Clique em **Criar** > **Envio** na Nota de Entrega.


![Remessa enviada](/files/shipment-from-delivery-note.png)
2. Preencha o formulário conforme mencionado na seção anterior.


## 3. Recursos


### 3.1. Envio de encomenda


Você pode especificar o comprimento, largura, altura e peso de um pacote na Remessa. Se houver vários lotes com dimensões idênticas, o campo **contagem** poderá ser definido de acordo.


Para buscar automaticamente dimensões de lote usadas com frequência, um modelo de lote pode ser criado e definido no campo **Modelo de lote**. Após adicionar o modelo, clique no botão **Adicionar modelo**.


![Remessa enviada](/files/shipment-parcel.png)


### 3.2. Informações/Detalhes da Remessa


A seção Informações da Remessa é uma seção **opcional** onde um usuário pode rastrear manualmente as informações da Remessa. Aqui estão alguns dos campos:


1. **Provedor de serviços** (opcional): um Provedor de serviços pode ser um serviço terceirizado que fornece serviços de remessa de várias transportadoras.
2. **ID da remessa**: o ID exclusivo da remessa na sua plataforma de remessa.
3. **Valor da remessa**: custo total incorrido na remessa
4. **Transportadora**: A transportadora que cuida da sua remessa e a entrega.
5. **Serviço da Transportadora** (opcional): O tipo/categoria de serviço fornecido pela transportadora. Por exemplo. algumas operadoras têm categorias como Econômica, Expressa, etc.
6. **Número AWB**: Um conhecimento aéreo (AWB) acompanha a carga aérea **internacional**. Geralmente possui um **número AWB** exclusivo, que facilita a identificação e o rastreamento de um transportador aéreo.
7. **Incoterm**: São um conjunto de regras reconhecidas internacionalmente que definem as responsabilidades de vendedores e compradores. [Saiba mais sobre isso aqui.](https://iccwbo.org/resources-for-business/incoterms-rules/incoterms-2020/)


### 3.3 Automação


Você também pode automatizar a comparação de taxas, a geração de etiquetas, o rastreamento etc. usando nossa [Integração de envio](/docs/pt/erpnext_integration/erpnext_shipping).


### 4. Tópicos Relacionados


1. [Nota de entrega](/docs/pt/stock/delivery-note)
2. [Guia de embalagem](/docs/pt/stock/packing-slip)



