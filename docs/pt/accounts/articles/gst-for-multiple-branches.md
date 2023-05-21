# GST para várias filiais


Isso ajudará você a automatizar o cálculo do GST se sua empresa tiver filiais diferentes com GSTIN separado.

  


Esta é uma extensão do blog: [5 etapas para automatizar o Indian GST no ERPNext](https://erpnext.com/blog/erpnext-features/5-steps-to-automate-indian-gst-in-erpnext)

  


1. **Atualize os endereços das filiais da sua empresa**
2. **Configurar contas GST estaduais** ***(Opcional)***
3. **Configuração de GST por item**
4. **Classificação de Impostos Interestaduais e Intraestaduais**
5. **Configuração de modelos de fatura**

  


### Etapa 1- Atualize os endereços de cobrança da filial da sua empresa

  


O primeiro passo é atualizar o endereço da filial da sua empresa com o GSTIN apropriado, pois ele será diferente *(se em estados diferentes)* de filial para filial.

  


![](https://erpnext.com/files/RU29P7U.png)

﻿

Agora, certifique-se de que os endereços do seu cliente e fornecedor tenham *GST State* e *Party GSTIN* configurado corretamente.

  


﻿![](https://erpnext.com/files/LdjEDNd.png)

###

### ﻿Etapa 2 - Configurar contas GST estaduais ***(Opcional)***

  


Para configurar, vá para Plano de contas, crie um conjunto estadual de contas GST *(CGST, SGST e IGST)* conforme mostrado na captura de tela abaixo.

﻿

﻿![](https://erpnext.com/files/BVg9U1f.png)

  


  


Adicione essas contas recém-criadas na tabela *GST Accounts* em **GST Settings**, para incluí-las em todos os relatórios GST.

  


![](https://erpnext.com/files/JBtVopQ.png)



### Etapa 3 - Configuração do GST por item

  


a. Crie **Modelo de imposto de item** para taxas diferentes e adicione todas as *Contas GST* que criamos na etapa anterior.

b. Defina as taxas.

Isso ajuda o sistema a saber quais contas de ICMS e alíquotas de imposto aplicar nas faturas.

  


Seu modelo de imposto de item deve ficar assim:

![](https://erpnext.com/files/MuMGvEa.png)

  


**Da mesma forma, você pode criar diferentes modelos de impostos de itens para diferentes taxas de GST.**

  


Após a criação dos Modelos de Imposto de Item, você pode começar atribuindo esses modelos aos seus respectivos Itens no Cadastro de Itens.

  


![](https://erpnext.com/files/qhXeg1d.png)



### Passo 4 - Classificação dos Impostos Interestaduais e Intraestaduais

  


Estamos quase lá.

Crie duas **Categorias Fiscais**, para cada uma de nossas filiais em diferentes Estados. O **Estado de origem** em cada *Categoria fiscal* corresponderá a cada uma das filiais da nossa empresa.

Cada estado terá duas Categorias de Impostos, uma para transações dentro do estado e outra para fora do estado.

  


**Para Categorias de imposto "Out State", marque a caixa de seleção "Is Inter State" como ativada.**

  


*NA categoria de imposto estadual para Delhi:*

![](https://erpnext.com/files/qJiylOa.png)

  


*﻿Categoria de imposto estadual FORA para Delhi:*

![](https://erpnext.com/files/vL7KwMs.png)



**Criar para outros Estados da mesma forma que mostrado acima.**

  


### Etapa 5 - Configurando nossos modelos de fatura

  


Por fim, configure um conjunto de dois **Modelos de impostos e cobranças sobre vendas** e dois **Modelos de impostos e cobranças sobre compras para cada categoria de imposto criada.**

**﻿**

Acesse Modelo de impostos e cobranças sobre vendas e defina um conjunto de dois modelos para cada estado (conforme visto na captura de tela abaixo para Maharashtra)

  


*Para o modelo IN State, escolha a categoria de imposto IN State e a conta CGST & SGST apropriada em* ***Cabeçalho da conta.***

  


![](https://erpnext.com/files/Jv8R3fX.png)

  


*Para o modelo OUT State, escolha a categoria de imposto OUT State e a conta IGST apropriada em* ***Cabeçalho da conta.***

![](https://erpnext.com/files/lwQVAOr.png)

  


**Observação: Insira nossas *Contas de impostos* em *Cabeçalhos de contas* e deixe o *resto como '0'* - já que as taxas de impostos serão buscadas no Cadastro de Itens.**

  


Repita o mesmo processo para configurar **Purchase Taxes and Charges Template** e também para outros **Estados**.

  


### Aproveitamos os frutos do nosso trabalho:

  


Atualize sua conta agora, pois concluímos a configuração agora.

  


Para verificar se tudo funciona conforme o esperado, crie uma Fatura ou um Pedido:

1. Selecione um Cliente/Fornecedor.
2. Verifique o Endereço da Empresa e selecione-o novamente para qualquer Filial da qual você deseja criar a Fatura/Pedido.
3. Selecionar Cliente/Fornecedor buscará o modelo correto, verifique se os Impostos e Encargos foram buscados corretamente.

  


### Exemplo 1:

Aqui eu selecionei um **cliente de Maharashtra e o endereço da empresa como Maharashtra** também, ele deve buscar o modelo IN State que criamos acima.

  


![](https://erpnext.com/files/KOv2bSi.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/Kz3m5ux.png)

  


### Exemplo 2:

Aqui eu selecionei um **cliente de Maharashtra e o endereço da empresa como Delhi**, ele deve buscar o modelo OUT State que criamos acima.

  


![](https://erpnext.com/files/edIsIvn.png)

  


Ele buscou automaticamente o seguinte modelo de impostos e cobranças:

![](https://erpnext.com/files/0DvILkB.png)