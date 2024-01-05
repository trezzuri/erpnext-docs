# Fazer upload de backups para o Amazon S3



  



> Observação: se você for usuário do Frappe Cloud, backups locais e externos serão criados automaticamente para você: <https://frappecloud.com/docs/sites/backups>
> 
> 

## Pré-requisitos

* [Conta de e-mail](/docs/pt/setting-up/email/email-account)

Para receber e-mails de backups com falha ou bem-sucedidos, crie primeiro uma **conta de e-mail**.

## Criar bucket S3 e configurar o acesso

1. Crie um novo bucket S3.

Nas configurações do bucket, habilite " Bloqueie todo o acesso público" para manter seus dados privados. Sinta-se à vontade para ativar criptografia, controle de versão ou bloqueio de objeto de acordo com seus requisitos (consulte [Documentação da Amazon](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).
2. Open Identity and Access Management (IAM).
3. Crie uma nova política para o Serviço "S3", permitindo as Ações "ListBucket" e "PutObject".

![Screenshot de "Criar Política" na AWS](/files/s3-backup-policy.png)  


Ou usando o editor JSON:


```
{
    "Versão": "2012-10-17",
    "Declaração": [
        {
            "Sid": "VisualEditor0",
            "Efeito": "Permitir",
            "Ação": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Recurso": [
                "arn:aws:s3:::\*/\*",
                "arn:aws:s3:::SEU BALDE DE ALVO"
            ],
            "Condição": {
                "Endereço IP": {
                    "aws:SourceIp": "IP DO SEU SERVIDOR"
                }
            }
        }
    ]
}
  

```
4. Crie um novo usuário para acesso programático.

<img alt='Screenshot de "Adicionar usuário" class="screenshot" contenteditable="false" draggable="true" src="/files/s3\_backup\_add\_user.png"/>
5. Anexe a política que você criou ao novo usuário.
6. Copie a chave de acesso e o segredo do usuário.

Para excluir automaticamente backups antigos ou movê-los para uma classe de armazenamento mais barata, consulte [gerenciamento do ciclo de vida](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

## Configurar ERPNext

* Open **Configurações de backup do S3**.
* Marque "Ativar backup automático".
* Cole a chave de acesso e segredo da AWS.
* Defina um endereço de e-mail para receber uma notificação quando um backup falhar. Se você também quiser receber um e-mail para backups bem-sucedidos, ative "Enviar e-mail para backup bem-sucedido".
* Especifique o nome do bucket que você criou na etapa 1.
* Escolha com que frequência você deseja fazer e enviar backups. Isso pode variar de mensal a diário. Se você quiser apenas fazer backups manuais, defina a frequência como "Nenhum".

![S3 Backup Settings in ERPNext](/files/s3_backup_settings.png)  




