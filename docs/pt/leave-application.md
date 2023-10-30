# Sair da inscrição



**O Pedido de Licença é um documento formal criado por um funcionário para solicitar licenças por um determinado período de tempo.**

O Frappe HR permite que seus funcionários solicitem licenças via Deixe os Formulários e faça com que sejam aprovados pelos Aprovadores de Licenças.

Para acessar o Formulário de Licença, vá para:


> Página inicial > Recursos Humanos > Licenças > Formulário de Licença
> 
> 

## 1. Pré-requisitos

Antes de criar um pedido de licença, é aconselhável que você tenha os seguintes documentos:

* [Departamento](/docs/pt/human-resources/department)
* [Período de licença](/docs/pt/human-resources/leave-period)
* [Lista de feriados](/docs/pt/human-resources/holiday-list)
* [Tipo de licença](/docs/pt/human-resources/leave-type)
* [Sair Política](/docs/pt/human-resources/leave-policy)
* [Deixar alocação](/docs/pt/human-resources/leave-allocation)

## 2. Como criar um pedido de licença

1. Vá para a lista de pedidos de licença, clique em Novo.
2. Uma tabela de licenças alocadas será exibida mostrando. Com base nas licenças tiradas, as licenças disponíveis são exibidas para cada tipo de licença.

![Leave Application](/files/leave-app.png)
3. Selecione o nome do funcionário e o tipo de licença.
4. Defina a duração da licença usando Data inicial e Data final. Com base nas datas selecionadas, serão exibidos os campos 'Total de dias de licença' e 'Saldo de licença antes da aplicação'.
5. Se a licença aplicada for de meio dia, marque a caixa de seleção 'Meio dia'.
6. Insira o motivo da licença.

![Leave Application](/files/leave-app1.png)
7. Selecione Aprovador de licença.
8. Selecione a data de publicação do pedido de licença.
9. Marque a caixa de seleção 'Seguir por e-mail' para enviar a notificação do pedido de licença ao aprovador de licença.
10. Você também pode vincular o comprovante de salário do funcionário no pedido de licença para registro.

![Aplicativo de licença](/files/leave-app3.png)
11. Clique em Salvar. Depois que o funcionário salva o pedido de licença, o status do pedido de licença muda para 'Aberto' e um e-mail é enviado ao aprovador de licença para aprovação. O modelo de notificação de aprovação de licença pode ser configurado em [Configurações de RH](/docs/pt/human-resources/hr-settings) na seção Configurações de licença.
12. Assim que o aprovador de licença receber o e-mail, ele poderá aprovar, rejeitar ou cancelar o pedido de licença. Feito isso, o aprovador de licença pode enviar o pedido de licença. Após o envio, o status do documento muda de acordo e um e-mail é enviado ao Funcionário notificando-o do mesmo.


> **Observação:** O pedido de licença não pode ser enviado se o salário já tiver sido processado para o período de licença.
> 
> 

O fluxo do processo de pedido de licença está resumido abaixo:

* O funcionário solicita licença por meio do Formulário de Licença.
* O aprovador recebe notificação por e-mail. Para isso, a caixa de seleção "Seguir por e-mail" deve ser marcada.
* Revisões do aprovador Sair da inscrição.
* Aprovador aprova/rejeita/cancela o pedido de licença
* O funcionário recebe a notificação sobre o status do seu pedido de licença

## 3. Recursos

### 3.1 Configuração do aprovador de licença

Um aprovador de licença é um usuário que pode aprovar um pedido de licença de um funcionário. No Frappe HR versão 12, os aprovadores de licenças podem ser definidos em dois níveis:

* **Nível de departamento:** os aprovadores de licenças para cada departamento podem ser configurados no [Departamento](/docs/pt/human-resources/department) mestre. Vários aprovadores de licenças podem ser definidos em um departamento. O primeiro aprovador de licenças na lista será considerado o aprovador de licenças padrão.

![Leave Application-Leave Approvers](/files/leave-app4.png)Quando um Funcionário pertencente a um determinado departamento solicita licença, os Aprovadores de Licença definidos no cadastro de departamento desse Funcionário serão considerados como seus Aprovadores de Licença.
* **Nível do funcionário:** Os aprovadores de licença também podem ser definidos por funcionário no cadastro de funcionários.

![Aplicativo de licença-Aprovadores de licença](/files/employee-level-aprovadors.png)

Se os Aprovadores de licenças forem definidos em nível de funcionário e de departamento, o Aprovador de licenças em nível de funcionário será considerado como o Aprovador de licenças padrão neste caso.

Quando um novo pedido de licença é criado, se o aprovador de licença selecionado não tiver acesso a ele, o documento é compartilhado com o aprovador com permissão de "envio".

**Dica:** se quiser que todos os usuários criem seus próprios pedidos de licença, você pode definir o “ID do funcionário” como regra de correspondência nas configurações de permissão de pedido de licença. Verifique [Configurando permissões](https://docs.erpnext.com/docs/v144/user/manual/en/setting-up/users-and-permissions/user-permissions) para obter mais informações.


> **Notas adicionais:**
> 
> 


> * O período de solicitação de licença deve ocorrer dentro de um único período de alocação de licença. Caso você esteja solicitando licença durante o período de alocação de licença, será necessário criar dois registros de solicitação de licença.
> * O período de solicitação de licença deve estar no último período de alocação de licença.
> * O funcionário não pode solicitar licença nas datas adicionadas no [Sair da lista de bloqueios](/docs/pt/human-resources/leave-block-list).
> 

Para entender como o Frappe HR permite que você configure licenças para funcionários, verifique [Folhas](/docs/pt/human-resources/leave-management-intro/) .

## 3. Tópicos relacionados

1. [Tipo de saída](/docs/pt/human-resources/leave-type)
2. [Período de licença](/docs/pt/human-resources/leave-period)
3. [Política de saída](/docs/pt/human-resources/leave-policy)
4. [Leave Allocation](/docs/pt/human-resources/leave-allocation)
5. [Sair da lista de bloqueios](/docs/pt/human-resources/leave-block-list)



