# Congelar taxa de câmbio


No ERPNext, você pode buscar taxas de câmbio entre moedas em tempo real ou salvar taxas de câmbio específicas também. No ERPNext, as taxas de câmbio salvas também são referidas como Taxa de câmbio obsoleta.


Em suas transações de compra e venda, se o campo Taxa de Câmbio estiver congelado, é porque o recurso de permitir taxas de câmbio obsoletas nas transações está ativado. Para tornar o campo Taxa de câmbio editável novamente, desative o recurso Taxa de câmbio obsoleta em:


* Contabilidade > Mestres de contabilidade > Configurações de contas
* Desmarque o campo "Permitir taxas de câmbio obsoletas".


![Permitir taxas de câmbio obsoletas](/files/allow-stale-exchange-rates.png)
* Salvar configurações da conta
* Atualize sua conta ERPNext
* Verifique a transação de compra/venda mais uma vez


Após esta configuração, o campo Taxa de Câmbio nas transações deve ficar editável novamente.

