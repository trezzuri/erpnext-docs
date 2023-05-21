# Reconciliação bancária


**Uma entrada de reconciliação bancária é usada para combinar os extratos da conta ERPNext com os extratos da sua conta bancária.**


Se estiver a receber pagamentos ou a efetuar pagamentos através de cheques, os extratos bancários não corresponderão exatamente às datas da sua entrada, porque o banco costuma demorar a “compensar” esses pagamentos.


Além disso, você pode ter enviado um cheque ao seu fornecedor e pode levar alguns dias até que ele seja recebido e depositado pelo fornecedor. No ERPNext você pode sincronizar seus extratos bancários e seus Lançamentos Diários usando as datas das transações.


## 1. O que é um Extrato de Conciliação Bancária?


O Relatório de Conciliação Bancária fornece a diferença entre o saldo bancário apresentado no extrato bancário da organização, fornecido pelo banco, contra o valor apresentado no Plano de Contas da empresa.


É assim que um extrato de reconciliação bancária se parece:


![Extrato de reconciliação bancária](/files/bank-reconciliation-2.png)


No relatório, verifique se o campo 'Saldo conforme banco' corresponde ao Extrato da Conta Bancária. Se for coincidente, significa que a Data de Compensação está atualizada corretamente para todos os lançamentos bancários. Se houver desencontro, é devido a lançamentos bancários cuja Data de Liquidação ainda não foi atualizada.


Para acessar a Conciliação Bancária, acesse:



>
> Home > Contabilidade > Bancos e pagamentos > Atualizar data de transação bancária
>
>
>


## 2. Como atualizar datas de transações bancárias


1. Vá para Atualizar datas de transações bancárias.
2. Selecione sua conta bancária.
3. Selecione uma data de e até.
4. Você pode optar por incluir lançamentos reconciliados e transações PDV.
5. Clique no botão **Obter entradas de pagamento**.
6. Agora você terá todos os cadastros do tipo “Boleto Bancário”.
7. Em cada uma das entradas, na coluna mais à direita, atualize o campo “Data de Liberação” e clique no botão **Atualizar Data de Liberação**.


Ao fazer isso, você poderá sincronizar seus extratos bancários e lançamentos no sistema.


![Reconciliação Bancária](/files/bank-reconciliation.png)


## 3. Tipos de ferramentas de reconciliação


O ERPNext possui duas ferramentas de reconciliação:


1. Uma ferramenta de reconciliação manual que permite definir datas de compensação em relação a entradas de pagamento, pagamentos de faturas de vendas ou lançamentos contábeis manuais
2. Uma ferramenta de reconciliação semiautomática que permite compensar transações bancárias contra entradas de pagamento, pagamentos de faturas de vendas e compras, lançamentos contábeis manuais ou declarações de despesas.


### 3.1 Ferramenta Manual de Reconciliação Bancária


Para visualizar este relatório, vá para **Contas > Banco e Pagamentos > Extrato de Conciliação Bancária**. No relatório, verifique se o campo 'Saldo conforme banco' corresponde ao Extrato da Conta Bancária. Se for coincidente, significa que a Data de Compensação está atualizada corretamente para todos os lançamentos bancários. Se houver desencontro, é porque a Data de Compensação ainda não está atualizada para os lançamentos bancários.


### 3.2 Ferramenta de Reconciliação Bancária Semiautomática


É um processo de duas etapas:


1. Adicionar transações bancárias ao ERPNext via importação de extrato bancário ou sincronização de conta bancária
2. Conciliar o Extrato Bancário


#### 3.2.1 Importação de extrato bancário


1. Baixe um extrato bancário do site do seu banco


![Reconciliar transações bancárias](/files/sample_bank_statement.png)
Certifique-se de ter pelo menos a data, o débito/crédito e a moeda em cada linha do seu extrato bancário.


Para fazer o upload do seu Extrato Bancário, acesse:



