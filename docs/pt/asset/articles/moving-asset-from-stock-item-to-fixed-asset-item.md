# Movimento de ativo de item de estoque para item de ativo fixo



**Pergunta:** Adicionamos um item de ativo como item de estoque/consumível. Como mover este item para o registro de Ativo Fixo, para que a Depreciação possa ser aplicada a ele?  
**Resposta:** Por favor, siga os passos fornecido abaixo para que o item de estoque seja movido para item de ativo fixo.  
### **Estocagem de item consumível**

  
1. Crie uma entrada de estoque do tipo **Emissão de material**
2. Selecionar itens , com o respectivo armazém de origem, onde o estoque do item está disponível.
3. Para um item, selecione "Ajuste de estoque" como conta de diferença.

  
Ao submeter esta Entrada de Stock, o artigo em questão estará completamente esgotado no seu Armazém. Além disso, a avaliação do item será debitada na Conta de Ajuste de Estoque.  
###  **Adicionando item como item de ativo fixo**

  
1. Crie um novo ativo em Ativos > Novo
2. No Ativo master, selecione Item e insira os detalhes relevantes
3. Selecione "É ativo existente" como **Sim**.

  
E novamente, para atualizar fixo conta de ativo, você deve passar um lançamento contábil manual onde poderá debitar a conta de ativo fixo e creditar a conta de ajuste de estoque.

