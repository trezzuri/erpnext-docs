# Categoria de retenção de imposto



**A categoria de retenção de imposto é deduzida na fonte.**


De acordo com isso, a pessoa responsável por efetuar os pagamentos é obrigada a deduzir o imposto na fonte de acordo com as taxas prescritas. Em vez de receber de você o imposto sobre sua renda posteriormente, o governo deseja que os pagadores deduzam o imposto antecipadamente e o depositem no governo.


Para acessar a lista de categorias de retenção de impostos, acesse:



> 
> Home > Contabilidade > Impostos > Categoria de Retenção de Impostos
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma categoria de retenção de imposto, é aconselhável criar primeiro o seguinte:


1. [Fornecedor](/docs/pt/buying/supplier)
2. [Cliente](/docs/pt/CRM/customer)


## 2. Como criar uma categoria de retenção de imposto


No ERPNext, as categorias de retenção de impostos para a maioria dos casos estão disponíveis por padrão, no entanto, você pode criar mais, se necessário.


1. Vá para a lista Categoria de retenção de impostos e clique em Novo.
2. Insira um nome exclusivo, por exemplo: Seção 194C Indivíduo.
3. Insira um nome de categoria (dividendos, honorários profissionais, etc.).
4. Insira uma taxa de retenção de imposto em relação a um [ano fiscal](/docs/pt/accounts/fiscal-year).
5. Você pode definir o limite para uma única fatura ou a soma de todas as faturas.
6. Selecione uma conta da sua empresa na qual o imposto será creditado.
7. Adicione mais empresas e contas conforme necessário.
8. Salvar.


![Categoria de retenção de imposto](/files/tax-withholding-category.png)


Nos detalhes contábeis, a conta TDS é adicionada para cada empresa no sistema.


### 2.1 Atribuição de retenção de imposto ao fornecedor


Após salvar, pode ser atribuído a um Fornecedor:


![Categoria de retenção de imposto no fornecedor](/files/tax-withholding-category-in-supplier.png)


### 2.2 Como funciona o limite?


Considere um fornecedor ao qual é aplicada uma categoria de retenção de imposto.


Por exemplo, digamos que uma taxa de 5% será aplicável à fatura em que o limite único seja 20.000 e o limite cumulativo seja 30.000. Se uma fatura for criada com um total geral de 20.000, o limite único será acionado e um imposto de 5% será cobrado.


Mas se o valor da fatura totalizar 15.000, nenhum imposto será cobrado, pois não ultrapassou o limite. Se novamente for criada outra fatura contra o mesmo fornecedor com um total de 15.000, embora não tenha ultrapassado o limite Único, os encargos serão deduzidos desde a soma da última fatura e esta fatura soma 30.000, o que é igual ao Limite cumulativo especificado.


## 3. Usando retenção de impostos


### 3.1 Uso na fatura de compra


No exemplo a seguir, selecionamos 'TDS-194C-Individual' que tem um limite único de 30.000, limite cumulativo de 1.00.000 e taxa de 1%.


1. Se o **Fornecedor** tiver o campo de retenção de imposto definido, ao selecionar esse Fornecedor, uma caixa de seleção ficará visível na fatura de compra para selecionar se deseja aplicar imposto ou não.


![Categoria de retenção de imposto na fatura de compra](/files/tax-withholding-category-in-purchase-invoice.png)


1. Vamos criar uma fatura de 90.000. Salvar a fatura calcula automaticamente o imposto e o anexa à tabela de impostos.


![Categoria de retenção de imposto na fatura de compra](/files/withheld-tax-calculation-in-purchase-invoice.png)
2. Para ver o efeito do limite cumulativo, vamos criar uma fatura com valor de 10.000 e enviá-la.


![Limite cumulativo da categoria de retenção de imposto](/files/tax-withholding-category-cumulative-threshold.png)


Embora o valor da fatura não tenha ultrapassado o limite Único (30.000), vemos que o imposto foi cobrado. Isso ocorre porque a fatura anterior e a atual somam 1.10.000, o que excede o limite Acumulado. Portanto, o imposto baseado na alíquota fornecida na **categoria de retenção de imposto** é aplicado adequadamente.



> 
> Observação: Ao enviar a fatura, três lançamentos contábeis são criados:
> 
> 
> 



> 
> 1. Primeiro para débito do responsável pelas despesas
> 2. Segundo em crédito na conta dos credores
> 3. Terceiro para crédito na conta selecionada na categoria Retenção de Imposto.
> 
> 
> 


