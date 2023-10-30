# Modelo de condições de pagamento



**O modelo de condições de pagamento permite agrupar várias condições de pagamento e buscar transações.**

Após a criação, a tabela de condições de pagamento pode ser definida para um cliente específico/Fornecedor. Ao selecionar o Cliente/Fornecedor em uma transação, o Modelo de Condições de Pagamento será buscado automaticamente na transação.

Por exemplo:

Se você receber o pagamento na faixa de 30-70 , então você pode definir o Prazo de Pagamento para cada placa, ou seja, 30% e 70%.

No Modelo de Condições de Pagamento, você pode selecionar todas as Condições de Pagamento e definir um modelo que possa ser facilmente aplicado nas vendas e transações de compra.

![Modelo de termos de pagamento](/files/payment-terms-template.png)   


## 1. Pré-requisitos

Antes de criar e usar a Solicitação de Pagamento, é aconselhável criar primeiro os seguintes:

1. [Condições de pagamento](/docs/pt/accounts/payment-terms)

## 2. Como criar um modelo de condições de pagamento

Um modelo de condições de pagamento informa ao ERPNext como preencher a tabela na seção 'Cronograma de condições de pagamento' do documento de vendas/compra.

Você deve usar use-o se você tiver um conjunto de condições de pagamento padrão ou para facilidade de uso.

1. Vá para a lista de modelos de condições de pagamento e clique em Novo.
2. Insira um nome para o modelo.
3. Adicione as condições de pagamento criadas nas linhas da tabela.
4. Certifique-se de que a parcela total da fatura seja 100.
5. Salve.

## 3. Vídeo

### 4. Alocação de pagamento baseada em prazo

Se 'Alocar pagamento com base em termos de pagamento' estiver habilitado em um modelo, os pagamentos feitos na fatura através de Criar->Pagamento terão alocação baseada nos Termos.

1. Modelo com 'Alocar pagamento com base nas condições de pagamento' ativado. ![Screenshot 2023-08-01 às 10h30.32](/files/Screenshot 2023-08-01 às 10h30.32.png "Screenshot 2023-08-01 às 10h30.32.png")
2. Fatura feita acima modelo. ![Screenshot 2023-08-01 às 10.32.01 AM](/files/Screenshot 2023-08-01 às 10.32.01 AM.png "Screenshot 2023-08-01 às 10.32.01 AM.png")
3. Pagamento criado acima fatura. ![Screenshot 2023-08-01 às 10h32.31](/files/Screenshot 2023-08-01 às 10h32.31.png "Screenshot 2023-08-01 às 10h32.31.png")


