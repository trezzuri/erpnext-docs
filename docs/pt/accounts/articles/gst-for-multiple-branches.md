# GST para várias filiais


Isso ajudará você a automatizar o cálculo do GST se sua empresa tem ramificações diferentes com GSTIN separado. 

  


Esta é uma extensão para o blog: [5 etapas para automatizar o GST indiano no ERPNext](https://erpnext.com/blog/erpnext-features /5-steps-to-automate-indian-gst-in-erpnext)

  


1. **Atualize os endereços das filiais da sua empresa**
2. **Configurar contas GST estaduais** ***(Opcional)***
3. **Configuração de GST por item**
4. **Classificação de Impostos Interestaduais e Intraestaduais**
5. **Configuração de modelos de fatura**

  


### Etapa 1- Atualize os endereços de cobrança da filial da sua empresa

  


A primeira etapa é atualizar o endereço da filial da sua empresa com o GSTIN apropriado, pois ele será diferente *(se em estados diferentes)* deramo a ramo. 

  


![](https://erpnext.com/files/RU29P7U .png)

﻿

Agora, certifique-se de que os endereços de seus Clientes e Fornecedores tenham *Estado GST* e *Party GSTIN* configurado corretamente.

  


﻿![](https://erpnext.com/files/LdjEDNd.png)

### 

### ﻿Etapa 2 - Configurar contas GST estaduais ***(Opcional)***

  


Para configurar, vá para Plano de contas, crie um conjunto estadual de contas GST *(CGST, SGST e IGST)* como visto na captura de tela abaixo .

﻿

﻿![](https://erpnext.com/files/BVg9U1f.png)

  
 

  


Adicione essas contas recém-criadas na tabela *GST Accounts*  de **GST Settings**, para incluir isso em todos Relatórios GST.

  


![](https://erpnext.com/files/JBtVopQ.png)

< span style="background-color: rgb(255, 255, 255);"> 

### Etapa 3 - Configuração do GST por item

  


a. Criar **Modelo de imposto de item** para taxas diferentes e adicione todas as *Contas GST* que criamos na etapa anterior.

b. Defina as taxas.

Ajuda o sistema a saber quais contas de ICMS e alíquotas aplicar nas faturas.

  


Seu modelo de imposto de item deve ficar assim: 

![](https://erpnext.com/files/MuMGvEa.png)< /p>  


**Da mesma forma, você pode criar diferentes modelos de impostos de itens para diferentes taxas GST.** 

  
 

Após a criação dos Modelos de Imposto de Item, você pode começar atribuindo esses modelos aos seus respectivos Itens no Cadastro de Itens.

  


< img src="https://erpnext.com/files/qhXeg1d.png"/>

 

### Passo 4 - Classificação dos Impostos Interestaduais e Intraestaduais

  


Estamos quase lá.

Crie dois **Categorias de impostos**, para cada uma de nossas filiais em diferentes estados. O **Estado da fonte** em cada *Categoria de imposto* corresponderá a cada uma das filiais da nossa empresa.

Cada estado terá duas categorias fiscais, uma para transações dentro do estado e outra para fora do estado. 

  


< estilo forte="cor: rgb(45, 55, 72); background-color: transparent;">Para categorias de impostos 'Out State', marque a caixa de seleção 'Is Inter State' como habilitada. 

  


*NA categoria de imposto estadual para Delhi:* 

![](https://erpnext.com/files/qJiylOa.png)

  


*﻿Out State Tax Category for Delhi:* 

![](https://erpnext.com/files/vL7KwMs.png)

 

**Criar para os demais Estados da mesma forma mostrada acima.**

  


### Etapa 5 - Configurando nossos modelos de fatura

  


Finalmente, configure um conjunto de dois **Modelos de impostos e cobranças sobre vendas** e dois **Compra de Modelos de Impostos e Cobranças, para cada Categoria de Imposto criada.** 

**﻿**

Vá para Modelo de impostos e cobranças sobre vendas e defina um conjunto de dois modelos para cada estado (como visto na captura de tela abaixo para Maharashtra)

  


*Para o modelo IN State, escolha a categoria IN State Tax e a conta CGST & SGST apropriada em* ***Account Head.*** 

  


![](https://erpnext.com/files/Jv8R3fX.png)

  


*Para o modelo OUT State, escolha a categoria OUT State Tax e a conta IGST apropriada em* ***Account Head.*** 

![](https://erpnext.com/files/lwQVAOr.png)

  


**Observação: Insira nossas *Contas fiscais* em *Cabeçalhos da conta* e deixe *resto como '0'* - já que as taxas de imposto serão obtidas do Item Master.**

  


Repita o mesmo processo para configurar **Modelo de impostos e cobranças de compra** e para outros **Estados** também. 

  


### Aproveitamos os frutos do nosso trabalho:

  


Atualize sua conta agora como concluímos a configuração agora.

  


Para verificar se tudo funciona conforme o esperado, crie uma Fatura ou um Pedido:

1. Selecione um cliente/fornecedor.
2. Verifique o endereço da empresa e selecione-o novamente para qualquer filial da qual você deseja criar a fatura/pedido.
3. Selecionar Cliente/Fornecedor buscará o modelo correto, verifique se os Impostos e Encargos foram buscados corretamente.

  


### Exemplo 1:

Aqui selecionei um **cliente de Maharashtra e o endereço da empresa como Maharashtra** também, ele deve buscar o modelo IN State que criamos acima.

  


![](https://erpnext.com/files/KOv2bSi.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/Kz3m5ux.png)

  


### Exemplo 2:

Aqui selecionei um **Cliente de Maharashtra e Endereço da empresa como Delhi**, deve buscar o modelo OUT State que criamos acima.

  


![](https://erpnext.com/files/edIsIvn.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/0DvILkB. png)



