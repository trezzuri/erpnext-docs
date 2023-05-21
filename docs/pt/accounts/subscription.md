# Inscrição


Se você oferece um serviço que exige renovação em um determinado período de tempo ou paga algumas despesas mensais como aluguel (anual, mensal, trimestral etc.), pode usar o recurso Assinatura do ERPNext para rastreá-las. O mestre de Assinatura captura todos os detalhes necessários para a criação automática de Faturas de Venda ou Compra.


Vamos considerar um caso de uso da própria assinatura do ERPNext. Nossos planos de hospedagem estão disponíveis anualmente. A conta de cada cliente tem uma data de vencimento da assinatura, após a qual os clientes devem renovar sua assinatura conosco.


Para gerenciar o vencimento da assinatura do cliente e a geração automática da Nota Fiscal de Venda para a renovação, usamos o recurso Assinatura.


Para acessar a lista de assinaturas, acesse:



>
> Home > Contabilidade > Gerenciamento de assinaturas > Assinatura
>
>
>


## 1. Pré-requisitos


Antes de criar e usar uma Assinatura, é aconselhável criar primeiro o seguinte:


1. [Plano de assinatura](/docs/v13/user/manual/en/accounts/plano de assinatura)


## 2. Como definir uma assinatura


1. Vá para a lista de Assinaturas e clique em Novo.
2. Selecione o Tipo de Parte como 'Cliente' ou 'Fornecedor' e selecione a parte.
3. Defina a Data de início a partir da qual a assinatura estará ativa.
4. Opcionalmente, você também pode inserir a data de término da assinatura se souber com antecedência.
5. Dias até o vencimento é o número de dias em que o Cliente deve pagar uma Fatura de venda gerada.
6. Selecione [Planos de assinatura](/docs/v13/user/manual/en/accounts/plano de assinatura).
7. Salve.
![Assinatura](/files/subscription.png)


Com base nas datas de início e término da assinatura, as datas reais das faturas serão calculadas.


## 3. Características


### 3.1 Período Experimental


Se você estiver oferecendo um período de avaliação para a assinatura, uma Data de início do período de avaliação e uma Data de término do período de avaliação podem ser definidas. As faturas não serão geradas durante o período de teste e o status da Assinatura mostrará 'Em teste'.
![Avaliação de assinatura](/files/subscription-trial.png)


### 3.2 Cancelar renovação automática


Ao habilitar o 'Cancelar no final do período', a Assinatura será cancelada no final de seu período. Por exemplo, se for uma assinatura anual, o sistema deixará de gerar faturas após um ano de assinatura.


### 3.3 Impostos


Você pode aplicar impostos a uma assinatura usando um modelo de impostos e cobranças sobre vendas. Visite a página [Modelo de impostos e cobranças sobre vendas](/docs/v13/user/manual/en/selling/sales-taxes-and-charges-template) para saber mais.


### 3.4 Aplicação de descontos


Você pode aplicar descontos adicionais na Assinatura com base no Total Geral (antes dos impostos) ou Total Líquido (após os impostos). Uma porcentagem de desconto também pode ser definida. Por exemplo, um desconto de 2% em 12.000 seria 240 de desconto.
 ![Desconto na assinatura](/files/subscription-discount.png)
Visite a página [Aplicando desconto](/docs/v13/user/manual/en/selling/articles/applying-discount) para mais detalhes.


### 3.5 Criar faturas automaticamente


Com base no intervalo [Planos de assinatura](/docs/v13/user/manual/en/accounts/plano de assinatura), as faturas serão criadas automaticamente. "Gerar fatura no início do período" precisa ser ativado se você deseja gerar faturas assim que a assinatura estiver ativa. Se "Gerar novas faturas vencidas" estiver ativado, novas faturas continuarão sendo geradas, mesmo que a fatura atual não seja paga ou vencida. Se "Gerar fatura com antecedência" estiver ativado, uma fatura será gerada antes do final do período pelo número de dias inserido em "Gerar fatura com dias de antecedência".


As faturas geradas serão enviadas automaticamente por padrão. Se 'Enviar fatura automaticamente' estiver desabilitado, a fatura será salva como rascunho.


![Faturas de assinatura](/files/subscription-invoices.png)


### 3.6 Siga os meses do calendário


Se 'Seguir os meses do calendário' estiver ativado, os meses do calendário apropriados serão seguidos, mesmo que a Data de início da assinatura seja no meio do mês. Por exemplo: suponha que o intervalo de cobrança seja 'Mês' e a contagem do intervalo de cobrança seja 3 no plano de assinatura e a Data de início da assinatura seja '15-04-2020', então, se 'Seguir meses do calendário' estiver marcado, a primeira fatura será gerada para '15- 04-2020' a '30-06-2020' em vez de '15-04-2020' a '14-07-2020'


### 3.8 Cancelando uma Assinatura


Se o Cliente decidir cancelar uma Assinatura, ela poderá ser cancelada no sistema usando **Cancelar Assinatura**. O sistema deixará de gerar faturas quando uma Assinatura for cancelada.
 ![Cancelamento de assinatura](/files/subscription-cancel.png)


### 3.9 Atualizando uma Assinatura


Clicar no botão **Fetch Subscription Updates** atualizará a assinatura com as últimas faturas geradas.


## 4. Diferença entre assinatura e repetição automática




| Repetição Automática | Assinatura |
| --- | --- |
| É aplicável em transações | É aplicável em Itens |
| Múltiplas transações como Pedido de Vendas, Pedido de Compra, Faturas, Lançamento Diário, etc. são criadas automaticamente | Apenas faturas de venda e faturas de compra são criadas automaticamente |
| Possui apenas alguns controles | Possui diversas opções de controle para definição de trial, vencimento de cobrança e criação de Planos de Assinatura |


### 5. Tópicos Relacionados


1. [Fatura de venda](/docs/v13/user/manual/en/accounts/fatura-de-venda)
2. [Fatura de compra](/docs/v13/user/manual/en/accounts/purchase-invoice)
3. [Item](/docs/v13/user/manual/en/stock/item)
4. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
5. [Plano de assinatura](/docs/v13/user/manual/en/accounts/subscription-plan)