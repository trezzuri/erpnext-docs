# Cobrança



**Um documento a ser enviado como uma exigência persistente de pagamento de dívida.**


A cobrança é um documento para armazenar e enviar como uma demanda persistente de pagamento de dívida contra uma fatura de venda não paga.


Para acessar a lista de cobranças, acesse:



> 
> Página inicial > Contabilidade > Cobrança
> 
> 
> 


## 1. Pré-requisitos


* [Fatura de vendas](/docs/pt/accounts/sales-invoice)


Uma cobrança só pode ser criada em relação a uma fatura de vendas vencida.
* Tipo de cobrança


Um **Tipo de cobrança** é usado para preencher previamente juros, taxas e blocos de texto em uma nova **cobrança**.


## 2. Como criar uma cobrança


Uma cobrança é criada com base em uma lista de pagamentos programados em atraso. Você pode criar uma cobrança de duas maneiras diferentes:


### a) Criar uma nova cobrança


1. Vá para a lista de **Cobranças** e clique em "Adicionar cobranças".
2. Selecione um **Cliente** e clique em "Obter Pagamentos Atrasados". Isso mostrará uma lista de faturas de vendas vencidas para este cliente. Selecione aqueles que você gostaria de buscar nesta **cobrança** e clique em "Obter itens".


### b) Criar uma cobrança a partir de uma fatura de vendas vencida


1. Vá para a lista de **Faturas de Vendas** e abra qualquer **Fatura de Vendas** vencida.
2. Clique em "Criar > Cobrança". Isso buscará todos os pagamentos vencidos da tabela de programação de pagamentos da fatura em uma nova **cobrança**.


### Preencha os campos restantes


1. Selecione um **Tipo de cobrança** para preencher juros, taxas de cobrança e blocos de texto com valores predeterminados. Ou você também pode definir esses valores manualmente.
2. Você já pode definir uma **Conta** de receita (por exemplo, "Outros juros e receitas similares") e um **Centro de Custo** para a receita gerada por juros e taxas de cobrança. Eles serão usados ​​quando uma **Entrada de Pagamento** for criada a partir desta **Cobrança**.
3. Salve e envie a **Cobrança** antes de enviá-la ao **Cliente**.


![Exemplo de cobrança](/files/dunning9768a2.png)


### 2.1 O que é um tipo de cobrança


O tipo de cobrança armazena valores padrão para taxa de cobrança, taxa de juros e blocos de texto a serem incluídos. Por exemplo, um tipo de cobrança "Primeiro aviso" não terá nenhuma taxa, mas o tipo de cobrança "Segundo aviso" terá uma taxa de cobrança e juros cobrados sobre o valor pendente.


![Tipo de cobrança](/files/first_dunning.png)


### 2.2 Status


Esses são os status atribuídos automaticamente à cobrança.


* **Rascunho**: um rascunho foi salvo, mas ainda não foi enviado.
* **Não resolvido**: a cobrança não foi resolvida quando é enviada, mas nenhum pagamento foi recebido.
* **Resolvido**: a cobrança será resolvida quando o pagamento pendente for recebido.
* **Cancelado**: um status cancelado é um documento de cobrança cancelado.


## 3. Pagamento


Quando você receber o pagamento integral, incluindo juros e taxas, abra a **cobrança** não resolvida e clique em "Criar > Pagamento". Isto criará uma **Entrada de Pagamento** contra os pagamentos programados pendentes e registrará os juros e taxas como "Deduções ou Perdas de Pagamento". A **entrada de pagamento** definirá automaticamente o status da **cobrança** como resolvido.


![Dunning Payment](/files/dunning_payment_entry.png)


## 4. Tópicos Relacionados


1. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
2. [Fatura de vendas](/docs/pt/accounts/purchase-invoice)



