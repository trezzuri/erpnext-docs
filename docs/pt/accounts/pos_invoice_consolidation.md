# Consolidação de faturas de PDV



No refatoramento da versão 13 do Ponto de Venda, em um esforço para adicionar velocidade ao Ponto de Venda, as vendas da sessão de PDV não afetam o estoque e os livros contábeis até que um Voucher de Fechamento do PDV seja enviado para essa sessão . Funciona assim: 


1. Cada transação na tela do PDV agora cria uma fatura intermediária (chamada fatura do PDV) que não atualiza o estoque e os livros contábeis para mantê-la o mais rápido possível. Isso também é chamado de “sub-livro”. Separar o razão do PDV do Razão Geral torna o sistema muito mais escalonável.
2. Os lançamentos de estoque e contábeis agora são criados no final do dia ao fechar uma sessão de PDV por meio de uma única fatura de venda que mescla todas as faturas intermediárias criadas ao longo do dia.
3. Essa única fatura de vendas consolidada cria apenas de 3 a 4 entradas no razão. O sistema mais antigo criaria n x 3 entradas contábeis, onde ‘n’ é o número de faturas criadas ao longo do dia.
4. Como são feitas drasticamente menos entradas no razão, a carga no razão geral também é facilitada, tornando-a mais rápida.


### Como o estoque é rastreado até que uma sessão de PDV seja fechada


Embora seja verdade que o livro razão de estoque excluirá transações de qualquer sessão de PDV ativa, os níveis de estoque deste "livro auxiliar" atualizam o relatório de quantidade projetada de estoque.



> 
> Estoque > Relatórios de estoque > Quantidade projetada de estoque
> 
> 
> 


![Relatório de quantidade projetada de estoque](/files/36.png)


Na imagem acima, a coluna "Quantidade Real" representa o valor do razão de ações. O “Reservado para Transações de PDV” representa a “Qtd Real” menos quais quantidades estão atualmente reservadas devido às sessões de PDV ativas que ainda não efetuaram lançamentos no Razão de Estoque porque as sessões não foram encerradas. Observe também que "Qtd Projetada" ("Qtd Ativa" menos quantidades reservadas para PDV, produção, etc.) adiciona uma quantidade de 100 ao primeiro item de linha devido a um pedido de 100 unidades que ainda não foi recebido.
No entanto, no Ponto de Venda, as quantidades encomendadas mas não recebidas não serão refletidas no campo "Quantidade disponível no armazém" na visualização Detalhes do item. No caso abaixo, como não há quantidade suficiente em mãos, a transação não será permitida. Isso se aplica a toda e qualquer sessão de PDV aberta a qualquer momento e é aplicado globalmente (por exemplo, a transação de uma sessão afeta as quantidades disponíveis para todas as outras sessões abertas).


![Quantidade disponível no armazém](/files/37.png)


![Item indisponível](/files/38.png)





