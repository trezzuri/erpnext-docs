# Reconciliação Bancária



**Uma entrada de Reconciliação Bancária é usada para combinar os extratos da conta ERPNext com os extratos da sua conta bancária.**

Se você estiver recebendo pagamentos ou fazendo pagamentos através de cheques, o banco os extratos não corresponderão exatamente às datas de sua entrada, isso ocorre porque o banco geralmente demora para “compensar” esses pagamentos. Além disso, você pode ter enviado um cheque ao seu Fornecedor e pode levar alguns dias até que ele seja recebido e depositado pelo Fornecedor. 

No ERPNext você pode sincronizar seus extratos bancários e seus lançamentos contábeis manuais usando as datas das transações. 

## 1. O que é um extrato de reconciliação bancária?

O Relatório de Reconciliação Bancária fornece a diferença entre o saldo bancário mostrado no extrato bancário de uma organização, conforme fornecido pelo banco, em relação ao valor mostrado no Plano de Contas da empresa. 

Esta é a aparência de um extrato de reconciliação bancária: ![Declaração de reconciliação bancária](/files/bank-reconciliation-2.png)

No relatório, verifique se o campo 'Saldo por banco' corresponde ao Extrato da conta bancária. Se for coincidente, significa que a Data de Liquidação está atualizada corretamente para todos os lançamentos bancários. Se houver inconsistência é por causa de lançamentos bancários cuja Data de Liquidação ainda não foi atualizada. 

Para acessar a Reconciliação Bancária, vá para: 


> Home > Contabilidade > Bancos e Pagamentos > Atualizar Data da Transação Bancária 
> 
> 

## 2. Como atualizar datas de transações bancárias

* Vá para **Liquidação Bancária**.
* Selecione sua conta bancária.
* Selecione uma data de e até.
* Você pode optar por incluir entradas reconciliadas e transações de PDV.
* Clique no botão **Obter entradas de pagamento**.
* Agora você receberá todas as entradas do tipo “Voucher Bancário”.
* Em cada uma das entradas, na coluna mais à direita, atualize o campo **Data de liberação** e clique em **Atualizar data de liberação** botão. Ao fazer isso, você poderá sincronizar seus extratos bancários e lançamentos no sistema.

![Screenshot 19/06/2023 às 18h1632](/files/Screenshot 19/06/2023 às 18h1632.png "Screenshot 19/06/2023 às 18h1632.png")

## 3. Tipos de ferramentas de reconciliação

O ERPNext possui duas ferramentas de reconciliação: 

1. Uma ferramenta de reconciliação manual que permite definir datas de liquidação em relação a lançamentos de pagamento, pagamentos de faturas de vendas ou lançamentos contábeis manuais
2. Uma ferramenta de reconciliação semiautomática que permite compensar transações bancárias em relação a entradas de pagamento, pagamentos de faturas de vendas e compras, lançamentos contábeis manuais ou relatórios de despesas.

### 3.1 Ferramenta manual de reconciliação bancária

Para visualizar este relatório, vá para:


> Contas > Bancos e Pagamentos > Extrato de Conciliação Bancária
> 
> 

No relatório, verifique se o campo 'Saldo por banco' corresponde ao Extrato de Conta Bancária. Se for coincidente, significa que a Data de Liquidação está atualizada corretamente para todos os lançamentos bancários. Se houver inconsistência é porque a Data de Liquidação ainda não está atualizada para os lançamentos bancários. 

### 3.2 Ferramenta semiautomática de reconciliação bancária

É um processo de duas etapas: 

1. Adicionar transações bancárias ao ERPNext por meio de extrato bancário Importação ou sincronização de conta bancária
2. Reconciliar o extrato bancário

#### 3.2.1 Importação de extrato bancário

* Baixe um extrato bancário do site do seu banco ![Reconcile bank transaction](/files/sample_bank_statement.png)Certifique-se de ter pelo menos a data, o débito/crédito e a moeda em cada linha do seu extrato bancário. Para enviar seu extrato bancário, acesse: 


> **Contabilidade > Extrato bancário > Importação de extrato bancário** 
> 
> 

Ou simplesmente pesquise **Importação de extrato bancário** na barra incrível.
* Selecione sua empresa e conta bancária
* Clique em Salvar
* Anexe o extrato bancário
* Clique em **Mapear colunas** para inserir o mapeamento entre as colunas no extrato bancário carregado e no DocType da transação bancária
* Clique em Iniciar importação para iniciar o processo de importação. As transações bancárias serão criadas por meio de um trabalho em segundo plano, embora o progresso seja mostrado aqui ![Reconcile bank transaction](/files/bank_transaction_upload.gif)
* O mapeamento realizado fica armazenado no documento bancário vinculado à conta bancária correspondente. No próximo upload, o mapeamento é retirado daqui, mas o sistema permite ao usuário alterá-lo se necessário. O mapeamento alterado também é atualizado no documento do Banco. ![Reconciliar transações bancárias](/files/bank_configuration.png)

