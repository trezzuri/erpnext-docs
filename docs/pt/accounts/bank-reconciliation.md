# Reconciliação Bancária


**Uma entrada de reconciliação bancária é usada para combinar os extratos da conta SOMA com os extratos da sua conta bancária.**


Se estiver a receber pagamentos ou a efetuar pagamentos através de cheques, os extratos bancários não corresponderão exatamente às datas da sua entrada, porque o banco costuma demorar a “compensar” esses pagamentos.


Além disso, você pode ter enviado um cheque ao seu fornecedor e pode levar alguns dias até que ele seja recebido e depositado pelo fornecedor. No SOMA você pode sincronizar seus extratos bancários e seus lançamentos contábeis manuais usando as datas das transações.


## 1. O que é um Extrato de Reconciliação Bancária?


O Relatório de Conciliação Bancária fornece a diferença entre o saldo bancário mostrado no extrato bancário de uma organização, conforme fornecido pelo banco, em relação ao valor mostrado no Plano de Contas da empresa.


É assim que um extrato de reconciliação bancária se parece:


![Extrato de reconciliação bancária](/files/bank-reconciliation-2.png)


No relatório, verifique se o campo 'Saldo conforme banco' corresponde ao Extrato da Conta Bancária. Se for coincidente, significa que a Data de Compensação está atualizada corretamente para todos os lançamentos bancários. Se houver incompatibilidade, é devido a lançamentos bancários cuja Data de Liquidação ainda não foi atualizada.


Para acessar a Reconciliação Bancária, acesse:



> 
> Página inicial > Contabilidade > Bancos e pagamentos > Atualizar data de transação bancária
> 
> 
> 


## 2. Como atualizar datas de transações bancárias


1. Vá para Atualizar datas de transações bancárias.
2. Selecione sua conta bancária.
3. Selecione uma data de e até.
4. Você pode optar por incluir entradas reconciliadas e transações PDV.
5. Clique no botão **Obter entradas de pagamento**.
6. Agora você receberá todas as entradas do tipo “Bank Voucher”.
7. Em cada uma das entradas, na coluna mais à direita, atualize o campo “Data de Liberação” e clique no botão **Atualizar Data de Liberação**.


Ao fazer isso, você poderá sincronizar seus extratos bancários e lançamentos no sistema.


![Bank Reconciliation](/files/bank-reconciliation.png)


## 3. Tipos de ferramentas de reconciliação


SOMA possui duas ferramentas de reconciliação:


1. Uma ferramenta de reconciliação manual que permite definir datas de compensação em entradas de pagamento, pagamentos de faturas de vendas ou lançamentos contábeis manuais
2. Uma ferramenta de reconciliação semiautomática que permite compensar transações bancárias contra entradas de pagamento, pagamentos de faturas de vendas e compras, lançamentos contábeis ou declarações de despesas.


### 3.1 Ferramenta manual de reconciliação bancária


Para visualizar este relatório, vá para **Contas > Bancos e pagamentos > Extrato de reconciliação bancária**. No relatório, verifique se o campo 'Saldo conforme banco' corresponde ao Extrato da Conta Bancária. Se for coincidente, significa que a Data de Compensação está atualizada corretamente para todos os lançamentos bancários. Se houver desencontro, é porque a Data de Liquidação ainda não foi atualizada para os lançamentos bancários.


### 3.2 Ferramenta de reconciliação bancária semiautomática


É um processo de duas etapas:


1. Adicionar transações bancárias ao SOMA via importação de extrato bancário ou sincronização de conta bancária
2. Reconcilie o extrato bancário


#### 3.2.1 Importação de extrato bancário


1. Baixe um extrato bancário do site do seu banco


![Reconciliar transações bancárias](/files/sample_bank_statement.png)
Certifique-se de ter pelo menos a data, o débito/crédito e a moeda em cada linha do seu extrato bancário.


