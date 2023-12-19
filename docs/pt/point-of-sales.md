# Ponto de venda



**Um ponto de venda refere-se à hora e ao local onde ocorre uma transação de varejo.**


Para operações de varejo, a entrega da mercadoria, o acúmulo da venda e o pagamento acontecem em um único evento, normalmente chamado de 'Ponto de Venda' (PDV).


No ERPNext as faturas de vendas podem ser geradas a partir do PDV. Existem duas etapas para configurar o PDV:


Para acessar o PDV, acesse:



> 
> Home > Varejo > Operações de Varejo > PDV
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e utilizar Ponto de Venda, é aconselhável criar primeiro o seguinte:


1. [Perfil de PDV](/docs/pt/accounts/pos-profile)


## 2. Como criar uma fatura de PDV


Depois de configurar um perfil de PDV, você poderá começar a faturar no PDV.


1. Acesse o PDV e selecione um cliente.
2. Adicione itens da lista exibida à direita clicando neles.
3. Certifique-se de que o item tenha um preço de venda definido na lista de preços do item.
4. Edite as quantidades conforme necessário.
5. Para editar Taxa e Desconto, você precisa habilitá-los no Perfil do PDV.
6. Um armazém padrão precisa ser definido para concluir a transação. Se o Armazém estiver definido no perfil Item e PDV, aquele no Perfil PDV terá preferência.
7. Observe que você precisa ter itens em seu armazém antes de poder vender. Se os itens não estiverem disponíveis, um ponto vermelho será mostrado próximo ao item quando selecionado. ![Tela POS](/files/pos-screen.png)
8. Quando todos os itens forem adicionados, verifique os totais líquidos e gerais e também a quantidade total no resumo na parte inferior. ![Resumo dos totais do PDV](/files/totals display.gif)
9. Selecione a forma de pagamento e clique em Concluir pedido. Você será solicitado a enviar a fatura de vendas.
10. Você pode então imprimir a fatura do PDV. ![POS Checkout](/files/pos-checkout.gif)


Depois que a fatura de vendas for enviada, você poderá imprimi-la ou enviá-la por e-mail diretamente ao cliente.


### 2.2 Adicionando um item


No balcão de cobrança, o varejista precisa selecionar os Itens que o Cliente compra. Na interface do PDV você pode selecionar um item por dois métodos. Uma, é clicando na imagem do Item e a outra, é através do Código de Barras/Número de Série.


1. **Selecionar Item**: Para selecionar um produto clique na imagem do Item e adicione-o ao carrinho. Um carrinho é uma área que prepara o cliente para a finalização da compra, permitindo editar informações do produto, ajustar impostos e adicionar descontos.
2. **Código de barras/Número de série**: Um código de barras/Número de série é uma representação óptica legível por máquina de dados relacionados ao objeto ao qual está anexado.
3. ![](/files/BczEpbC.png)
4. Insira o código de barras/número de série na caixa conforme mostrado na imagem abaixo e pause por um segundo, o item será adicionado automaticamente ao carrinho.



> 
> Dica: para alterar a quantidade de um item, insira a quantidade desejada na caixa de quantidade. Eles são usados ​​principalmente se o mesmo item for comprado a granel.
> 
> 
> 


Se a sua lista de produtos for muito longa, use o campo Pesquisar e digite o nome do produto na caixa Pesquisar.


### 2.3 Removendo um item do carrinho


1. Selecione a linha no carrinho e clique no botão 'Remover' no teclado numérico
2. ![Remover item do PDV](/files/remove-item-from-pos.png)
3. Defina a Quantidade como zero para remover o Item da fatura do PDV. Existem duas maneiras de remover um item.
4. Se a quantidade do item for 1, clique no sinal de menos para zerá-la.
5. Insira manualmente a quantidade 0 (zero).


### 2.4 Valor da alteração


O PDV calcula o valor extra pago pelo cliente, que o usuário pode devolver da conta à vista. O usuário deve definir a conta para o valor da alteração no perfil do PDV.


![Alterar valor no PDV](/files/change-amount-in-pos.png)


## 3. Recursos


### 3.1 Adicionando um novo cliente