### 3.2 Dedução do imposto na fonte sobre adiantamentos


#### 3.2.1 Dedução de TDS antecipado em relação ao pedido de compra


1. Configure a Categoria de Retenção de Imposto contra o fornecedor e faça um Pedido de Compra contra o fornecedor. Um ponto a ser lembrado aqui é não marcar a opção "Aplicar retenção de imposto" no pedido, pois o pedido deve ser gerado pelo valor total
2. Crie uma entrada de pagamento para esse pedido de compra. Na seção Impostos e encargos, ative "Aplicar retenção de imposto" e insira outros detalhes e, em seguida, salve e envie a entrada.


![Entrada de pagamento retido na fonte de imposto](/files/Tax-Withholding-Payment Entry.png)


3. Crie uma fatura de compra para este pedido e ative "Definir adiantamentos e alocação (FIFO)" para que o pagamento vinculado ao pedido correspondente seja aplicado automaticamente. Nenhum Imposto será retido na Fatura de Compra se o Imposto pago antecipadamente for maior ou igual ao valor do imposto na Fatura. O imposto será retido apenas para o valor excedente, se aplicável.


### 3.2.2 Dedução de TDS de adiantamentos pagos (usando entrada de pagamento)


1. Selecione "Tipo de pagamento" como "Pagamento"
2. Selecione "Tipo de parte" como "Fornecedor" e o fornecedor apropriado
3. Insira o valor pago, o valor pago deve ser o valor antes da dedução do TDS
4. Na seção Impostos e Taxas, marque "Aplicar valor de retenção de imposto" e selecione Categoria de retenção de imposto
5. Clique em Salvar. O TDS será aplicado automaticamente
6. Envie a entrada
7. O mesmo também ficará visível no relatório mensal a pagar do TDS


### 3.3 Configuração do TCS-Seção 20C(1H) para clientes qualificados


No exemplo a seguir, criamos uma categoria de retenção de imposto para [TCS-Seção 20C(1H)](https://taxguru.in/income-tax/faqs-tcs-sales-goods-section-206c1h.html) e configurá-la para um cliente qualificado.


1. Primeiro criaremos uma categoria de retenção de imposto chamada **TCS-Seção 20C(1H)** e definiremos o limite cumulativo para 50 Lakhs de acordo com o esquema.


![Categoria de retenção de imposto para TCS](/files/tax-withholding-category-for-tcs.png)


1. Se for esperado que um **cliente** ultrapasse o limite de vendas de 50 Lakh no ano fiscal atual, podemos definir a categoria de retenção de imposto do cliente como TCS-Seção 20C(1H) para cálculo automático do TCS na venda de mercadorias em relação às faturas do cliente.


![TCS no cliente](/files/tcs-eligible-customer.png)
2. Vamos criar uma fatura de 50 Lakhs para o cliente qualificado. Salvar a fatura calcula automaticamente o imposto e o anexa à tabela de impostos.


![Cálculo de TCS na fatura de vendas](/files/tcs-invoice.png)


Como a fatura ultrapassa o limite cumulativo (50 Lakhs), vemos que o imposto foi cobrado. Portanto, o imposto baseado na alíquota fornecida na **categoria de retenção de imposto** é aplicado adequadamente. Observe que, de acordo com o esquema, o TCS é calculado sobre o valor que excede o limite, ou seja, 0,075% de 10 Lakhs.


### 3.4 Opções avançadas na categoria de retenção de impostos


![Opções avançadas de TDS](/files/tds-advance-options.png)


1. **Considere o valor total do razão da parte**: Em muitas situações, o limite deve ser calculado sobre o valor total do razão da parte, em vez da soma do total líquido de faturas específicas. Ao ativar esta verificação, o limite cumulativo será verificado em relação à soma do total geral de todas as faturas de um fornecedor/cliente específico.
2. **Deduzir apenas imposto sobre valor excedente**: Ao ativar este imposto será deduzido apenas sobre o valor que exceder o limite e não o valor total. Por exemplo, se o limite cumulativo for 50.000 e se o valor acumulado for até 52.000, o imposto será aplicado apenas sobre 2.000 e não sobre todos os 52.000.
3. **Arredondar valor do imposto**: ativar esta verificação arredondará o valor do imposto calculado para o valor inteiro mais próximo (método de arredondamento normal)


### 4. Tópicos Relacionados


1. [Regra tributária](/docs/pt/accounts/tax-rule)
2. [Fornecedor](/docs/pt/buying/supplier)
3. [Cliente](/docs/pt/CRM/customer)



