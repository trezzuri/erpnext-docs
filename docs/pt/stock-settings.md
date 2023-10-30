# Configurações de estoque



Você pode definir configurações padrão para suas transações relacionadas a ações na página Configurações de ações.

## 1. Nomeação de itens por

![Configurações de estoque](/files/stock-settings-1.png)![]()

Por padrão, o Nome do item é definido de acordo com o Código do item inserido. Se você deseja que os itens sejam nomeados por um conjunto [Nomeação Série](/docs/pt/setting-up/settings/naming-series) escolha a opção 'Nomear Série' .

## 2. Padrões

### 2.1 Grupo de itens padrão

Este será o grupo de itens padrão alocado para um item recém-criado. Os grupos de itens são úteis para classificação e configuração de propriedades para todo o grupo. Para saber mais, visite a página [Grupo de itens](/docs/pt/stock/item-group).### 2.2 UOM de estoque padrão

A unidade de medida padrão para estoque é definida como números (Nos), e pode ser alterada aqui.

### 2.3 Armazém padrão

Defina o Armazém padrão a partir do qual serão feitas as transações de estoque. Isso será buscado no Armazém Padrão no mestre de itens: ![Stock Settings](/files/stock-settings-def.png)![]()  


### 2.4 Armazém de retenção de amostras

Este é o armazém onde as retenções de amostras são armazenadas. Para saber mais, visite [esta página](/docs/pt/stock/retain-sample-stock).

### 2.5 Método de avaliação padrão

FIFO-primeiro a entrar, primeiro a sair ou avaliação de média móvel para seus itens. O método padrão é FIFO. Se você selecionar Média Móvel, os novos itens serão avaliados pela Média Móvel. Você pode alterar isso ao criar novos itens no formulário Item. Uma vez salvo o Item, o Método de Avaliação não poderá ser alterado. Leia mais [aqui](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average).

## 3. Porcentagem limite

Esta é a porcentagem que você tem permissão para receber ou entregar a mais em relação à quantidade solicitada. Por exemplo: Se você encomendou 100 unidades, o Fornecedor envia 120 unidades e a porcentagem está definida como 10%, então você poderá receber 110 unidades. Por padrão, isso é definido como 0.

## 4. Função com permissão para entregar/receber em excesso

Os usuários com esta função têm permissão para entregar/receber em excesso em pedidos acima da porcentagem permitida

## 5. Mostrar campo de código de barras

Um campo para inserir detalhes do código de barras de um item. Se desmarcado, o campo não ficará visível no formulário Item.

## 6. Converta a descrição do item em HTML limpo

Normalmente, as descrições são copiadas e coladas de um site ou arquivo Word/PDF e contêm muitos estilos incorporados. Isso atrapalha a visualização de impressão de suas faturas ou cotações.

Para corrigir isso, você pode marcar "Converter descrição do item em HTML limpo" nas configurações de estoque. Isso garantirá que quando você salvar os itens, suas descrições serão limpas.

Se quiser controlar sua descrição, visualizações e permitir que qualquer HTML seja incorporado, você pode desmarcar esta propriedade.## 7. Inserção automática

![Configurações de estoque](/files/stock-settings-2.png)![]()  


### 7.1 Inserir automaticamente a taxa da lista de preços se estiver faltando

Ativar isto irá inserir um Preço do Item para a Lista de Preços de um Item automaticamente ao usar o Item em sua primeira transação. Este preço é obtido a partir da ‘Taxa’ definida na primeira transação com o Item. A Lista de Preços depende se você está usando uma transação de Compra ou Venda.

Observe que o Preço do Item será inserido automaticamente apenas na primeira transação, se ainda não estiver presente.

 Se esta opção estiver desmarcada, a 'Taxa de venda padrão' definida no item ao criá-lo será adicionada como preço do item.

### 7.2 Definir números de série automaticamente com base no FIFO

Números de série o estoque será definido automaticamente com base nos itens inseridos com base no primeiro a entrar, primeiro a sair. Os Números de Série serão definidos automaticamente em transações como Faturas de Compra/Venda, Notas de Entrega, etc.

