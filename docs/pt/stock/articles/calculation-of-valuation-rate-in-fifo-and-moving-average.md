# Diferença de cálculo do FIFO e da média móvel



A Taxa de Avaliação de um item é calculada com base nas despesas totais incorridas para disponibilizar o produto para venda, como frete, mão de obra, custo de matéria-prima, etc.

No ERPNext, Taxa de Avaliação é calculado com base no método de avaliação selecionado para o item específico. 

Um item pode ter FIFO ou Média Móvel selecionada como método de avaliação. 

Considere o exemplo a seguir para saber como isso afeta seu estoque:



| **Data** **Transação** | **Quantidade** | **Custo unitário** | |
| 1-4-2020 | Comprar | 10 | 100 |
| 6-4-2020 | Compra | 20 | 120 |
| 10-4-2020 | Venda | 15 | ? |

  
Cálculo da taxa de avaliação no momento da venda:

**De acordo com o FIFO:**

Como este é o FIFO, consumiremos quantidades das *primeiras* transações, portanto, para fazer uma venda de 15 quantidades, pegaremos 10 quantidades da primeira transação e 5 quantidades da segunda. 

(10 \* 100) + (5 \* 120) = 1600, o que nos deixa 15 quantidades em estoque ao custo de 120, totalizando **1800**.

 **De acordo com a média móvel:**

No método da média móvel, o valor de um item é *recalculado* *toda vez* quando um item é adquirido. Isso é feito adicionando o custo dos itens recém-adquiridos ao valor do estoque existente e dividindo-o pela quantidade total disponível. 

((10 \* 100) + (20 \* 120))/30 = 113,33

Para fazer uma venda de 15 quantidades, multiplicaremos diretamente pelo valor médio que recebemos agora mesmo. 

15 \* 113,33 = 1700, o que nos deixa 15 quantidades em estoque, totalizando **1700**.

Se você verificar, mesmo que a quantidade seja a mesma, o estoque o valor é diferente, mas ambos equivalem a um total de apenas 3.400. 



