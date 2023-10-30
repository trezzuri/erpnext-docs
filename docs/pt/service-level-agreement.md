# Acordo de nível de serviço



**Um acordo de nível de serviço (SLA) é um contrato entre um provedor de serviços (interno ou externo) e o usuário final sobre o nível de serviço esperado do provedor de serviços.**


Os SLAs são baseados em resultados e seu objetivo é definir especificamente o cronograma em que o Cliente receberá o serviço. Os SLAs não definem como o serviço em si é fornecido ou entregue.


Para acessar a lista de Acordo de Nível de Serviço, acesse:
> Página inicial > Suporte > Acordo de nível de serviço > Acordo de nível de serviço


## 1.Pré-requisitos


Antes de criar e usar um Acordo de Nível de Serviço, é aconselhável que você crie/atualize primeiro o seguinte:


* [Lista de feriados](/docs/pt/human-resources/holiday-list)
* Ative **Acompanhar acordo de nível de serviço** nas configurações de suporte


![Acordo de nível de serviço](/files/sla-setting.png)


## 2. Como criar um acordo de nível de serviço


1. Vá para a lista de Acordo de Nível de Serviço e clique em Novo.
2. Insira um nome para o nível de serviço.
3. Selecione um grupo de funcionários que cuidará de um determinado nível de serviço.
4. Defina uma lista de feriados. O Acordo de Nível de Serviço não será aplicado nos dias mencionados na Lista de Feriados.
5. 'Ativar' determina se um Acordo de Nível de Serviço está ativado ou desativado.
6. Marcar 'Acordo de nível de serviço padrão' aplicará este SLA a um cliente se ele não tiver um SLA específico atribuído a ele.
7. Tipo de entidade: os acordos de nível de serviço podem ser atribuídos a um cliente/grupo de clientes/território, permitindo que você aplique o acordo de nível de serviço com base nesses fatores.
8. Entidade: selecione o cliente/grupo de clientes/território específico.
9. Data de início/término: define a validade do contrato.
10. Prioridades: você pode definir várias prioridades de problemas e seu tempo para responder e resolver (em horas e minutos).


![Nível de serviço](/files/priorities.png)
11. Prioridade Padrão: Prioridade Padrão selecionada na tabela Prioridades que será aplicada no Acordo de Nível de Serviço.
12. Horário de suporte: contém os dias da semana em que o suporte é fornecido. Tem hora de início e hora de término do dia útil.


![Horário de suporte do SLA](/files/sla-support-hours.png)
13. Salvar.


![SLA](/files/sla.png)


## 3. Recursos


### 3.1 Aplica-se a novos problemas


Depois que um SLA for salvo, ele será aplicado aos problemas levantados pelos clientes/territórios conforme a opção escolhida em 'Tipo de entidade'.


![SLA em questão](/files/sla-entity-type.png)


### 3.2 Redefinindo um SLA


Um SLA também pode ser redefinido até que o tempo não falhe. Por exemplo, se o SLA for de 3 dias, você poderá redefinir o SLA somente dentro de 3 dias após a criação do problema. Depois disso, o nível de serviço será exibido com falha.


![Problema de SLA](/files/reset-sla.gif)


### 3.3 Tempo de resposta/resolução de problemas


O tempo para responder a um problema e o tempo para resolver serão mostrados:
 ![SLA em questão](/files/sla-in-issue.png)


Esses tempos são baseados nos cronogramas definidos no campo 'Prioridade' na tabela Prioridades do nível de serviço.


### 3.4 Pausar SLA em status


A partir da versão 13, o ERPNext permite pausar o SLA em problemas quando você está aguardando a ocorrência de um evento. Você pode fazer isso selecionando um status configurado na tabela "Pausar SLA ativado".


* Defina os status nos quais você deseja pausar o SLA no documento de SLA. Você também pode adicionar status personalizados aqui.
![Nível de serviço](/files/pause-sla.png)
* Quando o status é alterado para qualquer um dos itens acima, os campos de resolução e resposta são desdefinidos e os indicadores do painel mudam para:
![Nível de serviço](/files/hold-indicator.png)
* Quando o status do problema voltar para um status sem espera (que não está configurado na tabela "Pausar SLA ativado"), o campo **Tempo total de espera** será definido no seu problema documento.
![Nível de serviço](/files/total-hold-time.png)
O tempo de resposta e resolução será recalculado adicionando o tempo de espera, reiniciando assim os temporizadores do SLA.


> Observação: o DocType de nível de serviço foi removido na versão 13 e todas as funções são tratadas apenas com o DocType do acordo de nível de serviço.



