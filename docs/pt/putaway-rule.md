# Regra de armazenamento



**Uma regra de armazenamento define uma estratégia de atribuição de armazém para o estoque recebido.**


Uma Regra de Armazenamento é definida exclusivamente para uma combinação Item-Armazém em uma Empresa. Leva em consideração a capacidade e a prioridade do armazém.


Em **Recebimentos de Compra** e **Entradas de Estoque** (Recebimento de Material e Transferência de Material), as Regras de Armazenamento são aplicadas e os Itens são **atribuídos automaticamente** aos Armazéns baseados na estratégia dada.


Isso é particularmente útil para gerenciamento de capacidade em grandes armazéns com vários locais.


Para acessar uma regra de armazenamento, acesse:


> Página inicial > Estoque > Transações de estoque > Regra de armazenamento


## 1. Pré-requisitos


Antes de criar e usar uma regra de armazenamento, é aconselhável criar primeiro o seguinte:


* [Item em estoque](/docs/pt/stock/item)
* [Armazém](/docs/pt/stock/warehouse)


## 2. Como criar uma regra de armazenamento


1. Vá para a lista Regra de armazenamento e clique em Novo.
![Regra de armazenamento não salva](/files/unsaved-putaway-rule.png)
2. Defina a empresa e selecione um item.
3. Selecione o armazém ao qual esta regra se aplica.
4. Defina a capacidade. Você também pode selecionar uma UDM se desejar definir a capacidade em uma UDM diferente. A UDM Capacidade em Estoque será definida automaticamente.
![Regra de armazenamento de múltiplas UOM](/files/multi-uom-putaway-rule.png)
5. Defina a prioridade. Isso pode começar de 1 em diante, sendo 1 a prioridade mais alta.
6. Salvar.
7. Você também pode desativar uma regra de armazenamento.


A regra é exclusiva para cada combinação Item-Armazém.


## 3. Como o armazenamento é planejado


1. Aqui a estratégia é puramente baseada em **Capacidade** e **Prioridade**.
2. Os armazéns serão atribuídos automaticamente até atingirem a capacidade total.
3. A prioridade será considerada primeiro. Seguido de espaço livre. Se duas regras tiverem a mesma prioridade, será atribuída a regra com mais espaço livre disponível.
4. Se você estiver operando com capacidade total (sem espaço livre em nenhum armazém), o ERPNext irá informá-lo.


## 4. Como funciona


Conforme mencionado anteriormente, as Regras de Armazenamento são aplicadas em **Recebimentos de Compra** e **Entradas de Estoque** (Recebimento e Transferência de Material).


Uma caixa de seleção chamada **Aplicar regra de armazenamento** alocará itens aos armazéns com base nas regras de armazenamento.
 ![Caixa de seleção Aplicar regra de armazenamento](/files/apply-putaway-rule.png)


As regras de armazenamento são aplicadas ao marcar esta caixa de seleção. Eles também serão aplicados novamente ao salvar se esta caixa de seleção estiver ativada.


Vejamos o mesmo em ação:


1. Aqui está um pedido de compra com exigência de 5 caixas (60 Nos) de água mineral.
![Ordem de compra](/files/po-putaway-demo.png)
2. Duas regras de armazenamento ativas foram criadas abaixo, com capacidade para 4 caixas (48 números) cada. Um tem uma prioridade maior que o outro.
![Lista de regras de armazenamento ativo](/files/active-putaway-rules-list.png)
3. Um recibo de compra é criado a partir deste pedido de compra.
4. Ao marcar **Aplicar regra de armazenamento**, uma linha de 5 caixas é dividida e atribuída de acordo com as regras.
![Regras de armazenamento aplicadas em um recibo de compra](/files/pr-putaway-apply.gif)
5. Primeiro, 4 em cada 5 caixas são acomodadas no Armazém de 'Produtos Acabados-UPI'. Quando este Armazém estiver lotado, ele atribui o restante (1 Caixa) ao Armazém 'Lojas-UPI'.


## 5. Resumo da capacidade do armazém


O relatório **Resumo da capacidade do armazém** mostra as capacidades do armazém e seus respectivos níveis de estoque.


Somente armazéns com regras de armazenamento serão listados aqui. O botão **Editar capacidade** permite editar a capacidade da regra de armazenamento.


![Resumo da capacidade do armazém](/files/warehouse-capacity-summary.png)


## 6. Tipos de aplicação de armazenamento


### 6.1. Armazenamento direto


1. O exemplo da seção anterior explica o **armazenamento direto**.
2. É, essencialmente, atribuir diretamente o estoque recebido a determinados Armazéns com base em uma estratégia.
3. Isso pode ser facilmente exercido por meio de um recibo de compra.


### 6.2. Armazenamento indireto (combinado)


1. O estoque geralmente é recebido primeiro em armazéns **temporários** ou **de preparação**.
2. A partir daqui, ele é colocado em locais apropriados dentro do Armazém.
3. Isso é chamado de armazenamento **indireto ou combinado**.
4. Para simular isto dentro do ERPNext, um simples Recibo de Compra pode ser criado no Armazém temporário, sem aplicação de Armazenamento.
5. A partir daqui, uma entrada de estoque (transferência de material) pode ser feita, onde as regras de armazenamento podem ser aplicadas de forma semelhante aos recibos de compra.


## 7. Tópicos Relacionados


1. [Recibo de compra](/docs/pt/stock/purchase-receipt)
2. [Entrada de estoque](/docs/pt/stock/stock-entry)



