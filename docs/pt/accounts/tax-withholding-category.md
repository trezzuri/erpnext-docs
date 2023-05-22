# Categoria de Retenção de Impostos


**Categoria de Retenção de Imposto é Imposto Deduzido na Fonte.**


De acordo com este, a pessoa responsável pelos pagamentos é obrigada a reter o imposto na fonte às taxas prescritas. Em vez de receber impostos sobre sua renda em uma data posterior, o governo deseja que os contribuintes deduzam o imposto antecipadamente e o depositem no governo.


Para acessar a lista de categorias de retenção de impostos, acesse:



> 
> Página inicial > Contabilidade > Impostos > Categoria de retenção de impostos
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma Categoria de Retenção de Imposto, é recomendável criar primeiro o seguinte:


1. [Fornecedor](/docs/pt/buying/supplier)
2. [Cliente](/docs/pt/CRM/customer)


## 2. Como criar uma categoria de retenção de imposto


No ERPNext, as Categorias de Retenção de Impostos para a maioria dos casos estão disponíveis por padrão, no entanto, você pode criar mais, se necessário.


1. Vá para a lista Categoria de retenção de impostos e clique em Novo.
2. Insira um nome exclusivo, por exemplo: Seção 194C Individual.
3. Insira um nome de categoria (dividendos, honorários profissionais etc.).
4. Insira uma taxa de retenção de imposto em relação a um [ano fiscal](/docs/pt/accounts/fiscal-year).
5. Você pode definir o limite para uma única fatura ou a soma de todas as faturas.
6. Selecione uma conta contra sua empresa na qual o imposto será creditado.
7. Adicione mais empresas e contas conforme necessário.
8. Salvar.


![Categoria de retenção de impostos](/files/tax-withholding-category.png)


Nos detalhes da contabilidade, a conta TDS é adicionada para cada empresa no sistema.


### 2.1 Atribuição de retenção de impostos ao fornecedor


Depois de salvar, pode ser atribuído a um Fornecedor:


![Categoria de retenção de impostos no fornecedor](/files/tax-withholding-category-in-supplier.png)


### 2.2 Como funciona o limite?


Considere um Fornecedor ao qual uma Categoria de Retenção de Imposto é aplicada.


Por exemplo, digamos que uma taxa de 5% será aplicável na fatura em que o Limite único é 20.000 e o Limite cumulativo é 30.000. Se uma fatura for criada com um total geral de 20.000, o limite único será acionado e um imposto de 5% será cobrado.


Mas se o valor da fatura totalizar 15.000, nenhum imposto será cobrado, pois não ultrapassou o limite. Se novamente outra fatura for criada contra o mesmo fornecedor com um total de 15.000, embora não ultrapasse o limite Único, os encargos serão deduzidos desde a soma da última fatura e esta fatura soma 30.000, o que é igual ao limite cumulativo especificado.


## 3. Usando a retenção de impostos


### 3.1 Uso na fatura de compra


No exemplo a seguir, selecionamos 'TDS - 194C - Individual', que tem um limite único de 30.000, limite cumulativo de 1.00.000 e taxa de 1%.


1. Se o **Fornecedor** tiver o campo de retenção de imposto definido, ao selecionar esse Fornecedor, uma caixa de seleção ficará visível na Fatura de compra para selecionar se o imposto será aplicado ou não.


![Categoria de retenção de imposto na fatura de compra](/files/tax-withholding-category-in-purchase-invoice.png)


1. Vamos criar uma fatura de 90.000. Salvar a fatura calcula automaticamente o imposto e o anexa à tabela de impostos.


![Categoria de retenção de imposto na fatura de compra](/files/withheld-tax-calculation-in-purchase-invoice.png)
2. Para ver o efeito do Limite cumulativo, vamos criar uma fatura com valor de 10.000 e enviá-la.


![Limite cumulativo da categoria de retenção na fonte](/files/tax-withholding-category-cumulative-threshold.png)


Embora o valor da fatura não ultrapasse o limite Único (30.000), vemos que o imposto foi cobrado. Isso ocorre porque a fatura anterior e a atual somam 1.10.000, o que excede o limite cumulativo. Portanto, o imposto com base na alíquota fornecida na **Categoria de Retenção de Impostos** é aplicado de acordo.



> 
> Observação: Ao enviar a fatura, três entradas contábeis são criadas:
> 
> 
> 



> 
> 1. Primeiro para débito da cabeça de despesas
> 2. Segundo para crédito na conta do Credor
> 3. Terceiro para crédito na conta selecionada na categoria de retenção de impostos.
> 
> 
> 


