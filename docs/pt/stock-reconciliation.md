# Reconciliação de estoque



**Conciliação de estoque é o processo de contagem e avaliação de materiais/produtos, periodicamente no final do ano.**


Isso é feito para:


* Mantenha a contagem real do estoque físico e a contagem do estoque contábil sincronizadas
* Avaliar o estoque para elaboração das demonstrações contábeis


O recurso de reconciliação de estoque no ERPNext é usado para:


* Lançamento do estoque de abertura
* Conciliando estoque contábil e real


Para acessar a lista de Conciliação de Estoque, acesse:
> Home > Estoque > Ferramentas > Reconciliação de estoque


## 1. Como criar uma reconciliação de estoque para o estoque pós-abertura


Usando a reconciliação de estoque você pode atualizar o número de itens específicos em um armazém em um horário específico.
Você também pode adicionar itens no estoque que tenham números de série ou números de lote.


1. Vá para a lista de reconciliação de estoque e clique em Novo.
2. Selecione a finalidade como 'Estoque inicial'. Você pode editar a data e hora da postagem.
3. Selecione Código do Item, Armazém, Quantidade e Taxa de Avaliação. Se houver um número de série/lote envolvido, adicione-o.
4. Se você deseja gerar automaticamente o número de série/número do lote, mantenha esses campos em branco.
	* Para a geração automática do número de série, você precisa definir "Série do número de série" no cadastro de itens.
	* Para a geração automática do número do lote, você precisa ativar a caixa de seleção "Criar novo lote automaticamente" no cadastro de itens.
5. A conta de diferença será definida como 'Abertura temporária'.
6. Salvar e enviar.


![Abertura de estoque](/files/opening_stock.png)


> Observação: a opção Manter estoque deve estar habilitada no item mestre para que isso funcione.


## 2. Como criar uma reconciliação de estoque para reconciliar a contagem de estoque físico e contábil


Conciliação de Estoques é o processo de contagem e avaliação de estoques, periodicamente e no final do ano, a fim de avaliar o estoque total para preparação das demonstrações contábeis. Neste processo, os estoques físicos reais são verificados e registrados no sistema. Os estoques reais e o estoque no sistema devem estar de acordo e precisos. Caso contrário, você poderá usar a ferramenta Reconciliação de estoque para reconciliar o saldo e o valor do estoque com os valores reais.


Para reconciliar o estoque:


1. Vá para a lista de reconciliação de estoque, clique em Novo
2. Selecione a Finalidade como 'Reconciliação de Estoque'. Você pode editar a data e hora da postagem.
3. Definir código do item, armazém.
4. A quantidade atual e a taxa de avaliação serão obtidas. Altere a quantidade conforme necessário.
5. A conta de despesas na conta de diferença será definida como 'Ajuste de estoque' por padrão.
6. O padrão do Centro de Custo será 'Principal', altere se necessário.
7. Salvar e enviar.


![Reconciliação de estoque](/files/stock_recon.png)


## 3. Recursos


### 3.1 Carregar dados por meio de planilha


Se você tiver muitos itens, poderá fazer upload dos detalhes por meio de uma planilha.


1. Baixar modelo


Abra uma nova reconciliação de estoque e clique no botão Download para baixar o modelo em formato CSV.


![Reconciliação de estoque](/files/stock-recon-1.png)
2. Insira os dados no modelo CSV.


O formato CSV diferencia maiúsculas de minúsculas. Não edite os cabeçalhos predefinidos no modelo. Na coluna Código do Item e Armazém, insira o Código do Item e Armazém exatos conforme criados em sua conta ERPNext. Para quantidade, insira o nível de estoque que deseja definir para aquele item, em um armazém específico.


![Reconciliação de estoque](/files/stock-reco-data.png)
3. Faça upload do arquivo CSV com os dados clicando no botão 'Upload'.


![Reconciliação de estoque](/files/stock-recon-2.png)
4. Revise, salve e envie.


![Reconciliação de estoque](/files/stock-reco-upload.gif)
5. Verifique o Relatório de Registro de Estoque para ver o saldo de estoque atualizado.


![Reconciliação de estoque](/files/stock-reco-ledger.png)


### 3.2 Obtenha o saldo e a avaliação do estoque em uma data e hora específicas


Você pode importar o saldo do estoque e a avaliação em uma data e hora específicas de um armazém selecionado clicando no botão **Itens**. Você pode atualizar a quantidade e a taxa de avaliação conforme necessário.


![Botão de itens de reconciliação de estoque](/files/stock_reconciliation_items_button.gif)


### 3.3 Usando o leitor de código de barras para digitalizar o inventário físico


Se você configurou códigos de barras para seus itens, poderá usar um leitor de código de barras para reconciliar quantidades físicas. Para fazer isso, siga estas etapas:


1. Definir armazém padrão
2. Ative o "Modo de digitalização", isso desativará a busca da quantidade existente e permitirá que você adicione quantidades digitalizando itens de forma incremental.
3. Clique no campo "Scan Barcode" e use seu leitor de código de barras para enviar a entrada. A tabela de itens de reconciliação continuará sendo atualizada à medida que você digitaliza os itens. O vídeo a seguir demonstra esse processo.


