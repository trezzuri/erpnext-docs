# Configurações do sistema



**A configuração do sistema contém configurações para a configuração da conta em todo o sistema.**

Você pode localizar o ERPNext para usar fuso horário, data, número ou formato de moeda específico, e também defina a expiração global da sessão nas Configurações do sistema.

Para abrir as Configurações do sistema, vá para:

> Início > Configurações > Configurações do sistema

![ Configurações do sistema](/private/files/system-settings.png)  
## 1. Seções nas configurações do sistema

### 1.1 Geral

* **País**: Você pode definir o país padrão aqui, ele será obtido ao criar um novo endereços. Se sua empresa tiver várias filiais em países diferentes, escolha o local da sede.
* **Fuso horário**: define a hora automaticamente com base no fuso horário.
* **Idioma**: Define o idioma global para a conta ERPNext. Em seguida, o idioma será alterado em todos os menus, transações, mestres, etc.
* **Desativar compartilhamento de documentos**: Desativa o acesso de compartilhamento para todos os usuários no sistema (exceto Administrador) para garantir que o acesso seja concedido apenas por meio de permissões. Os usuários só poderão ver com quem o documento é compartilhado e não compartilhar o documento em si. Além disso, a atribuição de um documento a um usuário será **bloqueada** se o destinatário tiver acesso ao documento.

### 1.2 Formato de data e número

* **Formato de data**: Formato em que as datas serão exibidas. Por exemplo, dd.mm.aaaa ou mm/dd/aaaa. Isso depende de como as datas são formatadas em sua região.
* **Formato de hora**: formato em que a hora será exibida. Você pode optar por mostrar (`HH:mm:ss`) ou ocultar os segundos definindo a opção como (`HH:mm`) .
* **Formato de Número**: Formato no qual os números serão formatados. Por exemplo, 1.000 ou 1.000,00.
* **Float Precision**: o número de zeros exibidos após a vírgula decimal para quantidades, etc. O intervalo é de 2 a 9 . O padrão é 3.
* **Precisão da moeda**: número de zeros exibidos após o ponto decimal para valores monetários. Se deixado em branco, será baseado no **formato numérico**.
* **Primeiro dia da semana**: pode ser usado para configurar o dia de início da semana. Isso afeta filtros dinâmicos por semana usados ​​em visualizações de lista e relatório, layout de seleção de data e visualização de calendário.
* **Método de arredondamento**: especifica o método de arredondamento a ser usado em todos os lugares. O método de arredondamento padrão é o Arredondamento do Banqueiro, que arredonda 0,5 para o número par mais próximo. "Arredondamento Comercial", que arredonda 0,5 para o próximo número a partir de zero, por ex. 1,5 se torna 2,0 e-1,5 se torna-2,0 quando arredondado.

### 1.3 Backups

No ERPNext você pode fazer backup do banco de dados, bem como de seus arquivos. Os backups de banco de dados são criados automaticamente, enquanto os backups de arquivos precisam ser baixados explicitamente.

Este campo mostra o número de backups após os quais os mais antigos serão excluídos. Por padrão, três backups são salvos em 24 horas. Novos backups são criados automaticamente a cada poucas horas e o backup mais recente substituirá o mais antigo. Para fazer backup dos arquivos, clique no botão Baixar Backup de Arquivos no formulário Baixar Backups.

Manter backups regulares do seu sistema é uma boa prática no caso de algum acidente e você deseja reverter ou apenas para seus registros.

### 1.4 Permissões

Usando permissões, você pode limitar o acesso do usuário a tipos de documentos. A limitação pode ser baseada em campos como Empresa, Território, Filial, etc. Para saber mais sobre permissões de usuário, [clique aqui](/docs/pt/setting-up/users-and-permissions/user-permissions).

Se a caixa de seleção Aplicar permissões restritas ao usuário estiver marcada e a permissão do usuário estiver definida para um DocType para um usuário, então todos os documentos onde o valor do link estiver **em branco**, não serão mostrados para esse usuário.

Isso é feito em: > Página inicial > Usuários e permissões > Permissões > Usuário Permissões

Por exemplo: se você definir Permissões de usuário para Território e definir o valor como Índia. Se a caixa de seleção estiver desmarcada, todas as transações (pedidos de vendas, cotações) com a Índia e **em branco** serão mostradas aos usuários.

Se a caixa de seleção Aplicar permissões restritas ao usuário estiver marcada, os documentos , onde Território está em branco, não será mostrado aos usuários.

### 1.5 Segurança

