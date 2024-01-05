# Fluxos de trabalho



**Com fluxos de trabalho você pode reescrever como um determinado processo/fluxo de trabalho é aprovado no ERPNext.**


Você pode definir vários níveis de aprovação para um fluxo de trabalho ERPNext. Para permitir que múltiplas pessoas enviem múltiplas solicitações, para aprovações de múltiplos usuários, o ERPNext exige que você preencha as condições do Workflow.
O ERPNext rastreia as múltiplas permissões antes do envio.


Considere um cenário em que são necessários vários níveis de aprovação para uma cotação. Um vendedor (usuário com função de 'Usuário de vendas') criará uma cotação. Em seguida, ele é aprovado ou rejeitado por um lead de vendas (usuário com função de 'Gerente de Vendas'). Se aprovado pelo líder de vendas, será aprovado ou rejeitado pelo gerente regional (usuário com função de 'Gerente Regional').


Para criar um fluxo de trabalho e regras de transição, acesse:


> Página inicial > Configurações > Fluxo de trabalho


Depois que um fluxo de trabalho for criado, você poderá executar ações nele por meio de [Ações de fluxo de trabalho](/docs/pt/setting-up/workflow-actions).
## 1. Pré-requisitos


Antes de criar um fluxo de trabalho, é aconselhável criá-los primeiro:


* [Ações de fluxo de trabalho](/docs/pt/setting-up/workflow-actions)
* Estados do fluxo de trabalho como Aprovado, Cancelado, etc.


## 2. Como criar um fluxo de trabalho


1. Vá para a lista Fluxo de trabalho e clique em Novo.
2. Insira um nome para o **fluxo de trabalho** e selecione o DocType ao qual será aplicado.
3. Insira os diferentes estados do fluxo de trabalho. Insira o status do documento para eles, selecione qual campo atualizar na coluna Atualizar campo e insira o valor que será atualizado em Atualizar valor.


Os estados do fluxo de trabalho podem ter cores diferentes de acordo com o estado. Ex.: Verde para o sucesso. Status do documento: Salvo = 0, Enviado = 1, Cancelado = 2.


![Workflow](/files/workflow.png)
4. Insira as regras de transição.


![Regras de transição de fluxo de trabalho](/files/workflow-transition-rules.png)


### 2.2 Coisas a serem observadas ao criar um fluxo de trabalho


* A criação de um fluxo de trabalho no ERPNext essencialmente substitui o fluxo de trabalho normal de Salvar e Enviar. Assim, o documento funcionará com base no seu Workflow e não com base no fluxo de trabalho do código predefinido. Portanto, pode não haver botão/opção Enviar se você não o tiver especificado no fluxo de trabalho criado.


Se você não aplicar um fluxo de trabalho a um documento e esse documento puder ser enviado, ele terá o fluxo de trabalho padrão com estados: Rascunho-Enviado-Cancelado. Se você estiver aplicando um fluxo de trabalho a um documento que pode ser enviado, esses estados padrão deverão ser tratados pelo usuário.
* Um documento não pode ser cancelado a menos que seja enviado.
* Se desejar dar a opção de cancelar, você terá que escrever um
etapa de transição do fluxo de trabalho que diz que você pode cancelar a partir do envio.
* Se os campos na coluna Atualizar campo não forem atualizados, um novo campo personalizado será criado com o nome definido no campo 'Campo de estado do fluxo de trabalho'.


### 2.3 Outras opções para um fluxo de trabalho


1. Está ativo: ao marcar esta opção, todos os outros fluxos de trabalho do DocType selecionado ficam inativos.
2. Não substituir o status: o status deste fluxo de trabalho não substituirá o status do documento (cotação) na visualização de lista.
3. Enviar alertas por e-mail: e-mails serão enviados ao usuário com as próximas ações possíveis do fluxo de trabalho.


## 3. Recursos


### 3.1 Ativar/desativar estado opcional do fluxo de trabalho


> Introduzido na versão 12


Nos estados, o estado opcional do fluxo de trabalho significa que o estado pode não fazer parte da aprovação final.


Ex. estados como Cancelado ou Rejeitado podem ser opcionais.
![Estado opcional](/files/workflow-optional-state.png)


**Observação:** as ações de fluxo de trabalho não são criadas para estados opcionais.


### 3.2 Condições


Você também pode adicionar uma condição para que a Transição seja aplicável. Por exemplo, neste caso, se o executivo de vendas criar uma cotação com total geral de US$ 100.000 ou mais, uma função específica deverá aprovar. Para que isso aconteça na transição específica, você pode definir uma propriedade para **Condição**:



```
doc.grand_total <= 100000

```

Aqui, `grand_total` é o nome do campo 'Total Geral' de Cotação. Para ver o nome de um campo, vá em Menu > Personalizar.


Isso pode ser estendido a qualquer propriedade do documento.


> Introduzido na versão 13


Na versão 13, você pode usar funções de data/hora, sessão, get*valor e get*list em suas expressões de condição.


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
doc.creation> frappe.utils.add_to_date(frappe.utils.now_datetime(), dias=-5, as_string=True, as_datetime=True)

```

## 4. Exemplo de processo de aprovação de cotação


Quando uma cotação é salva pelo usuário de vendas, o status do documento muda para "Rascunho" e ao clicar em enviar o status muda para 'Aprovação pendente pelo gerente de vendas':


![Estado do fluxo de trabalho na transação](/files/workflow-status-in-transaction.png)


Quando o Gerente de Vendas faz login, ele pode Aprovar ou Rejeitar. Se aprovado o
o status do documento muda para "Aprovação pendente pelo gerente regional".


![Opções de ação de fluxo de trabalho](/files/workflow-action-options.png)


Quando o Gerente Regional abre a cotação, ele pode finalmente "Aprová-la" ou "Rejeitá-la".


![Opções de ação de fluxo de trabalho](/files/workflow-action-options-2.png)


## 5. Vídeo








### 6. Tópicos Relacionados


1. [Ações de fluxo de trabalho](/docs/pt/setting-up/workflow-actions)
2. [Regra de atribuição](/docs/pt/automation/assignment-rule)