#### 3.2.2 Sincronização de contas bancárias

Você pode usar o Plaid (consulte a [página Integrações do Plaid](/docs/pt/erpnext_integration/plaid_integration)) para sincronizar automaticamente sua conta bancária com o ERPNext. Todas as suas transações bancárias serão importadas automaticamente para o ERPNext. 

#### 3.2.3 Correspondência automática de partes para transações bancárias

Opcionalmente, você pode ativar a correspondência automática de partes para que uma parte seja definida automaticamente (se correspondida) na transação bancária. Para ativar isso, vá para: 


> Configurações de contas > Banco > Ativar correspondência automática de partes 
> 
> 

![Screenshot 19/06/2023 às 5h58 0,51 PM](/files/Screenshot 19/06/2023 às 17h58.51.png "Screenshot 19/06/2023 às 17h58.51.png")

 Você também pode marcar **Ativar correspondência difusa** , onde o nome/descrição da parte na transação bancária corresponde **aproximadamente** a todas as partes no sistema. Isto é útil quando a conta bancária da parte não está registrada no sistema.

Uma vez ativado, a correspondência da parte acontecerá automaticamente no **envio** da transação bancária. 

Para auxiliar no mapeamento, você pode armazenar facilmente dados bancários de **Cliente**, **Fornecedor** e **Funcionário** criando um [Conta bancária](/docs/pt/accounts/bank-account) contra partes individuais. **Após o Envio**, o Tipo de Parte e Parte na Transação Bancária serão automaticamente definidos e poderão ser corrigidos/atualizados. 


> Os resultados da correspondência difusa dependem da natureza dos dados das partes existentes no sistema. Pode não ser preciso quando existem várias partes com nomes extremamente semelhantes.   
>   
> Seria melhor testar esse recurso primeiro:   
> 1. Ativando o recurso   
> 2. Ter alguns registros de festas no sistema   
> 3. Criação de uma transação bancária onde o nome/descrição da parte contém o nome da parte alvo   
> 4. Envio da transação bancária após a qual a parte deverá ser automaticamente definida na Transação Bancária. Aqui você pode determinar se os resultados são aceitáveis.
> 
> 

#### 3.2.4 Reconciliar o extrato bancário

Depois que todas as suas transações bancárias forem importadas para o ERPNext, você poderá reconciliá-las com seus vouchers existentes. Vá para: 


> Contabilidade > Extrato Bancário > Ferramenta de Reconciliação Bancária 
> 
> 

Ou simplesmente procure por **Ferramenta de Reconciliação Bancária** na barra incrível. 

* Selecione sua empresa, conta bancária, data de início e término do extrato bancário.
* Certifique-se de que o saldo inicial do ERPNext corresponda o saldo inicial do seu extrato bancário.
* Insira o saldo final do extrato bancário.
* Salvar o documento mostrará as transações bancárias correspondentes. ![Reconciliar transações bancárias](/files/bank_reconciliation_tool.png)
* O objetivo final da Reconciliação Bancária é fazer com que o valor da diferença zero (verde) combinando com um voucher existente ou criando um novo voucher.
* Para todas as transações bancárias que estão presentes no extrato bancário, mas não possuem um data de liquidação, clique no botão Ações para combinar/criar vouchers
* Para combinar, escolha 'Combinar com voucher' em 'Ação'. Serão exibidos os vouchers relacionados a esta transação. Eles serão classificados com base no número máximo de campos correspondentes. Você pode combinar um ou vários vouchers com a mesma transação bancária usando as caixas de seleção. ![Reconciliar transações bancárias](/files/match_voucher.png)
* Para criar um novo voucher, escolha 'Criar voucher ' em 'Ação' e escolha o tipo de documento. Preencha os dados que não estavam disponíveis na Transação Bancária. Clicar em Enviar criará o voucher correspondente e atualizará sua data de liquidação. ![Reconcile banking transaction](/files/create_voucher.png)
* Também é possível atualizar as transações bancárias. Atualizar a Transação Bancária pode ajudar o ERPNext a encontrar melhores correspondências. Para atualizar uma transação bancária, escolha 'Atualizar transação bancária' em 'Ação', preencha os dados necessários e clique em Enviar para salvar a transação bancária. ![Reconciliar transações bancárias](/files/update_bank_transaction.png)

### 4. Tópicos relacionados

* [Reconciliação de pagamento](/docs/pt/accounts/payment-reconciliation)
* [Garantia Bancária](/docs/pt/accounts/bank-guarantee)
* [Entrada de pagamento](/docs/pt/accounts/payment-entry)


