# Repetição automática



O recurso de repetição automática ajuda a criar determinados documentos automaticamente em um determinado período.


A partir da versão 12, você pode personalizar qualquer formulário para tornar os documentos **repetíveis**.


Por exemplo: supondo que você siga o sistema de despesas diferidas para alguns itens. Requer que você crie o mesmo lançamento contábil manual todos os meses para creditar a conta de despesas diferidas e debitar a conta de despesas. Você pode criar o primeiro lançamento contábil manual para ele e, em seguida, criar uma transação de repetição automática para ele.


Para acessar a repetição automática, vá para:
> Início > Configurações > Automação > Repetição automática


## 1. Como configurar a repetição automática


### 1.1 Personalize o formulário


1. Vá para: **Página inicial > Personalização > Personalização de formulário > Personalizar formulário**.
2. Selecione o formato no qual deseja permitir a criação de documentos repetíveis.
3. Marque 'Permitir repetição automática' para permitir a criação de documentos repetíveis para esse formulário. Isso é necessário para que o tipo de documento apareça no campo Documento de referência no tipo de documento Repetição automática.


![Permitir repetição automática](/files/allow-auto-repeat.png)


### 1.2 Configurar a repetição automática


1. Vá para **Página inicial > Configurações > Automação > Repetição automática > Novo**.
2. Selecione o tipo de documento de referência, como lançamento contábil manual ou fatura de vendas, etc.
3. Selecione o Documento de Referência. Este é o documento individual que você deseja repetir.
4. Defina a data de início e a data de término (opcional).
Se a Data de término não for especificada, documentos recorrentes serão criados, a menos que a Repetição automática esteja desativada.
5. Definir a frequência para criação de documentos repetíveis
(Diariamente, Semanalmente, Mensalmente, Trimestralmente, Semestralmente, Anualmente).
6. Salvar.


### 1.3 Configure a repetição automática diretamente do documento


Você também pode definir um documento para repetição automática clicando na opção **Repetir** no **Menu** da barra de ferramentas.


**Observação**: se um documento já estiver em Repetição automática, a opção Repetir não estará disponível.


![Repetir em transações](/files/repeat-option.png)


Depois de clicar em Repetir, um prompt para Repetição Automática será exibido. Preencha os dados e clique em Salvar.


![Prompt de repetição automática](/files/auto-repeat-prompt.png)


## 2. Recursos


### 2.1 Enviar na criação


Se o tipo de documento de referência for submissível, você terá uma opção chamada *Enviar na criação*. Se esta opção estiver marcada, seu documento será enviado na criação.


![Repetir envio automático na criação](/files/submit-on-creation.png)


### 2.2 Notificar por e-mail


Se quiser notificar determinados contatos sempre que os documentos recorrentes forem criados, você pode marcar 'Notificar por e-mail' na seção Notificação de Repetição automática. Isso enviará os documentos recorrentes gerados automaticamente para os endereços de e-mail especificados. Os campos para o mesmo são explicados abaixo:


* **Destinatários**: define os IDs de e-mail dos destinatários para e-mails recorrentes de criação de documentos.
* **Obter Contatos**: Este botão irá buscar os contatos vinculados ao documento que está definido como Repetição Automática e preencher o campo Destinatários com os mesmos.
* **Modelo**: você pode escolher um modelo de email para o email. Isso também preencherá os campos Assunto e Mensagem.
* **Assunto**: Assunto do seu e-mail (exemplo: Tarefa recorrente criada com sucesso).
* **Mensagem**: Mensagem a ser enviada no Email.
* **Visualizar mensagem**: este botão mostrará uma prévia da mensagem.
* **Formato de impressão**: Selecione um formato de impressão para definir a visualização do documento que deve ser enviado por e-mail ao cliente.


> **Observação**: se o documento para o qual você está configurando a repetição automática puder ser enviado, certifique-se de que "Permitir impressão para rascunho" esteja ativado em [Configurações de impressão](/docs/pt/setting-up/print/print-settings) para receber o novo documento recorrente no e-mail de notificação de repetição automática. Se não estiver ativado, você será notificado sobre a criação recorrente de documentos sem o documento.


### 2.3 Repetir em um determinado dia


Se a frequência for definida como Mensal, Trimestral, Semestral ou Anual, serão criados documentos recorrentes nos respectivos meses no mesmo dia da 'Data de Início' da Repetição Automática. Se quiser criar documentos recorrentes em outro dia, você pode definir uma das seguintes opções:


* **Repetir no Dia**: Dia do mês em que o documento recorrente será criado. Por exemplo, se a frequência for Mensal e você inserir 7, será gerado um documento recorrente no dia 7 do respectivo mês.
* **Repetir no último dia do mês**: Esta opção está disponível porque o último dia de cada mês é diferente. Por exemplo, em um ano bissexto, o último dia de fevereiro é 29 e, caso contrário, é 28. Se você marcar esta opção, serão criados documentos recorrentes no último dia dos respectivos meses.


### 2.4 Capacidade de selecionar dias da semana para repetição automática


> Introduzido na versão 13


A repetição automática com frequência semanal permite selecionar os dias em que deseja que os documentos recorrentes sejam criados.


![Repetição automática de dias da semana](/files/auto-repeat-weekdays.png)


### Painel 2.5


Você pode ver a programação da Repetição Automática no documento Painel de Repetição Automática. Se você não especificar a data de término, a programação mostrará apenas a próxima data agendada.


![Painel de repetição automática](/files/auto-repeat-dashboard.png)


### 2.6 Frequência de repetição automática na barra lateral


Quando um documento está definido para Repetição Automática, você pode ver a frequência de Repetição Automática na barra lateral.
Você pode clicar no status para ver o documento vinculado de Repetição automática.


![Frequência de repetição automática](/files/auto-repeat-frequency.png)


### 2.7 Desativar repetição automática


Se você marcar este campo, a criação de documentos recorrentes será interrompida e o documento de repetição automática será desvinculado do documento de referência.



