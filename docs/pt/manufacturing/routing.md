# Roteamento



**O roteiro é um modelo de operações de BOM.**


Um roteiro armazena todas as operações junto com a descrição, taxa horária, tempo de operação, tamanho do lote, etc. Criar um roteiro para suas operações de BOM é útil quando operações semelhantes são usadas para fabricar itens diferentes.


Para acessar a lista de roteamento, vá para:



> 
> Página inicial > Fabricação > Lista de materiais > Roteamento
> 
> 
> 


## 1. Pré-requisitos


* [Operação](/docs/pt/manufacturing/operation)
* [Estação de trabalho](/docs/pt/manufacturing/workstation)


## 2. Como criar uma rota


1. Vá para a lista Roteamento e clique em Novo.
2. Insira um nome para a rota.
3. Insira as operações na tabela de operações da BOM:
	1. Selecione a operação.
	2. A estação de trabalho padrão será buscada.
	3. Insira a taxa horária para executar esta operação.
	4. Insira o tempo de operação em minutos.
	5. Insira o Tamanho do Lote, ou seja, o número de unidades processadas nesta Operação.
	6. O Custo Operacional será calculado com base na Taxa Horária e no Tempo de Operação.
4. Salvar.


![Routing](/files/routing.png)


Uma vez criado, um Roteiro pode ser selecionado em uma BOM para buscar as Operações armazenadas no Roteiro.
![Routing BOM](/files/routing-bom.png)


## 3. ID de sequência no roteamento


![ID de sequência de roteamento](/files/sequence-id-routing.png)
O ID de sequência obriga os usuários a concluir as operações sequencialmente por meio do cartão de trabalho. Caso um usuário tente concluir uma operação antes de concluir qualquer uma de suas operações precedentes de acordo com o ID de sequência, o sistema gera um erro de validação.



## 2. Tópicos Relacionados


1. [Ordem de serviço](/docs/pt/manufacturing/work-order)
2. [Lista de materiais](/docs/pt/manufacturing/bill-of-materials)



