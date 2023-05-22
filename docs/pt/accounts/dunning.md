# Reclamação


**Um documento a ser enviado como um pedido persistente de pagamento de dívida.**


Dunning é um documento para armazenar e enviar como uma solicitação persistente de pagamento de dívida contra uma fatura de venda não paga.


Para acessar a lista de cobranças, acesse:



> 
> Página inicial > Contabilidade > Cobrança
> 
> 
> 


## 1. Pré-requisitos


* [Fatura de vendas](/docs/pt/accounts/sales-invoice)


Uma cobrança só pode ser criada para uma fatura de vendas vencida.
* Tipo de Cobrança


Um **Tipo de Cobrança** é usado para pré-preencher juros, taxas e blocos de texto em um novo **Dunning**.


## 2. Como criar uma Cobrança


Uma Cobrança é criada em relação a uma lista de pagamentos programados atrasados. Você pode criar uma cobrança de duas maneiras diferentes:


### a) Criar uma nova Dunning


1. Vá para a lista **Cobrança** e clique em "Adicionar Cobrança".
2. Selecione um **Cliente** e clique em "Buscar pagamentos atrasados". Isso mostrará uma lista de faturas de vendas vencidas para este cliente. Selecione aqueles que você gostaria de buscar nesta **Cobrança** e clique em "Obter itens".


### b) Criar uma cobrança a partir de uma fatura de venda vencida


1. Vá para a lista **Fatura de venda** e abra qualquer **Fatura de venda** vencida.
2. Clique em "Criar > Cobrança". Isso buscará todos os pagamentos atrasados ​​da tabela de programação de pagamentos da fatura em uma nova **Cobrança**.


### Preencha os campos restantes


1. Selecione um **Tipo de advertência** para preencher juros, taxas de advertência e blocos de texto com valores predeterminados. Ou você também pode definir esses valores manualmente.
2. Você já pode definir uma **Conta** de receita (por exemplo, "Outros juros e receitas similares") e um **Centro de custo** para a receita gerada com juros e taxas de cobrança. Eles serão usados ​​assim que uma **Entrada de pagamento** for criada a partir desta **Cobrança**.
3. Salve e envie a **Cobrança** antes de enviá-la ao **Cliente**.


![Dunning example](/files/dunning9768a2.png)


### 2.1 O que é um tipo de cobrança


Tipo de cobrança armazena valores padrão para taxa de cobrança, taxa de juros e blocos de texto a serem incluídos. Por exemplo, um Tipo de Cobrança "Primeiro Aviso" não terá nenhuma taxa, mas o Tipo de Cobrança "Segundo Aviso" terá uma taxa de cobrança e juros cobrados sobre o valor pendente.


![Dunning Type](/files/first_dunning.png)


### 2.2 Status


Estes são os status que são atribuídos automaticamente à Cobrança.


* **Rascunho**: um rascunho foi salvo, mas ainda não foi enviado.
* **Não resolvido**: a Cobrança não foi resolvida quando foi enviada, mas nenhum pagamento foi recebido.
* **Resolvido**: a Cobrança é resolvida quando o pagamento pendente for recebido.
* **Cancelado**: um status cancelado é um documento de cobrança cancelado.


## 3. Pagamento


Ao receber um pagamento integral, incluindo juros e taxas, abra a **Cobrança** não resolvida e clique em "Criar > Pagamento". Isso criará uma **Entrada de pagamento** contra os pagamentos agendados pendentes e registrará os juros e taxas como "Deduções ou Perdas de Pagamento". A **Entrada de pagamento** definirá automaticamente o status da **Cobrança** como resolvida.


![Dunning Payment](/files/dunning_payment_entry.png)


## 4. Tópicos Relacionados


1. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
2. [Fatura de venda](/docs/pt/accounts/purchase-invoice)
