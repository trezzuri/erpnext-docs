# fluxos de trabalho


**Com os fluxos de trabalho, você pode reescrever como um determinado processo/fluxo de trabalho é aprovado no ERPNext.**


Você pode definir vários níveis de aprovação para um ERPNext Workflow. Para permitir que várias pessoas enviem várias solicitações, para aprovações de vários usuários, o ERPNext exige que você preencha as condições do Workflow.
O ERPNext rastreia as múltiplas permissões antes do envio.


Considere um cenário em que vários níveis de aprovação são necessários para uma cotação. Um vendedor (usuário com função de 'Usuário de vendas') criará uma cotação. Em seguida, ele é aprovado ou rejeitado por um lead de vendas (usuário com função de 'Gerente de vendas'). Se aprovado pelo líder de vendas, é posteriormente aprovado ou rejeitado pelo gerente regional (usuário com função de 'Gerente Regional').


Para fazer um Workflow e regras de transição acesse:



>
> Início > Configurações > Fluxo de trabalho
>
>
>


Depois que um fluxo de trabalho é criado, você pode executar ações nele por meio de [Ações de fluxo de trabalho](/docs/v13/user/manual/en/setting-up/workflow-actions).


## 1. Pré-requisitos


Antes de criar um fluxo de trabalho, é recomendável criar primeiro:


* [Ações do fluxo de trabalho](/docs/v13/user/manual/en/setting-up/workflow-actions)
* Estados do fluxo de trabalho como Aprovado, Cancelado, etc.


## 2. Como criar um fluxo de trabalho


1. Vá para a lista Fluxo de trabalho, clique em Novo.
2. Insira um nome para o **Workflow** e selecione o DocType no qual será aplicado.
3. Insira os diferentes estados do fluxo de trabalho. Insira o Status do documento para eles, selecione qual campo atualizar na coluna Atualizar campo, insira o valor para o qual será atualizado em Atualizar valor.


Os Estados do Fluxo de Trabalho podem ter cores diferentes de acordo com o estado. Ex.: Verde para o sucesso. Status do documento: Salvo = 0, Enviado = 1, Cancelado = 2.


![Fluxo de trabalho](/files/workflow.png)
4. Insira as Regras de Transição.


![Regras de transição de fluxo de trabalho](/files/workflow-transition-rules.png)


### 2.2 Pontos a observar ao criar um fluxo de trabalho


* A criação de um fluxo de trabalho no ERPNext basicamente substitui o fluxo de trabalho normal de salvar e enviar. Assim, o documento funcionará com base no seu fluxo de trabalho e não com base no fluxo de trabalho do código predefinido. Portanto, pode não haver botão/opção Enviar se você não o especificou no fluxo de trabalho criado.


Se você não aplicar um fluxo de trabalho a um documento e esse documento puder ser enviado, ele terá o fluxo de trabalho padrão com os estados: Rascunho - Enviado - Cancelado. Se você estiver aplicando um fluxo de trabalho a um documento que pode ser enviado, esses estados padrão devem ser manipulados pelo usuário.
* Um documento não pode ser cancelado a menos que seja enviado.
* Caso deseje dar a opção de cancelamento, deverá escrever um
etapa de transição do fluxo de trabalho que diz a partir do envio que você pode cancelar.
* Se os campos na coluna Atualizar campo não forem atualizados, um novo campo personalizado será criado com o nome definido no campo 'Campo de estado do fluxo de trabalho'.


### 2.3 Outras opções para um Workflow


1. Está ativo: Ao marcar isso, todos os outros fluxos de trabalho para o DocType selecionado tornam-se inativos.
2. Não substituir o status: o status deste fluxo de trabalho não substituirá o status do documento (cotação) na exibição de lista.
3. Enviar alertas de e-mail: os e-mails serão enviados ao usuário com as próximas ações de fluxo de trabalho possíveis.


## 3. Características


### 3.1 Habilitar/Desabilitar Estado de Fluxo de Trabalho Opcional



>
> Introduzido na versão 12
>
>
>


Nos Estados, o estado opcional do Fluxo de Trabalho significa que o estado não pode fazer parte da aprovação final.


Por exemplo. estados como Cancelado ou Rejeitado podem ser opcionais.
![Estado opcional](/files/workflow-optional-state.png)


**Observação:** as ações de fluxo de trabalho não são criadas para estados opcionais.


### 3.2 Condições


Você também pode adicionar uma condição para que a Transição seja aplicável. Por exemplo, neste caso, se o executivo de vendas criar uma cotação com um total geral de US$ 100.000 ou mais, uma função específica deverá aprovar. Para que isso aconteça na transição específica, você pode definir uma propriedade para **Condição**:



```
doc.grand_total <= 100000

```

Aqui, `grand_total` é o nome do campo 'Grand Total' da Cotação. Para ver o nome de um campo, vá para Menu > Personalizar.


Isso pode ser estendido a qualquer propriedade do documento.



>
> Introduzido na versão 13
>
>
>


Na versão 13, você pode usar as funções de data/hora, sessão, obter*valor e obter*lista em suas expressões de condição.


Funções permitidas:


* frappe.db.get\_value
* frappe.db.get\_list
* frappe.session
* frappe.utils.now\_datetime
* frappe.utils.get\_datetime
* frappe.utils.add*até*data
* frappe.utils.now


Exemplos:



```
doc.creation > frappe.utils.add_to_date(frappe.utils.now_datetime(), dias=-5, as_string=True, as_datetime=True)

```

## 4. Exemplo de Processo de Aprovação de Cotação


Quando uma cotação é salva pelo usuário de vendas, o status do documento muda para "Rascunho" e quando clicado em enviar o status muda para 'Aprovação Pendente do Gerente de Vendas':


![Estado do fluxo de trabalho na transação](/files/workflow-status-in-transaction.png)


Quando o Gerente de Vendas faz login, ele pode Aprovar ou Rejeitar. Se aprovado o
o status do documento muda para "Aprovação Pendente do Gerente Regional".


![Opções de ação do fluxo de trabalho](/files/workflow-action-options.png)


Quando o Gerente Regional abre a cotação, ele pode finalmente "Aprovar" ou "Rejeitar".


![Opções de ação do fluxo de trabalho](/files/workflow-action-options-2.png)


## 5. Vídeo








### 6. Tópicos Relacionados


1. [Ações do fluxo de trabalho](/docs/v13/user/manual/en/setting-up/workflow-actions)
2. [Regra de atribuição](/docs/v13/user/manual/en/automation/assignment-rule)