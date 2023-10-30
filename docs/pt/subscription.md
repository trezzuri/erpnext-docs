# Assinatura



Se você oferece um serviço que requer renovação em um determinado período de tempo ou paga algumas despesas mensais como aluguel (anual, mensal, trimestral, etc.), você pode usar o recurso de Assinatura no ERPNext para rastreá-las. O mestre de assinaturas captura todos os detalhes necessários para a criação automática de faturas de vendas ou compras.


Vamos considerar um caso de uso da própria assinatura do ERPNext. Nossos planos de hospedagem estão disponíveis anualmente. A conta de cada Cliente tem uma data de expiração da assinatura, após a qual os clientes devem renovar sua assinatura conosco.


Para gerenciar o vencimento da assinatura do cliente e a geração automática da fatura de vendas para a renovação, usamos o recurso Assinatura.


Para acessar a lista de assinaturas, acesse:



> 
> Página inicial > Contabilidade > Gerenciamento de assinaturas > Assinatura
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar uma Assinatura, é aconselhável criar primeiro o seguinte:


1. [Plano de assinatura](/docs/pt/accounts/subscription-plan)


## 2. Como definir uma assinatura


1. Vá para a lista de assinaturas e clique em Novo.
2. Selecione o tipo de parte como 'Cliente' ou 'Fornecedor' e selecione a parte.
3. Defina a data de início a partir da qual a assinatura estará ativa.
4. Opcionalmente, você também pode inserir a data de término da assinatura, caso saiba disso de antemão.
5. Dias Até o Vencimento é o número de dias dentro dos quais o Cliente tem que pagar uma Fatura de Vendas gerada.
6. Selecione os [Planos de assinatura](/docs/pt/accounts/subscription-plan).
7. Salvar.
![Subscription](/files/subscription.png)


Com base nas datas de início e término da assinatura, as datas reais das faturas serão calculadas.


## 3. Recursos


### 3.1 Período de teste


Se você estiver oferecendo um período de avaliação para a assinatura, uma data de início e uma data de término do período de avaliação poderão ser definidas. As faturas não serão geradas durante o período de teste e o status da assinatura mostrará 'Em teste'.
![Teste de assinatura](/files/subscription-trial.png)


### 3.2 Cancelar renovação automática


Ao ativar o 'Cancelar no final do período', a assinatura será cancelada no final do seu período. Por exemplo, se for uma assinatura anual, o sistema deixará de gerar faturas após um ano de assinatura.


### 3.3 Impostos


Você pode aplicar impostos a uma assinatura usando um modelo de impostos e cobranças sobre vendas. Visite a página [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template) para saber mais.


### 3.4 Aplicação de descontos


Você pode aplicar descontos adicionais à Assinatura com base no Total Geral (antes de impostos) ou no Total Líquido (pós-impostos). Uma porcentagem de desconto também pode ser definida. Por exemplo, um desconto de 2% em 12.000 seria 240 de desconto.
 ![Desconto de assinatura](/files/subscription-discount.png)
Visite a página [Aplicando desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.5 Criar faturas automaticamente


Com base no intervalo dos [Planos de assinatura](/docs/pt/accounts/subscription-plan), as faturas serão criadas automaticamente. "Gerar fatura no início do período" precisa estar habilitado se você quiser gerar faturas assim que a assinatura estiver ativa. Se "Gerar novas faturas com data de vencimento vencida" estiver ativado, novas faturas continuarão sendo geradas mesmo que a fatura atual não tenha sido paga ou tenha vencido. Se a opção "Gerar fatura antecipada" estiver ativada, uma fatura será gerada antes do final do período pelo número de dias inserido em "Gerar dias de fatura antecipada".


As faturas geradas serão enviadas automaticamente por padrão. Se a opção "Enviar fatura automaticamente" estiver desativada, a fatura será salva como rascunho.


![Faturas de assinatura](/files/subscription-invoices.png)


### 3.6 Seguir meses do calendário


Se 'Seguir Meses do Calendário' estiver ativado, os meses do calendário apropriados serão seguidos mesmo que a Data de Início da Assinatura seja no meio do mês. Por exemplo: suponha que o intervalo de cobrança seja 'Mês' e a contagem do intervalo de cobrança seja 3 no plano de assinatura e a data de início da assinatura seja '15-04-2020', então se 'Seguir meses do calendário' estiver marcado, a primeira fatura será gerada para '15-04-2020' para '30-06-2020' em vez de '15-04-2020' para '14-07-2020'


### 3.8 Cancelamento de uma assinatura


Se o Cliente decidir cancelar uma Assinatura, ela poderá ser cancelada no sistema usando o botão **Cancelar Assinatura**. O sistema irá parar de gerar faturas quando uma Assinatura for cancelada.
 ![Cancelamento de assinatura](/files/subscription-cancel.png)


### 3.9 Atualizando uma assinatura


Clicar no botão **Obter atualizações de assinatura** atualizará a assinatura com as últimas faturas geradas.


## 4. Diferença entre assinatura e repetição automática




| Repetição automática | Assinatura |
| --- | --- |

| É aplicável em transações | É aplicável em itens |

| Várias transações, como pedido de vendas, pedido de compra, faturas, lançamento contábil manual, etc., são criadas automaticamente | Somente faturas de vendas e faturas de compra são criadas automaticamente |

| Possui apenas alguns controles | Tem muitas opções de controle para definir testes, data de vencimento de cobrança e criação de planos de assinatura |



### 5. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Item](/docs/pt/stock/item)
4. [Cliente](/docs/pt/CRM/customer)
5. [Plano de assinatura](/docs/pt/accounts/subscription-plan)




