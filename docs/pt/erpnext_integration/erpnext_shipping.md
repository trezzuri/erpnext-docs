# ERPNext Envio



> Introduzido na versão 13


**O aplicativo ERPNext Shipping ajuda você a comparar as taxas de envio oferecidas por vários provedores de serviços, gerar etiquetas e rastrear o status de suas remessas.**


A integração com os seguintes provedores de serviços está disponível:


1. [Packlink](https://www.packlink.com/en-GB/)
2. [LetMeShip](https://www.letmeship.com/en/)
3. [SendCloud](https://www.sendcloud.com)


> Para aproveitar esses recursos, o aplicativo **ERPNext Shipping** deverá estar instalado em seu site. Você pode disponibilizar o aplicativo [no GitHub](https://github.com/frappe/erpnext-shipping/tree/master), [no Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/shipping) ou você pode entrar em contato com sua plataforma de hospedagem.


## 1. Configuração


Para que o aplicativo funcione perfeitamente, você terá que gerar uma chave de API de **pelo menos uma** das plataformas listadas acima. Aqui está um guia para configurá-los:


### 1.1 API Packlink


1. Registre-se no [Packlink PRO](https://auth.packlink.com/en-GB/pro/register?platform=PRO&platform_country=UN).
2. Siga [estas etapas](https://support-pro.packlink.com/hc/en-gb/articles/213431749-How-to-generate-an-API-key-on-PRO)  para gerar uma **chave de API**.
3. Procure por **Packlink** na barra incrível.
4. Adicione a **chave API** ao Packlink DocType, marque o campo 'Ativado'.
5. Salvar.


![Packlink API](/files/packlink_api.png)


### 1.1 API Sendcloud


1. Registre-se no [Sendcloud](https://panel.sendcloud.sc/accounts/signup/).
2. Siga [estas etapas](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) para gerar uma **chave pública** e uma **chave secreta**.
3. Pesquise **SendCloud** na barra incrível.
4. Adicione a **Chave Pública** no campo 'API Key' e a **Chave Secreta** no campo 'API Secret' do SendCloud DocType.
5. Marque o campo **Ativado**.
6. Salvar.


![API Sendcloud](/files/sendcloud_api.png)


### 1.1 API LetMeShip


1. Registre-se em [LetMeShip](https://www.letmeship.com/en/).
2. Siga [estas etapas](https://www.letmeship.com/en-de/shipping-api/) para gerar um **ID de API** e **Senha da API**.
3. Procure por **LetMeShip** na barra incrível.
4. Adicione o **API ID** e a **API Password** ao LetMeShip DocType. Verifique o campo **Ativado**.
5. Salvar.


![API LetMeShip](/files/letmeship_api.png)


## 2. Recursos


### 2.1 Comparação de taxas de envio


Depois que uma [remessa](/docs/pt/stock/shipment) for enviada, se o aplicativo estiver instalado, o botão **Obter taxas de envio aparecerá. Ao clicar, você receberá uma lista de serviços junto com seus prestadores de serviços e tarifas.**


![Taxas de busca](/files/fetch_rates.png)


Você também pode adicionar serviços usados ​​com frequência aos seus **Serviços Preferenciais** usando o **Tipo de serviço de encomendas**:


1. Supondo que o serviço destacado seja nosso serviço usado com frequência, vamos adicioná-lo aos nossos **Serviços Preferenciais**


![Serviço de destaque](/files/service_highlight.png)
2. Vá para **Tipo de serviço de encomendas** > **Novo**. Crie um novo **serviço de encomendas**. No nosso caso, é 'TNT'.
3. Adicione um **Tipo de serviço de encomendas**. No nosso caso, será 'Economia'.
4. Adicione também 'Economia' à tabela **Alias ​​do tipo de serviço de encomendas**.
5. Adicione uma descrição (opcional).
6. Ative o campo **Mostrar na lista de serviços preferenciais**. Salvar.


Agora, ao clicar no botão **Obter taxas de envio**, você sempre verá o serviço destacado anteriormente em **Serviços preferenciais**.


![Serviço Preferencial](/files/preferred_service.png)


### 2.2 Criação de Remessa


Depois de comparar as taxas, você pode prosseguir com qualquer um dos serviços clicando em **Selecionar** na linha de serviço apropriada. Ao clicar, uma Remessa é criada automaticamente na plataforma do seu provedor de serviços.


Você notará que a seção **Informações da Remessa** é atualizada automaticamente, com base na Remessa criada.


![Criação de Remessa](/files/create_shipment.gif)


Você também pode pesquisar sua transação na plataforma do seu provedor de serviços usando o campo **ID da remessa**.


![Packlink Shipment](/files/packlink_shipment.png)


### 2.3 Impressão de etiquetas


Para utilizar o botão **Imprimir etiqueta de envio**, o **ID da remessa** deve ser gerado no registro atual.


![Imprimir botão de etiqueta](/files/print_label_button.png)


Você pode clicar nele e gerar sua etiqueta de envio.


![Etiqueta de envio fictícia](/files/dummy_shipping_label.png)


Você também pode acompanhar o status da sua remessa clicando em **Ver** > **Rastrear status**.


> **Observação** : as plataformas atualmente integradas podem não atender à sua região. Visite os links anexados a eles para saber mais.



