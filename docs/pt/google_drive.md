# Integração com o Google Drive



ERPNext fornece uma integração com o Google Drive para que todos os usuários possam fazer backup de seus dados no Google Drive.

## Como configurar a integração com o Google Drive

Para permitir que um ERPNext faça upload de backups para o Google Drive, você precisa autorizar o ERPNext a fazer upload de arquivos para o Google Drive. A integração do Google Drive é configurada com as seguintes etapas:

* Criar credenciais OAuth 2.0 por meio de [Configurações do Google](/docs/pt/erpnext_integration/google_settings).
* Na lista do Google Drive, clique em Novo. Digite o nome da pasta de backup para salvar os backups no Google Drive, a frequência do backup e o e-mail da pessoa para quem o e-mail é enviado notificando o status do backup e depois salve-o. Agora clique em **Autorizar acesso ao Drive** para autorizar o ERPNext a enviar arquivos para o Google Drive.
* Uma vez autorizado, você pode salvar seu backup no Google Drive.

## Como usar a integração com o Google Drive


> Observação: se você é usuário do Frappe Cloud, backups locais e externos são criados automaticamente para você: <https://frappecloud.com/docs/sites/backups>
> 
> 

### Fazendo upload do backup para o Google Drive

* Depois que a integração do Google Drive for bem-sucedida, você poderá fazer upload do backup do sistema, bem como de todos os seus arquivos públicos e privados para Google Drive.
* Para fazer backup dos dados no Google Drive, clique em **Fazer backup**. O processo de backup será executado em segundo plano e você será notificado sobre o status do backup. ![](/files/google_drive.gif)
> **Observação**: se o tamanho do backup compactado exceder 1 GB (Gigabyte), o sistema fará upload do último backup disponível para o Google Drive em vez de gerar um novo arquivo de backup.



