# Exclusão de dados pessoais


Como parte da conformidade com o GDPR, o ERPNext possui exclusão de dados pessoais.


A ferramenta de exclusão de dados pessoais permite que um usuário exclua sua conta e anonimize todos os dados de identificação pessoal que um usuário gerou ao usar o ERPNext. Ou seja, as informações de identificação pessoal serão randomizadas. Isso inclui dados de identificação pessoal de sua conta de usuário, como: nome de usuário, nome completo, data de nascimento, números de telefone, números de celular, localização, interesses, biografia, assinatura de e-mail, e-mail, contato, endereço, comunicação, etc. Também inclui dados de leads e Oportunidades, os detalhes que você salvou, como números de telefone, números de celular, fax, site e nome.


No entanto, isso exclui os dados que são exigidos por lei para serem mantidos por uma empresa.


## 1. Como solicitar a exclusão da conta


1. Para começar a excluir contas de usuários e dados de identificação pessoal, você precisa visitar [nome do host]/request-for-account-deletion (por exemplo, example.erpnext.com/request-for-account-deletion) no campo URL .


![Pedido de exclusão de conta](/files/Screenshot 2021-12-01 às 8.53.14 PM.png)


2. Insira o e-mail associado à sua conta ERPNext. Depois de enviar sua solicitação, você receberá uma resposta de sucesso.


![Sucesso da solicitação de exclusão](/files/deletion-request-success.png)
3. Isso enviará um e-mail com um link de verificação para excluir dados para o endereço de e-mail associado ao usuário.


![E-mail de verificação](/files/verification-email.png)
4. Assim que o usuário clicar no link de verificação. Uma mensagem de confirmação será exibida.
![Confirmed Verification](/files/confirmed-verification.png)


## 2. Como funciona a exclusão dos dados pessoais do usuário


A solicitação de exclusão de dados é registrada no doctype "Pedido de exclusão de dados pessoais".


![Doctype de solicitação de download de dados pessoais](/files/personal-data-deletion-request-doctype.png)


Este doctype mantém três estados de status para concluir o processo de remoção de dados do usuário.


### 2.1 Verificação pendente


Este status indica que o usuário solicitou a exclusão de dados por meio do formulário da web. No entanto, a verificação desse pedido ainda está pendente. Pesquise Solicitação de exclusão de dados pessoais na barra de pesquisa.


![Pending Verification](/files/pending-verification.png)


### 2.2 Aprovação pendente


Isso indica que o usuário verificou a solicitação por e-mail. Isso habilita a opção de "Excluir dados" para os gerentes do sistema.


![Pending Approval](/files/pending-approval.png)


### 2.3 Excluído


Isso indica que o gerente do sistema clicou no botão "Excluir dados". Isso significa que os dados de identificação pessoal do usuário foram anonimizados.


![Usuário excluído](/files/deleted-user.png)


### 3. Definição de SLA para solicitação de exclusão de dados pessoais.


Você também pode definir um SLA para solicitação de exclusão de dados pessoais por meio das configurações do site. Isso aparecerá na descrição do formulário da web.


* Ir para as configurações do site
* Role até a seção chamada Configurações de exclusão de conta
* No campo **SLA de exclusão de conta (dias)**, defina o número de dias em que a solicitação de exclusão de conta dos usuários será atendida.
* Se você ativar **Mostrar link de exclusão de conta na página Minha conta**, o link do formulário ficará visível para os usuários na página Minha conta do site


![Configurações de exclusão de conta](/files/Screenshot 2021-12-01 às 8.50.39 PM.png)


### 4. Tópicos Relacionados


1. [Download de dados pessoais](/docs/pt/setting-up/personal-data-download)
