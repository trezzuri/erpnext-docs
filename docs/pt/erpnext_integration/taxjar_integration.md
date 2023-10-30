# Integração Taxjar



A integração do TaxJar permite que os usuários do ERPNext calculem automaticamente os impostos com base nos endereços dos clientes, empresas e locais de entrega.


### Como configurar o TaxJar?


### Conta TaxJar e tokens de API:


Você precisará dos tokens API da sua conta para configurar o Taxjar.


1. Crie uma [conta Taxjar](https://www.taxjar.com/) primeiro de acordo com seus requisitos.
2. Faça login no painel da sua conta e clique no botão **Conta** e clique em **API TaxJar** na lista suspensa de opções.![](/files/RExrQMg.png)
3. Agora você verá seus tokens de API, esses tokens seriam necessários para configurar sua integração ERPNext TaxJar.![](/files/0fs0ug5.png)


### Adicionando Nexus e estados no TaxJar:


**O que é Nexus?**


Você não precisa se registrar para coletar impostos sobre vendas de clientes em todos os estados. Você só coletará impostos sobre vendas de clientes que moram nos estados onde você tem domicílio fiscal!


"Nexus" é um tipo específico de conexão com um estado que é significativo o suficiente para que você seja obrigado a cumprir as leis de imposto sobre vendas desse estado.


**Como posso saber onde tenho o Nexus?**


Você sempre terá presença física em seu estado de origem onde está localizado.


Para mais detalhes, leia o [TaxJar oficial página sobre o Nexus](https://support.taxjar.com/article/115-how-do-i-know-where-i-have-nexus) sem falhas!


**Adicionando estados:**


Siga as instruções detalhadas fornecidas na página oficial do TaxJar [aqui](https://support.taxjar.com/article/116-add-or-remove-states-from-your-dashboard) em relação à adição/remoção de estados do seu painel, siga as instruções de cima para baixo, pois isso o ajudará a configurar tudo perfeitamente.


### Configurando TaxJar no ERPNext:


Na barra incrível, procure por **'Configurações do TaxJar'.** É aqui que você configura sua integração do TaxJar no ERPNext.


![](/files/R0w9mXD.png)


**Modo sandbox:**


TaxJar fornece um ambiente sandbox para testes e desenvolvimento automatizados. Depois de gerar um token de API sandbox, direcione seu cliente API para o ambiente sandbox: <https://api.sandbox.taxjar.com>] 


**Configurar tokens e chefes de conta:**


1. Ativar cálculo de impostos, criar transação TaxJar:
2. Você precisa ativar essas opções para cálculos automáticos de impostos e essas transações aparecerão na página de transações da sua conta TaxJar, onde você pode rastreá-las e analisar os detalhamentos dos impostos.
3. Depois de fazer algumas transações, elas aparecerão automaticamente na página **Transações** do TaxJar:![](/files/o54QVVm.gif)- Você pode conferir todas as transações realizadas e o detalhamento dos impostos.
- Copie os tokens de API da sua conta TaxJar conforme indicado acima e cole-os nos campos **Live API Key** e **Sandbox API key.**
- Você terá que definir duas contas para Impostos e Frete, selecionar as contas conforme necessário e depois que tudo estiver configurado, clicar em salvar e pronto!


### Definindo endereços corretos


Para que a integração funcione perfeitamente, certifique-se de ter criado endereços corretos para sua empresa, clientes, fornecedores, etc.


**Observação:**


1. Ao criar um endereço, certifique-se de inserir o estado correto no campo **Estado/Província**. TaxJar requer o formato de 2 letras para os estados, por exemplo. Nova York é considerada NY, mas **não precisa** ser inserida obrigatoriamente dessa forma, o sistema converte-o automaticamente para o código do estado de 2 letras.![](/files/aAiBsBk.png)
2. Você pode marcar as caixas de seleção **Endereço de cobrança preferencial** e **Endereço de entrega preferencial** para preencher automaticamente esses campos em faturas diferentes e evitar complicações.
3. Certifique-se de ter preenchido corretamente os campos **Cidade/município, estado/província, país, código postal**.
4. Você pode querer desativar os impostos, se houver, que são definidos por padrão.


### TaxJar em ação!


Neste caso, temos uma empresa sediada em **Nova York** e estamos emitindo uma fatura de vendas para um cliente localizado no mesmo estado.![](/files/SvGCGB3.gif)


Como você pode ver, os impostos e cobranças com base no estado e no código PIN são aplicados automaticamente ao economizar.



