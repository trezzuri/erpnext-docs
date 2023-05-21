# Livro-razão imutável



>
> Introduzido na versão 13
>
>
>


Uma grande mudança foi introduzida no ERPNext a partir da versão 13. Isso altera a forma de funcionamento do Razão Contábil (General Ledger) e do Estoque no ERPNext. Existem várias razões pelas quais os livros contábeis devem ser imutáveis. Para listar alguns:


* Repassar entradas futuras é computacionalmente caro. Para lançar uma transação retroativa, todas as entradas futuras precisam ser lançadas novamente.
* No livro-razão de estoque, onde as avaliações são baseadas no método primeiro a entrar, primeiro a sair (FIFO), toda a sequência pode ser regenerada, o que pode prejudicar as avaliações e o lucro das transações subsequentes.
* Os impostos pagos por um período também podem ser alterados.


## A seguir estão os impactos nas transações do dia a dia


### 1. Lançamentos Estornos no cancelamento de transações


![Contagem Geral](/files/general-ledgercb549a.png)


No cancelamento de qualquer transação, em vez de excluir as Entradas GL para essas transações, serão passadas entradas reversas para cancelar o efeito dessa transação na data do cancelamento.


![Document Delete](/files/document-delete.png)


Como as entradas contábeis vinculadas a uma transação nunca serão excluídas, isso também significa que as transações canceladas e seus documentos vinculados não podem mais ser excluídos.


### 2. Restrição ao lançamento de entradas de estoque retroativas


Como os livros contábeis são imutáveis ​​agora, isso significa que as transações futuras não podem ser atualizadas ou repassadas.
Portanto, os usuários não poderão mais lançar transações de estoque retroativas.


![Entrada com data anterior](/files/backdated-entry603ad4.png)


Por exemplo: suponha que uma transação de estoque tenha sido feita para **Item A** com hora de lançamento como `19-06-2020 23:00:10`, então após esta transação você não pode lançar uma transação para **Item A** com tempo de postagem antes deste carimbo de data/hora.