Para enviar seu Extrato Bancário, acesse:



> 
> Contabilidade > Extrato bancário > Importação de extrato bancário
> 
> 
> 


ou simplesmente procure por 'Importação de Extrato Bancário' na barra incrível.


1. Selecione sua empresa e conta bancária
2. Clique em Salvar
3. Anexe o extrato bancário
4. Clique em 'Mapear Colunas' para inserir o mapeamento entre as colunas no Extrato Bancário carregado e no Tipo de Documento da Transação Bancária
5. Clique em Iniciar importação para iniciar o processo de importação. As transações bancárias serão criadas por meio de um trabalho em segundo plano, embora o progresso seja mostrado aqui


![Reconciliar transações bancárias](/files/bank_transaction_upload.gif)
6. O mapeamento feito é armazenado no documento Banco vinculado à Conta Bancária correspondente. No próximo upload, o mapeamento é retirado daqui, mas o sistema permite que o usuário o altere, se necessário. O mapeamento alterado também é atualizado no documento do Banco.
![Reconciliar transações bancárias](/files/bank_configuration.png)


#### 3.2.2 Sincronização de contas bancárias


Você pode usar o Plaid (consulte a [página Integrações do Plaid](/docs/pt/erpnext_integration/plaid_integration)) para sincronizar automaticamente sua conta bancária com o SOMA. Todas as suas transações bancárias serão importadas automaticamente para o SOMA.


#### 3.2.3 Conciliar o extrato bancário


Depois que todas as suas transações bancárias forem importadas para o SOMA, você poderá reconciliá-las com seus comprovantes existentes. Acesse:



> 
> Contabilidade > Extrato bancário > Ferramenta de reconciliação bancária
> 
> 
> 


ou simplesmente procure por 'Ferramenta de reconciliação bancária' na barra incrível.


1. Selecione sua empresa, conta bancária, data de início e término do extrato bancário.
2. Certifique-se de que o saldo inicial do SOMA corresponda ao saldo inicial do seu extrato bancário.
3. Insira o saldo final do extrato bancário.
4. Salvar o documento mostrará as transações bancárias correspondentes.
![Reconciliar transações bancárias](/files/bank_reconciliation_tool.png)
5. O objetivo final da Reconciliação Bancária é fazer com que o valor da diferença seja zero (verde) correspondendo a um comprovante existente ou criando um novo comprovante.
6. Para todas as movimentações bancárias que constam no Extrato Bancário mas não possuem data de compensação, clique no Botão Ações para Conciliar/Criar Comprovantes
7. Para correspondência, escolha 'Combinar com Voucher' em 'Ação'. Serão exibidos os comprovantes relacionados a esta transação. Eles serão classificados com base no número máximo de campos correspondentes. Você pode combinar um ou vários vouchers com a mesma transação bancária usando as caixas de seleção.
![Reconciliar transações bancárias](/files/match_voucher.png)
8. Para criar um novo voucher, escolha 'Criar Voucher' em 'Ação' e depois escolha o tipo de documento. Preencha os dados que não estavam disponíveis na Transação Bancária. Clicar em Enviar criará o comprovante correspondente e atualizará sua data de liberação.
![Reconciliar transações bancárias](/files/create_voucher.png)
9. Também é possível atualizar as Movimentações Bancárias. Atualizar a Transação Bancária pode ajudar o SOMA a encontrar correspondências melhores. Para atualizar uma transação bancária, escolha 'Atualizar transação bancária' em 'Ação', preencha os detalhes necessários e clique em Enviar para salvar a transação bancária.
![Reconciliar transações bancárias](/files/update_bank_transaction.png)


### 4. Tópicos Relacionados


1. [Reconciliação de pagamentos](/docs/pt/accounts/payment-reconciliation)
2. [Garantia bancária](/docs/pt/accounts/bank-guarantee)
3. [Entrada de pagamento](/docs/pt/accounts/payment-entry)
