# Reavaliação da taxa de câmbio


No ERPNext, você pode fazer lançamentos contábeis em várias moedas. Por exemplo, se você tiver uma conta bancária em moeda estrangeira, poderá fazer transações nessa moeda e o sistema mostrará o saldo bancário nessa moeda específica.


O objetivo do mestre de reavaliação da taxa de câmbio é ajustar o saldo nas contas do Razão de acordo com quaisquer alterações nas taxas de câmbio. Isso é útil quando você está fechando seus livros contábeis e deseja atualizar as contas contábeis da sua empresa trazendo o dinheiro de outras contas em moeda.


***Observação: A partir do ERPNext v14, a Reavaliação da Taxa de Câmbio pode lidar com Contas em Moeda Estrangeira com saldo '0' na Moeda Base ou na Moeda da Conta. Um diário separado do tipo 'Ganho/perda de câmbio' será criado no status de rascunho para eles.***


Para acessar a lista de Reavaliação da Taxa de Câmbio, acesse:



> 
> Página inicial > Contabilidade > Várias moedas > Reavaliação da taxa de câmbio
> 
> 
> 


## 1. Como configurar a moeda em uma conta


1. Para começar a usar a contabilidade multimoeda, você precisa atribuir a moeda contábil em um registro de conta.
2. Você pode definir a Moeda no Plano de Contas ao criar uma conta.


![Moeda no Ledger](/files/currency-in-ledger.png)
3. Você também pode atribuir/modificar a moeda para contas existentes abrindo o registro de conta específico.
4. Clique na conta e clique em Editar.


![Definir moeda da conta](/files/update-currency-in-ledger.png)


## 2. Como ativar a reavaliação da taxa de câmbio


O recurso de Reavaliação da Taxa de Câmbio é para lidar com a situação quando você tem contas com moedas diferentes no Plano de Contas de uma empresa.


1. Vá para: **Configuração > Empresa > *selecione a empresa***.
2. Defina o campo 'Conta de ganho/perda de troca não realizada' em Company DocType. Esta conta é para equilibrar a diferença entre o crédito total e o débito total.


![Ledger de ganhos/perdas de câmbio não realizado na empresa](/files/unrealized-exchange-gain-loss-ledger-in-company.png)
3. Vá para **Contabilidade > Configuração > Reavaliação da taxa de câmbio > Novo**.
4. Selecione a empresa.
5. Clique no botão 'Obter inscrições'. Ele buscará as contas com moeda diferente da 'Moeda padrão' definida na empresa.
6. Isto buscará a nova taxa de câmbio automaticamente se não for definido em Currency Exchange DocType para essa moeda, caso contrário, buscará a 'Taxa de câmbio' definida no [Câmbios](/docs/v13/user/manual/ pt/accounts/currency-exchange) DocType.
![Reavaliação da taxa de câmbio](/files/exchange-rate-revaluation.png)
7. Ao enviar, o botão **Criar entrada de diário** aparecerá.
![Opção de entrada de diário após o envio](/files/exchange-rate-revaluation-submit.png)
8. Clicar neste botão criará um lançamento contábil manual para a reavaliação da taxa de câmbio.
![Registro do diário de reavaliação da taxa de câmbio](/files/exchange-rate-revaluation-journal-entry.png)
9. Ao enviar o lançamento contábil manual, o razão geral é afetado da seguinte forma:
![Exchange Rate Revaluation GL](/files/exchange-rate-revaluation-gl.png)


### 3. Tópicos Relacionados


1. [Entrada no diário da empresa](/docs/pt/accounts/inter-company-journal-entry)
2. [Faturas entre empresas](/docs/pt/accounts/inter-company-invoices)
