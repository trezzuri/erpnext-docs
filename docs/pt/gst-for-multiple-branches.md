# GST para múltiplas filiais



Isso ajudará você a automatizar o cálculo do GST se sua empresa tem filiais diferentes com GSTIN separados. 

  


Esta é uma extensão para o blog: [5 etapas para automatizar o GST indiano no ERPNext](https://erpnext.com/blog/erpnext-features/5-steps-to-automate-indian-gst-in-erpnext)

  
1. **Atualize os endereços das filiais da sua empresa**
2. **Configurar contas GST estaduais** ***(Opcional)***
3. **Configuração de GST por item**
4. **Classificação de Impostos Interestaduais e Intra-Estaduais**
5. **Configurando modelos de fatura**

  


### Etapa 1-Atualize os endereços de cobrança das filiais da sua empresa

  


O primeiro passo é atualizar o endereço da filial da sua empresa com o GSTIN apropriado, pois será diferente *(se em estados diferentes)* deramo a ramo. 

  


![](https://erpnext.com/files/RU29P7U.png)

﻿

Agora, certifique-se de que os endereços do seu Cliente e Fornecedor tenham *Estado GST* e *Party GSTIN* configurado corretamente.

  


﻿![](https://erpnext.com/files/LdjEDNd.png)

### 

### ﻿Etapa 2-Configurar contas GST estaduais ***(Opcional)***

  


Para configurar, vá para Plano de contas, crie um conjunto estadual de contas GST *(CGST, SGST e IGST)* como visto na captura de tela abaixo .

﻿

﻿![](https://erpnext.com/files/BVg9U1f.png)

  
 

  


Adicione essas contas recém-criadas na tabela *Contas GST* em **Configurações GST**, para incluí-las em todas Relatórios GST.

  


![](https://erpnext.com/files/JBtVopQ.png)

 

### Etapa 3-Configuração do GST por item

  


a. Crie um **modelo de imposto de item** para taxas diferentes e adicione todas as *Contas GST* que criamos na etapa anterior.

b. Defina as taxas.

Isso ajuda o sistema a saber quais contas GST e taxas de imposto aplicar nas faturas.

  


Seu modelo de imposto de item deve ser parecido com este: 

![](https://erpnext.com/files/MuMGvEa.png)

  


**Da mesma forma, você pode criar diferentes modelos de impostos de itens para diferentes taxas de GST.** 

  
 

Após a criação dos Modelos de Impostos de Itens, você pode começar atribuindo esses modelos aos seus respectivos itens no Cadastro de Itens.

  


![](https://erpnext.com/files/qhXeg1d.png)

 ### Etapa 4-Classificação dos Impostos Interestaduais e Intra-Estaduais

  


Estamos quase lá.

Crie dois **Categorias de impostos**, para cada uma de nossas filiais em um estado diferente. O **Estado de origem** em cada *Categoria de Imposto* corresponderá a cada uma das filiais da nossa empresa.

Cada estado terá duas categorias de impostos, uma para transações interestaduais e outra para transações fora do estado. 

  


Para categorias de impostos 'Fora do estado', marque a caixa de seleção 'É interestadual' como ativada. 

  


*Categoria de imposto estadual IN para Delhi:* 

![](https://erpnext.com/files/qJiylOa.png)

  
*Categoria de imposto estadual OUT para Delhi:* 

![](https://erpnext.com/files/vL7KwMs.png) 

**Crie para outros estados da mesma forma mostrada acima.**

  


### Etapa 5-Configurando nossos modelos de fatura

  


Finalmente, configure um conjunto de dois **Modelos de impostos e taxas sobre vendas** e dois **Modelos de Impostos e Taxas de Compra, para cada Categoria de Imposto criada.** 

**﻿**

Vá para Modelo de impostos e taxas sobre vendas e defina um conjunto de dois modelos para cada estado (como visto na captura de tela abaixo para Maharashtra)  


*Para o modelo IN State, escolha a categoria de imposto estadual IN e a conta CGST e SGST apropriada em* ***Cabeçalho da conta.*** 

  


![](https://erpnext.com/files/Jv8R3fX.png)

  


*Para o modelo OUT State, escolha a categoria de imposto estadual OUT e a conta IGST apropriada em* ***Cabeçalho da conta.*** 

![](https://erpnext.com/files/lwQVAOr.png)

  


**Nota: Insira nossas *Contas Fiscais* em *Cabeçais de Conta* e deixe *resto como '0'*-já que as taxas de imposto serão obtidas no Item Master.**

  


Repita o mesmo processo para configurar o **Modelo de impostos e cobranças de compra** e para outros **Estados** também. 

  


### Aproveitamos os frutos do nosso trabalho:

  


Atualize sua conta agora como concluímos a configuração agora.

  


Para verificar se tudo funciona conforme o esperado, crie uma fatura ou um pedido:

1. Selecione um cliente/fornecedor.
2. Verifique o endereço da empresa e selecione-o novamente para a filial a partir da qual você deseja criar a fatura/pedido.
3. Selecionar Cliente/Fornecedor irá buscar o modelo correto, verifique se os Impostos e Taxas foram buscados corretamente.

  


### Exemplo 1:

Aqui eu selecionei um **Cliente de Maharashtra e o endereço da empresa como Maharashtra** também, ele deve buscar o modelo IN State que criamos acima.

  


![](https://erpnext.com/files/KOv2bSi.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/Kz3m5ux.png)

  
 

### Exemplo 2:

Aqui selecionei um **Cliente de Maharashtra e o endereço da empresa é Delhi**, ele deve buscar o modelo OUT State que criamos acima.

  


![](https://erpnext.com/files/edIsIvn.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/0DvILkB.png)













