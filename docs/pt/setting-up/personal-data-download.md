# Download de dados pessoais



Como parte da conformidade com o GDPR, o ERPNext oferece download de dados pessoais.


A ferramenta de download de dados pessoais permite que um usuário baixe automaticamente todos os dados pessoais gerados ao usar o ERPNext. Isso inclui dados de identificação pessoal de sua conta de usuário, como: nome de usuário, nome completo, data de nascimento, números de telefone, números de celular, localização, interesses, biografia, assinatura de e-mail, e-mail, contato, endereço, comunicação, etc. e Oportunidades, os detalhes que você salvou, como números de telefone, números de celular, fax, site e nome.


## 1. Como solicitar o download dos dados do usuário


1. Para iniciar o download dos dados, o usuário deve **fazer login** e visitar [nome do host]/request-data (por exemplo, erpnext.com/request-data) no campo URL. 


![Request Data](/files/request-data-webform.png)
2. Após enviar sua solicitação, você receberá uma resposta de sucesso.
![Solicitar dados](/files/download-request-succes.png)
3. Isso enviará um e-mail com um link para download dos dados para o endereço de e-mail associado ao usuário.
![Download de dados por e-mail](/files/download-data-email.png)


O arquivo disponível para download estará no formato JSON.


## 2. Solicitação de download de dados pessoais DocType


A solicitação também fica registrada no DocType “Solicitação de Download de Dados Pessoais”, o link do arquivo que é enviado ao usuário via e-mail também está anexado ao documento. Pesquise Solicitação de download de dados pessoais na barra de pesquisa.


![Doctype de solicitação de download de dados pessoais](/files/personal-data-download-request-doctype.png)


### 3. Tópicos Relacionados


1. [Exclusão de dados pessoais](/docs/pt/setting-up/personal-data-deletion)



