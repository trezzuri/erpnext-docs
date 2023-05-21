# Processar Extrato de Contas



>
> Introduzido na versão 13
>
>
>


**O extrato de contas do processo é uma ferramenta que ajuda você a enviar o extrato de contas (relatório do razão geral) e o relatório de vencimento (resumo de contas a receber) como um PDF para seus clientes em massa por e-mail manualmente ou periodicamente.**


Esse recurso é útil quando você deseja enviar atualizações por e-mail aos clientes periodicamente sobre suas transações (como faturas de vendas). No anexo PDF enviado por e-mail enviado aos clientes, para cada cliente, haverá detalhes como data de postagem da fatura, número da fatura de vendas, detalhes de débito e crédito, etc. relevantes para sua conta.


O objetivo desse recurso é lembrar a vários clientes que eles têm faturas pendentes não pagas.


  

Para acessar a lista *Processar Extrato de Contas*, você pode pesquisar na barra de navegação ou ir para:



>
> Home > Contabilidade > Ferramentas > Extrato de Processo de Contas
>
>
>


## 1. Pré-requisitos


1. A ferramenta usa os IDs de e-mail dos clientes para enviar os relatórios. Ao não encontrar as entradas de e-mail abaixo nos contatos do cliente, a ferramenta não permitirá que você selecione o respectivo cliente, portanto, certifique-se de que os seguintes detalhes sejam preenchidos nos documentos do cliente.


* E-mail de cobrança do cliente: obrigatório e pode ser definido no [Contato do cliente](/docs/v13/user/manual/en/CRM/contact#1-how-to-create-a-contact) com "É Contato de cobrança" marcada.
* E-mail principal do cliente: não é obrigatório, a menos que você selecione "Enviar para contato principal" no formulário.
2. Configuração de conta de e-mail com saída ativada. Saiba mais sobre isso [aqui](/docs/v13/user/manual/en/setting-up/email/email-account).


## 2. Como criar uma entrada de conta de extrato de processo


1. Vá para a exibição de lista "Processar Extrato de Conta" pesquisando na barra de navegação e clique em "Novo".
2. Insira um nome para a entrada, para referência futura.
3. Defina os filtros do Razão para os extratos que serão enviados aos clientes.


* Os filtros "Da data" e "Até a data" serão ocultos e preenchidos automaticamente dinamicamente quando a opção "Ativar e-mail automático" for selecionada.
* "Projeto" e "Centro de custo" são campos [Table MultiSelect](/docs/v13/user/manual/en/customize-erpnext/articles/table-multiselect-field). Isso significa que você pode selecionar vários projetos e centros de custo nos filtros do razão geral.![Novo extrato de contas do processo](/files/process-statement-of-accounts.png)
4. Na seção "Clientes", você tem a opção de selecionar clientes na tabela filho e buscar seus e-mails principais e de cobrança.


* O campo "Selecionar cliente por" permite selecionar clientes em massa, agrupando-os com base em "Grupo de clientes", "Território", "Parceiro de vendas" e "Pessoa de vendas", inserindo a seleção e clicando em "Buscar clientes" .
* Em tipos de documento de árvore como "Território", "Pessoa de vendas" e "Grupo de clientes" ao selecionar os valores do grupo, os clientes com os valores filhos desses campos também serão buscados. Portanto, quando você selecionar "Índia" como território no formulário, todos os clientes com valores de "Território" na Índia na árvore Território serão selecionados.
* A opção "Enviar para o contato principal" também enviará o extrato da conta para os IDs de e-mail do contato principal dos clientes, além do e-mail de cobrança.![Cliente](/files/psoa-customers.png)
5. Na seção "Preferências de impressão", você pode selecionar 2 coisas:


* Orientação de impressão do arquivo PDF, "Paisagem" ou "Retrato".
* Se você deseja ver o relatório de vencimento (Relatório de resumo de contas a receber), que mostra o valor de vencimento para 30/60/90/120 dias para vouchers (como fatura de venda), com base em "Data de vencimento" ou "Data de lançamento" .![Preferência de impressão](/files/psoa-print.png)
6. A seção "Configurações de e-mail" permite configurar como deseja que os e-mails sejam enviados. Existem duas subseções neste:


![Configurações de e-mail](/files/psoa-auto-email.png)


* Ao selecionar "Ativar e-mail automático" você verá as opções para enviar relatórios periódicos automatizados para os clientes na entrada.
* Você pode selecionar a "Frequência" em que os e-mails serão enviados após a "Data de início" para os clientes. As opções disponíveis são semanais, mensais e trimestrais.
* Você também pode selecionar a "Duração do filtro" em meses. Por exemplo, se você definir "Duração do filtro" como '3', obterá os relatórios dos últimos três meses contados a partir da data atual. Aqui, a data atual refere-se à data em que os e-mails são enviados.
* Esses e-mails não são enviados imediatamente, mas à meia-noite como um processo em segundo plano.
* Depois disso, você pode selecionar os campos "Assunto", "CC para" e "Corpo" do e-mail. Se você não definir valores para este campo, os valores padrão serão definidos conforme mostrado abaixo.
7. Revise suas configurações e clique em "Salvar".


Agora, aguarde o envio dos e-mails se você ativou "Ativar e-mail automático" ou clique em Enviar e-mails para enviá-los imediatamente.


## 3. Características


### 3.1 Baixar PDF consolidado de todos os clientes


Ao criar uma entrada, existe um botão visto na parte superior chamado "Download" que permite ver o PDF do relatório consolidado de todos os clientes. Você pode usar isso para revisão.


### 3.2 Enviar e-mails manualmente


Ao criar uma entrada, existe um botão visto na parte superior chamado "Enviar e-mails" que permite acionar o envio de e-mail manualmente para os clientes. Os e-mails são enfileirados por meio de um trabalho em segundo plano, que você pode acompanhar no tipo de documento "Email Queue" com as referências DocType e Document. Você pode fazer isso mesmo se "Ativar e-mail automático" estiver ativado.


![Enviar e-mail e baixar](/files/psoa-buttons.png)


### 3.3 Usando valores dinâmicos no assunto e no corpo do e-mail


Você pode usar tags Jinja para inserir valores dinâmicos de:


* O cliente para o qual o e-mail será enviado no objeto "cliente"
* Qualquer campo no documento Extrato de conta do processo selecionado sob o objeto "doc"
* Qualquer método em [`frappe.utils`](https://github.com/frappe/frappe/blob/develop/frappe/utils/__init__.py) sob o objeto "frappe"


Eles podem ser usados ​​como mostrado abaixo:


![Modelo](/files/psoa-template.png)


E-mail resultante:


![Email](/files/psoa-email.png)


PDF do relatório:


![Relatório](/files/psoa-report.png)


## 4. Tópicos Relacionados


1. [Configuração de uma conta de e-mail](/docs/v13/user/manual/en/setting-up/email/email-account)
2. [Criando contato do cliente](/docs/v13/user/manual/en/CRM/contact#1-how-to-create-a-contact)
3. [Contato](/docs/v13/user/manual/en/CRM/contato)