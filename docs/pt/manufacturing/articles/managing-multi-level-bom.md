# Gerenciamento de BOM multinível



Considere um cenário em que seu processo de fabricação envolva a produção de itens de submontagem antes do produto final. Neste caso, como você deve gerenciar a lista técnica?


Primeiro de tudo, você precisa ter BOMs para as submontagens, então essas BOMs devem estar vinculadas à BOM do produto final acabado. Na captura de tela a seguir, você pode ver que a lista técnica de cerdas do pincel (submontagem) está vinculada à lista técnica do pincel de barbear (produto final). Isso é visto na tabela Materiais no mestre da Lista de Materiais.


![BOM multinível](/files/multi-bom.png)


A tabela 'Materiais' mostrará apenas os subconjuntos, enquanto a tabela 'Materiais necessários (explodidos)' mostrará todas as matérias-primas necessárias para fabricar o produto final.


Tabela de materiais da BOM onde a submontagem é mostrada:
![BOM multinível](/files/bom-materials.png)


Na vista explodida apenas as matérias-primas são mostradas:
![BOM multinível](/files/bom-materials-exploded.png)


Para usar BOM multinível em uma ordem de serviço, ative a caixa de seleção 'Usar BOM multinível'. Isso é ativado por padrão. Se você deseja planejar materiais para submontagens do item que você está fabricando, deixe esta opção habilitada. Se você planeja e fabrica as submontagens separadamente, desative esta caixa de seleção.


Vamos considerar outro exemplo para entender melhor isso, onde um computador está sendo montado. O disco rígido e a unidade de DVD também estão sendo fabricados e são subconjuntos. A lista técnica multinível ou aninhada terá esta aparência:


* Computador pessoal (item FG)
	+ Placa mãe
	+ SMTP
	+ Acessórios e fios
	+ Disco rígido (submontagem)
		- Item A
		- Item B
		- Item C
	+ Unidade de DVD (subconjunto)
		- Item X
		- Item Y
		- Item Z


## Cuidado


Tenha cuidado ao atualizar a BOM de uma submontagem. A peça que inclui a submontagem com uma BOM atualizada precisará ser atualizada para fazer referência à BOM atualizada dessa peça. O resultado prático disso é que a troca de um parafuso em uma montagem de baixo nível levará a uma onda de listas de materiais atualizadas na estrutura da lista de materiais.


Usando o exemplo do computador pessoal acima.
O computador pessoal (PC-001 com BOM-PC-001) usa disco rígido (HDD-001 com BOM-HDD-001).
BOM-HDD-001 inclui os três itens mostrados (Item A, B e C).


Se precisarmos trocar o Item C por um novo item (Item D) então devemos atualizar a criação do BOM-HDD-002 (com os Itens A, B e D). O disco rígido (HDD-001) é então atualizado para fazer referência ao novo BOM-HDD-002. Porém, BOM-PC-001 ainda faz referência ao HDD-001 com BOM-HDD-001. A mudança do Item C para o Item D não será atualizada na BOM explodida para PC-001.


BOM-PC-002 deve ser criado referenciando HDD-001 com BOM-HDD-002 para fazer esta atualização.



