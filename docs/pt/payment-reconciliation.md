# Reconciliação de pagamentos



**A reconciliação de pagamentos é usada para vincular pagamentos a faturas.**

Em cenários complexos, especialmente no setor de bens de capital, às vezes não há vínculo direto entre pagamentos e faturas. Por exemplo, suponha que uma parte seja um cliente, você envia faturas a um cliente e o cliente lhe envia pagamentos bloqueados ou pagamentos com base em algum cronograma que não está vinculado às suas faturas.

Nesses casos, você pode combine pagamentos com faturas usando a reconciliação de pagamentos.

Para acessar a reconciliação de pagamentos, vá para:


> Página inicial > Contabilidade > Contas a receber > Reconciliação de pagamentos
> 
> 

 ## 1. Como combinar pagamentos com faturas

1. Vá para Reconciliação de pagamentos.
2. Selecione uma empresa.
3. Selecione um tipo de festa e selecione a festa. A conta a receber/a pagar será selecionada automaticamente.
4. Selecione a conta bancária/dinheiro com a qual os pagamentos precisam ser reconciliados.
5. Se desejar filtrar os registros, selecione um intervalo de datas para as faturas ou defina o valor mínimo ou máximo para as faturas, bem como para as transações de pagamento.
6. Clique no botão **Obter entradas não reconciliadas**.
7. Isso irá buscar todas as faturas e transações de pagamento não vinculadas dessa parte na tabela Faturas e Pagamentos, respectivamente.
8. Você pode selecionar quaisquer entradas específicas a serem alocadas ou clicar no botão **Alocar** sem selecionar nada para alocar todas as entradas.
9. A tabela de alocação será preenchida com base no FIFO e/ou seleção.
10. Valor Alocado é o valor que você deseja alocar para a reconciliação.
11. Clique em **Reconciliar** para reconciliar as entradas alocadas. Você receberá uma mensagem que diz 'Reconciliado com sucesso'.

![Ferramenta de reconciliação de pagamento](/files/payment_recon.gif)![]()

## 2 . O que acontece na reconciliação de pagamento

Se as faturas forem reconciliadas com: 

1. **Lançamento de pagamento**-Um lançamento contábil não é criado automaticamente quando a reconciliação ocorre em relação a um lançamento de pagamento. Isso ocorre porque as entradas de pagamento estão associadas a transações vinculadas.
2. **Nota de crédito/débito** -Um lançamento contábil manual é criado automaticamente para alocar uma nota de crédito/débito a uma fatura que está sendo reconciliada. Esta criação automática de um lançamento contábil manual é necessária porque as notas de crédito/débito não possuem transações vinculadas. O lançamento contábil manual resultante da reconciliação indica o ajuste de uma nota de crédito/débito específica com uma fatura específica.

### 2. Tópicos relacionados

1. [Solicitação de pagamento](/docs/pt/accounts/payment-request)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
3. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
4. [Reconciliação de pagamento semiautomática](/docs/pt/accounts/semi-auto-payment-reconciliation)


