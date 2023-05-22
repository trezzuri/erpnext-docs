# Consolidação de Fatura PDV


Na refatoração da versão 13 do Ponto de Venda, em um esforço para adicionar velocidade ao Ponto de Venda, as vendas da sessão de PDV não afetam o estoque e os livros contábeis até que um Voucher de fechamento de PDV seja enviado para essa sessão . Funciona assim: 


1. Cada transação da tela do PDV agora cria uma fatura intermediária (chamada de Fatura do PDV) que não atualiza o estoque e os livros contábeis para mantê-la o mais rápido possível. Isso também é chamado de “sub-livro”. Separar o razão PDV do Razão Geral torna o sistema muito mais escalável.
2. Os registos de stock e contabilísticos são agora criados ao final do dia ao fechar uma sessão de PDV por uma única fatura de venda que mescla todas as faturas intermediárias criadas ao longo do dia.
3. Esta única fatura de venda consolidada cria apenas 3-4 lançamentos contábeis. O sistema antigo criaria n x 3 lançamentos contábeis onde 'n' é o número de faturas criadas ao longo do dia.
4. Como são feitas drasticamente menos entradas no razão, a carga no razão geral também é facilitada, tornando-o mais rápido.


### Como o estoque é rastreado até que uma sessão de PDV seja fechada


Embora seja verdade que o livro-razão de estoque excluirá as transações de qualquer sessão de PDV ativa, os níveis de estoque deste "sub-livro" atualizam o relatório de quantidade projetada de estoque.



> 
> Estoque > Relatórios de estoque > Quantidade projetada de estoque
> 
> 
> 


![Relatório de quantidade projetada de estoque](/files/36.png)


Na imagem acima, a coluna "Quantidade real" representa o valor do registro de estoque. O "Reservado para transações de PDV" representa a "Quantidade real" menos as quantidades atualmente reservadas devido a sessões de PDV ativas que ainda não fizeram entradas no Razão de Estoque porque as sessões não foram encerradas. Observe também que "Quantidade projetada" ("Quantidade ativa" menos quantidades reservadas para PDV, produção etc.) adiciona uma quantidade de 100 ao primeiro item de linha devido a um pedido de 100 unidades que ainda não foi recebido.


No ponto de venda, no entanto, as quantidades solicitadas, mas não recebidas, não serão refletidas no campo "Quantidade disponível no depósito" na exibição Detalhes do item. No caso abaixo, como não há quantidade suficiente em mãos, a transação não será permitida. Isso se aplica a toda e qualquer sessão aberta de PDV ativa a qualquer momento e é aplicada globalmente (como em, a transação de uma sessão afeta as quantidades disponíveis para todas as outras sessões abertas).


![Quantidade disponível no depósito](/files/37.png)


![Item indisponível](/files/38.png)

