# Ferramenta de atualização de BOM



**Na ferramenta de atualização de BOM, você pode substituir uma BOM de submontagem e atualizar os custos de todas as BOMs principais.**


Usando este utilitário, você pode substituir uma BOM existente de um item de submontagem que esteja vinculado a uma BOM pai. O sistema atualizará a nova BOM em todas as BOMs pai onde ela foi usada. Você precisa criar uma nova BOM primeiro.


Para usar a ferramenta de atualização de BOM, acesse:


> Home > Fabricação > Ferramentas > Ferramenta de atualização de BOM


## 1. Como usar a ferramenta de atualização de BOM


Vamos considerar um cenário para entender isso melhor.


Suponha que uma empresa fabrique computadores, a lista de materiais do computador será semelhante a esta:


1. Monitorar
2. Teclado
3. Rato
4. CPU


De todos os itens acima, a CPU é montada separadamente. Portanto, uma lista técnica separada será criada para a CPU. A seguir estão os itens da BOM da CPU.


1. Disco rígido de 250 GB
2. Placa-mãe
3. Processador
4. SMTP
5. Leitor de DVD


Se for necessário adicionar mais itens ou editar itens existentes na BOM da CPU, crie uma nova BOM para eles.


1. *Disco rígido de 950 GB*
2. Placa-mãe
3. Processador
4. SMTP
5. Leitor de DVD


Selecione a BOM atual e a nova BOM do item de **submontagem**:


![Ferramenta de atualização de BOM](/files/bom-update-tool.png)


Para atualizar a nova BOM em todas as BOMs pai, onde a CPU está selecionada como submontagem, você pode usar o botão **Substituir**.


Ao clicar no botão Substituir, a BOM antiga da CPU será substituída pela nova BOM na BOM do item finalizado (Computador).


**A ferramenta de substituição de BOM funcionará para substituir os itens explodidos na BOM pai?**


Não, itens explodidos que não possuem nenhuma BOM própria não podem ser substituídos na BOM pai. Por exemplo, considere se o Monitor de Itens não possui uma submontagem e não pode ser atualizado usando esta ferramenta. Para atualizar itens explodidos, você deve cancelar e alterar a lista técnica atual ou criar uma nova lista técnica para o item finalizado.


## Atualizar custo da BOM


Usando o botão **Atualizar último preço em todas as listas técnicas**, você pode atualizar o custo de todas as listas de materiais, com base no último preço de compra/taxa de lista de preços/taxa de avaliação de matérias-primas. Isso é útil se sua BOM atualizada tiver materiais com taxas diferentes.


Ao clicar neste botão, o sistema criará um processo em background para atualizar todos os custos da BOM. Ele é processado por meio de trabalhos em segundo plano porque esse processo pode levar alguns minutos (dependendo do número de BOMs) para atualizar todas as BOMs.


Esta funcionalidade também pode ser executada automaticamente diariamente. Para isso, você precisa ativar "Atualizar custo da lista de materiais automaticamente" nas configurações de fabricação.



