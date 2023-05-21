# Cobrança


**Um documento a ser enviado como um pedido persistente de pagamento da dívida.**


Cobrança é um documento para armazenar e enviar como uma demanda persistente de pagamento de dívida contra uma Nota Fiscal de Venda não paga.


Para acessar a lista de Cobranças, acesse:



>
> Início > Contabilidade > Cobrança
>
>
>


## 1. Pré-requisitos


* [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura-de-venda)


Uma cobrança só pode ser criada em relação a uma fatura de venda vencida.
* Tipo de Cobrança


Um **Tipo de advertência** é usado para pré-preencher juros, taxas e blocos de texto em um novo **Dunning**.


## 2. Como criar uma Cobrança


Uma Cobrança é criada em relação a uma lista de pagamentos programados atrasados. Você pode criar uma cobrança de duas maneiras diferentes:


### a) Criar uma nova Cobrança


1. Vá para a lista **Cobrança** e clique em "Adicionar Cobrança".
2. Selecione um **Cliente** e clique em "Buscar pagamentos atrasados". Isso mostrará uma lista de faturas de vendas vencidas para este cliente. Selecione aqueles que você gostaria de buscar neste **Dunning** e clique em "Obter itens".


### b) Criar uma cobrança a partir de uma fatura de venda vencida


1. Vá para a lista **Fatura de Venda** e abra qualquer **Fatura de Venda** vencida.
2. Clique em "Criar > Cobrança". Isso buscará todos os pagamentos vencidos da tabela de programação de pagamentos da fatura em uma nova **Cobrança**.


### Preencha os restantes campos


1. Selecione um **Tipo de Cobrança** para preencher juros, taxas de cobrança e blocos de texto com valores predeterminados. Ou você também pode definir esses valores manualmente.
2. Você já pode definir uma **Conta** de receita (por exemplo, "Outros juros e receitas similares") e um **Centro de custos** para a receita gerada por juros e taxas de cobrança. Eles serão usados ​​assim que uma **Entrada de pagamento** for criada a partir desta **Cobrança**.
3. Salve e envie a **Cobrança** antes de enviá-la ao **Cliente**.


![Exemplo de cobrança](/files/dunning9768a2.png)


### 2.1 O que é um Tipo de Cobrança


Tipo de cobrança armazena valores padrão para taxa de cobrança, taxa de juros e blocos de texto a serem incluídos. Por exemplo, um Tipo de Cobrança "Primeiro Aviso" não terá nenhuma taxa, mas o Tipo de Cobrança "Segundo Aviso" terá uma taxa de cobrança e juros cobrados sobre o valor pendente.


![Tipo de Cobrança](/files/first_dunning.png)


### 2.2 Situações


Esses são os status atribuídos automaticamente a Cobrança.


* **Rascunho**: Um rascunho foi salvo, mas ainda não foi enviado.
* **Não resolvido**: A cobrança não foi resolvida quando foi enviada, mas nenhum pagamento foi recebido.
* **Resolvido**: A Cobrança é resolvida quando o pagamento pendente for recebido.
* **Cancelado**: Um status cancelado é um documento de cobrança cancelado.


## 3. Pagamento


Quando você receber um pagamento integral, incluindo juros e taxas, abra a **Cobrança** não resolvida e clique em "Criar > Pagamento". Isso criará uma **Entrada de Pagamento** contra os pagamentos agendados pendentes e registrará os juros e taxas como "Deduções ou Perdas de Pagamento". A **Entrada de pagamento** definirá automaticamente o status da **Cobrança** como resolvido.


![Pagamento de Cobrança](/files/dunning_payment_entry.png)


## 4. Tópicos Relacionados


1. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
2. [Fatura de venda](/docs/v13/user/manual/en/accounts/purchase-invoice)