>
> Contabilidade > Extrato bancário > Importação de extrato bancário
>
>
>


ou simplesmente procure por 'Importação de Extrato Bancário' na barra incrível.


1. Selecione sua Empresa e Conta Bancária
2. Clique em Salvar
3. Anexe o Extrato Bancário
4. Clique em 'Mapear Colunas' para inserir o mapeamento entre as colunas no Extrato Bancário carregado e no Tipo de Documento da Transação Bancária
5. Clique em Iniciar importação para iniciar o processo de importação. As transações bancárias serão criadas por meio de um trabalho em segundo plano, embora o progresso seja mostrado aqui


![Reconciliar transações bancárias](/files/bank_transaction_upload.gif)
6. O mapeamento realizado é armazenado no documento Banco vinculado à Conta Bancária correspondente. No próximo upload, o mapeamento é retirado daqui, mas o sistema permite que o usuário o altere, se necessário. O mapeamento alterado também é atualizado no documento do Banco.
![Reconciliar transações bancárias](/files/bank_configuration.png)


#### 3.2.2 Sincronização de Conta Bancária


Você pode usar o Plaid (consulte [Página de integrações do Plaid](/docs/v13/user/manual/en/erpnext_integration/plaid_integration)) para sincronizar automaticamente sua conta bancária com o ERPNext. Todas as suas transações bancárias serão automaticamente importadas para o ERPNext.


#### 3.2.3 Conciliar o Extrato Bancário


Depois que todas as suas transações bancárias forem importadas para o ERPNext, você poderá reconciliá-las com seus comprovantes existentes. Vá para:



>
> Contabilidade > Extrato bancário > Ferramenta de reconciliação bancária
>
>
>


ou simplesmente procure por 'Ferramenta de reconciliação bancária' na barra incrível.


1. Selecione sua empresa, conta bancária, data inicial e final do extrato bancário.
2. Certifique-se de que o saldo inicial do ERPNext corresponda ao saldo inicial do seu Extrato Bancário.
3. Insira o Saldo Final do Extrato Bancário.
4. Salvar o documento mostrará as transações bancárias correspondentes.
![Reconciliar transações bancárias](/files/bank_reconciliation_tool.png)
5. O objetivo final da Reconciliação Bancária é zerar o valor da diferença (verde), combinando com um voucher existente ou criando um novo voucher.
6. Para todas as movimentações bancárias que constam no Extrato Bancário mas não possuem data de compensação, clique no Botão Ações para Conciliar/Criar Comprovantes
7. Para combinar, escolha 'Combinar com Voucher' em 'Ação'. Serão exibidos os comprovantes relacionados a esta transação. Eles serão classificados com base no número máximo de campos correspondentes. Você pode combinar um ou vários vouchers com a mesma transação bancária usando as caixas de seleção.
![Reconciliar transações bancárias](/files/match_voucher.png)
8. Para criar um novo voucher, escolha 'Criar Voucher' na 'Acção' e depois escolha o tipo de documento. Preencha os dados que não estavam disponíveis na Transação Bancária. Clicar em Enviar criará o comprovante correspondente e atualizará sua data de liberação.
![Reconciliar transações bancárias](/files/create_voucher.png)
9. Também é possível atualizar as Movimentações Bancárias. Atualizar a Transação Bancária pode ajudar o ERPNext a encontrar correspondências melhores. Para atualizar uma transação bancária, escolha 'Atualizar transação bancária' em 'Ação', preencha os detalhes necessários e clique em Enviar para salvar a transação bancária.
![Reconciliar transações bancárias](/files/update_bank_transaction.png)


### 4. Tópicos Relacionados


1. [Reconciliação de pagamento](/docs/v13/user/manual/en/accounts/payment-reconciliation)
2. [Garantia Bancária](/docs/v13/user/manual/en/accounts/bank-guarantee)
3. [Entrada de pagamento](/docs/v13/user/manual/en/accounts/payment-entry)