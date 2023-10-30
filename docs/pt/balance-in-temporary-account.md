# Saldo em conta temporária



**Pergunta:**


Usamos a conta de abertura temporária para atualizar o saldo inicial. Após ter saldo atualizado em todas as contas do Balanço, ainda resta algum saldo na Conta Temporária? Qual é a causa deste saldo e como zerar o saldo desta conta?


**Resposta:**


Ao atualizar os saldos iniciais no ERPNext, você deve primeiro garantir que o Balanço Patrimonial no sistema anterior esteja contabilizando (Ativo = Passivo).


Então você começa a atualizar os saldos iniciais do extrato acima, usando a Abertura Temporária como uma conta para equilibrar o lançamento. Ao final, ao atualizar a abertura de todas as contas do Ativo e Passivo, o saldo da conta Temporária zera automaticamente.


Se você ainda tiver saldo na conta temporária, pode ser por um dos dois (ou ambos) motivos.


1. O Balanço Patrimonial seguido para atualização do saldo inicial não foi fechado corretamente e seu valor de Ativo e Passivo não estava sendo contabilizado.
2. Quando o saldo de abertura foi atualizado no ERPNext, a Conta de Abertura Temporária não foi usada de forma consistente.


Revise os pontos acima, pois eles podem ser a causa do saldo restante na conta de abertura temporária.



