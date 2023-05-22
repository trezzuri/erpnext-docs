# Ponto de venda


**Um ponto de venda refere-se ao local e hora em que ocorre uma transação de varejo.**


Para operações de varejo, a entrega de mercadorias, o acúmulo de vendas e o pagamento acontecem em um único evento, geralmente chamado de 'Ponto de venda' (POS).


No ERPNext as Notas Fiscais podem ser geradas a partir do PDV. Existem duas etapas para configurar o PDV:


Para acessar o PDV, acesse:



> 
> Página inicial > Varejo > Operações de varejo > PDV
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e utilizar o Ponto de Venda, é aconselhável criar primeiro o seguinte:


1. [Perfil PDV](/docs/pt/accounts/pos-profile)


## 2. Como criar uma fatura PDV


Depois de configurar um perfil de PDV, você pode começar a faturar no PDV.


1. Vá para PDV e selecione um cliente.
2. Adicione itens da lista exibida à direita clicando neles.
3. Certifique-se de que o item tenha um preço de venda definido na lista de preços do item.
4. Edite as quantidades conforme necessário.
5. Para editar Tarifa e Desconto, você precisa ativá-los no Perfil PDV.
6. Um depósito padrão precisa ser definido para concluir a transação. Se o Armazém for definido no perfil de Item e PDV, o perfil PDV terá preferência.
7. Observe que você precisa ter itens em seu Armazém antes de poder vender. Se os itens não estiverem disponíveis, um ponto vermelho será mostrado ao lado do item quando selecionado. ![POS Screen](/files/pos-screen.png)
8. Quando todos os itens forem adicionados, verifique os totais líquido e geral e também a quantidade total no resumo na parte inferior. ![Resumo dos Totais POS](/files/totals display.gif)
9. Selecione a forma de pagamento e clique em Finalizar Pedido. Você será solicitado a enviar a fatura de venda.
10. Você pode então imprimir a fatura do PDV. ![POS Checkout](/files/pos-checkout.gif)


Após o envio da fatura de venda, você pode imprimi-la ou enviá-la por e-mail diretamente ao cliente.


### 2.2 Adicionar um item


No balcão de cobrança, o varejista precisa selecionar os itens que o cliente compra. Na interface POS, você pode selecionar um Item por dois métodos. Uma, é clicando na imagem do Item e a outra, é através do Código de Barras/Número de Série


1. **Selecionar item**: Para selecionar um produto, clique na imagem do item e adicione-o ao carrinho. Um carrinho é uma área que prepara um cliente para finalizar a compra, permitindo editar informações do produto, ajustar impostos e adicionar descontos.
2. **Código de barras/número de série**: um código de barras/número de série é uma representação ótica legível por máquina de dados relacionados ao objeto ao qual está anexado.
3. ![](/files/BczEpbC.png)
4. Digite o código de barras / número de série na caixa conforme mostrado na imagem abaixo e espere um segundo, o item será adicionado automaticamente ao carrinho.



> 
> Dica: Para alterar a quantidade de um Item, insira a quantidade desejada na caixa de quantidade. Eles são usados ​​principalmente se o mesmo item for comprado em massa.
> 
> 
> 


Se sua lista de produtos for muito longa, use o campo de pesquisa, digite o nome do produto na caixa de pesquisa.


### 2.3 Removendo um item do carrinho


1. Selecione a linha no carrinho e clique no botão 'Remover' no teclado numérico
2. ![Remover item do PDV](/files/remove-item-from-pos.png)
3. Defina a Qtd como zero para remover o item da fatura do PDV. Existem duas maneiras de remover um item.
4. Se a quantidade do item for 1, clique no sinal de menos para zerar.
5. Insira manualmente a quantidade 0 (zero).


### 2.4 Alterar valor


O POS calcula o valor extra pago pelo cliente, que o usuário pode devolver da conta de caixa. O usuário deve definir a conta para o valor do troco no perfil PDV.


![Change Amount in POS](/files/change-amount-in-pos.png)


## 3. Recursos


### 3.1 Adicionar um novo cliente


