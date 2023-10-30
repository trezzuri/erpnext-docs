# Planejamento de capacidade baseado na ordem de produção



A funcionalidade de planejamento de capacidade ajuda você a rastrear trabalhos de produção alocados em cada estação de trabalho.


![](/files/Screenshot 30/01/2017 às 20h06.24.png)


A seguir estão as etapas para usar o recurso de planejamento de capacidade em sua conta ERPNext.


**Operações**


Para adicionar operações, acesse: Fabricação > Lista de materiais > Operações


**Estação de trabalho**


Adicione cada estação de trabalho em sua conta ERPNext em: Fabricação > Lista de materiais > Estação de trabalho


No mestre de Estações de Trabalho você pode definir quais operações serão realizadas nela, quais os custos associados a elas e quais são os horários de funcionamento daquela Estação de Trabalho.


**Lista de materiais (BOM)**


Em uma lista técnica, com a lista de matérias-primas necessárias para a fabricação, você também pode listar as operações e as estações de trabalho através das quais essas matérias-primas serão processadas.


**Ordem de produção**


No envio da Ordem de Produção, Quadro de Horários de Operações. Isso ajuda você a alocar trabalhos de produção em cada estação de trabalho, bem como a atualizar o tempo real gasto em cada operação.


--


**Pergunta** : Ao enviar a ordem de produção, estamos recebendo a seguinte mensagem de erro.


![](/files/Screenshot 30/01/2017 às 20h12.40.png)


**Resposta**: Verifique se você atualizou o horário de trabalho no mestre de estações de trabalho. Caso contrário, atualize-o e tente enviar o pedido de produção. Ao enviar a Ordem de Produção, as Operações (conforme adicionadas na BOM) são alocadas na estação de trabalho. Cada operação deve começar e terminar no mesmo dia. Se um sistema não conseguir agendar essa operação em um dia, o sistema solicitará que você divida esse projeto, para que o sistema possa alocar operações menores em um dia. Se você atualizou o horário de trabalho na estação de trabalho, mas ainda está tendo esse problema, é porque uma de suas operações está demorando muito e não pode ser concluída em um dia. Divida essa operação em operações menores, para que possa ser alocada na estação de trabalho e concluída no mesmo dia.



