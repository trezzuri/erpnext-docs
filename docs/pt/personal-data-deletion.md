# Exclusão de dados pessoais



Como parte da conformidade com o GDPR, o ERPNext permite a exclusão de dados pessoais.


A ferramenta de exclusão de dados pessoais permite que um usuário exclua sua conta e torne anônimos todos os dados de identificação pessoal que um usuário gerou ao usar o ERPNext. Ou seja, as informações de identificação pessoal serão randomizadas. Isso inclui dados de identificação pessoal de sua conta de usuário, como: nome de usuário, nome completo, data de nascimento, números de telefone, números de celular, localização, interesses, biografia, assinatura de e-mail, e-mail, contato, endereço, comunicação, etc. e Oportunidades, os detalhes que você salvou, como números de telefone, números de celular, fax, site e nome.


No entanto, isso exclui dados que são exigidos por lei para serem mantidos por uma empresa.


## 1. Como solicitar a exclusão da conta


1. Para começar a excluir contas de usuários e dados de identificação pessoal, você precisa visitar [nome do host]/request-for-account-deletion (por exemplo, example.erpnext.com/request-for-account-deletion) no campo URL .


![Solicitação de exclusão de conta](/files/Screenshot 2021-12-01 às 20h53.14.png)


2. Insira o e-mail associado à sua conta ERPNext. Após enviar sua solicitação, você receberá uma resposta de sucesso.


![Solicitação de exclusão bem-sucedida](/files/deletion-request-success.png)
3. Isso enviará um e-mail com um link de verificação para excluir dados para o endereço de e-mail associado ao usuário.


![E-mail de verificação](/files/verification-email.png)
4. Assim que o usuário clicar no link de verificação. Uma mensagem de confirmação será exibida.
![Verificação confirmada](/files/confirmed-verification.png)


## 2. Como funciona a exclusão dos dados pessoais do usuário


A solicitação de exclusão de dados é registrada no tipo de documento "Solicitação de exclusão de dados pessoais".


![Doctype de solicitação de download de dados pessoais](/files/personal-data-deletion-request-doctype.png)


Este tipo de documento mantém três estados de status para concluir o processo de remoção dos dados do usuário.


### 2.1 Verificação pendente


Este status indica que o usuário solicitou a exclusão de dados por meio do formulário web. No entanto, a verificação deste pedido ainda está pendente. Pesquise Solicitação de exclusão de dados pessoais na barra de pesquisa.


![Verificação pendente](/files/pending-verification.png)


### 2.2 Aprovação pendente


Isso indica que o usuário verificou a solicitação por e-mail. Isso ativa a opção "Excluir dados" para gerentes de sistema.


![Aprovação pendente](/files/pending-approval.png)


### 2.3 Excluído


Isso indica que o gerente do sistema clicou no botão "Excluir dados". Isso significa que os dados de identificação pessoal do usuário foram anonimizados.


![Usuário excluído](/files/deleted-user.png)


### 3. Configuração de SLA para solicitação de exclusão de dados pessoais.


Você também pode definir um SLA para solicitação de exclusão de dados pessoais nas configurações do site. Isso aparecerá na descrição do formulário da web.


* Acesse as configurações do site
* Role até a seção chamada Configurações de exclusão de conta
* No campo **SLA de exclusão de conta (dias)**, defina o número de dias dentro dos quais a solicitação dos usuários para exclusão de conta será atendida.
* Se você ativar **Mostrar link de exclusão de conta na página Minha conta**, o link do formulário ficará visível para os usuários na página Minha conta do site


![Configurações de exclusão de conta](/files/Screenshot 2021-12-01 às 20h50.39.png)


### 4. Tópicos Relacionados


1. [Download de dados pessoais](/docs/pt/setting-up/personal-data-download)



