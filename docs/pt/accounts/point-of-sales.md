# Ponto de venda


**Um ponto de venda refere-se à hora e ao local em que ocorre uma transação de varejo.**


Para operações de varejo, a entrega de mercadorias, o acúmulo de vendas e o pagamento acontecem em um único evento, geralmente chamado de 'Ponto de Venda' (POS).


No ERPNext, as Notas Fiscais de Venda podem ser geradas a partir do PDV. Existem duas etapas para configurar o POS:


Para acessar o PDV, acesse:



>
> Home > Varejo > Operações de Varejo > PDV
>
>
>


## 1. Pré-requisitos


Antes de criar e utilizar Ponto de Venda, é aconselhável criar primeiro o seguinte:


1. [Perfil POS](/docs/v13/user/manual/en/accounts/pos-profile)


## 2. Como criar uma Fatura PDV


Depois de configurar um perfil de PDV, você pode começar a cobrar no PDV.


1. Vá para PDV e selecione um Cliente.
2. Adicione itens da lista exibida à direita clicando neles.
3. Certifique-se de que o Item tenha um Preço de Venda definido na lista de Preços do Item.
4. Edite as quantidades conforme necessário.
5. Para editar Tarifa e Desconto, é necessário habilitá-los no Perfil PDV.
6. Um depósito padrão precisa ser definido para concluir a transação. Se o Armazém for definido no perfil Item e PDV, o perfil PDV terá preferência.
7. Observe que você precisa ter itens em seu Armazém antes de poder vender. Se os itens não estiverem disponíveis, um ponto vermelho será mostrado ao lado do item quando selecionado. ![Tela POS](/files/pos-screen.png)
8. Quando todos os itens forem adicionados, verifique os totais líquidos e gerais e também a quantidade total no resumo na parte inferior. ![Resumo dos Totais POS](/files/totals display.gif)
9. Selecione a forma de pagamento e clique em Finalizar Pedido. Você será solicitado a enviar a Fatura de Vendas.
10. Você pode então imprimir a fatura do PDV. ![Checkout PDV](/files/pos-checkout.gif)


Após o envio da Fatura de Vendas, você pode imprimi-la ou enviá-la por e-mail diretamente ao cliente.


### 2.2 Adicionando um Item


No balcão de cobrança, o varejista precisa selecionar os itens que o cliente compra. Na interface POS, você pode selecionar um Item por dois métodos. Uma, é clicando na imagem do Item e a outra, é através do Código de Barras/Nº de Série.


1. **Selecionar item**: Para selecionar um produto, clique na imagem do item e adicione-o ao carrinho. Um carrinho é uma área que prepara um cliente para o checkout, permitindo editar informações do produto, ajustar impostos e adicionar descontos.
2. **Código de Barras/Nº de Série**: Um Código de Barras/Nº de Série é uma representação ótica legível por máquina de dados relacionados ao objeto ao qual está anexado.
3. ![](/files/BczEpbC.png)
4. Digite o código de barras / número de série na caixa conforme mostrado na imagem abaixo e espere um segundo, o item será adicionado automaticamente ao carrinho.



>
> Dica: Para alterar a quantidade de um Item, insira a quantidade desejada na caixa de quantidade. Eles são usados ​​principalmente se o mesmo item for comprado em massa.
>
>
>


Se sua lista de produtos for muito longa, use o campo Pesquisar, digite o nome do produto na caixa Pesquisar.


### 2.3 Removendo um Item do Carrinho


1. Selecione a linha no carrinho e clique no botão 'Remover' no teclado numérico
2. ![Remove Item From POS](/files/remove-item-from-pos.png)
3. Defina Qty como zero para remover Item da fatura do PDV. Existem duas maneiras de remover um item.
4. Se a quantidade do item for 1, clique no sinal de menos para zerar.
5. Insira manualmente a quantidade 0 (zero).


### 2.4 Valor da Alteração


O PDV calcula o valor extra pago pelo cliente, que o usuário pode devolver da conta caixa. O usuário deve definir a conta para o valor da alteração no perfil do PDV.


![Change Amount in POS](/files/change-amount-in-pos.png)


## 3. Características


### 3.1 Adicionando um novo cliente


