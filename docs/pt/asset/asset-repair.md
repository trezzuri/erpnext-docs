# Reparo de ativos



**Reparo de ativos refere-se a qualquer atividade realizada para reparar um ativo quebrado para restaurar a funcionalidade completa.**


Você também pode manter registros de Reparos/Falhas de Ativos que não estão listados em Manutenção de Ativos.


Para acessar a lista de Reparo de ativos, vá para:



> 
> Página inicial > Ativos > Manutenção > Reparo de ativos
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar o Asset Repair, é aconselhável criar primeiro o seguinte:


* [Ativo](/docs/pt/asset/asset)


## 2. Como criar um reparo de ativos


1. Vá para a lista Reparo de ativos e clique em Novo.
2. Selecione o recurso.
3. Selecione a data da falha.
4. Insira o custo do reparo.
5. Salvar.
6. Altere o status do reparo de 'Pendente' para 'Concluído' ou 'Cancelado'.
7. Selecione uma fatura de compra se o custo de reparo for maior que zero.
8. Salvar e enviar.


![Asset Repair](/files/Asset Repair.png)



> 
> Observação: como alternativa, você pode abrir o registro do ativo em questão e clicar no botão **Reparar ativo** em **Gerenciar** e seguir as etapas 3 a 8.
> 
> 
> 


### 2.1 Opções adicionais ao criar um reparo de ativo


* **Capitalizar Custo de Reparo**: Se marcado, o Custo de Reparo será adicionado ao valor do Ativo. Isso também pode permitir que você aumente a vida útil do recurso.
* **Aumento da vida útil do ativo (meses)**: O número de meses pelos quais a vida útil do ativo pode ser estendida pelo reparo pode ser adicionado aqui. Isso modificará o Cronograma de Depreciação do Ativo. Este campo só estará visível se a opção Capitalizar custo de reparo estiver marcada.


![Reparo de ativos com Capitalize Repair Cost verificado](/files/Capitalize Repair Cost.png)


* **Estoque consumido durante o reparo**: marcar esta opção permitirá que você anote todos os itens de estoque consumidos durante o reparo.
* **Armazém**: O Armazém de onde foram retirados os Itens de Estoque consumidos durante o reparo deve ser inserido aqui, se o Estoque Consumido Durante o Reparo estiver marcado.
* **Itens de Estoque**: Inserir Itens de Estoque consumidos durante o reparo aqui criará um registro de Entrada de Estoque do tipo Emissão de Material para eles, diminuindo assim sua quantidade. Entradas GL também serão criadas para cada item da tabela. Esta tabela só será visível se a opção Estoque Consumido Durante o Reparo estiver marcada. No caso de itens serializados, a linha do item pode ser expandida para revelar o botão *Adicionar número de série*.


![Reparo de ativo com estoque consumido durante o reparo verificado](/files/Estoque consumido durante o reparo.png)


* **Descrição do erro**: Uma descrição detalhada do problema pode ser inserida aqui.
* **Ações realizadas**: Uma sequência de ações realizadas para realizar o reparo pode ser anotada aqui.


![Seção de descrição de reparo de ativos](/files/Description Section.png)


## 3. Recursos


### 3.1 Dimensões contábeis


As dimensões contábeis permitem marcar transações com base em um território, filial, cliente específico etc. Isso ajuda a visualizar os demonstrativos contábeis separadamente com base nas dimensões selecionadas. Para saber mais, consulte a ajuda no recurso [Dimensões contábeis](/docs/user/manual/en/accounts/accounting-dimensions).



> 
> Observação: Projeto e Centro de Custo são tratados como dimensões por padrão.
> 
> 
> 


### 3.2 Fatura de compra


Uma Fatura de Compra pode ser vinculada ao Reparo de Ativos, para contabilizar quaisquer Itens que precisem ser adquiridos para realizar o reparo ou o serviço de reparo oferecido.


### 3.3 Custo total de reparo


Se a opção Estoque Consumido Durante o Reparo estiver marcada, o Custo Total do Reparo será calculado com base no valor dos Itens de Estoque consumidos e no Custo do Reparo inserido.


## 4. Tópicos Relacionados


1. [Manutenção de ativos](/docs/pt/asset/asset-maintenance)
2. [Ajuste do valor do ativo](/docs/pt/asset/asset-value-adjustment)