* **Expiração da sessão**: número de horas ociosas após o qual você será desconectado de uma sessão. Isso ajuda a melhorar a segurança. Por exemplo, se não houver atividade por 6 horas, sua conta será desconectada.
* **Expiração da sessão no celular**: expiração da sessão quando conectado a partir de um telefone celular.
* **Expiração da chave de compartilhamento do documento (em dias)**: número de dias após os quais o "link da web do documento" enviado por e-mail expirará .
* **Permitir apenas uma sessão por usuário**: se você quiser usar um único conjunto de credenciais para vários usuários, marque esta caixa de seleção. O número de sessões simultâneas pode ser alterado em Usuário mestre. As sessões de celular não são contadas aqui.
* **Permitir login usando número de celular**: marcando a caixa de seleção 'Permitir login usando número de celular', você pode fazer login no ERPNext usando um número de celular válido definido em sua conta de usuário.
* **Permitir login usando nome de usuário**: Permitir login do usuário através de seu nome de usuário definido no [Mestre de usuários](/docs/pt/setting-up/users-and-permissions/adding-users).
* **Mostrar erro completo e permitir relato de problemas ao desenvolvedor**: Isso exibirá todo o erro na tela e permitirá relatar problemas. Se você tiver conhecimento técnico nesta área, poderá ter uma ideia melhor do erro lendo a mensagem completa.
* **Remover tags EXIF ​​das imagens enviadas**: Metadados armazenados em arquivos de imagem no formato EXIF ​​podem ser explorados para obter informações confidenciais do usuário. Esta opção permite que os usuários removam esses dados das imagens antes do upload.
* **Permitir links de visualização da Web mais antigos (inseguros)**: a configuração que permite links da Web com sem vencimento. Nota: Links da web mais antigos (gerados na v13) são considerados inseguros porque não expiraram. Recomenda-se manter esta configuração desmarcada.

### 1.6 Senha

* **Forçar usuário a redefinir senha**: Número de dias após os quais uma redefinição de senha é obrigatória. 0 significa sem limite.
* **Ativar política de senha**: ativa um verificador de força de senha para que os usuários tenham que usar senhas fortes para fazer login.

* **Pontuação mínima de senha**: a pontuação do verificador de força da senha


	+ 2 é média
	+ 3 é forte
	+ 4 é muito forteA complexidade é baseada no número de caracteres, letras maiúsculas, caracteres especiais, etc.
* **Duração de expiração do link de redefinição de senha**: Esta configuração é usada para definir a duração após a qual o novo O link de redefinição de senha criado expirou. A expiração padrão do link de redefinição de senha é de 20 minutos. Definir como "0 segundos" desativa a funcionalidade "Expiração do link de redefinição de senha".
* **Limite de geração de link de redefinição de senha**: usando esta configuração, o limite para o número de solicitações de redefinição de senha por hora pode ser definido. O limite padrão é 3. Definir como 0 permitirá solicitações ilimitadas de geração de link de redefinição de senha.

### 1.7 Segurança de força bruta

* **Permitir tentativas de login consecutivas**: logins consecutivos após os quais sua conta será bloqueada por um período específico. Isso ajuda se um invasor tentar fazer login na sua conta.
* **Permitir login após falha**: segundos após os quais uma tentativa de login será permitida após tentativas consecutivas. tentativas malsucedidas.

### 1.8 Autenticação de dois fatores

As configurações para autenticação de dois fatores podem ser definidas aqui.

Ao marcar 'Ativar' Two Factor Auth', as duas opções a seguir serão vistas.

* **Ignorar Two Factor Auth para usuários que fazem login a partir de um endereço IP restrito**: Usuários que fazem login entradas de endereços IP restritos não serão solicitadas para autenticação de dois fatores. Você pode restringir IPs do usuário mestre no campo Restringir IP.
* **Ignorar verificação de endereço IP restrito se autenticação de dois fatores estiver ativada**: se marcado, todos os usuários podem fazer login com autenticação de dois fatores, independentemente de seu IP ser restrito ou não.
* **Método de autenticação de dois fatores**: Selecione o método de autenticação a ser usado-Aplicativo OTP, SMS ou e-mail.
* **Tempo de expiração da página de imagem do código QR**: Tempo de expiração da imagem QRCode se "Aplicativo OTP" for selecionado em o método.
* Nome do emissor OTP da senha de uso único.

![Two Factor Auth](/files/twofactor-settings.png)

### 1.9 E-mail

* **Endereço do rodapé de e-mail**: O nome da organização, endereço e outros detalhes podem ser adicionados aqui. Isso será definido como padrão em todos os e-mails enviados.
* **Desativar rodapé de e-mail padrão**: se marcado, o rodapé de e-mail padrão será desativado para e-mails enviados. .
* **Ocultar rodapé em relatórios de e-mail automático**: se marcado, os rodapés ficarão ocultos em [Relatórios automáticos por e-mail](/docs/pt/setting-up/email/auto-email-reports).
* **Incluir link de visualização da Web no e-mail**: quando você ativa *Anexar impressão de documento* para um novo e-mail, o sistema anexa uma versão em PDF ou HTML do seu documento ao e-mail. Se você também ativar *Incluir link de visualização da Web no e-mail* nas **Configurações do sistema**, um link será adicionado ao e-mail, permitindo que o destinatário visualize o documento on-line como uma página da web. 

![system_settings_email](/files/system_settings_email.png "system_settings_email.png")

### 1.10 Atualizações do sistema

* **Desativar notificação de atualização do sistema**: Esta opção desativa todas as notificações de atualização de versão acionadas pelo aplicativo.

### Arquivo 1.11

* **Tamanho máximo do arquivo (MB)**: Esta opção permite configurar o tamanho máximo para qualquer arquivo enviado. Se não estiver configurado, o tamanho máximo padrão é 25 MB.

### 2. Tópicos relacionados

1. [Configuração da empresa](/docs/pt/setting-up/company-setup)
2. [Padrões globais](/docs/pt/setting-up/settings/global-defaults)
3. [Mostrar ou ocultar módulos](/docs/pt/setting-up/settings/show-hide-modules)




