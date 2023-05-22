# Registro imutável



> 
> Introduzido na versão 13
> 
> 
> 


Uma grande mudança foi introduzida no SOMA a partir da versão 13 em diante. Isso altera a forma de funcionamento do Razão Contábil (General Ledger) e do Estoque no SOMA. Existem várias razões pelas quais os livros contábeis devem ser imutáveis. Para listar alguns:


* Repostar entradas futuras é computacionalmente caro. Para lançar uma transação retroativa, todas as entradas futuras precisam ser repostadas.
* No Stock Ledger, onde as avaliações são baseadas no método First-in-First-out (FIFO), toda a sequência pode ser regenerada, o que pode prejudicar as avaliações e o lucro para transações subsequentes.
* Os impostos pagos por um período também podem ser alterados.


## A seguir estão os impactos nas transações do dia a dia


### 1. Lançamentos reversos no cancelamento de transações


![General Ledger](/files/general-ledgercb549a.png)


No cancelamento de qualquer transação, em vez de excluir as entradas GL para essas transações, as entradas reversas serão passadas para cancelar o efeito dessa transação na data do cancelamento.


![Document Delete](/files/document-delete.png)


Como as entradas contábeis vinculadas a uma transação nunca serão excluídas, isso também significa que as transações canceladas e seus documentos vinculados não podem mais ser excluídos.


### 2. Restrição ao lançamento de entradas de estoque retroativas


Como os livros contábeis são imutáveis ​​agora, isso significa que as transações futuras não podem ser atualizadas ou repassadas.
Portanto, os usuários não poderão mais postar transações de estoque retroativas.


![Entrada com data anterior](/files/backdated-entry603ad4.png)


Por exemplo: suponha que uma transação de estoque tenha sido feita para o **item A** com horário de postagem como `19-06-2020 23:00:10`, depois dessa transação, você não pode postar uma transação para o **Item A** com hora de postagem anterior a este carimbo de data/hora.

