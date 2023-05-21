# Livro de Pagamentos


Um livro-razão separado para registrar transações em contas a receber e a pagar.


## Projeto


Os campos 'Débito' e 'Crédito' foram substituídos por 'Tipo de Conta' e 'Valor' (que podem ter valores +ve e -ve).
Se Voucher,


* aumenta o saldo da conta - valor tem valor +ve
* diminui o saldo da conta - valor tem valor -ve


## Campos Chave


* Tipo de conta - a receber/a pagar
* Conta - Nome da conta
* Parte - Nome da Parte
* Voucher No - Voucher afetando o saldo da conta
* Contra Voucher Não - Voucher Vinculado
* Valor - Valor do voucher


### Exemplo:


Uma fatura de venda de ₹ 1.000 e uma entrada de pagamento contra essa fatura terão a aparência abaixo.
![Captura de tela 2022 05 18 às 11.13.28 AM](/arquivos/Captura de tela 2022-05-18 às 11.13.28 AM.png)


## Fluxograma do design antigo e novo


Desenho antigo
![Pagamento Ledger.001](/arquivos/Pagamento Ledger.001.jpeg)


Novo design
![Pagamento Ledger.002](/arquivos/Pagamento Ledger.002.jpeg)


## Vantagem


Considere um cenário em que um pagamento é reconciliado com uma fatura de venda. No design antigo, isso exigiria que as entradas contábeis da entrada de pagamento fossem canceladas
e novos lançamentos contábeis com o link para a nota fiscal de venda serão repassados.


Com o novo design, há necessidade de tocar GL Entry. Somente o Razão de Pagamentos será atualizado.