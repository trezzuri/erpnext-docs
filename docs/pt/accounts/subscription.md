# Assinatura


Se você oferece um serviço que exige renovação em um determinado período de tempo ou paga algumas despesas mensais como aluguel (anual, mensal, trimestral etc.), pode usar o recurso Assinatura do SOMA para rastreá-las. O mestre de assinatura captura todos os detalhes necessários para a criação automática de faturas de venda ou compra.


Vamos considerar um caso de uso da própria assinatura do SOMA. Nossos planos de hospedagem estão disponíveis anualmente. A conta de cada cliente tem uma data de vencimento da assinatura, após a qual os clientes devem renovar sua assinatura conosco.


Para gerenciar o vencimento da assinatura do cliente e a geração automática da Nota Fiscal de Venda para a renovação, usamos o recurso Assinatura.


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
2. Selecione o Tipo de Parte como 'Cliente' ou 'Fornecedor' e selecione a parte.
3. Defina a data de início a partir da qual a assinatura estará ativa.
4. Opcionalmente, você também pode inserir a data de término da assinatura se souber com antecedência.
5. Dias até o vencimento é o número de dias em que o Cliente deve pagar uma fatura de venda gerada.
6. Selecione [Planos de assinatura](/docs/pt/accounts/subscription-plan).
7. Salvar.
![Subscription](/files/subscription.png)


Com base nas datas de início e término da assinatura, as datas reais das faturas serão calculadas.


## 3. Recursos


### 3.1 Período de avaliação


Se você estiver oferecendo um período de avaliação para a assinatura, uma Data de início do Período de avaliação e uma Data de término do período de avaliação podem ser definidas. As faturas não serão geradas durante o período de teste e o status da Assinatura mostrará 'Em teste'.
![Subscription Trial](/files/subscription-trial.png)


### 3.2 Cancelar renovação automática


Ao habilitar 'Cancelar no final do período', a Assinatura será cancelada no final de seu período. Por exemplo, se for uma assinatura anual, o sistema deixará de gerar faturas após um ano de assinatura.


### 3.3 Impostos


Você pode aplicar impostos a uma assinatura usando um modelo de impostos e cobranças sobre vendas. Visite a página [Modelo de impostos e cobranças sobre vendas](/docs/pt/selling/sales-taxes-and-charges-template) para saber mais.


### 3.4 Aplicação de descontos


Você pode aplicar descontos adicionais na Assinatura com base no Total Geral (antes dos impostos) ou Total Líquido (após os impostos). Uma porcentagem de desconto também pode ser definida. Por exemplo, um desconto de 2% em 12.000 seria 240 de desconto.
 ![Desconto na assinatura](/files/subscription-discount.png)
Visite a página [Como aplicar desconto](/docs/pt/selling/articles/applying-discount) para obter mais detalhes.


### 3.5 Criar faturas automaticamente


Com base no intervalo [Planos de assinatura](/docs/pt/accounts/subscription-plan), as faturas serão criadas automaticamente. "Gerar fatura no início do período" precisa ser ativado se você deseja gerar faturas assim que a assinatura estiver ativa. Se "Gerar novas faturas vencidas" estiver ativado, novas faturas continuarão sendo geradas, mesmo que a fatura atual não seja paga ou vencida. Se "Gerar fatura com antecedência" estiver ativado, uma fatura será gerada antes do final do período pelo número de dias inserido em "Gerar fatura com dias de antecedência".


As faturas geradas serão enviadas automaticamente por padrão. Se 'Enviar fatura automaticamente' estiver desativado, a fatura será salva como rascunho.


![Subscription Invoices](/files/subscription-invoices.png)


### 3.6 Siga os meses do calendário


Se 'Seguir os meses do calendário' estiver ativado, os meses do calendário apropriados serão seguidos, mesmo que a Data de início da assinatura esteja no meio do mês. Por exemplo: suponha que o intervalo de cobrança seja 'Mês' e a contagem do intervalo de cobrança seja 3 no plano de assinatura e a Data de início da assinatura seja '15-04-2020', então, se 'Seguir meses do calendário' estiver marcado, a primeira fatura será gerada para '15- 04-2020' a '30-06-2020' em vez de '15-04-2020' a '14-07-2020'


### 3.8 Cancelando uma assinatura


Se o Cliente decidir cancelar uma Assinatura, ela poderá ser cancelada no sistema usando **Cancelar Assinatura**. O sistema deixará de gerar faturas quando uma Assinatura for cancelada.
 ![Subscription Cancel](/files/subscription-cancel.png)


### 3.9 Atualizando uma assinatura


Clicar no botão **Buscar atualizações de assinatura** atualizará a assinatura com as últimas faturas geradas.


## 4. Diferença entre assinatura e repetição automática




| Repetição automática | Assinatura |
| --- | --- |

| Aplicável em transações | Aplicável a itens |

| Múltiplas transações, como Pedido de Vendas, Pedido de Compra, Faturas, Lançamento Diário, etc., são criadas automaticamente | Somente faturas de venda e faturas de compra são criadas automaticamente |

| Possui apenas alguns controles | Tem muitas opções de controle para definir testes, data de vencimento da cobrança e criar planos de assinatura |




### 5. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
3. [Item](/docs/pt/stock/item)
4. [Cliente](/docs/pt/CRM/customer)
5. [Plano de assinatura](/docs/pt/accounts/subscription-plan)