![Verificação de reconciliação de estoque](/files/stock_reco_scanning.gif)


## 4. Como funciona a reconciliação de estoque


Depois que uma reconciliação de estoque for lançada para atualizar a quantidade em data e hora específicas para um item em um depósito, ela não será modificada por transações de estoque subsequentes, mesmo que tais transações tenham uma data de lançamento anterior à data de reconciliação de estoque . Em outras palavras, lançamentos retroativos não alterarão os números do estoque após o lançamento de um lançamento de Reconciliação de estoque.


Os exemplos são os seguintes.


### 4.1 Para itens não serializados


Considere um item com o código 'ABC001' em um depósito em 'Mumbai'.
Vamos supor que o estoque em 10 de janeiro seja de 100 unidades.
A reconciliação de estoque é feita no dia 12 de janeiro para definir o saldo do estoque em 150 unidades.


O livro razão de estoque ficaria conforme mostrado abaixo:



 td {
 preenchimento: 5px 10px 5px 5px;
 };
 imagem {
 alinhar:centro;
 };
 tabela, th, td {
 borda: 1px preto sólido;
 colapso da fronteira: colapso;
 }




| **Data de postagem** | **Quantidade** | **Quantidade do saldo** | **Tipo de voucher** |

| 01/10/2014 | 100 | 100  | Recibo de compra |

| 12/01/2014 | 150 | 150 | Reconciliação de estoque |



Se um novo lançamento de recibo de compra for feito em 5 de janeiro de 2014, que é anterior à data de entrada de reconciliação de estoque, o razão de estoque teria a aparência mostrada abaixo.



```




```

|  |  |  |  |
| --- | --- | --- | --- |
| **Data de postagem** | **Quantidade** | **Quantidade do saldo** | **Tipo de voucher** |
| 01/05/2014 | 20 | 20 | Recibo de compra |
| 01/10/2014 | 100 | 120 | Recibo de compra |
| 12/01/2014 |  | **150** | Reconciliação de estoque |






Como você pode ver, a quantidade de saldo de 10 de janeiro foi atualizada de 100 para 120. Mas a quantidade de saldo de 12 de janeiro não foi atualizada de 150 para 170.


### 4.2 Para itens serializados

Para um item, ITEM-00225 que possui 6 números de série HJF00020, HJF00021, HJF00022, HJF00023, HJF00024, HJF00025 com taxa de avaliação de 530 por número de série. No final do ano, o usuário ficou sabendo que possui apenas 3 números de série naquele item com taxa de avaliação 620. Portanto, para remover os antigos números de série HJF00020, HJF00021, HJF00022, HJF00023, HJF00024, HJF00025 e adicionar o novo números de série com nova Taxa de Avaliação, a Reconciliação de Estoque pode ser utilizada da seguinte forma:

Selecione o item ITEM-00225 na conciliação de estoque, ao selecionar o Item o sistema irá puxar automaticamente os números de série existentes. Em seguida, defina Qtd como 3, Taxa de avaliação como 530 e número de série como HJF00026, HJF00027, HJF00028.


![Reconciliação de estoque](/files/stock-recon-for-serialized.png)

Antes da reconciliação, a taxa de avaliação era de 530 e a quantidade disponível era de 6, portanto o valor total do estoque era de 3.180. Após a reconciliação, a taxa de avaliação mudou para 620 e a quantidade disponível mudou para 3, então o novo valor do estoque passa a ser 1.860. Para ajustar o valor do estoque na contabilidade, o sistema creditou o valor extra 3.180-1.860 = 1.320 na conta do Armazém e debitou na conta de ajuste de estoque. As entradas GL para a entrada acima são as seguintes:

Para visualizar os lançamentos contábeis, clique no botão Visualizar > Razão Contábil

![Reconciliação de estoque](/files/gl_entry_for_serialized_items.png)

O saldo de stocks após apresentação da reconciliação de stocks:
![Reconciliação de estoque](/files/stock_balance_after_stock_reco_submission.png)

O razão geral da conta de armazém Nagpur após a apresentação da reconciliação de estoque:
![Reconciliação de estoque](/files/general_ledger_after_stock_reco_submission.png)### 4.3 Para itens em lote

A reconciliação de estoque para itens de lote será usada para adicionar um novo lote ou para atualizar a quantidade do lote existente. Por exemplo, o lote JHGJH00003 tem a quantidade atual de 60, mas se o usuário quiser aumentar para 100, usando a reconciliação de estoque, o usuário pode atualizar a quantidade do lote.

![Reconciliação de estoque](/files/for_batch_item_after_stock_reco_submission.png)

Relatório de histórico de saldo em lote após o envio da reconciliação de estoque:
![Reconciliação de estoque](/files/batchwise_balance_history_after_stock_reco_submission.png)

## 5. Vídeo





### 6. Tópicos Relacionados


- [Entrada de estoque](/docs/pt/stock/stock-entry)

- [Contabilidade do estoque](/docs/pt/stock/accounting-of-inventory-stock)







