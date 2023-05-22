# Registro de Pagamentos


Um livro-razão separado para registrar transações em contas a receber e a pagar.


## Design


Os campos 'Débito' e 'Crédito' foram substituídos por 'Tipo de Conta' e 'Valor' (que podem ter valores +ve e -ve).
Se for voucher,


* aumenta o saldo da conta - o valor tem +ve valor
* diminui o saldo da conta - valor tem valor -ve


## Campos-chave


* Tipo de conta - a receber/a pagar
* Conta - Nome da conta
* Parte - Nome da Parte
* Voucher No - Voucher afetando o saldo da conta
* Contra Voucher Não - Voucher Vinculado
* Valor - Valor do voucher


### Exemplo:


Uma fatura de venda de ₹ 1.000 e uma entrada de pagamento contra essa fatura terão a aparência abaixo.
![Captura de tela 2022 05 18 às 11.13.28](/files/Screenshot 2022-05-18 às 11.13.28 AM.png)


## Fluxograma do design antigo e novo


Desenho antigo
![Payment Ledger.001](/files/Payment Ledger.001.jpeg)


Novo Design
![Payment Ledger.002](/files/Payment Ledger.002.jpeg)


## Vantagem


Considere um cenário em que um pagamento é reconciliado com uma fatura de venda. No design antigo, isso exigiria que as entradas contábeis da entrada de pagamento fossem canceladas
e novas entradas GL com o link para fatura de vendas serão repostadas.


Com o novo design, é necessário tocar no GL Entry. Apenas o livro-razão de pagamentos será atualizado.

