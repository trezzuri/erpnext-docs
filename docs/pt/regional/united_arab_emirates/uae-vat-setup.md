# Implementação do imposto IVA/EXCISE para Emirados Árabes Unidos/KSA



### 1. Configurando Nº de Registro Fiscal para cliente, fornecedor e empresa


Defina o Número de Registro Fiscal no campo, CNPJ do Cliente, Fornecedor e Empresa.


1. Para o cliente
![TRN no cliente](/files/tax-id-customer.png)
2. Para empresa
![TRN in Company](/files/tax-id-company.png)


### 2. Configurando código fiscal para produtos


Configure o código tributário no cadastro de itens, o sistema irá buscar o mesmo código na fatura de venda/compra ao selecionar um item.


![Código tributário no item](/files/tax-code-item.png)


### 3. Modelos fiscais padrão


ERPNext fornece modelo de imposto padrão para IVA (5%, zero, isento) e impostos especiais de consumo (50%, 100%). Você pode criar seu próprio [modelo de imposto](/docs/pt/setting-up/setting-up-taxes.html).


![Modelo de imposto padrão](/files/uae-tax-templates.png)


### 3. Elaboração de faturas prontas para IVA


Se você configurou o TRN de seus clientes e fornecedores e seu modelo de imposto, você está pronto para fazer faturas prontas para IVA!


Para **fatura de vendas**,


1. Selecione o Cliente e o Item corretos e o endereço onde a transação acontecerá.
2. Verifique se o TRN da sua Empresa e Fornecedor foi configurado corretamente.
3. Verifique se o Código Fiscal foi definido no Item
4. Selecione o modelo que você criou com base no tipo de transação
5. Salvar e enviar a fatura


![Fatura de IVA](/files/vat-invoice.gif)


### 4. Imprimir nota fiscal


ERPNext fornece dois formatos de impressão padrão


1. Nota Fiscal Simplificada
![Nota Fiscal Simplificada](/files/simplified-invoice.png)
2. Nota fiscal detalhada
![Nota fiscal detalhada](/files/detailed-invoice.png)


### 5. Configurar contas de IVA


Selecione aqui as contas que serão usadas para criar faturas de IVA.


![Configurações da conta de IVA dos Emirados Árabes Unidos](/files/uae-vat-account-settings.png)