No PDV, o usuário pode selecionar o Cliente existente ao fazer um pedido ou criar um novo cliente. Esse recurso também funciona no modo offline. O usuário também pode adicionar os detalhes do cliente, como número de contato, detalhes do endereço, etc., no formulário. O Cliente criado a partir do PDV será sincronizado quando a conexão com a Internet estiver ativa.


![Adicionar novo cliente no PDV](/files/pos-add-new-customer.gif)


### 3.2 Lançamentos contábeis (entrada contábil) para um ponto de venda:


Débitos:


1. Cliente (total geral)
2. Banco/Dinheiro (pagamento)


Créditos:


1. Receita (total líquido, menos impostos para cada item)
2. Impostos (obrigações a serem pagas ao governo)
3. Cliente (pagamento)
4. Anulação (opcional)
5. Conta para alterar o valor (opcional)


Para ver as entradas após enviar a [Fatura de vendas](/docs/pt/accounts/sales-invoice), clique em **Exibir razão** .


### 3.3 E-mail


Você também pode enviar o recibo por e-mail.


![Enviar e-mail com recibo do PDV](/files/pos-email.png)


### 3.4 Criar nota de crédito de devolução


Você também pode criar uma nota de crédito de devolução contra uma fatura de PDV em caso de devolução de itens ou de todo o pedido. Abaixo estão as etapas para emitir uma nota de crédito contra uma fatura:


1. Clique no menu (3 pontos) e depois clique em **Alternar pedidos recentes**. O atalho de teclado para o mesmo é **⌘+O**.
![POS Return Credit Open Recent Orders](/files/pos-return-credit-1.png)
2. Todas as faturas de transações recentes de PDV serão exibidas no painel **Pedidos recentes**. Você pode pesquisar a fatura diretamente com seu nome ou filtrar os resultados da pesquisa de acordo com o status da fatura, que pode ser **Pago, Consolidado, Rascunho, Devolução**.
3. Selecione a fatura contra a qual você precisa criar a nota de crédito, após a qual você verá os detalhes da fatura e as opções para imprimir, enviar o recibo por e-mail e uma opção para fazer uma devolução. Clique em **'Devolver'**.
![POS Return Credit Select Invoice](/files/pos-return-credit-2.png)
4. A tela do PDV exibirá os itens da nota fiscal, juntamente com as respectivas quantidades negativas e totais no Carrinho de itens, indicando que é uma nota de crédito de devolução.
![Tela de carrinho de item de crédito de devolução POS](/files/pos-return-credit-3.png)
5. Depois de finalizar a compra, você verá o total geral, o valor pago e os impostos, se aplicável.
6. Clicar em **Concluir pedido** concluirá o processo e criará a fatura final de crédito de devolução e exibirá a fatura na tela como um pedido normal
![POS-Return Credit Credit Final Bill](/files/pos-return-credit-4.png)


### 3.5 Voucher de fechamento de PDV


Ao final do dia, o caixa pode fechar seu PDV criando um Voucher de Fechamento de PDV. Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu Perfil de PDV e seu usuário para recuperar todas as vendas registradas.
Ao final do dia, o caixa pode fechar seu turno criando um Voucher de Fechamento de PDV.


Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu perfil de PDV e seu usuário para recuperar todas as vendas registradas.


Ao criar um Voucher de Fechamento de PDV, todas as faturas de PDV obtidas para o período selecionado serão consolidadas em uma Fatura de Venda final. O status de todas as faturas de PDV mudará de 'Pago' para 'Consolidado' assim que forem consolidadas com sucesso em uma fatura de venda no fechamento.


![POS Closing Entry](/files/pos-closing-entry.png)


Se houver mais de 10 faturas ao fechar um PDV, a consolidação das faturas ocorrerá em um trabalho em segundo plano e será enviada após a conclusão do trabalho em segundo plano. Os Livros Contábeis seriam afetados somente após o Comprovante de Fechamento ser enviado com sucesso e as faturas de vendas consolidadas serem criadas.


### 4. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Pedido de compra](/docs/pt/buying/purchase-order)
3. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
4. [Solicitação de pagamento](/docs/pt/accounts/payment-request)
