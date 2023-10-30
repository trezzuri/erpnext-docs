# Recursos GST no ERPNext



### 1. Criação de Empresa e Masters


A lei GST exige que você mantenha os detalhes do GSTIN de todos os seus clientes e fornecedores. No ERPNext, o GSTIN está vinculado tanto ao **Endereço** quanto às **Partes**.


#### 1.1 Atualizar as informações de GSTIN da sua empresa


Atualize os detalhes do GST para a empresa. As validações de GST serão aplicadas a todas as transações da sua empresa com base na categoria de GST definida para ela.


Além disso, crie ou atualize o endereço da sua empresa com os detalhes de GST apropriados.


![Detalhes do GST da empresa](/files/company_gst_details.gif)


#### 1.2 Criar clientes e fornecedores


De maneira muito semelhante, crie ou atualize seus clientes e fornecedores com detalhes do GSTIN. Além disso, eles precisam ser atualizados nos endereços relevantes das partes.


O GST será aplicado e validado a uma transação específica com base neste mestre. Os detalhes do GST serão obtidos primeiro no endereço. Caso o Endereço não esteja disponível em uma transação, ele será aplicado conforme o Cliente ou Fornecedor.


![Criar entrada rápida de festa](/files/create_party_quick_entry.gif)


### 2. Configurações pré-empacotadas


#### 2.1 Códigos HSN


De acordo com a Lei GST, suas faturas detalhadas devem conter o Código HSN relacionado a esse Item. O ERPNext vem pré-instalado com todos os mais de 12.000 códigos HSN para que você possa selecionar facilmente o código HSN relevante em seu item


![HSN no item](/files/hsn-item.gif)


#### 2.2 Contas fiscais


Com novas instalações, você obtém contas GST padrão criadas para sua empresa.


![Ledgers GST](/files/gst-ledger.png)


#### 2.3 Modelos fiscais


Os modelos padrão de impostos sobre vendas e compras são pré-configurados para sua empresa.


![Modelo de imposto GST](/files/gst-tax-template.png)


#### 2.4 Modelos de impostos de itens


Para diferentes alíquotas de impostos, você obtém modelos de impostos de itens pré-configurados para sua empresa. Eles são úteis quando você deseja configurar taxas de imposto de item diferentes daquelas configuradas nos modelos de imposto sobre vendas e compras padrão.


![Modelo de imposto de item GST](/files/gst_item_tax_template.png)


#### 2,5 contas GST nas configurações de GST


Quando as contas GST são criadas automaticamente, suas configurações são atualizadas automaticamente para sua empresa nas configurações de GST. Isso garantirá validações de GST e relatórios de GST apropriados.


![Configurações de GST para conta GST](/files/gst_settings_accounts.png)



> 
> Se desejar ter configurações padrão diferentes, você deverá configurá-las manualmente em todos os locais acima.
> 
> 
> 


### 3. Fazendo faturas prontas para GST


Se você configurou o GSTIN de seus clientes e fornecedores e seu modelo fiscal, você está pronto para fazer faturas prontas para GST!


#### 3.1 Criação de fatura de vendas


1. Selecione o cliente e o item.
2. Verifique se o GSTIN da sua Empresa e do Cliente foi configurado corretamente.
3. Verifique se o Número HSN foi configurado corretamente no Item.
4. Selecione **GST no estado** ou **GST fora do estado** como modelo de imposto.
5. Salve e envie a fatura.


![Fatura GST](/files/gst-invoice.gif)


#### 3.2 Impressão de fatura fiscal GST


Para imprimir a fatura fiscal de acordo com as diretrizes da GSTN, selecione o formato de impressão da **fatura fiscal GST**. Este formato de impressão inclui endereço da empresa, números GSTIN, código HSN/SAC e divisão de impostos por item. E durante a impressão selecione o valor correto do campo Cópia da Fatura, para mencionar se é para o Cliente, Fornecedor ou Transportador.


![Exemplo de fatura fiscal GST](/files/sample-gst-tax-invoice.png)


### 4. Transações de GST


#### 4.1 Reversão de crédito de imposto sobre insumos


Para registrar o estorno do ITC, acesse o tipo de documento de lançamento contábil manual e siga as etapas a seguir


1. Selecione "Tipo de entrada" como "Reversão de ITC"
2. Em "Tipo de reversão" selecione "De acordo com as regras 42 e 43 das Regras CGST" ou "Outros" com base nos tipos de reversão
3. Selecione o endereço da empresa (GSTIN) apropriado para o qual o ITC está sendo revertido
4. Preencha as contas e valores nos Lançamentos Contábeis conforme mostrado abaixo
5. Salvar e enviar


![Reversão de crédito de imposto pago a montante](/files/reversal-of-itc.png)


### 5. Configuração de cobrança reversa e lançamento de faturas de compra de cobrança reversa


#### 5.1 Adicionar contas de cobrança reversa nas configurações de GST


Adicione contas de cobrança reversa para GST conforme mostrado na imagem abaixo e marque "É conta de cobrança reversa" conforme mostrado na imagem abaixo. Em vez de uma conta de autoliquidação separada, a conta de imposto GST de saída usada para vendas também pode ser marcada como conta de autoliquidação


![Configurações de cobrança reversa de GST](/files/gst-reverse-charge-setting.png)


#### 5.2 Tornar faturas de compra sujeitas a cobrança reversa


Para tornar faturas de compra passíveis de cobrança reversa de faturas, siga as etapas a seguir


* Selecione Fornecedor e adicione itens à fatura normalmente
* Selecione "Cobrança reversa aplicável como "Y" na seção de detalhes do GST
* Se o GST pago for elegível para crédito de imposto pago a montante, em "Elegibilidade para ITC" selecione "ITC sobre cobrança reversa"
* "Adicionar" impostos usando os cabeçalhos normais da conta de imposto pago a montante


![Carga reversa](/files/reverse-charge-add.png)


* "Deduza" o mesmo valor de impostos usando as contas de cobrança reversa para que o GST líquido a pagar pelo fornecedor seja 0


![Cobrança reversa](/files/reverse-charge-deduct.png)


* Salvar e enviar


Para evitar a seleção manual de contas e automatizar esse processo, siga as etapas abaixo


* Criar categoria de imposto para cobrança reversa


![Categoria de imposto de cobrança reversa](/files/reverse-charge-tax-category.png)


* Atualizar categoria de imposto nos cadastros de fornecedores relevantes


![Categoria de imposto do fornecedor](/files/supplier-tax-category.png)


* Criar modelo de impostos e taxas de compra para cobrança reversa


![Modelo de cobrança reversa](/files/reverse-charge-template.png)


* Depois que esta configuração for feita, na seleção do fornecedor, o modelo de impostos e encargos de compra apropriado será aplicado.


### 6. Relatórios


ERPNext vem com a maioria dos relatórios necessários para preparar seus retornos de GST. Vá para Contas > GST Índia para ver a lista.


![Relatórios GST](/files/gst-reports.png)


Você pode verificar o impacto da sua fatura no **Registro de vendas do GST** e no **Registro de vendas discriminadas do GST**


![GST Itemized Sales Register](/files/gst-itemised-sales-register.png)



