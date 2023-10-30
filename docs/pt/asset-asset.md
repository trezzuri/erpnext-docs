# Ativos



**Um ativo é qualquer item valioso de propriedade de uma empresa.**

Móveis, computadores, telefones celulares, impressoras, carros e equipamentos de fabricação são exemplos de ativos. Geralmente, um ativo é um item tangível localizado nas instalações da empresa ou transportado por um funcionário. Em alguns casos, um activo pode ser um item intangível.

A vida útil de um activo abrange vários anos e, portanto, o seu valor económico é distribuído pelos anos correspondentes do ponto de vista contabilístico. Se você comprar uma impressora por US$ 300 e espera-se que ela seja útil por três anos, do ponto de vista contábil, US$ 100 serão registrados como despesa de três anos cada, em vez de todos os US$ 300 do primeiro ano. A maioria dos países tem regras para tais cálculos.

No ERPNext, o registro de ativos é o coração do módulo de gerenciamento de ativos. Todas as transações relacionadas a um Ativo, como compra, depreciação, manutenção, movimentação, desmantelamento e vendas, serão registradas no registro do Ativo.

Para acessar a lista de Ativos, vá para: > Home > Ativos > Ativos > Ativo

## 1. Pré-requisitos

Antes de criar e usar o Asset, é aconselhável criar primeiro o seguinte:

* [Item](/docs/pt/stock/item) com 'É ativo fixo' ativado.
* [Categoria de ativo](/docs/pt/asset/asset-category)

## 2. Como criar um ativo

Deve ser criado um item representando o ativo. A opção **'Manter estoque'** deve estar **desmarcada** e **'É ativo fixo'** deve estar **marcada**.

 ![Asset Item](/files/asset-item.png)![]()

### 2.1 Criação automática de ativos

Você pode configurar o ERPNext para criar ativos automaticamente no envio da Compra Recebimento ativando **'Criação automática de ativos na compra'** no Item.

![Asset](/files/asset-auto-create.png)![]()  


Se você tiver ativado a criação automática de ativos para o item que representa um ativo, você terá que fornecer a localização do ativo ao enviar o recibo de compra.

![Localização do ativo no recibo de compra](/files/asset-location-in-purchase-receipt.png)![]()  


Uma mensagem confirmando a criação de ativos é exibida no envio do recibo de compra.

![Mensagem de confirmação de criação de ativos](/files/asset-auto-create-on-purchase.png)![]()  


### 2.2 Criação manual de ativos

Se desejar criar ativos manualmente, crie um item com 'É ativo fixo' ativado e deixe 'Criar ativos automaticamente ativado Comprar' desmarcado. Ao enviar um recibo de compra/fatura de compra com esse item, uma mensagem é mostrada indicando que você precisa criar ativos manualmente.

![Criação manual de ativos](/files/asset-manual-creation-message.png)![]()  
Siga as etapas abaixo para criar ativos manualmente.

1. Vá para a lista Ativos e clique em Novo.
2. Insira um nome para o recurso.
3. Selecione o código do item. O nome do item e a categoria do ativo serão obtidos automaticamente.
4. Selecione o proprietário do ativo, ou seja, empresa, fornecedor ou cliente.
5. Selecione a Empresa/Fornecedor/Cliente.
6. Selecione o Recibo de Compra/Fatura de Compra. A Data de Compra e o Valor Bruto da Compra serão obtidos automaticamente.
7. Selecione um Local. Ex: Escritório de Mumbai. Isso será obtido automaticamente se especificado na tabela de itens do recibo de compra
8. Definir data de disponibilidade para uso. A depreciação será calculada a partir desta data.
9. Salvar e enviar.

Observe que você precisa criar **um registro de ativo para cada ativo que você comprou**. Se você comprou cinco computadores e criou apenas um recibo de compra com quantidade definida como cinco, você terá que criar cinco registros de ativos manualmente.

### 2.3 Criando ativos compostos

