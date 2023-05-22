# Repetição automática


O recurso de repetição automática ajuda você a criar certos documentos automaticamente em um determinado período de tempo.


A partir da versão 12, você pode personalizar qualquer formulário para tornar os documentos **repetíveis**.


Por exemplo: supondo que você siga o sistema de despesas diferidas para alguns itens. Requer que você crie o mesmo Lançamento Diário todos os meses para creditar a conta de Despesas Diferidas e debitar a Conta de Despesas. Você pode criar a primeira entrada de diário manualmente para ela e, em seguida, criar uma transação de repetição automática para ela.


Para acessar a Repetição automática, acesse:



> 
> Início > Configurações > Automação > Repetição automática
> 
> 
> 


## 1. Como configurar a repetição automática


### 1.1 Personalize o formulário


1. Vá para: **Página inicial > Personalização > Personalização de formulário > Personalizar formulário**.
2. Selecione o formulário no qual deseja permitir a criação de documentos repetíveis.
3. Marque 'Permitir repetição automática' para permitir a criação de documentos repetíveis para esse formulário. Isso é necessário para que o tipo de documento apareça no campo Documento de referência no tipo de documento de repetição automática.


![Permitir repetição automática](/files/allow-auto-repeat.png)


### 1.2 Configurar a repetição automática


1. Vá para **Página inicial > Configurações > Automação > Repetição automática > Novo**.
2. Selecione o Tipo de Documento de Referência, como Lançamento Diário ou Fatura de Vendas, etc.
3. Selecione o Documento de Referência. Este é o documento individual que você deseja repetir.
4. Defina a data de início e a data de término (opcional).
Se a Data de término não for especificada, serão criados documentos recorrentes, a menos que a Repetição automática esteja desativada.
5. Definir a frequência para criar documentos repetíveis
(Diário, Semanal, Mensal, Trimestral, Semestral, Anual).
6. Salvar.


### 1.3 Configure a repetição automática diretamente do documento


Você também pode configurar um documento para Repetição Automática clicando na opção **Repetir** no **Menu** da Barra de Ferramentas.


**Observação**: se um documento já estiver em Repetição automática, a opção Repetir não estará disponível.


![Repetição em transações](/files/repeat-option.png)


Depois de clicar em Repetir, um prompt para Repetição automática aparecerá. Preencha os detalhes e clique em Salvar.


![Auto Repeat Prompt](/files/auto-repeat-prompt.png)


## 2. Recursos


### 2.1 Enviar na criação


Se o tipo de documento de referência for submissível, você terá uma opção chamada *Enviar na Criação*. Se esta opção estiver marcada, seu documento será enviado na criação.


![Auto Repeat Submit on Creation](/files/submit-on-creation.png)


### 2.2 Notificar por e-mail


Se você deseja notificar determinados contatos sempre que os documentos recorrentes são criados, você pode marcar 'Notificar por e-mail' na seção Notificação de Repetição automática. Isso enviará os documentos recorrentes gerados automaticamente para os endereços de e-mail especificados. Os campos para o mesmo são explicados abaixo:


* **Destinatários**: define os IDs de e-mail dos destinatários para e-mails recorrentes de criação de documentos.
* **Obter contatos**: este botão buscará os contatos vinculados ao documento que está definido em Repetição automática e preencherá o campo Destinatários com os mesmos.
* **Modelo**: você pode escolher um modelo de e-mail para o e-mail. Isso também preencherá os campos Assunto e Mensagem.
* **Assunto**: Assunto do seu e-mail (exemplo: ToDo recorrente criado com sucesso).
* **Mensagem**: Mensagem a ser enviada no Email.
* **Visualizar mensagem**: este botão mostrará uma visualização da mensagem.
* **Formato de impressão**: selecione um formato de impressão para definir a exibição do documento que deve ser enviado por e-mail ao cliente.



> 
> **Observação**: se o documento para o qual você está configurando a Repetição automática puder ser enviado, certifique-se de que "Permitir impressão para rascunho" esteja ativado em [Configurações de impressão](/docs/v13/user/manual /en/setting-up/print/print-settings) para receber o novo documento recorrente no e-mail de notificação de repetição automática. Se isso não estiver ativado, você será notificado sobre a criação do documento recorrente sem o documento.
> 
> 
> 


### 2.3 Repetir em um determinado dia


Se a frequência for definida como Mensal, Trimestral, Semestral ou Anual, ele criará documentos recorrentes nos respectivos meses no mesmo dia da 'Data de início' da Repetição automática. Se você deseja criar documentos recorrentes em outro dia, pode definir uma das seguintes opções:


* **Repetir no dia**: Dia do mês em que o documento recorrente será criado. Por exemplo, se a frequência for Mensal e você inserir 7, ele gerará um documento recorrente no dia 7 do respectivo mês.
* **Repetir no último dia do mês**: esta opção está disponível porque o último dia de cada mês é diferente. Por exemplo, em um ano bissexto, o último dia de fevereiro é 29 e, caso contrário, é 28. Se você marcar esta opção, ele criará documentos recorrentes no último dia dos respectivos meses.


### 2.4 Capacidade de selecionar dias da semana para repetição automática



> 
> Introduzido na versão 13
> 
> 
> 


A repetição automática com frequência semanal permite que você selecione os dias em que deseja que os documentos recorrentes sejam criados.


![Dias da semana de repetição automática](/files/auto-repeat-weekdays.png)


### 2.5 Painel


Você pode ver a programação de Repetição Automática no documento Painel de Repetição Automática. Se você não especificar a data de término, a programação mostrará apenas a próxima data de programação.


![Painel de repetição automática](/files/auto-repeat-dashboard.png)


### 2.6 Frequência de repetição automática na barra lateral


Quando um documento é configurado para Repetição Automática, você pode ver a frequência de Repetição Automática na barra lateral.
Você pode clicar no status para ver o documento de repetição automática vinculado.


![Frequência de repetição automática](/files/auto-repeat-frequency.png)


### 2.7 Desativar a repetição automática


Se você marcar este campo, ele interromperá a criação de documentos recorrentes e desvinculará o documento de repetição automática do documento de referência.

