# Consumo de materiais



A funcionalidade de consumo de material permite que você tenha vários `entradas de estoque` de consumo em relação a uma ordem de serviço. Para ativar isso, vá para Fabricação > Configurações de Fabricação.


![Item Alternativo](/files/allow-material-consumption.png)


Depois de ativado, um botão `Consumo de material` estará disponível na ordem de serviço quando iniciada.


![Item Alternativo](/files/material-consumption-button.png)


Quando o botão é clicado, ele fará o seguinte:


1. Irá criar Entrada de Estoque com finalidade `Consumo de Material para Fabricação`.


![Item Alternativo](/files/material-consumption-for-manufacture.png)


2. Se "Backflush de matérias-primas com base em" nas configurações de fabricação estiver definido como `BOM`, será proposto consumir toda a quantidade necessária para fabricação.
3. Se "Backflush de matérias-primas com base em" nas configurações de fabricação estiver definido como `Material transferido para fabricação`, será proposto consumir toda a quantidade transferida para fabricação.
4. Depois de enviado, ele atualizará a coluna `Quantidade Consumida` na Ordem de Serviço.


![Item Alternativo](/files/consumed-qty.png)


5. Ao suceder o Consumo de Material, ele irá sugerir a quantidade não consumida.
6. Depois que o botão "Concluir" for clicado na Ordem de Serviço, será considerada a quantidade consumida.


### Validações


* Se "Permitir consumo de vários materiais" não estiver definido nas configurações de fabricação, mas "Consumo de materiais para fabricação" for usado na entrada de estoque.


![Item Alternativo](/files/material-consumption-stock-entry.gif)


* Não é possível cancelar "Consumo de material para fabricação" para ordem de serviço concluída.


![Item Alternativo](/files/cancel-material-consumption-stock-entry.gif)



