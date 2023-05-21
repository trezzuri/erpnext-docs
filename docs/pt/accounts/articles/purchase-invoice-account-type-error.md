# Fatura de compra - Erro de tipo de conta


**Pergunta:** Ao salvar a Fatura de Compra, recebo uma mensagem de validação de que a Conta de Crédito deve ser uma conta do Balanço.


![Crédito na conta na fatura de compra](/files/credit-to-ledger-in-purchase-invoice.png)


*\*Resposta: \**Ao enviar uma Fatura de Compra, o valor a pagar é atualizado para o Fornecedor. De acordo com os padrões contábeis, a Conta a Pagar está alinhada no Passivo Circulante (lado do crédito do Balanço).


A mensagem de erro indica que a conta selecionada no campo Credit To não pertence ao Grupo de obrigações. Certifique-se de que a conta a pagar selecionada na fatura de compra esteja localizada no grupo Passivo.