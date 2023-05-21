# Relatórios automáticos de e-mail


**Relatórios de e-mail automáticos enviam relatórios automaticamente para o documento selecionado.**


Você pode configurar **Auto Email Report** para enviar relatórios em intervalos regulares. Devem ser relatórios salvos de qualquer tipo (Construtor de Relatórios, Script ou Relatório de Consulta).


Você pode encontrar o Auto Email Report em:



>
> Início > Configurações > Relatório automático de e-mail
>
>
>


## 1. Como criar um relatório de e-mail automático


1. Vá para a lista Auto Email Report, clique em New.
2. Selecione o Relatório para o qual deseja gerar e-mails.
3. Selecione o usuário para o qual deseja criar este relatório (as permissões serão aplicadas a este usuário).
4. Defina os endereços de e-mail para os quais deseja que este relatório seja enviado e a frequência do relatório. Os e-mails serão enviados à meia-noite. A data será repetida em caso de frequência semanal/mensal/anual. Por exemplo, se a data selecionada for 7 e a frequência for mensal, o e-mail será enviado no dia 7 de cada mês.


![Com filtros](/files/auto-email-2.png)
5. Salve.


Você pode testar o relatório clicando em "Baixar" ou "Enviar agora". Aqui está um exemplo do e-mail que você receberá para um relatório de razão geral:


![Relatório por e-mail](/files/auto-email-4.png)


## 2. Características


### 2.1 Filtrar Dados


* **Enviar somente se houver dados**: Se habilitada, os e-mails não serão enviados se não houver dados no relatório.
* **Só enviar registros atualizados nas últimas X horas**: Se definido como 24, um e-mail conterá apenas registros atualizados nas últimas 24 horas.
* **No of Rows**: O número de linhas a serem enviadas no e-mail. O máximo é 500.


### 2.2 Filtros de relatórios


Se o seu relatório tiver filtros, você poderá vê-los. Clique na tabela para editá-la:


![Editar filtros](/files/auto-email-3.png)


Por exemplo, se o e-mail estiver no relatório 'Resumo do faturamento do projeto', selecione o projeto. O intervalo de datas aqui é o intervalo de datas do 'Resumo do faturamento do projeto'.


### 2.3 Mensagem


Uma mensagem também pode ser adicionada para ser enviada com o relatório de e-mail. Por exemplo, 'Este é o seu relatório mensal de resumo de cobrança do projeto:'


Você também pode alterar o formato do arquivo no qual o relatório é criado. As opções disponíveis são HTML, XLSX e CSV.


### 2. Tópicos Relacionados


1. [Email Digest](/docs/v13/user/manual/en/setting-up/email/email-digest)
2. [Document Follow](/docs/v13/user/manual/en/setting-up/email/document-follow)