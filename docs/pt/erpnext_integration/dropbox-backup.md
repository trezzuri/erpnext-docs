# Configurando backups do Dropbox



Sempre recomendamos aos clientes manter backup de seus dados no ERPNext. O backup do banco de dados é baixado na forma de um arquivo SQL. Se necessário, este arquivo SQL de backup também pode ser restaurado em outra conta ERPNext.

Você pode automatizar o download do backup do banco de dados da sua conta ERPNext para sua conta do Dropbox.


> Observação: Se você é usuário do Frappe Cloud, backups locais e externos são criados automaticamente para você: <https://frappecloud.com/docs/sites/backups>
> 
> 

Para configurar o Dropbox Backup, > Home > Integrações > Configurações do Dropbox

  


#### Etapa 1: Faça login na área de desenvolvedores do Dropbox

[https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps )

  


#### Etapa 2: Crie um novo aplicativo do Dropbox

![Create new](/files/dropbox-open-3.png)  


  


#### Etapa 3: Preencha os detalhes do seu novo aplicativo

![Escolha a API do Dropbox e digite como APP Folder](/files/dropbox-open-1.png) ![Nome do aplicativo de configuração](/files/dropbox-open-2.png)  


![https://support.frappe.io/files/nBdh7wu.png](https://support.frappe.io/files/nBdh7wu.png)  


#### Etapa 4: insira seu URI de redirecionamento de domínio personalizado

`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish` ![Definir redirecionamento URL](/files/dropbox_redirect_uri.png)  


  


#### Etapa 5: Em uma nova janela, abra a página Configurações do Dropbox em sua instalação do ERPnext

  
 

#### Etapa 6: Defina a frequência de backup e e-mail

Defina a frequência de download dos backups do seu site para sua conta do Dropbox. ![definir frequência](/files/setup-backup-frequency.png)  
 

#### Etapa 7: Insira as chaves da janela do seu aplicativo Dropbox

Na página do seu aplicativo Dropbox, insira a chave do aplicativo e o segredo (não oculto) do aplicativo na página de configurações do ERPnext Dropbox.

Como alternativa, você pode inseri-lo manualmente em `sites/{sitename}/site_config.json` como segue,


```
 {
 "db\_name": "demonstração",
 "db\_password": "DZ1Idd55xJ9qvkHvUH",
 "dropbox\_access\_key": "ACCESSKEY",
 "dropbox\_secret\_key": "SECRECTKEY"
}

    
```
  


#### Etapa 8: clique em Salvar antes de continuar

  


#### Etapa 9: Após salvar, clique em "Permitir acesso ao Dropbox"

A página de login do Dropbox será aberta na nova guia. Isso pode exigir que você permita pop-up para sua conta ERPNext.

  


#### Etapa 11: permitir acesso ao Dropbox

 Após o login bem-sucedido, você encontrará uma mensagem de confirmação conforme a seguir. Clique em "Permitir" para permitir que sua conta ERPNext tenha acesso à sua conta Dropbox. ![Allow](/files/dropbox-3.png)  


  


#### Etapa 12: Confirmar se os backups funcionam

Na página ERPnext Dropbox, clique em `Fazer backup agora` e depois vá para a visualização dos arquivos do Dropbox. Você deverá ver uma nova pasta no Dropbox chamada `Apps` e dentro dela sua pasta {New App}. Dentro dele deve haver pastas de backup para arquivos e banco de dados. Portanto, para um aplicativo chamado `erpnext`, a seguir estão os locais das pastas:


```
Database arquivos: /Apps/erpnext/database
Público arquivos: /Apps/erpnext/arquivos
Privados arquivos: /Apps/erpnext/privado/arquivos
  

```
> **Observação**: se o tamanho do backup compactado exceder 1 GB (Gigabyte), o sistema fará upload do último arquivo disponível faça backup no Dropbox em vez de gerar um novo arquivo de backup.



