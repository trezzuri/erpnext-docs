# Definir valor atual para série de nomenclatura



O recurso Naming Series permite definir o prefixo para nomear um documento. Por exemplo, se um Pedido de Venda tiver o prefixo "SO", então a série será gerada como SO-00001, SO-00002... e assim por diante. Clique [aqui](/docs/pt/setting-up/settings/naming-series.html) para saber como você pode personalizar a série numérica para uma transação/mestre no ERPNext .


### 1. Configurando o valor atual


O recurso Naming Series também oferece uma ferramenta onde você pode definir o valor atual para um prefixo específico. Isto geralmente é necessário se você começou a usar o ERPNext recentemente, e tem transações antigas no sistema anterior, e deseja que a série de numeração comece de onde terminou no sistema antigo. Vamos considerar um cenário para entender melhor isso.


Por exemplo, você tem 322 pedidos de vendas criados em seu sistema antigo com SO00322 como ID de pedido de vendas mais alto. No ERPNext, você precisa que o primeiro Pedido de Venda pegue o #323 quando for salvo. Para ativar isso, você deve definir o valor atual para a série SO nas etapas a seguir.


#### Vá para a ferramenta de nomeação de séries


`Configuração > Sistema > Nomeando séries`


#### Seção de atualização da série


![Atualizar seção da série](/files/current-no-1.png)


#### Selecionar prefixo


Considerando nosso cenário, o prefixo do Pedido de Venda será "SO".


![Series Prefix](/files/current-no-2.png)


#### Valor Atual


Se você tiver atualmente 12 pedidos de vendas criados em sua conta, o valor atual atualizado será 12. Você pode editar o valor atual para 322 e clicar em Atualizar número de série.


![Valor atual da série](/files/current-no-3.png)


Com esta configuração, você terá numeração para novos pedidos de vendas começando com #323.


### 2. Erro devido ao número da série


Se você receber um erro de Nome Duplicado ao salvar uma transação, por exemplo, ao salvar o Preço do Item, você receberá um erro dizendo:


`Nome duplicado Item Preço RFD/00016`


Esta mensagem de erro indica que quando você está salvando o Preço do Item, o sistema está tentando alocar "RFD/00016" para esse registro de Preço do Item. Mas verifica-se que o preço do item com este ID já existe em seu sistema.


Este erro pode surgir porque o valor atual da série/prefixo do preço do item está perturbado e não está sincronizado com o valor atual real. Embora o valor atual real do preço do item possa ser 20 (ou qualquer número maior que 16), alguém definiu o valor atual para esta série como 15.


Para confirmar o valor atual real para uma série específica, você deve verificar o relatório do documento em questão (preço do item neste caso) e verificar o ID do preço do item com valor mais alto.


Vamos supor que descobrimos que o valor atual real do preço do item é 22, então você nomeia a série e define o valor atual do prefixo/série do preço do item como 22 e atualiza o número da série.


Estas instruções são aplicáveis ​​a todos os documentos no ERPNext para os quais o usuário pode personalizar a Série e seu Valor Atual.


Vamos considerar outro cenário para aprender melhor. Ao atribuir um documento a outro usuário, a mensagem de erro diz:


`Nome duplicado ToDo TDI00014286`


Isso indica que o valor atual da série/prefixo do ToDo (TDI) foi perturbado. Você deve seguir estas etapas para corrigir o valor do valor atual do prefixo TDI.


1. Verifique o relatório ToDo para obter o valor de ID de ToDo mais alto.
2. Configuração >> Configurações >> Série de nomes
3. Verifique a seção B da série de atualizações
4. Selecione o prefixo para ToDo "TDI"
5. Certifique-se de que o número mais alto para tarefas pendentes seja atualizado como valor atual na série de nomenclatura. Caso contrário, corrija o valor atual e clique em "Atualizar numeração de série".