No PDV, o usuário pode selecionar o Cliente existente ao fazer um pedido ou criar um novo cliente. Este recurso também funciona no modo offline. O usuário também pode adicionar os detalhes do cliente, como número de contato, detalhes de endereço, etc. no formulário. O Cliente criado a partir do POS será sincronizado quando a ligação à Internet estiver ativa.


![Adicionar novo cliente no PDV](/files/pos-add-new-customer.gif)


### 3.2 Lançamentos contábeis (entrada GL) para um ponto de venda:


Débitos:


1. Cliente (total geral)
2. Banco/Dinheiro (pagamento)


Créditos:


1. Renda (total líquido, menos impostos para cada item)
2. Impostos (passivos a serem pagos ao governo)
3. Cliente (pagamento)
4. Baixa (opcional)
5. Conta para valor de alteração (opcional)


Para ver as entradas após enviar a [fatura de vendas](/docs/pt/accounts/sales-invoice), clique em **Ver razão** .


### 3.3 E-mail


Você também pode enviar o recibo por e-mail.


![Enviar e-mail com recibo de PDV](/files/pos-email.png)


### 3.4 Criar nota de crédito de devolução


Você também pode criar uma nota de crédito de devolução em uma fatura de PDV em caso de devolução de itens ou de todo o pedido. Abaixo estão as etapas para emitir uma nota de crédito contra uma fatura:


1. Clique no menu (3 pontos) e depois clique em **Alternar pedidos recentes**. O atalho de teclado para o mesmo é **⌘+O**.
![POS Devolução de Crédito Aberto Pedidos Recentes](/files/pos-return-credit-1.png)
2. Todas as faturas de transações recentes de PDV serão exibidas no painel **Pedidos recentes**. Você pode pesquisar a fatura diretamente com seu nome ou filtrar os resultados da pesquisa de acordo com o status da fatura, que pode ser **Paga, Consolidada, Rascunho, Devolvida**.
3. Selecione a fatura contra a qual você precisa criar a nota de crédito, após a qual você verá os detalhes da fatura e as opções para imprimir, enviar o recibo por e-mail e uma opção para fazer uma devolução. Clique em **'Retornar'**.
![POS Return Credit Select Invoice](/files/pos-return-credit-2.png)
4. A tela do PDV exibirá os itens da fatura, juntamente com as respectivas quantidades negativas e totais no Carrinho de Itens o que indica que se trata de uma nota de crédito de devolução.
![Tela do carrinho de item de crédito de devolução do PDV](/files/pos-return-credit-3.png)
5. Depois de finalizar a compra, você verá o total geral, o valor pago e os impostos, se aplicável.
6. Clicar em **Concluir pedido** concluirá o processo e criará a fatura de crédito de devolução final e exibirá a fatura na tela como um pedido normal
![Conta final de crédito de devolução de PDV](/files/pos-return-credit-4.png)


### 3.5 Voucher de fechamento de PDV


Ao final do dia, o caixa pode fechar seu PDV criando um Voucher de Fechamento de PDV. Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu perfil de PDV e seu usuário para recuperar todas as vendas registradas.
No final do dia, o caixa pode fechar o seu turno criando um Voucher de Fechamento do PDV.


Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu perfil de PDV e seu usuário para recuperar todas as vendas registradas.


Ao criar um Voucher de Fechamento de PDV, todas as faturas de PDV obtidas no período selecionado serão consolidadas em uma Fatura de Venda final. O status de todas as faturas de PDV mudará de 'Paga' para 'Consolidada' assim que forem consolidadas com sucesso em uma fatura de venda no fechamento.


![Entrada de fechamento de PDV](/files/pos-closing-entry.png)


Se houver mais de 10 faturas durante o fechamento de um PDV, a consolidação das faturas ocorrerá em um trabalho em segundo plano e será enviada após a conclusão do trabalho em segundo plano. Os livros contábeis seriam afetados somente depois que o comprovante de fechamento fosse enviado com sucesso e as faturas de vendas consolidadas fossem criadas.


### 4. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Pedido de compra](/docs/pt/buying/purchase-order)
3. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
4. [Solicitação de pagamento](/docs/pt/accounts/payment-request)



