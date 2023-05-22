# Definir valor atual para nomear séries


O recurso Naming Series permite que você defina o prefixo para nomear um documento. Por exemplo, se um Pedido de Venda tiver o prefixo "SO", então a série será gerada como SO-00001, SO-00002... e assim sucessivamente. Clique [aqui](/docs/pt/setting-up/settings/naming-series.html) para saber como você pode personalizar o Number Series para uma transação/mestre no SOMA .


### 1. Definindo o valor atual


O recurso de série de nomes também oferece uma ferramenta onde você pode definir o valor atual para um prefixo específico. Isso geralmente é necessário se você começou a usar o SOMA recentemente e possui transações antigas no sistema anterior e deseja que a série de numeração comece de onde terminou no sistema antigo. Vamos considerar um cenário para aprender isso melhor.


Por exemplo, você tem 322 pedidos de vendas criados em seu sistema antigo com SO00322 como ID de pedido de vendas mais alto. No SOMA, você precisa que o primeiro Pedido de Venda seja retirado #323 quando for salvo. Para habilitar isso, você deve definir o valor atual para a série SO nas etapas a seguir.


#### Ir para a Ferramenta de Nomeação de Séries


`Configuração > Sistema > Série de nomes`


#### Seção de atualização da série


![Update Series Section](/files/current-no-1.png)


#### Selecione o prefixo


Considerando nosso cenário, o prefixo do pedido de vendas será "SO".


![Series Prefix](/files/current-no-2.png)


#### Valor atual


Se você tiver atualmente 12 pedidos de vendas criados em sua conta, o valor atual atualizado será 12. Você pode editar o valor atual para 322 e, em seguida, clicar em Atualizar número de série.


![Valor atual da série](/files/current-no-3.png)


Com esta configuração, você terá a numeração para os Novos Pedidos de Venda começando com #323.


### 2. Número de série devido ao erro


Se você receber um erro de nome duplicado ao salvar uma transação, por exemplo, ao salvar o preço do item, receberá um erro dizendo:


`Nome duplicado Preço do item RFD/00016`


Esta mensagem de erro indica que, quando você está salvando o Preço do Item, o sistema está tentando alocar "RFD/00016" para esse registro de Preço do Item. Mas está descobrindo que o preço do item com esse ID já existe em seu sistema.


Este erro pode ocorrer porque o valor atual da série/prefixo do preço do item está alterado e não está sincronizado com o valor atual real. Embora o valor atual real para o preço do item possa ser 20 (ou qualquer número maior que 16), alguém definiu o valor atual para esta série como 15.


Para confirmar o valor atual real para uma série específica, você deve verificar o relatório do documento em questão (preço do item neste caso) e verificar a ID do preço do item com o valor mais alto.


Vamos supor que descobrimos que o valor atual real para o preço do item é 22, então você vai nomear a série e define o valor atual para o prefixo/série do preço do item como 22 e atualiza o número da série.


Estas instruções são aplicáveis ​​a todos os documentos no SOMA para os quais o usuário pode personalizar a Série e seu Valor Atual.


Vamos considerar outro cenário para aprender melhor. Ao atribuir um documento a outro usuário, a mensagem de erro diz:


`Nome duplicado ToDo TDI00014286`


Isto indica que o valor atual da série/prefixo de ToDo (TDI) foi alterado. Você deve seguir estas etapas para corrigir o valor do valor atual para o prefixo TDI.


1. Verifique o relatório ToDo para obter o maior valor de id ToDo.
2. Configuração >> Configurações >> Série de nomes
3. Verifique a seção B da Série de Atualização
4. Selecione o prefixo para ToDo "TDI"
5. Certifique-se de que o número mais alto para ToDo seja atualizado como Current Value em Noming Series. Caso contrário, corrija o valor atual e clique em "Atualizar numeração de série".


