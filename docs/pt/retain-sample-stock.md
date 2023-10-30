# Retenção de estoque de amostra



**O estoque de amostra é um lote de qualquer item armazenado para análise caso haja necessidade posteriormente.**


O item para o qual o estoque de amostra é armazenado pode ser matéria-prima, material de embalagem ou produto acabado.


## 1. Pré-requisitos


Antes de usar a retenção de amostra, é aconselhável criar primeiro o seguinte:


* [Item](/docs/pt/stock/item)
* [Lote](/docs/pt/stock/batch)
* [Armazém](/docs/pt/stock/warehouse)


## 1. Como definir o depósito de retenção de amostras nas configurações de estoque


É aconselhável criar um novo Armazém separadamente para retenção de amostras e não utilizá-lo na produção.


![Armazém de retenção de amostras](/files/sample-warehouse.png)


### 1.2 Ativar retenção de amostra no item mestre


Reter amostra é baseado em lote, portanto, o número de lote deve ser ativado primeiro. Marque Reter amostra e defina o máximo de amostras permitidas para um lote.


![Retain Sample](/files/retain-sample.png)


### 1.3 Fazer entrada de estoque


* Sempre que um [Lançamento de Estoque](/docs/pt/stock/stock-entry) for criado com a finalidade de Recebimento de Material, para itens que tenham Reter Amostra ativado, a Quantidade de Amostra pode ser definida durante essa Entrada de Estoque. Você precisa selecionar o número do lote para o item/itens. A quantidade de amostra não pode ser maior que a quantidade máxima de amostra definida no Cadastro de Itens.


![Reter amostra](/files/material-receipt-sample.png)
* Ao enviar esta Entrada de Estoque, o botão 'Fazer Entrada de Estoque de Retenção' estará disponível para fazer outra Entrada de Estoque para a transferência de itens de amostra do lote mencionado para o armazém de retenção definido nas Configurações de Estoque.


![Botão de retenção de amostra](/files/sample-retention-button.png)
* Clicar neste botão direcionará você para uma nova Entrada de Estoque do tipo 'Transferência de Material'. Esta entrada está transferindo sua retenção de amostras do seu Armazém de Destino (Lojas) para o Armazém de Retenção de Amostras. Ele conterá todas as informações, verifique e clique em Enviar.


![Reter amostra](/files/material-transfer-sample.png)


### 2. Tópicos Relacionados


1. [Armazém](/docs/pt/stock/warehouse)



