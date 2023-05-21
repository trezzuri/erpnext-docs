# Reavaliação da Taxa de Câmbio


No ERPNext, você pode fazer lançamentos contábeis em várias moedas. Por exemplo, se você tiver uma conta bancária em moeda estrangeira, poderá fazer transações nessa moeda e o sistema mostrará o saldo bancário nessa moeda específica.


O objetivo do mestre de reavaliação da taxa de câmbio é ajustar o saldo nas contas do Razão de acordo com quaisquer alterações nas taxas de câmbio. Isso é útil quando você está fechando seus livros contábeis e deseja atualizar as contas contábeis da sua empresa trazendo o dinheiro de outras contas em moeda.


***Observação: A partir do ERPNext v14, a Reavaliação da Taxa de Câmbio pode lidar com Contas em Moeda Estrangeira com saldo '0' na Moeda Base ou na Moeda da Conta. Um Diário Separado do tipo 'Ganho/Perda de Câmbio' será criado no status de rascunho para eles.***


Para acessar a lista de Reavaliação da Taxa de Câmbio, acesse:



>
> Home > Contabilidade > Multi Moeda > Reavaliação da Taxa de Câmbio
>
>
>


## 1. Como configurar a moeda em uma conta


1. Para iniciar a contabilidade multimoeda, você precisa atribuir a moeda contábil em um registro de Conta.
2. Você pode definir a Moeda no Plano de Contas ao criar uma conta.


![Moeda no razão](/files/currency-in-ledger.png)
3. Você também pode atribuir/modificar a moeda para contas existentes abrindo o registro de conta específico.
4. Clique na conta e clique em Editar.


![Definir moeda da conta](/files/update-currency-in-ledger.png)


## 2. Como habilitar a reavaliação da taxa de câmbio


O recurso de Reavaliação da Taxa de Câmbio é para lidar com a situação quando você tem contas com moedas diferentes no Plano de Contas de uma Empresa.


1. Acesse: **Configuração > Empresa > *selecione a empresa***.
2. Defina o campo 'Conta de ganho/perda de troca não realizada' em Company DocType. Esta conta é para equilibrar a diferença entre o crédito total e o débito total.


![Ledger de ganhos/perdas de câmbio não realizados na empresa](/files/unrealized-exchange-gain-loss-ledger-in-company.png)
3. Vá para **Contabilidade > Configuração > Reavaliação da taxa de câmbio > Novo**.
4. Selecione a Empresa.
5. Clique no botão 'Obter inscrições'. Ele buscará as contas que possuem moeda diferente da 'Moeda Padrão' definida na Empresa.
6. Isso buscará a nova taxa de câmbio automaticamente se não for definido no DocType de câmbio para essa moeda, caso contrário, ele buscará a 'Taxa de câmbio' definida no [Câmbio](/docs/v13/user/manual/en/accounts/ câmbio) DocType.
![Reavaliação da taxa de câmbio](/files/exchange-rate-revaluation.png)
7. Ao enviar, o botão **Create Journal Entry** aparecerá.
![Opção de entrada de diário após o envio](/files/exchange-rate-revaluation-submit.png)
8. Clicar neste botão criará um lançamento contábil manual para a reavaliação da taxa de câmbio.
![Entrada do diário de reavaliação da taxa de câmbio](/files/exchange-rate-revaluation-journal-entry.png)
9. Ao enviar o Lançamento Diário, o razão geral é afetado da seguinte forma:
![GL de reavaliação da taxa de câmbio](/files/exchange-rate-revaluation-gl.png)


### 3. Tópicos Relacionados


1. [Entrada no diário da empresa](/docs/v13/user/manual/en/accounts/entrada do diário na empresa)
2. [Faturas entre empresas](/docs/v13/user/manual/en/accounts/inter-company-invoices)