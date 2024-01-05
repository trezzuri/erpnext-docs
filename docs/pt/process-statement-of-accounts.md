# Processar extrato de contas



> Introduzido na versão 13


**Processar Extrato de Contas é uma ferramenta que ajuda você a enviar Extrato de Contas (Relatório de Razão Geral) e Relatório de Vencimento (Resumo de Contas a Receber) como PDF para seus clientes em massa por e-mail, manualmente ou de forma automatizada periodicamente.**


Esse recurso é útil quando você deseja enviar atualizações por e-mail aos clientes periodicamente sobre suas transações (como faturas de vendas). No anexo PDF enviado por e-mail enviado aos clientes, para cada cliente, haverá detalhes como data de lançamento da fatura, número da fatura de venda, detalhes de débito e crédito, etc., relevantes para sua conta.


O objetivo deste recurso é lembrar a vários clientes que eles têm faturas pendentes não pagas.


  

Para acessar a lista *Processar extrato de contas* você pode pesquisar na barra de navegação ou ir para:


> Home > Contabilidade > Ferramentas > Processar extrato de contas


## 1. Pré-requisitos


1. A ferramenta usa os IDs de e-mail dos clientes para enviar-lhes os relatórios. Ao não encontrar as entradas de e-mail abaixo nos contatos do Cliente, a ferramenta não permitirá que você selecione o respectivo Cliente, portanto, certifique-se de que os seguintes detalhes sejam preenchidos nos documentos do Cliente.


	* E-mail de cobrança do cliente: é obrigatório e pode ser definido em  [Contato do cliente](/docs/pt/CRM/contact#1-how-to-create-a-contact) com a opção "O contato de cobrança" marcada.
	* E-mail principal do cliente: não é obrigatório, a menos que você selecione "Enviar para contato principal" no formulário.
2. Configuração de conta de e-mail com saída ativada. Saiba mais sobre isso [aqui](/docs/pt/setting-up/email/email-account).


## 2. Como criar uma entrada de conta de extrato de processo


1. Vá para a visualização de lista "Processar extrato de conta" pesquisando na barra de navegação e clique em "Novo".
2. Insira um nome para a entrada, para referência futura.
3. Defina os filtros do Razão para os extratos que serão enviados aos clientes.


	* Os filtros "Data inicial" e "Data final" serão ocultados e preenchidos automaticamente de forma dinâmica quando a opção "Ativar e-mail automático" for selecionada.
	* "Projeto" e "Centro de custo" são campos [Table MultiSelect](/docs/pt/customize-erpnext/articles/table-multiselect-field). Isso significa que você pode selecionar vários projetos e centros de custo nos filtros do Razão.![Novo extrato de contas do processo](/files/process-statement-of-accounts.png)
4. Na seção "Clientes", você tem a opção de selecionar clientes na tabela secundária e buscar seus e-mails principais e de cobrança.


	* O campo "Selecionar cliente por" permite selecionar clientes em massa, agrupando-os com base em "Grupo de clientes", "Território", "Parceiro de vendas" e "Vendedor", inserindo a seleção e clicando em "Buscar Clientes".
	* Em documentos de árvore como "Território", "Vendedor" e "Grupo de Clientes" ao selecionar valores de grupo, os clientes que possuem os valores filhos desses campos também serão buscados. Portanto, quando você seleciona "Índia" como território no formulário, todos os clientes com valores de "Território" na Índia na árvore Território serão selecionados.
	* A opção "Enviar para contato principal" enviará o extrato da conta para os IDs de e-mail de contato principal dos clientes, além do e-mail de cobrança.![Customer](/files/psoa-customers.png)
5. Na seção "Preferências de impressão" você pode selecionar duas coisas:


	* Orientação de impressão do arquivo PDF, "Paisagem" ou "Retrato".
	* Se você deseja ver o relatório de vencimento (relatório Resumo de contas a receber), que mostra o valor de vencimento de 30/60/90/120 dias para vouchers (como fatura de vendas), com base em "Data de vencimento" ou "Lançamento Data".![Preferência de impressão](/files/psoa-print.png)
6. A seção "Configurações de e-mail" permite configurar como você deseja que os e-mails sejam enviados. Existem duas subseções nisso:


![Configurações de e-mail](/files/psoa-auto-email.png)


	* Ao selecionar "Ativar e-mail automático", você verá as opções para enviar relatórios periódicos automatizados aos clientes na entrada.
	* Você pode selecionar a "Frequência" com que os e-mails serão enviados após a "Data de Início" aos clientes. As opções disponíveis são semanal, mensal e trimestral.
	* Você também pode selecionar a "Duração do filtro" em meses. Por exemplo, se você definir "Duração do filtro" como '3', obterá os relatórios dos últimos três meses contados a partir da data atual. Aqui, a data atual refere-se à data em que os e-mails foram enviados.
	* Esses e-mails não são enviados imediatamente, mas à meia-noite como um processo em segundo plano.
	* Depois disso você pode selecionar os campos "Assunto", "CC para" e "Corpo" do e-mail. Se você não definir valores para este campo, os valores padrão serão definidos conforme mostrado abaixo.
7. Revise suas configurações e clique em "Salvar".


Agora, espere os e-mails serem enviados se você tiver ativado "Ativar e-mail automático" ou clique em Enviar e-mails para enviá-los imediatamente.


## 3. Recursos


### 3.1 Baixe o PDF consolidado de todos os clientes


Ao criar um cadastro, existe um botão na parte superior chamado "Download" que permite visualizar o PDF do relatório consolidado de todos os clientes. Você pode usar isso para revisão.


### 3.2 Enviar e-mails manualmente


Ao criar uma entrada, existe um botão na parte superior chamado "Enviar Emails" que permite acionar o envio de email manualmente para os clientes. Os e-mails são enfileirados por meio de um trabalho em segundo plano, que você pode acompanhar no tipo de documento "Fila de e-mail" com as referências DocType e Document. Você pode fazer isso mesmo se "Ativar e-mail automático" estiver ativado.


![Enviar e-mail e download](/files/psoa-buttons.png)


### 3.3 Usando valores dinâmicos no assunto e no corpo do email


Você pode usar tags Jinja para inserir valores dinâmicos de:


* O cliente para o qual o e-mail será enviado no objeto "cliente"
* Qualquer campo no documento Processar extrato de conta selecionado no objeto "doc"
* Qualquer método em [`frappe.utils`](https://github.com/frappe/frappe/blob/develop/frappe/utils/__init__.py) sob o objeto "frappe"


Eles podem ser usados ​​conforme mostrado abaixo:


![Template](/files/psoa-template.png)


E-mail resultante:


![Email](/files/psoa-email.png)


Relatório em PDF:


![Report](/files/psoa-report.png)


## 4. Tópicos Relacionados


1. [Configurar uma conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Criando contato do cliente](/docs/pt/CRM/contact#1-how-to-create-a-contact)
3. [Contato](/docs/pt/CRM/contact)