Se, por Por exemplo, você deseja criar um ativo "Computador" feito de vários itens diferentes, como "Monitor", "Teclado" etc., você pode criar um ativo WIP composto marcando a caixa de seleção `is_composite_asset`. Depois, você pode marcar esse ativo no campo `WIP Composite Asset` do item em recibos/faturas de compra e, quando todos os itens estiverem disponíveis, você pode usar o [Recurso de capitalização de ativos](https://docs.erpnext.com/docs/user/manual/en/asset-capitalization) para capitalizar o ativo.

 ![](/files/t6xnhCo.png)![](/files/jdmoSl4.png)![]()  


### 2.4 Importando ativos existentes

Quando você muda de um sistema legado para o ERPNext, você terá que adicionar detalhes de todos os ativos que sua empresa comprou anteriormente, juntamente com detalhes de depreciação de cada ativo.

 Para um ativo existente, você pode criar o registro do ativo diretamente marcando a caixa de seleção **"É um ativo existente"** e fornecendo os detalhes abaixo.

* Valor bruto da compra


- Data de compra
- Data de disponibilidade para uso
- Abertura acumulada Depreciação: o valor da depreciação acumulada que já foi contabilizada para um ativo existente.
- Número de depreciações contabilizadas: número de entradas de depreciação já contabilizadas.
 - Está totalmente depreciado: marque esta caixa de seleção se o ativo existente estiver totalmente depreciado
Com base nesses detalhes, o cronograma de depreciação do valor restante será criado automaticamente .

### 2.5 Opções adicionais ao criar um Ativo

1. **Custodiante**: O funcionário que carregará o ativo.
2. **Departamento**: O departamento do Custodiante.
3. **Calcular Depreciação**: Habilite isto caixa de seleção para calcular a depreciação dos ativos.

## 3. Recursos

### 3.1 Depreciação

* **Frequência de depreciação (meses)**: o número de meses entre depreciações.
* **Número total de depreciações**: O número total de depreciações durante a vida útil do Ativo. No caso de ativos existentes parcialmente amortizados, mencionar o número de amortizações pendentes. Por exemplo, se você definir a frequência como 12 meses e não. de depreciações como 3, 1 depreciação será contabilizada a cada 12 meses durante 3 anos.
* **Método de depreciação**: Existem quatro métodos disponíveis para depreciação: Direto Linha, Valor Abatido, Saldo Decrescente Duplo e Manual. Você pode encontrar mais detalhes [aqui](https://docs.erpnext.com/docs/user/manual/en/asset-depreciation) .
* **Data de lançamento da depreciação**: a data a partir da qual o registro da depreciação será iniciado.
* **Valor esperado após vida útil**: Vida útil é o período de tempo durante o qual a empresa espera que o ativo seja produtivo. Após esse período, o ativo é sucateado ou vendido. Caso seja vendido mencione aqui o valor estimado. Esse valor também é conhecido como valor residual, valor residual ou valor residual.
* **Porcentagem do valor residual**: se você deseja o `Valor esperado Após a Vida Útil` ser calculada automaticamente com base em um percentual do `Valor Bruto da Compra`, mencione o percentual aqui.
* **Taxa de Depreciação**: Será calculada com base no valor inserido no valor esperado após a vida útil.
* **Livro Financeiro**: O livro contra o qual os lançamentos de depreciação devem ser contabilizados. Para obter mais detalhes, clique [aqui](/docs/pt/accounts/finance-book).
* **Depreciação diária**: divide o valor da depreciação pelo número de dias em um período de calendário. Portanto, o valor da depreciação varia de acordo com a quantidade de dias do mês. Por exemplo, o valor da depreciação em fevereiro é menor que o valor da depreciação dos meses que têm 31 dias.

### 3.2 Cronograma de depreciação

Na contabilização de depreciações contra este Ativo, a seção Cronograma de Depreciação ficará visível. Esta tabela possui colunas para livro financeiro, data de programação, valor de depreciação, valor depreciado e lançamento contábil manual.

![Cronograma de depreciação](/files/asset-depreciation-schedule.png)![]()  


###  3.3 Detalhes do Seguro

Se o Seguro tiver sido contratado para o Ativo que você está registrando, você poderá armazenar os seguintes detalhes do Seguro:

* Número da Apólice
* Seguradora
* Valor segurado
* Data de início do seguro
* Data de término do seguro
* Seguro abrangente

### 3.4 Lançamentos contábeis

Na apresentação de um ativo, será creditada a conta “Capital Obras em Andamento” e debitada a conta do ativo referente ao ativo. O envio só é possível após inserir a “Data disponível para uso”. Se a "Data disponível para uso" for uma data futura, o lançamento contábil será registrado automaticamente nessa data por meio do agendador.

### 3.5 Manutenção

Marcar Manutenção necessária permite a gravação Entradas de manutenção de ativos para este ativo. Para saber mais, visite a página [Manutenção de ativos](/docs/pt/asset/asset-maintenance).

### 3.6 Após o envio

Depois de criar um ativo, você verá opções para transferir, descartar ou vender o ativo. No botão Criar, você pode ajustar seu valor e fazer um lançamento de depreciação.

![Asset Submit](/files/asset-submit.png)![]()  


### 4. Tópicos relacionados

1. [Manutenção de ativos](/docs/pt/asset/asset-maintenance)
2. [Movimentação de ativos](/docs/pt/asset/asset-movement)
3. [Recibo de compra](/docs/pt/stock/purchase-receipt)
4. [Fatura de compra](/docs/pt/accounts/purchase-fatura)


