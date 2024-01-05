# Reavaliação da taxa de câmbio



No ERPNext, você pode fazer lançamentos contábeis em múltiplas moedas. Por exemplo, se você tiver uma conta bancária em moeda estrangeira, poderá fazer transações nessa moeda e o sistema mostrará o saldo bancário nessa moeda específica.

O objetivo do mestre de reavaliação cambial é ajustar o saldo nas contas do Razão Geral de acordo com quaisquer alterações nas taxas de câmbio. Isto é útil quando você está fechando seus livros contábeis e deseja atualizar as contas contábeis da sua empresa trazendo o dinheiro de contas de outras moedas.

***Nota: Do ERPNext v14, Reavaliação da Taxa de Câmbio pode lidar com contas em moeda estrangeira com saldo '0' na moeda base ou na moeda da conta. Um Diário Separado do tipo 'Ganhos/Perdas Cambiais' será criado em status de rascunho para eles.***

Para acessar a lista de Reavaliação da Taxa de Câmbio, vá para:

 
> Home > Contabilidade > Multimoedas > Reavaliação da Taxa de Câmbio
> 
> 

## 1. Como configurar a moeda em uma conta

1. Para começar a usar a contabilidade multimoeda, você precisa atribuir a moeda contábil em um registro de conta.
2. Você pode definir a moeda no plano de contas ao criar uma conta.

![Moeda no razão](/files/currency-in-ledger.png)![]()
3. Você também pode atribuir/modificar a moeda para contas existentes abrindo o registro específico da conta.
4. Clique na conta e clique em Editar. 

![Definir moeda da conta](/files/update-currency-in-ledger.png)![]()

## 2. Como ativar a reavaliação da taxa de câmbio

O recurso de reavaliação da taxa de câmbio serve para lidar com a situação quando você tem contas com moedas diferentes no plano de contas de uma empresa.

1. Vá para: **Configuração > Empresa > *selecione a empresa***.
2. Defina o campo 'Conta de ganhos/perdas cambiais não realizados' no DocType da empresa. Esta conta serve para equilibrar a diferença entre o crédito total e o débito total.

![Ledger de ganhos/perdas cambiais não realizados na empresa](/files/unrealized-exchange-gain-loss-ledger-in-company.png)![]()
3. Vá para **Contabilidade > Configuração > Reavaliação da taxa de câmbio > Novo**.
4. Selecione a empresa .
5. Clique no botão 'Obter inscrições'. Ele buscará as contas que possuem moeda diferente da 'Moeda Padrão' definida na Empresa.
6. Isso buscará a nova taxa de câmbio automaticamente se não estiver definida no DocType de Câmbio de Moedas para essa moeda, caso contrário, ele buscará a 'Taxa de câmbio' definida em  [Câmbio de moeda](/docs/pt/accounts/currency-exchange) DocType. ![Reavaliação da taxa de câmbio](/files/exchange-rate-reavaliação.png)![]()
7. Ao enviar, o botão **Criar entrada de diário** aparecerá. ![Opção de entrada de diário após envio](/files/exchange-rate-revaluation-submit.png)![]()
8. Clicar neste botão criará um lançamento contábil manual para a reavaliação da taxa de câmbio. ![Lançamento diário de reavaliação da taxa de câmbio](/files/exchange-rate-reavaliação-journal-entry.png)![]()
9. Ao enviar o lançamento contábil manual, o razão geral é afetado da seguinte forma: ![Reavaliação da taxa de câmbio GL](/files/exchange-rate-reavaliação-gl.png)![]()

### 3. Criação automatizada de reavaliação de taxa de câmbio

A provisão para criação automática de reavaliação de taxa de câmbio está disponível no mestre da empresa em `**Configurações de reavaliação de taxa de câmbio**`

![Screenshot 10/07/2023 às 11h52/17](/files/Screenshot 10/07/2023 às 11h52/17.png "Screenshot 2023/07-10 às 11h52.17.png")![]()  


### 4. Tópicos relacionados

1. [Lançamento contábil entre empresas](/docs/pt/accounts/inter-company-journal-entry)
2. [Faturas entre empresas](/docs/pt/accounts/inter-company-invoices)


