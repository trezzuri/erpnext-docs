# Gerenciando frações na UOM



UoM significa Unidade de Medida. Poucos exemplos de UM são Números (Nos), Kgs, Litro, Metro, Caixa, Caixa, etc.


Existem poucas UOMs que não podem ter valor em casas decimais. Por exemplo, se tivermos televisão para um item, com Ns como unidade de medida, não podemos ter 1,5 Nºs de televisão ou 3,7 Nºs de aparelhos de computador. O valor da quantidade desses itens deve ser um número inteiro.


Você pode configurar se determinada UM pode ter valor em casa decimal ou não. Por padrão, serão permitidos valores em casas decimais para todas as UOMs. Para restringir casas decimais ou valores fracionários para qualquer unidade de medida, siga estas etapas.


#### Lista UOM


Para lista UOM, vá para:


`Estoque > Configuração > Unidade de medida`


Na lista de UOM, selecione UOM cujo valor em casa decimal será restrito. Vamos supor que a UM seja Nos.


#### Configurar


Na UoM mestre, você encontrará um campo chamado "Deve ser um número inteiro". Marque este campo para impedir que o usuário insira o valor em casas decimais no campo de quantidade, para o item que possui esta UOM.


![UoM deve ser inteiro Não](/files/uom-fraction-1.png)


#### Validação


Ao criar a transação, se você inserir o valor em fração para o item cuja UOM tenha a opção "Deve ser um número inteiro" marcada, você receberá uma mensagem de erro informando:


`A quantidade não pode ser uma fração na linha #`


![Mensagem de validação da unidade de medida](/files/uom-fraction-2.png)




