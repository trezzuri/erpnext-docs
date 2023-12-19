# Código de cupom



**O código do cupom permite que um cliente aproveite descontos em produtos do carrinho de compras.**


Todo mundo adora descontos! o mesmo acontece com os cupons que oferecem esses descontos. Para incentivar os clientes a comprar no site de comércio eletrônico,
O recurso de código de cupom é interessante.


Existem revendedores/outros sites que geram leads para os produtos/itens/serviços do seu site de comércio eletrônico ERPNext.


Quando o cliente potencial vem de outros sites OU e-mails promocionais para o seu site ERPNext para compra, você deve ser capaz de:



```
a) Rastreie de qual afiliado/parceiro de vendas o lead está vindo, ou seja, [código de referência]
(/docs/pt/selling/sales-partner)

b) Dê desconto (com base na regra de preços) na compra geral, ou seja, código do cupom

```

Para acessar a lista de códigos de cupom, acesse:


> Página inicial > Contabilidade > Código do cupom


## 1. Pré-requisitos


1. Para ativar o recurso Código de cupom, ative **Mostrar aplicar código de cupom** em **Configurações de comércio eletrônico**.
2. Crie uma regra de preços com o sinalizador **Baseado em código de cupom** ativado.


## 2. Como criar um código de cupom


1. Vá para a lista de códigos de cupom e clique em Novo.
2. Insira um **Nome do cupom**, por exemplo "ECONOMIZE 20"
3. Em **Tipo de cupom**, selecione Promocional ou Vale-presente.


Promocional, é promover um esquema genérico.


Vale-presente, serve para gerar aleatoriamente um código de cupom e distribuí-lo para um cliente/usuário específico.
4. **Código de cupom** é um código exclusivo somente leitura em letras maiúsculas, gerado com base no tipo e no nome do cupom.


Para tipo de cupom,


a) *Promocional* , remove todos os espaços e ocupa até os primeiros 8 caracteres. por exemplo. SALVE20


b) *GiftCard* , gera um código aleatório de 11 dígitos. por exemplo. AP48K7CT9LP


Ele pode ser usado na página do carrinho de compras antes de fazer o pedido para obter desconto.
5. Selecione [Regra de preços](/docs/pt/accounts/pricing-rule) com o sinalizador **baseado em código de cupom** ativado.
6. Clique em Salvar


![Doctype do código de cupom](/files/coupon-code.png)


## 3. Recursos


### 3.1 Validade e uso


1. **Válido de-até**-validade do cupom
2. **Uso Máximo**-Limite para limitar o uso do código do cupom
3. **Usado**-para cada pedido de vendas enviado com código de cupom , a contagem usada aumenta em 1.
4. **Descrição do código do cupom**-pode ser usado durante a criação do modelo de e-mail para informar clientes em potencial sobre o código do cupom e informações do esquema


![Regra de preços baseada em código de cupom](/files/coupon-code-pricing-rule.png)


### 3.2 O código do cupom pode ser aplicado de duas maneiras


1. Através do URL, o código do cupom será obtido automaticamente do parâmetro URL ("cc") e preenchido na caixa de texto Aplicar código de cupom, para facilitar a aplicação pelo usuário.


http://xyz.erpnext.com/products/golden-ring?cc=SAVE5
2. Aplicar explicitamente o código, preenchendo o código e clicando no botão "Aplicar código de cupom", conforme mostrado abaixo na página do carrinho de compras


![Carrinho de compras Aplicar CouponCode](/files/coupon-code-pricing-rule.png)


O preço será atualizado após a aplicação bem-sucedida do código do cupom.


### 4. Tópicos Relacionados


1. [Carrinho de compras](/docs/pt/website/shopping-cart)
2. [Regra de preços](/docs/pt/accounts/pricing-rule)



