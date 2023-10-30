# Relatório Imutável



> Introduzido na versão 13


Uma grande mudança foi introduzida no ERPNext a partir da versão 13. Isso muda a forma como o Razão Contábil (razão geral) e o razão de estoque funcionam no ERPNext. Existem vários motivos pelos quais os livros contábeis devem ser imutáveis. Para listar alguns:


* A republicação de entradas futuras é computacionalmente dispendiosa. Para lançar uma transação retroativa, todas as entradas futuras precisam ser republicadas.
* No Stock Ledger, onde as avaliações são baseadas no método First-in-first-out (FIFO), toda a sequência pode ser regenerada, o que pode perturbar as avaliações e o lucro para transações subsequentes.
* Os impostos pagos por um período também podem ser alterados.


## A seguir estão os impactos nas transações do dia a dia


### 1. Estornar lançamentos em cancelamento de transações


![General Ledger](/files/general-ledgercb549a.png)


No cancelamento de qualquer transação, em vez de excluir os lançamentos contábeis dessa transação, os lançamentos reversos serão repassados ​​para cancelar o efeito dessa transação na data do cancelamento.


![Excluir documento](/files/document-delete.png)


Como as entradas contábeis vinculadas a uma transação nunca serão excluídas, isso também significa que as transações canceladas e seus documentos vinculados não poderão mais ser excluídos.


### 2. Restrição ao lançamento de lançamentos de estoque retroativos


Como os livros contábeis são imutáveis ​​agora, isso significa que as transações futuras não podem ser atualizadas ou republicadas.
Assim, os usuários não poderão mais publicar transações de ações retroativas.


![Entrada com data anterior](/files/backdated-entry603ad4.png)


Por exemplo: suponha que uma transação de estoque tenha sido feita para o **item A** com horário de lançamento como `19-06-2020 23:00:10` então, após esta transação, você não poderá poste uma transação para o **item A** com horário de lançamento anterior a esse carimbo de data/hora.



