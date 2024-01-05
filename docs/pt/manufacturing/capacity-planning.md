# Planejamento de capacidade baseado em ordem de serviço



A funcionalidade de planejamento de capacidade ajuda você a rastrear trabalhos de produção alocados em cada estação de trabalho.


![Permissão do Role Desk](/files/capacity-1.png)


A seguir estão as etapas para usar o recurso de planejamento de capacidade em sua conta ERPNext.


1. Operações


Para adicionar operações, acesse:


`Fabricação > Lista de materiais > Operações`
2. Estação de trabalho


Adicione cada estação de trabalho na sua conta ERPNext de:


`Fabricação > Lista de materiais > Estação de trabalho`


No mestre de Estações de Trabalho você pode definir quais operações serão realizadas nela, quais os custos associados a elas e quais são os horários de funcionamento daquela Estação de Trabalho.
3. Lista de materiais (BOM):


Em uma lista técnica, com a lista de matérias-primas necessárias para a fabricação, você também pode listar as operações e as estações de trabalho através das quais essas matérias-primas serão processadas.
4. Ordem de serviço:


No envio da Ordem de Serviço, Quadro de Horários de Operações. Isso ajuda você a alocar trabalhos de produção em cada estação de trabalho, bem como a atualizar o tempo real gasto em cada operação.


  

**Erro devido ao planejamento de capacidade**


**Pergunta:** Ao enviar a ordem de serviço, estamos recebendo a seguinte mensagem de erro.


![Permissão do Role Desk](/files/capacity-2.png)


*\*Resposta: \**Verifique se você atualizou o horário de trabalho no mestre de estações de trabalho. Caso contrário, atualize-o e tente enviar a Ordem de Serviço.


Ao enviar a Ordem de Serviço, as Operações (conforme adicionadas na BOM) são alocadas na estação de trabalho. Cada operação deve começar e terminar no mesmo dia. Se um sistema não conseguir agendar essa operação em um dia, o sistema solicitará que você divida esse projeto, para que o sistema possa alocar operações menores em um dia.


Se você atualizou o horário de trabalho na estação de trabalho, mas ainda está tendo esse problema, é porque uma de suas operações está demorando muito e não pode ser concluída em um dia. Divida essa operação em operações menores, para que possa ser alocada na estação de trabalho e concluída no mesmo dia.


  

**Evite horário de trabalho na estação de trabalho**


Se você deseja ignorar a validação acima e permitir o agendamento do trabalho de produção além do horário de trabalho da Estação de Trabalho, habilite
Horas extras nas configurações de fabricação.


![Permissão do Role Desk](/files/capacity-3.png)


Se você deseja desativar o recurso Planejamento de Capacidade, nas Configurações de Fabricação, marque o campo "Desativar Planejamento de Capacidade e Controle de Tempo".