No PDV, o usuário pode selecionar o Cliente existente ao fazer um pedido ou criar um novo cliente. Esse recurso também funciona no modo offline. O usuário também pode adicionar os detalhes do cliente, como número de contato, detalhes do endereço, etc., no formulário. O Cliente criado a partir do PDV será sincronizado quando a conexão com a internet estiver ativa.


![Adicionar novo cliente no PDV](/files/pos-add-new-customer.gif)


### 3.2 Lançamentos Contábeis (Entrada Contábil) para um Ponto de Venda:


Débitos:


1. Cliente (total geral)
2. Banco/Dinheiro (pagamento)


Créditos:


1. Receita (total líquido, menos impostos para cada item)
2. Impostos (obrigações a pagar ao governo)
3. Cliente (pagamento)
4. Cancelar (opcional)
5. Conta para o valor da alteração (opcional)


Para ver as entradas depois de enviar a [Fatura de vendas](/docs/v13/user/manual/en/accounts/sales-invoice), clique em **View Ledger**.


### 3.3 E-mail


Você também pode enviar o comprovante por e-mail.


![Enviar e-mail com recibo do PDV](/files/pos-email.png)


### 3.4 Criar Nota de Crédito de Devolução


Você também pode criar uma nota de crédito de devolução contra uma fatura de PDV em caso de devolução de itens ou de todo o pedido. Seguem-se os passos para emissão de nota de crédito contra fatura:


1. Clique no menu (3 pontos) e depois clique em **Toggle Recent Orders**. O atalho de teclado para o mesmo é **⌘+O**.
![Pedidos recentes abertos de crédito de devolução de PDV](/files/pos-return-credit-1.png)
2. Todas as faturas de transações POS recentes serão exibidas no painel **Pedidos recentes**. Você pode pesquisar a fatura diretamente com seu nome ou filtrar os resultados da pesquisa de acordo com o status da fatura, que pode ser **Pago, Consolidado, Rascunho, Devolução**.
3. Selecione a fatura contra a qual você precisa criar a nota de crédito, após a qual você verá os detalhes da fatura e as opções para imprimir, enviar o recibo por e-mail e uma opção para fazer uma devolução. Clique em **'Devolver'**.
![Pos Return Credit Select Invoice](/files/pos-return-credit-2.png)
4. A tela do PDV exibirá os itens da nota fiscal, juntamente com as respectivas quantidades negativas e totais no Carrinho de Item, indicando que é uma nota de crédito de devolução.
![Tela de carrinho de item de crédito de devolução PDV](/files/pos-return-credit-3.png)
5. Depois de finalizar a compra, você verá o total geral, o valor pago e os impostos, se aplicável.
6. Clicar em **Concluir pedido** concluirá o processo e criará a fatura de crédito de devolução final e exibirá a fatura na tela como um pedido normal
![Fatura Final de Crédito de Devolução POS](/files/pos-return-credit-4.png)


### 3.5 Voucher de Fechamento de PDV


Ao final do dia, o caixa pode fechar seu PDV criando um Voucher de Fechamento de PDV. Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu Perfil de PDV e seu usuário para recuperar todas as vendas registradas.
Ao final do expediente, o caixa pode fechar seu turno criando um Voucher de Fechamento de PDV.


Clique no Menu e selecione 'Fechar o PDV'. Selecione o período, seu Perfil de PDV e seu usuário para recuperar todas as vendas registradas.


Ao criar um Voucher de Fechamento PDV, todas as Notas Fiscais PDV obtidas no período selecionado serão consolidadas em uma Nota Fiscal de Venda final. O status de todas as faturas do PDV mudará de 'Pago' para 'Consolidado' assim que forem consolidadas com sucesso em uma fatura de venda no fechamento.


![Entrada de fechamento POS](/files/pos-closing-entry.png)


Se houver mais de 10 faturas ao fechar um PDV, a consolidação das faturas ocorrerá em um trabalho em segundo plano e será enviada após a conclusão do trabalho em segundo plano. Os Razões Contábeis seriam afetados somente após o Comprovante de Fechamento ser enviado com sucesso e as faturas de vendas consolidadas serem criadas.


### 4. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Pedido de compra](/docs/v13/user/manual/en/buying/purchase-order)
3. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)
4. [Solicitação de pagamento](/docs/v13/user/manual/en/accounts/payment-request)