## 8. Permitir estoque negativo

Isso permitirá que os itens de estoque sejam exibidos em valores negativos. O uso desta opção depende do seu caso de uso. Por exemplo, as entradas de transações de ações são inseridas no fim de semana ou no final do mês. Nesse caso, o estoque negativo precisa ser ativado para que você possa continuar com suas transações de compra/venda.

Em vez de ativar o estoque negativo globalmente, você também pode ativá-lo para itens específicos.

 h2>9. Definir quantidade em transações com base em série sem entradaA quantidade de itens será definida de acordo com os números de série. Por exemplo, se o usuário adicionou números de série como A001, A002 e A003, o sistema definirá a quantidade como 3 na transação.

## 10. Solicitação automática de material

![Configurações de estoque](/files/stock-settings-3.png)![]()  


### 10.1 Aumentar solicitação de material quando o estoque atingir o nível de novo pedido

Esta opção é útil se quiser garantir um abastecimento constante de matérias-primas/produtos e evitar a escassez. Uma [Solicitação de material](/docs/pt/stock/material-request) será gerada automaticamente quando o estoque atingir o nível de reordenamento definido no [formulário de item](/docs/pt/stock/item#34-automatic-reordering).

### 10.2 Notificar por E-mail sobre a criação de Solicitação de Material automática

Um e-mail será enviado para notificar o Usuário com a função 'Gerente de Compras' quando uma Solicitação de Material automática for criado.

## 11. Configurações de transferência entre armazéns

![Transferência de material de nota de entrega](/files/inter-warehouse.png) ![]()  


### 11.1 Habilitar o armazém do cliente para transferência de materiais da nota de entrega e da fatura de vendas

 Esta opção é útil quando a transferência de material precisa ser apresentada como Nota de Remessa. Por exemplo, se houver requisitos legais onde os impostos devem ser aplicados em cada transferência de Material. É mais fácil gerenciar em uma transação como Nota de Remessa, do que na Entrada de Estoque

### 11.2 Habilitar armazém do fornecedor para transferência de material do Recibo de Compra e Fatura de Compra

Semelhante à opção acima, esta opção é útil quando a transferência de material precisa ser apresentada como recibo de compra.

Para saber mais sobre transferência de material entre armazéns via nota de entrega e fatura de compra, consulte este artigo [Transferência de material da nota de entrega](/docs/pt/stock/articles/material-transfer-from-delivery-note)

## 12. Congelar entradas de estoque

O usuário não poderá fazer lançamentos de ações além desta data.

![Configurações de estoque](/files/stock-settings-4.png)![]()  


 * **Estoque congelado até**: uma data limite até a qual os estoques serão congelados.
* **Congelar estoques mais antigos Mais de [Dias]**: os estoques com mais de x dias serão congelados. Isso é calculado com base na data de criação do item.
* **Função com permissão para editar estoque congelado**: A função que você escolher aqui terá permissão para editar estoque congelado.

## 13. Identificação de lote

Configuração global para lotes de estoque a serem identificados por um [Série de nomenclatura](/docs/pt/setting-up/settings/naming-series). Você pode substituir isso no Item DocType.

## 14. Permitir editar quantidade de estoque

  


Ativar "Permitir editar quantidade de UOM de estoque para documentos de vendas/Permitir editar quantidade de UOM de estoque para compra Documentos" nas configurações de estoque.

![stock_settings_edit_stock_qty](/files/stock_settings_edit_stock_qty.png "stock_settings_edit_stock_qty.png") ![]()  


**Por que editar a quantidade/quantidade de estoque conforme UOM de estoque**Se você estiver usando multi-uom e seu estoque uom for um número inteiro, você poderá enfrentar o problema de que o estoque UOM não deve ser decimal. Os usuários enfrentam esse problema quando não conseguem definir um fator de conversão preciso.

**Solução**

O usuário irá defina a quantidade de estoque e o sistema calculará o fator de conversão

![stock_qty_editable](/files/stock_qty_editable.gif "stock_qty_editable.gif")![]()  


  


  


  


  


  