### 3.2 Dedução de imposto na fonte sobre adiantamentos


#### 3.2.1 Adiantamento de Dedução TDS contra Pedido de Compra


1. Configurar a Categoria de Retenção de Imposto contra o fornecedor e fazer um Pedido de Compra contra o fornecedor. Um ponto a ser lembrado aqui é não marcar o cheque "Aplicar retenção de imposto" na PO, pois a PO deve gerar o valor total
2. Crie uma entrada de pagamento para esse pedido de compra. Na seção Impostos e cobranças, ative "Aplicar retenção de impostos" e insira outros detalhes, salve e envie a entrada.


![Entrada de pagamento retido na fonte](/files/Tax-Withholding-Payment Entry.png)


3. Crie uma Fatura de Compra para este pedido e ative "Definir Adiantamentos e Alocar (FIFO)" para que o pagamento vinculado ao pedido correspondente seja aplicado automaticamente. Nenhum Imposto será retido na Fatura de Compra se o Imposto pago antecipadamente for maior ou igual ao valor do imposto na Fatura. O imposto será retido apenas pelo valor em excesso, se aplicável.


### 3.2.2 Dedução de TDS contra adiantamentos pagos (usando entrada de pagamento)


1. Selecione "Tipo de pagamento" como "Pagamento"
2. Selecione "Tipo de Parte" como "Fornecedor" e o fornecedor apropriado
3. Insira o valor pago, o valor pago deve ser o valor antes da dedução do TDS
4. Na seção Impostos e cobranças, marque "Aplicar valor de retenção de imposto" e selecione Categoria de retenção de imposto
5. Clique em Salvar. O TDS será aplicado automaticamente
6. Enviar a entrada
7. O mesmo também ficará visível no relatório mensal a pagar do TDS


### 3.3 Configuração do TCS - Seção 20C(1H) para clientes elegíveis


No exemplo a seguir, criamos uma categoria de retenção de imposto para [TCS - Seção 20C(1H)](https://taxguru.in/income-tax/faqs-tcs-sales-goods-section-206c1h.html) e configurá-lo contra um cliente elegível.


1. Primeiro criaremos uma categoria de retenção de imposto chamada **TCS - Seção 20C(1H)** e definiremos o limite cumulativo para 50 Lakhs de acordo com o esquema.


![Categoria de retenção de impostos para TCS](/files/tax-withholding-category-for-tcs.png)


1. Se espera-se que um **Cliente** ultrapasse o limite de vendas de 50 Lakh no ano fiscal atual, podemos definir a Categoria de Retenção de Imposto do cliente como TCS - Seção 20C(1H) para calcular automaticamente o TCS na venda de mercadorias contra as faturas do cliente.


![TCS no cliente](/files/tcs-eligible-customer.png)
2. Vamos criar uma fatura de 50 Lakhs contra o cliente qualificado. Salvar a fatura calcula automaticamente o imposto e o anexa à tabela de impostos.


![Cálculo de TCS na fatura de vendas](/files/tcs-invoice.png)


Como a fatura ultrapassou o limite cumulativo (50 Lakhs), vemos que o imposto foi cobrado. Portanto, o imposto com base na alíquota fornecida na **Categoria de Retenção de Impostos** é aplicado de acordo. Observe que, de acordo com o esquema, o TCS é calculado sobre o valor que excede o limite, ou seja, 0,075% de 10 Lakhs.


### 3.4 Opções avançadas na categoria de retenção de impostos


![Opções avançadas de TDS](/files/tds-advance-options.png)


1. **Considere o valor total do livro-razão**: em muitas situações, o limite deve ser calculado com base no valor total do livro-razão, em vez da soma do total líquido de faturas específicas. Ao ativar esta verificação, o limite cumulativo será verificado em relação à soma do total geral de todas as faturas de um Fornecedor/Cliente específico.
2. **Deduzir apenas o imposto sobre o valor em excesso**: Ao habilitar este imposto, será deduzido apenas o valor que exceder o limite e não o valor total. Por exemplo, se o limite cumulativo for 50.000 e se o valor cumulativo for até 52.000, o imposto será aplicado apenas em 2.000 e não em todo o 52.000.
3. **Arredondamento do valor do imposto**: habilitar esta verificação arredondará o valor do imposto calculado para o valor inteiro mais próximo (método de arredondamento normal)


### 4. Tópicos Relacionados


1. [Regra fiscal](/docs/pt/accounts/tax-rule)
2. [Fornecedor](/docs/pt/buying/supplier)
3. [Cliente](/docs/pt/CRM/customer)
